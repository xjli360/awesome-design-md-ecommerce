---
version: alpha
name: "Fiddlershop"
source_url: "https://www.fiddlershop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A warm, instrument-focused marketplace built on a near-white canvas (#ffffff) and a deep, almost-ink black (#121212) that gives every product photo and detail page a crisp, gallery-like presence. The brand’s signature moves are subtle: a soft gray divider (#dedede) that separates sections without visual noise, and a typographic pairing of Figtree (clean, modern sans-serif for navigation and body copy) with Fraunces (a refined, slightly ornamental serif for display headings) that bridges traditional craftsmanship with contemporary e-commerce. Product cards use gentle rounded corners ({rounded.sm}) and generous whitespace ({spacing.lg}) to let the instruments — violins, cellos, basses — command attention. The top navigation is a simple, high-contrast bar with the brand name in Fraunces, signaling heritage, while the search bar and filter controls use Figtree for clarity. There is no aggressive accent color; the brand trusts its product imagery and the stark contrast of {colors.ink} on {colors.canvas} to create hierarchy. Buttons are solid, rectangular, and purposeful — no pill shapes, no gradients — reinforcing a no-nonsense, educational tone that says “we know instruments, and we want you to know them too.” The footer is dense with links, reflecting a catalog-driven business where every product category (violin, viola, cello, bass, accessories) needs clear entry points. The overall feel is that of a specialty shop that has been carefully digitized: clean, trustworthy, and built for browsing with intent.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#dedede"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#c0392b"
  badge-new: "#27ae60"
  badge-sale: "#c0392b"
  star-rating: "#f1c40f"

typography:
  display-xl:
    fontFamily: "'Fraunces', 'Georgia', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Fraunces', 'Georgia', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Fraunces', 'Georgia', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Fraunces', 'Georgia', serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  link:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  footer-link:
    fontFamily: "'Figtree', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0

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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 12px
    height: 44px
  text-input-focus:
    border: "1px solid {colors.ink}"
    boxShadow: "0 0 0 1px {colors.ink}"
  text-input-error:
    border: "1px solid {colors.accent}"
    boxShadow: "0 0 0 1px {colors.accent}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 32px 10px 12px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "8px 16px"
    height: 40px
  search-bar-focus:
    border: "1px solid {colors.ink}"
    backgroundColor: "{colors.canvas}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 14px"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    padding: "0 4px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.footer-link}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.footer-link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.base}"
  hero-banner-heading:
    typography: "{typography.display-xl}"
    marginBottom: "{spacing.md}"
  hero-banner-subtext:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  category-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  pagination-disabled:
    textColor: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for “Add to Cart,” “Checkout,” and key form submissions. Solid black background ({colors.primary}) with white text, a subtle 4px corner radius ({rounded.sm}), and 44px height for comfortable tapping. On hover, the background deepens to pure black ({colors.primary-active}). Disabled state uses the light gray divider color ({colors.primary-disabled}) with muted text to signal inactivity without visual noise.

**`button-secondary`** — Used for secondary actions like “View Details,” “Compare,” or “Cancel.” A white background with a 1px hairline border ({colors.hairline}) that matches the site’s clean, understated aesthetic. On hover, the border becomes solid ink and the background shifts to the soft surface tone ({colors.surface-soft}). Height and typography match the primary button for alignment in forms.

**`button-tertiary-text`** — A text-only button for inline actions such as “Clear filters” or “Learn more.” No background, no border — just the Figtree button typography in ink. Used sparingly to avoid visual clutter in dense UI areas like filter panels and product descriptions.

### Cards
**`product-card`** — The core product display unit on collection pages and search results. A white card with a subtle drop shadow (0 1px 3px rgba(0,0,0,0.08)) and no padding — the product image fills the top edge-to-edge. Title and price sit below the image with standard padding ({spacing.sm} top, {spacing.base} sides). On hover, the shadow deepens (0 4px 12px rgba(0,0,0,0.12)) to signal interactivity. Badges for “New” or “Sale” overlay the top-left corner of the image with uppercase, 11px type on green or red backgrounds.

**`category-card`** — Used on the homepage and category landing pages to link to instrument families (Violin, Viola, Cello, Bass, Accessories). A white card with a gentle shadow, centered title in Fraunces display-sm, and an optional background image or icon. Padding is generous ({spacing.lg}) to create a comfortable tap target. Hover deepens the shadow and optionally scales the image.

