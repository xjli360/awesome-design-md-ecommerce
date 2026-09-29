---
version: alpha
name: "Printed Matter"
source_url: "https://www.printedmatter.org"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A riot of saturated color against a white page — #e90c8c, #5187ed, #ef882d, #fdd028, #38f4a5, #28bafd, #e7a3a0 — the brand's palette reads like a zine library exploded across the screen, each hue a different cover screaming for attention. The primary pink (#e90c8c) is the loudest voice in the room, used sparingly but unmistakably for key actions and headers, while a secondary chorus of electric blue, marigold, mint, and coral fills badges, tags, and category markers. BellGothicStd-Black, a heavy, slightly condensed gothic typeface, provides the typographic muscle — it appears in all-caps display settings at 28–36px with tight tracking, evoking punk flyers and photocopied manifestos. Body copy defaults to Arial/Helvetica at 14–16px, clean and utilitarian, letting the display type do all the emotional work. Corners are mostly sharp ({rounded.none} to {rounded.sm}) — there are no pill buttons or soft cards here; the brand treats the browser as a printed page, with rectangular blocks, hard edges, and generous white gutters. The nav bar is a simple horizontal strip of BellGothicStd-Black links in all caps, with a search bar that sits flush to the grid rather than floating. Product cards are minimal: a cover image, a title in the gothic face, a price in body weight. The overall feel is not "ecommerce" but "catalog" — a direct, unadorned, slightly anarchic presentation that trusts the content (artists' books, zines, ephemera) to provide the visual interest.

colors:
  primary: "#e90c8c"
  primary-active: "#c00a75"
  primary-disabled: "#f4a0d0"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#5187ed"
  accent-orange: "#ef882d"
  accent-yellow: "#fdd028"
  accent-mint: "#38f4a5"
  accent-cyan: "#28bafd"
  accent-coral: "#e7a3a0"
  accent-green: "#14720f"
  accent-brown: "#ac947e"
  accent-lime: "#b6d825"
  accent-purple: "#9974d9"
  accent-hot-pink: "#fa0064"
  accent-salmon: "#fa4a5a"
  accent-rose: "#db6b94"
  accent-magenta: "#f261c2"
  accent-light-pink: "#fc91d2"
  accent-pale-pink: "#f9a2f9"
  accent-blush: "#f4bed7"
  accent-coral-pink: "#f48395"
  accent-burnt-orange: "#dc5917"
  accent-peach: "#f7a653"
  accent-gold: "#d9ac28"
  accent-lemon: "#e5dc37"
  accent-sunflower: "#feef2d"
  accent-olive: "#90c541"
  accent-forest: "#1b9713"
  accent-dark-green: "#3a552d"

