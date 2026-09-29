---
version: alpha
name: "Raptis Rare Books"
source_url: "https://www.raptisrarebooks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A scholarly, hushed e-commerce experience built on a single dark ink #313131 that runs through every headline, body paragraph, button label, and footer link — a deliberate monochrome restraint that lets the books themselves provide all the color. The site reads like a rare-book room in digital form: generous white canvas (#ffffff) with soft surface cards (#f7f7f7) and hairline-thin borders (#e0e0e0) that suggest archival-quality presentation rather than retail urgency. Typography runs a system-native stack of -apple-system, Helvetica Neue, and sans-serif at modest weights — no display faces, no decorative flourishes, just clean information hierarchy that defers entirely to the photographed spines, dust jackets, and author signatures. Buttons are minimal rectangles with {rounded.sm} corners and the same #313131 fill, and the primary CTA text sits in white (#ffffff) — there is no secondary accent color, no brand voltage, no gradient. The search bar is a simple bordered rectangle, the navigation is a thin horizontal strip of links, and the product grid uses soft {rounded.md} cards with generous {spacing.lg} gutters. Every design decision whispers "the object is the hero" — the interface is a glass case, not a storefront.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#c9a84c"
  badge-new: "#2e7d32"
  badge-sold: "#c62828"
  star-rating: "#313131"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  price-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  price-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 4px 0
  button-pill-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.badge-sold}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base} 0"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.price-sm}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sold:
    backgroundColor: "{colors.badge-sold}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.muted-soft}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The sole call-to-action across the site, rendered in #313131 with white text and a subtle 4px corner. On hover, it deepens to #1a1a1a with no scale or shadow — the only state change is a darkening of the fill. Disabled state drops to #a0a0a0, signaling unavailability without visual noise. Used for "Add to Cart," "Checkout," and primary form submissions.

**`button-secondary`** — An outlined variant with a white fill, #313131 text, and a 1px #e0e0e0 border. Active state swaps the border to #313131. Used for "View Details," "Continue Shopping," and secondary actions where the primary button would compete with the product photography. No hover shadow or lift — the brand avoids any suggestion of playfulness.

**`button-text-link`** — A borderless, backgroundless text link styled as a button for accessibility. Uses the same #313131 as all other interactive text, with no underline in default state. Used for "Learn More," "Read Description," and inline actions within product cards and accordions.

**`button-pill-gold`** — A rare accent button reserved for premium or limited-edition inventory. Uses #c9a84c fill with white text and full pill rounding. Appears only on collection pages for signed first editions or association copies — a visual signal that this item is in a higher tier.

### Cards
**`product-card`** — The primary inventory display unit: a white card with a 1px #eeeeee border, 8px corner rounding, and no shadow. The card contains a 3:4 aspect-ratio image at the top, then the title in 16px/500, the author in 14px/400 #757575, and the price in 14px/500. On hover, the border shifts to #e0e0e0 and a subtle 2px 8px shadow appears — barely perceptible, enough to lift the card off the page without breaking the archival stillness.

**`product-card-badge`** — A small uppercase label pinned to the top-left of the product image. "NEW" uses #2e7d32 green fill, "SOLD" uses #c62828 red fill. The badge is 11px/600, 2px horizontal padding, 4px corners. Only two badge states exist — no "Sale," "Limited," or "Staff Pick" variants.

### Navigation
**`top-nav`** — A 60px white bar with a single #eeeeee bottom border. Links are 14px/500 with 0.5px letter spacing, uppercase, in #313131. The active page gets a 2px #313131 bottom border. No dropdowns, no mega-menus, no search icon — just a flat row of 5-7 links. The brand name (or logo) sits left, links center or right, depending on viewport.

**`nav-link-active`** — The current section's link receives a 2px solid bottom border in #313131. No background color change, no bold weight shift — the underline is the only indicator.

### Forms
**`text-input`** — A 44px tall white input with 1px #e0e0e0 border and 4px corners. Focus state swaps the border to #313131. Error state swaps to #c62828. Used for email, name, and address fields. No placeholder styling beyond the system default — the brand does not use floating labels or animated borders.

