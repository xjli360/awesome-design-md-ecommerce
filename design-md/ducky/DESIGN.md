---
version: alpha
name: "Ducky"
source_url: "https://www.duckychannel.com.tw"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The golden #ecb320 operates as the sole voltage signal across a near-black envelope — every primary CTA, active navigation state, and price callout channels through one amber frequency against chassis backgrounds of #101010 and #111111 that cover roughly 80% of the visible canvas. What makes the palette structurally unusual is that the remaining accent spectrum — #c72d00 crimson, #31862d forest green, #07ccd7 cyan-teal — maps directly onto mechanical switch taxonomy: crimson for linear switches, green for clicky switches, cyan for bump-feedback variants. The brand's most decisive design move is using its own product's specification language as a color-coding system; switch-type indicator badges inherit their hue from the physical switch rather than from an arbitrary brand library.

  Type runs Montserrat for display and navigation at weights 600–800, giving product names the compressed visual density appropriate to a hardware catalog. Inter handles body copy and UI chrome at 400–500 weight, with Ubuntu appearing in secondary utility and monospace-adjacent roles. The hierarchy is deliberately binary: display titles hit 40–48px on hero sections with tracking around −0.5px, then step directly to 16–18px for card product names — almost no editorial mid-range exists between headline-scale and utility-scale copy. This compressed typographic range keeps attention on photography rather than hierarchy navigation.

  Corner radii are restrained — 4px on buttons and inputs — keeping the product aesthetic closer to precision hardware than lifestyle consumer goods. The one exception is {rounded.full} on small switch-type indicator pills, where the round-versus-rectangle contrast between badge and card frame creates an information hierarchy without additional typography. Product cards sit on #1f1f1f surfaces with #343434 hairline borders, letting keyboard photography carry the visual load without decorative interference from container shapes.

  Section spacing ({spacing.section}, 64px+) is generous because dramatic-angle keyboard hero photography needs room to establish mood before the specification grid begins. The footer collapses into a tight dark band that continues {colors.canvas} without a background change, preserving the near-black envelope that characterizes the entire brand surface. Secondary amber variants — #f7b829, #eebd3c, #ffcc00 — form a warm cluster used for hover states, promotional accents, and rating elements, preventing the primary #ecb320 from feeling isolated as a single-point-of-warmth.

