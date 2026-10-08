#!/usr/bin/env python3
# coding: utf-8
"""
AIGC 特征多维度扫描器 — 15 维度（自写，纯标准库，零第三方包）
部分维度设计参考 xiaofenggan01/aigc-reduce (MIT) 的 aigc_scan.py 思路，代码原创。

维度清单：
  1. 模板句式密度        8. 口语化/网络用语密度（语体门禁预警）
  2. 被动语态比例        9. 破折号密度（每段 ≤1 个）
  3. 突发性 CV（句长）  10. 的字密度（自然落点监控，非硬指标）
  4. 段落对称性          11. 三层名词嵌套（X的Y的Z）
  5. 嵌套编号            12. 同义词循环检测（同一对象 3+ 称呼）
  6. 冒号并列            13. "是…的"八股密度
  7. 标点规律性          14. 信息点计数（数字/专名/结构标记前后比对）
                        15. 改写深度估算（句级相似度，需 --original 参数）

用法: python check_patterns.py <file.txt> [--json] [--original 原文.txt]
"""

import re
import sys
import json
import argparse
from collections import Counter
from pathlib import Path

# ─── 模板句式库 ───
TEMPLATE_PATTERNS = [
    r'^(综上所述[，,])',
    r'^(基于.{2,10}(分析|研究|探讨))',
    r'^(通过.{2,15}(验证|实验|研究|测定))',
    r'^(随着.{2,20}(发展|进步|深入))',
    r'^(近年来[，,])',
    r'^(在.{2,20}(背景下|条件下|过程中))',
    r'^(本研究[旨在对通过])',
    r'^(目前[，,])',
    r'^(当前[，,])',
    r'^(因此[，,])',
    r'^(由此可见[，,])',
    r'^(总而言之[，,])',
    r'(此外[，,])',
    r'(另外[，,])',
    r'(与此同时[，,])',
    r'(值得注意的是[，,])',
    r'(需要指出的是[，,])',
    r'(据统计[，,])',
    r'(相关研究表明[，,])',
    r'(一般认为[，,])',
    r'(具有重要的.{2,10}(意义|价值|作用))',
    r'(具有广阔的应用前景)',
    r'(为.{2,20}(提供了|奠定了).{2,10}(基础|依据|参考))',
    r'(不是[^\n。！？!?.]{1,40}而是)',
    r'(但至少)',
    r'(不代表)',
]

PASSIVE_MARKERS = [
    r'被.{1,15}(测定|检测|验证|确认|证明|发现|计算)',
    r'由.{1,15}(进行|完成|测定|检测|计算)',
    r'经.{1,15}(测定|检测|计算|分析)',
    r'通过.{1,15}(测定|检测|验证|实验|计算)',
]

NESTED_NUM_RE = re.compile(r'[（(](\d+)[）)]')
COLON_LIST_RE = re.compile(r'[：:]\s*.+?[；;]\s*.+?[；;]')

EM_DASH = '\u2014\u2014'
DE = '\u7684'

COLLOQUIAL_TERMS = [
    'yyds', '绝绝子', '破防', 'emo', '拿捏', '整活', '有梗', '无语',
    '离谱', '逆天', '炸裂', '社死', '摆烂', '搞定', '踩坑', '翻车',
    '封神', '硬核', '谁懂啊', '手感',
    '气死', '乐死', '笑死', '烦躁', '郁闷',
    '说实话', '坦白讲', '老实说', '不瞒你说', '说白了', '讲真', '反正',
    '大概齐', '差不多就是', '这事的难度', '这事儿', '不得不考虑的一环',
    '一点一点磨出来', '撑起来', '比表面看起来大得多', '说到底', '归根结底就是',
]

# AI 高频词（用于同义词循环检测的对照——同一对象被叫多个名字）
SYNONYM_GROUPS = [
    ['凝胶', '胶体', '水凝胶', '复合物'],
    ['显著', '明显', '大幅', '可观地'],
    ['提升', '提高', '增强', '改善'],
    ['促进', '推动', '驱动', '有利于'],
    ['揭示', '显示', '指向', '表明'],
]


def split_paragraphs(text):
    paras = re.split(r'\n\s*\n', text.strip())
    return [p.strip() for p in paras if p.strip()]


def split_sentences(text):
    sents = re.split(r'[。！？!?\n]|(?<!\d)\.|\.(?!\d)', text)
    return [s.strip() for s in sents if s.strip() and len(s.strip()) > 5]


