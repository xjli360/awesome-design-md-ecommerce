---
version: alpha
name: "Anita Ko"
source_url: "https://www.anitako.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Five near-black tones cluster in the extracted palette — #111111, #121212, #1e1e1e — before a single dusty-rose spike at #b43f69 interrupts the void. That one color does concentrated work: it marks every primary CTA, editorial accent, and hover state without softening the brand's hard-edged Los Angeles sensibility. Typography runs between two deliberate poles — The Seasons, an elegant variable serif deployed at weight 300 for all display headline work, and Helvetica for navigation labels, product copy, and form fields. The pairing creates editorial gravity from the serif against Swiss-grid precision from the sans; nothing in the hierarchy is redundant. Product imagery sits against near-black grounds ({colors.surface-dark}), which makes diamonds and colored gemstones read as self-luminous rather than ornamental. Rounding is near-absent: product cards, buttons, and input fields hold sharp corners ({rounded.none}), and only material tags and pill selectors reach {rounded.full}. The result is an architectural grid that lets the jewelry provide all the organic softness. Navigation is spare — a monochromatic top bar carrying four to five Helvetica uppercase links at wide letter-spacing, a cart icon, and the Anita Ko wordmark centered or left-aligned by viewport. Layout uses generous vertical rhythm ({spacing.section} at 64px between editorial modules) so full-bleed photography can breathe. Collection pages surface product names in The Seasons thin-weight and pricing in the same serif at lighter weight still, both against the white product-card ground ({colors.canvas}). The dusty-rose primary ({colors.primary}) appears on button hover states, active link underlines, and wishlist icon fills — never as a background wash, always as a single precision accent. Footer type runs at {typography.caption} against {colors.surface-dark}, a typographic whisper beneath the visual weight of the collection above. The entire system operates as a near-two-tone composition: near-black for structure and ground, white for product revelation, rose as the brand's one voltage point.

colors:
  primary: "#b43f69"
  primary-active: "#8f2e52"
  primary-disabled: "#d4a0b5"
  ink: "#111111"
  ink-deep: "#1e1e1e"
  body: "#444444"
  muted: "#888888"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-dark: "#121212"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'The Seasons', 'Times New Roman', Georgia, serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.02em
  display-md:
    fontFamily: "'The Seasons', 'Times New Roman', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.01em
  display-sm:
    fontFamily: "'The Seasons', 'Times New Roman', Georgia, serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05em
  button-md:
    fontFamily: "Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-label:
    fontFamily: "Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  product-name:
    fontFamily: "'The Seasons', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "'The Seasons', 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.2
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    hoverBackgroundColor: "{colors.primary}"
    transition: background-color 200ms ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
    hoverBackgroundColor: "{colors.ink}"
    hoverTextColor: "{colors.on-dark}"
  button-rose:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    hoverBackgroundColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoPosition: center
    linkHoverColor: "{colors.primary}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-label}"
    height: 64px
    linkHoverColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    productNameTypography: "{typography.product-name}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.md}"
    hoverImageEffect: "secondary image crossfade"
    gap: "{spacing.sm}"
  hero-editorial:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 90vh
    contentAlignment: center
    imageFit: cover
    overlayOpacity: 0.3
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.body}"
    padding: "{spacing.section} 0"
    textAlign: center
    maxWidth: 640px
  product-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    letterSpacing: 0.1em
    textTransform: uppercase
  material-tag:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  quickadd-button:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 40px
    position: absolute
    bottom: 0
    width: "100%"
    showOn: hover
    hoverBackgroundColor: "{colors.primary}"
  wishlist-icon:
    defaultColor: "{colors.hairline}"
    activeColor: "{colors.primary}"
    size: 20px
    position: "top-right of product card image"
    padding: "{spacing.sm}"
  size-selector:
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    inactiveBorder: "1px solid {colors.hairline}"
    disabledTextColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    size: 40px
  newsletter-band:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-sm}"
    inputBackgroundColor: "transparent"
    inputBorder: "1px solid {colors.on-dark}"
    inputTypography: "{typography.body-md}"
    buttonBackgroundColor: "{colors.on-dark}"
    buttonTextColor: "{colors.ink}"
    buttonTypography: "{typography.button-md}"
    padding: "{spacing.xxl} 0"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.caption}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.title-md}"
    borderTop: "1px solid {colors.body}"
    padding: "{spacing.section} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.sm}"

## Components

### Buttons