colors:
  primary: "#ecb320"
  primary-active: "#f7b829"
  primary-hover: "#eebd3c"
  primary-disabled: "#78766f"
  on-primary: "#111111"
  ink: "#f5f5f5"
  body: "#c7c7c7"
  muted: "#78766f"
  hairline: "#343434"
  canvas: "#101010"
  surface-soft: "#1a1a1a"
  surface-card: "#1f1f1f"
  surface-raised: "#2b2b2b"
  switch-red: "#c72d00"
  switch-green: "#31862d"
  switch-cyan: "#07ccd7"
  accent-red: "#dd4242"
  promo-yellow: "#ffcc00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Montserrat, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Montserrat, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Montserrat, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Montserrat, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "Inter, Ubuntu, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, Ubuntu, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, Ubuntu, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  label-mono:
    fontFamily: "Ubuntu, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "Montserrat, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Montserrat, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  switch-badge:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  price-display:
    fontFamily: "Montserrat, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoAccentColor: "{colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    minHeight: 560px
    overlayGradient: "linear-gradient(90deg, rgba(16,16,16,0.85) 0%, rgba(16,16,16,0.2) 60%, transparent 100%)"
    ctaSpacing: "{spacing.xl}"
  switch-badge-base:
    typography: "{typography.switch-badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  switch-badge-red:
    backgroundColor: "{colors.switch-red}"
    textColor: "#ffffff"
    typography: "{typography.switch-badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  switch-badge-green:
    backgroundColor: "{colors.switch-green}"
    textColor: "#ffffff"
    typography: "{typography.switch-badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  switch-badge-cyan:
    backgroundColor: "{colors.switch-cyan}"
    textColor: "{colors.canvas}"
    typography: "{typography.switch-badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderUnselected: "2px solid transparent"
    gap: "{spacing.xs}"
  product-specs-row:
    backgroundColor: "{colors.surface-soft}"
    borderBottom: "1px solid {colors.hairline}"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    padding: "12px {spacing.base}"
  keycap-legend-tag:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.body}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    iconColor: "{colors.primary}"
    height: 44px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.switch-badge}"
    rounded: "{rounded.full}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "#ffffff"
    typography: "{typography.switch-badge}"
    rounded: "{rounded.full}"
    padding: "3px 8px"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Gold (#ecb320) fill against the near-black surface, uppercase Montserrat at 14px/700 with 0.5px tracking. The 4px radius ({rounded.xs}) keeps the shape decisively rectangular — pill shapes would undercut the hardware precision aesthetic. Hover shifts to `button-primary-hover` using #f7b829 (a fractionally warmer amber); disabled state collapses to the warm gray muted token (#78766f) with {colors.canvas} text, reading as inert without requiring opacity tricks.

**`button-secondary`** — Transparent background with a {colors.hairline} border (#343434) and {colors.ink} text, identical padding and radius to `button-primary` for side-by-side parity. Hover fills to {colors.surface-raised} (#2b2b2b) without changing the border, preserving the outline silhouette while communicating state. Used for secondary actions like "Learn More" or spec-sheet downloads alongside gold purchase CTAs.

### Navigation

**`nav-bar`** — 64px dark bar at {colors.canvas} (#101010) with a {colors.hairline} bottom separator. Navigation links in {typography.nav-link} (Montserrat 14px/600, 0.3px tracking). The Ducky wordmark uses {colors.primary} as the accent, making the logo the only warm element in an otherwise neutral-dark header. Active category states highlight in {colors.primary} gold rather than underline, consistent with the brand's single-voltage approach.

**`announcement-bar`** — Full-width {colors.primary} band above the nav at 36px height, carrying promotional copy in {typography.button-sm} uppercase Montserrat in {colors.on-primary} (#111111 dark text on gold). The inverted contrast — gold-on-black nav bar below, black-on-gold announcement strip above — creates an immediate visual entry hierarchy that signals the brand color twice before the user sees a single product.

### Product Cards

**`product-card`** — Rendered on {colors.surface-card} (#1f1f1f) with a {colors.hairline} border and {rounded.sm} corners. Product name in {typography.title-md} (Montserrat 18px/600), price in {typography.price-display} (22px/700) colored {colors.primary} gold. Switch-type badges from the `switch-badge-*` family float above the product name, color-coding the listing by switch family — the card communicates switch type without a single word of prose copy in the badge label beyond the color signal itself.

### Switch Badges

**`switch-badge-red / green / cyan`** — Pill-shaped ({rounded.full}) micro-labels in {typography.switch-badge} (Inter 11px/600, all-caps, 0.4px tracking). Crimson (#c72d00) for linear switches, green (#31862d) for clicky, cyan (#07ccd7) for bump-feedback variants. These are the only fully-rounded elements in the entire component set — using round-versus-rectangle contrast between badge and card frame to signal "specification tag" rather than "interactive element." The palette here is borrowed directly from the physical switches, not from a brand color library.

### Hero

**`hero`** — Full-bleed keyboard photography at minimum 560px height with a left-anchored gradient overlay (rgba(16,16,16,0.85) at 0% to transparent at 60%). Display copy in {typography.display-xl} (Montserrat 48px/800, −0.5px tracking) renders in {colors.ink} (#f5f5f5) over the dark overlay zone. The right 40% of the frame is unobscured keyboard photography, making the product the dominant visual rather than the headline. A {colors.primary} CTA button sits below the headline with {spacing.xl} separation from the subhead.

### Color Swatch Picker

**`color-swatch`** — 24px circles ({rounded.full}) for keycap colorway selection. Selected state gains a 2px {colors.primary} ring with a 2px gap between ring and swatch fill, a standard "ring offset" pattern that keeps the swatch color visible. Unselected swatches carry a transparent border. Swatches sit {spacing.xs} (4px) apart in a horizontal flex row below the product title, accommodating six or more colorway options before overflow.

### Specification Table

**`product-specs-row`** — Two-column rows on {colors.surface-soft} (#1a1a1a), separated by {colors.hairline} bottom borders. Left column: spec label in {typography.title-sm} (Montserrat 13px/600, uppercase, {colors.muted}). Right column: spec value in {typography.body-sm} (Inter 14px/400, {colors.ink}). The alternating rhythm between rows is subtle — surface-soft (#1a1a1a) and canvas (#101010) are only marginally different — so the hairline carries most of the visual separation work.

### Keycap Legend Tag

**`keycap-legend-tag`** — Ubuntu monospace 13px/500 rendering keycap text (e.g., "ESC", "F1–F12") inside a 1px {colors.hairline}-bordered box on {colors.surface-raised}. Used in product detail sections to visually replicate the physical keycap legend in the spec description zone. The monospace face (Ubuntu) differentiates these tags from all other UI text, signaling "hardware label" without requiring an icon asset.

### Search Bar

**`search-bar`** — Matching height and radius to `text-input` for consistency across the form system. The search icon renders in {colors.primary} gold at rest rather than {colors.muted} — an active affordance that signals the field's purpose before interaction. On focus, the border transitions from {colors.hairline} to {colors.primary}, completing the gold-focus pattern used across all interactive inputs.

### Badges

**`badge-new`** — {colors.primary} gold pill with {colors.on-primary} dark text, using the same {typography.switch-badge} scale as switch indicators for visual family consistency. **`badge-sale`** — {colors.accent-red} (#dd4242) pill with white text, distinguishable from the switch-badge-red (#c72d00) by its softer, lighter red. Both badges use {rounded.full} and sit in the same spatial position as switch badges above the product name.

### Footer

**`footer`** — Continues {colors.canvas} (#101010) without a background shift, separated from content only by a {colors.hairline} top border. Column headings in {typography.title-sm} (Montserrat uppercase, {colors.ink}). Body links in {typography.body-sm} (Inter 14px) at {colors.muted} (#78766f) resting, transitioning to {colors.primary} gold on hover — the only interactive affordance in the footer zone, keeping the amber signal consistent to the page bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero drops to 320px min-height with overlay covering full width; nav collapses to logo + hamburger; announcement bar truncates to one line; switch badge row scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; hero text column at 55% width; nav shows primary categories only, secondary links in overflow menu; color swatch row wraps to two rows if needed |
| Desktop | 1128–1440px | Three-column product grid; full nav with all category links visible; hero at 560px min-height with left-gradient layout; spec table two columns at full width |
| Wide | > 1440px | Four-column product grid; hero and content max-width caps at 1440px with padding expansion; section spacing scales from {spacing.section} to 80px |

### Touch Targets
- All buttons minimum 48px height on mobile
- Color swatches scale to 32px diameter on mobile (from 24px desktop)
- Switch badge pills gain 12px vertical padding on mobile to increase tap area
- Nav hamburger icon minimum 44×44px tap target
- Spec table rows minimum 48px height on mobile for tappable accordion headers

### Collapsing Strategy
- Product specification table collapses to accordion on mobile — each spec group is a tappable row that expands in place
- Switch badge row scrolls horizontally on mobile rather than wrapping to second line
- Color swatch picker caps at 6 visible swatches with "+N more" overflow chip on mobile
- Hero subhead text hides below 480px to reduce cognitive load on small screens
- Footer columns collapse to a single stacked list with disclosure chevrons on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font detected — Montserrat, Inter, and Ubuntu are all Google Fonts; any licensed custom cuts or weight-specific hinting are unknown
- Dark-mode vs. light-mode split unverified — near-black canvas is inferred from the extracted color distribution; whether the site switches to a light canvas for specific page zones (e.g., editorial or blog sections) is unknown
- Meta theme-color was absent, so PWA and mobile browser chrome color is unspecified
- Exact button corner radius from the live site unconfirmed — 4px ({rounded.xs}) is an inference from hardware-brand norms, not extracted CSS
- Animation timing and easing curves not extractable — hover and active transition durations are unspecified
- Grid column counts and gutter widths not extracted from layout CSS
- Full keycap colorway swatch palette extends well beyond the 20 extracted hex values — Ducky ships dozens of colorways that likely introduce many additional swatches not represented here
- Cart drawer, quantity selector, and checkout component styling not captured
- Product comparison table (if present) layout and behavior not verified