def count_template_matches(text):
    hits = []
    for pat in TEMPLATE_PATTERNS:
        ms = re.findall(pat, text, re.MULTILINE)
        if ms:
            for m in (ms if isinstance(ms[0], str) else [x[0] if isinstance(x, tuple) else x for x in ms]):
                hits.append(m)
    return {'count': len(hits), 'density_per_1k': round(len(hits) / max(len(text), 1) * 1000, 2),
            'sample': hits[:10], 'risk': '偏高' if len(hits) > 3 else '正常'}


def count_passive_markers(text):
    total = sum(len(re.findall(p, text)) for p in PASSIVE_MARKERS)
    sc = max(len(split_sentences(text)), 1)
    return {'count': total, 'per_sentence': round(total / sc, 3),
            'risk': '仅参考'}


def analyze_burstiness(paragraphs):
    lengths = []
    for p in paragraphs:
        for s in split_sentences(p):
            lengths.append(len(s))
    if len(lengths) < 3:
        return {'cv': 0, 'risk': '数据不足'}
    avg = sum(lengths) / len(lengths)
    var = sum((l - avg) ** 2 for l in lengths) / len(lengths)
    cv = var ** 0.5 / max(avg, 1)
    return {'avg_len': round(avg, 1), 'cv': round(cv, 3),
            'risk': '本技能以长句为主，CV偏低属正常' if cv < 0.35 else '正常'}


def analyze_para_symmetry(paragraphs):
    lens = [len(p) for p in paragraphs]
    if len(lens) < 3:
        return {'risk': '段落数不足'}
    runs = 0
    cur = 0
    for i in range(1, len(lens)):
        dev = abs(lens[i] - lens[i-1]) / max(lens[i-1], 1)
        if dev < 0.2:
            cur += 1
        else:
            if cur >= 2:
                runs += 1
            cur = 0
    if cur >= 2:
        runs += 1
    return {'symmetrical_runs': runs, 'risk': f'发现{runs}处对称段组' if runs else '未发现'}


def count_nested_numbers(text):
    ms = NESTED_NUM_RE.findall(text)
    return {'count': len(ms), 'risk': '正常' if len(ms) <= 3 else f'检测到{len(ms)}处'}


def count_colon_lists(text):
    ms = COLON_LIST_RE.findall(text)
    return {'count': len(ms), 'risk': '正常' if len(ms) <= 1 else f'检测到{len(ms)}处'}


def analyze_punctuation(text):
    comma = text.count('，') + text.count(',')
    sc = max(len(split_sentences(text)), 1)
    cps = round(comma / sc, 2)
    return {'commas_per_sentence': cps, 'risk': '偏高' if cps > 2.5 else '正常'}


def count_colloquial(text):
    hits = []
    for t in COLLOQUIAL_TERMS:
        c = text.count(t)
        if c:
            hits.extend([t] * c)
    return {'count': len(hits), 'terms': sorted(set(hits)),
            'risk': f'⚠️ 语体门禁：{len(hits)}处口语化' if hits else '正常'}


def analyze_dash_density(paragraphs):
    over = 0
    total = 0
    for p in paragraphs:
        n = p.count(EM_DASH)
        total += n
        if n >= 2:
            over += 1
    return {'total': total, 'over_limit': over,
            'risk': f'⚠️ {over}段破折号超标' if over else '正常'}


def analyze_de_density(text):
    clean = re.sub(r'\s', '', text)
    de = clean.count(DE)
    dens = round(de / max(len(clean), 1), 4)
    return {'de_count': de, 'density': dens,
            'note': '自然落点 0.03~0.09 均属正常；>0.07 且拗口时检查是否堆砌',
            'risk': '监控值'}


def count_nested_nouns(text):
    nest = re.findall(r'[\u4e00-\u9fa5]{1,3}\u7684[\u4e00-\u9fa5]{1,4}\u7684[\u4e00-\u9fa5]{1,4}', text)
    return {'count': len(nest), 'sample': sorted(set(nest))[:5],
            'risk': f'⚠️ {len(nest)}处三层嵌套，拆一层' if len(nest) > 0 else '正常'}


def detect_synonym_cycling(text):
    hits = []
    for group in SYNONYM_GROUPS:
        found = [w for w in group if w in text]
        if len(found) >= 3:
            hits.append(found)
    return {'groups': hits, 'risk': f'⚠️ {len(hits)}组同义词循环' if hits else '正常'}


