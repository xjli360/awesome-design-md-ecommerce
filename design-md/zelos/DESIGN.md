---
version: alpha
name: "Zelos"
source_url: "https://www.zeloswatches.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The dense cluster of orange variants — #f48120 through #f89f20 — saturating sale callouts and accent elements on zeloswatches.com is less a marketing choice than a dial reference: Zelos builds tool watches with orange-tipped hands and lume indices, and the site palette reads as continuous with the product. Against the near-black substrate that dominates the primary canvas (#1c1b1b, #121212), electric blue (#006fcf) claims every primary CTA and navigation interaction — sharp enough to read at a glance, like a watch's lume-filled bezel markings snapping into focus in the dark. The Jost geometric sans-serif carries all headings with weight that lands between utilitarian and bold, closer to watch-catalog typography than editorial fashion, while Karla handles body copy and specification text with a slightly warmer humanist finish that keeps long technical descriptions legible without stiffness.

  The brand's identity is shaped by its "dares" tagline and a Singapore-based direct-to-consumer model: limited production runs, no retail markup, and a product page that leans into the gear-head's appetite for precise specifications. Button labels and badge text are uppercase Jost with generous letter spacing — the stamped-caseback aesthetic is intentional. Product cards sit on a cool near-white surface ({colors.surface-soft}), while the main hero drops to a deep dark canvas ({colors.surface-dark}) for product photography, echoing the shift between a lit dial and a dark wrist.

  Red (#c8232c) operates as a warning register: sold-out states, limited-inventory counters, price-drop callouts — borrowing from the red zone of a tachymeter. Warm sand (#c8b494) appears in lifestyle photography and material reference imagery but never in interactive elements. Rounded corners are near-absent — {rounded.xs} (2px) on cards and inputs, {rounded.none} on badges — reinforcing a machine-tolerance aesthetic over the soft-corner friendliness of mainstream Shopify templates. There are no cursive details, no serif ornaments, no gradient fills on primary surfaces: the interface is precision-industrial from top nav to footer, with a 2px orange border at the very bottom as the brand's one voltage signature.

colors:
  primary: "#006fcf"
  primary-active: "#0056a8"
  primary-disabled: "#a3c9ef"
  ink: "#1c1b1b"
  body: "#363636"
  muted: "#6a6a6a"
  muted-faint: "#777777"
  hairline: "#dedede"
  hairline-soft: "#dbdbdb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  surface-dark-raised: "#231f20"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-orange: "#f48120"
  accent-red: "#c8232c"
  accent-amber: "#f6a429"
  warm-tan: "#c8b494"
  muted-blue: "#4469af"
  deep-navy: "#1a1a2e"
  mid-dark: "#5a5b5b"
  footer-text: "#bfbfbf"

typography:
  display-xl:
    fontFamily: "'Jost', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Karla', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Karla', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Karla', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Jost', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  price-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  badge-label:
    fontFamily: "'Jost', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  spec-mono:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  logo-display:
    fontFamily: "'Jost', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 2px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 12px
  xl: 24px
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-ghost-white:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.on-dark}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 52px
    width: 100%
  button-sold-out:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 52px
    width: 100%
    cursor: not-allowed
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-faint}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.logo-display}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.10)"
    borderBottom: none
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    accentColor: "{colors.accent-orange}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    imageRounded: "{rounded.none}"
    padding: "{spacing.base}"
    badgeOffset: 8px
    hoverEffect: "image scale 1.03, 300ms ease"
    captionColor: "{colors.muted}"
  badge-limited:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-sold-out:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    accentBorder: "3px solid {colors.accent-orange}"
    padding: "96px {spacing.xl}"
    ctaRow: "button-primary + button-ghost-white, gap 16px"
  hero-split:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    layout: "50/50 image-left text-right"
    padding: "80px {spacing.xl}"
  collection-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-sm}"
    accentColor: "{colors.accent-orange}"
    padding: "60px {spacing.xl}"
    layout: "full-bleed background image with overlaid text block"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-mono}"
    border: "1px solid {colors.hairline}"
    rowBorderBottom: "1px solid {colors.hairline-soft}"
    rowPadding: "10px {spacing.base}"
  model-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    height: 40px
  inventory-counter:
    textColor: "{colors.accent-red}"
    typography: "{typography.badge-label}"
    dotSize: 6px
    dotColor: "{colors.accent-red}"
    threshold: 5
  collection-grid:
    columns: 3
    gap: "{spacing.lg}"
    cardRounded: "{rounded.none}"
    backgroundColor: "{colors.canvas}"
  newsletter-bar:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    accentColor: "{colors.accent-orange}"
    inputBackgroundColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.xl}"
    accentUnderline: "2px solid {colors.accent-orange}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    inputBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    scrim: "rgba(28,27,27,0.6)"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.footer-text}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.canvas}"
    sectionTitleTypography: "{typography.badge-label}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "2px solid {colors.accent-orange}"

