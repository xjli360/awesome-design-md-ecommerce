---
version: alpha
name: "Royal Consumer Information"
source_url: "https://www.royal.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Navy and amber sit together the way a government-issue hallmark does — Royal's #003388 deep blue and #f7b818 gold carry institutional weight that makes sense for a company that has been manufacturing paper-handling machines since 1904. The custom "Rey Primary" typeface anchors display headings and navigation labels; Open Sans carries body copy and spec data at modest weights, keeping feature comparison tables and DIN-rating readouts clean without academic formality. Primary interactive chrome — buttons, links, focus rings — runs on #055e94, a mid-range royal blue that reads as authoritative on both white canvas and product photography. The golden amber (#f7b818) surfaces strictly as a promotional signal: sale flags, new-arrival callouts, limited-run badges. It never appears as a primary button color, preserving its meaning as a reward marker rather than a navigation device.

  Corner radii are kept deliberately conservative — `{rounded.xs}` for text inputs and form fields, `{rounded.sm}` for cards and primary buttons, never pill-shaped. There are no soft organic curves; the geometry reads utilitarian. The grid is functional and dense, built around feature comparison and specification readout rather than editorial whitespace. Product cards carry structured metadata rows — sheet capacity, security level, and DIN rating for shredders; display type and memory capacity for calculators — making each card function as a condensed datasheet. The purple accent (#6246d7) appears selectively, likely marking a premium or commercial product tier, while the lighter periwinkle #5e74c4 handles secondary navigation states and promotional band backgrounds. A narrow top-stripe in #003388 carries utility links (support, where to buy, language) above the main nav, a corporate-site convention that Royal has preserved from the era when such strips first appeared in office-product catalogs. Footer surfaces use near-black (#252525) with hairline-gray type, anchoring regulatory copy, warranty terms, and retailer-finder links in a register that reads permanent rather than promotional.

colors:
  primary: "#055e94"
  primary-deep: "#003388"
  primary-active: "#044a75"
  primary-disabled: "#a8cde0"
  accent-gold: "#f7b818"
  accent-gold-dark: "#c9940e"
  accent-purple: "#6246d7"
  accent-periwinkle: "#5e74c4"
  accent-sky: "#2ea3f2"
  ink: "#222222"
  body: "#32373c"
  muted: "#252525"
  muted-soft: "#6b6b6b"
  hairline: "#d8d8d8"
  hairline-soft: "#eaeaea"
  canvas: "#fefefe"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-footer: "#252525"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-gold: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'Rey Primary', 'Open Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Rey Primary', 'Open Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Rey Primary', 'Open Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Rey Primary', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Rey Primary', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Rey Primary', 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Rey Primary', 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Rey Primary', 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  logo-display:
    fontFamily: "'Rey Primary', 'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.0
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-gold-accent:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-sm-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 34px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  nav-bar-top-stripe:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    linkColor: "{colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
    logoTypography: "{typography.logo-display}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "1/1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    specTypography: "{typography.body-sm}"
    specLabelTypography: "{typography.spec-label}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.08)"
  badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-premium:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    accentColor: "{colors.accent-gold}"
    ctaBackgroundColor: "{colors.accent-gold}"
    ctaTextColor: "{colors.on-gold}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.sm}"
  category-nav-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    hoverTextColor: "{colors.primary}"
    padding: "{spacing.lg}"
    iconColor: "{colors.primary}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    altRowBackground: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted-soft}"
    valueColor: "{colors.ink}"
    borderColor: "{colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.base}"
  product-line-band:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.accent-gold}"
    padding: "{spacing.xxl} {spacing.section}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
    iconColor: "{colors.primary}"
    submitButton: "button-primary"
  retailer-finder-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
  warranty-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.md}"
  footer:
    backgroundColor: "{colors.surface-footer}"
    textColor: "{colors.hairline}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — The standard CTA sits at 44px tall with `{rounded.sm}` corners and #055e94 fill. Hover darkens to `{colors.primary-active}` (#044a75); disabled washes out to `{colors.primary-disabled}`. Used for "Add to Cart," "Shop Now," and primary form submissions across the site.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and matching text; same height and radius as primary. Appears alongside primary CTAs for secondary actions like "Compare," "Download Manual," or "View Specs."

