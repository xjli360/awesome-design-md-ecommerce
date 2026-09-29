---
version: alpha
name: "Skylight Books"
source_url: "https://www.skylightbooks.com"
captured_at: "2026-09-29T04:35:29.384536+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Skylight Books' storefront runs on a Drupal-based commerce theme whose CSS
  custom properties confirm Raleway as the active --font-family, with sage
  green (#5f775f) and slate blue (#64769d) set as the theme's primary and
  secondary variables. The broader observed palette is muted and paper-toned:
  near-white canvases (#ffffff, #fafafa, #f7f7f7), warm charcoal text
  (#232323, #454545), and soft grays for hairlines and disabled UI (#dddddd,
  #eeeeee). A teal (#1a936f) and a pale yellow (#fffa90) also appear in the
  palette; they are used here as inferred accents for staff-pick badges and
  light emphasis, alongside a red (#da4343) reserved for error/alert states.
  Typography beyond Raleway is uncertain: the codebase exposes a long list of
  serif and sans font names (Domine, Lora, Merriweather, Crimson Pro, Bitter,
  Poppins, Jost, and others) typical of a Drupal font-picker; their live
  rendering role is not confirmed by the supplied CSS. This spec inferentially
  assigns Domine as a literary serif for display headings to suit an
  independent bookstore's editorial tone, while keeping Raleway for body copy
  and interface text. Layout, spacing, and interaction states were not
  captured in this static CSS extraction and are proposed here as restrained,
  content-forward defaults appropriate to a catalog- and event-heavy
  bookstore site.

colors:
  primary: "#5f775f"
  secondary: "#64769d"
  ink: "#232323"
  canvas: "#ffffff"
  body: "#454545"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#fafafa"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  accent: "#1a936f"
  highlight: "#fffa90"
  error: "#da4343"
  border-strong: "#c5c5c5"
typography:
  display-xl: {fontFamily: "Domine, serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "Domine, serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Raleway, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Raleway, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Raleway, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Raleway, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Raleway, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  event-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    dateAccent: "{colors.secondary}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** carries the theme's sage-green primary variable as its fill with white text, used for the RSVP, add-to-cart, and checkout actions implied by the navigation's Cart/Wishlist utilities. Hover/active states are proposed, not observed.

**button-secondary** is an outlined variant in the same primary hue, intended for lower-emphasis actions such as "See all items" links beside the Bestsellers and Upcoming Events carousels named in the page content.

**text-input** models the search field and account forms (login, gift-card balance check) referenced in the utility menu, using the hairline gray border and near-black ink text observed elsewhere in form-adjacent CSS (e.g., the jQuery UI widget rules using #dddddd/#333333).

**nav-bar** represents the persistent main/utility navigation (Shop, Events, Programs, About, Log in, Wishlist, Cart) on a white canvas with a single hairline underline; dropdown/mega-menu sub-navigation behavior is proposed, not measured.

**product-card** covers bestseller and staff-pick listings, pairing a serif title with body-weight author and price text on the off-white card surface; the "Staff Pick" label is expected to use the badge component.

**hero** is a proposed pattern for the homepage's rotating image block ("Home Page Image Image Image Image"), set on the soft off-white surface with large serif display type; no measured hero copy or CTA placement was present in the evidence.

**footer** is proposed as a dark, ink-toned band for store info, social links, and newsletter/membership prompts (Friends with Benefits, Signed First Editions Club) mentioned in the Programs navigation; no footer markup was directly observed.

**badge** uses the pale-yellow highlight color for short labels like "Staff Pick," which appears repeatedly in the bestseller excerpt text.

**search** is a pill-shaped field for the site's stated multi-type search (Books, Audiobooks, Merch & Gift, Services), styled with the soft surface background and full rounding.

**event-card** is the category-appropriate component for Skylight's extensive events calendar (author talks, book clubs, off-site venues like Bar Henry and Saban Theatre); it separates a date/time accent in the secondary slate-blue from the event title and location meta text.

## Responsive Behavior

This breakpoint table is a recommendation based on common patterns for content-dense independent retailer sites; no responsive behavior was measured from the supplied evidence.

| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| Mobile | <600px | Collapsed hamburger, utility icons condensed | 1-column cards |
| Tablet | 600-960px | Horizontal primary nav, sub-nav on tap/hover | 2-column cards |
| Desktop | >960px | Full mega-menu sub-navigation shown on hover | 3-4 column cards |

Touch targets are proposed at a minimum 44x44px for cart/wishlist icons and event RSVP buttons. Sub-navigation (Shop, Events, Programs, About) should collapse into an accordion on mobile; this interaction is not verified against live markup.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived solely from static CSS and page-text extraction; no rendered layout, computed styles, or interaction states were observed. The --font-family variable confirms Raleway as the base typeface, but the numerous additional font names in the evidence (Domine, Lora, Merriweather, Crimson Pro, Bitter, Poppins, Jost, Quicksand, Figtree, Ubuntu, Noto Serif) are theme-available options whose actual applied role on this site is unconfirmed; the display/heading assignment to Domine here is an editorial inference, not a measured fact. All spacing, rounding beyond the one confirmed 4px border-radius (from Klaro cookie-notice CSS), breakpoints, hover/focus states, and hero/footer markup are proposed defaults, not observed. Color role assignments (ink, muted, hairline, surface-soft/card) are inferred pairings drawn from the supplied hex palette rather than confirmed component usage. Custom font licensing and self-hosting/CDN availability were not verified. Mobile navigation collapse behavior and menu interaction patterns were not present in the supplied evidence and are marked proposed throughout.
