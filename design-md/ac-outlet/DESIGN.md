---
version: alpha
name: "The AC Outlet"
source_url: "https://www.theacoutlet.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The AC Outlet's palette does something unexpected for wholesale HVAC: olive-khaki (#929457, #62623a) anchors the brand character while a coral-red (#db5757) handles every CTA — no safety orange, no construction yellow, just an earthy warmth that reads as jobsite-credible to contractors who recognize Goodman model strings on sight. The deep slate-navy (#394962) frames the navigation and structural chrome, with a darker olive topStripe carrying wholesale account status and freight messaging above the primary nav band — a two-tier top chrome that signals B2B identity before any product appears. The main canvas leans into cool industrial gray tones (#c6c7c9, #929495) rather than the clean white of consumer retail, and the full extracted palette — cool blue-grays (#677a82, #96a4a9), warm taupes (#938888, #c6b7b7), and teal-grays (#687979) — suggests a system built from careful component layering rather than a single dominant brand hue. DM Sans carries the entire typographic load without family changes: its geometric-but-approachable construction handles dense model-number strings (Goodman GSX14024, ARUF25B14) at tracked uppercase in product cards and large display headings with equal composure. Rounded corners stay deliberately minimal — {rounded.xs} and {rounded.sm} throughout — reinforcing a transactional pro interface rather than a consumer one; pill shapes and soft shadows are absent entirely. The coral accent (#db5757) is the sole warm-voltage moment in an otherwise cool palette, placing Add-to-Cart and Get Quote buttons in immediate relief without requiring additional visual weight. Trust signals — Goodman authorized-dealer status, wholesale account gates, freight-shipping thresholds, and net-30 availability — occupy prime real estate in the olive topStripe and footer, reflecting a B2B repeat-buyer flow. Search and model-number lookup dominate the UX priority queue, with category filters (Split Systems, Package Units, Air Handlers, Thermostats, Refrigerants) as the secondary path for the contractor who already knows which GSX-series unit they need.

colors:
  primary: "#db5757"
  primary-active: "#c04040"
  primary-disabled: "#edacac"
  nav: "#394962"
  nav-hover: "#6d788b"
  olive: "#929457"
  olive-dark: "#62623a"
  olive-light: "#c6c775"
  ink: "#303030"
  body: "#626263"
  muted: "#929495"
  muted-warm: "#938888"
  hairline: "#cfcfcf"
  hairline-cool: "#c6c7c9"
  canvas: "#ffffff"
  surface-soft: "#d0d6d9"
  surface-card: "#ffffff"
  surface-industrial: "#c6c7c9"
  teal-gray: "#687979"
  on-primary: "#ffffff"
  on-nav: "#ffffff"

typography:
  display-xl:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  model-number:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-msrp:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    textDecoration: line-through
  button-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  tag:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        textColor: "{colors.on-primary}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.nav}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.nav}"
    states:
      hover:
        borderColor: "{colors.primary}"
        textColor: "{colors.primary}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
    states:
      focus:
        borderColor: "{colors.nav}"

  nav-bar:
    backgroundColor: "{colors.nav}"
    textColor: "{colors.on-nav}"
    typography: "{typography.nav-link}"
    height: 60px
    topStripe:
      backgroundColor: "{colors.olive-dark}"
      textColor: "{colors.on-nav}"
      typography: "{typography.caption}"
      height: 32px
      padding: 0 {spacing.base}

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspect: "4/3"
    modelNumber:
      typography: "{typography.model-number}"
      textColor: "{colors.muted}"
    title:
      typography: "{typography.title-md}"
      textColor: "{colors.ink}"
    price:
      typography: "{typography.price-display}"
      textColor: "{colors.ink}"
    msrpStrikethrough:
      typography: "{typography.price-msrp}"
      textColor: "{colors.muted}"
    ctaButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-md}"
      rounded: "{rounded.xs}"
      width: 100%
    badge:
      position: top-left
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.badge}"
      rounded: "{rounded.none}"
      padding: 3px 8px

  hero-banner:
    backgroundColor: "{colors.nav}"
    textColor: "{colors.on-nav}"
    accentColor: "{colors.olive}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-md}"
    minHeight: 400px
    padding: "{spacing.xxl} {spacing.section}"
    ctaButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-md}"
      rounded: "{rounded.xs}"
      padding: 12px 28px

  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 48px
    border: "1px solid {colors.hairline-cool}"
    placeholderColor: "{colors.muted}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-md}"
      rounded: "{rounded.xs}"
      padding: 0 20px
    states:
      focus:
        borderColor: "{colors.primary}"

  category-chip:
    backgroundColor: "{colors.surface-industrial}"
    textColor: "{colors.nav}"
    typography: "{typography.tag}"
    rounded: "{rounded.xs}"
    padding: 6px 14px
    states:
      active:
        backgroundColor: "{colors.nav}"
        textColor: "{colors.on-nav}"
      hover:
        backgroundColor: "{colors.nav-hover}"
        textColor: "{colors.on-nav}"

  brand-logo-strip:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.xl} 0"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    logoFilter: grayscale(100%)
    logoFilterHover: grayscale(0%)
    gap: "{spacing.xxl}"

  product-spec-table:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    headerRow:
      backgroundColor: "{colors.nav}"
      textColor: "{colors.on-nav}"
      typography: "{typography.title-md}"
      padding: "{spacing.sm} {spacing.base}"
    dataRow:
      typography: "{typography.body-sm}"
      textColor: "{colors.ink}"
      padding: "{spacing.sm} {spacing.base}"
    alternateRow:
      backgroundColor: "{colors.surface-soft}"
    labelCell:
      textColor: "{colors.muted}"
      fontWeight: 500

  account-gate-banner:
    backgroundColor: "{colors.olive-dark}"
    textColor: "{colors.on-nav}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    ctaLink:
      textColor: "{colors.olive-light}"
      typography: "{typography.button-sm}"
      textDecoration: underline

  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.nav}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline-cool}"
    iconColor: "{colors.olive}"

  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px

  footer:
    backgroundColor: "{colors.nav}"
    textColor: "{colors.on-nav}"
    linkColor: "{colors.surface-soft}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — Coral-red (`{colors.primary}` #db5757) fill with white text at `{typography.button-md}` (600 weight), `{rounded.xs}` radius, and 44px height. Hover darkens to `{colors.primary-active}` (#c04040); disabled washes to `{colors.primary-disabled}` (#edacac). This is the single high-voltage CTA across Add-to-Cart, Request Quote, and search submission throughout the site.