**`button-gold-accent`** — Amber (#f7b818) background with near-black text (`{colors.on-gold}`). Reserved for hero CTAs within the deep-navy (`{colors.primary-deep}`) banner where the blue primary would disappear against the dark background. Also used for promotional section CTAs.

**`button-ghost`** — Transparent background, `{colors.primary}` text, no border. Appears in spec table footers and within product cards for low-priority secondary links ("Learn More," "See All Reviews").

### Navigation

**`nav-bar-top-stripe`** — A 36px dark navy (`{colors.primary-deep}`) band above the main nav carries utility links: store locator, customer support, and account links in `{typography.caption}` hairline-toned type. Standard corporate utility-nav pattern.

**`nav-bar`** — 64px white main navigation with `{typography.nav-link}` labels and a 1px `{colors.hairline}` bottom border. Active category underlines in `{colors.primary}`. Megadropdowns expand below the nav rail, organized by product category (shredders, calculators, accessories).

### Product Cards

**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.sm}` corners. A 1:1 image region sits above a content block with product name in `{typography.title-sm}`, price in `{typography.title-md}`, and two to four key spec rows using `{typography.spec-label}` for the label (uppercase, spaced) and `{typography.body-sm}` for the value. Hover lifts the card with a soft shadow. Badges (sale, new, premium) overlay the top-left corner of the image.

### Badges

**`badge-sale`** — Amber (#f7b818) chip with near-black text in uppercase `{typography.badge}`. Appears on product cards and within promotional bands to signal discounts without using primary blue.

**`badge-new`** — Blue (`{colors.primary}`) chip with white text. Marks recently introduced models in the product catalog.

**`badge-premium`** — Purple (`{colors.accent-purple}`) chip marks commercial or professional-tier products (heavy-duty shredders, high-capacity models). The purple differentiates the commercial tier visually from the consumer product line.

### Hero Banner

**`hero-banner`** — Full-width deep-navy (`{colors.primary-deep}`) background with product photography inset on the right side. Headline in `{typography.display-xl}` white type; subheadline in `{typography.body-md}`. CTA uses `{colors.accent-gold}` fill so it reads against the dark background. The amber-on-navy pairing is the most "Royal" moment in the UI — the heraldic register is strongest here.

### Specification Table

**`spec-table-row`** — Alternates between white and `{colors.surface-soft}` rows. Labels in uppercase `{typography.spec-label}` sit in the left column in `{colors.muted-soft}`; values in `{typography.body-sm}` sit right in `{colors.ink}`. Used for shredder DIN ratings, sheet capacity, motor specs, and calculator display/memory specs. This is the brand's primary information-density surface.

### Search

**`search-bar`** — Full-width search input at 42px tall with `{rounded.xs}` corners. A `{colors.primary}` search icon sits left-aligned inside the input; submits to a results page. On mobile this collapses to an icon in the nav that expands to full-width.

### Retailer Finder

**`retailer-finder-card`** — Used on a "Where to Buy" page to surface authorized retail partners (Best Buy, Staples, Amazon, Walmart). Each card shows retailer logo, availability note, and a ghost-style link in `{colors.primary}`. Light `{colors.surface-soft}` background with hairline border.

### Warranty Badge

**`warranty-badge`** — A small framed chip with `{colors.primary-deep}` text and a 2px `{colors.primary}` border. Appears on product pages to surface warranty duration ("2-Year Limited Warranty"). The border-frame treatment signals official documentation rather than a promotional call-out.

### Footer

**`footer`** — Near-black (`{colors.surface-footer}`) with a 3px `{colors.primary}` top border as the only color interrupt. Link columns in `{typography.body-sm}` hairline-toned type; column headings in `{typography.title-sm}` white. Hover links shift to `{colors.accent-gold}` — the amber reappears here as a navigational reward color. Contains legal copy, sitemap, social icons (FontAwesome), and a condensed retailer-finder link.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top utility stripe hidden; nav collapses to hamburger; product grid goes single-column; spec tables switch to stacked label/value pairs; hero headline drops to `{typography.display-sm}` |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with hamburger overflow; hero retains image but reduces padding to `{spacing.xl}`; spec tables remain tabular |
| Desktop | 1128–1440px | Three-column product grid; full megadropdown nav; hero at full padding `{spacing.section}`; side-by-side spec comparison active |
| Wide | > 1440px | Content max-width capped (~1280px) and centered; four-column product grid; hero gains wider image bleed |

### Touch Targets

- All primary and secondary buttons minimum 44px tall
- Nav top-stripe links minimum 36px tap target height
- Product card entire surface is tappable on mobile
- Badge chips do not require independent tap targets — they are display-only overlays

### Collapsing Strategy

- Top utility nav stripe disappears below 744px; its links migrate into a hamburger drawer's footer section
- Megadropdown nav collapses to a full-screen side drawer on mobile with category accordion
- Spec tables reflow to single-column stacked layout on mobile (label above value) rather than horizontal scroll
- Hero banner stacks vertically on mobile: image above, text and CTA below, on `{colors.primary-deep}` background
- Footer link columns collapse to a single accordion on mobile; each column heading becomes an expand toggle

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted — mobile browser chrome color for nav bar unknown; `{colors.primary-deep}` assumed as safest default
- "Rey Primary" font details (weights available, whether it is a variable font, exact licensing) not available from extraction; weight range and tracking assumed from visual inspection
- "aslsicons2" icon font purpose and glyph set undocumented; likely a custom product-category icon font used alongside FontAwesome
- Exact hover/active states for nav megadropdown items not extractable from static snapshot
- Checkout and account page design patterns not captured — e-commerce detail (cart drawer, order summary layout) unverified
- Shadow and elevation scale not confirmed; single hover-shadow value estimated from typical corporate e-commerce patterns
- Whether #6246d7 purple is a live product-line tier or a legacy/draft color could not be confirmed from extraction alone
- Price display formatting (MSRP vs. sale price strikethrough, MAP enforcement styling) not confirmed
