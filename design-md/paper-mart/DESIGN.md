---
version: alpha
name: "Paper Mart"
source_url: "https://www.papermart.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Paper Mart runs its primary voltage at `#b71c1c` — a red-900 that sits closer to blood than traffic cone, deployed across every add-to-cart button, promotional callout, and price emphasis on a site carrying tens of thousands of SKUs. That red shares the stage with `#006064`, a Material cyan-900 that functions as a cooler structural anchor for category navigation and department headers. The two together recall industrial safety color conventions more than consumer e-commerce aesthetics, which maps precisely onto Paper Mart's actual buyer: procurement managers, event decorators, and small manufacturers sourcing corrugated mailers, tissue paper, and polymailers by the case. What most distinguishes the font stack is the presence of `barcode-39`, a genuine barcode-compatible letterform extracted from the site's live font registry — it surfaces in order confirmation and label-generation flows, making visible the reality that Paper Mart doesn't merely sell packaging but generates the print artifacts that go on packages. Montserrat carries all interactive chrome at semibold-to-bold weights, with uppercase tracking on buttons and category labels. Merriweather handles editorial content in its sturdy slab-serif cut, adding warmth that prevents the catalog from reading as purely transactional. Rounded corners are held to 4px across every interactive surface — a hard-edged, functional vocabulary with no pill shapes anywhere; pill geometry would feel incongruous against the utilitarian product photography. Accent moments use `#00acc1` and `#4dd0e1` for availability signals and featured-product ribbons, while `#bf360c`, a burnt-orange-red, marks clearance and urgency labels separately from the primary crimson, preventing promotional noise from washing out the brand anchor. A dark slate (`#3d4752`) grounds the top navigation and footer, pushing the red CTAs into sharp relief. The spacing system runs open — 64px section gaps let a high-density SKU grid breathe without the page collapsing into a wall of product tiles.

colors:
  primary: "#b71c1c"
  primary-hover: "#c62828"
  primary-active: "#9b0000"
  primary-disabled: "#ef9a9a"
  accent-teal: "#006064"
  accent-teal-mid: "#00acc1"
  accent-teal-light: "#4dd0e1"
  accent-teal-wash: "#b2ebf2"
  clearance: "#bf360c"
  clearance-mid: "#f4511e"
  clearance-light: "#ff8a65"
  promo-orange: "#ff6d00"
  ink: "#212121"
  body: "#424242"
  muted: "#616161"
  muted-soft: "#838a95"
  hairline: "#e0e0e0"
  hairline-light: "#eeeeee"
  canvas: "#fafafa"
  canvas-white: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-alt: "#f2f4f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-teal: "#ffffff"
  nav-dark: "#3d4752"
  nav-mid: "#2c6372"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.1px
  category-label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "'Merriweather', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  body-sm:
    fontFamily: "'Merriweather', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.64
    letterSpacing: 0
  body-ui:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.25px
  price-unit:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
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
    padding: 12px 24px
    height: 44px
    hoverBackgroundColor: "{colors.primary-hover}"
    activeBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"

  button-secondary:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px

  button-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-teal}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px

  text-input:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.accent-teal-mid}"
    typography: "{typography.body-ui}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px

  search-bar:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "2px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-ui}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
    submitButtonRounded: "{rounded.none}"

  nav-bar:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    topStripBackgroundColor: "{colors.primary}"
    topStripTextColor: "{colors.on-primary}"
    topStripTypography: "{typography.caption}"
    logoContainerBackgroundColor: "{colors.canvas-white}"
    borderBottom: "none"

  mega-menu:
    backgroundColor: "{colors.canvas-white}"
    headerColor: "{colors.accent-teal}"
    headerTypography: "{typography.category-label}"
    linkColor: "{colors.body}"
    linkTypography: "{typography.body-ui}"
    linkHoverColor: "{colors.primary}"
    borderTop: "3px solid {colors.primary}"
    shadow: "0 6px 16px rgba(0,0,0,0.12)"
    padding: "{spacing.lg}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "1:1"
    imageBackgroundColor: "{colors.canvas}"
    titleColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceColor: "{colors.primary}"
    priceTypography: "{typography.price-display}"
    unitColor: "{colors.muted}"
    unitTypography: "{typography.price-unit}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.1)"
    hoverBorderColor: "{colors.accent-teal-mid}"
    padding: "{spacing.sm}"

  price-tag:
    textColor: "{colors.primary}"
    typography: "{typography.price-display}"
    unitTextColor: "{colors.muted}"
    unitTypography: "{typography.price-unit}"
    strikethroughColor: "{colors.muted}"
    strikethroughTypography: "{typography.body-ui}"

  quantity-selector:
    backgroundColor: "{colors.canvas-white}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    buttonBackgroundColor: "{colors.surface-soft}"
    buttonHoverBackgroundColor: "{colors.accent-teal-wash}"
    buttonBorder: "1px solid {colors.hairline}"
    height: 40px
    width: 120px

  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  clearance-badge:
    backgroundColor: "{colors.clearance}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  new-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-teal}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  category-chip:
    backgroundColor: "{colors.accent-teal-wash}"
    textColor: "{colors.accent-teal}"
    border: "1px solid {colors.accent-teal-light}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 12px

  hero-banner:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-ui}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    overlayColor: "rgba(33,33,33,0.45)"
    minHeight: 420px
    padding: "{spacing.section} {spacing.xl}"

  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-sm}"
    ctaBorder: "1px solid {colors.on-primary}"
    ctaRounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.xl}"

  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    hoverColor: "{colors.primary}"
    padding: "{spacing.sm} 0"

  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas-white}"
    inactiveTextColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 36px
    minWidth: 36px

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-teal-light}"
    linkHoverColor: "{colors.canvas-white}"
    headingColor: "{colors.on-primary}"
    headingTypography: "{typography.category-label}"
    linkTypography: "{typography.body-ui}"
    dividerColor: "{colors.body}"
    copyrightTypography: "{typography.caption}"
    copyrightColor: "{colors.muted-soft}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The workhorse CTA rendered in `#b71c1c` with uppercase Montserrat tracking at 0.6px, 4px radius, and 44px height. On hover the shade lifts to `#c62828`; on press it deepens to `#9b0000`. Disabled state uses `#ef9a9a` — faded but still clearly red, preserving the brand signature even when inactive.

