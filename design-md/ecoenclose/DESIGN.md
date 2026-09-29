---
version: alpha
name: "EcoEnclose"
source_url: "https://www.ecoenclose.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  EcoEnclose pairs two typefaces that rarely share a page: Merriweather serif for editorial headers where certification metrics and environmental statistics carry moral weight, and Poppins for the transactional layer — SKUs, fill weights, unit minimums. The color system pulls from a narrow band of the spectrum anchored by #002b2f, a teal so deep it reads as near-black until placed against #f3f8f3, a section background carrying just enough green that no surface here is ever truly neutral. Sage runs in two registers: #83b785 handles interactive accents and secondary CTAs while #466c50 deepens into hover and confirmed states, both distinct enough from the primary that borders are rarely necessary. Cards sit on #ffffff but section washes use #e5f1ea, keeping the material story present even on checkout pages. Button geometry is unusually restrained — 4px radii rather than the pill shapes common to consumer DTC, a choice that reads as honest about the industrial context of corrugated mailers and recycled poly bags. Sustainability credentials — FSC marks, recycled-content percentages, carbon-neutral badges — receive the same typographic treatment as primary navigation, signaling that compliance is a product category, not a footnote. A faint salmon (#f19066) surfaces only in promotional call-outs, isolated from the green narrative, while #003eff appears as a hyperlink fallback in body copy — both colors feel like interruptions, which is exactly the point. Spacing inside components is generous; spacing between sections tighter, creating a page cadence closer to a B2B catalog read with purpose than a consumer shop browsed for pleasure.

colors:
  primary: "#002b2f"
  primary-active: "#003a40"
  primary-hover: "#173a3c"
  primary-disabled: "#9fbab1"
  ink: "#1a1a1a"
  body: "#383a36"
  muted: "#555555"
  muted-soft: "#6b6b6b"
  hairline: "#e0e0e0"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f3f8f3"
  surface-section: "#e5f1ea"
  surface-card: "#ffffff"
  on-primary: "#f3f8f3"
  accent-sage: "#83b785"
  accent-sage-hover: "#466c50"
  accent-muted: "#8fa893"
  accent-warm: "#f19066"
  badge-cert: "#466c50"
  badge-cert-text: "#f3f8f3"
  tag-light: "#e5f1ea"
  tag-text: "#002b2f"
  promo-highlight: "#003eff"
  charcoal: "#2b2b2b"

typography:
  display-xl:
    fontFamily: "'Merriweather', Georgia, serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Merriweather', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Merriweather', Georgia, serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  overline:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.8px
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
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link-bold:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge-label:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
  button-sage:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-sage-hover:
    backgroundColor: "{colors.accent-sage-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "none"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 42px
  nav-top-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    linkColor: "{colors.accent-sage}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    activeTextColor: "{colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    boxShadow: "0 4px 16px rgba(0,43,47,0.10)"
    headingTypography: "{typography.nav-link-bold}"
    itemTypography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
  product-card-hover:
    border: "1px solid {colors.accent-muted}"
    boxShadow: "0 2px 12px rgba(0,43,47,0.08)"
  product-card-badge:
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.accent-sage}"
    ctaTextColor: "{colors.primary}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  hero-light:
    backgroundColor: "{colors.surface-section}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 400px
    padding: "{spacing.section} {spacing.xl}"
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.surface-section}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    hoverBorder: "1px solid {colors.accent-sage}"
    hoverBoxShadow: "0 2px 10px rgba(0,43,47,0.07)"
  cert-badge:
    backgroundColor: "{colors.badge-cert}"
    textColor: "{colors.badge-cert-text}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  sustainability-tag:
    backgroundColor: "{colors.tag-light}"
    textColor: "{colors.tag-text}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    border: "1px solid {colors.accent-sage}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    iconColor: "{colors.muted}"
    placeholderColor: "{colors.muted-soft}"
  promo-banner:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    fontWeight: 600
    height: 40px
    linkColor: "{colors.primary}"
    linkDecoration: underline
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    height: 40px
    buttonWidth: 36px
    buttonBackgroundColor: "{colors.surface-soft}"
  pagination:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    activeBorder: "1px solid {colors.primary}"
    activeBackground: "{colors.surface-section}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  section-divider:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} 0"
  overline-label:
    textColor: "{colors.accent-sage-hover}"
    typography: "{typography.overline}"
    marginBottom: "{spacing.sm}"
  alert-info:
    backgroundColor: "{colors.surface-section}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.accent-sage}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-sage}"
    linkHoverColor: "{colors.accent-muted}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "none"

## Components

### Buttons

