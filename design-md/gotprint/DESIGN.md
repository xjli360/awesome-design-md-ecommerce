---
version: alpha
name: "GotPrint"
source_url: "https://www.gotprint.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The grass-green #8cc63f carries more signal than the house blue at GotPrint — it marks upload-complete states, proof-approved badges, and checkout confirmations, embedding the physical print-job workflow directly into the color language. The primary #3e84b6 is a workmanlike mid-blue that anchors navigation, primary CTAs, and product links without drama; it reads as competent and utilitarian rather than expressive. Below these two live an entire Bootstrap 4 alert system — success greens, info teals, warning ambers, danger reds — each with paired light backgrounds and dark text tones, which the site uses to surface job-status messages, file-requirement warnings, and order confirmations across a highly transactional UI. Type runs entirely on the system stack: Arial and Helvetica Neue at weights 400–700, sized conservatively across a tight scale. There are no custom display typefaces, no editorial serifs, no decorative ligatures — the typographic posture says "quick quote, fast checkout" rather than "premium brand moment." Cards sit at {rounded.sm} with hairline borders at #dae0e5; form inputs borrow the same 4px radius. The canvas is white (#ffffff) against a soft blue-gray surface (#f0f4f7) that gives product listing pages a light panel feel without introducing shadows. Navigation is a dense horizontal bar in #004085 navy — darker than the primary — with white labels, creating a hard authority stripe across the top that anchors the page even when the product grid beneath it gets busy. The footer mirrors this with the same navy ground. The overall system is openly pragmatic: a printing company that understands its customers need price calculators and file upload flows, not mood lighting.

colors:
  primary: "#3e84b6"
  primary-dark: "#004085"
  primary-active: "#0062cc"
  primary-disabled: "#b3d7ff"
  accent: "#8cc63f"
  accent-dark: "#1e7e34"
  ink: "#1d2124"
  body: "#383d41"
  muted: "#818182"
  muted-light: "#c8cbcf"
  hairline: "#dae0e5"
  hairline-soft: "#ececf6"
  canvas: "#ffffff"
  surface-soft: "#f0f4f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-dark: "#ffffff"
  success-bg: "#b1dfbb"
  success-text: "#155724"
  success-border: "#1e7e34"
  info-bg: "#abdde5"
  info-text: "#0c5460"
  info-border: "#117a8b"
  warning-bg: "#ffe8a1"
  warning-text: "#856404"
  warning-border: "#d39e00"
  danger-bg: "#f1b0b7"
  danger-text: "#721c24"
  danger-border: "#bd2130"
  link: "#3e84b6"
  link-active: "#0062cc"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase
  breadcrumb:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 44px
    opacity: 0.65
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: 9px 19px
    height: 44px
  button-success:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 44px
  button-success-active:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 44px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 14px
    height: 34px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 40px
    focusBorder: "1px solid {colors.primary}"
    focusOutline: "0 0 0 3px {colors.primary-disabled}"
    placeholderColor: "{colors.muted}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.danger-border}"
    padding: 8px 12px
    height: 40px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 40px
    appearance: auto
  nav-bar:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: none
    logoArea: 160px
  nav-top-utility:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-light}"
    typography: "{typography.caption}"
    height: 32px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    shadow: "0 4px 12px rgba(0,0,0,0.12)"
    padding: "{spacing.sm} 0"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    shadow: none
    padding: "{spacing.base}"
    imageAspect: 1/1
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    captionTypography: "{typography.body-sm}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    shadow: "0 2px 8px rgba(62,132,182,0.18)"
  hero:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 320px
    padding: "{spacing.xxl} 0"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaButton: "button-primary"
  hero-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 200px
    padding: "{spacing.xl} 0"
    headlineTypography: "{typography.display-md}"
    subTypography: "{typography.body-sm}"
  category-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    hoverBorder: "1px solid {colors.primary}"
    hoverBackground: "{colors.surface-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 {spacing.base}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.none}"
  breadcrumb-nav:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.breadcrumb}"
    separator: "/"
    separatorColor: "{colors.muted-light}"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.success-border}"
    padding: "{spacing.base}"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.info-border}"
    padding: "{spacing.base}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.warning-border}"
    padding: "{spacing.base}"
  alert-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.danger-border}"
    padding: "{spacing.base}"
  status-badge-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  status-badge-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  status-badge-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  price-calculator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.label}"
    totalTypography: "{typography.price-display}"
    totalColor: "{colors.primary-dark}"
  order-summary-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    lineTypography: "{typography.body-sm}"
    totalTypography: "{typography.price-sm}"
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.muted-light}"
    linkColor: "#b8daff"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.xxl} 0"
    borderTop: "4px solid {colors.accent}"
  pagination:
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.primary}"
    inactiveBorder: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    minWidth: 36px

## Components

### Buttons

**`button-primary`** — Solid #3e84b6 background with white labels at 16px/600 weight Arial, 4px radius, 44px height. On hover the background darkens to #0062cc; disabled state drops to #b3d7ff at 65% opacity. Used for "Get a Quote", "Add to Cart", and configuration confirmations throughout the product flow.

**`button-success`** — The accent green #8cc63f with white text, same sizing as `button-primary`. This button appears specifically on checkout completion, proof approval, and file upload success — it visually signals that a print job is moving forward. Active state darkens to #1e7e34.

**`button-secondary`** — White background with #3e84b6 border and label, matching the `button-primary` dimensions but inset by 1px to account for border. Used for secondary actions alongside a primary: "Save for Later", "Download Proof", "Continue Shopping". Hover fills the background with a soft #f0f4f7 tint.

**`button-sm`** — Compact 34px tall blue button at 14px/600 weight for inline actions inside product cards and data tables (e.g., "View Details", "Reorder").

