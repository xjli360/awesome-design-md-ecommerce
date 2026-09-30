---
version: alpha
name: "Blackwing"
source_url: "https://blackwing602.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every Blackwing pencil ships with a replaceable flat eraser — a mechanical holdover that most pencilmakers abandoned decades ago — and the digital system inherits the same logic: one purposeful element per surface, nothing ornamental. The site grounds itself in near-black (#232323) rather than the clinical white that most Shopify storefronts default to, placing product photography against a dark field where lacquer color and finish can be read accurately against the ground. The primary voltage is a warm coral-red (#e9514b), warm enough to read as wax or lacquer rather than urgency; it appears on add-to-cart buttons and edition markers throughout the shop. A secondary orange (#ff8b21) handles sale pricing and promotional callouts while a slate blue (#338fb1) owns informational link states — three accent channels that share the palette without competing because each holds a distinct semantic lane. Open Sans carries the full typographic system at moderate weights; no custom display cut was found in extraction, meaning hierarchy is built from size and scale alone rather than typeface contrast. Monospaced labels surface on SKU codes and edition series numbers, borrowing ledger-floor precision to serve a collector community that catalogues pencil grades the way audiophiles track pressings. Rounded values stay minimal: {rounded.xs} at 4px for inputs and badges, {rounded.sm} at 8px for product cards — no pill shapes appear anywhere, echoing the hexagonal cross-section of the pencil barrel. Light surface grays cluster in a narrow band — #f8f8f8, #fafafa, #f6f6f6 — separating layers without ever reaching true brightness. Spacing is generous at hero scale and tight at component level, keeping individual elements legible without adding visual weight to the page. The system reads like archival print applied to a Shopify storefront: high figure-ground contrast, restrained color, and authority earned through specificity rather than volume.

colors:
  primary: "#e9514b"
  primary-active: "#d93333"
  primary-disabled: "#fceeee"
  primary-error-text: "#d93333"
  accent-orange: "#ff8b21"
  accent-blue: "#338fb1"
  accent-gold: "#e0b252"
  ink: "#191919"
  body: "#3c3c3c"
  muted: "#969696"
  muted-soft: "#cbcbcb"
  hairline: "#e6e6e6"
  hairline-soft: "#e9e9e9"
  border-strong: "#868686"
  canvas: "#fafafa"
  surface-soft: "#f8f8f8"
  surface-card: "#f6f6f6"
  surface-mid: "#dedede"
  canvas-dark: "#232323"
  surface-dark: "#323232"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success-surface: "#dff0d8"
  warning-surface: "#fff2dd"
  error-surface: "#fceeee"
  scrim: "#191919"

typography:
  display-xl:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'Open Sans', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  mono-label:
    fontFamily: "monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  edition-code:
    fontFamily: "monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1px
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
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 48px
    border: "1px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspectRatio: "1:1"
  hero:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  edition-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.edition-code}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sale-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-dark}"
    typography: "{typography.edition-code}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  pencil-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "2px solid transparent"
    gap: "{spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 40px
    padding: 8px 14px
    borderColorFocus: "{colors.ink}"
  price-display:
    typography: "{typography.price}"
    regularColor: "{colors.ink}"
    saleColor: "{colors.primary-active}"
    compareAtColor: "{colors.muted}"
    compareAtDecoration: line-through
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-mid}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    paddingVertical: "{spacing.xxl}"
    borderTop: "1px solid {colors.surface-dark}"
  mono-tag:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.mono-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 2px 6px

## Components

### Buttons