**`button-primary`** — Deep teal (#002b2f) fill with an off-white green-tinted label, 4px radius keeping the form strictly utilitarian. Hover deepens to #173a3c; active drops further to #003a40. Disabled state washes to the muted sage #9fbab1 with no label color change, signaling unavailability without red-state alarm.

**`button-secondary`** — White fill with a 1.5px primary-teal border and primary-teal text. Hover introduces a #f3f8f3 background wash so the boundary between the button and the canvas softens without disappearing. This variant appears most heavily in filter panels and comparison toolbars.

**`button-sage`** — #83b785 fill with dark primary text — the reverse of the primary button — used exclusively for supplementary CTAs like "Request a Sample" or "Download Spec Sheet." Hover deepens the fill to #466c50 and inverts the text to on-primary, giving a committed, confirmed feeling.

**`button-ghost`** — Transparent, no border, underlined text in primary teal. Used inline inside body copy for links that carry a call-to-action intent (e.g. "learn more about our certifications") without interrupting the reading rhythm.

### Navigation

**`nav-top-bar`** — A 36px teal bar (#002b2f) sits above the main nav, carrying shipping thresholds, sustainability credentials, and login links in #f3f8f3 caption type. Sage-colored links (#83b785) stand out against the dark ground. This bar is the first design element a visitor encounters and immediately establishes the teal-as-authority register.

**`nav-bar`** — White 64px bar with a 1px hairline bottom border. Logo renders in primary teal. Nav links at 14px Poppins weight 500, turning primary teal on active. Dropdowns (`nav-dropdown`) open as flat white panels with a subtle teal box-shadow rather than a colored header, keeping the drop zone calm and scannable.

### Product Cards

**`product-card`** — White card with 1px hairline border and 4px radius. Title in Poppins 15px/600, price in Poppins 20px/700 (primary teal), supporting spec copy in body-sm muted. On hover the border transitions to accent-muted (#8fa893) and a faint teal-tinted shadow appears. Certification badges (`cert-badge`) pin to the top-left as flat forest-green chips with no radius — industrial rather than decorative.

**`sustainability-tag`** — Pill-shaped (#e5f1ea fill, #83b785 border, #002b2f text) tags appear on cards and PDPs to surface specific eco-credentials (100% Recycled, Compostable, FSC Certified). They use `{rounded.full}` — the only fully rounded element in the system, deliberately contrasting the flat geometry of structural components.

### Hero

**`hero-dark`** — Full-width #002b2f section with #f3f8f3 Merriweather headline (display-xl) and Poppins body copy. The primary CTA button uses the `button-sage` style (#83b785 fill, primary text), creating a warm sage accent against the teal ground. Min-height 480px; copy block maxes at 640px wide and left-aligns against a 64px section pad.

**`hero-light`** — Alternate hero for secondary landing pages uses #e5f1ea background with primary-teal headline. The sage accent disappears; the CTA reverts to `button-primary`. This variant signals an informational rather than conversion intent.

### Badges and Tags

**`cert-badge`** — Zero-radius rectangular chip in #466c50 with #f3f8f3 text at 10px/700 uppercase. Applied to product images and category tiles. The hard corner is intentional: certifications are facts, not brand expressions.

**`promo-banner`** — Full-width #83b785 strip at 40px height carrying shipping thresholds or limited-time offers in Poppins body-sm bold, with primary-teal underlined links. Appears between the top-bar and nav-bar, so the entry sequence is teal → sage → white.

### Forms and Inputs

**`text-input`** — White fill, 1px hairline border, 4px radius. Focus ring is a 1.5px solid primary-teal replacement of the hairline — no glow or drop shadow, matching the brand's aversion to decorative effects. Placeholder text in muted-soft (#6b6b6b).

**`quantity-stepper`** — Flat white center field flanked by no-radius increment buttons in #f3f8f3 background. No border-radius on the stepper wrapper — the component looks like a linear control panel segment rather than a rounded pill. Appears on product detail pages and bulk order configurators.

### Footer

**`footer`** — Full-width #002b2f block, matching the top-bar and hero-dark palette, creating a visual bookend that frames every page interior as a light content well. Column headings in Poppins title-sm on-primary; links in #83b785 sage, turning #8fa893 on hover. No border-top, no divider — the dark background is boundary enough.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top bar collapses to single centered line; nav becomes hamburger menu in primary teal; hero drops to min-height 320px with 16px horizontal pad; product grid goes 1-column; price and CTA stack vertically on PDP |
| Tablet | 744–1128px | Nav bar retains full links but dropdowns become bottom-sheet drawers; hero min-height 400px; product grid 2-column; category cards 2-up |
| Desktop | 1128–1440px | Full 3-column product grid; nav dropdowns fly out as mega-menus; hero returns to 480px min-height with constrained content column |
| Wide | > 1440px | Content column max-width 1320px centered; section padding scales to 80px; hero background extends full bleed while content remains in grid |

### Touch Targets

- All buttons minimum 44px height with 12px+ vertical padding
- Quantity stepper increment/decrement buttons minimum 40×40px tap area
- Nav hamburger icon minimum 44×44px hit area
- Sustainability tags and cert badges non-interactive; no tap target requirement
- Search icon button minimum 44×44px

### Collapsing Strategy

- Top promotional bar: collapses to a single rotating message on mobile, hidden on scroll-down, reappears on scroll-up
- Mega-menu navigation: collapses to an accordion drawer on tablet and below; top-level categories expand in-place rather than flying out
- Product filter sidebar: collapses to a slide-up filter sheet triggered by a "Filter & Sort" button; active filters shown as removable tags above the grid
- Certification details panel: collapses to a collapsed accordion on PDP mobile; each cert expands individually
- Footer columns: stack vertically on mobile with each heading acting as an accordion toggle

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand typeface loading URL confirmed — Merriweather and Poppins inferred from font-family stack extraction; weights and custom variants not verified
- Exact button border-radius values not measured from live DOM; 4px inferred from visual appearance and brand utilitarian character
- Icon system not extracted — glyph set, stroke weight, and sizing unknown
- Hover/focus animation durations and easing not captured; no motion tokens defined
- Mobile nav drawer color and transition behavior not confirmed
- Form validation states (error, success) color values not extracted; #f19066 assumed for error accent but not confirmed
- Shadow values estimated; actual box-shadow definitions may differ from the 8% teal-tinted values used here
- Exact line-height and letter-spacing values for Merriweather display sizes not measured; values approximate typical Merriweather rendering
- Cart drawer and checkout flow design not extracted — those pages may deviate from the marketing-site color system
