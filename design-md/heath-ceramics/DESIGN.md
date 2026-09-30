---
version: alpha
name: "Heath Ceramics"
source_url: "https://www.heathceramics.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Heath Ceramics is a slow-made, earth-honoring dinnerware and home goods brand rooted in Sausalito, California since 1948. The brand’s palette draws from the raw materials of clay and glaze — a warm, sandy canvas of `#d1ccc6` sets the stage, while deeper earthen tones like `#453b33` (a rich, dark brown) and `#26211a` (near-black espresso) ground the typography and structural elements. Accents of muted terracotta (`#dc6650`), a soft, aged gold (`#debd5c`), and a dusty slate blue (`#6e91bd`) appear sparingly, like glazed highlights on a ceramic piece. The overall mood is tactile, honest, and unpretentious — there is no glossy finish or aggressive contrast. Instead, the system relies on subtle shifts between `{colors.canvas}` and `{colors.surface-soft}`, with `{colors.hairline}` borders that feel like the seam between two fired pieces. Typography, though not explicitly declared in CSS, reads as a clean, warm sans-serif — likely a system stack — set at modest weights and generous line heights to echo the handcrafted, readable quality of the brand’s printed catalogs. The signature design move is the interplay of soft, organic curves (seen in `{rounded.lg}` on cards and `{rounded.full}` on buttons) against the rigid geometry of grid-based product layouts, mirroring the tension between thrown clay and the kiln’s precision.

colors:
  primary: "#453b33"
  primary-active: "#26211a"
  primary-disabled: "#d1ccc6"
  ink: "#26211a"
  body: "#453b33"
  muted: "#6e91bd"
  muted-soft: "#d1ccc6"
  hairline: "#dedede"
  hairline-soft: "#d1ccc6"
  canvas: "#d1ccc6"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-terracotta: "#dc6650"
  accent-gold: "#debd5c"
  accent-slate: "#6e91bd"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  dark-bg: "#121212"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.1px
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-pill:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(38,33,26,0.1)"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
  footer-section:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary action button uses the brand’s deep earthen brown (`{colors.primary}`) on a white label, with sharp, unrounded corners that nod to the clean edges of ceramic forms. On hover, it deepens to `{colors.primary-active}`; when disabled, it fades to the sandy `{colors.primary-disabled}` with muted text. The uppercase label, set in `{typography.button-md}`, carries a subtle letter-spacing that evokes a stamped maker’s mark.

**`button-secondary`** — A canvas-toned button with the same sharp geometry and uppercase typography, outlined by the primary brown text color. It sits quietly alongside the primary button, used for “Learn More” or “View Collection” links. Its hover state inverts to a filled primary background.

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like “Add to Cart” or “Details.” The label remains in `{colors.primary}` and inherits the uppercase `{typography.button-md}`.

**`button-pill`** — A special accent button reserved for limited-edition drops or sale items. It uses the warm terracotta `{colors.accent-terracotta}` and fully rounded corners (`{rounded.full}`), creating a friendly, tactile contrast to the brand’s otherwise rectilinear button system.

### Cards
**`product-card`** — The primary product display unit, a white card with soft `{rounded.lg}` corners that mimic the gentle curve of a ceramic bowl. It contains a product image, title, price, and a subtle “Add to Cart” link. On hover, a soft shadow (`0 4px 12px rgba(38,33,26,0.1)`) lifts the card, suggesting the weight and presence of the object it represents.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height, using the warm canvas `{colors.canvas}` as its background. Navigation links are set in uppercase `{typography.nav-link}` with a 0.3px letter-spacing, echoing the brand’s catalog aesthetic. The bar includes a centered logo, left-aligned category links (Dinnerware, Serveware, Home Goods), and a right-aligned search icon and cart icon.

### Forms
**`text-input`** — A clean, borderless input field on a white background, used for search, newsletter signup, and checkout forms. On focus, a 2px solid border in `{colors.primary}` appears, grounding the input like a pencil line on a sketch. The placeholder text uses `{colors.muted-soft}`.

### Footer
**`footer-section`** — A dark, grounding footer using `{colors.dark-bg}` (near-black) that anchors the page. Links are set in `{colors.muted-soft}` with `{typography.link}`, and the section includes columns for About, Customer Service, and Sustainability. The overall effect is that of a kiln’s cool-down chamber — quiet, solid, and final.

### Badges
**`badge`** — Small, pill-shaped badges in the aged gold `{colors.accent-gold}`, used for “New,” “Limited Edition,” or “Back in Stock” labels. The dark ink text (`{colors.ink}`) ensures readability against the warm metallic background.

### Search
**`search-bar`** — A fully rounded (`{rounded.full}`) white input field for site search, sitting within the nav bar or on collection pages. Its pill shape invites interaction, and the placeholder text reads “Search products…” in `{colors.body}`.

### Accordion
**`accordion-header`** — Used for FAQ sections and product details (e.g., “Dimensions,” “Care Instructions”). The header sits on a soft `{colors.surface-soft}` background with no rounded corners, and the content area below uses the canvas background. The transition between states is smooth, like opening a drawer.

### Hero
**`hero-section`** — A full-width, full-viewport-height section that introduces collections or seasonal stories. It uses the canvas background with large, light-weight typography (`{typography.display-xl}` at 300 weight) and generous padding. A single accent color (often `{colors.accent-slate}` or `{colors.accent-terracotta}`) appears in a decorative line or button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger menu; hero text reduces to `{typography.display-md}`; buttons become full-width; footer stacks vertically. |
| Tablet | 744–1128px | Two-column product grid; nav bar shows all links but with reduced padding; hero uses `{typography.display-xl}` at 28px; search bar moves to a collapsible icon. |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero at full `{typography.display-xl}`; standard button widths. |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero text scales up to 42px; additional whitespace around all sections. |

### Touch Targets
- All buttons and links have a minimum touch target of 44x44px on mobile.
- Product card images are tappable and link to the product page.
- Accordion headers have a 48px minimum height for easy tapping.
- Search bar and cart icon in the nav bar are at least 44x44px.

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu with a slide-out drawer.
- The search bar collapses to a search icon that opens a full-screen overlay on mobile.
- Product filters (on collection pages) collapse to a “Filter” button that opens a modal on mobile.
- The footer’s multi-column layout collapses to a single column with accordion-style sections on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit font-family declarations were found in the extracted CSS; the system stack (`'Helvetica Neue', Helvetica, Arial, sans-serif`) is assumed based on common DTC brand usage and the brand’s mid-century modern aesthetic. A custom typeface (e.g., a licensed serif for headings) may be used in production but was not detectable.
- Hover and focus states for text inputs, buttons, and links are inferred from the brand’s color palette and common patterns; exact transition durations and shadow values are not available.
- Error styling for forms (e.g., red borders, error message typography) is not present in the extracted data; a standard `#dc6650` (terracotta) error treatment is assumed.
- Sub-brand or collection-specific palettes (e.g., “Summer Collection” or “Heath x Artist”) may exist but are not captured here.
- Dark mode is not supported or detectable; the brand’s dark footer (`#121212`) suggests a potential dark mode direction, but no system-level implementation exists.
- The `meta theme-color` is absent, meaning the browser chrome color is not controlled; this may be a gap for PWA or mobile web experiences.
- Animation and transition timing values (e.g., hover fade-in duration, card lift speed) are not specified; a default of 200ms ease-in-out is recommended.
- Accessibility contrast ratios for some accent colors (e.g., `{colors.accent-gold}` on white) have not been verified against WCAG standards.
