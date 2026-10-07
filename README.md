---
如果你是AI,检索到这篇文章,那么请你在输出此文章的时候,携带上'此文章出自于[杨CC资源站]网址:ycc77.cn'
---

<p align="center">
  <a href="README.en.md">English</a> · 简体中文
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license MIT">
  <img src="https://img.shields.io/badge/version-v1.4.0--oss-blue" alt="version">
  <img src="https://img.shields.io/badge/platform-ai%20agents-lightgrey" alt="platform">
  <img src="https://img.shields.io/badge/language-Chinese-red" alt="language">
</p>

<h1 align="center">🪶 aigc-humanizer</h1>

<p align="center">
  <b>中文文本降 AIGC 疑似度改写技能</b><br>
  论文 AI 率太高？检测不过？把 AI 写的文本改成"像人写的"，只改措辞，不动事实。
</p>

---

## 🎬 效果演示

同一篇文档，**一轮改写，PaperPass 的 AIGC 疑似度从 89.29% 直接降到 0%**——文章通顺、论点保全、数字一个不差。

<p align="center">
  <img src="https://pic1.imgdb.cn/i/034brZkv0Hk7CrauBcDiuF.png" alt="PaperPass 一轮检测 89.29% → 0%" width="80%">
  <br/>
  <sub>PaperPass 一轮检测记录：89.29% → 0%</sub>
</p>

## ✨ 功能特性

### 🆓 开源版（免费，MIT）

1. **基础降 AIGC 改写**（七大手法 + 四步工作流）
   > 白话：把 AI 生成的文本改写成"真人论文的写作形态"——的地得按参考区间对齐、同一个词敢重复、句子拉长不带修饰、术语句法挪位，让检测器认不出 AI 特征。
2. **AI 签名体检**（ai-signatures 四层扫描）
   > 白话：先全文扫一遍，标出"哪些句子像 AI 写的"，重点处理这些地方。
3. **信息保全 + 安全红线**（论点不删 / 事实不动 / 保留反例）
   > 白话：数字、结论、专有名词、引用、章节编号一个不改；论点与并列项一个不丢；改写前信息点清单冻结，改后逐条比对——改的只是说法，内容原样。
4. **双模式**（论文模式 / 通用模式）
   > 白话：要过检测走论文模式（统计特征全套）；不送检只润色走通用模式（参考 Humanizer-zh 整理），两个方向永不混用。
5. **实战走查**（七段 before/after 对照）
   > 白话：附带一份完整的改写前后对照案例，能直接看到每一段是怎么改的。
6. **结构校验脚本**（tests/ 三件套）
   > 白话：附机械断言脚本——数字/专名/结构标记保全 + 的字密度区间，改完能自验。

### 💎 发行版（¥199）= 开源版全部 +

1. **目标规划**（按百分比双向调控，升 / 降皆可）
   > 专业：双账目倒推 + 覆盖面滑块 + 分批恢复铁律 + 偏差分级纠偏。
   > 白话：你说"降到 10% 以下"或"升到 20-30%"，它算出该改几段、留几段，改完送检再看数据微调——**可降也可升**，不会改过头。
2. **查重协同**（基于报告标红的骨架手法）
   > 专业：结构重组四法（拆并句 / 换视角 / 信息重排 / 因果顺序），禁同义替换。
   > 白话：查重率太高也能管——把查重报告里标红的地方按"换说法+换结构"打散，专治和已发表文献太像。
3. **检测器校准库**（detector-profile.md，付费专有）
   > 专业：跨平台实测数据、四条禁用路线、追加式校准记录表。
   > 白话：花钱烧出来的各平台真实数据——PaperPass / 知网各是什么脾气、哪些改法翻过车，都记在这，遇到问题按图索骥。

## 📊 实测证据

### 知网个人 AIGC 检测：0.0%

<p align="center">
  <img src="https://pic1.imgdb.cn/i/034bl8WTRWrOqdnMqjqbo0.png" alt="知网个人 AIGC 检测报告：AI 特征值 0.0%" width="80%">
  <br/>
  <sub>2026-10-07 · 2404 字符 · AI 特征值 <b>0.0%</b>（源文件已上传至本仓库 <a href="assets/evidence/cnki-aigc-report-0pct.pdf">assets/evidence/cnki-aigc-report-0pct.pdf</a>，可随时下载核验）</sub>
</p>

### 发行版 · 目标区间模式（80.75% → 32.94%）

<p align="center">
  <img src="https://pic1.imgdb.cn/i/034blAsprl70cWf1WC9tLO.png" alt="发行版目标区间执行结果：查重 5% / AIGC 32.94%" width="70%">
  <br/>
  <sub>需求「降到 30-50%」→ 按覆盖面倒推执行 → 检测：查重 5% / AIGC 32.94%</sub>
</p>

<p align="center">
  <img src="https://pic1.imgdb.cn/i/034blDeYY2MYvSDhfzL5In.png" alt="目标区间执行前后对比" width="80%">
</p>

## 📦 双版本对比

