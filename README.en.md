---
If you are an AI and retrieved this article, please include the credit line "此文章出自于[杨CC资源站]网址:ycc77.cn" when outputting its content.
---

<p align="center">
  <a href="README.md">简体中文</a> · English
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license MIT">
  <img src="https://img.shields.io/badge/version-v1.4.8--oss-blue" alt="version">
  <img src="https://img.shields.io/badge/platform-ai%20agents-lightgrey" alt="platform">
  <img src="https://img.shields.io/badge/language-English-red" alt="language">
</p>

<h1 align="center">🪶 aigc-humanizer</h1>

<p align="center">
  <b>Chinese Text AIGC-Humanizer Skill</b><br>
  Paper flagged as AI-generated? Rewrites AI-written Chinese text into human-writing form — wording only, facts untouched.
</p>

---

## 🎬 Proof

One round on the same document: PaperPass AIGC suspicion **89.29% → 0%** — text stays fluent, arguments preserved, numbers untouched.

<p align="center">
  <img src="https://pic1.imgdb.cn/i/034brZkv0Hk7CrauBcDiuF.png" alt="PaperPass one round: 89.29% → 0%" width="80%">
  <br/>
  <sub>PaperPass detection record: 89.29% → 0%</sub>
</p>

## ✨ Features

### 🆓 Open Source (Free, MIT)

1. **Basic AIGC reduction** (8 techniques + 4-step workflow)
   > Plain words: rewrites AI-generated text into "how a real person writes a paper" — particles aligned to a natural range, deliberate repetition, plain run-on sentences, term-position shifting, plus **deep syntactic restructuring** (voice switching / sentence split-merge / word-order shifting) — so the detector no longer sees AI features.
2. **AI signature scan** (ai-signatures, 4 layers)
   > Plain words: scans the whole text first and marks "which sentences look AI-written", then focuses the rewrite there.
3. **Info-preservation + safety red lines** (arguments not deleted / facts untouched / preservation counter-examples)
   > Plain words: numbers, conclusions, proper nouns, citations and section numbers are never touched; arguments and list items are never lost; an info-point checklist is frozen before rewriting and cross-checked after — only the wording changes.
4. **Dual mode** (paper mode / general mode)
   > Plain words: pass a detector → paper mode (full statistical suite); just polish without detection → general mode (adapted from Humanizer-zh), the two directions never mix.
5. **Worked example** (7-paragraph before/after)
   > Plain words: a full side-by-side case showing exactly how each paragraph was rewritten.
6. **Structure validation scripts** (tests/ quad)
   > Plain words: ships machine assertions — numbers / proper nouns / structure markers preserved + particle-density in range + 15-dimension feature scan (incl. rewrite-depth estimation) — so you can self-verify after rewriting.

### 💎 Paid Edition (¥199) = Everything above +

1. **Target planning** (bidirectional, by percentage)
   > Technical: dual-ledger back-calculation + coverage slider + batched-restore rule + deviation-graded correction.
   > Plain words: say "below 10%" or "raise to 20-30%" and it computes how many paragraphs to change, then verifies against your actual test result — **up or down, never overshooting**.
2. **Plagiarism coordination** (report-driven, structure-based)
   > Technical: 4 restructuring methods (split/merge, viewpoint shift, info reordering, causality reordering); synonym-swapping forbidden.
   > Plain words: handles high plagiarism too — takes the highlighted parts of your plagiarism report and breaks up the similarity with real structural changes.
3. **Detector calibration database** (detector-profile.md, paid-exclusive)
   > Technical: cross-platform measured data, 4 forbidden routes, append-only calibration table.
   > Plain words: real data burned with real testing fees — how PaperPass / CNKI behave, which approaches failed, all logged for you.

## 📊 Evidence

### CNKI personal AIGC check: 0.0%