## Components

### Buttons

**`button-primary`** — Sharp-cornered (`{rounded.none}`) electric-blue block at 48px height, set in uppercase Jost 14px with 0.8px letter spacing. Hover darkens to `{colors.primary-active}` (#0056a8) over a 200ms ease transition; disabled state bleaches to `{colors.primary-disabled}` with a blocked cursor and no hover animation. Width is content-driven on desktop layouts; on mobile product pages it stretches full-width.

**`button-secondary`** — Transparent fill with a 1.5px solid `{colors.ink}` border, same uppercase Jost spec as primary. Sits alongside `button-primary` in two-CTA pairs (e.g., "Notify Me" + "View Collection"). Hover fills to `{colors.surface-soft}` over 200ms.

**`button-ghost-white`** — Same proportions and uppercase typography as secondary but inverts for dark backgrounds — white border, white text — used in `hero-dark` sections and dark modals. Hover fills to a 15% white overlay.

**`button-add-to-cart`** — Full-width, 52px tall to anchor the product page. Always renders in `{colors.primary}` blue on in-stock items. When inventory reaches zero, the entire component swaps atomically to `button-sold-out` — gray fill, muted text, `cursor: not-allowed`, no animation.

### Navigation

**`nav-bar`** — 64px white bar with a 1px `{colors.hairline}` bottom border. The logo wordmark is uppercase Jost 22px/700 with 2px letter spacing, left-aligned. Desktop links center between logo and icon cluster (search, account, cart bag). On scroll, the bottom border fades and `nav-bar-scrolled` applies a subtle `box-shadow` to maintain separation. The announcement bar above carries shipping thresholds and discount codes in white caption text with orange-highlighted values.

### Product Cards

**`product-card`** — Zero border radius, portrait image aspect, with a 1.03× scale on the image over 300ms ease on hover — the only motion on the card. Title in Jost 16px/600, price in Jost 18px/700 immediately below. Secondary metadata (case diameter, material) renders in Karla 13px `{colors.muted}`. Badges stack at the top-left corner of the image with 8px offset; multiple badges stack vertically with 4px gap.

### Badges

**`badge-limited`** — Orange (#f48120) stamp with white uppercase Jost 10px, 1px tracking, no radius. This is the only orange element that overlaps product photography directly.

**`badge-sold-out`** — Red (#c8232c) variant of the same stamp; applied simultaneously with the `button-sold-out` swap on the product page.

**`badge-new`** — Blue (#006fcf) variant, used for the first 30 days after a watch launches.

**`badge-sale`** — Red, identical to `badge-sold-out` in structure but paired with a struck-through compare-at price in `{colors.muted}` next to the sale price.

### Spec Table

**`spec-table`** — Two-column table on a `{colors.surface-soft}` background with 1px `{colors.hairline-soft}` row dividers. Left column carries muted Karla 13px labels (Water Resistance, Case Diameter, Movement, Lug Width); right column renders values in monospace 13px for a technical-readout feel. Used below the product image on all watch PDPs.

### Model Selector

**`model-selector`** — Rectangular label chips with a 1px `{colors.hairline}` border at rest; switches to 2px `{colors.ink}` border when selected. No swatch fills — dial-color and strap variants are label-only, keeping the UI language textual rather than decorative. Minimum 40px height for tap comfort.

### Heroes

**`hero-dark`** — Full-viewport dark canvas (`{colors.surface-dark}`) with large watch photography centered or offset-right. Heading in `{typography.display-xl}` white, optionally framed by a 3px orange left-border accent on the text block. CTA row is always `button-primary` + `button-ghost-white` side by side with 16px gap.

**`hero-split`** — Light `{colors.surface-soft}` section, 50/50 split with product image left and headline plus CTA right. Heading in `{typography.display-md}`, body copy in Karla 16px. Used for named-collection callouts below the main hero.

**`collection-banner`** — Full-bleed dark image section with an overlaid text block. Heading in `{typography.display-sm}`, with an orange `{colors.accent-orange}` accent line above or beside the headline. Typically introduces a product family (dive, field, dress) within the collection page.

### Inventory Counter

**`inventory-counter`** — Renders "Only X left" above the add-to-cart button when stock falls to five units or fewer. Red dot (6px) prefixes the label in `{colors.accent-red}` `{typography.badge-label}`. Disappears when stock is comfortably above threshold.

### Newsletter Bar

**`newsletter-bar`** — Deep navy (#1a1a2e) horizontal band with centered heading, a 2px orange underline accent on the section title, and an email input + `button-primary` arranged side by side on desktop. Stacks vertically on mobile with full-width input and button.

### Footer

**`footer`** — Near-black canvas (`{colors.ink}`) with a 2px `{colors.accent-orange}` top border — the orange re-appears here as a brand closing signature after being used as an energizer throughout the page. Four-column link grid uses `{typography.badge-label}` (uppercase Jost, 10px) for section headers and `{typography.body-sm}` for links at `{colors.hairline-soft}`, brightening to `{colors.canvas}` on hover.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen drawer; add-to-cart becomes sticky bottom bar at 52px with safe-area-inset-bottom padding; hero heading drops to `display-sm`; announcement bar becomes a scrolling ticker |
| Tablet | 744–1128px | Two-column product grid; nav retains logo and icon cluster but moves category links into hamburger drawer; hero-split stacks portrait image above text |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav; hero-split in 50/50 layout; spec-table shown in sidebar alongside product imagery |
| Wide | > 1440px | Max-width container ~1400px centered; product grid 3–4 columns; hero padding increases; footer columns expand to five |

### Touch Targets

- Nav icon buttons (search, account, cart) minimum 44×44px tap area
- Model selector chips minimum 40px height on touch devices
- Sticky add-to-cart bar is full-width 52px, always above the keyboard on iOS with safe-area padding
- Badge chips in collection filters minimum 36px height on mobile

### Collapsing Strategy

- Product grid collapses 3 → 2 → 1 column as viewport narrows
- Spec table stays two-column at all sizes; labels truncate with ellipsis below 320px
- Footer collapses to two columns at tablet, single column at mobile with accordion section headings (Jost badge-label as accordion trigger)
- Hero-dark stays full-viewport height at all sizes; text block shifts to bottom-anchored overlay on mobile
- Newsletter bar stacks input above button on mobile; input goes full-width

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values extracted from site CSS; near-zero radius inferred from the tool-watch industrial aesthetic and Shopify theme visual scan
- Animation easing curves and durations not extractable from static HTML; 200–300ms ease values are category inferences
- Exact sticky-nav behavior on mobile scroll not confirmed; box-shadow treatment inferred
- Logo mark (whether a wordmark only or paired with an icon mark) not confirmed from extraction; Jost uppercase treatment inferred from typography stack and page-title casing
- Cart drawer and quick-add modal designs not seen in static extraction
- Orange gradient cluster (#f48120–#f89f20) may be a single linear gradient on sale banners rather than discrete palette tokens; exact gradient stops and direction not confirmed
- Karla font weight usage not specified in extracted stack; 400 for body and 700 for emphasis assumed
- Whether a dark-mode toggle or full alternate dark theme exists is not confirmed; dark sections appear to be per-section overrides rather than a global theme switch
- Social proof elements (review stars, verified buyer labels, aggregate rating display) not extracted; color and typography unconfirmed
