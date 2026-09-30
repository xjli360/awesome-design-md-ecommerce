---
version: alpha
name: "Grimey's New & Loved Music"
source_url: "https://www.grimeys.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, ink-black canvas (#040404) frames a record store that wears its history in every corner — the primary red (#bd0000) isn't a friendly accent but a vintage neon sign, a hot pulse against the near-black. The palette reads like a dimly lit shop floor: warm whites (#fbfbfb, #fafafa) for text and card surfaces, a secondary red (#cc3b3b) for hover states and sale tags, and a muted gray (#aaaaaa) for secondary info and hairline borders. The type family Alice, a serif with a gentle, old-press character, runs across display and body sizes, giving the brand a literary, lived-in feel — not the clean sans-serif of a modern retailer but the voice of a zine or a hand-printed flyer. Buttons and badges use the full red (#bd0000) with white text, while secondary actions sit in the near-black (#111111) with white text, creating a high-contrast, no-nonsense hierarchy. The layout leans on generous spacing — {spacing.lg} between sections, {spacing.base} between elements — and soft corners ({rounded.sm}, {rounded.md}) that keep the interface from feeling harsh despite the dark canvas. The overall mood is intimate, slightly gritty, and deeply analog: a digital storefront that respects the vinyl it sells.

colors:
  primary: "#bd0000"
  primary-active: "#cc3b3b"
  primary-disabled: "#e99292"
  ink: "#040404"
  body: "#111111"
  muted: "#aaaaaa"
  muted-soft: "#e1e1e1"
  hairline: "#272727"
  hairline-soft: "#1e1e1e"
  canvas: "#040404"
  surface-soft: "#111111"
  surface-card: "#1e1e1e"
  on-primary: "#ffffff"
  on-dark: "#fbfbfb"
  accent-red: "#cc3b3b"
  accent-warm-white: "#fafafa"
  accent-light-gray: "#eeeeee"
  sale-tag: "#bd0000"
  star-rating: "#fbfbfb"

typography:
  display-xl:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    borderColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 32px 0
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: 64px 0
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  category-tab-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  link-inline:
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  link-inline-hover:
    textColor: "{colors.primary-active}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand's signature red (#bd0000) on a dark canvas. On hover, it shifts to a slightly lighter red (#cc3b3b) for visual feedback. Disabled state uses a muted pink (#e99292) to indicate unavailability. Padding is generous at 12px 24px, with a 6px corner radius that feels approachable without being pill-shaped.

**`button-secondary`** — A dark-surface button for secondary actions, using the card background (#1e1e1e) with white text. On hover, the background darkens to the hairline color (#272727). This button is used for "Add to Wishlist" or "View Details" actions where the primary red would be too dominant.

**`button-tertiary-text`** — A text-only button with no background, used for subtle actions like "Cancel" or "Learn More." The text color matches the on-dark white (#fbfbfb), and it inherits the button-md typography for consistency.

### Cards
**`product-card`** — The core product display unit, using a dark card surface (#1e1e1e) with white text. Corners are rounded at 10px, and the card includes 16px padding for content. On hover, the background shifts to the surface-soft color (#111111) for a subtle lift effect. Used for vinyl albums, CDs, and merchandise.

**`badge`** — A small, uppercase label for sale items, new arrivals, or genre tags. Uses the primary red background with white text, tight 4px 8px padding, and 4px corner radius. The typography is a compact 11px uppercase badge style.

### Navigation
**`nav-bar`** — A fixed top navigation bar on the dark canvas (#040404), 64px tall. Navigation links use the nav-link typography (16px, serif, with slight letter-spacing). The bar remains transparent to the canvas, letting the content breathe without a separate background layer.

**`category-tab`** — A text-based tab for filtering by genre or format (e.g., "Vinyl," "CD," "New," "Used"). Inactive tabs use the muted gray (#aaaaaa) text; the active tab uses a dark card background (#1e1e1e) with white text and 6px rounded corners.

### Forms
**`text-input`** — A dark input field with a card background (#1e1e1e) and a subtle hairline border (#272727). On focus, the border switches to the primary red (#bd0000) for clear visual feedback. Padding is 12px 16px, matching the button height at 44px.

**`search-bar`** — A pill-shaped search field (full rounded) for the site's search functionality. Uses the same dark card background and hairline border, with 20px horizontal padding for comfort. The pill shape contrasts with the more angular cards, giving the search action a distinct, friendly identity.

### Footer
**`footer`** — A full-width footer on the dark canvas, with text in the muted gray (#aaaaaa) for secondary information like links, copyright, and store hours. Padding is 32px top and bottom, with body-sm typography for readability.

### Hero
**`hero-section`** — A full-width hero area on the dark canvas, using the display-xl typography (36px serif) for a bold, editorial headline. Padding is 64px top and bottom, creating a generous vertical rhythm that lets the brand's voice land without visual clutter.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero text reduces to display-lg (28px); search bar moves to top of page |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links (Home, Shop, About); hero padding reduces to 48px; category tabs wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links; hero at full 64px padding; search bar in nav-bar |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero text scales to 40px display-xl; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons and badges are at least 32px × 32px.
- Nav-bar links have 48px touch targets (padding + height).
- Search bar is 48px tall for easy tapping.

### Collapsing Strategy
- On mobile, the nav-bar collapses to a hamburger icon; the full menu appears as a slide-in drawer from the left.
- Category tabs collapse to a horizontal scrollable strip on mobile, with the active tab pinned to the left.
- Product cards stack to a single column on mobile; the grid reflows to two columns on tablet and three on desktop.
- The hero section reduces vertical padding on tablet (48px) and mobile (32px) to conserve space.
- Footer links collapse to a single column on mobile, with reduced padding.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors are heavily weighted toward dark tones and reds; the brand may have additional accent colors (e.g., for genre tags or sale badges) that were not captured.
- The font-family list included Arial and Helvetica as fallbacks; Alice was the only serif found, but the brand may use a secondary sans-serif for UI elements (e.g., prices, dates) that was not extracted.
- Hover and focus states for all components (except buttons and inputs) are inferred from the brand's dark theme; actual implementations may vary.
- Error states for forms (validation messages, error borders) were not observed; a red error style using the primary-active color (#cc3b3b) is assumed.
- Dark mode is the default (and only observed) theme; no light mode or high-contrast variant was detected.
- Sub-brand or seasonal palettes (e.g., Record Store Day, holiday sales) were not extracted.
- The site's meta theme-color was not set; the browser chrome may default to white or system color.
- Stock photography and album art may introduce additional colors that are not part of the design system.
