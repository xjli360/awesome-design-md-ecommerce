---
version: alpha
name: "Blackstone"
source_url: "https://www.blackstoneproducts.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The first thing that hits you on Blackstone's site is that #f26322 orange — not a caution label, not a sunset gradient, but the exact color of a griddle surface at 400°F when seasoning oil flashes into polymerized carbon. That single hue saturates every primary CTA, every announcement ribbon, every "Add to Cart" moment, punching through a system that otherwise runs almost entirely in industrial grayscale: deep #1c1c1c ink fields, #58595b body copy, and #f5f5f5 surface planes that read like brushed stainless panels on commercial kitchen equipment. Dark-mode hero sections — full-bleed #212121 backgrounds carrying CheddarGothicSans headlines in uppercase white — frame the product as serious cooking hardware that happens to live on a patio, never the other way around.

  Typography is where Blackstone breaks from the outdoor-brand template. CheddarGothicSans, a wide gothic sans with heavy horizontal stress and visible ink traps, handles all display text (`{typography.display-xl}` at 56px, all-caps, 1.05 leading) and gives headlines the same stamped-fascia presence you see laser-etched on the griddle's own front panel. Below that, Acumin Pro — Adobe's neo-grotesque workhorse — picks up titles, body, and UI labels in regular through semibold weights, with the condensed cut (`acumin-pro-condensed`) reserved for footer headings and dense comparison-table labels. DIN 2014 surfaces exclusively in price stacks, lending dollar figures the monolinear clarity of engineering spec sheets. Corners stay minimal throughout: `{rounded.xs}` (4px) on buttons, cards, and inputs; `{rounded.full}` only appears on the search bar. No soft 12px or 20px lifestyle radii exist in the main product flow — the geometry is square enough to feel machined from flat stock.

  The color system supports a deliberate two-canvas strategy. Product grids and informational layouts run on white `{colors.canvas}` with `{colors.surface-soft}` card backgrounds, while hero modules and collection banners drop into `{colors.canvas-dark}` or `{colors.surface-charcoal}` (#212121), always pairing that signature orange against high-contrast white type. A warm peach `{colors.surface-warm}` (#ffe6da) appears in feature-highlight cards and promotional callouts — the only softness in an otherwise utilitarian palette. Sale pricing uses a dedicated `{colors.sale}` (#c00000) red, deliberately separated from brand orange so discounting never dilutes the primary signal. Badges snap to card corners at `{rounded.xs}` with uppercase `{typography.badge}` text at 11px, small but legible at browsing speed.

colors:
  primary: "#f26322"
  primary-active: "#e35205"
  primary-disabled: "#f9b691"
  accent-flame: "#ff5a00"
  ink: "#1c1c1c"
  ink-deep: "#111111"
  body: "#58595b"
  muted: "#919191"
  muted-soft: "#777777"
  hairline: "#d9d9d9"
  hairline-soft: "#d5d5d5"
  canvas: "#ffffff"
  canvas-dark: "#1c1c1c"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-warm: "#ffe6da"
  surface-charcoal: "#212121"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale: "#c00000"
  sale-deep: "#a10018"
  steel: "#6d6d6d"

typography:
  display-xl:
    fontFamily: "'CheddarGothicSans', 'Acumin Pro', Impact, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: 0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'CheddarGothicSans', 'Acumin Pro', Impact, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'CheddarGothicSans', 'Acumin Pro', Impact, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.25px
    textTransform: uppercase
  title-lg:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', 'Barlow', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', 'Barlow', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Acumin Pro', 'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Acumin Pro', 'Barlow', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Acumin Pro', 'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Acumin Pro', 'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Acumin Pro', 'Barlow', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'din-2014', 'DIN 2014', 'Acumin Pro', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'din-2014', 'DIN 2014', 'Acumin Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through
  badge:
    fontFamily: "'Acumin Pro Semibold', 'Acumin Pro', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  condensed-label:
    fontFamily: "'acumin-pro-condensed', 'Acumin Pro', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-dark-hover:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
  hero-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 560px
  hero-split:
    backgroundColor: "{colors.surface-charcoal}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    ctaStyle: "button-primary"
    layout: "50/50 image-right"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    imageRounded: "{rounded.xs}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-bestseller:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  collection-banner:
    backgroundColor: "{colors.surface-charcoal}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl} {spacing.lg}"
  recipe-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(242,99,34,0.15)"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.condensed-label}"
    padding: "{spacing.section} {spacing.lg}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
  feature-icon-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.condensed-label}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.lg} {spacing.xl}"
  rating-stars:
    filledColor: "{colors.primary}"
    emptyColor: "{colors.hairline}"
    size: 16px
