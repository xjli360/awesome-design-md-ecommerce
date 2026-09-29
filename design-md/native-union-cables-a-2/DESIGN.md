---
version: alpha
name: "Native Union"
source_url: "https://www.nativeunion.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Burnt-orange signal-fire (#ef521b) set against a near-total-black field (#111111) — that single voltage marks every primary CTA, hero accent, and promotional callout, making a cable brand read as a design-object brand on first scroll. The tension between that orange and a warm camel-gold (#cb8a3d) does the work that lifestyle photography usually handles alone: communicating braided-fabric and brass-hardware material warmth without a single prop required. Neue Haas Grotesk anchors the display layer, a Swiss grotesque precise enough to evoke machined connectors and flush-fit plugs; the museo-sans family handles body and UI text, its humanist curves supplying enough softness to prevent the grid from reading clinical. Letter-spaced uppercase labels ({typography.label-caps}) and minimal-radius containers press the analogy of a stamped mark on precision hardware — the type is as flush and deliberate as the products themselves. Canvas is white (#ffffff), body text near-black (#111111), and the only relief from that binary contrast comes through mid-gray (#9a9a9a) for secondary text, a light hairline (#dedede) for borders and dividers, and a derived surface-soft for card backgrounds. Product cards surrender the full card top to imagery with zero decorative chrome — no drop shadows, no rounded overlays — because the object is the design. The orange primary appears at maximum contrast against white or black, never as a decorative wash: always a directive, always buy / add / select. Button type is set compact with uppercase tracking ({typography.button-md}), pressing the same stamped-label logic. Footer sections deepen to near-black (#121212), reversing text to white and letting the camel accent thread through material certifications and sustainability callouts. Navigation is white-barred and spare, the brand wordmark in Neue Haas at tight tracking, with orange reserved only for the announcement banner and cart-count badge. Spacing is generous by cable-brand standards — {spacing.xxl} and {spacing.section} gutters signal that these objects are worth a pause, not a scroll-past.

colors:
  primary: "#ef521b"
  primary-active: "#c93e0f"
  primary-disabled: "#f7a889"
  accent-camel: "#cb8a3d"
  ink: "#111111"
  muted: "#9a9a9a"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Neue Haas Grotesk Display', 'NeueHaasGrotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -0.02em
  display-lg:
    fontFamily: "'Neue Haas Grotesk Display', 'NeueHaasGrotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.02em
  display-md:
    fontFamily: "'Neue Haas Grotesk Display', 'NeueHaasGrotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.01em
  title-lg:
    fontFamily: "'Neue Haas Grotesk Display', 'NeueHaasGrotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'museo-sans', 'Museo Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'museo-sans', 'Museo Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'museo-sans', 'Museo Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'museo-sans', 'Museo Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "'museo-sans-condensed', 'Museo Sans Condensed', 'museo-sans', system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  overline:
    fontFamily: "'museo-sans-condensed', 'Museo Sans Condensed', 'museo-sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  button-md:
    fontFamily: "'museo-sans', 'Museo Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'museo-sans', 'Museo Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'museo-sans', 'Museo Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Neue Haas Grotesk Display', 'NeueHaasGrotesk', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 400
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
    padding: "14px 32px"
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "13px 31px"
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    focusBorderColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: "12px 16px"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.title-lg}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    height: 40px
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspect: "1 / 1"
    padding: "{spacing.md}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    secondaryTextColor: "{colors.muted}"
    captionTypography: "{typography.caption}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    minHeight: 640px
    padding: "{spacing.section} {spacing.xl}"
  material-badge:
    backgroundColor: "{colors.accent-camel}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  color-swatch:
    size: 20px
    borderRadius: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  cart-count-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    size: 18px
  section-label:
    textColor: "{colors.muted}"
    typography: "{typography.overline}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.accent-camel}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} {spacing.xl}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons

