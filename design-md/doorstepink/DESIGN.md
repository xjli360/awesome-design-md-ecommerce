---
version: alpha
name: "DoorStepInk"
source_url: "https://doorstepink.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The most literal brand move in the ink category — DoorStepInk built its chromatic identity around the actual colors that come out of printer cartridges. The primaries, #ba0e0e crimson, #e32e00 signal red, and #971e00 deep maroon, read as a tube of pigment squeezed onto a palette rather than a committee-approved corporate hue. More revealing is the accent layer: #ffcb67 amber-yellow, #ed66b2 magenta-pink, #86469c violet, and #1b6109 forest green appear in the extracted palette like a CMYK ink set converted into UI tokens, each mapping to a cartridge color the site actually sells. The canvas sits at near-white #f8f8f8 and a cooler #f3f3f8, with card surfaces staying white against charcoal ink text at #292929 — a high-contrast technical-catalog register rather than a lifestyle brand affect. Type runs Poppins for display and headings and Nunito for running text and UI labels, both geometric and slightly rounded in letterform, a combination that delivers a friendly-technical hybrid voice matching the blunt "Made in the USA" directness in the page title. Rounding stays moderate: buttons and badges at {rounded.sm} or {rounded.md}, never pill-shaped, keeping the brand in utilitarian rather than premium territory. Navigation leans dark — near-black #262626 surfaces carry the header, grounding crimson CTAs against a neutral that reads like an ink-stained workbench. Pricing is the brand's second language; large Poppins 700 numerals foreground a value-for-money message over aspirational mystique. The "Made in USA" signal is structural — wired into badge components and trust-band layout — and the entire system is optimized to move cartridge SKUs efficiently, not to cultivate a mood.

colors:
  primary: "#ba0e0e"
  primary-bright: "#e32e00"
  primary-active: "#971e00"
  primary-deep: "#730909"
  primary-disabled: "#f46d6d"
  fire-red: "#fc3300"
  usa-red: "#990000"
  ink: "#292929"
  ink-deep: "#030303"
  body: "#504d45"
  muted: "#7b7c81"
  muted-soft: "#626367"
  hairline: "#e6e6e6"
  hairline-soft: "#bfbebe"
  canvas: "#f8f8f8"
  canvas-cool: "#f3f3f8"
  surface-card: "#ffffff"
  surface-dark: "#262626"
  surface-deep: "#030303"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  ink-yellow: "#ffcb67"
  ink-magenta: "#ed66b2"
  ink-violet: "#86469c"
  ink-green: "#1b6109"

typography:
  display-xl:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  body-md:
    fontFamily: "'Nunito', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  label-sm:
    fontFamily: "'Nunito', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Nunito', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  sku-label:
    fontFamily: "'Nunito', monospace, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px

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
    padding: 12px 24px
    height: 46px
    hover:
      backgroundColor: "{colors.primary-active}"
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
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 46px
    hover:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  button-add-to-cart:
    backgroundColor: "{colors.primary-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 48px
    hover:
      backgroundColor: "{colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-logo:
    textColor: "{colors.on-dark}"
    typography: "{typography.display-sm}"
  nav-dropdown:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    shadow: "0 2px 8px rgba(0,0,0,0.06)"
    imageAspect: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  product-card-sku:
    typography: "{typography.sku-label}"
    textColor: "{colors.muted}"
  product-badge-usa:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-badge-compatible:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  cartridge-color-swatch:
    width: 20px
    height: 20px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  ink-category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 16px
  ink-category-tab-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 16px
    hover:
      borderColor: "{colors.primary}"
      textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xxl}"
    minHeight: 360px
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.hairline}"
  hero-cta:
    backgroundColor: "{colors.primary-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  printer-search-bar:
    backgroundColor: "{colors.surface-card}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
    height: 52px
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
  printer-search-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  trust-badge:
    backgroundColor: "{colors.canvas-cool}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.primary}"
  trust-badge-label:
    typography: "{typography.label-sm}"
    textColor: "{colors.body}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: "/"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  pagination:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    activeColor: "{colors.primary}"
    activeBg: "{colors.canvas-cool}"
    rounded: "{rounded.xs}"

