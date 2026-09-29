---
version: alpha
name: "Guidecraft"
source_url: "https://guidecraft.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy #023e8a anchors Guidecraft’s digital storefront, a color that reads more like a trusted school uniform than a playful toy brand — it’s the hue of chalkboard frames and wooden block bins, lending gravity to a catalog of children’s furniture and preschool tools. The palette leans heavily on warm neutrals (#ebe3d5, #f3d196, #ebebeb) that echo unfinished wood and natural light, with a single sharp accent in #ff5742 — a coral-red used sparingly for sale badges and cart indicators, never for primary actions. Typography runs Brown and Poppins in display roles, with Inter for body copy, creating a layered hierarchy where headings feel hand-lettered and instructional text stays crisp. Product cards sit on white canvas with soft {rounded.sm} corners, while the navigation bar uses a full-width dark band (#19181d) that frames the logo like a storefront awning. The overall rhythm is unhurried: generous {spacing.lg} gutters, centered hero imagery of children interacting with furniture, and a footer dense with links and accreditation badges. Guidecraft does not shout — it arranges.

colors:
  primary: "#023e8a"
  primary-active: "#002a5e"
  primary-disabled: "#8fa8c4"
  ink: "#19181d"
  body: "#3d4246"
  muted: "#636466"
  muted-soft: "#9da1a0"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-coral: "#ff5742"
  accent-gold: "#f3d196"
  accent-warm: "#ebe3d5"
  nav-dark: "#19181d"
  footer-bg: "#353740"

typography:
  display-xl:
    fontFamily: "'Brown', 'Poppins', 'Helvetica', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Brown', 'Poppins', 'Helvetica', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Brown', 'Poppins', 'Helvetica', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Helvetica', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Inter', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Inter', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Inter', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Inter', 'Helvetica', sans-serif"
    fontSize: 11px
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
    border: "1px solid {colors.hairline}"
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
  nav-link-item:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-category:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
    hoverColor: "{colors.on-primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    marginBottom: "{spacing.md}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  category-grid:
    gap: "{spacing.base}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and form submissions. Rendered in deep navy #023e8a with white text and soft {rounded.sm} corners. On hover, shifts to `primary-active` (#002a5e). Disabled state uses `primary-disabled` (#8fa8c4) with reduced opacity. Padding is 12px 24px for a comfortable tap target.

**`button-secondary`** — Outlined variant for secondary actions like "Learn More" or "View Details". White background with ink text and a 1px hairline border. Hover state fills background with `surface-soft` (#f7f7f7). Height matches primary at 44px for visual consistency.

**`button-accent-coral`** — Compact accent button reserved for sale badges, cart quantity adjusters, and promotional CTAs. Uses the coral #ff5742 with white text, smaller padding (8px 16px), and shorter height (36px). Appears only in high-emphasis contexts.

### Cards
**`product-card`** — White card with soft {rounded.sm} corners and 16px padding. Contains a square aspect-ratio image with matching rounded corners, followed by the product title in `title-sm` and price in `body-md`. Hover state adds a subtle shadow (not captured in extracted data). Used in grid layouts with {spacing.base} gaps.

**`badge-sale`** — Small coral pill badge overlaid on product images to indicate discounts. Uses uppercase `badge` typography with tight padding (2px 8px) and {rounded.xs} corners.

**`badge-new`** — Navy badge identical in structure to `badge-sale` but signaling new arrivals. Positioned top-left on product cards.

**`badge-category`** — Warm neutral (#ebe3d5) pill badge used in category filters and navigation strips. Full rounded corners and 4px 12px padding for a more substantial appearance.

### Navigation
**`nav-bar`** — Full-width dark band (#19181d) at 72px height, containing the logo and navigation links. Links use `nav-link` typography in white with 8px 12px padding. The bar is fixed at the top of the viewport with a z-index above content.

**`nav-link-item`** — Individual navigation links with transparent background and white text. Hover state adds subtle opacity reduction (not captured). Active state uses `primary` underline or background highlight.

### Forms
**`text-input`** — Standard input field with white background, 1px hairline border, and {rounded.sm} corners. On focus, border thickens to 2px and shifts to `primary` (#023e8a). Height is 44px with 10px 14px padding for comfortable text entry.

**`search-bar`** — Full-rounded pill input for site search, using {rounded.full} corners and a 1px hairline border. Includes a magnifying glass icon (not captured in tokens) on the left side. Height matches other inputs at 44px.

**`newsletter-input`** — Email input used in the footer, identical structure to `text-input` but paired with a `button-primary` for submission. The combined component forms a horizontal row with no gap.

### Footer
**`footer-section`** — Dark gray (#353740) footer spanning the full page width, with 64px vertical padding and 24px horizontal gutters. Links use `footer-link` style with muted text that brightens to white on hover. Contains columns for support, about, and legal links, plus social icons (colors not extracted).

### Hero
**`hero-banner`** — Full-width section with light gray (#f7f7f7) background, 64px vertical padding, and centered content. Features a `display-xl` heading, `body-md` subheading, and a `button-primary` CTA. Background may alternate with lifestyle photography on certain pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces full menu, hero padding reduces to 32px, font sizes scale down one step |
| Tablet | 744–1128px | Two-column product grid, nav links collapse to icon-only, hero maintains 48px padding |
| Desktop | 1128–1440px | Three-column product grid, full nav visible, standard hero padding (64px) |
| Wide | > 1440px | Max-width container at 1440px, centered content, four-column product grid |

### Touch Targets
- All interactive elements maintain minimum 44px height
- Button padding ensures 44px tap target even on smaller screens
- Nav links have 8px 12px padding for adequate spacing
- Product card images are tappable with full-card hit area

### Collapsing Strategy
- Navigation links collapse to hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport shrinks
- Footer columns stack vertically below 744px
- Hero content centers and reduces padding on mobile
- Category filter strip scrolls horizontally on mobile rather than wrapping

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were not reliably extracted from the live site CSS
- Error styling for form inputs (validation colors, error messages) is absent from extracted data
- Social media icon colors (likely from platform-specific palettes) were filtered out but may include brand-specific variations
- Dark mode is not implemented on the current site
- Sub-brand or collection-specific color palettes (e.g., "Wooden Collection" vs "STEM") could not be extracted
- Animation durations, easing curves, and transition properties are unknown
- Shadow tokens (box-shadow values for cards, modals, dropdowns) were not captured
- Modal, dropdown, and tooltip component styles are undocumented
- The extracted font list includes "Brown" which may be a custom typeface — fallback stack is inferred from remaining declarations
- Some extracted hex colors (#008000, #000080, #ffc0cb, #87ceeb) appear to be stock-image dominant tones or widget defaults and are excluded from the palette