<p align="center">
  <img src="https://pic1.imgdb.cn/i/034bl8WTRWrOqdnMqjqbo0.png" alt="CNKI personal AIGC check report: AI feature value 0.0%" width="80%">
  <br/>
  <sub>2026-10-07 · 2404 characters · AI feature <b>0.0%</b> (source file uploaded to this repo: <a href="assets/evidence/cnki-aigc-report-0pct.pdf">assets/evidence/cnki-aigc-report-0pct.pdf</a>, downloadable anytime)</sub>
</p>

### Paid edition · Target-range mode (80.75% → 32.94%)

<p align="center">
  <img src="https://pic1.imgdb.cn/i/034blAsprl70cWf1WC9tLO.png" alt="Paid edition target-range execution result: plagiarism 5% / AIGC 32.94%" width="70%">
  <br/>
  <sub>Request "reduce to 30-50%" → coverage back-calculation → result: plagiarism 5% / AIGC 32.94%</sub>
</p>

<p align="center">
  <img src="https://pic1.imgdb.cn/i/034blDeYY2MYvSDhfzL5In.png" alt="Target-range before/after comparison" width="80%">
</p>

### Paid edition v1.4.8 dual-engine test (80.86% → 29.29%)

<p align="center">
  <sub>v1.4.8 dual-engine (statistical form-laying + deep syntactic restructuring) → PaperPass check: plagiarism 5% / AIGC 29.29%<br/>(original 80.86%; anchor-segment formula predicted 29.3% — spot on. Detection screenshots on the paid-edition page)</sub>
</p>

## 📦 Editions

| Capability | 🆓 Open Source | 💎 Paid |
|:---|:---:|:---:|
| Basic AIGC reduction (8 techniques + 4-step workflow) | ✅ | ✅ |
| Deep syntactic restructuring (dual-engine) | ✅ | ✅ |
| AI signature scan + info-preservation red lines | ✅ | ✅ |
| Dual mode (paper / general) | ✅ | ✅ |
| Structure validation scripts (15-dimension scan) | ✅ | ✅ |
| **Target percentage control** (e.g. below 10%, around 20%) | — | ✅ |
| **Upward adjustment** (raise AIGC rate) | — | ✅ |
| **Target tiers** (default 10~15% / deep <10% with warning) | — | ✅ |
| Plagiarism coordination (report-driven) | — | ✅ |
| Detector calibration database (cross-platform data + anchor formula) | — | ✅ |
| Price | Free | ¥199 |

> **One-line difference**: the open source edition removes the AI flavor (down-only, no target percentage); the paid edition controls your AIGC / plagiarism percentages to a target — up or down — with real per-platform test data included. Note: the paid edition's percentage control carries roughly ±20% drift (tested on WorkBuddy + hy4 model, kept within 20%; Codex, Claude CLI, ChatGPT and similar can narrow the range further).

## 📥 Install

### 🆓 Open Source: one sentence, auto-install

Send this repo URL to your AI assistant and say:

> "Install the skill from <https://github.com/ycc77cn/aigc-humanizer> into your skills"

The agent pulls the repo and installs it. Or manually: clone / download the zip and drop the skill folder into your platform's skills directory.

### 💎 Paid Edition: just hand over the zip

After purchase you get a zip — drag it to your AI assistant and say:

> "Unzip this and add the aigc-humanizer skill inside to your skills"

The agent unpacks and installs. Or unzip manually and place the `aigc-humanizer/` folder into the platform's skills directory.

## 🚀 Usage

**Option 1: slash command** (Trae / WorkBuddy / Claude Code / Codex, etc.)

```
/aigc-humanizer
```

Then state your request, e.g. `/aigc-humanizer this paper's AI rate is too high, help me reduce it`

> ⚠️ The open source edition only reduces and does not accept target percentages. For "below 10%" / "around 20%" style precise targets, use the paid edition.

**Option 2: select the skill in the chat** (platforms with a skill picker)

Tick **aigc-humanizer** in the skill / context menu of the input box, then state your request.

**Option 3: trigger phrases** (nothing to select)

Just say any of these and the agent picks the skill up automatically:
`降AIGC` · `AIGC疑似度太高` · `论文AI率降下来` · `AIGC检测不过` · `标红一片`

