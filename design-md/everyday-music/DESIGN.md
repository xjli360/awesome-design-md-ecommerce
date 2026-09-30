---
version: alpha
name: "Everyday Music"
source_url: "https://www.everydaymusic.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep blue #116dff — the color of a record store's neon sign at dusk — anchors Everyday Music's digital storefront, appearing in primary buttons, navigation links, and hover states against a near-black #080808 ink and a cool gray #5f6360 for body text. The brand leans into a library-like seriousness with its typography stack: Cormorant Garamond for display headings (a serif that signals vintage record-sleeve sophistication) paired with Montserrat and Arial for body copy, creating a deliberate tension between old-world album art and modern e-commerce utility. The light blue wash of #e4ebfc surfaces in soft backgrounds and card states, suggesting the glow of a listening booth or a turntable's platter light. Everyday Music's design language is unpretentious but authoritative — it trusts its product photography and genre taxonomy over decorative flourishes, using generous whitespace and a restrained palette to let the records speak. The search bar, a primary entry point for crate-diggers, sits prominently with a full-pill shape, while product cards use soft rounded corners and minimal borders to keep focus on album covers. The overall mood is that of a well-organized basement archive: dark, focused, and rewarding to explore.

colors:
  primary: "#116dff"
  primary-active: "#0a4fbf"
  primary-disabled: "#a0c4ff"
  ink: "#080808"
  body: "#5f6360"
  muted: "#9aa0a6"
  muted-soft: "#c4c9d0"
  hairline: "#dadce0"
  hairline-soft: "#e8eaed"
  canvas: "#ffffff"
  surface-soft: "#e4ebfc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-new: "#116dff"
  badge-sale: "#080808"
  star-rating: "#fbbc04"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'CormorantGaramond', 'CormorantGaramond-Light', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cormorant Garamond', 'CormorantGaramond', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Arial', 'Helvetica', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Arial', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Arial', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Arial', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
  link:
    fontFamily: "'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Montserrat', 'Arial', 'Helvetica', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "#d93025"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 52px
    borderColor: "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    color: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 32px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart," "Checkout," and "Sign Up." Rendered in the brand's deep blue #116dff with white text and a soft 8px radius. On hover, shifts to `button-primary-active` (#0a4fbf) with a subtle darkening. Disabled state uses `button-primary-disabled` (#a0c4ff) to indicate inactivity.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Save for Later." White background with #080808 text and a 1px solid `{colors.hairline}` border. Active state fills the background with `{colors.surface-soft}` (#e4ebfc) for a gentle press effect.

**`button-tertiary-text`** — A text-only button for low-emphasis actions like "Cancel" or "Clear Filters." Uses the brand's primary blue for text color, with no background or border. Hover state adds a subtle underline.

**`button-pill`** — A compact, fully rounded button used for filter tags, "Pre-order" badges, and quick-add actions. Smaller padding and font size make it suitable for inline placement within product cards or category strips.

### Cards
**`product-card`** — The primary container for album listings. White background with a 12px rounded corner and a subtle 1px `{colors.hairline}` border. On hover, elevates with a soft box-shadow (`0 4px 12px rgba(0,0,0,0.08)`) to suggest a record being pulled from the shelf. The album cover image sits flush to the top with rounded top corners, while text details (artist, title, price) are padded below.

**`product-card-image`** — The image container within a product card, using a 12px radius on top corners only to match the card's curvature. Aspect ratio is typically 1:1 for album covers.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, white background, containing the store logo, genre links (Vinyl, CDs, Cassettes, Merch), and a search icon. Links use `{typography.nav-link}` with 0.5px letter spacing for a slightly elevated feel. Active or hovered links switch to `{colors.primary}`.

**`nav-link-active`** — Applied to the current page or section link. Uses the brand blue to indicate location within the site hierarchy.

### Forms
**`text-input`** — Standard text input for search, account forms, and checkout fields. White background with a 1px `{colors.hairline}` border and 8px radius. On focus, the border shifts to `{colors.primary}` (#116dff). Error state uses a red border (#d93025) with an error message below.

**`search-bar`** — The hero search element for crate-digging. A fully rounded pill shape (9999px) at 52px height, with a magnifying glass icon on the left and a clear button on the right. Uses `{typography.body-md}` for placeholder text like "Search artists, albums, labels…"

### Badges
**`badge-new`** — A small, blue badge for "New Arrival" tags. Uses `{typography.badge}` (10px, uppercase, bold) with 2px horizontal padding and a 4px radius. Placed on the top-left corner of product card images.

**`badge-sale`** — A black badge for sale or clearance items. Same typography and sizing as `badge-new`, but with a near-black background for high contrast against album art.

### Hero
**`hero-section`** — The full-width hero banner on the homepage, featuring a large serif headline (Cormorant Garamond, 36px) in white against a near-black #080808 background. Content is centered with generous padding (64px vertical, 32px horizontal). May include a secondary tagline and a `button-primary` CTA.

### Footer
**`footer`** — A dark footer matching the hero's background (#080808), containing links to "About Us," "Contact," "Shipping," "Returns," and social media icons. Text is set in `{typography.body-sm}` with `{colors.muted}` (#9aa0a6) for readability against the dark background. Links hover to white.

### Category Chips
**`category-chip`** — A pill-shaped filter chip for browsing by genre (Rock, Jazz, Hip-Hop, etc.). Uses a light blue background (#e4ebfc) with dark text. Active state fills with the brand's primary blue and white text to indicate the selected filter.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero text reduces to 24px; search bar shrinks to 44px height; category chips wrap to two rows |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 28px display; search bar at 48px height; category chips in a horizontal scrollable strip |
| Desktop | 1128–1440px | Three-column product grid; full nav with genre dropdowns; hero at 36px display; search bar at 52px height; category chips in a static row |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with wider margins; additional whitespace around product cards |

### Touch Targets
- All interactive elements (buttons, links, chips) maintain a minimum 44px height for mobile tap targets.
- Search bar and text inputs are at least 44px tall on all breakpoints.
- Category chips are 32px tall on desktop, expanding to 40px on mobile for easier tapping.
- Nav hamburger icon uses a 48x48px tap area.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu with a slide-out drawer.
- Category chips transition from a static row to a horizontally scrollable strip on tablet and mobile.
- Product grid reduces from 4 columns (wide) to 1 column (mobile) to maintain readable album art sizes.
- Footer links stack vertically on mobile, with social icons moving to a separate row.
- Hero section reduces vertical padding from 64px to 32px on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors (#116dff, #5f6360, #080808, #e4ebfc) appear to be a generic web palette (blue, gray, black, light blue) — the brand's true primary may be more distinctive if additional pages were scanned. The blue #116dff is used as primary based on its prominence in CTAs and links.
- Font-family declarations include many fallbacks (Arial, Helvetica, multiple avenir/cormorant variants) — the exact hierarchy and which fonts are used for which roles is inferred from common pairing patterns (serif for display, sans-serif for body).
- Hover states for buttons and cards are inferred from common e-commerce patterns; actual site hover colors may differ.
- Error styling for forms (text-input-error) uses a standard red (#d93025) as no brand-specific error color was extracted.
- Dark mode is not present on the live site; all colors assume a light theme.
- Sub-brand or seasonal palettes (e.g., Record Store Day, holiday sales) are not captured.
- Star rating color (#fbbc04) is a standard yellow and may not be brand-specific.
- Box-shadow values for product-card-hover are estimated; actual shadow depth and color may vary.
- The site may use additional typography weights (e.g., 300, 700) not declared in extracted font-family strings.