def count_shi_de_pattern(text):
    pat = re.compile(r'\u662f[^\u3002\uff01\uff1f\n]{0,30}\u7684')
    hits = pat.findall(text)
    sc = max(len(split_sentences(text)), 1)
    return {'count': len(hits), 'per_sentence': round(len(hits) / sc, 2),
            'risk': f'⚠️ 偏高（{len(hits)}/{sc}句）' if len(hits) / sc > 0.5 else '正常'}


def count_info_points(text):
    numbers = re.findall(r'\d+\.?\d*[%％]?', text)
    markers = re.findall(r'[（(]\d+[）)]', text)
    refs = re.findall(r'\[\d+\]', text)
    return {'numbers': len(numbers), 'structure_markers': len(markers),
            'references': len(refs), 'note': '前后比对用，改写后数字/标记数应一致'}


import difflib


def is_anchor_sentence(s):
    """锚段豁免判定：章节标题与参考文献条目本就不该改写，
    计入改写深度分母会虚拉低深度重写率（v1.4.8.1 修复）。"""
    t = s.strip()
    if not t:
        return True
    if len(t) <= 14 and not re.search(r'[，。；]', t):
        return True  # 短行无标点：标题类
    if re.match(r'^[一二三四五六七八九十百]+[、．.]', t):
        return True  # 中文章节标题："一、""二、"
    if re.match(r'^\d+(\.\d+)*[、\s]', t):
        return True  # 数字编号标题："3.1 ""12、"
    if re.match(r'^\[\d+\]', t):
        return True  # 参考文献条目："[1] …"
    return False


def estimate_rewrite_depth(text, original_text):
    """第15维：改写深度估算（v1.4.8.1 改写段口径）。

    三类句子，分三层处理：
    - 格式锚：章节标题/参考文献（is_anchor_sentence）——本就不在改写范围
    - 业务锚段：目标规划模式下刻意逐字保留的 AI 原句——自动识别为
      与原文最优相似度 >0.97 的句子（规划保留=不改，不该拖累深度指标）
    - 改写段：真正应该被深度重写的句子
      深度重写率（预警口径）= 深度句 ÷ 改写段句数，目标 80%+

    预警只挂"改写段深度率"；全文口径仅作参考输出。
    若无锚段规划（全文深改场景），与原文一致的句子同样被豁免——
    此时改写段口径自动退化为"应改未改句的深度率"，仍优于全文口径。
    """
    orig_sents = split_sentences(original_text)
    new_sents = split_sentences(text)
    if not orig_sents or not new_sents:
        return {'risk': '数据不足', 'note': '需 --original 参数提供原文'}
    best = []
    format_anchors = 0
    for ns in new_sents:
        if is_anchor_sentence(ns):
            format_anchors += 1
            continue
        m = 0
        for os_ in orig_sents:
            r = difflib.SequenceMatcher(None, os_, ns).ratio()
            if r > m:
                m = r
            if m > 0.97:
                break
        best.append((m, ns))
    if not best:
        return {'risk': '数据不足',
                'note': '全部句子命中格式锚豁免（标题/参考文献），无可评估正文句'}
    # 业务锚段：与原文逐字一致的句子（>0.97）= 规划保留的 AI 原句
    retained = [b for b in best if b[0] > 0.97]
    writable = [b for b in best if b[0] <= 0.97]
    light = [b for b in writable if 0.8 < b[0] <= 0.97]
    mid = [b for b in writable if 0.5 < b[0] <= 0.8]
    deep = [b for b in writable if b[0] <= 0.5]
    w_total = len(writable)
    deep_rate = round(len(deep) / max(w_total, 1), 3)
    avg_sim = round(sum(b[0] for b in writable) / max(w_total, 1), 3)
    # 全文参考口径（含锚段）
    f_total = len(best)
    full_deep_rate = round(len(deep) / max(f_total, 1), 3)
    return {
        'total_sentences': len(new_sents),
        'format_anchors': format_anchors,
        'retained_anchors': len(retained),
        'writable_sentences': w_total,
        'light_edit': len(light), 'mid_edit': len(mid), 'deep_rewrite': len(deep),
        'deep_rate': deep_rate, 'avg_similarity': avg_sim,
        'full_text_rate': full_deep_rate,
        'risk': f'⚠️ 改写段深度率 {deep_rate:.0%}（目标 80%+）' if deep_rate < 0.8
                else f'达标（改写段深度率 {deep_rate:.0%}）',
        'note': '改写段=总句-格式锚(标题/参考文献)-业务锚段(与原文逐字一致=规划保留)；'
                '预警只看改写段深度率；full_text_rate 为含锚段的全文参考口径；'
                '无锚段规划时（全文深改场景），retained_anchors 应接近 0——'
                '大于 0 意味着存在漏改句，不是锚段'
    }


