---
version: alpha
name: "Simplicity"
source_url: "https://www.simplicityvac.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The #00b5d1 teal that anchors Simplicity's interface reads less like a brand color and more like the indicator light on the machine itself — poolwater-bright against a near-black #242424 grid, marking every active CTA, hover ring, and navigation state while the surrounding layout stays deliberately flat. The tagline "Simply Powerful" is not decoration; it is a layout constraint. Pages are wide, uncluttered corridors of product photography where Gotham headings label rather than persuade, and the chrome stays out of the way.

  Gotham A and Gotham B carry all display and UI text — a geometric sans-serif that reads like hardware labeling at heavy weights and relaxes at book weight for body copy. Open Sans handles supplemental paragraphs where Gotham steps back. SignPainter surfaces as a script accent in promotional banners and sale callouts — a brief handwritten flourish against the machined geometry of Gotham's circles, the only decorative gesture the brand permits itself. The contrast is intentional and controlled.

  Urgency is layered through a warm amber pair (#c07600 ink on #fdf0d5 ground) for sale pricing callouts and a contained #e02b27 for error states and clearance badges. Neither warm tone appears in layout chrome — they are strictly badge-and-price-moment colors. The navigation bar runs at a deep #1a1a1a with teal active underlines, giving the header the density of an appliance control panel. Product cards sit on #f6f6f6 with #e8e8e8 borders and {rounded.xs} corners — barely softened, rectilinear, matching the geometry of the vacuums they present.

  Section breaks hold at 64px, compressing to 8–12px within card grids. Touch targets floor at 44px. The result sits between appliance documentation and clean-room product photography: systematic enough for a full catalog, confident enough to let the machines carry the visual weight.

colors:
  primary: "#00b5d1"
  primary-active: "#037fa5"
  primary-disabled: "#b3b3b3"
  link: "#1979c2"
  error: "#e02b27"
  promo-ink: "#6f4400"
  promo-text: "#c07600"
  promo-bg: "#fdf0d5"
  ink: "#242424"
  body: "#303030"
  muted: "#7d7d7d"
  muted-soft: "#bbbbbb"
  hairline: "#e8e8e8"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#fcfcfc"
  nav-dark: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Open Sans', 'Gotham A', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Gotham A', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  label-uppercase:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  promo-script:
    fontFamily: "'SignPainter', cursive"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  button-md:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Gotham A', 'Gotham B', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
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
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 44px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
    hoverBackgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 10px 16px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 3px
    padding: "0 {spacing.xl}"
  nav-top-utility:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageRatio: "4/3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    badgePosition: top-left
    hoverBoxShadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaComponent: button-primary
    imagePosition: right
    minHeight: 480px
  promo-banner:
    backgroundColor: "{colors.promo-bg}"
    textColor: "{colors.promo-ink}"
    scriptAccentColor: "{colors.promo-text}"
    scriptTypography: "{typography.promo-script}"
    labelTypography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
    borderBottom: "2px solid {colors.promo-text}"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-clearance:
    backgroundColor: "{colors.promo-bg}"
    textColor: "{colors.promo-ink}"
    border: "1px solid {colors.promo-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    iconColor: "{colors.primary}"
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
  category-tab:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 3px
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    activeTextColor: "{colors.ink}"
  feature-icon-block:
    backgroundColor: "{colors.surface-soft}"
    iconColor: "{colors.primary}"
    iconSize: 48px
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  price-regular:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-sale:
    textColor: "{colors.error}"
    typography: "{typography.price-display}"
  price-original-struck:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textDecoration: line-through
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.muted}"
    linkColor: "{colors.primary}"
    linkHoverColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary CTA runs in #00b5d1 with white Gotham type set in all-caps at 14px with 0.5px tracking. On hover the fill deepens to #037fa5 ({colors.primary-active}); disabled state drops to #b3b3b3. Corner radius holds at {rounded.xs} — 4px, almost flush, keeping the rectilinear geometry of the machines being sold. Used for Add to Cart, Find a Dealer, and primary form submits.

**`button-secondary`** — White fill with a 2px {colors.primary} border and matching teal text label. Background shifts to {colors.surface-soft} on hover. Same uppercase Gotham {typography.button-md}, same {rounded.xs} corners. Used for Compare, Learn More, and secondary page actions where the primary slot is already occupied.

**`button-ghost`** — Transparent field with {colors.ink} text and no border. Sized identically to other buttons for layout alignment. Used inside cards for tertiary actions like Save to Wishlist or See All Models.

### Text Input & Search
**`text-input`** — 44px tall, 1px {colors.hairline} border at rest, upgrading to 2px {colors.primary} on focus. Placeholder text renders in {colors.muted}. {rounded.xs} corners throughout. Used across account forms, checkout, and dealer-finder flows.

**`search-bar`** — A text input left-joined to a {colors.primary} submit button carrying a search glyph in {colors.on-primary}. The teal block makes the search entry impossible to overlook against the dark nav bar. Focus ring is 2px {colors.primary}. On mobile the bar drops full-width below the logo row.