typography:
  display-xl:
    fontFamily: "'BellGothicStd-Black', 'Helvetica', 'Arial', sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: 1.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'BellGothicStd-Black', 'Helvetica', 'Arial', sans-serif"
    fontSize: 28px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: 1.2px
    textTransform: uppercase
  display-md:
    fontFamily: "'BellGothicStd-Black', 'Helvetica', 'Arial', sans-serif"
    fontSize: 22px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  display-sm:
    fontFamily: "'BellGothicStd-Black', 'Helvetica', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 900
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  title-md:
    fontFamily: "'BellGothicStd-Black', 'Helvetica', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  title-sm:
    fontFamily: "'BellGothicStd-Black', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
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
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'BellGothicStd-Black', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'BellGothicStd-Black', 'Helvetica', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  link:
    fontFamily: "'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'BellGothicStd-Black', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'BellGothicStd-Black', 'Helvetica', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  button-accent-mint:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-hot-pink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  product-card-author:
    typography: "{typography.caption}"
    color: "{colors.muted-soft}"
    marginTop: "{spacing.xxs}"
  badge-new:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.accent-hot-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  badge-limited:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  badge-artist:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
  category-tag-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.canvas}"
    textDecoration: underline
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in BellGothicStd-Black uppercase on a vivid pink (#e90c8c) background. Sharp corners ({rounded.none}) reinforce the print-catalog ethos. On hover, the background shifts to a darker pink (#c00a75). The disabled state uses a washed-out pink (#f4a0d0) with reduced opacity. **`button-secondary`** — An outlined variant with a 2px black border on a white background. On hover, the fill and text invert to black-on-white. **`button-tertiary-text`** — A text-only button with no background or border, used for less prominent actions like "View all" or "Cancel". **`button-accent-*`** — A family of small accent buttons (blue, orange, yellow, mint) used for filtering, tagging, or category selection. Each uses its respective accent color as background with white or black text depending on contrast.

### Cards
**`product-card`** — A minimal, borderless card with a full-bleed cover image, the title set in BellGothicStd-Black uppercase at 14px, the price in Arial body at 14px in muted gray, and the author name in 12px caption weight. No rounded corners, no shadow — the card is simply an image with text below, separated by 8px of vertical space. On hover, the image may shift or the title may change color to the primary pink, but the card itself remains flat.

### Navigation
**`nav-bar`** — A 60px-high horizontal strip with a white background and a 1px bottom border. Links are set in BellGothicStd-Black uppercase at 14px with 0.8px letter-spacing. The active and hover states switch the link color to the primary pink (#e90c8c). The search bar sits to the right, a simple rectangular input with a gray background and a pink submit button.

### Forms
**`text-input`** — A rectangular input with a 1px gray border, 44px height, and Arial body text. On focus, the border thickens to 2px and turns pink. On error, the border becomes 2px hot pink (#fa0064). **`search-bar`** — Similar to the text input but with a gray background (#f5f5f5) and a separate pink submit button.

### Badges
**`badge-*`** — Small, sharp-cornered labels in BellGothicStd-Black uppercase at 11px. Each badge uses a distinct accent color: mint for "New", hot pink for "Sale", yellow for "Limited Edition", blue for "Artist Book". These are the primary way the brand communicates status without relying on icons or imagery.

### Footer
**`footer`** — A full-width black band with white text, using Arial body at 14px. Links are underlined white text. The footer contains the standard legal, about, and contact information, plus links to the Printed Matter / St. Mark's Books locations.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; product cards stack vertically; search bar moves below nav; hero text reduces to 24px display size; footer links stack. |
| Tablet | 744–1128px | Two-column grid for product cards; nav remains horizontal but links may be truncated; search bar is full-width below nav; hero text at 28px. |
| Desktop | 1128–1440px | Three-column grid for product cards; full nav with all links visible; search bar in nav; hero text at 36px. |
| Wide | > 1440px | Four-column grid for product cards; max-width container at 1440px; nav and search remain as desktop. |

### Touch Targets
- All buttons and links have a minimum touch target of 44x44px.
- Product card images are tappable and link to the product page.
- The hamburger menu icon on mobile is 48x48px.
- Badges are 20px tall but are always part of a larger tappable card or button.

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger menu with a slide-out drawer.
- The search bar collapses from a full input to an icon that expands on tap.
- The product grid collapses from 3–4 columns to 1–2 columns.
- The footer collapses from a multi-column layout to a single stacked column.
- Category tags collapse from a horizontal scrollable strip to a dropdown select on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (image zoom, color shift, shadow) could not be reliably extracted from the static HTML/CSS.
- Error states for forms beyond the hot-pink border are unknown (error message styling, icon placement).
- The exact font weight for BellGothicStd-Black is assumed to be 900; the actual weight may vary (the font file may define it differently).
- Sub-brand or section-specific palettes (e.g., Printed Matter / St. Mark's Books vs. Printed Matter / LA Art Book Fair) are not captured.
- Dark mode or high-contrast mode styles are not present in the extracted data.
- The spacing system is inferred from common grid patterns; the actual site may use a different base unit.
- Animation and transition durations (e.g., hover fades, menu slide-in speed) are unknown.
- The extracted color list includes many accent colors that may be used sparingly or only in specific contexts (e.g., event pages, artist features). Their exact usage frequency is unknown.
- The `textTransform: uppercase` property for BellGothicStd-Black is inferred from the brand's print identity; the site may use CSS `text-transform` or rely on the font's all-caps nature.
