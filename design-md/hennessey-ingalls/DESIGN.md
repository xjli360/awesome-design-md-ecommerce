---
version: alpha
name: "Hennessey + Ingalls"
source_url: "https://www.hennesseyingalls.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-blue (#003399) storefront that reads as a scholar’s library rendered for the web — the primary color is a confident, almost academic navy that anchors the header, primary buttons, and footer, while a warm maroon (#5f3f3f) and a muted teal (#2f4550) layer in as secondary accents that suggest leather bindings and aged paper. The palette is deliberately restrained: a clean white canvas (#ffffff) supports body text in a dark charcoal (#2b2b2b), with a soft gray (#c5c5c5) for hairline borders and a lighter gray (#e9e9e9) for subtle surface distinctions. A single bright accent — a golden yellow (#dad55e) — appears sparingly, perhaps on sale badges or callout elements, providing the only jolt of warmth against the otherwise cool, serious palette. Typography leans on Bitter (a slab serif with a literary feel) for display headings, paired with Figtree (a clean, modern sans-serif) for body text and navigation, creating a tension between tradition and readability. Buttons are rectangular with minimal rounding ({rounded.sm}), reinforcing the brand’s no-nonsense, intellectual character. The overall mood is one of quiet authority: this is a place for browsing rare and used books, not for flashy promotions. The site trusts its content — book covers, author names, and category headers — over decorative flourishes, using generous whitespace and a consistent grid to let the inventory speak.

colors:
  primary: "#003399"
  primary-active: "#002266"
  primary-disabled: "#b3c6ff"
  ink: "#2b2b2b"
  body: "#454545"
  muted: "#676767"
  muted-soft: "#aaaaaa"
  hairline: "#c5c5c5"
  hairline-soft: "#d3d3d3"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#dad55e"
  accent-gold-soft: "#fffa90"
  accent-maroon: "#5f3f3f"
  accent-teal: "#2f4550"
  error: "#c84a41"
  error-soft: "#fddfdf"