**`button-primary`** — The primary CTA uses coral-red (#e9514b) fill with white text and a 4px radius, keeping corners nearly square in keeping with the system's zero-pill discipline. Active state deepens to #d93333; disabled state washes the fill to #fceeee with muted gray text to signal unavailability without removing the shape. The label runs in Open Sans 600 at 14px with uppercase transform and 0.5px letter-spacing, adding a slight editorial formality to what is otherwise a minimal shape. Used for add-to-cart, checkout, and primary collection CTAs.

**`button-secondary`** — A 1px #191919 border on a #fafafa ground at the same 48px height as button-primary, ensuring consistent vertical rhythm in button pairs. Typography and letter-spacing match button-primary so the two shapes read as a system rather than two unrelated elements. Used for secondary actions like "Learn More", "View All", and wishlist operations.

**`button-ghost-dark`** — The outline treatment inverted for dark hero and footer contexts: transparent background, white 1px border, white text. Allows dark-ground sections to carry CTAs without introducing a colored surface that would compete with product photography. Pairs with button-primary in hero layouts where a primary and secondary CTA sit side by side.

### Text Input

**`text-input`** — A 44px tall field in Open Sans 16px with 4px radius and a resting border in #e6e6e6. Focus shifts the border to #191919 — a high-contrast signal that avoids using the brand's red for non-error states, preserving color meaning. Placeholder text renders in #969696. Used across search, newsletter signup, and checkout form fields.

### Navigation

**`nav-bar`** — 64px tall on a #fafafa ground with a 1px #e6e6e6 bottom border. Navigation links render in Open Sans 600 at 14px. Logo anchors to the left; cart icon and search trigger sit to the right. The bar stays light-ground even when the page beneath it is dark, acting as a consistent orientation landmark.

**`announcement-bar`** — A 36px strip in #232323 pinned above the nav, rendering caption text in white, center-aligned. Used for free-shipping thresholds, limited-edition launch countdowns, and promotional codes. Maintains the brand's dark surface vocabulary at the very top of the page before any product imagery appears.

### Product Card

**`product-card`** — A 1:1 image fills the card top against a #f6f6f6 surface; title and price stack below with 16px padding. Title in Open Sans 600/16px, price in 700/20px with 8px card radius. Edition and sale badges overlay the top-left corner of the image at a 3px offset, keeping the product silhouette unobstructed. Hover behavior should lift the card with a subtle shadow rather than color change.

### Hero

**`hero`** — Near-black #232323 canvas, minimum 560px tall, with a display-xl headline in white and a supporting body paragraph. CTAs run as button-ghost-dark and button-primary side by side. Used for new collection launches, artist collaborations, and seasonal campaigns where photography needs to read against a controlled dark ground rather than a bright page.

### Badges

**`edition-badge`** — Coral-red (#e9514b) label with 11px monospaced uppercase text and 1px letter-spacing; placed at the image corner of limited-run product cards. **`sale-badge`** — Identical structure in orange (#ff8b21) for promotional pricing contexts. Both use {rounded.xs} rather than any pill form, consistent with the system's corner restraint.

### Pencil Swatch

**`pencil-swatch`** — 24px circular swatches for pencil colorway and edition selectors, separated by 8px gaps. Active selection receives a 2px #191919 border; inactive swatches have a transparent border to maintain consistent sizing between states without a layout shift on selection. On mobile the swatch size scales to 36px for touch accuracy.

### Utility

**`search-bar`** — A 40px #f8f8f8 input with 4px radius and no visible border at rest; border appears in #191919 on focus. Placeholder in #969696, body-sm typography. Typically sits in a modal overlay triggered from the nav icon rather than inline in the header.

**`price-display`** — Regular price in #191919 at 20px/700; sale price in #d93333; compare-at price struck through in #969696. The three states can appear simultaneously on sale product cards, with sale price left of compare-at and separated by a space.

**`footer`** — Full-width #232323 footer with 48px vertical padding and a 1px #323232 top border to separate it from light-ground content above. Link columns use #dedede for legibility against the dark ground; section headings in Open Sans 600/16px, link items in 400/14px.

**`mono-tag`** — A hairline-bordered inline tag in the monospace stack — 12px, 0.5px letter-spacing — used on product detail pages for series codes, grade designations (602, Matte, Volume), and material callouts. Renders in #969696 against light surfaces.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero min-height drops to 360px; button-primary goes full-width; pencil swatches scale to 36px |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only with dropdowns on tap; hero shifts to stacked text-above-image |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav visible; hero uses two-column text-left image-right layout |
| Wide | > 1440px | Container caps at 1440px centered; horizontal padding increases to 80px; hero image bleeds to full viewport width behind contained text column |

### Touch Targets

- All buttons minimum 44px height on mobile
- Pencil swatch selectors expand from 24px to 36px on mobile
- Nav links use a minimum 44×44px hit area even when visible text is smaller
- Add-to-cart button goes full-width on mobile for maximum thumb reach
- Search and cart icons in the nav bar use a 44×44px tap zone with no visible change to icon size

### Collapsing Strategy

- Product grid collapses 4-col → 3-col → 2-col → 1-col across Wide → Desktop → Tablet → Mobile
- Hero layout: two-column side-by-side → stacked (text above image) at Tablet and below
- Footer columns: four-column link grid → two-column → single stacked list on Mobile
- Announcement bar remains visible at all breakpoints; wraps to two lines rather than truncating
- Monospace tags on product detail pages wrap to new lines rather than truncating edition codes

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom display or heading typeface confirmed — only Open Sans and monospace were found in font-stack extraction; the live site may load a licensed display face via JS that was not captured
- Exact nav layout (megamenu vs. simple dropdown, icon treatment) not confirmed from extraction
- Animation and transition timing values (hover lift, badge entrance, swatch selection) not available
- Icon library style (stroke weight, filled vs. outline) not confirmed
- Product grid column counts and card gap values not confirmed from extraction; values above are inferred from Shopify defaults
- Dark-mode or seasonal palette variants not confirmed
- Whether #e9514b or #e95144 is the canonical primary red (both appear in extraction; #e9514b used as primary due to ordering)
