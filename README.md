<div align="center">

<p><a href="https://sealeap.cn/"><img src="./assets/sealeap-logo.png" width="116" alt="SeaLeap" /></a></p>

# 🎨 awesome-design-md-ecommerce

<img src="./assets/hero.svg" alt="Example prompt: give an agent a DESIGN.md reference to guide palette, type, and spacing" width="820">

### Design systems your AI agent can actually read.

**An evidence-qualified collection of e-commerce design references** for AI coding agents. Files describe observed CSS values and inferred design interpretations; each lists its limitations.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![SeaLeap Website](https://img.shields.io/badge/Website-sealeap.cn-0ea5e9)](https://sealeap.cn/)
[![Brands](https://img.shields.io/badge/sites-2%2C636-0a0a0a)](./INDEX.md)
[![Categories](https://img.shields.io/badge/categories-306-444444)](./INDEX.md)
[![Built for AI coding agents](https://img.shields.io/badge/built%20for-AI%20coding%20agents-7c3aed)](#-quickstart)
[![License: MIT](https://img.shields.io/badge/license-MIT-3da639)](./LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-3da639)](./CONTRIBUTING.md)
[![GitHub stars](https://img.shields.io/github/stars/xjli360/awesome-design-md-ecommerce?style=social)](https://github.com/xjli360/awesome-design-md-ecommerce/stargazers)

[**SeaLeap projects**](#sealeap-open-source-projects) · [**Why**](#-why-this-exists) · [**See it**](#-see-it-in-action) · [**Quickstart**](#-quickstart) · [**The collection**](#-the-collection) · [**Recommended →**](./RECOMMENDED.md) · [**Full inventory**](./INDEX.md) · [**Contribute**](./CONTRIBUTING.md) · [**About SeaLeap**](#about-sealeap)

</div>

---

## SeaLeap open-source projects

Explore the companion projects for Amazon operations, multi-platform commerce, and e-commerce interface design:

| Project | What it helps you do |
| --- | --- |
| [sealeap-amazon-skills](https://github.com/xjli360/sealeap-amazon-skills) | Use Agent Skills for Amazon product research, listings, advertising, inventory, and operations. |
| [sealeap-ecommerce-skills](https://github.com/xjli360/sealeap-ecommerce-skills) | Run product research, operations, and advertising workflows for Shopify, Etsy, eBay, TikTok Shop, Walmart, Mercado Libre, and OZON. |
| [awesome-design-md-ecommerce](https://github.com/xjli360/awesome-design-md-ecommerce) (this repo) | Give AI agents e-commerce brand `DESIGN.md` references for storefronts, product pages, and branded interfaces. |

## 💡 Why this exists

AI coding agents are great at *structure* and bad at *taste*. Ask one for a landing page and you get the same rounded-blue-button, Inter-on-white, faintly-gray template every time — because that's the statistical average of everything it has ever seen.

A `DESIGN.md` fixes that. It's a single plain-text file that captures **one storefront's design interpretation** — its palette, type scale, spacing, radii, and component patterns — the visual characteristics associated with that storefront. Drop it into your agent's context and the UI it produces can use the documented palette, type and component guidance, while respecting its evidence limitations.

> Start with [recommended references](./RECOMMENDED.md). The [historical archive](./HISTORICAL.md) is for inspiration only and excluded from default recommendations. CSS value presence does not establish its semantic role. See [status and evidence coverage](./STATUS.md).

**Who it's for** — design engineers prototyping on-brand UI · agencies pitching brand-faithful mockups · indie hackers who want their MVP to *not* look like an MVP · anyone building with Claude Code, Cursor, Copilot, or v0.

## 👀 See it in action

The default entry point is [recommended references](./RECOMMENDED.md). For example, [Glossier's measured reference](./design-md/glossier/MEASURED.md) records actual component styles at desktop, tablet and mobile sizes, with the corresponding screenshots and selectors in [MEASUREMENTS.json](./design-md/glossier/MEASUREMENTS.json).

At capture time its body used `Apercu, "Gill Sans", sans-serif` at `16px`. This measured observation takes precedence over the separate historical DESIGN.md. Hidden or occluded samples are labelled and must not be treated as visible screenshot evidence.

```text
Build a product-page prototype using the attached MEASURED.md and MEASUREMENTS.json.
Use visible measured components where relevant. Mark any additional layout,
interaction, spacing or asset decisions as proposals. Compare screenshots at
matching viewport sizes before making a fidelity claim.
```

Measured components establish the captured state, not a complete site. No entry currently has a verified whole-site reconstruction.

## 🚀 Quickstart

1. **Find a reference** in [recommended references](./RECOMMENDED.md), which prioritizes measured components, then evidenced CSS values.
2. **Give the linked reference to your agent**; include its JSON evidence and screenshots when available.
3. **Ask it to build** — it now has a documented design reference, with explicit gaps.

**Claude Code**
```bash
claude "Build a product page for a ceramic kettle using @design-md/caraway/MEASURED.md — use observed components and label any additional design decisions as proposals."
```

**Cursor / Copilot / Windsurf** — drag the recommended `MEASURED.md` or `DESIGN.md` into chat (or `@`-mention it), then prompt as above.

**v0 / Lovable / bolt** — paste the file contents at the top of your prompt.

## 📐 What's inside each `DESIGN.md`

Nine sections, every file, in the same order — see the full spec in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

| Section | What it captures |
|---|---|
| **Description** | An evidence-grounded editorial read of the brand's design philosophy & voice |
| **`colors`** | Semantic tokens → hex: neutrals, surfaces, accents, semantic roles |
| **`typography`** | Full type scale — `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing` |
| **`rounded`** | Border-radius scale (`xs`–`full`) |
| **`spacing`** | Spacing scale (`xxs`–`section`) |
| **`components`** | Buttons, cards, inputs, nav — as token references |
| **Components** *(prose)* | Each component described with its state variants |
| **Responsive Behavior** | Breakpoints, touch targets, collapse strategy |
| **Known Gaps** | What couldn't be extracted reliably — stated honestly |

## 📚 The collection

<!-- collection-stats:start -->
**2,636 unique website URLs · 2,733 DESIGN.md files · 306 categories.**

Target: 2,817 unique URLs from 3,000 selected records; **181 unique URLs remain**. Historical aliases are preserved. See [collection status](./STATUS.md) for unresolved sources and [the manifest](./data/manifest.json) for canonical IDs, category tags, validation and evidence status.
<!-- collection-stats:end -->

Browse everything in **[`INDEX.md →`](./INDEX.md)**.

<!-- domain-table:start -->
| Domain | Unique websites |
|---|--:|
| More | 1056 |
| Tech & Computing | 242 |
| Books & Media | 186 |
| Home & Living | 165 |
| Outdoor & Garden | 162 |
| Gaming & Collectibles | 141 |
| Baby & Kids | 128 |
| Beauty & Personal Care | 119 |
| Music & Instruments | 112 |
| Stationery & Desk | 105 |
| Kitchen & Cookware | 95 |
| Sport & Fitness | 70 |
| Health & Wellness | 55 |
<!-- domain-table:end -->

### ⭐ Featured brands

Selected brands with measured desktop, tablet and mobile component references:

| Brand | Measured body font (desktop) |
|---|---|
| [**Glossier**](./design-md/glossier/MEASURED.md) | `Apercu, "Gill Sans", sans-serif` · `16px` |
| [**The Ordinary**](./design-md/ordinary/MEASURED.md) | `Raleway` · `16px` |
| [**Drunk Elephant**](./design-md/drunk-elephant/MEASURED.md) | `BrownRegular, "sans-serif"` · `16px` |
| [**Fenty Beauty**](./design-md/fenty-beauty/MEASURED.md) | `Brown, -apple-system, "system-ui", "Segoe UI", Roboto, sans-serif` · `16px` |
| [**Caraway**](./design-md/caraway/MEASURED.md) | `Saans, sans-serif` · `16px` |
| [**Our Place**](./design-md/our-place/MEASURED.md) | `Plaid-XS-Web, Arial, sans-serif` · `16px` |
| [**Hexclad**](./design-md/hexclad/MEASURED.md) | `din-2014, system-ui, sans-serif, "Apple Color Emoji"` · `16px` |
| [**Made In**](./design-md/made-in/MEASURED.md) | `aktiv-grotesk, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` · `16px` |
| [**Parachute**](./design-md/parachute/MEASURED.md) | `"Suisse Intl", sans-serif` · `16px` |
| [**Brooklinen**](./design-md/brooklinen/MEASURED.md) | `Times` · `16px` |
| [**Casper**](./design-md/casper/MEASURED.md) | `Calibre, sans-serif` · `18px` |
| [**Blueland**](./design-md/blueland/MEASURED.md) | `Sailec, "Sailec Fallback", sans-serif` · `17px` |
| [**Ritual**](./design-md/ritual/MEASURED.md) | `CircularXX` · `16px` |
| [**Peloton**](./design-md/peloton/MEASURED.md) | `Inter, sans-serif` · `16px` |

**→ [Browse all 2,636 canonical websites in `INDEX.md`](./INDEX.md)**

## 🛠️ How it's made

Every spec is produced by an automated, resumable pipeline ([`scripts/`](./scripts)):

1. **Crawl** the live storefront and extract real CSS — color values, font stacks, radii, spacing.
2. **Retain evidence** with source URLs, HTTP status, capture time and content hashes. Empty or blocked captures remain on hold.
3. **Generate** a `DESIGN.md` with Claude from captured CSS evidence, labelling inferred roles and measurements.
4. **Validate** real YAML syntax, schema, duplicate keys, token references and evidence allowlists before writing.
5. **Reconcile** canonical website identities and rebuild the index, CSV, manifest and counts.

These are best-effort extractions of public, observable design decisions — each file states its own **Known Gaps**. Provenance (slug, category, source URL) for every brand lives in [`data/brands.csv`](./data/brands.csv).

## 🤝 Contributing

PRs welcome — one brand per PR. Pick a genuinely DTC brand, add `design-md/<slug>/DESIGN.md` following the nine-section spec, and open a PR. Full guidelines in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## 🔗 Related

- [`awesome-design-md`](https://github.com/VoltAgent/awesome-design-md) — the original `DESIGN.md` format and spec this project follows. It curates ~73 developer-focused sites; this list is its e-commerce counterpart — a broad range of commerce categories, the long tail of real storefronts.

## 📄 License

[MIT](./LICENSE) — design tokens describe publicly observable facts about brand interfaces; all trademarks belong to their respective owners.

<div align="center">

---

**If this helps your agent build better UI, leave a ⭐ — it genuinely helps.**

Maintained by [SeaLeap](https://sealeap.cn/).

</div>

## Reproduce and resume

```bash
uv run --with-requirements requirements.txt python scripts/check_format.py
uv run --with-requirements requirements.txt python scripts/check_evidence.py
uv run --with-requirements requirements.txt python scripts/check_measurements.py
uv run --with-requirements requirements.txt python scripts/build_index.py
uv run --with-requirements requirements.txt python scripts/recommend.py cookware
uv run --with-requirements requirements.txt python scripts/worker_claude.py --target 200 --batch-id my-batch
```

`data/sites.csv` contains the selected input records. Install and authenticate Claude CLI separately. Reuse the same batch ID to resume; the target is successful new canonical websites, not attempts. Add `--retry-failed` to retry transient failures in that batch. A process lock prevents duplicate workers. No publishing or git operations are performed.

To review every remaining canonical URL, use `--all-remaining --target 397 --batch-id remaining-review` (the target is informational in this mode). The batch ends as `reviewed`; held sources remain incomplete and are listed in [STATUS.md](./STATUS.md). Resume with the same ID; `--retry-slugs slug-a slug-b` retries selected unresolved entries after source corrections. Successful existing documents are never regenerated by this option.

After an exhaustive review, `scripts/export_review.py <batch-id> --capture-root <recovery-root>` records unresolved sources in `data/source_holds.json`; run `scripts/build_index.py` to rebuild the public status page. Temporary access failures remain retryable. Holds marked `manual_review_required` need a source/identity review before release.

`scripts/capture_rendered.py` captures anonymous desktop, tablet and mobile states using Playwright. It records computed component styles, geometry, screenshots and sampled hover/focus states. Install Playwright separately. The latest attempt must be ready and its capture ID, URL and hashes must match before `--evidence-root` is accepted; a failed retry cannot reuse an old capture.

After reviewing brand identity, `scripts/publish_measurements.py <capture-root>` (with a matching `<capture-root>/brand-review.json`) publishes approved component references and their screenshots. Unrelated redirects and access challenges are excluded. Source images/fonts are referenced, not bundled. These observations do not validate an entire reconstructed website.

For a prototype you have rendered independently, compare each viewport explicitly:

```bash
uv run --with-requirements requirements.txt python scripts/compare_reconstruction.py reference.png candidate.png --report _state/comparison.json
```

This bounded pixel check requires matching image sizes; it never promotes corpus quality automatically. Menu-open behavior and full-page interaction coverage remain unmeasured. Historical references require explicit `scripts/recommend.py --include-historical` opt-in.

## About SeaLeap

**SeaLeap aims to build the world's largest AI cross-border e-commerce community.** We bring together cross-border sellers, brand teams, operators, and AI developers to exchange practical experience in product research, advertising, content, data analysis, and operations automation.

The community offers practical discussions, commerce news, and a Skill Hub where people and Agents turn experience into reusable Skills, tools, and workflows. SeaLeap maintains these three open-source projects. Join us to share your work, ask questions, and improve your next workflow with the community.

<div align="center">
  <p><strong>Shared knowledge. Open-source tools. Practical progress.</strong></p>
  <p><a href="https://sealeap.cn">Visit SeaLeap · Join the community</a> · <a href="https://sealeap.cn/skills">Explore the Skill Hub</a></p>
</div>
