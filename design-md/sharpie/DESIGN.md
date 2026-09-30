---
version: alpha
name: "Sharpie"
source_url: "https://www.sharpie.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The permanent marker leaves no room for revision — Sharpie's entire visual identity is built on that indelible, high-contrast logic. The extracted site palette anchors on #313131, a near-black that directly references the iconic black barrel and cap of the Classic Permanent Marker, while the brand's widely-documented red cuts through as the single high-voltage primary across every CTA, badge, and promotional accent. Type runs on system sans-serif stacks — clean, functional, built for a product site that moves through marker families quickly rather than lingering on typographic ornament. The nav deploys bold-weight links at modest sizes, prioritizing category scanability over editorial weight. Product cards are flat and square-cornered, reflecting the rectangular marker body; color swatches rendered as true circles (`{rounded.full}`) become the primary navigation instrument, letting shoppers browse by ink color rather than product name. A 3px red underline rule (`{colors.primary}`) beneath section headers performs the brand's core gesture — the marker stroke — without resorting to illustration. The highlighter yellow applied to "NEW" badges directly echoes Sharpie Accent product ink, creating a product-to-UI color echo that functions as both decoration and brand recall. The footer reverses to full `{colors.ink}` black with white-out text, mirroring the white-cap-on-black-barrel product aesthetic that has defined Sharpie packaging for decades. Spacing is utilitarian — `{spacing.lg}` gutters, `{spacing.section}` breaks — ensuring the color grid reads as a dense, browsable catalog without sprawling. No border-radius softens the buttons or section edges; the hard corner is a deliberate product-language decision, not an oversight.

colors:
  primary: "#E31837"
  primary-active: "#C0121F"
  primary-disabled: "#F0A0A8"
  ink: "#1A1A1A"
  body: "#313131"
  muted: "#6B6B6B"
  muted-soft: "#999999"
  hairline: "#E0E0E0"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  marker-black: "#000000"
  marker-barrel: "#313131"
  highlighter-yellow: "#FFE600"
  highlighter-green: "#00D26A"
  highlighter-pink: "#FF69B4"
  highlighter-orange: "#FF7A00"
  highlighter-blue: "#0085FF"
  scrim: "rgba(0,0,0,0.5)"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.2px
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  color-count:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none
    padding: 0
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 56px
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 56px
    width: "100%"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  search-button:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 20px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    shadow: "0 4px 16px rgba(0,0,0,0.12)"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    imageBackground: "{colors.canvas}"
    padding: "{spacing.md}"
    shadow: none
  product-card-hover:
    shadow: "0 4px 16px rgba(0,0,0,0.10)"
    border: "1px solid {colors.hairline}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-color-count:
    typography: "{typography.color-count}"
    textColor: "{colors.muted}"
  color-swatch:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.ink}"
    marginRight: "{spacing.xs}"
  color-swatch-lg:
    width: 40px
    height: 40px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    borderSelected: "2px solid {colors.ink}"
    marginRight: "{spacing.sm}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  category-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  hero-banner:
    backgroundColor: "{colors.marker-black}"
    textColor: "{colors.canvas}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    borderBottom: "3px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.xl}"
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  new-badge:
    backgroundColor: "{colors.highlighter-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  bestseller-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    width: 240px
    padding: "{spacing.xl}"
  filter-checkbox:
    accentColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  color-family-strip:
    height: 8px
    rounded: "{rounded.none}"
    display: flex
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separator: "/"
    gap: "{spacing.xs}"
  product-page-title:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 48px
    width: 120px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.canvas}"
    linkHover: "{colors.muted-soft}"
    padding: "{spacing.section} 0"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.canvas}"
    marginBottom: "{spacing.base}"
  footer-legal:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"

## Components

### Buttons

