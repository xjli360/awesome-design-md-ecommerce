---
version: alpha
name: "PNY"
source_url: "https://www.pny.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep navy #222222 and cool steel #656565 industrial palette grounds PNY’s hardware-first identity, with a sharp accent of #079bd5 — a cyan that reads as data-in-motion — used sparingly on category headers and spec-table highlights. The brand’s typography is a two-weight system: Bebas Neue Pro for all display and title roles, a compressed sans-serif with tight letter-spacing that evokes GPU shroud vents and server rack lines, paired with Arial for body copy in a no-nonsense 14px/16px. Every product card uses a 1px #dedede hairline border and {rounded.sm} corners, creating a grid of identical rectangles that feels like a warehouse shelf — functional, scannable, unadorned. The primary CTA is a solid #079bd5 rectangle with white 14px Bebas Neue Pro uppercase text, 48px tall, no shadow, no gradient. Secondary actions drop to a #222222 outline on white. The nav bar is a fixed 48px strip of #222222 with white Bebas Neue Pro navigation links, no dropdown chevrons, no hover underline — just a hard #079bd5 left-border on the active tab. Badges appear in two flavors: a green #76b900 “IN STOCK” and a red #991b1e “SALE”, both set in 11px uppercase Bebas Neue Pro with {rounded.xs} corners. The footer is a dense #222222 slab with white 12px Arial links in three columns, no icons, no newsletter signup — pure utility. PNY does not decorate; it indexes.

colors:
  primary: "#079bd5"
  primary-active: "#0689bc"
  primary-disabled: "#8d8f93"
  ink: "#222222"
  body: "#444444"
  muted: "#656565"
  muted-soft: "#a7a9ac"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#76b900"
  success-dark: "#558600"
  danger: "#991b1e"
  danger-bright: "#ff2727"
  warning: "#ff9b2f"
  accent-cyan: "#00aeef"
  accent-blue: "#19648a"
  accent-steel: "#8a8d91"

typography:
  display-xl:
    fontFamily: "'Bebas Neue Pro', 'Bebas Neue', 'bebas-neue-pro', 'bebasneue', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: 1.5px
  display-md:
    fontFamily: "'Bebas Neue Pro', 'Bebas Neue', 'bebas-neue-pro', 'bebasneue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: 1.2px
  display-sm:
    fontFamily: "'Bebas Neue Pro', 'Bebas Neue', 'bebas-neue-pro', 'bebasneue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: 1px
  title-md:
    fontFamily: "'Bebas Neue Pro', 'Bebas Neue', 'bebas-neue-pro', 'bebasneue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0.8px
  title-sm:
    fontFamily: "'Bebas Neue Pro', 'Bebas Neue', 'bebas-neue-pro', 'bebasneue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0.6px
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Bebas Neue Pro', 'Bebas Neue', 'bebas-neue-pro', 'bebasneue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Bebas Neue Pro', 'Bebas Neue', 'bebas-neue-pro', 'bebasneue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Bebas Neue Pro', 'Bebas Neue', 'bebas-neue-pro', 'bebasneue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 1px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "'Bebas Neue Pro', 'Bebas Neue', 'bebas-neue-pro', 'bebasneue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
  full: 9999px

spacing:
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
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 24px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "2px solid {colors.danger}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderLeft: "3px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  product-card-hover:
    border: "1px solid {colors.primary}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  badge-stock:
    backgroundColor: "{colors.success}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    height: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    height: 40px
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.body}"

## Components

### Buttons
**`button-primary`** — Solid #079bd5 rectangle with white uppercase Bebas Neue Pro 14px text, 8px rounded corners, 48px tall. On hover, darkens to #0689bc. Disabled state drops to #8d8f93 with no pointer events. Used for “Add to Cart”, “Buy Now”, and primary form submissions. No icon, no shadow, no gradient — pure flat rectangle.

**`button-secondary`** — White canvas with a 1px #222222 border and matching ink text. Hover fills the background with #f8f8f8. Same 48px height and 8px radius as primary. Used for “Learn More” and secondary checkout actions.

**`button-ghost`** — Transparent background with #079bd5 text only. No border, no fill. Used for text links styled as buttons in spec tables and comparison tools.

**`button-pill`** — Full-radius pill variant of primary, 36px tall with 8px vertical padding. Used for filter chips and quick-add actions on product listing pages.

### Cards
**`product-card`** — White rectangle with 1px #dedede border, 8px rounded corners, 16px padding. Title uses 16px Bebas Neue Pro in #222222, price in 16px Arial #444444. On hover, border shifts to #079bd5. Badges overlay top-left with {spacing.sm} offset. Image area is 4:3 ratio with no border-radius on the image itself.

