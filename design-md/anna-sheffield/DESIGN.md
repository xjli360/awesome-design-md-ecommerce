---
version: alpha
name: "Anna Sheffield"
source_url: "https://www.annasheffield.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The near-black #1d1a1e governing Anna Sheffield's interface carries a barely-perceptible violet cast — just enough to separate it from a generic black and signal that this is not the conventional white-marble bridal jeweler. Where most fine-jewelry sites reach for cream and champagne, Sheffield grounds everything in near-darkness, letting oxidized-metal product photography and raw-stone imagery glow against the void rather than compete with a pale backdrop. The effect is closer to a private gallery lit for evening viewing than to a daytime boutique. Type pairs Maison Neue — a crisp grotesque that handles every functional UI layer — with Portrait, a high-contrast serif whose ink-trap details reward the close reading a significant ring purchase deserves. Styrene A and Pegasus extend the vocabulary further, giving the system range from catalog-utilitarian to editorial-theatrical within a single scroll. Letter-spacing on display lines opens slightly, lending captions and price labels the deliberate pace the brand's customer expects. The chromatic palette is deliberately narrow: two extracted anchors — #1d1a1e and the mid-gray #6f6f77 — cover most of the interface, with canvas whites used only to lift product imagery. Anna Sheffield appears to derive all chromatic warmth from the gold, rose, and stone tones in photography rather than a persistent UI accent hue. Geometry is architectural: `{rounded.none}` dominates buttons and inputs, with only the lightest `{rounded.xs}` reserved for badges. Spacing breathes at `{spacing.section}` or wider between content zones, and product-card grids carry generous gutters — each piece of jewelry occupies its own considered rectangle of silence. Navigation is unhurried sparse text links in Maison Neue at modest size, no mega-menus, no category tiles, because the store trusts that a visitor who has found Anna Sheffield already knows what she is looking for.

colors:
  primary: "#1d1a1e"
  primary-active: "#0d0b0f"
  primary-disabled: "#9e9ea4"
  ink: "#1d1a1e"
  body: "#3a3a3f"
  muted: "#6f6f77"
  hairline: "#d4d4d8"
  hairline-soft: "#eaeaec"
  canvas: "#ffffff"
  surface-soft: "#f5f4f6"
  surface-card: "#ffffff"
  surface-dark: "#1d1a1e"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  overlay-scrim: "#1d1a1e"

typography:
  display-xl:
    fontFamily: "'Portrait', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Portrait', Georgia, serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Portrait', Georgia, serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Portrait', Georgia, serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Maison Neue', 'Maison Neue Bold', Helvetica Neue, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Maison Neue', Helvetica Neue, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'Maison Neue', Helvetica Neue, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Neue', Helvetica Neue, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue', Helvetica Neue, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  label-caps:
    fontFamily: "'Maison Neue', Helvetica Neue, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Maison Neue', Helvetica Neue, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Maison Neue', Helvetica Neue, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Maison Neue', Helvetica Neue, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.06em
  price-display:
    fontFamily: "'Maison Neue', Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  mono-detail:
    fontFamily: "'Maison Neue Mono', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.04em

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
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.on-dark}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 40px 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoSize: 120px
    gap: "{spacing.xl}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/5"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    metaColor: "{colors.muted}"
    metaTypography: "{typography.caption}"
    hoverEffect: image-zoom 1.03
  product-grid:
    columns: "2 (mobile) / 3 (tablet) / 4 (desktop)"
    gap: "{spacing.lg}"
    paddingX: "{spacing.xl}"
  hero-full:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    layout: full-bleed image-behind text
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    overlayColor: "{colors.overlay-scrim}"
    overlayOpacity: 0.35
    ctaVariant: button-ghost
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    layout: split 50/50 image-left text-right
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    textAlign: center
  badge-label:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
    border: "1px solid {colors.ink}"
  material-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    borderBottom: "1px solid {colors.hairline}"
    gap: "{spacing.xl}"
    height: 48px
  swatch-ring:
    size: 20px
    borderRadius: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "2px solid transparent"
    gap: "{spacing.xs}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    size: 40px
  product-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.title-md}"
    descriptionTypography: "{typography.body-md}"
    specTypography: "{typography.mono-detail}"
    paddingX: "{spacing.xxl}"
    gap: "{spacing.lg}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: none
    height: 48px
    padding: "0 {spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.nav-link}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: none
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    height: 36px
    textAlign: center