### Text Inputs & Forms

**`text-input`** — White field at 40px height with 1px #dae0e5 border and 4px radius. Focus ring is a 3px spread of #b3d7ff blue — a soft, approachable focus rather than a sharp outline. Error state swaps the border to #bd2130 without changing radius or padding. Placeholders render in #818182.

**`select-input`** — Same dimensions and border treatment as `text-input`, using the browser native select dropdown. No custom chevron override detected; relies on OS-default appearance for consistency across the heavily form-driven configurator pages.

**`price-calculator`** — A surface-soft #f0f4f7 panel housing the quote engine: quantity selectors, paper stock dropdowns, turnaround pickers, and a live total rendered in `price-display` (28px/700) in #004085 navy. Contained in a 8px-radius card with a hairline border to distinguish it from the page canvas.

### Navigation

**`nav-bar`** — A 56px navy (#004085) horizontal bar with white nav-link labels at 15px/500. The GotPrint logo sits in a fixed 160px left zone. Product categories expand into a `nav-dropdown` white panel with hairline borders. Above this bar, a 32px utility strip in #1d2124 near-black carries account links, tracking, and contact at 12px caption weight.

**`nav-dropdown`** — White surface with 4px radius, 1px #dae0e5 border, and a `0 4px 12px rgba(0,0,0,0.12)` shadow. Items render in body-sm (14px/400) with #3e84b6 hover text and a transparent hover background to maintain the panel's lightness.

### Product Discovery

**`product-card`** — White card with 1px #dae0e5 border, 4px radius, and flat shadow. On hover the border transitions to #3e84b6 and a soft 8px blue shadow lifts the card. Title in 16px/600, price in 18px/700, supporting copy in 14px/400. Product image fills a square 1:1 aspect region at top.

**`category-tile`** — A white bordered panel with centered product-category label in #3e84b6 at title-sm weight, used on the homepage grid for "Business Cards", "Flyers", "Banners", etc. Hover state fills background with #f0f4f7 and intensifies the border to full primary blue.

**`search-bar`** — Full-width 44px input at the top of category pages. The submit button attaches directly to the right edge with no gap, solid #3e84b6 fill and a zero-radius right join — creating a merged pill-of-sorts without the pill shape: rectangular, utilitarian.

### Status & Feedback

**`alert-success / alert-warning / alert-danger / alert-info`** — Full Bootstrap 4 alert quartet. Success (#b1dfbb bg, #155724 text), info (#abdde5 bg, #0c5460 text), warning (#ffe8a1 bg, #856404 text), danger (#f1b0b7 bg, #721c24 text). All share 4px radius, 16px padding, and 1px matching-dark-tone borders. These are not decorative — they carry file validation errors, turnaround deadline notices, and upload status messages that are central to the user workflow.

**`status-badge-success / status-badge-warning / status-badge-danger`** — Compact inline badges with the same color pairings as the alerts, at 12px/700 uppercase. Used inside order tables to show job status ("Proof Approved", "Awaiting Payment", "In Production").

### Order & Checkout

**`order-summary-card`** — White card with hairline border summarizing line items, quantities, and totals. Title in title-md (18px/600), line items in body-sm (14px/400), subtotal/total in price-sm (18px/700). Sits fixed in the right column during the checkout flow.

**`pagination`** — Active page in solid #3e84b6 with white label; inactive pages are white with hairline border and blue text. 36px square minimum touch target, 4px radius. Used on product listing and order history pages.

### Footer

**`footer`** — Navy #004085 background mirroring the nav, with a 4px top accent stripe in #8cc63f green — the only place the accent green appears as a decorative element rather than a functional one. Column headings in on-dark white at title-sm weight; body links in #b8daff light blue at 14px/400. Bottom subrow holds legal links and copyright in muted-light #c8cbcf.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger menu over navy bar; hero stacks headline above CTA; price calculator becomes full-width sticky footer panel; product cards 1-up |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + hamburger; hero retains side-by-side layout at reduced font sizes; order summary card moves below product configurator |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav at 56px; hero at full display-xl sizing; configurator + summary card in 8/4 column split |
| Wide | > 1440px | Grid max-width caps at ~1320px centered; hero background extends full bleed; no additional columns added beyond desktop layout |

### Touch Targets
- All buttons minimum 44px tall, 44px wide
- Nav links in collapsed mobile menu pad to 48px row height
- Pagination controls minimum 36×36px
- Form inputs 40px height with adequate label spacing above

### Collapsing Strategy
- Primary nav collapses hamburger-first; utility strip hides completely on mobile
- Product category tiles reflow from 4-column to 2-column to 1-column
- Price calculator moves from right-column sidebar to below configurator on tablet, sticky bottom sheet on mobile
- Footer columns stack vertically on mobile, maintaining the green top accent stripe
- Breadcrumb truncates middle segments with ellipsis on narrow viewports

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected — full system font stack (Arial, Helvetica, Roboto, -apple-system) with no web font loading observed; if GotPrint loads a custom font via JS or CDN post-render, it was not captured
- No meta theme-color defined, so mobile browser chrome color is unspecified
- Many extracted colors (#155724, #0c5460, #856404, #721c24, #b1dfbb, #abdde5, #ffe8a1, #f1b0b7) are Bootstrap 4 alert/badge utility colors rather than deliberate brand tokens — their usage is functional rather than expressive
- Exact weight and frequency of #8cc63f green in production UI not confirmed; may be used more narrowly than inferred
- Motion, animation, and transition timing data not captured
- Icon library and glyph style (outline vs filled, stroke weight) not identified from extraction
- Print preview / proof viewer UI components not characterized — likely the most complex and brand-specific surface on the site
- Dark mode support unknown; no prefers-color-scheme tokens observed