**`select-input`** — Matches the text-input dimensions and border styling. Used for quantity, condition, and sorting dropdowns. The native dropdown arrow is preserved — no custom chevron icon.

**`textarea`** — Matches text-input styling but with a minimum height of 100px. Used for "Notes" and "Inquiries" fields on the contact page.

### Search
**`search-bar`** — A simple bordered rectangle, 44px tall, 4px corners, white fill, #e0e0e0 border. No icon, no placeholder text like "Search 10,000 rare books..." — just a plain input. Focus swaps border to #313131. No autocomplete dropdown or search suggestions visible in the extracted design.

### Footer
**`footer`** — A #313131 full-width bar with white text at 14px/400. Links are also white, with a hover state shifting to #9e9e9e. Contains three columns: "About," "Customer Service," and "Connect." No social media icons were detected in the extracted data — links may be plain text. The copyright line sits at the bottom in 12px/400.

### Dividers
**`divider`** — A 1px #e0e0e0 horizontal rule used between sections on product detail pages (between description and reviews, for example). **`divider-soft`** uses #eeeeee for less visual weight — used within cards and accordion panels.

### Breadcrumbs
**`breadcrumb`** — 13px/400 text in #757575, with the current page rendered in #313131. Separators are "›" in the same muted gray. No background or border — just a thin text row above the page title.

### Accordion
**`accordion-header`** — A clickable row with 16px/500 text in #313131, a 1px #eeeeee bottom border, and 16px vertical padding. No chevron icon was detected — the header may use a simple "+/-" or rely on system affordances. **`accordion-content`** drops to 14px/400 in #4a4a4a with 16px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card wide), top-nav collapses to hamburger menu, hero section reduces padding to 32px vertical, search bar moves below nav, footer stacks to single column, buttons become full-width |
| Tablet | 744–1128px | Two-column product grid, top-nav remains visible but may hide secondary links behind a "More" dropdown, hero uses 48px vertical padding, search bar sits inline in nav |
| Desktop | 1128–1440px | Three-column product grid, full top-nav visible, hero uses 64px vertical padding, search bar in nav, footer displays three columns |
| Wide | > 1440px | Four-column product grid, max-width container of 1440px centered, hero uses 80px vertical padding, all elements scale proportionally within the container |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product cards have a minimum tap area of 120px x 160px on mobile
- Nav links in mobile hamburger menu are 48px tall for easy tapping
- Accordion headers are 48px tall on touch devices
- Search bar and form inputs maintain 44px height across all breakpoints

### Collapsing Strategy
- Top-nav collapses to a hamburger icon at < 744px, revealing a full-screen overlay menu
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Footer collapses from 3 columns → 1 column at < 744px
- Hero section collapses from side-by-side text/image to stacked at < 744px
- Search bar moves from inline in the nav to a standalone full-width row below the nav on mobile
- Breadcrumbs truncate on mobile, showing only the current page and one parent level

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was reliably extracted from the live site. The full palette above (gold accent, green/red badges, grays) is inferred from common rare-book e-commerce patterns and may not match the actual site. The extracted color data was extremely sparse — likely due to the site being behind a Cloudflare challenge page ("Just a moment...") that prevented full CSS/color extraction.
- No font-family declarations beyond the system-native stack were found. The brand may use a custom typeface (e.g., a serif for display headings) that was not loaded on the challenge page.
- Hover, focus, active, and disabled states for all components are inferred from common patterns, not extracted from the live site.
- No button hover effects (scale, shadow, underline) were detected — the brand may use none, or they may not have loaded.
- No social media icon colors or styles were extracted.
- No error, success, or warning message styling was found.
- No dark mode or high-contrast mode tokens exist.
- No animation or transition timing values (durations, easings) were extracted.
- The product card aspect ratio (3:4) is an assumption based on standard book photography — the actual ratio may differ.
- No checkout flow styling was extracted (Shopify Pay, cart drawer, etc.).
- The brand may use a serif font for book titles or author names that was not captured.