---

## Components

### Buttons

**`button-primary`** — A solid #f26322 orange rectangle with 4px radius, white uppercase text in Acumin Pro Semibold at 16px with 0.5px letter-spacing. Padding is generous (14px vertical, 32px horizontal) to create a 48px-tall hit target that feels substantial. On hover, background darkens to `{colors.primary-active}` (#e35205); disabled state washes out to `{colors.primary-disabled}` (#f9b691) while maintaining the same geometry.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, matching the primary's dimensions and typography but inverting the contrast relationship. On hover, the entire button floods to `{colors.ink}` with white text — a full inversion rather than a subtle tint shift, consistent with the brand's preference for high-contrast state changes over soft transitions.

**`button-dark`** — Used on light backgrounds where the primary orange would compete with nearby product imagery. Solid `{colors.ink}` fill, white text, same 4px radius and 48px height. Hover darkens to `{colors.body}` (#58595b), creating a subtle but perceptible shift.

### Navigation

**`nav-bar`** — A 64px-tall white bar with uppercase Acumin Pro Semibold links at 14px. The Blackstone wordmark sits left-aligned; primary navigation items are spaced with `{spacing.lg}` gaps. A thin `{colors.hairline}` bottom border separates nav from content. On collection and product pages, the nav switches to `nav-bar-dark` with a `{colors.canvas-dark}` background and white text to match dark hero sections below.

**`announcement-bar`** — A 40px ribbon in solid `{colors.primary}` orange that sits above the nav, carrying promotional copy in `{typography.caption}` white text. Often includes a dismissal ×, which removes the bar and shifts the nav upward.

**`mega-menu`** — Drops from the nav on category hover, white background with `{colors.hairline-soft}` border. Category headings use `{typography.condensed-label}` (Acumin Pro Condensed, 14px, uppercase) while subcategory links use `{typography.body-sm}`. Generous `{spacing.lg}` padding throughout.

### Product Cards

**`product-card`** — Sits on a `{colors.surface-soft}` background with `{rounded.xs}` corners. Product image fills the top portion with matching 4px radius. Title uses `{typography.title-sm}` (Acumin Pro 600, 16px), price uses `{typography.price}` (DIN 2014 700, 20px) for numerical clarity. On hover, a `0 4px 16px rgba(0,0,0,0.12)` shadow lifts the card slightly without any scale transform — movement stays subtle.

**Badges** snap to the top-left corner of the card image area. `badge-sale` uses `{colors.sale}` red, `badge-new` uses `{colors.primary}` orange, and `badge-bestseller` uses `{colors.ink}` black — each with white uppercase text at 11px, 4px radius, tight 4px/8px padding. Only one badge displays per card.

### Hero Sections

**`hero-dark`** — Full-viewport-width block with `{colors.canvas-dark}` background, minimum 560px height. Headlines render in CheddarGothicSans at `{typography.display-xl}` (56px, uppercase, 1.05 leading) — the gothic letterforms fill horizontal space aggressively, making even short copy feel monumental. Body text below in `{typography.body-lg}` (Acumin Pro 18px, 1.6 leading) provides the breathing room the display type refuses to. CTA button sits below with `{spacing.lg}` gap.

**`hero-split`** — A 50/50 layout with `{colors.surface-charcoal}` on the text half and a full-bleed product photo on the right. Title drops to `{typography.display-lg}` (40px) to fit the narrower text column. Used primarily for new product launches and seasonal campaigns.

### Recipe & Content Cards

**`recipe-card`** — White background with `{rounded.sm}` (8px) corners and a `{colors.hairline-soft}` border. Image fills the top with matching top-radius. Title in `{typography.title-md}` (20px, 600 weight), metadata (cook time, difficulty) in `{typography.caption}` at muted gray. Padding at `{spacing.base}` (16px) on all text-content sides.

### Feature & Comparison

**`feature-icon-card`** — Uses `{colors.surface-warm}` (#ffe6da) as background — the only warm-toned surface in the system. Icon in `{colors.primary}` orange, title in `{typography.title-sm}`, body in `{typography.body-sm}`. The peach background creates a temperature-appropriate warmth for cards explaining griddle features (heat zones, grease management, BTU output).

**`comparison-table`** — Clean horizontal-ruled table with `{colors.surface-soft}` header row. Headers use `{typography.title-sm}`, body cells use `{typography.body-sm}`. Outer container gets `{rounded.sm}` and a `{colors.hairline}` border. Used extensively on product pages to compare griddle sizes and included accessories.

### Search

**`search-bar`** — A pill-shaped (`{rounded.full}`) input sitting in the nav area, 48px tall with `{colors.surface-soft}` background and `{colors.hairline}` border. On focus, border strengthens to 2px `{colors.primary}` with a subtle orange box-shadow glow. Placeholder text in `{colors.muted}`.

### Footer

**`footer`** — Deep black `{colors.ink-deep}` (#111111) background, slightly darker than the nav-dark and hero-dark surfaces to create visual termination. Section headings in `{typography.condensed-label}` (Acumin Pro Condensed, uppercase, 14px), links in `{typography.body-sm}` with `{colors.on-dark}` white text. Generous `{spacing.section}` (64px) vertical padding separates footer from content above.

### Rating Stars

**`rating-stars`** — Filled stars use `{colors.primary}` orange rather than the typical gold/yellow, reinforcing brand color saturation even in micro-UI. Empty stars use `{colors.hairline}` gray. Displayed at 16px inline with product titles.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero headlines drop to `{typography.display-md}` (32px); product grid shifts to 2-col; hero-split stacks vertically (image on top); comparison table scrolls horizontally; footer columns stack single-file |
| Tablet | 744–1128px | Product grid at 3-col; hero-split maintains 50/50 but at reduced image height; nav shows primary links, overflow into hamburger; mega-menu renders as accordion |
| Desktop | 1128–1440px | Full nav with all links visible; product grid at 4-col; hero sections at full 560px min-height; mega-menu drops as overlay panel; comparison table fully visible |
| Wide | > 1440px | Content max-width caps at 1440px, centered; side margins grow symmetrically; hero images may extend to viewport edge while text stays within max-width container |

### Touch Targets

- All interactive elements maintain minimum 44px tap targets on mobile
- Buttons increase to 52px height on viewports below 744px
- Badge tap areas extend 8px beyond visible badge boundary via padding
- Mega-menu links get 44px row height on tablet accordion view
- Search bar expands to full-width below nav on mobile (not inline)

### Collapsing Strategy

- Navigation: full horizontal links → priority links + overflow hamburger → full hamburger with slide-out drawer
- Product grid: 4-col → 3-col → 2-col (never single-column for product grids)
- Hero-split: side-by-side → stacked (image top, text bottom)
- Comparison table: full table → horizontally scrollable with sticky first column
- Footer: 4-column grid → 2-column → single-column accordion with expandable sections
- Feature-icon-cards: 3-across → 2-across → single-column stack

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact CheddarGothicSans font-weight values could not be confirmed (only one weight appears available; 700 is assumed based on rendering)
- Transition/animation timing functions and durations are not extractable from static analysis — hover states likely use 150–200ms ease but this is inferred
- Specific Acumin Pro variable-font axis settings (if using the variable version) are not determinable from CSS extraction
- Mobile nav drawer animation direction (left vs right slide) and overlay scrim opacity are not confirmed
- Exact box-shadow values on product-card hover are approximated; the site may use a custom shadow stack
- Inter font usage context is unclear — may be a Shopify admin/checkout fallback rather than storefront-facing
- The role of `acumin-pro-wide` and `acumin-pro-extra-condensed` variants could not be pinpointed to specific components
- Icon system (line weight, size grid, filled vs outlined) is not extractable without component-level inspection
- Dark/light mode toggle behavior (if any) beyond the section-level canvas switching is not confirmed