**`button-primary`** — A full-width-capable black rectangle with Helvetica uppercase at 0.12em tracking, 48px tall, zero border-radius. On hover the fill shifts to the dusty-rose primary (#b43f69) over a 200ms ease transition — the only moment of color in the CTA layer. Disabled state uses the muted rose (#d4a0b5) and drops pointer events.

**`button-secondary`** — A 1px black outline on a transparent field; same uppercase Helvetica type as primary. On hover the colors invert: black fill, white text. Used for secondary actions on product pages (e.g. "Add to Wishlist", "More Details").

**`button-rose`** — The dusty-rose fill variant (#b43f69), white uppercase text. Reserved for editorial CTAs in dark-ground hero sections where black would disappear against the near-black background.

### Inputs

**`text-input`** — Hairline bottom border only at rest (1px #dedede), full border on focus (1px #111111). No border-radius, no shadow. Placeholder text at #888888 body-md weight. Used for search, email capture, and checkout fields.

### Navigation

**`nav-bar`** — 64px tall, white ground with 1px #dedede bottom border. Four to five Helvetica uppercase links at 0.08em tracking, spaced evenly. Wordmark centered on mobile and desktop; links collapse to hamburger below 744px. On dark editorial heroes the `nav-bar-dark` variant swaps to #121212 ground with white text. Link hover state animates to the rose primary.

### Product Card

**`product-card`** — Sharp-cornered image container in 3:4 aspect ratio. On hover a secondary product image crossfades in over the primary at 300ms. The quickadd button slides up from the bottom edge of the image on hover — black fill, uppercase Helvetica, full width. Below the image: product name in The Seasons 300 weight at 14px, then price in The Seasons 300 at 18px, with a small gap between. Wishlist icon sits top-right of the image at 20px, hairline gray at rest, switching to rose on activation.

### Hero

**`hero-editorial`** — Full-bleed dark module at minimum 90vh. Headline in The Seasons display-xl (56px, weight 300), white. Subhead in Helvetica body-md. Overlay scrim at 30% opacity over photography. Content centered both axes. Used for campaign launches and seasonal editorial.

### Collection Header

**`collection-header`** — White ground, centered layout. Headline in The Seasons display-md (36px, weight 300). One-to-two-sentence description in Helvetica body-md at #444444. Maximum width 640px to force elegant line breaks. 64px vertical padding top and bottom.

### Product Badges and Tags

**`product-badge`** — Flat soft-gray pill (#f5f5f5) at sharp corners, uppercase Helvetica caption (11px) at 0.1em tracking. Used for "New", "Limited Edition", and material callouts. `material-tag` is the outlined variant on a transparent ground with a full-radius pill shape — used for filter chips and material selectors on collection pages.

### Size / Variant Selector

**`size-selector`** — 40px square grid, no border-radius. Active state: black fill, white text. Inactive: white fill, 1px #dedede border. Disabled (sold-out): hairline text, no border emphasis. Type at Helvetica body-sm 12px.

### Newsletter Band

**`newsletter-band`** — Dark-ground (#121212) full-width strip. Headline in The Seasons display-sm (24px). Email input is borderless on three sides, 1px white bottom border only, transparent background. Submit button: white fill, black uppercase Helvetica text. 48px vertical padding on each side.

### Footer

**`footer`** — Near-black ground (#121212) with 1px #444444 top border. Column headings in Helvetica title-md uppercase tracking. Link lists in Helvetica caption (11px, 0.05em tracking) at white, hover shifts to rose primary. Social icons at 16px, white. Legal copy at caption size, #888888.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces link bar; hero headline drops to display-sm (24px); quickadd button always visible (no hover state); footer stacks columns vertically |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible if ≤ 4 items, else hamburger; hero headline at display-md (36px) |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav bar; hero at display-xl (56px); collection header max-width 640px centered |
| Wide | > 1440px | Grid stays at four columns, max-width container ~1400px centered; side gutters grow; hero image extends edge-to-edge |

### Touch Targets

- All tap targets minimum 44×44px on mobile
- Wishlist icon padded to 44×44px tappable area despite 20px visual size
- Size selector squares expand from 40px to 44px minimum on mobile
- Hamburger menu icon 44×44px tappable zone

### Collapsing Strategy

- Navigation: links collapse to hamburger at < 744px; cart and search icons always persist in top bar
- Product grid: 4 col → 3 col (1128px) → 2 col (744px) → 1 col (< 744px)
- Hero subhead text hides on mobile to reduce vertical scroll commitment
- Newsletter band: two-column layout (headline | form) collapses to single column stacked on mobile
- Footer: four-column link grid collapses to two columns at tablet, single column at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact primary-active (#8f2e52) and primary-disabled (#d4a0b5) values are derived by shifting the extracted rose; not confirmed from source
- Muted text color (#888888) not extracted; inferred from common Shopify theme patterns for mid-gray utility text
- Surface-soft (#f5f5f5) not in extracted palette; inferred for badge/chip backgrounds
- Canvas white (#ffffff) not explicitly in extracted hex list; inferred as standard Shopify product-page background
- Font weights for The Seasons beyond 300 (light) not confirmed — brand may use only the thin and light cuts
- Exact letter-spacing values for nav labels and buttons not extractable from current hints; values based on luxury jewelry conventions
- No animation timing or easing curves extracted; transition durations are estimated
- Mega-menu or dropdown nav structure not confirmed; unclear if collections use flyout or dedicated landing pages
- Mobile nav icon set (hamburger, cart, search) not extractable from color/font hints alone