**`button-primary`** — A compact rectangular CTA in burnt-orange (#ef521b) with near-zero radius ({rounded.xs}) and uppercase tracking type ({typography.button-md}). The shape never changes between states — only the fill shifts: hover/press moves to the darker orange ({colors.primary-active}), disabled fades to a washed peach ({colors.primary-disabled}) without reducing opacity, keeping the element in the layout without appearing interactive. This is the highest-energy component on the page; use it at most once per viewport unit.

**`button-secondary`** — White fill with a 1px ink border, matching uppercase tracking. At rest it reads as a quiet counterpart to the orange CTA; on hover, the border shifts to {colors.primary} to acknowledge proximity to the action without displacing it. Used for secondary choices: "Compare", "View Details", variant selectors.

**`button-ghost`** — Transparent background, ink-colored underlined text. Reserved for lowest-priority actions — cancel flows, inline "learn more" links, collapse toggles — where a bordered box would add visual weight the context cannot support.

**`button-dark`** — Ink-black fill with white text ({colors.on-dark}), used when the primary orange would compete with an adjacent orange element or announcement bar. Appears most often in full-bleed dark hero sections where the orange CTA would disappear into the background.

### Text Input

**`text-input`** — White background, 1px hairline border, 48px tall. Focus state swaps the border to full ink (#111111) — no glow, no shadow, no color flash, just the border weight signaling attention. Placeholder text in mid-gray ({colors.muted}). The form field reads as a precision slot: exact fit, no decorative surplus.

### Navigation

**`nav-bar`** — White bar, 64px tall, with a hairline bottom border that separates it from the page content without adding a second visual band. Brand wordmark sits left in Neue Haas Grotesk ({typography.title-lg}) at tight tracking; category links center in museo-sans ({typography.nav-link}) with no underline at rest — hover reveals a thin orange underline accent. Cart icon right with an orange circle badge ({cart-count-badge}) for item count. Dropdown menus use a flat white panel with hairline border; no dark overlay, no blur, no mega-menu animation.

**`announcement-bar`** — A full-width orange strip above the nav, 40px tall, label-caps text in white, centered. This is almost always the first brand-voltage moment on the page — the orange (#ef521b) reads before the logo does. Used for promotions, shipping thresholds, or new-collection countdowns. Copy is kept to a single short phrase.

### Product Card

**`product-card`** — Zero border-radius, white background, product image at full card width in a 1:1 aspect ratio. Below the image: product name in {typography.body-md}, a variant descriptor (color name, cable length) in {typography.caption} and {colors.muted}, then price in {typography.price-display}. Color swatches sit inline below the product name as 20px circles ({rounded.full}), with the selected swatch ringed by a 2px ink border. Material and launch badges (flat, zero-radius tags) overlay the top-left corner of the image: camel-gold for material type, ink for evergreen labels, orange for new arrivals. No "Add to Cart" button appears at card level — that action moves to the product detail page.

### Hero Banner

**`hero-banner`** — Full-bleed image or near-black (#111111) background with a display-xl headline in white — up to four words per line for maximum visual impact. A single orange CTA sits below the headline with 24–48px clearance; no subheadline competes with it. On product-hero layouts the background may shift to white with the product photograph occupying the right half. Minimum height 640px on desktop, 400px on mobile. No parallax or animated text reveal — the photograph and the type carry the entire weight of the moment.

### Badges

**`material-badge`** — A flat, zero-radius tag in camel-gold (#cb8a3d) with white label-caps text. Used for material callouts: BRAIDED, LEATHER, NYLON. The camel tone signals premium material provenance; it is the only non-orange color that carries a positive brand charge.

**`product-badge`** — Ink-black flat tag with white label-caps text. Used for evergreen commercial labels: BESTSELLER, BUNDLE DEAL, AWARD WINNER.

**`product-badge-new`** — Identical shape in orange (#ef521b) with white text. Reserved for time-sensitive launch signals: NEW, JUST DROPPED, LIMITED EDITION. The color is a deliberate voltage match to the CTA — it tells the shopper this item has the same urgency as a buy button.

### Color Swatch

**`color-swatch`** — 20px circles arranged horizontally with {spacing.xs} gaps. Unselected swatches have no visible border; the selected swatch gains a 2px ink ring with a 2px transparent gap between the swatch and the ring (creating a halo effect). Hover on an unselected swatch previews the ring at 50% opacity. The small size keeps multi-color SKU rows compact without hiding the palette.

### Section Label / Overline

**`section-label`** — Uppercase overline ({typography.overline}) in {colors.muted} used above section headlines to organize the page into named zones: FEATURED, SHOP BY MATERIAL, BEST SELLERS. Sits {spacing.lg} above its associated heading. Never appears in orange or ink — the muted gray preserves hierarchy without competing with headlines.

### Footer

**`footer`** — Near-black background ({colors.surface-dark}), white body-sm text, section headings in {typography.label-caps}. The camel accent (#cb8a3d) threads through link hover states and any certification or material-standard icons. Four-column layout on desktop with a fine hairline divider separating the link grid from the legal row. No top border — the dark background creates its own separation from the white page body above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + slide-in drawer; hero headline drops to display-md; announcement bar shrinks to 32px with abbreviated copy; footer collapses to accordion, one section open at a time |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only, no hover sub-links; hero crops to portrait or shifts to text-only with product inset |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with hover sub-link panels; hero uses full-bleed landscape image; announcement bar full copy |
| Wide | > 1440px | Grid max-width capped at 1440px, centered with auto margins; section padding increases from {spacing.section} to 80px; hero headline may scale to display-xl |

### Touch Targets
- All buttons minimum 48px tall, minimum 44px wide
- Color swatches expand tap area to 36×36px via invisible padding even when visual swatch is 20px
- Nav hamburger minimum 44×44px touch area
- Cart icon and all nav icons minimum 44×44px
- Announcement bar links minimum 40px tall (full bar height serves as tap target)

### Collapsing Strategy
- Navigation: full horizontal nav at ≥ 1128px collapses to hamburger → side drawer at < 744px; mid-range (744–1128px) shows top-level items only, no sub-links
- Product grid: 4-column → 3-column → 2-column → 1-column as viewport narrows through the breakpoints
- Hero: landscape split-image layout collapses to stacked (image above, text below) at < 744px; headline type scale steps down from display-xl to display-md
- Footer: four-column link grid collapses to single-column accordion on mobile; legal row stacks vertically

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `surface-soft` (#f7f7f7) is derived — not directly extracted from the live site; actual card-background tint may differ
- `primary-active` (#c93e0f) and `primary-disabled` (#f7a889) are computed by darkening/lightening the extracted #ef521b — no verified hover or disabled states were captured
- Exact button border-radius is unconfirmed; {rounded.xs} (4px) is an inference from the brand's minimal visual register
- Font weights per display scale not captured — Neue Haas offers 300/400/500/700 and the per-step weight assignment is an estimate
- Specific use contexts for museo-sans-rounded and museo-sans-display sub-variants not identified; both are in the font stack but no distinct UI role was confirmed
- Transition durations, easing curves, and hover animation timing not extracted
- Drop shadow values and any elevation system not observed
- Dark mode not observed; site appears to be light-mode only with one dark-surface zone (footer)
- Exact nav height (64px) is a visual estimate; no computed value was captured