## Components

### Buttons

**`button-primary`** — Crimson #ba0e0e background with white Poppins 600 text at 15px, height 46px, {rounded.sm} corners. Hover state deepens to `{colors.primary-active}` (#971e00); the disabled state substitutes the muted-pink `{colors.primary-disabled}` (#f46d6d), which keeps the hue family intact without false urgency. This button carries account-level and navigation-level actions where the tone is transactional but not cart-critical.

**`button-add-to-cart`** — One step brighter than `button-primary` at `{colors.primary-bright}` (#e32e00), 48px height to guarantee thumb accessibility. The intentional brightness delta between add-to-cart and the standard primary creates a visual hierarchy — two degrees of red urgency — without introducing a new hue family.

**`button-secondary`** — White fill with a 2px crimson border and crimson label text; on hover, fully inverts to crimson fill with white text. Paired with `button-add-to-cart` on product pages to give a lower-commitment path (e.g., "View Details" or "Compare") without visual noise.

**`button-ghost`** — Transparent background, `{colors.ink}` text, {rounded.xs}. Used for clear-filter links, modal dismissals, and read-more anchors where visual weight would compete with product content.

### Product Card

**`product-card`** — White surface on {rounded.md} with a 1px hairline border and a restrained `0 2px 8px` shadow. The 1:1 image cell at top is followed by a printer-compatibility string in `{typography.sku-label}` at muted gray, the product title in `{typography.title-sm}`, a crimson price in `{typography.price-display}`, and a full-width `button-add-to-cart` pinned to the card bottom. The badge row — `product-badge-usa` in crimson and `product-badge-compatible` in near-black — sits between the image and title, making manufacturing provenance and printer fit the first text the eye lands on.

**`product-badge-usa`** — Uppercase "MADE IN USA" in Poppins 700 at 11px on a crimson chip with {rounded.xs}. This is not decorative: it appears on nearly every SKU card as a primary differentiator and is treated as structural content, not a promotional overlay.

**`product-badge-compatible`** — Near-black `{colors.ink}` background badge carrying the printer model string (e.g., "For HP 64XL"). Adjacent to the USA badge in a horizontal row; the dark chip creates contrast so the two badges read as distinct information layers rather than a single block.

### Navigation

**`nav-bar`** — Deep charcoal #262626 at 64px height with no bottom border. The dark bar frames the white product canvas from above and makes the crimson CTAs — account, cart, promotions — read as voltage against a neutral field. Logo in `{typography.display-sm}` white anchors left; a compact search input sits embedded in the bar on desktop, giving the printer-model lookup persistent access without a separate search page.

**`nav-dropdown`** — Inherits the dark surface in matching #262626. Category sub-menus (Black Cartridges, Color Cartridges, Combo Packs, High-Yield) use `{typography.body-sm}` white text with hairline dividers. The dark dropdown extends the nav-bar's tone rather than breaking to a light popover, maintaining the dark-bracket framing that wraps the white canvas.

### Printer Search

**`printer-search-bar`** — A 52px compound control: the text input carries a 2px primary-crimson border signaling that "find your printer model" is the entry action, not a secondary utility. The {rounded.md} shape is softer than standard inputs. The paired `{printer-search-button}` in crimson attaches flush to the right edge, forming a single control. The placeholder leading with "printer model" trains the user's search behavior toward the SKU-lookup flow rather than generic keyword search.

### Hero

**`hero-banner`** — Full-bleed near-black `{colors.surface-dark}` with a 360px minimum height. Headline in `{typography.display-xl}` white; subhead in `{typography.body-md}` at `{colors.hairline}` (#e6e6e6), dimmed enough to step back from the headline but fully legible against dark. The `{hero-cta}` uses `{colors.primary-bright}` (#e32e00) to pop against the dark field with the same brightness logic as the add-to-cart button — the single brightest red reserved for the highest-intent action in each viewport zone.

### Ink Color Swatches and Category Tabs

**`cartridge-color-swatch`** — 20px circular chip with a 2px hairline border used in color-variant selectors on product pages. The four ink-accent tokens — `{colors.ink-yellow}` (#ffcb67), `{colors.ink-magenta}` (#ed66b2), `{colors.ink-violet}` (#86469c), `{colors.ink-green}` (#1b6109) — map directly to color-cartridge product lines, turning functional product taxonomy into the brand's secondary palette system.

**`ink-category-tab-active`** / **`ink-category-tab-inactive`** — Horizontal filter tabs for Black / Color / Photo / High-Yield SKU browsing. Active fills with `{colors.primary}` and white text; inactive shows hairline border with muted `{colors.body}` label. Hover on inactive shifts border and text to crimson — the brand hue intrudes at every interaction point, keeping the color signature consistent across the catalog-filtering experience.

### Trust Band

**`trust-badge`** — Light `{colors.canvas-cool}` (#f3f3f8) card with hairline border and a crimson icon, rendered in a 4-up horizontal band covering Made in USA / Fast Shipping / Satisfaction Guarantee / Quality Tested. The cool-white background separates the band from the product grid without a new color introduction. `{trust-badge-label}` in `{typography.label-sm}` runs below each icon in `{colors.body}`, keeping the signal calm and factual.

### Footer

**`footer`** — Near-black `{colors.surface-deep}` (#030303) background, mirroring the nav-bar's dark anchor and closing the page's dark-bracket framing around the white product canvas. Column headings in `{typography.title-sm}` white; body links in `{colors.hairline}` (#e6e6e6) at `{typography.body-sm}`. The four columns cover Shop, Support, Company, and Legal at desktop width.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; printer-search-bar goes full-width below logo row; trust badge band stacks 2×2; hero drops to 280px min-height with text-only (no side image) |
| Tablet | 744–1128px | 2-column product grid; nav shows logo + search + cart icon, category links hidden behind hamburger; hero enables side-by-side text and image layout at 50/50 split |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with all category links visible; printer-search bar centered at 640px max-width; product filters visible in left-rail sidebar |
| Wide | > 1440px | Grid max-width caps at 1320px with auto side margins; hero text column fixed at 560px left; font sizes hold at defined scales with no super-display scaling |

### Touch Targets

- `button-add-to-cart` at 48px height meets the 44px minimum on all breakpoints
- `nav-bar` drawer links on mobile minimum 48px row height per item
- `cartridge-color-swatch` at 20px desktop scales to 28px on mobile
- `ink-category-tab-active` / inactive minimum 80px wide with 8px gap; on mobile, tabs scroll horizontally rather than wrap to prevent layout compression

### Collapsing Strategy

- Navigation collapses left-to-right: secondary category links hide first, then account label (icon only remains), leaving logo + search + cart as the mobile core
- Product filters move from a left-rail sidebar at desktop to a bottom-sheet modal on mobile, triggered by a "Filter" ghost button above the grid
- Trust badge band collapses from 4-column horizontal to 2×2 grid at tablet, then single-column at mobile
- Footer columns collapse from 4-up to 2-up at tablet and single-column at mobile, with accordion expand on each section heading

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom icon set or glyph library was extractable; icon style (filled, outlined, stroke weight) is unknown and assumed to follow Shopify theme defaults
- Font weight subset loaded for Poppins and Nunito is unconfirmed; intermediate weights (500) may not be available in the active subset, so designs using weight 500 should have a 600 fallback specified
- Exact nav-bar height (64px) is estimated; no rendered DOM measurements were available
- Animation and transition durations not detected — hover transitions assumed at 150ms ease throughout
- Grid gutter values (estimated at 16px / 24px) not confirmed from static extraction
- Shopify theme template name not identified; block and section schema follow Shopify 2.0 conventions by assumption
- The purple `{colors.ink-violet}` (#86469c) and pink `{colors.ink-magenta}` (#ed66b2) appear in extraction but their exact UI roles — cartridge swatches, promotional banner accents, or tag colors — could not be confirmed without rendered page access
- No subscription, yield-tier, or multipack upsell UI components were extractable; these are inferred from the product category and common DTC ink patterns
- Serif font (Times) detected in the font-family stack but no usage context identified; may be a fallback artifact in a Shopify liquid template rather than intentional brand typography
