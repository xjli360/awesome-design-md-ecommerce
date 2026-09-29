---
version: alpha
name: "Heron"
source_url: "https://www.heronwatches.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The theme color — #211f1e — sits a degree warmer than neutral black, reading like a vintage darkroom under incandescent light rather than a cold void. Héron Watch Co. builds its entire digital environment inside this single warm shadow, layering it with #1c1d1d panels and #141212 card wells until the depth feels physical rather than flat. Against that atmosphere, the brand's singular accent — a vivid orange-red at #ff4f33 — performs the same optical work a lume application does on a dark dial: a single precisely placed signal that reads immediately without disturbing the surrounding calm.

  Typography divides cleanly between two faces. Montserrat handles all display and navigation at tracked-out uppercase settings — no lower-case headings, no soft wordmark treatment — giving the brand the same finish a machined case edge gives a watch: precise, non-negotiable. Barlow steps in for body copy and specification panels, its legible construction matching the factual register of case diameter, lug width, and movement caliber. Together they produce a voice that never ornaments: it names, specifies, declares.

  Radii are hard or absent throughout. Where friendlier commerce brands use pill shapes to signal approachability, Héron favors `{rounded.none}` on buttons, cards, and inputs — corners as sharp as a case-back seam. Spacing respects the hierarchy of information: specification grids breathe at `{spacing.base}` intervals, hero panels push to `{spacing.section}` top padding, and a 2px ember-colored left border on watch detail panels marks the focal column without requiring any additional graphical weight.

  The announcement bar pulls #ff4f33 across the full viewport width — a compressed horizontal band that uses the accent as a utility signal (sale threshold, limited drop, waitlist) rather than decorating with it. CTAs on the product page are flat rectangles, `{rounded.none}`, filled with the same #ff4f33, ensuring the eye's path from hero image to purchase is lit by the same color temperature as a single pilot light on a dark panel. The `{colors.primary-active}` state drops to a deep crimson (#c20000), reinforcing that this brand's color vocabulary contains no pastels, no gradients — only signal and shadow.