**`hero-banner`** — Full-width #222222 slab, 400px tall, with #ffffff display-xl Bebas Neue Pro headline and a single #079bd5 CTA button. Background may carry a product image at 50% opacity. No carousel dots, no secondary text.

### Navigation
**`nav-bar`** — Fixed 48px #222222 strip across the full viewport. Links are white 14px uppercase Bebas Neue Pro with 1px letter-spacing. Active tab gets a 3px #079bd5 left border. No dropdowns, no mega-menus, no search icon in the nav itself. The logo sits left in white, typically the PNY wordmark.

**`category-strip`** — A 40px #f8f8f8 horizontal band below the nav, containing category links in muted #656565 Bebas Neue Pro. Active category gets a 2px #079bd5 bottom border. Used for SSD, Graphics, Memory, Storage, Networking, and Accessories.

### Forms
**`text-input`** — White background, 1px #dedede border, 8px radius, 44px tall, 14px Arial body text. Focus state swaps to a 2px #079bd5 border with no outline. Error state uses 2px #991b1e. Placeholder text in #a7a9ac.

**`select-dropdown`** — Same dimensions as text-input but with a custom chevron arrow in #656565. No native browser chrome visible.

### Footer
**`footer`** — Dense #222222 slab with 48px vertical padding and 64px horizontal. Three columns of 12px Arial links in #a7a9ac, hovering to white. No social icons, no newsletter form, no brand story — just product categories, support links, and legal text in 11px Arial #656565.

### Badges
**`badge-stock`** — Green #76b900 pill with white 11px uppercase Bebas Neue Pro, 4px radius, 2px vertical / 8px horizontal padding. “IN STOCK” only. **`badge-sale`** — Red #991b1e with same styling, “SALE”. **`badge-new`** — Cyan #079bd5, “NEW”. All badges sit at top-left of product cards with 8px offset.

### Tables
**`spec-table`** — White background with 1px #dedede borders. Header row uses #f8f8f8 background with 16px Bebas Neue Pro #222222. Alternating rows get #f8f8f8 background. Cells are 14px Arial #444444 with 12px padding. Used extensively on product detail pages for technical specifications.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero banner reduces to 240px height; category strip scrolls horizontally; footer stacks to single column |
| Tablet | 744–1128px | Nav links remain visible but font-size drops to 12px; product cards in 2-column grid; hero at 320px; category strip wraps to two rows |
| Desktop | 1128–1440px | Full 3–4 column product grid; nav at full 14px; hero at 400px; footer in three columns |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid expands to 5 columns; hero remains 400px |

### Touch Targets
- All buttons and links minimum 44px height
- Nav hamburger icon 48x48px tap area
- Category strip items 40px height with 16px horizontal padding
- Product card CTA buttons 48px tall
- Pagination items 44x44px minimum

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Category strip becomes horizontally scrollable on mobile
- Product grid drops from 4–5 columns to 2 columns on tablet, 1 column on mobile
- Footer columns stack vertically below 744px
- Hero banner text reduces from display-xl to display-md on mobile
- Spec tables become horizontally scrollable on mobile, with first column frozen

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components could not be reliably extracted from the live site; the above are best-guess based on common patterns
- Error message styling (inline validation, toast notifications) not observed
- Dark mode — no evidence of implementation
- Sub-brand palettes (e.g., NVIDIA GeForce co-branded products may use #76b900 green, but this appears as a badge color only)
- Animation and transition timing values (durations, easings) not extracted
- Modal and overlay styling not observed
- Loading states (skeleton screens, spinners) not documented
- The extracted color list is heavily weighted toward grays (#dedede, #222222, #656565, #a7a9ac, #eeeeee, #444444, #1a1a1a, #3f3f3f, #8a8d91, #8d8f93, #9a9ca0, #f8f8f8, #f3f3f3) with a few accent blues (#19648a, #248ab6, #079bd5, #0577a4, #0689bc, #00aeef, #3372df), one green (#76b900, #558600, #117744), one orange (#ff9b2f), one yellow (#ffe92f), and multiple reds (#991b1e, #ff2727, #ff202b, #a51d21, #ff2f2f). The true brand primary appears to be #079bd5 based on its use in CTAs and active states, but the palette is dominated by neutral tones with the accent colors likely tied to specific product lines or third-party integrations.
- Font stack includes both `bebas-neue-pro` and `bebasneue` — the former is the intended brand font, the latter likely a fallback or older variant
- `GEforce` font declaration suggests NVIDIA co-branded pages may use a different typeface, but this is not part of the core PNY system
