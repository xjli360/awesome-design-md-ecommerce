---
version: alpha
name: "Rotiform"
source_url: "https://rotiform.com"
captured_at: "2026-09-28T10:18:33.112697+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Rotiform's supplied CSS surfaces a neutral, high-contrast utility palette (white
  #ffffff, near-black #1e1e1e, and a spread of mid-grays from #888888 to #f9f9f9)
  layered with a vivid orange family (#ff8400, #f98b25, #ff9635) that appears in
  vendor slider and lightbox component code. No labeled brand token was present
  in the evidence, so the orange is treated as an inferred primary accent — a
  plausible fit for an aftermarket-wheel brand's aggressive, performance-driven
  tone — while the near-black #1e1e1e (matching the fancybox overlay
  rgba(30,30,30,.7)) is proposed as the ink/dark-surface color. A secondary blue
  (#4ea7f9) and yellow (#ffdf66) are held in reserve for inferred link/focus and
  badge/highlight roles, since no usage context was captured for either.
  Typography is confirmed only as a Helvetica Neue/Helvetica/Arial sans-serif
  stack pulled from vendor CSS (slick, fancyambox); no custom display face or
  verified type scale was observed, so all sizes below are proposed editorial
  defaults built on that confirmed family, with 13px and 16px anchored to
  observed vendor rules. The resulting interpretation favors a dark, industrial
  e-commerce shell — black/near-black surfaces, sharp small-radius UI, and
  orange CTAs — suited to a wheel/tire catalog built around product cards, size
  and finish selectors, and spec-driven detail pages.

colors:
  primary: "#ff8400"
  primary-alt: "#f98b25"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#888888"
  hairline: "#dddddd"
  surface-soft: "#efefef"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-blue: "#4ea7f9"
  accent-yellow: "#ffdf66"
  border-strong: "#aaaaaa"
typography:
  display-xl: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.45, letterSpacing: "0px"}
  caption: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.5px"}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.primary}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary** uses the inferred orange accent as a solid fill for the main "Shop" / "Add to Cart" actions, with white text for contrast. Hover/active/disabled states were not observed and are proposed: a darker orange fill (`{colors.primary-alt}`) on hover and reduced opacity on disabled.

**button-secondary** is a transparent, hairline-bordered variant for lower-priority actions such as "View Gallery" or "Compare," sitting beside the primary button on product and category pages. Hover state (subtle background tint) is proposed, not observed.

**text-input** covers login, newsletter, and search-adjacent form fields referenced in the page text (Email, Password fields). A thin hairline border and minimal radius keep it consistent with the site's flat, utilitarian UI; focus-ring color is proposed as `{colors.accent-blue}` since no focus style was captured.

**nav-bar** represents the persistent header housing Products, Galleries, Dealers, Support, Account, and Search entries named in the page text. A white background with hairline bottom border is proposed for a clean, catalog-forward feel; sub-menu flyouts for "Wheels / Cast MonoBlock / Flow Formed / RotiSpec Forged" etc. are anticipated but not verified.

**product-card** models the wheel-listing tiles seen in the excerpt (name, "Starting at $X.XX", Sizes, Material, Features). Card background is a very light off-white (`{colors.surface-card}`) with a hairline border to separate tiles in a dense grid; price and spec rows use `body-md`/`body-sm`.

**hero** is proposed as a dark, full-bleed banner (near-black background, white text, orange accent) for campaign moments like "Shop new MonoBlock styles" — consistent with the confirmed dark-overlay color from the fancybox infobar rule, though no hero markup was directly observed.

**footer** mirrors the dark ink background with light text, hosting Support/Dealer/Account links; this is a proposed layout inference from the presence of extensive footer-style navigation text (Help Center, Dealer Login, Locate A Dealer) rather than an observed footer selector.

**badge** is a small pill for flags like "NEW" (seen prefixing TDX, SCP, CGN, ZBF, CJJ in the excerpt) or review counts ("1 Review," "2 Reviews"). Yellow fill on dark ink text is proposed to draw attention without competing with the orange CTA color.

**search** is a rounded, soft-gray field for the "Search" affordance named near "Shopping Cart" in the header text; expand/collapse and results-dropdown behavior are proposed, not observed.

**size-selector** is a category-specific component for choosing wheel diameter (e.g., 18", 19", 20") shown repeatedly in product data. Pills toggle from a neutral gray idle state to an orange-filled selected state, matching the primary CTA color for consistency between browsing and purchasing actions.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Range | Layout guidance (proposed) |
|---|---|---|
| mobile | up to 599px | Single-column product grid; nav collapses to a hamburger/drawer; size-selector pills wrap to 2–3 per row. |
| tablet | 600–959px | 2-column product grid; nav shows condensed top-level items with an overflow/menu toggle. |
| desktop | 960–1279px | 3–4 column product grid; full horizontal nav with mega-menu-style dropdowns for Products/Galleries. |
| wide | 1280px+ | 4+ column grid with fixed content max-width; hero and gallery modules gain generous side padding (`{spacing.section}`). |

Touch targets should target a minimum ~44px hit area for buttons, size-selector pills, and nav items on mobile, per general accessibility practice — not derived from measured CSS. Sticky/collapsing header behavior on scroll is plausible for a catalog site but unverified.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, DOM structure, or interaction states (hover, focus, active, error) were observed.
- Semantic color roles (primary, ink, muted, hairline, etc.) are inferred from vendor/utility CSS (slick carousel, fancyambox lightbox) rather than confirmed brand style-guide usage; the orange family's status as an official brand color is not verified.
- All typography sizes except `body-sm` (13px, from `.fancyambox-infobar__body`) and the 16px reference point are proposed editorial defaults, not measured from headline/body CSS.
- No custom or licensed webfont was found; only a system Helvetica/Arial sans-serif stack is confirmed, so no font licensing claims are made.
- Rounded and spacing scales follow a standard proposed system, not values extracted from the site's CSS.
- Mobile navigation pattern, cart/drawer behavior, and gallery/lightbox visual treatment are inferred from component names in page text (Wishlist, Shopping Cart, Search, galleries) but not visually confirmed.