## Components

### Buttons

**`button-primary`** — Flat black rectangle at 48px tall with no border radius, uppercase Maison Neue at 12px / 0.1em tracking. The square geometry reads architectural rather than approachable, which is appropriate for a brand whose customer is selecting a ring she will wear for decades. Active state deepens to #0d0b0f; disabled state substitutes the mid-gray `{colors.primary-disabled}`. Add a 150ms background-color transition on hover.

**`button-secondary`** — Same dimensions as primary, reversed: white fill with a 1px `{colors.ink}` border. Used on light-canvas sections where a solid black block would overwhelm the composition. Hover state fills the button with `{colors.surface-soft}`.

**`button-ghost`** — Transparent background with a 1px `{colors.on-dark}` border, deployed exclusively on dark hero or editorial overlays. White label remains legible against the `{colors.overlay-scrim}` hero treatment. Add an opacity-0.8 hover state.

**`button-text-link`** — No background, no border; underlined `{typography.body-sm}` in `{colors.ink}`. Used for secondary actions like "Learn more" or "View size guide" where a full button would over-emphasize a minor action.

### Navigation

**`nav-bar`** — 64px tall, white canvas, with a barely-there 1px `{colors.hairline-soft}` bottom border that only becomes visible on scroll. Logo sits left at ~120px wide; nav links (Maison Neue 12px, 0.06em tracking) space centrally or right with `{spacing.xl}` gaps. A dark variant (`nav-bar-dark`) is used on the homepage hero where the bar overlays photography — background becomes `{colors.surface-dark}` and links shift to `{colors.on-dark}`.

