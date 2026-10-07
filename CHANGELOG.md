# CHANGELOG

## v1.3.4 - 2026-10-07

- rules 三文件示例全面脱敏：rewrite-rules / ai-signatures / safety-lines 中
  源自真实项目文本的示例句，全部替换为虚构养老领域示例（与 worked-example
  配套统一）；手法规则与教学结构不变

## v1.3.3 - 2026-10-07

- worked-example.md 全面脱敏：实战走查示例从真实项目文本替换为
  虚构领域文本（智慧养老平台），七段对照结构、手法标注、核对示例
  全部保留；SKILL.md 示例章"实测通过版"字样同步改为"按规则改写"

## v1.3.2 - 2026-10-07

- docx 处理双轨兜底：SKILL.md 4 处 docx 引用全部改为
  "运行环境提供 docx 技能时按其流程执行、无该技能环境用 pandoc /
  python-docx 通用工具兜底"——消除跨平台使用时的悬空引用，
  不绑定任何平台名称，开工前备份、格式保留、水印规则不变
- 修正备份规则的悬空表述：开源版无升向功能，SKILL.md 与
  rules/safety-lines.md 的"升比例 / 恢复原文依赖备份"统一改为
  "用户不满意或改写有问题，整体回退到备份"

## v1.3.1 - 2026-10-07

- 措辞中性化：description 与场景词删除"骗过检测"表述，
  与技能定位对齐，降低上架合规风险

## v1.3.0 - 2026-10-07

- 新增"开工前先备份"硬规则：处理用户文件之前，原文件必须先做完整备份，
  无备份不动手——同步写进 Step 1 工作流、SKILL.md 红线、
  rules/safety-lines.md 交付红线三处

## v1.2.0 - 2026-10-07

- 技能更名：paper-aigc-reducer → aigc-humanizer
  - 原名 paper 限死论文场景、reducer 限死"降"方向
  - 新名 aigc-humanizer：方向中性、场景不限（论文/报告/知乎/公众号通吃）

## v1.1.0 - 2026-10-07

- 新增"信息零新增"红线（rules/safety-lines.md）：只在原有句子上改写，
  禁止任何形式的新增内容（新事实 / 例子 / 解读句 / 过渡句 / 扩写）

## v1.0.0 - 2026-10-06

初版发布。

- 核心改写规则库（六大手法 + 两条全局法则 + 句式模板转换表）：rules/rewrite-rules.md
- AI 句式签名清单（词汇/结构/修辞/统计四层全量体检）：rules/ai-signatures.md
- 安全红线（事实/结构/交付/边界四类）：rules/safety-lines.md
- 完整七段实战走查：references/worked-example.md
- 许可模式：本包全部内容采用 MIT 开源；付费完整版另含
  检测器画像库（detector-profile.md），见杨CC资源站 ycc77.cn
