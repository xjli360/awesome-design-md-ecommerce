---
version: alpha
name: "ViewSonic"
source_url: "https://www.viewsonic.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep crimson (#990000) bleeds through every navigation hover, CTA gradient terminus, and category accent on ViewSonic's site — a color closer to dried lacquer than the cherry-reds typical of consumer electronics, anchoring the interface in something almost industrial. The palette doubles down with #db0025 for primary action buttons and promotional flashes, while #6e0000 lurks beneath as the pressed/active darkening — three registers of the same red bloodline. Body type runs Open Sans at 400/600 weights across a neutral Helvetica Neue fallback stack, kept deliberately unserifed and tight-tracked so product specs and comparison tables remain scannable at 14px. Display headlines push to 600–700 weight but rarely exceed 32px; the brand lets full-bleed monitor photography do the shouting. Cards and product tiles sit on #ffffff surfaces with `{rounded.xs}` corners — barely softened rectangles that echo the physical geometry of bezels and screens. The canvas alternates between pure white and #f2f2f2 banding for section separation, with #e2e2e2 hairlines dividing spec rows. A secondary palette surfaces in product-category contexts: #7fbbe7 (a washed cerulean for "Business" lines), #ff5501 (a construction-cone orange for gaming/promotional urgency), and a quiet #c5d7ce sage that appears in sustainability messaging. Navigation is a sticky black bar (#111111) with white type, collapsing to a hamburger below 1024px. Spacing is utilitarian — `{spacing.base}` (16px) between card grid gutters, `{spacing.section}` (64px) between marketing bands — and the overall density is high: ViewSonic packs monitor specs, comparison toggles, and purchase CTAs into viewport-height hero modules without scroll prompting.

colors:
  primary: "#990000"
  primary-bright: "#db0025"
  primary-active: "#6e0000"
  primary-disabled: "#c2a0a0"
  accent-orange: "#ff5501"
  accent-blue: "#7fbbe7"
  accent-sage: "#c5d7ce"
  accent-sage-dark: "#607068"
  accent-cream: "#fdf0d5"
  alert-red: "#e02b27"
  ink: "#111111"
  body: "#303030"
  muted: "#555555"
  muted-soft: "#777777"
  muted-light: "#7d7d7d"
  hairline: "#d1d1d1"
  hairline-soft: "#e2e2e2"
  border-mid: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-band: "#f2f2f2"
  surface-card: "#ffffff"
  surface-muted: "#f0f0f0"
  surface-divider: "#e8e8e8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  nav-bg: "#111111"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-lg:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.15px
  display-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  spec-label:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  spec-value:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  mono:
    fontFamily: "Consolas, Monaco, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
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
  section-lg: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary-bright}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-cta-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  nav-bar-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    hoverBorder: "1px solid {colors.primary}"
  product-card-image:
    backgroundColor: "{colors.surface-band}"
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
    padding: "{spacing.md}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-secondary:
    backgroundColor: "{colors.surface-band}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    minHeight: 360px
    padding: "{spacing.xxl} {spacing.xl}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.surface-divider}"
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.surface-divider}"
  comparison-toggle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    activeBackgroundColor: "{colors.primary-bright}"
    activeTextColor: "{colors.on-primary}"
  category-badge:
    backgroundColor: "{colors.surface-band}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  promo-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 40px
    border: "1px solid {colors.border-mid}"
    padding: "0 12px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    hoverColor: "{colors.on-dark}"
  breadcrumb:
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
    width: 260px
    border: "1px solid {colors.hairline-soft}"

---

## Components

### Buttons