typography:
  display-xl:
    fontFamily: "'Bitter', 'Crimson Pro', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Bitter', 'Crimson Pro', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Bitter', 'Crimson Pro', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Figtree', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  nav-link-active:
    textColor: "{colors.accent-gold}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "8px 16px"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    fontWeight: 600
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  category-badge-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
  sale-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    textColor: "{colors.accent-gold}"
    opacity: 1
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-lg}"
    color: "{colors.muted}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    margin: "0 {spacing.xs}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.sm}"
  accordion-content:
    padding: "{spacing.base}"
    typography: "{typography.body-md}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Sign Up". Rendered in the brand navy {colors.primary} with white text, a subtle {rounded.sm} corner, and 44px height for comfortable tapping. On hover/active, shifts to {colors.primary-active} (#002266). The disabled state uses {colors.primary-disabled} (#b3c6ff) to signal non-interactivity while maintaining brand consistency.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Cancel". Uses a white background with a 2px {colors.primary} border and navy text. On hover, fills solid with the primary color and inverts to white text. Height matches the primary button at 44px for alignment in forms.

**`button-ghost`** — A text-only button with no background or border, used for inline actions like "Clear Filters" or "Learn More". Text is {colors.primary} and the hit area is padded to 44px minimum for touch accessibility. On hover, a subtle background tint (rgba(0,51,153,0.05)) appears.

**`button-gold`** — A compact, high-visibility button reserved for sale items, limited-time offers, or loyalty program CTAs. Uses {colors.accent-gold} (#dad55e) background with dark {colors.ink} text. Shorter at 36px, it sits neatly within product cards or promotional banners without competing with the primary button hierarchy.

### Cards
**`product-card`** — The core inventory display unit. A white card with a subtle drop shadow (0 1px 3px rgba(0,0,0,0.08)) and {rounded.md} corners. Contains a 3:4 aspect ratio book cover image with {rounded.sm} corners, the title in {typography.title-md}, the author in {typography.body-sm} in {colors.muted}, and the price in bold {typography.body-md}. On hover, the shadow deepens to 0 4px 12px rgba(0,0,0,0.12) to signal interactivity. Padding is {spacing.base} (16px) on all sides.

### Navigation
**`nav-bar`** — A fixed-height (64px) top navigation bar in {colors.primary} with white text. Contains the store logo/name on the left, category links in the center, and utility icons (search, account, cart) on the right. Links use {typography.nav-link} (15px, weight 500) with {spacing.sm} vertical and {spacing.md} horizontal padding. The active link or current section is highlighted in {colors.accent-gold}. On mobile, the nav collapses into a hamburger menu.

### Forms
**`text-input`** — Standard text input for search, login, and checkout forms. A white background with a 1px {colors.hairline} (#c5c5c5) border and {rounded.sm} corners. On focus, the border thickens to 2px {colors.primary} with no outline. Error state uses a 1px {colors.error} (#c84a41) border. Height is 44px with 10px 14px padding for comfortable text entry.

### Search
**`search-bar`** — A pill-shaped ({rounded.full}) search field typically placed in the hero or below the nav. White background with a 1px {colors.hairline} border, 40px height, and 8px 16px padding. Uses {typography.body-md} for input text. On focus, the border transitions to 2px {colors.primary}. The search icon sits at the left edge as a visual affordance.

### Badges
**`category-badge`** — A pill-shaped ({rounded.full}) tag for filtering or browsing by genre (e.g., "Fiction", "History", "Art"). Uses a light gray background ({colors.surface-soft}) with muted text. The active state fills with {colors.primary} and white text. Padding is 4px 12px with uppercase {typography.badge} (11px, weight 700).

**`sale-badge`** — A small, rectangular ({rounded.sm}) badge for marking discounted items. Uses {colors.accent-gold} background with dark {colors.ink} text. Compact at 2px 8px padding, it sits in the top-left corner of product card images without overwhelming the cover art.

### Footer
**`footer`** — A full-width footer in {colors.primary} with white text. Contains columns for "About Us", "Customer Service", "Categories", and "Connect". Links are in {typography.link} with 0.85 opacity, transitioning to full opacity and {colors.accent-gold} on hover. Padding is {spacing.xxl} (48px) top and bottom with {spacing.xl} (32px) horizontal.

### Hero
**`hero-section`** — A full-width banner at the top of the homepage or category pages. Uses a light gray background ({colors.surface-soft}) with generous padding ({spacing.section} vertical, {spacing.xl} horizontal). The title uses {typography.display-xl} (36px Bitter, weight 700) in {colors.ink}, with a subtitle in {typography.body-lg} in {colors.muted}. A search bar and/or primary CTA sits below the text.

### Pagination
**`pagination-button`** — Used on search results and category listing pages. A white button with a 1px {colors.hairline} border and {rounded.sm} corners. The active page uses {colors.primary} fill with white text. Buttons are 36px tall with 8px 12px padding. Previous/Next arrows use the same styling.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column (100% width); hero padding reduces to {spacing.xl} vertical; search bar moves below hero text; footer columns stack vertically; category badges wrap in a horizontal scroll strip |
| Tablet | 744–1128px | Nav links remain visible but reduce font size to 14px; product cards display in 2-column grid; hero uses 60/40 text-to-image split; footer shows 2-column layout; category badges show in a 3-column grid |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero uses 50/50 split with larger imagery; footer shows 4-column layout; sidebar filters appear on category pages |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-column grid; hero content max-width at 1200px; additional whitespace on sides; footer columns expand to 5 with more link groups |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and minimum width of 44px for touch accessibility.
- Nav links have 48px touch targets even if the text is smaller.
- Product cards are fully tappable, with the entire card surface acting as a link to the product detail page.
- Search bar has a 48px touch height on mobile devices.
- Pagination buttons are 44px x 44px minimum on touch screens.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at < 744px, with the logo centered and icons (search, cart, account) moved to a bottom tab bar or persistent header.
- Sidebar filters on category pages collapse into a "Filters" button that opens a modal or slide-in panel on mobile and tablet.
- Product card grids reduce columns: 4 → 3 → 2 → 1 as viewport shrinks.
- Footer columns collapse from 5 to 4 to 2 to 1, with the first column (About) always visible and the rest toggling via accordion on mobile.
- Hero sections reduce padding and may hide secondary imagery on mobile, keeping only the headline, subtitle, and search bar.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons, cards, and links are inferred from common patterns; exact transition durations and easing curves were not extracted from the live site.
- Error styling for form validation (error messages, iconography, border colors) is based on the extracted {colors.error} (#c84a41) but the specific implementation (inline vs. tooltip, icon usage) is unknown.
- The extracted color list includes many generic web colors (multiple grays, blues, pinks) that may come from third-party widgets, stock images, or framework defaults. The primary (#003399) and accent (#dad55e) are the most distinctive and likely brand-specific; the maroon (#5f3f3f) and teal (#2f4550) are plausible secondary accents but could also be image-derived.
- Font usage is inferred from extracted `font-family` declarations; exact weights, sizes, and pairings (Bitter for headings, Figtree for body) are based on common literary bookstore patterns and may not match the live site's actual CSS.
- Dark mode is not supported by the extracted data; the palette assumes a light theme only.
- Sub-brand or seasonal color variations (e.g., holiday themes, clearance sales) were not detected.
- The extracted `font-family` list includes "Apple Color Emoji" and "Consolas" which are likely fallbacks or system fonts, not actively used in the design system.
- Spacing and rounded values are estimated based on common design system patterns and the brand's aesthetic; exact values from the live site's CSS were not extracted.
- Component heights (e.g., 44px for buttons, 64px for nav) are standard accessibility recommendations and may differ from the live implementation.