colors:
  primary: "#ff4f33"
  primary-active: "#c20000"
  primary-disabled: "#3c3836"
  ink: "#f0eeed"
  body: "#e9e8e7"
  muted: "#444444"
  muted-soft: "#3e3e3e"
  hairline: "#3c3836"
  canvas: "#211f1e"
  surface-soft: "#1c1d1d"
  surface-card: "#141212"
  surface-raised: "#323232"
  on-primary: "#f7f6f5"
  on-dark: "#f0eeed"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: 0.06em
    textTransform: uppercase
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0.05em
    textTransform: uppercase
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  body-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.14em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.14em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  logo-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: 0.2em
    textTransform: uppercase
  spec-label:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  price:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.02em

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.logo-display}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    minHeight: 90vh
  watch-detail-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    specLabelTypography: "{typography.spec-label}"
    specValueTypography: "{typography.body-sm}"
    accentBorder: "2px solid {colors.primary}"
    padding: "{spacing.xl}"
  spec-grid:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted-soft}"
    valueColor: "{colors.body}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.base}"
    rowGap: "{spacing.md}"
  badge-limited:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  badge-sold-out:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    height: 36px
    textAlign: center
  collection-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    activeColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — A flat-fill rectangle with `{rounded.none}` hard corners, ember orange-red background (`{colors.primary}` #ff4f33), and all-caps Montserrat at 700 weight, 0.14em letter-spacing. The geometry echoes a watch pusher or crown — mechanical, purposeful, zero softening. On hover the fill drops to `{colors.primary-active}` (deep crimson, #c20000); disabled state renders the same shell in a near-invisible `{colors.primary-disabled}` fill with `{colors.muted}` label text rather than fading opacity. This is the only element on the page that carries the orange-red at full weight.

**`button-secondary`** — Transparent fill with a 1px border in `{colors.ink}` (#f0eeed) against the dark canvas, creating a ghost rectangle that holds its shape without competing with the primary CTA. Hover state fills with `{colors.surface-raised}` (#323232), a barely perceptible elevation. Used for secondary actions — "View Specs," "Compare," "Notify Me" — where the orange-red must remain singular. Typography is identical to `{typography.button-md}` to maintain optical balance between paired actions.

### Navigation

**`nav-bar`** — 64px tall, fixed on scroll, sitting on `{colors.canvas}` and separated from page content by a 1px `{colors.hairline}` line that reads as a machined edge rather than a design flourish. All navigation links use `{typography.nav-link}` (11px Montserrat, 600 weight, 0.12em spacing, uppercase). The wordmark uses `{typography.logo-display}` (0.2em letter-spacing, 800 weight), spacing the brand name wide enough that each character registers individually — a detail borrowed from watch-dial typography conventions where legibility at small sizes demands generous tracking. No drop shadow on scroll; the dark ambient canvas provides its own visual separation.

### Product Card

**`product-card`** — Zero-radius card on `{colors.surface-card}` (#141212), the deepest level of the warm dark palette. A 1px `{colors.hairline}` border defines the perimeter. Watch photography fills the full card width with no interior padding, edge-to-edge; below the image, the product name renders in `{typography.title-md}` (uppercase Montserrat) and price in `{typography.price}` (20px Barlow, 500 weight). Limited-edition flags layer over the image corner using `badge-limited`. Sold-out watches render the same card shell with `badge-sold-out` and the CTA replaced by a static text label in `{colors.muted}`, preserving the grid rhythm without orange-red urgency for unavailable pieces.

### Watch Detail Panel

**`watch-detail-panel`** — The primary product-page layout component, split 60/40 between photography and specification on desktop. A 2px left border in `{colors.primary}` marks the spec column — the only vertical line of color in an otherwise monochrome composition, functioning like the red seconds hand on a tool watch: optional to most eyes, unmissable once you find it. Title renders in `{typography.display-md}`; specification row labels use `{typography.spec-label}` (11px Barlow, uppercase, 0.08em tracking) against values in `{typography.body-sm}`. The contrast between Montserrat for the watch name and Barlow for its technical specifications mirrors a dial where the brand name and printed markings occupy distinct typographic registers.

### Spec Grid

**`spec-grid`** — A two-column table inset inside the detail panel, set on `{colors.surface-soft}`. Labels render in `{colors.muted-soft}` (#3e3e3e), values in `{colors.body}` (#e9e8e7), each row separated by a `{colors.hairline}` line. Standard rows cover: case diameter, lug width, thickness, lug-to-lug, water resistance rating, movement caliber, crystal material, and strap material. Padding is `{spacing.base}` on all sides with `{spacing.md}` row gap. On mobile the grid collapses to a single-column stacked list.

### Hero Banner

**`hero-banner`** — Full-bleed panel, minimum 90vh, with the headline in `{typography.display-xl}` (52px Montserrat, 700 weight, 0.06em tracking, all caps) printed over watch photography. No scrim overlay — the brand relies on photograph darkness to provide direct contrast, keeping the atmosphere continuous rather than layered. Subhead in `{typography.body-md}` uses `{colors.body}` (#e9e8e7) for slightly reduced luminosity against the dark. The single CTA is `button-primary`. On mobile the headline steps down to `{typography.display-sm}` and the button extends to full container width.

### Announcement Bar

**`announcement-bar`** — A 36px strip pinned above the nav in `{colors.primary}` (#ff4f33), centered `{typography.button-sm}` label in `{colors.on-primary}`. Carries limited-edition drop alerts, production-run countdowns, free-shipping thresholds, or waitlist confirmations. This is the loudest element on the page by design — it occupies the maximum viewport width and holds the brand's most vivid color while the rest of the page stays in shadow. On mobile it can be dismissed to a slide-up state.

### Badges

**`badge-limited`** — Flat rectangle, `{rounded.none}`, `{colors.primary}` fill with `{colors.on-primary}` label in `{typography.button-sm}`. Overlaid top-left on product card images for limited-edition and first-run designations. **`badge-sold-out`** — Identical geometry, `{colors.surface-raised}` fill, `{colors.muted}` text. Communicates unavailability without invoking the orange urgency signal; the neutral gray reads as a mechanical state rather than a disappointment.

### Collection Filter

**`collection-filter`** — Flat tag buttons on `{colors.surface-soft}`, `{rounded.none}`, 1px `{colors.hairline}` border. Active filter highlights with `{colors.primary}` left border accent (2px) rather than a fill change, maintaining the dark ambient feel across selected and unselected states. Uses `{typography.body-sm}` rather than the uppercase Montserrat treatment, keeping filter interactions in the reading register rather than the labeling register. Padding `{spacing.sm}` vertical, `{spacing.base}` horizontal.

### Footer

**`footer`** — Sits on `{colors.surface-card}` (#141212) with a 1px `{colors.hairline}` top border. Column headings use `{typography.title-sm}` (uppercase Montserrat, 0.12em tracking) in `{colors.ink}`; links use `{typography.body-sm}` in `{colors.muted-soft}`, stepping up to `{colors.body}` on hover. Social icons remain monochromatic at `{colors.muted-soft}` weight — no orange-red used here, keeping the accent color architecturally reserved for CTAs and alert strips only. The footer's darkness matches `{colors.surface-card}` exactly, creating a seamless descent from page content into institutional copy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero headline drops to `display-sm` (22px); nav collapses to hamburger with full-screen `{colors.canvas}` overlay; spec grid becomes single-column stacked list; product cards fill full container width; announcement bar remains pinned |
| Tablet | 744–1128px | Two-column product grid; hero remains full-bleed; watch detail panel retains side-by-side layout but at narrower image proportion (55/45); nav shows abbreviated link set (3–4 items) with remaining items in dropdown |
| Desktop | 1128–1440px | Full nav link set visible; three-column product grid; watch detail panel splits 60/40 image/spec; hero headline at full `display-xl`; spec grid two-column |
| Wide | > 1440px | Max content width 1440px centered; hero image bleeds edge-to-edge behind constrained content container; increased whitespace at `{spacing.section}` between page sections; footer four-column grid at full span |

### Touch Targets

- All buttons maintain minimum 48px height at every breakpoint
- Nav hamburger target: minimum 44×44px tap area
- Collection filter tags expand vertical padding to `{spacing.md}` on mobile
- Product card CTA extends to full container width on mobile
- Announcement bar close/dismiss area: minimum 44px tap target height

### Collapsing Strategy

- Navigation: full horizontal link row → hamburger at < 744px; overlay opens as full-screen `{colors.canvas}` panel with vertical link stack in `{typography.nav-link}`
- Watch detail panel: 60/40 split → stacked (image above, specs below) at mobile; spec grid collapses from two-column to single-column list
- Hero: 90vh height preserved across all breakpoints; headline font steps through `display-xl` → `display-md` → `display-sm` at tablet and mobile breakpoints respectively
- Footer: four-column grid → two-column at tablet → single-column accordion at mobile, sections collapsed by default with Montserrat uppercase label as the toggle trigger

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed button border-radius values from live extraction — `{rounded.none}` is inferred from brand aesthetic and watch-brand conventions, not measured
- Exact nav height unconfirmed; 64px estimated from Shopify theme patterns common to independent watch micro-brands
- Font weight assignments for Montserrat and Barlow (700 display, 600 nav, 400 body) are consistent with the extracted font stacks but not directly site-verified from rendered CSS
- No confirmed hover/focus state animation durations or easing curves extracted
- `#007aff` extracted but identified as iOS/WebKit system blue (link or form default) — excluded from brand palette
- Swiper confirmed as a dependency via `swiper-icons` font-family detection, indicating at least one carousel component; no carousel-specific layout tokens or autoplay intervals were extractable
- Product photography art direction (lifestyle vs. studio, background color, model presence) is unknown and may significantly affect hero-banner contrast assumptions
- No confirmed header scroll behavior (transparent-to-filled vs. always-filled) — always-filled on `{colors.canvas}` is assumed
- Price display format (currency symbol placement, sale price strikethrough color) not extractable from static analysis
