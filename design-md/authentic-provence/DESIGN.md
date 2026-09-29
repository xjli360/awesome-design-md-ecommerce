---
version: alpha
name: "Authentic Provence"
source_url: "https://www.authenticprovence.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Chronicle Display's editorial serifs carry the brand's voice before a single product image loads — this is a site that thinks of itself as a magazine for the Provençal garden rather than a catalog. The anchor color is a deep French navy (#003388), pressed against warm parchment (#fafae1) in a combination that reads less as commercial and more as a printed lifestyle book about outdoor living. Sage (#757c71) handles secondary surfaces and hover states — the muted khaki-green that recurs in limestone walls and dried lavender bunches — while harvest gold (#c49800) punctuates seasonal callouts and category badges with the color of Provençal market stalls in August. Body text runs in Gotham at #1a1918, a near-charcoal that softens the contrast just enough to feel like quality offset printing rather than a screen. Barlow Condensed handles utility labels, nav categories, and price displays — its compressed geometry giving a sprawling garden-decor inventory a clean information hierarchy without visual clutter. Antonio appears in hero headlines and large campaign numerals, its tall condensed form suited to garden collection counts and seasonal drops. Corner radii are conservative throughout — `{rounded.sm}` at 8px on cards and inputs, `{rounded.none}` on hero banners and editorial imagery — no softening that might undercut the authority of a design-led brand. Spatial rhythm is generous: `{spacing.section}` at 64px between editorial zones and `{spacing.xl}` between product rows give the grid room to breathe the way an actual Provençal garden does. Two high-contrast pairings recur across banners, product tables, and badge systems — gold-on-navy and cream-on-navy — anchoring the visual language to a palette that looks as natural printed on linen as it does on screen.

colors:
  primary: "#003388"
  primary-active: "#002270"
  primary-disabled: "#b0bcdc"
  accent-gold: "#c49800"
  accent-gold-warm: "#f0b849"
  sage: "#757c71"
  sage-deep: "#67a671"
  ink: "#1a1918"
  body: "#2f2f2f"
  muted: "#43454b"
  hairline: "#e8e8eb"
  hairline-soft: "#eeeeee"
  canvas: "#fafae1"
  surface-soft: "#e8e8eb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#1a1918"
  charcoal: "#3a3a3a"

typography:
  display-xl:
    fontFamily: "'Chronicle Display A', 'Chronicle Display B', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Chronicle Display A', 'Chronicle Display B', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Chronicle Display A', 'Chronicle Display B', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  collection-header:
    fontFamily: "'Chronicle Display A', 'Chronicle Display B', Georgia, serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  hero-numeral:
    fontFamily: "'Antonio', Arial, sans-serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  title-md:
    fontFamily: "'Gotham A', 'Gotham B', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Gotham A', 'Gotham B', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Gotham A', 'Gotham B', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham A', 'Gotham B', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham A', 'Gotham B', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  utility-label:
    fontFamily: "'Barlow Condensed', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Barlow Condensed', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham A', 'Gotham B', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Gotham A', 'Gotham B', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham A', 'Gotham B', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.6px
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
    padding: 14px 28px
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    height: 48px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageRounded: "{rounded.none}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "{spacing.base}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    accentColor: "{colors.accent-gold}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  collection-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-accent}"
    typography: "{typography.utility-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  new-badge:
    backgroundColor: "{colors.sage}"
    textColor: "{colors.on-accent}"
    typography: "{typography.utility-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  seasonal-callout:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    accentColor: "{colors.accent-gold-warm}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl} {spacing.section}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.utility-label}"
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
    activeColor: "{colors.primary}"
    activeIndicator: "2px solid {colors.primary}"
  garden-feature-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    accentColor: "{colors.sage}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 48px
    iconColor: "{colors.muted}"
  promo-ribbon:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-accent}"
    typography: "{typography.utility-label}"
    height: 40px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-gold-warm}"
    headlineTypography: "{typography.utility-label}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Deep navy (#003388) fill with white Gotham uppercase text at 0.8px tracking and `{rounded.sm}` corners, 48px tall. On hover it darkens to `{colors.primary-active}` (#002270); the disabled state uses washed-out `{colors.primary-disabled}` (#b0bcdc). This is the standard commerce CTA — "Shop Collection," "Add to Cart," "View Details" — appearing most frequently against the cream canvas.

**`button-secondary`** — Transparent background, 2px navy border, navy Gotham uppercase text. Pairs naturally against the cream canvas on editorial pages; when placed on a dark or navy background it should be replaced with `button-ghost`. Hover state fills with navy background and inverts text to white.