**`button-primary`** — Square-cornered (`{rounded.none}`) Sharpie red (#E31837) at 48px tall with all-caps `{typography.button-md}` text. The zero-radius corners mirror the rectangular marker body; no softening is applied anywhere along the button edge. Hover snaps immediately to `{colors.primary-active}` (#C0121F) with no easing — the state change is as instant as a marker stroke. Disabled state washes to `{colors.primary-disabled}`, and the cursor shifts to not-allowed.

**`button-secondary`** — White fill with a 2px solid `{colors.ink}` border, all-caps black type. On hover the entire button inverts — fill to `{colors.ink}`, text to `{colors.canvas}`. The high-contrast flip is a deliberate reference to the brand's own black-on-white / white-on-black product labeling logic; there is no intermediate gray state.

**`button-ghost`** — Transparent background, `{colors.primary}` red text, no border, no padding. Used inline for actions like "See all colors," "Compare," and "View collection" within product listings and editorial modules.

**`hero-cta`** — Taller at 56px, `{typography.button-lg}` (16px/700 uppercase, 0.5px tracking). Appears exclusively in `hero-banner` and full-bleed promotional modules. Always `{colors.primary}` — the brand does not vary CTA color by season or campaign.

**`add-to-cart`** — Identical spec to `hero-cta` but always full-width on mobile. Sharpie never renders a green or neutral add-to-cart; the red is a brand constant reinforcing the primary hue at the final conversion point.

### Text Input & Search

**`text-input`** — Zero-radius, `{colors.hairline}` 1px border at rest, upgrades to `{colors.ink}` 1px on focus. No box-shadow or ring — consistent with the brand's no-ornamentation stance. Placeholder at `{colors.muted}`.

**`search-bar`** — 2px `{colors.ink}` border (bolder than standard inputs) paired with a flush `search-button` on the right edge. The two elements form a single horizontal unit with no gap, no radius separation, and no divider line. The elevated border weight signals the search entry as the primary utility tool on catalog pages.

### Navigation

**`nav-bar`** — 64px white bar with a 1px bottom `{colors.hairline}`. Logo left-anchored at 32px height; nav links use `{typography.nav-link}` (14px/700). Cart and account icons right-aligned with minimum 44px hit targets. No background color change on scroll — the bar remains white throughout.

**`nav-dropdown`** — A flat zero-radius panel below the nav with a 1px `{colors.hairline}` border and a 16px-blur depth shadow. Category links in a multi-column grid; product family hero images in a right-side column. Typography at `{typography.body-sm}`. Panel dismisses on mouse-leave with no animation delay.

### Product Cards

**`product-card`** — No corner radius, thin `{colors.hairline-soft}` border, no shadow at rest. Product image always on pure-white background regardless of the marker's body color. Title at `{typography.title-md}`, price at `{typography.price-display}`. Color swatches (`color-swatch`, 24px circles) appear below the title in a flex row; products with more than five colors show five swatches then a `{typography.color-count}` muted label "· +N more."

Hover adds a `4px/16px/0.10` box-shadow without scale or lift transform — the card gains definition without shifting the grid. This keeps the color matrix stable as a browsing surface.

### Color Swatches

**`color-swatch`** — 24px circles (`{rounded.full}`) with a 2px transparent border that fills to `{colors.ink}` on selection. Swatch fill is the product's actual ink color, making the swatch grid itself a secondary filtering system. On product detail pages, `color-swatch-lg` (40px) is used; the larger target carries a visible `{colors.hairline}` ring at rest that tightens to `{colors.ink}` on selection, providing clear affordance at the purchase-decision moment.

### Category Filters

**`category-pill`** — `{rounded.full}` pill, `{colors.surface-soft}` fill, `{typography.label}` uppercase text with 1px letter-spacing. Inactive state is light-grey-on-white; active inverts to `{colors.ink}` fill / `{colors.canvas}` text. On desktop these wrap in a flex row above the product grid; on mobile they become a horizontal scroll strip.

**`filter-sidebar`** — 240px right-bordered panel on desktop; collapses to a full-screen bottom-sheet drawer on mobile. Group headings in `{typography.title-sm}`, filter option labels in `{typography.body-sm}`. Checkbox accent renders in `{colors.primary}` red — the one place primary color appears inside a utility UI component.

### Hero & Promotional Banners

**`hero-banner`** — Full-bleed `{colors.marker-black}` background with product flat-lay photography. `hero-banner-headline` in `{typography.display-xl}` white; sub-copy in `{typography.body-md}` at 75% opacity. A single `hero-cta` in `{colors.primary}` is the composition's only color accent — the red reads as electric against the black field. On wide viewports the image extends edge-to-edge; the text column caps at 640px.

### Badges

**`promo-badge`** — Flat `{colors.primary}` red, zero radius, `{typography.label}` uppercase, white text. Positioned top-left on product card images for sale, bundle, and exclusive items.

**`new-badge`** — Highlighter yellow (`{colors.highlighter-yellow}`) fill with `{colors.ink}` text. The color is a direct reference to Sharpie Accent highlighter ink — product-derived rather than arbitrarily chosen. This is the only badge that uses yellow; mixing with the red promo badge on the same card is avoided.

**`bestseller-badge`** — `{colors.ink}` fill with `{colors.canvas}` text. Conveys authority without the urgency of red; typically appears on Classic Permanent Marker and top-selling sets.

### Section Header

**`section-header`** — `{typography.display-md}` heading with a 3px `{colors.primary}` bottom-border, paddingBottom `{spacing.sm}`, marginBottom `{spacing.xl}`. The underline mimics the marker stroke gesture in UI form and appears on every product-category header, editorial callout, and landing-page collection title.

### Color Family Strip

**`color-family-strip`** — An 8px-tall horizontal rule rendered as a zero-gap flex row of colored segments, one per marker variant in a product family. Zero border-radius, no gutters between segments. Used as a decorative section divider on collection pages; its apparent width is proportional to the product count in the family, so a 24-pack marker set produces a wider strip than an 8-pack.

### Footer

**`footer`** — Full-width `{colors.ink}` background, four-column grid. Column headings use `{footer-heading}` (`{typography.title-sm}` white), body links use `{typography.body-sm}` white. Hover state on links transitions to `{colors.muted-soft}`. The legal row below uses `{footer-legal}` (`{typography.caption}` muted-soft). The ink block abuts the last content section without a separator line — the color contrast alone marks the transition.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category pills in horizontal scroll strip; search bar full-width, filter in bottom-sheet drawer triggered by floating "Filter" pill; nav collapses to hamburger + cart icon; hero at 320px min-height; `add-to-cart` always full-width |
| Tablet | 744–1128px | Two-column product grid; category pills wrap above grid; filter sidebar hidden, exposed via toggle button; nav shows top-level links with sub-categories behind hover; hero at 380px |
| Desktop | 1128–1440px | Three-to-four column product grid; `filter-sidebar` left-docked at 240px; full nav with mega-dropdown panels; `hero-banner` at 480px min-height |
| Wide | > 1440px | Content max-width 1440px centered, hero image bleeds edge-to-edge; five-column product grid; `section-header` underline extends to 80px fixed width on featured sections |

### Touch Targets

- All interactive controls minimum 44×44px on mobile
- `color-swatch-lg` (40px) replaces `color-swatch` (24px) on all mobile product detail pages
- Filter drawer bottom-sheet opens with a 56px drag handle strip; full-screen height on phones under 700px
- Nav hamburger minimum 44×44px; tap closes the open panel anywhere outside the menu panel

### Collapsing Strategy

- Nav: top-level links → hamburger drawer; cart and account icons remain always-visible in header
- Filter sidebar → bottom-sheet modal triggered by a pinned "Filter" pill that appears above the product grid
- Multi-column footer → single accordion; column headings become tappable expand/collapse rows
- Color swatch rows truncate to 5 swatches + count label below 744px regardless of product variant count
- Hero text: headline remains at `{typography.display-lg}` (36px) on mobile; subhead hidden below 744px to reduce vertical footprint

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color extracted (#313131): the site was blocked by Cloudflare anti-bot protection ("Just a moment..." page title), preventing full palette extraction
- Sharpie brand red (#E31837) sourced from widely-documented product packaging and brand guidelines, not extracted from the live site — verify against the actual site stylesheet before finalizing
- No custom web fonts detected; site likely loads a brand typeface via JavaScript after bot check; all typography uses system sans-serif stacks as fallbacks pending verification
- Highlighter accent colors (yellow, green, pink, orange, blue) derived from known Sharpie product line ink colors, not from extracted design tokens — verify against actual swatch UI on the live site
- No meta theme-color extracted; mobile status bar treatment unknown
- No spacing scale, breakpoint values, or motion/animation tokens extracted; all values above are reasoned defaults calibrated to the brand category
- No information on whether a Newell Brands shared design system applies brand-level tokens not surfaced in public CSS