def scan(text, original_text=None):
    paras = split_paragraphs(text)
    result = {
        'summary': {'chars': len(text), 'paragraphs': len(paras), 'sentences': len(split_sentences(text))},
        '1_template': count_template_matches(text),
        '2_passive': count_passive_markers(text),
        '3_burstiness': analyze_burstiness(paras),
        '4_para_symmetry': analyze_para_symmetry(paras),
        '5_nested_num': count_nested_numbers(text),
        '6_colon_list': count_colon_lists(text),
        '7_punctuation': analyze_punctuation(text),
        '8_colloquial': count_colloquial(text),
        '9_dash': analyze_dash_density(paras),
        '10_de_density': analyze_de_density(text),
        '11_nested_nouns': count_nested_nouns(text),
        '12_synonym_cycle': detect_synonym_cycling(text),
        '13_shi_de': count_shi_de_pattern(text),
        '14_info_points': count_info_points(text),
    }
    if original_text:
        result['15_rewrite_depth'] = estimate_rewrite_depth(text, original_text)
    else:
        result['15_rewrite_depth'] = {'risk': '跳过', 'note': '需 --original 参数提供原文'}
    return result


def print_report(r):
    s = r['summary']
    print(f"\n{'=' * 60}")
    print(f"  AIGC 特征 15 维度扫描报告")
    print(f"{'=' * 60}")
    print(f"  文本: {s['chars']} 字符, {s['paragraphs']} 段, {s['sentences']} 句")

    labels = [
        ('1_template', '模板句式', 'risk'),
        ('2_passive', '被动语态', 'risk'),
        ('3_burstiness', '突发性CV', 'risk'),
        ('4_para_symmetry', '段落对称', 'risk'),
        ('5_nested_num', '嵌套编号', 'risk'),
        ('6_colon_list', '冒号并列', 'risk'),
        ('7_punctuation', '标点规律', 'risk'),
        ('8_colloquial', '口语化预警', 'risk'),
        ('9_dash', '破折号密度', 'risk'),
        ('10_de_density', '的字密度', 'note'),
        ('11_nested_nouns', '三层嵌套', 'risk'),
        ('12_synonym_cycle', '同义词循环', 'risk'),
        ('13_shi_de', '是…的八股', 'risk'),
        ('14_info_points', '信息点计数', 'note'),
        ('15_rewrite_depth', '改写深度', 'risk'),
    ]

    warnings = 0
    for key, name, val_key in labels:
        d = r[key]
        v = d.get(val_key, d.get('risk', ''))
        if '⚠️' in str(v):
            warnings += 1
        extra = ''
        if key == '10_de_density':
            extra = f"  de={d['de_count']} dens={d['density']}"
        elif key == '13_shi_de':
            extra = f"  count={d['count']} per_sent={d['per_sentence']}"
        elif key == '11_nested_nouns' and d.get('sample'):
            extra = f"  {d['sample'][:3]}"
        elif key == '8_colloquial' and d.get('terms'):
            extra = f"  {d['terms'][:5]}"
        elif key == '15_rewrite_depth':
            if d.get('deep_rate') is not None:
                extra = (f"  深度重写{d.get('deep_rewrite', 0)}/{d.get('writable_sentences', 0)}句"
                         f"（锚段豁免{d.get('format_anchors', 0)}+{d.get('retained_anchors', 0)}，"
                         f"全文口径{d.get('full_text_rate', 0):.0%}）")
            elif d.get('note'):
                extra = f"  {d['note']}"
        print(f"  [{key.split('_')[0]:>2}] {name:10s}  {v}{extra}")

    print(f"\n  综合预警: {warnings} 项触发")
    print(f"  {'=' * 60}")


def main():
    p = argparse.ArgumentParser(description='AIGC 15维扫描')
    p.add_argument('file', help='待扫描的文本文件（改写后）')
    p.add_argument('--original', help='原文文本文件（用于第15维改写深度估算）', default=None)
    p.add_argument('--json', action='store_true')
    a = p.parse_args()
    text = Path(a.file).read_text(encoding='utf-8')
    orig_text = Path(a.original).read_text(encoding='utf-8') if a.original else None
    r = scan(text, orig_text)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print_report(r)


if __name__ == '__main__':
    main()