**`button-gold`** — Harvest gold (#c49800) fill with `{colors.on-accent}` dark text in the same Gotham uppercase treatment. Reserved for hero CTAs placed on navy backgrounds where the gold-on-navy pairing is the brand's strongest visual signature. Also used for seasonal promotions and marquee landing pages.

**`button-ghost`** — Transparent with a 1px white border and white Gotham text; lives exclusively on dark navy hero and callout backgrounds. Typically a secondary action alongside `button-gold` — for example, "Learn More" beside "Shop Now."

**`button-sm`** — A reduced 12px Gotham uppercase variant used in compact contexts: category badges with an action, search suggestions, inline quick-add. Same rounded and color logic as the parent; inherits state colors from the corresponding full-size sibling.

### Text Input

**`text-input`** — White fill, 1px `{colors.hairline}` border, `{rounded.sm}` corners, 48px height. Placeholder text in `{colors.muted}`. On focus, `text-input-focus` upgrades the border to 2px navy with no outline ring. Used in site search, newsletter capture, and garden consultation request forms.

### Navigation

**`nav-bar`** — 80px tall, warm cream (`{colors.canvas}`) background with a 1px `{colors.hairline}` bottom border. The wordmark renders in `{colors.primary}` navy. Nav links use Gotham 500 at 14px with 0.3px tracking. On wide viewports the nav is flanked by a search icon and cart icon at right. The cream-on-white palette keeps the header editorial and quiet rather than high-contrast commercial.

**`nav-dropdown`** — White-card panels dropping below top-level categories, padded at `{spacing.lg}` with a subtle border. Grouped columns list sub-categories: Furniture, Planters, Water Features, Lighting, Accessories. Each column head uses `{typography.utility-label}` in navy; links use `{typography.body-sm}`. No imagery inside the dropdown — text-only to keep load fast and navigation unambiguous.

### Product Card

**`product-card`** — Zero-radius imagery bleeds edge to edge within the tile, reinforcing the magazine-grid feel. Product title in Gotham 600 15px, price in Barlow Condensed 600 18px in `{colors.primary}`, material or origin notes in 12px muted caption. On hover, a 4px box shadow lifts the tile. Collection badges and new-arrival labels appear below the image block rather than overlaid, preserving the editorial image presentation.

### Hero Banners

**`hero-banner`** — Full-width navy (#003388) section, minimum 560px tall. Chronicle Display XL headline in white, Gotham body copy in white at 80% opacity for visual hierarchy. On desktop, imagery anchors the right half while the headline and CTA sit left. CTA defaults to `button-gold` — the gold-on-navy combination is the brand's most distinctive moment. Used for seasonal collection launches, homepage above-the-fold, and campaign landing pages.

**`hero-editorial`** — Warm cream (`{colors.canvas}`) hero with Chronicle Display XL headline in `{colors.ink}` and a thin gold rule above the headline in `{colors.accent-gold}`. Used for journal entries, brand-story pages, and style guide features. No hard CTA block — links run as underlined Gotham body text rather than buttons. Minimum height 480px with generous `{spacing.section}` vertical padding.

### Badges and Labels

**`collection-badge`** — Harvest gold (#c49800) tag in Barlow Condensed uppercase, `{rounded.xs}` corners. Labels seasonal groupings ("Summer Collection," "New Arrivals," "Editor's Pick") and curated garden sets. Sits below the product image in the card grid.

**`new-badge`** — Sage green (`{colors.sage}`) variant for newly listed individual SKUs. Uses dark `{colors.on-accent}` text rather than white for legibility on the medium-toned sage. Same Barlow Condensed uppercase treatment; consistent placement below imagery.

### Seasonal Callout

**`seasonal-callout`** — Full-width navy stripe with Chronicle Display MD headline and Gotham body copy, all in white. A warm amber `{colors.accent-gold-warm}` (#f0b849) accent highlights key phrases or acts as a decorative horizontal rule. Padding at 48px vertical and 64px horizontal gives this section substantial editorial weight. Used for marquee seasonal promotions, new arrivals, and Provençal-sourced collection launches.

### Category Strip

**`category-strip`** — 48px bar on cream background, Barlow Condensed uppercase labels in `{colors.ink}`. The active category receives a 2px navy bottom indicator, the same treatment as a print magazine section marker. Links: All, Furniture, Planters, Water Features, Lighting, Accessories, Sale. Scrolls horizontally on mobile with per-item snap points; active indicator persists through scroll.

### Garden Feature Tile

**`garden-feature-tile`** — Light gray (`{colors.surface-soft}`) block with Chronicle Display SM headline and Gotham SM body. A sage accent line or icon provides the decorative element. Used in editorial grids explaining provenance, materials, and French craft sourcing — the "Why Authentic Provence" content blocks. Square corners (`{rounded.none}`) throughout; three-up grid on desktop, single-column on mobile.

### Search

**`search-bar`** — White fill, 1px `{colors.hairline}` border, `{rounded.sm}`, 48px tall with a magnifier icon in `{colors.muted}`. On focus, border upgrades to 2px navy per `text-input-focus`. Inline autocomplete dropdown appears on a white surface card with `{typography.body-sm}` suggestions grouped by category.

### Promo Ribbon

**`promo-ribbon`** — 40px harvest-gold ribbon pinned to the very top of the viewport, Barlow Condensed uppercase in `{colors.on-accent}`. Used for site-wide announcements: free shipping thresholds, limited-edition alerts, and seasonal sale headlines. Always gold — never navy — so it reads as distinct from the nav directly below it.

### Footer

**`footer`** — Deep navy (#003388) full-width footer. Column headers in Barlow Condensed uppercase white. Links in `{colors.accent-gold-warm}` (#f0b849) for warm contrast against navy. Sections: Customer Care, About Authentic Provence, Collections, Newsletter signup (text-input rendered light on dark), and social icons. Newsletter input field inverts to a white-bordered ghost style on dark background. Bottom row in smaller Gotham caption: copyright, privacy, and shipping policy links at reduced opacity.

### Breadcrumb

**`breadcrumb`** — Muted `{colors.muted}` caption text with `{colors.hairline}` separator chevrons. The current page label switches to `{colors.ink}` without underline. Appears on all product and category pages, sitting between the nav and the page headline.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero min-height drops to 360px, `display-xl` Chronicle scales to 32px; nav collapses to hamburger opening a full-width cream drawer from left; category strip becomes horizontal scroll with snap; footer columns stack single-column |
| Tablet | 744–1128px | Two-column product grid; hero splits 50/50 text and image; nav shows top-level categories only, dropdowns on tap; category strip fits without scroll; seasonal callout reduces Chronicle to 28px |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with hover dropdowns; hero 60/40 headline-to-image split; garden feature tile runs 3-up; full Chronicle Display XL scales restored |
| Wide | > 1440px | Content max-width 1440px centered with wider lateral margins; hero imagery scales to fill remaining width; product grid caps at four columns; generous whitespace flanks all editorial blocks |

### Touch Targets
- All nav links and icon buttons minimum 44×44px tap area
- Category strip items minimum 48px height for comfortable horizontal thumb navigation
- Product card tappable area covers the entire tile including image
- Footer links have 40px minimum height on mobile to prevent mis-taps
- Promo ribbon close/dismiss button minimum 44×44px if present

### Collapsing Strategy
- Nav collapses to hamburger at < 744px; drawer slides in from the left over cream background with navy brand mark in the header
- Mega-nav dropdowns become stacked accordion panels inside the mobile drawer; sub-categories expand on tap
- `hero-banner` stacks image above text block on mobile; CTA button spans full width
- `hero-editorial` collapses gold rule and headline to single column; Chronicle Display scales down to 32px
- `seasonal-callout` reduces to single column, Chronicle Display to 28px, vertical padding to `{spacing.xl}`
- `garden-feature-tile` grid collapses from 3-up on desktop to 1-up on mobile
- `footer` columns reorder: newsletter signup first, then Customer Care, then legal row

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Multiple extracted hex values (#00d084, #0693e3, #cd2653, #7a00df, #4721fb, #ab1dfe, #34e2e4, #4ab866, #cc1818) match the WordPress Gutenberg editor color palette exactly and were excluded from the brand color system as editor UI artifacts
- Exact Chronicle Display weight in use (Light 300 vs Regular 400) could not be confirmed; modeled as 400 for body display and 300 for collection-header scale
- Logo mark dimensions, clearspace rules, and wordmark SVG treatment not extractable; modeled as a navy Chronicle/Gotham wordmark
- Hover and focus state transitions (duration, easing) not captured from extraction
- Cart drawer, wishlist sidebar, and quantity stepper component patterns not observed
- Confirmed breakpoint pixel values from the live site unavailable; standard responsive breakpoints applied
- Product image aspect ratio enforced per card not confirmed; assumed 3:4 portrait for garden product imagery
- Whether Antonio is used for hero numerals only or also for display headlines on certain campaign pages could not be verified
- Mobile nav drawer exact background color (#fafae1 canvas vs pure white) not confirmed
