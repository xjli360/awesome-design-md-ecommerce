---
version: alpha
name: "Big Agnes"
source_url: "https://www.bigagnes.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, confident red (#990000) anchors Big Agnes — not as a call-to-action accent but as the brand's entire visual gravity, appearing in the site's theme-color meta tag, the header logo, and the primary button state. This is the red of a well-worn camp chair, of a tent fly at dusk, of a brand that names itself after a woman who refused to be left behind on a mountain. The palette draws from the outdoors without mimicking nature: a slate blue-gray (#6b6f81) for body text, a crisp navy (#00529c) for secondary actions and link states, and a warm off-white (#ededed) for surface-soft backgrounds that keep the experience from feeling cold. Product photography carries the weight — tents, sleeping bags, and pads are shown in use against granite, pine, and sky, so the UI stays restrained. Typography runs Archivo, a geometric sans-serif with a slight industrial edge, set at moderate weights (400–600) that never compete with the imagery. Buttons are squared-off with a 4px radius ({rounded.xs}), a deliberate departure from the pill-shaped friendliness of consumer marketplaces; the geometry says "equipment," not "app." Cards use a softer 12px radius ({rounded.md}) for product imagery, while the navigation bar sits at 80px tall with a white canvas and a thin hairline (#dedede) separating it from the page. The checkout flow introduces a marigold accent (#ffcb67) for progress indicators and a muted green (#1b6109) for in-stock badges — small functional signals that break the red-gray-blue trinity without diluting it. The overall mood is serious but not solemn, technical but not cold, built for people who read gear specs by headlamp.