**`button-secondary`** — White fill with a 2px crimson border and matching crimson text, paired with the same uppercase Montserrat as primary. Used for secondary CTAs like "Save to Wishlist" or "Download Spec Sheet" where the primary action is already occupied by an add-to-cart.

**`button-teal`** — Fills with `#006064` for category-browse or account-action contexts where the red is reserved for transactional moments. Keeps the same uppercase button-md treatment.

**`button-ghost`** — Transparent fill with a 1px `#e0e0e0` border and `#424242` text. Used for filter toggles, sort controls, and secondary filter pills inside the product grid sidebar.

### Search

**`search-bar`** — Full-width bar with 2px hairline border that snaps to a 2px `#b71c1c` focus ring. The submit button is a flush right-attached block in `#b71c1c` with no border radius break, creating a single unified input-plus-trigger unit. Placeholder text uses `#616161` Montserrat at 14px.

### Navigation

**`nav-bar`** — Three-layer structure: a slim `#b71c1c` announcement strip at top (shipping thresholds, promo codes) in caption Montserrat, followed by a white logo zone, then the main `#3d4752` nav rail at 56px carrying category links in semibold Montserrat at 14px. The dark slate background pushes red CTAs and teal accents into sharp relief. On scroll the logo zone collapses, leaving only the dark rail sticky.

**`mega-menu`** — Drops from the nav rail on hover with a white panel and a 3px `#b71c1c` top accent border. Category group headers render in `#006064` uppercase Montserrat at 12px; individual item links use `#424242` body-ui that transitions to `#b71c1c` on hover. A soft shadow at 16px blur grounds the panel without obscuring underlying content.

### Product Grid

**`product-card`** — 1px `#e0e0e0` border, 4px radius, white fill, with a square image well on a `#fafafa` background. Title runs in semibold Montserrat at 14px in `#212121`. The price leads in 22px bold Montserrat at `#b71c1c`; the per-unit denomination sits below in 13px medium at `#616161`. On hover the border transitions to `#00acc1` and a soft shadow emerges — a teal hover signal distinguishes interactive cards from static layout.

**`price-tag`** — The price display system separates bulk price (`#b71c1c`, price-display) from the per-unit qualifier (`#616161`, price-unit) and any struck-through original price (`#616161`, body-ui with `text-decoration: line-through`). All three coexist in a tight vertical stack.