### Navigation
**`nav-bar`** — The persistent top navigation bar, 64px tall on desktop, with a white background and a soft bottom border ({colors.hairline-soft}). The brand name “Fiddlershop” sits on the left in Fraunces display-sm, while nav links (Violins, Violas, Cellos, Basses, Accessories, Rentals, Learn) use Figtree nav-link typography. Active link has a 2px bottom border in {colors.primary}. On mobile, the bar collapses to 56px and the links become a hamburger menu.

**`breadcrumb`** — A secondary navigation element on product detail and category pages. Uses caption typography in muted gray, with ink-colored links and a simple separator (/) in muted-soft. Helps users understand their location in the catalog hierarchy (Home > Violins > Student Violins).

### Forms
**`text-input`** — Standard text input for search, account forms, and checkout. White background, 1px hairline border, 44px height, and 4px corner radius. On focus, the border becomes solid ink with a matching 1px box-shadow ring. Error state uses the accent red ({colors.accent}) for the border and shadow.

**`select-input`** — Custom-styled select dropdown for filtering (by price, brand, size) and sorting. Matches the text-input dimensions but includes a 32px right padding for the dropdown arrow icon. The arrow is a custom SVG in {colors.muted}.

### Footer
**`footer`** — A dark, information-dense footer with a {colors.primary} background and white text. Organized into columns (Shop, Learn, Support, About) with heading titles in Figtree title-sm and links in footer-link typography. Link color is muted-soft on default, shifting to full white on hover. Padding is generous ({spacing.xxl}) to give the dense link list breathing room. Social media icons and payment method logos sit at the bottom in a lighter gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu (56px height). Product cards stack in single column. Category cards become full-width tiles. Footer columns stack vertically. Hero banner padding reduces to {spacing.xl}. Search bar moves to a dedicated overlay. |
| Tablet | 744–1128px | Nav-bar remains horizontal but some links collapse into a “More” dropdown. Product cards display in 2-column grid. Category cards in 3-column grid. Footer columns in 2x2 layout. |
| Desktop | 1128–1440px | Full nav-bar with all links visible. Product cards in 3- or 4-column grid. Category cards in 4-column grid. Footer in 4-column layout. Max content width capped at 1200px. |
| Wide | > 1440px | Same as desktop but with increased whitespace on sides. Max content width remains 1200px for readability. Background canvas color extends to edges. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile to meet WCAG touch target guidelines.
- Filter chips and pagination buttons are at least 32px tall with adequate padding.
- Product card tap targets (title, price, image) are the full card area — no small, isolated links.
- Nav-bar hamburger icon is 44x44px.

### Collapsing Strategy
- Top navigation links collapse into a hamburger menu on mobile (< 744px).
- Product filter sidebar collapses into a bottom sheet or overlay on mobile.
- Footer columns stack vertically on mobile, with accordion-style expand/collapse for each column heading.
- Hero banner text and CTA stack vertically on mobile; image may be cropped or hidden.
- Breadcrumb trail truncates on mobile, showing only the current page and parent category.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color palette is minimal (only two hex values from the live site: #dedede and #121212). The accent red (#c0392b), badge green (#27ae60), and star-rating yellow (#f1c40f) are inferred from common e-commerce patterns for this category — they may not match the live site exactly. A full design audit is needed to confirm.
- No extracted data for hover states, focus rings, error styling, or disabled states — these are constructed from common patterns and may not reflect the brand’s actual implementation.
- Font-family declarations found Figtree and Fraunces, but exact weights, letter-spacing, and line-height values are estimated based on typical usage. A full type scale audit is needed.
- No extracted data for dark mode, high-contrast mode, or reduced-motion preferences.
- Shopify platform detected, but checkout-specific colors (Shopify Pay button blue, Klarna pink, Afterpay black) were filtered out. The brand may have custom checkout styling not captured here.
- No data on iconography style, illustration approach, or photography treatment (product shots, lifestyle imagery).
- Spacing values are based on common e-commerce patterns and may not match the brand’s actual grid system.
- Rounded corner values are estimated from typical usage — the site may use different radii for specific components.