### Navigation
**`nav-bar`** — 60px tall, {colors.nav-dark} (#1a1a1a) background. Category links in {typography.nav-link} at white. The active link receives a 3px {colors.primary} underline at the bottom edge — the teal bar reads like a cursor on a control panel readout. Account and cart icons anchor the trailing end.

**`nav-top-utility`** — A 36px utility strip above the main nav in {colors.ink} background with {typography.caption} text in {colors.muted-soft}. Carries the free-shipping threshold message, dealer locator link, and a phone number. Hidden on mobile viewports.

### Product Card
**`product-card`** — {colors.surface-card} field with 1px {colors.hairline} border and {rounded.xs} corners. Product image displays at a 4:3 ratio. Title in {typography.title-md}, price in {typography.price-display}. On hover the card lifts with a subtle box-shadow. Badge chips (Sale, New, Clearance) pin to the top-left corner of the image region.

### Hero Banner
**`hero-banner`** — Full-width {colors.surface-soft} band, headline in {typography.display-xl} at left, product photography at right, single primary CTA below the headline. Min-height 480px on desktop. Image collapses below the text block on mobile. No decorative overlays or gradient scrim — the machine photograph stands unobstructed.

### Promo Banner
**`promo-banner`** — A full-bleed #fdf0d5 strip with #6f4400 label text and {typography.promo-script} SignPainter headline for the offer amount (e.g. "Save $50"). A 2px #c07600 border anchors the bottom edge. {rounded.none} — runs wall to wall. Used site-wide for seasonal campaigns and clearance events; the amber warmth is immediately distinct from the teal primary system.

### Badges
**`badge-sale`** — #e02b27 fill, white all-caps {typography.badge}, {rounded.xs}. 3px 8px padding. Compact and high-contrast.

**`badge-new`** — #00b5d1 fill, identical specs. Signals product freshness in the brand's primary teal.

**`badge-clearance`** — #fdf0d5 fill with 1px #c07600 border and #6f4400 text. Warm-amber containment distinguishes clearance from sale without competing with the teal badge system.

### Feature Icon Block
**`feature-icon-block`** — {colors.surface-soft} tile, 48px {colors.primary} icon centered above a {typography.title-md} heading and {typography.body-sm} body paragraph. {rounded.sm} corners, {spacing.lg} internal padding. Used in "Why Simplicity" and "Key Features" grids, typically 3-up or 4-up on desktop, collapsing to 2-up on tablet and 1-up on mobile.

### Pricing
**`price-regular`** — {typography.price-display} in {colors.ink}. **`price-sale`** — same scale in {colors.error} (#e02b27). **`price-original-struck`** — {typography.body-sm} in {colors.muted} with line-through. The three-part cluster (struck original, red sale, amber badge) forms the standard promotional price unit on product cards and PDPs.

### Footer
**`footer`** — {colors.ink} (#242424) background with a 3px {colors.primary} top border as the brand's closing accent. Link columns in {typography.body-sm} white, section headers in {typography.label-uppercase} teal. Social icons and legal links render in {colors.muted}. The teal top border echoes the nav active indicator, framing the page as a complete system.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero image stacks below headline block; nav collapses to hamburger icon; utility strip hidden; promo banner text reduces to 20px script |
| Tablet | 744–1128px | 2-column product grid; hero shows cropped image at right; main nav shows top-level categories, sub-nav in flyout drawer |
| Desktop | 1128–1440px | 3-column product grid; full nav bar and utility strip visible; hero at full 480px min-height; feature blocks 4-up |
| Wide | > 1440px | Content max-width 1440px centered; hero image scales proportionally; product grid stays 3–4 columns with wider gutters |

### Touch Targets
- All interactive controls minimum 44×44px
- Nav links hold 44px tap height even when rendered at 14px type
- Badge chips are display-only; no tap target requirement applies
- Search submit button maintains 44px height inside the compound search-bar

### Collapsing Strategy
- Primary nav collapses to hamburger at < 744px; utility strip removed entirely on mobile
- Product filters shift from left sidebar (desktop) to a bottom-sheet modal (mobile)
- Feature icon grid: 4-up → 2-up → 1-up across desktop → tablet → mobile
- Hero image hidden below 480px viewport height to preserve headline legibility
- Promo banner SignPainter script scales from 28px (desktop) to 20px (mobile) to prevent text overflow
- Category tabs scroll horizontally on mobile rather than wrapping

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values from live extraction; {rounded.xs} = 4px is inferred from the brand's rectilinear product aesthetic
- No confirmed Gotham font weights in use — 600 and 700 are standard Gotham family variants; verify against the actual font license and CSS delivery
- No confirmed button padding or height from extraction; 44px floor follows WCAG 2.5.5 minimum touch target guidance
- The blues #1979c2, #135d95, #003399, #499bf8 likely originate from the platform's default link and interactive-state CSS rather than defined brand tokens; {colors.link} at #1979c2 is used conservatively and should be verified
- #00b5de appears alongside #00b5d1 — the two teal variants may represent hover/active states or simply anti-aliasing artifacts; extraction cannot distinguish; #00b5d1 is designated primary
- No dark-mode or alternate theme tokens detected — site appears to be single-theme only
- No confirmed icon library or icon style; product imagery extraction did not yield icon set details
- SignPainter font confirmed present in the stack but its exact sizing and color application is inferred from common DTC promotional patterns, not direct pixel extraction
