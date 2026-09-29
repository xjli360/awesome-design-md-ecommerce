---
version: alpha
name: "Disk Union"
source_url: "https://diskunion.net"
captured_at: "2026-09-29T04:17:26.465538+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Disk Union's storefront CSS shows a utilitarian, Bootstrap-derived system layered with a curated warm-red accent family (#de5d50, #b24a40, #bd4f44, #cf3f34, #fdf1f0) alongside a muted teal family (#5cb1b1, #4a8e8e, #4e9696). These paired families are proposed here as primary/secondary accents for sale badges, format tags, and reservation states, since the observed page text is dense with pricing, discount percentages, and stock-status labels (予約, 新品在庫あり, OFF). Neutral grays (#212529, #333333, #6c757d, #dee2e6, #f8f9fa, #f7f8f9) form the working ink/body/surface scale typical of a high-density catalog listing. Font evidence includes Noto Sans JP and Yu Gothic (Japanese body text), Oswald (a condensed display face, inferred here for numerals/headings such as prices and section titles), and Font Awesome icon fonts (not used for text). Bootstrap CSS variables (--bs-*) confirm a component-library foundation rather than a fully bespoke design system. This interpretation treats Disk Union as a catalog-first, inventory-heavy record/media retailer: dense grids, compact badges, and strong red/teal status coding, with layout rhythm and interaction states proposed rather than observed.

colors:
  primary: "#cf3f34"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#f7f8f9"
  on-primary: "#ffffff"
  accent-tint: "#fdf1f0"
  accent-deep: "#b24a40"
  secondary: "#4e9696"
  secondary-deep: "#4a8e8e"
  link: "#337ab7"
  warning: "#ffc107"
  info: "#0dcaf0"
  success: "#198754"
  danger: "#dc3545"
  footer-dark: "#343a40"
typography:
  display-xl: {fontFamily: "Oswald, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Oswald, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Noto Sans JP, Yu Gothic, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Noto Sans JP, Yu Gothic, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Noto Sans JP, Yu Gothic, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Noto Sans JP, Yu Gothic, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "Noto Sans JP, Yu Gothic, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.43, letterSpacing: 0.2px}
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
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.footer-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-tint}"
    textColor: "{colors.accent-deep}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  format-tag:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"

## Components

**button-primary** proposes the warm-red accent (#cf3f34) for primary actions such as "カートに入れる" (add to cart) or "予約" (reserve), reflecting the discount/urgency coloring seen throughout the pricing text (OFF percentages, sale labels). States (hover/active/disabled) are proposed, not observed.

**button-secondary** is an outlined variant sharing the primary hue for lower-emphasis actions like "お店で受け取る" (store pickup), inferred from the pairing of dual CTAs seen in the chart section text.

**text-input** models a neutral bordered field using the hairline gray, suited to the site's search and account-login flows (パスワード再設定 references imply forms exist); no focus-ring color was directly observed, so it is proposed only.

**nav-bar** is a light, bordered top navigation inferred from the multi-section menu text (オンラインショップ, 中古販売, 買取情報, 店舗情報); exact height, sticky behavior, and active-state styling are not measured from static CSS.

**product-card** is the core catalog unit—cover art, title/artist, format, price, and stock badge—derived from the repeating "新入荷商品", "予約商品", and "アウトレット" listing patterns in the page text. Border and radius values are proposed defaults, not extracted layout metrics.

**hero** proposes a soft-surface banner area for featured releases or campaign messaging (e.g., "レコードの日 2026"), using surface-soft as background since no hero-specific CSS was supplied.

**footer** uses a dark charcoal background (#343a40, drawn from the Bootstrap-influenced dark palette) for the extensive footer link list (店舗一覧, 買取情報, 利用規約, 関連部門), consistent with the long footer text block observed.

**badge** models the discount/status chips seen in text such as "40%OFF", "新品在庫あり", and "予約終了", using the tinted red family for visual consistency with the sale-heavy outlet section; exact badge shapes were not directly measured.

**search-bar** is inferred for the "商品一覧・検索はこちらから" prompt; no search-specific selectors were present in the supplied CSS.

**format-tag** is a category-appropriate component for labeling media type (CD／レコード／映像／書籍), using the teal secondary family observed in the palette to visually distinguish format from discount badges.

## Responsive Behavior

Recommended breakpoints (not measured from live site, but aligned to the Bootstrap `--bs-breakpoint-*` custom properties present in the CSS): xs 0px, sm 576px, md 768px, lg 992px, xl 1200px, xxl 1400px. Nav and category filters are expected to collapse into a hamburger/drawer pattern below `md`; product-card grids likely reflow from multi-column (desktop) to 2-column or single-column (mobile). Touch targets should be a minimum 44×44px for cart/reserve buttons given the dense catalog listing. This section is a design recommendation only; no responsive or interaction behavior was observed from static CSS extraction.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from static CSS and page-text evidence only; no rendered layout, computed spacing, or live interaction states (hover, focus, active, loading, error) were observed. Font rendering for Oswald and Noto Sans JP assumes standard web-safe delivery; actual licensing, weights, and fallback behavior were not verified. Color role assignments (e.g., primary, secondary, ink) are inferred from frequency and contextual pairing within the supplied palette, not from confirmed brand guidelines. Spacing, radius, and breakpoint values are proposed conventions, not measured from the site. Mobile navigation, drawer, and carousel (slick-dots) interaction beyond the default/active states shown in CSS were not confirmed. The `.production-category-list-item.is-active` rule suggests category-filter active states exist, but its full context and trigger were not observed.