**`announcement-bar`** — 36px strip above the nav, solid `{colors.primary}` (#1d1a1e), centered uppercase Maison Neue in white. Used for shipping thresholds or campaign notes. Thin enough to read as a ribbon rather than a billboard.

### Product Card

**`product-card`** — Edge-to-edge image at a 4:5 portrait ratio with zero corner radius. Title renders in `{typography.body-sm}` at `{colors.ink}`; price follows in `{typography.price-display}` at `{colors.body}`. A material or stone note in `{typography.caption}` at `{colors.muted}` occupies a third line for PDP-enriched grids. On hover the image scales to 1.03× over 300ms with overflow hidden — no overlay, no icon intrusion — because the product itself is the signal. The grid runs 2 columns on mobile, 3 on tablet, 4 on desktop with `{spacing.lg}` gutters.

### Product Detail Panel

**`product-detail-panel`** — Right column on desktop PDPs. Title uses `{typography.display-sm}` (Portrait 22px light), price follows in `{typography.title-md}`. Ring-size selector (`size-selector`) is a row of 40px squares with 1px borders; selected state thickens the border to match `{colors.ink}` — no fill change. Stone/metal spec lines use `{typography.mono-detail}` (Maison Neue Mono) to communicate precision. The "Add to Cart" CTA is a full-width `button-primary` at the base of the form stack.

### Badges & Labels

**`badge-label`** — Zero-radius pill in `{colors.primary}` (#1d1a1e), white uppercase Maison Neue at 10px / 0.12em. Used sparingly: "New," "Limited," "Bespoke." Because the background matches the near-black that anchors the entire palette, overuse would blend these into the surrounding dark regions. Use at most one badge per product card.

**`badge-outline`** — Same geometry and type scale as `badge-label` but with transparent fill and a 1px `{colors.ink}` border. Used for secondary tags ("In Stock," stone type) where the filled variant would create too much visual weight.

**`material-tag`** — Soft `{colors.surface-soft}` background with `{rounded.xs}`, `{typography.caption}` in `{colors.body}`. The softest label in the system; used inside product detail for gold karat, stone origin, or finish descriptors.

### Editorial Hero

**`hero-full`** — Full-bleed photograph with the brand's near-dark scrim (`{colors.overlay-scrim}` at 35% opacity) over the image, placing `{typography.display-xl}` Portrait headline and a `button-ghost` CTA on top. The extreme letterweight (300) against the dark overlay creates the gallery-at-night effect central to the brand's mood. Text block aligns bottom-left or centered depending on composition.

**`hero-editorial`** — Split 50/50 layout: image left, text right on white canvas. Title in `{typography.display-lg}` Portrait light, body copy in `{typography.body-md}` Maison Neue, CTA in `button-secondary`. Used for collection stories, designer notes, or bridal editorial. No border radius anywhere.

**`collection-banner`** — Centered text block on `{colors.surface-soft}` at `{spacing.xxl}` vertical padding, used as a section header between product grids. Title in `{typography.display-md}` Portrait; subtitle in `{typography.body-sm}` Maison Neue. A thin `1px {colors.hairline}` separator above and below optionally frames the block.

### Filter & Search

**`filter-bar`** — A horizontal strip of uppercase `{typography.label-caps}` filter labels pinned below the nav on collection pages. Active filter gets an underline in `{colors.ink}`; inactive sits in `{colors.muted}`. The bar is borderless top and carries only the `1px {colors.hairline}` bottom edge, maintaining the lean horizontal rhythm of the nav.

**`search-bar`** — No border, `{colors.surface-soft}` fill, flat rectangle. Placeholder in `{colors.muted}` Maison Neue. Expands from the nav icon on click; does not slide in from an overlay — it replaces the nav bar's central zone inline, keeping the page still.

### Accordion

**`accordion`** — Used for care instructions, size guides, and shipping details on PDPs. Label in `{typography.title-sm}` with a 1px `{colors.hairline}` top border and no background change. Expand icon is a minimal plus/minus glyph in `{colors.muted}`. Content body uses `{typography.body-sm}` with `{spacing.base}` bottom padding.

### Footer

**`footer`** — Full `{colors.primary}` (#1d1a1e) background, white text throughout. Column headings in `{typography.label-caps}`; links in `{typography.nav-link}` Maison Neue at `{colors.on-dark}`. No background break between footer and the last content section — the near-black simply begins. Social icon links are inline SVGs, no filled backgrounds. Newsletter input reverses to a 1px white-border flat rectangle on dark.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero text reduces to `{typography.display-md}`; hero switches from split to stacked layout; filter-bar becomes a horizontal scroll strip; product detail panel stacks below image |
| Tablet | 744–1128px | 2-column product grid shifts to 3 columns; hero-editorial uses 45/55 split; nav shows top-level links only, categories in a drop-down; announcement-bar remains full-width |
| Desktop | 1128–1440px | 4-column product grid; full nav-bar with all links visible; hero-full uses wide aspect (16:7); product detail panel floats right in a 55/45 image/detail split |
| Wide | > 1440px | Max content width clamps at 1440px with auto horizontal margins; hero imagery scales to fill; spacing between sections increases to 1.5× `{spacing.section}` |

### Touch Targets

- All tappable buttons minimum 48px height
- Nav hamburger and icon buttons minimum 44×44px hit area
- Swatch rings padded to a 32px tap target despite 20px visual size
- Size-selector squares minimum 40×40px; enlarge to 48×48px on mobile
- Filter-bar tabs minimum 44px tall on mobile

### Collapsing Strategy

- Primary nav links collapse to hamburger at < 1024px; drawer slides in from left over `{colors.primary}` background with white links
- Filter-bar on mobile becomes a horizontal scroll strip; a "Filter" button opens a bottom sheet with all options
- Hero-editorial stacks image above text at < 744px; image takes 100vw at 50vw aspect height
- Product detail accordion items default to collapsed on mobile to reduce scroll depth
- Footer columns collapse to a single stacked list with accordion-style expand per column group

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two hex values (#1d1a1e and #6f6f77) were extractable from the live site; all surface, canvas, hairline, and error-state colors are derived by interpolation and brand-category inference rather than direct extraction
- No dedicated accent or gold-tone color was present in the extraction — Anna Sheffield's warmth appears to come entirely from photography, not a persistent UI token; a gold or rose-metal hex should be confirmed from the live site and added as `colors.accent-gold`
- Pegasus appears in the font stack but its role (likely a custom or licensed script/display face) and its intended use cases could not be confirmed from extraction alone
- Styrene A's exact deployment (editorial headers vs. UI labels) is inferred; direct inspection of heading elements would confirm
- Button hover and focus states (outline color for keyboard accessibility, exact transition curves) were not extractable and are specified here at reasonable design-system defaults
- No error or form-validation colors were extracted; `colors.primary-error` tokens should be audited from the checkout flow
- Dark/light nav switching logic (when the site uses `nav-bar-dark` vs. `nav-bar`) was not confirmed — behavior described here is inferred from typical fine-jewelry Shopify patterns