**`quantity-selector`** — A stepper with minus/plus buttons flanking a centered count input. Buttons have a `#f5f5f5` fill that transitions to `#b2ebf2` on hover — a teal wash that softly signals interactivity. The counter input itself is borderless; the containing box provides the 1px `#e0e0e0` perimeter.

### Badges & Labels

**`sale-badge`** — Tight uppercase capsule in `#b71c1c`, 4px radius, white text at 11px bold Montserrat. Overlaid at the top-left corner of product card image wells.

**`clearance-badge`** — Same capsule form in `#bf360c`, a burnt-orange-red that visually distinguishes deep clearance from standard sales promotion without introducing a fourth brand color.

**`new-badge`** — Deep teal `#006064` capsule. Used for new SKU launches, keeping the teal family associated with positive discovery signals rather than urgency.

**`category-chip`** — Soft `#b2ebf2` fill with a `#4dd0e1` border and `#006064` label text. Appears on browse landing pages as filterable taxonomy chips, carrying the teal accent palette into a softer interaction zone.

### Hero & Promotions

**`hero-banner`** — Full-width module with a `#3d4752` base, a 45% dark overlay for image compositions, and white headline type at 32px bold Montserrat. Sub-headline drops to 20px semibold. The CTA button uses `button-primary` dimensions and typography, keeping the red CTA consistent whether in context or on dark.

**`promo-banner`** — Slim `#b71c1c` strip that spans the content well for sitewide offers. White Montserrat semibold at 16px for the message; a right-aligned ghost-white button (white border, white text, transparent fill) creates a contained CTA without competing with the background.

### Footer

**`footer`** — `#212121` near-black background with `#4dd0e1` light-teal links (hover to white) and uppercase `#006064` replaced by `{colors.accent-teal-light}` for section header labels rendered in the category-label style. The teal-on-dark pairing is the only place teal reads at full saturation, since everywhere else on the site it competes with or complements the primary red.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top nav collapses to hamburger + search icon; announcement strip truncates to one offer; mega-menu becomes full-screen drawer sliding left; quantity selector stacks below add-to-cart button |
| Tablet | 744–1128px | Two-column product grid; nav retains top category links but drops secondary utility row; hero switches to 50/50 text-image split layout; mega-menu drops as overlay panel rather than full-width |
| Desktop | 1128–1440px | Three- or four-column grid depending on sidebar presence; full three-layer nav visible; mega-menu at full width with three-column internal layout; hero at full bleed with constrained content column |
| Wide | > 1440px | Content column caps at 1440px max-width with `#fafafa` canvas gutters; product grid holds at four columns; hero image area expands but text column stays constrained to ~560px |

### Touch Targets

- All buttons minimum 44px height to meet WCAG 2.5.5 target size guidance
- Quantity selector stepper buttons minimum 40×40px tap zone
- Nav hamburger icon minimum 48×48px
- Product card entire surface area is tappable on mobile, not just the title link
- Filter chip minimum 36px height with 8px horizontal padding at minimum

### Collapsing Strategy

- Top utility strip (track order, store finder) collapses first at tablet breakpoint
- Secondary nav categories move to hamburger drawer below 1128px
- Sidebar filters collapse into a bottom-sheet modal on mobile, triggered by a sticky filter button at viewport bottom
- Footer four-column layout collapses to single accordion-style column on mobile
- Breadcrumb truncates middle segments with ellipsis on mobile, retaining only root and current page

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No animation or transition timing values were extractable — duration and easing for hover states, drawer open/close, and mega-menu reveal are undocumented
- Icon system uses both `icomoon` and `Material Icons` font stacks; the exact glyph mapping and which icons belong to which set could not be determined from extraction
- `barcode-39` font usage context is inferred from font registry presence; exact rendering size, color, and placement in label/order confirmation flows was not confirmed
- Exact box-shadow values for product card hover states are estimated at standard Material elevation levels; actual extracted shadow tokens are absent
- Mobile breakpoints at 360px and 480px sub-ranges were not determinable — the tablet/mobile cutpoint at 744px is an estimate based on common practice
- Whether `#ececf6` (light lavender-white) and `#a8dab5` (light green) represent in-use palette tokens or framework artifacts is ambiguous; they are excluded from the token set pending confirmation
- Wholesale pricing tier logic (unit price at quantity breaks) component styling could not be extracted — the price-tag component documents the single-price display only
