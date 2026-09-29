---
version: alpha
name: "Arctic Spas"
source_url: "https://www.arcticspas.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Arctic Spas runs a five-stop crimson family from #a2051b to #8e0d27 with almost no chromatic variation between stops, then makes a hard cut to near-black (#231f20) and near-white (#fbfbfb) with no midtone color bridging the gap — a palette architecture that reads as engineered precision rather than lifestyle warmth. The effect is deliberate: a brand selling all-weather outdoor equipment in cold climates does not want terracotta softness; it wants the authority of a pressure gauge. Primary CTAs land in #a32035 against the near-white canvas, and the darker crimson #8e0d27 carries active/hover states, ensuring the red never blooms warm or orange at any interaction state. A secondary navy #003388 appears as link text and inline actions, borrowing trust-signal blue without competing with the crimson primary. The forest green #2e7d32 is used sparingly — almost certainly confined to availability indicators or eco-certification badges — and its presence in the extraction is a tell that the brand wants an environmental credibility signal without turning the whole system green. Type is built on Poppins for display and headline work, with Lato carrying body copy; the pair gives the interface a modest modernity — neither the neutrality of Inter nor the aggression of a slab serif. Roboto Condensed appears in the font stack and likely governs spec labels, comparison table headers, or feature callouts where horizontal compression matters in a data-dense layout. Button corners use a small radius ({rounded.sm}), product cards sit at {rounded.md}, and there are no pill shapes anywhere in the observed palette — the geometry is angular by product category association, echoing the cabinet lines of the tubs themselves. The four near-white tinted swatches (#eeffee, #ffeeee, #eeeeff, #eeeeee) suggest hover/focus state colorization across an interactive component library rather than true background fills — a pattern where buttons, checkboxes, and toggle surfaces shift slightly warm or cool on interaction. Section spacing is generous, matching the expectation of a premium product page where photography and feature prose need room to land.