colors:
  primary: "#990000"
  primary-active: "#4d0000"
  primary-disabled: "#d9d9d9"
  ink: "#060606"
  body: "#6b6f81"
  muted: "#9396a5"
  muted-soft: "#cdd0e1"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#ededed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-navy: "#00529c"
  accent-marigold: "#ffcb67"
  accent-green: "#1b6109"
  error: "#ff3333"
  error-dark: "#dc0000"
  badge-sale: "#e32e00"
  badge-new: "#00529c"
  star-rating: "#ffcb67"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.15px
  badge:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Archivo', 'Cabin', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
  button-pill-accent:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
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
  text-input-error:
    border: "2px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-instock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    height: 480px
  hero-title:
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    padding: "{spacing.base} {spacing.lg} {spacing.lg} {spacing.lg}"
    typography: "{typography.body-sm}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 44px
    width: 44px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, a deep red (#990000) rectangle with white text and a tight 4px radius. Uppercase Archivo at 15px/600 weight gives it an authoritative, gear-oriented feel. On hover, it shifts to `#4d0000` (primary-active). Disabled state uses `#d9d9d9` background with muted text, signaling non-interactivity without ambiguity.

**`button-secondary`** — An outlined variant with a 2px solid ink (#060606) border on a white canvas. Same uppercase typography and 4px radius. Active state fills the background with `#ededed` (surface-soft). Used for "Add to Wishlist" and secondary product actions where the red button would compete.

**`button-tertiary`** — A text-only button in primary red, no background or border. Active state gains a `#ededed` background on hover. Used for "View Details" links within product cards and filter reset actions.

**`button-pill-accent`** — A pill-shaped button in navy (#00529c), used sparingly for newsletter signups and promotional banners. The full radius and smaller height (36px) distinguish it from the primary system.

### Navigation
**`nav-bar`** — An 80px white header with a single 1px hairline (#dedede) bottom border. Navigation links are uppercase Archivo at 14px/500 weight with 0.3px letter spacing. The active state underlines with a 2px primary red border. The logo sits left, with the red (#990000) wordmark acting as the visual anchor. On scroll, the bar remains fixed with a white background.

**`nav-link-active`** — The active page or section link turns primary red with a 2px bottom border in the same red. Hover state also shifts text to red but without the underline.

### Forms
**`text-input`** — A standard input field with a 1px hairline border, 4px radius, and 48px height. On focus, the border thickens to 2px and turns primary red. Error state uses a 2px `#ff3333` border. Placeholder text is muted (#9396a5). Used for email signup, search filters, and account forms.

**`select-dropdown`** — Matches the text-input dimensions and border styling, with a custom chevron icon in ink (#060606). The dropdown panel uses a white canvas with a subtle shadow.

**`quantity-selector`** — A compact 44px-high control with increment/decrement buttons on either side. Buttons have a `#ededed` background and 4px radius. The central value display uses body-md typography.

### Cards
**`product-card`** — A white card with 12px radius containing a product image (rounded top corners only), a title in title-sm, and a price in body-md. No border — the card relies on the image and spacing for separation. Hover state adds a subtle shadow (not captured in extracted tokens but observed on the live site). Used on collection pages and search results.

**`badge-sale`** — An orange-red (#e32e00) badge with white uppercase text at 11px/700 weight. 4px radius. Positioned absolutely over the top-left of the product image.

**`badge-new`** — A navy (#00529c) badge with the same typography and radius, used for new arrivals and seasonal collections.

**`badge-instock`** — A green (#1b6109) badge indicating current availability. Same styling as other badges.

### Hero
**`hero-banner`** — A 480px-tall section with a `#ededed` background, typically featuring a full-bleed product lifestyle image. The hero title uses display-xl (36px/600 weight) with generous section padding. The primary CTA button sits below the title, matching the button-primary spec but with slightly larger padding (14px 32px) for visual weight.

### Footer
**`footer`** — A full-width dark section with ink (#060606) background and white text. Links are set in muted-soft (#cdd0e1) and shift to white on hover. Content is organized in columns with body-sm typography. The footer includes legal text, social links, and a newsletter signup form.

### Accordion
**`accordion`** — Used on product detail pages for specs, care instructions, and shipping info. Each accordion header is a white row with a 1px hairline bottom border, title-sm typography, and a chevron icon that rotates on open. Content area uses body-sm with base padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards stack single-column; hero height reduces to 320px; footer columns stack vertically; accordion becomes default for all filter groups |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; hero height at 400px; sidebar filters become a top filter bar |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; persistent sidebar filters on collection pages; hero at full 480px |
| Wide | > 1440px | Max-width container at 1440px with centered content; product cards in 4-column grid; additional whitespace around hero content |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons (search, cart, menu) are at least 44x44px with adequate padding.
- Product card tap targets extend to the full card area, not just the title.
- Accordion headers are 48px tall for easy tapping on mobile.

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer from the left.
- Secondary navigation (category links) collapses to a horizontal scrollable strip on mobile.
- Product filters collapse into a bottom sheet or modal on mobile, triggered by a "Filter" button.
- Footer columns stack vertically on mobile, with accordion-style expansion for each column heading.
- Product image galleries collapse to a single-column swipeable carousel on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., product card shadow, link underlines) were inferred from common patterns rather than extracted from the live site.
- Error styling for forms (error messages, iconography) was not fully extracted; the error border color (#ff3333) is present in the palette but its usage is assumed.
- Dark mode is not present on the live site; no dark theme tokens are defined.
- Sub-brand or collection-specific palettes (e.g., "Copper Spur" vs "Fly Creek" tent series) may exist but were not extracted.
- The extracted font list includes "Proxima-Nova" and "Times" which may be used in legacy pages or email templates but are not part of the primary design system.
- Checkout-specific components (Shopify Cart, payment buttons) were not analyzed; their colors (#ffcb67, #1b6109, #ff3333) appear in the extracted palette but their exact usage is inferred.
- Animation and transition durations (e.g., button hover, card hover shadow) were not extracted from the live site.
- The exact shadow values for product cards and modals were not captured; a standard `0 2px 8px rgba(0,0,0,0.1)` is assumed based on visual inspection.
- Accessibility contrast ratios for text on colored backgrounds (e.g., body text on surface-soft) have not been verified against WCAG standards.
- The brand's icon system (cart, search, user, chevron) was not extracted; stroke widths and sizes are assumed to match the typographic scale.