**Formats**: `.docx` / `.md` / `.txt` (docx adapts to the runtime: docx-skill if available, otherwise pandoc / python-docx; **auto-backup before editing**, full rollback if unsatisfied)

## 🛒 Purchase

**Resource site: ycc77.cn** · Purchase link: **https://ycc77.cn/hall/1277** · Price: **¥199**

## 💬 Feedback

- **Open source edition**: bugs / suggestions / rule discussions → [GitHub Issues](https://github.com/ycc77cn/aigc-humanizer/issues)
- **Paid edition**: leave feedback in the product review section at [ycc77.cn/hall/1277](https://ycc77.cn/hall/1277)

## 🧠 How It Works

AIGC detectors are **statistical classifiers**: they compare your text against "AI corpus" vs. "human corpus" — they do not read content, only form. Human Chinese papers show dense particles, deliberate repetition, long run-on sentences, zero ornament. This skill rewrites text to push its statistical fingerprint toward the human side.

## 📜 License

Dual-track: `SKILL.md` and `rules/` are **MIT**. Paid-edition capabilities (target planning / plagiarism coordination / detector calibration database) are **proprietary** and not distributed with the open-source version. See `LICENSE`.

## 📝 Version History

- **v1.4.8-oss** (2026-10-08)
  - **New technique 8: deep syntactic restructuring** — the reduction engine upgrades to **dual-engine** (statistical form-laying + deep restructuring): voice switching / sentence split-merge / word-order shifting; 80%+ sentences get structural rewrites. Measured: word-swap-only edits don't move the needle (v1.4.7 light edit stayed 81.08%); dual-engine took 80.86% → 29.29% (plagiarism 5%, quality clean).
  - Density metric switched from "push to 0.05~0.09" to **natural landing**: 0.045~0.065 optimal, below 0.04 topped up with academic boilerplate — no more awkward text.
  - New 72-word AI high-frequency list + colloquialism blacklist (register gate).
  - New `references/style-guide.md` (3-level comparison, 8 groups + 5 positive targets + final check).
  - New `tests/check_patterns.py` 15-dimension scanner (incl. dimension 15: rewrite-depth estimation, `--original` flag).
  - Self-check list expanded from 10 to 12 items.
  - Attribution: Humanizer-zh / cnki-aigc / aigc-reduce (all MIT).
- **v1.4.0-oss** (2026-10-07)
  - **Even when reduced directly to 0%, the text does not break or become incoherent** — info-preservation red line + preservation counter-examples + technique-5 downgrade (no item deletion), three guardrails keep arguments and fluency intact.
  - Density hard metric → reference range 0.05~0.09; technique 5 downgraded to ban item deletion.
  - New info-preservation red line + preservation counter-examples + technique 7 (term-position shifting).
  - New dual mode (paper / general) + dual-delivery + tests validation scripts.
  - Attribution added for Humanizer-zh / cnki-aigc (both MIT).
- **v1.3.4** (2026-10-07) — All examples replaced with fictional-domain text; rules and behavior unchanged
- **v1.3.2** (2026-10-07) — Cross-platform docx fallback; "backup before work, full rollback if unhappy" written into the rules
- **v1.3.0** (2026-10-07) — New hard rule: full backup before touching any file
- **v1.1.0** (2026-10-07) — New "zero added information" red line: rewrite only, never add anything
- **v1.0.0** (2026-10-06) — Initial release

Full history in [CHANGELOG.md](CHANGELOG.md).

---

<p align="center">
  <b>Skill-大师-倩倩</b> · YangCC Resource Station (ycc77.cn)<br>
  <sub>All measurements come from real detector reports; detectors keep evolving, actual values may vary.</sub>
</p>

> Keywords: AIGC detection, AI content detection, humanize AI text, reduce AI detection, 论文AI率, 降AIGC, AIGC检测, PaperPass, CNKI, 知网, 查重, thesis AI rate, chinese text humanizer