colors:
  primary: "#a32035"
  primary-active: "#8e0d27"
  primary-hover: "#a3051b"
  primary-disabled: "#c3c3c3"
  primary-tint: "#ffeeee"
  accent-navy: "#003388"
  accent-green: "#2e7d32"
  ink: "#231f20"
  ink-secondary: "#383838"
  body: "#515151"
  muted: "#6d6e71"
  muted-soft: "#777777"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#fbfbfb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-mid: "#b7b7b7"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  state-focus-blue: "#eeeeff"
  state-focus-green: "#eeffee"
  state-error-tint: "#ff9999"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  overline:
    fontFamily: "'Roboto Condensed', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  badge:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link-sub:
    fontFamily: "'Lato', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  link:
    fontFamily: "'Lato', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
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
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
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
    borderColor: "{colors.primary}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    borderColorFocus: "{colors.accent-navy}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.ink}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.35)"
  nav-utility-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    shadow: "0 2px 12px rgba(0,0,0,0.08)"
  product-card-hover:
    shadow: "0 6px 24px rgba(0,0,0,0.13)"
    borderColor: "{colors.primary}"
  product-card-title:
    typography: "{typography.title-lg}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  hero-full:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    overlayColor: "rgba(10,0,0,0.45)"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 600px
  hero-overline:
    textColor: "{colors.primary}"
    typography: "{typography.overline}"
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  award-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  eco-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.ink}"
    headerTextColor: "{colors.on-dark}"
    rowAlternateBackground: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
  feature-tile:
    backgroundColor: "{colors.surface-soft}"
    iconColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  comparison-card:
    backgroundColor: "{colors.surface-card}"
    highlightBorderColor: "{colors.primary}"
    highlightBorderWidth: 3px
    normalBorderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-sm}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
  dealer-locator:
    backgroundColor: "{colors.surface-soft}"
    inputBackground: "{colors.surface-card}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    linkColor: "{colors.accent-navy}"
    rounded: "{rounded.sm}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    borderLeft: "4px solid {colors.primary}"
    bodyTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.nav-link-sub}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Deep crimson (#a32035) fill on a 48px-tall rectangle with 8px corner radius, Poppins semibold at 15px with 0.3px tracking. On hover the fill steps to #a3051b; on active press it drops to #8e0d27; disabled state replaces the fill with mid-gray (#c3c3c3) while preserving white text. Padding is 14px vertical and 28px horizontal, giving the label generous air without borrowing pill-shaped softness from the geometry.

**`button-secondary`** — Near-white canvas fill enclosed by a 2px #a32035 border, with crimson text, same 48px height and {rounded.sm} radius as the primary. Hover shifts the fill to the soft #ffeeee tint so the border color reinforces rather than fights the background change. Used for "Learn More" and secondary configurator actions placed alongside a primary CTA.

**`button-ghost`** — Transparent background, ink (#231f20) text, Poppins semibold at 13px. Carries tertiary navigation actions and inline text triggers that need button affordance without color emphasis.

### Nav Bar

**`nav-bar`** — Full-width bar locked to #231f20, standing 72px tall. Top-level links are Poppins semibold 14px in white. A 36px `nav-utility-bar` in primary crimson (#a32035) sits above the main bar and carries phone number, dealer-locator link, and locale switcher in 12px white Lato. The dark bar persists on scroll without a transparency transition; `nav-bar-scrolled` adds a 0.35-opacity black shadow. The logo sits left-aligned; mega-menu dropdowns open on hover with a white panel and ink body copy in `{typography.nav-link-sub}`.

### Product Card

**`product-card`** — White surface with 1px #e0e0e0 border, 12px radius, and a shallow 8px ambient shadow. The card title uses `{typography.title-lg}` in ink; price renders in `{typography.price-display}` at #a32035. On hover the shadow deepens and the border steps to the primary crimson, creating a selection highlight without a separate selected state. The product image occupies the top 55% of the card at full bleed with radius-clipped corners. A `category-badge` in crimson sits in the upper-left of the image zone. An `eco-badge` in accent-green may appear alongside for certified models.

### Hero

**`hero-full`** — Full-viewport-width image or video with a 45% dark overlay (rgba(10,0,0,0.45)) that ensures white headline type reads at WCAG AA against variable photography. The overline uses `{typography.overline}` in crimson #a32035 above the main `{typography.display-xl}` heading. A subhead in `{typography.display-sm}` follows, then a primary CTA and optional ghost CTA arranged in a horizontal flex row with 16px gap. Minimum height is 600px; on mobile it collapses to 480px with the overline hidden.

### Spec Table

**`spec-table`** — Two-column key-value table with a dark (#231f20) header row and alternating #f5f5f5/white row backgrounds. The label column uses `{typography.spec-label}` (Roboto Condensed, uppercase, 0.5px tracking) to pack dense feature names into narrow widths. The value column uses `{typography.body-sm}` in ink. Borders are 1px #e0e0e0 throughout. On mobile the table enables horizontal scroll with a sticky first column so feature names remain anchored.

### Feature Tile

**`feature-tile`** — Soft-gray (#f5f5f5) card with 12px radius and 32px padding. Each tile leads with a 40px icon rendered in #a32035, followed by a `{typography.title-md}` heading and `{typography.body-sm}` body in #515151. Feature grids run 3-up on desktop, 2-up on tablet, 1-up on mobile. Used to communicate all-weather insulation ratings, jet configurations, and filtration claims.

### Comparison Card

**`comparison-card`** — White card with a 3px crimson top border applied to the recommended model tier; all other tiers receive a 1px #e0e0e0 border. Title in `{typography.title-lg}`, feature rows in `{typography.body-sm}`, check marks in accent-green (#2e7d32) and cross marks in muted (#6d6e71). Cards stack 2–4 side by side on desktop in the Compare Models section; on mobile they become a snap-scroll carousel with 88vw card width.

### Promo Banner

**`promo-banner`** — Full-width crimson (#a32035) strip at 36px height, `{typography.caption}` in white, center-aligned text. Carries seasonal sale messaging or a persistent promotional code. Stacks above `nav-utility-bar` in the z-order, making the top of the page a two-tier crimson header before the dark nav bar below.

### Dealer Locator

**`dealer-locator`** — Soft-gray (#f5f5f5) section with a white postal-code text input and a primary crimson submit button arranged side by side in a single row. Dealer result cards below use ink-on-white with accent-navy (#003388) for phone and email links. The search input uses the standard `{typography.body-md}` Lato stack at 48px height.

### Testimonial Card

**`testimonial-card`** — White card with a 4px left border in #a32035, 12px radius, and 32px padding. The body quote uses `{typography.body-md}` at #515151; the author line uses `{typography.caption}` at #6d6e71. On desktop testimonials grid 3-up; on mobile they scroll horizontally in a snap carousel with full-width cards.

### Footer

**`footer`** — Near-black (#231f20) background with white column headings in `{typography.title-sm}` (Poppins semibold). Footer links use `{typography.nav-link-sub}` (Lato regular 14px) in #eeeeee, brightening to full white on hover. A 1px #383838 divider separates the link columns from the legal strip below. Social icon row and legal text sit in the bottom strip in caption-scale type. Section padding is `{spacing.section}` top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero drops to 480px min-height and hides overline; nav collapses to hamburger with full-screen #231f20 drawer; product cards stack vertically; spec table enables horizontal scroll with sticky label column; feature tiles go 1-up; comparison cards become snap-scroll carousel; footer link columns collapse to accordion |
| Tablet | 744–1128px | Two-column product grid; feature tiles 2-up; hero overline visible; nav retains condensed horizontal links with flyout dropdowns; comparison cards scroll horizontally 2-at-a-time; dealer locator input and button stack vertically |
| Desktop | 1128–1440px | Three-column product grid; feature tiles 3-up; full mega-menu on hover; comparison cards 3–4 up; hero CTA row horizontal; spec table at full width |
| Wide | > 1440px | Content width locked to 1440px max with auto side margins; hero image scales to fill; footer columns gain additional whitespace between groups |

### Touch Targets
- All buttons minimum 48px height on all viewports
- Nav hamburger button and drawer close icon are 48×48px tap area
- Product card tap area spans full card including image zone
- Dealer-locator submit button minimum 48px height regardless of viewport
- Utility-bar links padded to minimum 36px height; phone icon given 48px touch area on mobile

### Collapsing Strategy
- Primary nav collapses to full-screen dark (#231f20) overlay drawer on mobile with a × close button in the top-right corner
- `nav-utility-bar` and `nav-bar` merge on mobile to a single 56px combined bar showing only phone icon and hamburger
- Mega-menu subcategories become tap-to-expand accordion sections inside the mobile drawer, with Poppins semibold headings as triggers
- Footer link columns collapse to tap-to-expand accordions with the heading row acting as the toggle
- Comparison table switches from side-by-side cards to a horizontal snap-scroll carousel at 88vw card width with 12vw right peek showing the next card

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed logo dimensions, lockup variants, or SVG source — logo file not extracted from the site
- Poppins and Lato role assignments (display vs. body) inferred from font-stack ordering in CSS, not from a formal brand guide
- Poppins weight split between 600 and 700 at display scale is estimated; exact weights not confirmed
- Roboto Condensed role is inferred from font-stack presence; may be limited to a single legacy template rather than a system-wide token
- The four near-white tinted hex values (#eeffee, #ffeeee, #eeeeff, #eeeeee) may be programmatically generated focus or hover states rather than static palette tokens; their exact trigger conditions are unconfirmed
- Dark-mode or high-contrast variant not observed in extraction
- Icon library version not confirmed — FontAwesome is present in the font stack but specific icon set, version, and any custom glyph extensions are unknown
- Animation easing curves and transition durations not captured in static extraction
- Form validation state color usage (error, warning beyond the extracted #ff9999) not confirmed from live UI observation
- Exact nav-bar height of 72px is estimated from typical premium DTC patterns for this product category; live measurement not available