**`button-primary`** — Filled red (#db0025) rectangle with 4px radius and white 14px semi-bold text. On hover, background darkens to `{colors.primary-active}` (#6e0000). Disabled state shifts to a desaturated rose-gray. Used for "Buy Now," "Add to Cart," and primary form submissions across the product detail and checkout flows.

**`button-secondary`** — White fill with a 1px red border and red text. Hover fills the background with `{colors.surface-soft}` and deepens the border to the active red. Commonly used for "Compare," "Add to Wishlist," and secondary navigation actions on product pages.

**`button-ghost`** — No background, red text only. Appears inline for "Learn More" and "View All" links that need slightly more weight than a text hyperlink.

**`button-cta-orange`** — High-urgency orange (#ff5501) button used sparingly for promotional campaigns, gaming product launches, and limited-time offers. Larger at 48px height with 16px bold text. The orange reads as a one-time promotional interrupt against the otherwise red-and-gray system.

### Navigation

**`nav-bar`** — A 56px sticky header bar with #111111 background and white text. ViewSonic logo left-aligned, product category mega-menu links centered, search icon and account/cart utilities right-aligned. On scroll, a subtle 1px bottom shadow appears. The dark bar provides maximum contrast for the full-bleed product photography that typically begins immediately below.

**`nav-bar-dropdown`** — White mega-menu panels that unfurl on hover, organized into product-line columns (Monitors, Projectors, Digital Signage, etc.) with thumbnail images for featured products. No border-radius — panels are hard-edged to align with the rectilinear nav bar.

### Product Display

**`product-card`** — A vertical card with 4/3 aspect-ratio image area (light gray #f2f2f2 background for product shots on transparent backgrounds), followed by product name in `{typography.title-sm}`, a one-line spec summary in `{typography.caption}`, and price. Cards have a 1px #e2e2e2 border that shifts to the brand red on hover, signaling interactivity. Grid spacing uses `{spacing.base}` gutters.

**`product-card-image`** — The image container within product cards uses the band gray as backdrop, with `{spacing.md}` internal padding so products never bleed to the card edge. Monitor product shots are consistently shown at a 15° angle.

### Spec & Comparison

**`spec-table-row`** — Alternating white and #f4f4f4 rows for specification tables. Label column uses `{typography.spec-label}` (13px/600), value column uses `{typography.spec-value}` (13px/400). Rows are separated by 1px #e8e8e8 borders. High information density — typically 20-40 rows visible per product.

**`comparison-toggle`** — Small pill-shaped toggles (4px radius) that activate product comparison columns. Inactive state is light gray with muted text; active state fills with the bright red and flips text to white. Appears in a sticky sub-header when comparison mode is engaged.

### Hero & Marketing

**`hero-banner`** — Full-width dark (#111111) panels with display-xl white text and a large product render. Minimum height 480px. Copy is typically left-aligned with product image right-aligned or centered behind. ViewSonic uses these for new product launches and technology showcases (e.g., ColorPro series, gaming monitors).

**`hero-banner-secondary`** — Lighter variant on #f2f2f2 with dark text. Used for mid-page feature callouts and technology explanations (refresh rate, color accuracy panels). Smaller minimum height at 360px.

### Badges & Labels

**`category-badge`** — Neutral gray pill indicating product line ("Gaming," "Business," "Creative"). Small 12px bold text on the #f2f2f2 surface.

**`promo-badge`** — Orange (#ff5501) filled badge for "NEW," "SALE," or "HOT" indicators. Placed in the top-left corner of product cards, overlaying the image area.

### Search

**`search-bar`** — A 40px-tall input with medium-gray border, expanding to full mega-search overlay on focus (desktop) or a full-screen takeover on mobile. Placeholder text reads "Search products, specs, or solutions..." in muted gray.

### Footer

**`footer`** — Dark (#111111) multi-column footer with link groups organized by audience: Products, Solutions, Support, About. Links render in #d1d1d1 and brighten to white on hover. Bottom row contains legal links, region selector, and social icons. Generous `{spacing.section}` top padding separates it from content.

### Utility

**`breadcrumb`** — Muted gray text path with "/" separators, positioned below the nav bar and above product content. Uses `{typography.caption}` at 12px.

**`filter-sidebar`** — A 260px left-rail panel on product listing pages with checkbox filters for resolution, screen size, panel type, and price range. Each filter group is collapsible with a `{typography.title-sm}` header.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | Hamburger nav replaces mega-menu; product grid collapses to 1-column; hero text shrinks to display-md; spec tables become horizontally scrollable cards; filter sidebar becomes a bottom-sheet overlay; footer stacks into accordion sections |
| Tablet | 768–1024px | 2-column product grid; nav remains dark bar but categories collapse into a "Products" dropdown; hero images scale down but maintain minimum 320px height; comparison limited to 2 products side-by-side |
| Desktop | 1024–1440px | Full mega-menu navigation; 3-4 column product grid; spec comparison supports up to 3 products; filter sidebar is persistent; hero banners at full 480px height |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid expands to 4-5 columns; additional whitespace padding on hero banner sides; mega-menu panels widen for more thumbnail previews |

### Touch Targets
- All interactive elements maintain minimum 44px touch target on mobile/tablet
- Product card tap area extends to the full card surface, not just the text link
- Filter checkboxes are padded to 48px row height on touch devices
- Navigation hamburger icon has 48×48px hit area

### Collapsing Strategy
- Mega-menu → hamburger with accordion sub-menus at < 768px
- Product comparison bar → hidden; accessed via a floating "Compare" FAB on mobile
- Filter sidebar → bottom-sheet modal triggered by a sticky "Filter" button
- Spec tables → horizontal scroll with sticky first column (label column)
- Footer columns → collapsible accordion groups with chevron indicators
- Hero banner copy + image side-by-side → stacked vertically (copy above image)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font beyond Open Sans detected; ViewSonic may load a proprietary display face via JS or font-display swap that was not captured in the static extraction
- The iconic three-bird logo colors (red/green/blue) are partially represented in the palette (#990000 red, #7fbbe7 blue, #c5d7ce sage-green) but exact logo-mark hex values may differ from UI tokens
- No CSS custom properties or design-token file was extractable — the site appears to run on a Magento/Adobe Commerce instance with compiled CSS
- Animation/transition timing values were not captured; ViewSonic likely uses subtle fade-ins on scroll for product cards and hero elements
- Dark-mode variant was not detected — the site appears to be light-only despite the dark nav and footer
- Exact icon set is unclear; `luma-icons` and `icons-blank-theme` suggest Magento defaults rather than a custom icon library
- Gaming sub-brand (ELITE) may use a distinct color/typography sub-system not fully represented in the main site extraction
- No evidence of a formal spacing scale in the CSS — the spacing tokens above are inferred from observed patterns rather than declared variables