**`button-secondary`** — White canvas with `{colors.nav}` navy border and navy text. On hover, both border and text shift to `{colors.primary}` coral, creating a warm crossover that reinforces the palette tension between navy structure and coral action. Used for secondary choices alongside a primary: View Full Specs, Save to List, Compare.

**`button-ghost`** — Transparent background with `{colors.primary}` coral text at `{typography.button-sm}`. Reserved for inline text-adjacent links like "See all Goodman models →" and pagination where a filled button would crowd the grid.

### Search Bar
**`search-bar`** — Full-width 48px input with a self-contained coral submit button on the right edge. The placeholder defaults to model-number-oriented language, reflecting that most traffic arrives knowing the SKU. Border highlights to `{colors.primary}` on focus; no radius change on focus, consistent with the site's sharp-corner system.

### Navigation
**`nav-bar`** — Two-tier top chrome: a 32px `{colors.olive-dark}` (#62623a) topStripe carries wholesale account status, freight thresholds, and promotional copy in `{typography.caption}` white; the main 60px `{colors.nav}` navy band below holds category dropdowns at `{typography.nav-link}`. This topStripe is the primary mechanism for communicating wholesale-vs-retail context on first glance. Dropdown mega-menus on desktop organize by equipment category (Split Systems, Package Units, Air Handlers, Accessories, Brands).

### Product Card
**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.xs}` corner. Model number renders above the title in `{typography.model-number}` (uppercase, tracked, `{colors.muted}`), a deliberate pro-market signal that part-number legibility matters more than marketing copy. Price at `{typography.price-display}` with MSRP strikethrough in `{colors.muted}` when discounted. A square `{rounded.none}` coral badge snaps flush to the top-left corner for sale and clearance states. CTA button runs full-width at the card bottom.

### Hero Banner
**`hero-banner`** — Full-bleed `{colors.nav}` navy with `{colors.olive}` (#929457) olive as the accent color for underlines, borders, or decorative rule elements. Headlines at `{typography.display-xl}` white; subheadings at `{typography.title-lg}`. Minimum 400px height on desktop. Used for authorized-wholesaler brand features (Goodman, Daikin, Amana) and seasonal demand campaigns (cooling season, heat pump incentives).

### Category Chips
**`category-chip`** — `{colors.surface-industrial}` cool-gray fill with `{colors.nav}` navy text at `{typography.tag}`. Active state inverts to solid navy with white text; hover uses `{colors.nav-hover}` (#6d788b) as the intermediate step. Chips appear in a horizontal scrolling filter strip above the product grid on category pages: Split Systems, Package Units, Air Handlers, Thermostats, Refrigerants, Tools & Accessories.

### Brand Logo Strip
**`brand-logo-strip`** — A `{colors.surface-soft}` band between the hero and product grid displaying partner brand logos (Goodman, Daikin, Amana) in grayscale, revealing full color on hover. Top and bottom 1px `{colors.hairline}` borders treat it as structural shelf rather than decorative flourish. Communicates authorized wholesale relationships at a glance.

### Product Spec Table
**`product-spec-table`** — Dense technical table used on PDPs for SEER ratings, BTU capacity, refrigerant type (R-410A, R-32), voltage, amperage, and dimensions. Header row in `{colors.nav}` navy with white `{typography.title-md}`; data rows alternate between white and `{colors.surface-soft}` for scannability without colored row fills. Label cells use `{colors.muted}` to visually subordinate the attribute name to the value. Horizontal scroll container activates below 1128px rather than reflowing rows.

### Account Gate Banner
**`account-gate-banner`** — Full-width `{colors.olive-dark}` (#62623a) strip carrying wholesale pricing gate copy ("Log in to view contractor pricing and net-30 terms") in white `{typography.body-sm}`. The inline CTA link renders in `{colors.olive-light}` (#c6c775), a pale green-yellow that reads against dark olive without reaching for the coral primary. Appears just below the nav-bar and disappears once the user is authenticated into a wholesale account.

### Trust Badges
**`trust-badge`** — Small capsule with `{colors.surface-soft}` background, `{colors.olive}` icon, and `{typography.caption}` text in `{colors.nav}`. Displayed in a horizontal row below the main search bar: "Authorized Goodman Dealer," "Free Freight on Orders Over $X," "Net-30 Available," "Ships from U.S. Warehouse." The olive icon color connects these components to the brand accent layer without activating the coral CTA weight.

### Footer
**`footer`** — Full-bleed `{colors.nav}` navy with a 3px `{colors.primary}` coral top border as the sole decorative line — the coral reappears as a framing device rather than just a button fill. Column headings at `{typography.title-md}` white; link text at `{typography.body-sm}` in `{colors.surface-soft}` light gray. Four desktop columns: Shop by Category, Shop by Brand, Account & Wholesale, Policies & Support.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar full-width below collapsed nav; topStripe collapses to single-line ticker or hidden; category chips become horizontal scroll strip with no wrap; hero min-height reduces to 240px; product card CTA becomes sticky bottom bar on PDP; spec table gains horizontal scroll |
| Tablet | 744–1128px | 2-column product grid; primary nav collapses to hamburger with slide-out drawer; topStripe present but abbreviated; category chips wrap to two rows; hero at 320px; brand logo strip visible; footer 2-column layout |
| Desktop | 1128–1440px | 3–4 column product grid; full two-tier nav with dropdown mega-menus; brand logo strip full-width; side-filter panel on category pages; hero at 400px; trust badge row visible below search |
| Wide | > 1440px | Content max-width ~1400px centered; 4–5 column product grid; hero background bleeds edge-to-edge while content stays inside max-width container |

### Touch Targets
- All CTA buttons minimum 44px height on mobile and tablet
- Category chips minimum 36px height with 12px horizontal padding on touch
- Nav hamburger icon minimum 44×44px tap target
- Product card entire surface tappable on mobile (full card links to PDP)
- Search submit button minimum 44×44px on touch

### Collapsing Strategy
- Primary nav collapses to hamburger at < 1128px; drawer slides from left at full viewport height with category accordion
- Two-tier chrome (topStripe + nav-bar) merges to single bar on mobile; topStripe content moves to drawer header
- Spec table gains horizontal scroll container at tablet and mobile; never reflowed to stacked rows
- Brand logo strip hidden on mobile to reduce scroll length; reappears at 744px
- Footer 4-column grid → 2-column at tablet → single-column accordion (collapsed by default) at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Primary color assignment (coral #db5757 as CTA primary, navy #394962 as structural nav) is inferred from palette distinctiveness and B2B HVAC convention — verify against live rendered button and nav elements
- Canvas base color not extracted; assumed #ffffff but site may use a very light warm or cool gray as the true page background
- No shadow or elevation tokens extracted; drop-shadow and box-shadow values for product cards and dropdowns are unspecified
- Icon system unknown — custom HVAC line icons, a commercial icon library, or Shopify defaults cannot be determined from color extraction alone
- DM Sans weight range in active use not narrowed; the family supports 300–700 but only display and body context was used to infer weights
- Exact topStripe presence, copy, and behavior not confirmed; topology inferred from common Shopify B2B wholesaler patterns
- Wholesale account tier structure (contractor vs. distributor pricing, net terms display logic) not accessible from front-end color pass
- Mobile navigation pattern (hamburger drawer vs. bottom tab bar) not confirmed
- No animation, transition, or motion tokens extractable from static color pass
- Mega-menu structure and depth (number of nested category levels) not confirmed
