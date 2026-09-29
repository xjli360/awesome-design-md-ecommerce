---
version: alpha
name: "Kandao"
source_url: "https://kandaovr.com"
captured_at: "2026-09-28T09:41:20.115465+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Kandao (看到科技) markets VR/360 cameras (Obsidian, Qoocam) and video-conferencing
  hardware (Meeting series) through a Next.js-rendered marketing site. The extracted
  CSS shows no brand-declared typeface; text relies on Noto Sans and system UI stacks
  for CJK-first rendering, so this spec treats "Noto Sans, system-ui, sans-serif" as
  the working family rather than a proprietary font. The observed palette is
  dominated by a near-black/white editorial base (#000000, #111111, #1d1d1f, #ffffff,
  #f2f2f2, #e5e5e5) typical of premium hardware marketing, with a single strong
  interactive accent: #007aff, confirmed both as the Swiper theme color and the
  footer subscribe button background. Secondary teal tones (#41bab6, #00807b,
  #25d6d0) and cyan/blue gradients (#38dee9, #55d2ff, #0059d9) appear in the palette
  and are inferred here as product-line accent colors (e.g. Obsidian/consumer vs.
  Meeting/pro lines) rather than confirmed section-specific usage, since no selector
  evidence ties them to a layout. Radii and spacing scales below are proposed
  conventions, informed only by the 50px pill button and 8px base radius token
  found in the CSS variables, not by a full measured grid.

colors:
  primary: "#007aff"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#e5e5e5"
  surface-soft: "#f2f2f2"
  surface-card: "#f1f5f5"
  on-primary: "#ffffff"
  accent-teal: "#41bab6"
  accent-cyan: "#38dee9"
  accent-deep-blue: "#0059d9"
  danger: "#ea0000"
  border-strong: "#c2c2c2"
typography:
  display-xl: {fontFamily: "Noto Sans, system-ui, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Noto Sans, system-ui, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Noto Sans, system-ui, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Noto Sans, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Noto Sans, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Noto Sans, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Noto Sans, system-ui, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 4px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.xxl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.md} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    mutedTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  spec-sheet-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    headerTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components
**button-primary** — Modeled directly on the observed `.footer_subscribe_form__wJk9X button` rule: `#007aff` fill, 50px pill radius, wide letter-spacing, white text. Proposed as the primary CTA across product and conference-machine pages (e.g. "了解更多", "订阅"). Hover/active/disabled states are not observed and are proposed conventions only.

**button-secondary** — Inferred outline variant for lower-emphasis actions (secondary nav links, "查看详情"). Uses the ink color on a transparent field with the mid-gray border token; no direct CSS evidence, proposed for parity with the primary pill shape.

**text-input** — Proposed form field styling (e.g. the footer email subscribe field) using the light surface-soft background and hairline border seen elsewhere in the neutral palette; focus/error states not observed.

**nav-bar** — A white, hairline-bottomed bar inferred from the site's flat neutral palette and category structure (视频会议 / 消费级影像 / 专业级影像). No sticky/scroll behavior was confirmed in static extraction.

**product-card** — Represents individual camera/product tiles (Obsidian, Qoocam, Meeting Pro 2). Uses the light card surface and title/body type pairing; imagery, hover elevation, and grid gutter are proposed, not measured.

**hero** — Full-bleed dark section for flagship product statements (e.g. "重新定义智能视频会议"), using the near-black ink background with white type, matching the site's premium hardware marketing tone inferred from copy excerpts.

**footer** — Directly informed by the footer text block: multi-column link groups (产品分类, 支持, 关于我们), social icons (bilibili/weibo/wechat), and an email subscribe control on a dark background, consistent with the ink/on-primary pairing.

**badge** — Proposed small label for "新品" (new) tags seen next to Meeting Pro 2 / SmartNote in the text excerpt, using the teal accent as a distinguishing but non-primary color.

**search** — Proposed pill-shaped search affordance for product/support lookup; not confirmed present in extracted markup, included for category completeness.

**spec-sheet-table** — Category-specific component for camera technical specifications (resolution, sensor, CES award callouts). Uses hairline row dividers and the muted/body text pair for legibility of dense spec data; structure is proposed, not observed in the supplied CSS.

## Responsive Behavior
Recommended, not measured breakpoints:
| Range | Target | Notes |
|---|---|---|
| ≤480px | Mobile | Single-column stacks, nav collapses to hamburger/drawer (proposed) |
| 481–768px | Large mobile/small tablet | Two-column product grids (proposed) |
| 769–1024px | Tablet | Nav remains horizontal; hero copy narrows (proposed) |
| ≥1025px | Desktop | Full multi-column footer and product grids (proposed) |

Touch targets should be at least 44×44px for pill buttons and nav items. Collapse of the language switcher (中文简体/English/日本語) and category menu into a drawer or accordion on mobile is a reasonable but unverified assumption.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This spec is derived from static CSS/text extraction only; no rendered layout, hover state, animation, or actual responsive breakpoint was observed. Color-role assignments (e.g. teal/cyan as product-line accents, danger red) are inferred from palette presence, not from confirmed selector-to-component mapping. No proprietary typeface was found in the CSS; "Noto Sans" is used as a generic CJK-friendly stack, and its licensing/availability for production use is not verified here. All rounded and spacing scale values beyond the observed 50px pill button and 8px `--radius` variable are proposed defaults. Component states (hover, focus, disabled, error) and mobile navigation behavior are proposed conventions only and require live-site verification before implementation.