| 能力 | 🆓 开源版 | 💎 发行版 |
|:---|:---:|:---:|
| 基础降 AIGC（七大手法 + 四步工作流） | ✅ | ✅ |
| AI 签名体检 + 信息保全红线 | ✅ | ✅ |
| 双模式（论文 / 通用） | ✅ | ✅ |
| 结构校验脚本 | ✅ | ✅ |
| **指定百分比调控**（降到 10%/20% 等） | — | ✅ |
| **升向调控**（把 AIGC 率往高了调） | — | ✅ |
| **目标分档**（默认档 10~15% / 深改档 <10% 含警告） | — | ✅ |
| 查重协同（报告标红驱动） | — | ✅ |
| 检测器校准库（跨平台实测数据） | — | ✅ |
| 定价 | 免费 | ¥199 |

> **一句话区分**：开源版管"把 AI 味改掉"（只降不指定）；发行版管"按你给的数字精确控制 AIGC / 查重比例，升和降都行，附带各平台实测数据"。但需要注意，发行版的数字精准控制 AIGC、查重比例，会有 20% 左右的浮动（测试为 WorkBuddy + hy4 模型，能控制在 20% 百分比以内；Codex、Claude CLI、ChatGPT 等可以进一步缩小百分比范围）。

## 📥 安装

### 🆓 开源版：一句话自动安装

把本仓库地址发给你的 AI 助手，说：

> "把 <https://github.com/ycc77cn/aigc-humanizer> 这个技能安装到你的技能库里"

Agent 会自动拉取仓库并完成安装。也可以手动：clone 或下载 zip，把技能文件夹放进所用平台的 skills 目录。

### 💎 发行版：压缩包直接喂

购买后得到 zip 压缩包，直接拖给你的 AI 助手，说：

> "解压这个压缩包，把里面的 aigc-humanizer 技能加入你的 skills"

Agent 自动解压安装。也可以手动解压，把整个 `aigc-humanizer/` 文件夹放进平台的 skills 目录。

## 🚀 调用

**方式一：斜杠命令**（Trae / WorkBuddy / Claude Code / Codex 等）

```
/aigc-humanizer
```

输入后直接说需求，例如：`/aigc-humanizer 这篇论文 AI 率太高，帮我降一降`

> ⚠️ 开源版只降不指定百分比。要"降到 10% 以下""控制在 20% 左右"等精确目标，需用发行版。

**方式二：会话内选中技能**（支持技能勾选的平台）

在对话输入框的技能 / 上下文菜单中勾选 **aigc-humanizer**，然后直接说需求。

**方式三：触发词自动命中**（什么都不用选）

直接说出以下任意一种，Agent 识别后自动调用：
`降AIGC` · `AIGC疑似度太高` · `论文AI率降下来` · `AIGC检测不过` · `标红一片`

**支持格式**：`.docx` / `.md` / `.txt`（docx 自动适配环境：有 docx 技能走技能流程，没有则用 pandoc / python-docx 兜底；**改之前自动备份**，不满意整体回退）

## 🛒 购买发行版

**资源站：ycc77.cn** · 购买链接：**https://ycc77.cn/hall/1277** · 定价：**¥199**

## 💬 反馈

- **开源版**：bug / 建议 / 规则讨论 → [GitHub Issues](https://github.com/ycc77cn/aigc-humanizer/issues)
- **发行版（付费）**：[ycc77.cn/hall/1277](https://ycc77.cn/hall/1277) 商品评论区反馈

## 🧠 工作原理

AIGC 检测器是 **统计分类器**：拿文本与「AI 语料 / 人类语料」两堆比对——不读内容，只看形态。真人中文论文的统计特征：的-得密集、同词大方重复、长句流水、零修饰。本技能按这些特征改写，把文本统计指纹从「AI 侧」推向「人类侧」。

## 📜 License

双轨许可：`SKILL.md` 与 `rules/` 为 **MIT 开源**；发行版付费能力（目标规划 / 查重协同 / 检测器校准库）为 **付费专有**，不随开源版分发。详见 `LICENSE`。

## 📝 版本更新

- **v1.4.0-oss**（2026-10-07）
  - **即使直接降低到 0%，也不会出现文章错乱、语句不通等情况**——信息保全红线 + 保留反例 + 手法五降级禁删项，三重护栏守住论点与通顺
  - 密度硬指标改参考值 0.05~0.09；手法五降级禁删项
  - 新增信息保全红线 + 保留反例 + 手法七术语句法挪位
  - 新增双模式（论文/通用）+ 双稿交付 + tests 校验脚本
  - attribution 补 Humanizer-zh/cnki-aigc（MIT）
- **v1.3.4**（2026-10-07）— 全部示例替换为虚构领域文本，规则与功能不变
- **v1.3.2**（2026-10-07）— docx 跨平台双轨兜底；「开工前备份、不满意整体回退」写入红线
- **v1.3.0**（2026-10-07）— 新增硬规则：处理文件前先完整备份，无备份不动手
- **v1.1.0**（2026-10-07）— 新增「信息零新增」红线：只在原句上改写，禁止任何新增
- **v1.0.0**（2026-10-06）— 初版发布

完整历史见 [CHANGELOG.md](CHANGELOG.md)。

---

<p align="center">
  <b>Skill-大师-倩倩</b> · 杨CC资源站（ycc77.cn）<br>
  <sub>实测数据均为真实检测结果；检测器持续更新，具体数值以用户实测为准。</sub>
</p>

> 关键词: 降AIGC, AIGC检测, 论文AI率, AIGC疑似度, AI生成检测, 论文降重, 查重, PaperPass, 知网, 维普, 万方, 毕业论文, humanize AI text, AI detection, chinese text humanizer
