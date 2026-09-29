---
version: alpha
name: "Cuisinart"
source_url: "https://www.cuisinart.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  That unmistakable cyan — #00a1e0, the color of a gas flame's hottest ring — anchors every primary CTA, navigation highlight, and interactive element on cuisinart.com, a hue no other countertop-appliance brand owns. It reads less like a corporate blue and more like the glow of a backlit control panel, a signal that this is a site built to move you toward a purchase decision with industrial efficiency. The typography is pure system-native stack — Helvetica Neue, Roboto, Arial, Noto Sans — rendered at moderate weights that let the product photography do the heavy lifting. Headlines sit at 600–700 weight in the 28–36px range, but the real workhorse is the 16px body text in #444444 on a bright #f9f9f9 canvas, a combination that reads cleanly without the stark contrast of pure black on white. Green accents (#008827, #00853e) appear throughout category badges and eco-messaging callouts, while a persistent #cc0000 red marks sale pricing, clearance tags, and error states — the three-color system (cyan, green, red) maps directly to the informational hierarchy of a kitchen-appliance catalog. Corner radii are modest: `{rounded.sm}` on buttons, `{rounded.md}` on cards, `{rounded.xs}` on badges — nothing pill-shaped, nothing playful, just enough softness to keep the interface from feeling like a spec sheet. The navigation architecture is deep, with a full-width mega-menu system that exposes product categories (Food Prep, Cookware, Coffee & Espresso, Microwaves, Toaster Ovens) in organized columns, each with lifestyle imagery and promotional callouts. A persistent top utility bar in #1a1816 carries account links and customer service, sitting above the main nav like the control strip on a range hood. Spacing follows a disciplined `{spacing.base}` of 16px grid, with `{spacing.section}` at 64px separating major content blocks. Product cards use generous `{spacing.lg}` gutters and present a clean image-over-text layout with star ratings, model numbers, and price prominently stacked. The overall effect is a digital showroom — polished, navigable, and engineered to convert browsers into buyers with the same precision Cuisinart brings to its blade assemblies.

colors:
  primary: "#00a1e0"
  primary-active: "#007cad"
  primary-disabled: "#abdde5"
  primary-dark: "#005474"
  accent-green: "#008827"
  accent-green-dark: "#00853e"
  accent-green-deep: "#005518"
  sale-red: "#cc0000"
  sale-red-dark: "#990000"
  sale-red-deep: "#6a0000"
  ink: "#1a1816"
  ink-alt: "#1d2124"
  body: "#444444"
  muted: "#545b62"
  muted-soft: "#818182"
  hairline: "#c8cbcf"
  hairline-soft: "#dae0e5"
  border-strong: "#b9bbbe"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  surface-cool: "#ececf6"
  surface-warm: "#ffe8a1"
  surface-highlight: "#94e1ff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  dark-forest: "#233c28"
  teal-info: "#0c5460"
  teal-info-active: "#117a8b"
  alert-gold: "#d39e00"
  alert-gold-dark: "#856404"
  utility-bar: "#1b1e21"
  utility-bar-text: "#383d41"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  link:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  nav-utility:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  spec-value:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  price-current:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, Roboto, 'Noto Sans', 'Liberation Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through
  model-number:
    fontFamily: "'Consolas', 'Courier New', 'Liberation Mono', Monaco, Menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.5px

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
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: 1px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: 1px solid "{colors.primary-active}"
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-sale-active:
    backgroundColor: "{colors.sale-red-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.sale-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline-soft}"
  utility-bar:
    backgroundColor: "{colors.utility-bar}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-utility}"
    height: 36px
    padding: 0 "{spacing.lg}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
    borderBottom: 1px solid "{colors.hairline-soft}"
    boxShadow: 0 4px 12px rgba(0,0,0,0.08)
  mega-menu-heading:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: 0 0 "{spacing.sm}" 0
    borderBottom: 2px solid "{colors.primary}"
  mega-menu-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  mega-menu-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-model:
    typography: "{typography.model-number}"
    textColor: "{colors.muted}"
    padding: "0 {spacing.base}"
  product-card-price:
    typography: "{typography.price-current}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price-sale:
    typography: "{typography.price-current}"
    textColor: "{colors.sale-red}"
  product-card-price-compare:
    typography: "{typography.price-compare}"
    textColor: "{colors.muted}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.alert-gold}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-card-badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 52px
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  category-card-image:
    rounded: "{rounded.sm}"
  category-card-label:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} 0 0"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
  promo-banner-alt:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
  info-alert:
    backgroundColor: "#d1ecf1"
    textColor: "{colors.teal-info}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: 1px solid "{colors.teal-info-active}"
  warning-alert:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.alert-gold-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  error-alert:
    backgroundColor: "#f8d7da"
    textColor: "{colors.sale-red-deep}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px 12px 40px
    height: 44px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 1px solid "{colors.primary}"
  search-suggestion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: 1px solid "{colors.hairline-soft}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: 1px solid "{colors.hairline-soft}"
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.ink}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.body}"
  star-rating:
    textColor: "{colors.alert-gold}"
    typography: "{typography.caption}"
  star-rating-empty:
    textColor: "{colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.dark-forest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    padding: "0 0 {spacing.sm} 0"
  footer-link:
    textColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  footer-bottom:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.base} {spacing.lg}"
  newsletter-signup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.xl} {spacing.lg}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs} 0 0 {rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "0 {rounded.xs} {rounded.xs} 0"
    padding: 12px 24px
    height: 48px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderBottom: 1px solid "{colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: 1px solid "{colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    width: 44px
    height: 44px

## Components

### Buttons
**`button-primary`** — A solid rectangle filled with `{colors.primary}` (#00a1e0) carrying white text at `{typography.button-md}` — 16px semibold with 0.3px letter spacing. Corners are softened to `{rounded.sm}` (8px). On hover/active, the background deepens to `{colors.primary-active}` (#007cad), a darker teal that reads as a natural pressed state. The disabled variant uses `{colors.primary-disabled}` (#abdde5), a washed-out sky blue that maintains the hue family while clearly signaling non-interactivity. No shadows, no gradients — the flat fill and sharp type do all the communicating.

**`button-secondary`** — An outlined counterpart to the primary button, using a white fill with a 1px solid border in `{colors.primary}`. Text is set in the same `{typography.button-md}` but colored `{colors.primary}`. On hover, the background shifts to `{colors.surface-soft}` (#f9f9f9) and the border darkens to `{colors.primary-active}`. Used for secondary actions like "Compare" or "Add to Registry" where the full weight of the cyan fill would create visual competition with the primary CTA.

**`button-sale`** — A variant reserved for sale and clearance contexts, filled with `{colors.sale-red}` (#cc0000) and white text. On active state, it deepens to `{colors.sale-red-dark}` (#990000). This button appears on promotional banners and clearance product pages where the urgency signal overrides the brand's usual cyan palette.

**`button-ghost`** — A borderless, background-free text button using `{typography.button-sm}` in `{colors.primary}`. Used for tertiary actions like "View All", "Learn More", or inline navigation within content blocks. The smaller 14px size and absence of a container keep it subordinate to the primary and secondary buttons.

### Text Inputs
**`text-input`** — A standard input field with a 1px border in `{colors.hairline}` (#c8cbcf), `{rounded.xs}` (4px) corner radius, and 48px height. Text uses `{typography.body-md}` at 16px. Placeholder text is `{colors.muted-soft}` (#818182). On focus, the border transitions to `{colors.primary}` (#00a1e0), providing a clear cyan highlight. Error state replaces the border with `{colors.sale-red}` (#cc0000). Select inputs mirror this treatment but include a dropdown chevron in `{colors.muted}`.

### Navigation
**`utility-bar`** — A slim 36px bar pinned to the very top of the viewport, rendered in `{colors.utility-bar}` (#1b1e21) — a near-black that reads as gunmetal. It carries account links, customer service, and location/language selectors in `{typography.nav-utility}` (12px regular, white text). This bar establishes the dark upper boundary of the page and provides a visual anchor for the entire header stack.

**`nav-bar`** — The primary navigation bar sits directly below the utility bar at 64px height on a white background with a 1px bottom border in `{colors.hairline-soft}` (#dae0e5). Links use `{typography.nav-link}` at 15px medium weight. The Cuisinart logo occupies the left, with category navigation centered or left-aligned and utility icons (search, cart, account) on the right. Active and hover states highlight links in `{colors.primary}`.

**`mega-menu`** — A full-width dropdown panel that opens on category hover, displaying product subcategories in organized columns. Each column is headed by a `{typography.title-md}` label with a 2px bottom border in `{colors.primary}`, giving the menu a tabbed-catalog feel. Links use `{typography.body-sm}` in `{colors.body}`, shifting to `{colors.primary}` on hover. A lifestyle image or promotional callout typically occupies the rightmost column. The panel casts a soft 0 4px 12px rgba(0,0,0,0.08) shadow beneath it.

### Product Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners containing a product image over stacked text details. The image area sits on a `{colors.surface-soft}` (#f9f9f9) background for consistent tone even before the image loads. Below the image, the product name appears in `{typography.title-sm}` (14px semibold), followed by the model number in `{typography.model-number}` — a monospaced font at 12px in `{colors.muted}`, which gives the model identifiers (e.g., "TOB-260N1") the mechanical precision they deserve. The current price is rendered in `{typography.price-current}` (20px bold). When a product is on sale, the sale price switches to `{colors.sale-red}` and the original price appears in `{typography.price-compare}` with a line-through. Star ratings sit at the bottom in `{colors.alert-gold}` (#d39e00). Sale badges use a `{colors.sale-red}` background; "New" badges use `{colors.accent-green}`.

### Hero Banner
**`hero-banner`** — A full-width section on `{colors.surface-soft}` carrying a large lifestyle or product image alongside headline text in `{typography.display-xl}` (36px bold with tight letter-spacing). The subtitle uses `{typography.body-md}` in `{colors.body}`. A prominent CTA button sits below, sized slightly larger than the standard primary button at 52px height with extra horizontal padding. The section is padded with `{spacing.section}` (64px) top and bottom. Hero banners often feature seasonal promotions, new product launches, or curated collections, and may rotate in a carousel.

### Category Cards
**`category-card`** — A rounded rectangle (`{rounded.md}`) containing a category image and label, used in grid layouts on the homepage and landing pages. The image uses `{rounded.sm}` corners. Below, the category name is set in `{typography.title-md}` (16px semibold). These cards serve as the primary wayfinding mechanism for the product catalog, with categories like "Food Processors", "Coffee Makers", "Toaster Ovens" each getting their own card with representative product imagery.

### Promotional Banners
**`promo-banner`** — A slim 40px banner typically placed above the hero or below the utility bar, filled with `{colors.primary}` and white text in `{typography.body-md}`. Used for sitewide promotions like free shipping thresholds or seasonal sales. The alternate variant `promo-banner-alt` uses `{colors.surface-warm}` (#ffe8a1), a warm yellow, with `{colors.ink}` text for less urgent promotions.

### Alerts
**`info-alert`** — A teal-tinted alert box for informational messages (shipping updates, stock notices), using a light blue background with `{colors.teal-info}` (#0c5460) text and a matching border. **`warning-alert`** uses the warm yellow `{colors.surface-warm}` with `{colors.alert-gold-dark}` (#856404) text. **`error-alert`** uses a light red background with `{colors.sale-red-deep}` (#6a0000) text. All three share `{rounded.xs}` corners and `{spacing.base}` padding.

### Spec Table
**`spec-table-row`** — An alternating-row table used on product detail pages to present technical specifications (wattage, capacity, dimensions, weight). Labels use `{typography.spec-label}` (13px semibold) and values use `{typography.spec-value}` (13px regular) in `{colors.body}`. Rows alternate between white and `{colors.surface-soft}`. This is a core component for an appliance site — buyers cross-reference specs constantly, so the table needs to be scannable with clear label/value separation.

### Search
**`search-bar`** — A border-defined input with `{rounded.sm}` corners and a left-side magnifying glass icon, providing 40px of left padding to clear the icon. The input uses `{typography.body-md}` at 16px. On focus, the border transitions to `{colors.primary}`. Search suggestions appear in a dropdown below, each suggestion using `{typography.body-sm}` with `{spacing.sm}` vertical padding and a `{colors.hairline-soft}` bottom border.

### Footer
**`footer`** — A full-width section on `{colors.dark-forest}` (#233c28), a deep green-black that sets Cuisinart apart from the typical charcoal or pure-black footer. Text is white (`{colors.on-dark}`). Section headings use `{typography.title-sm}`, and links use `{typography.body-sm}` in `{colors.hairline}` (#c8cbcf), brightening to white on hover. The footer bottom strip sits on `{colors.ink}` (#1a1816) with copyright and legal links in `{typography.caption}`. Padding is `{spacing.section}` top and bottom.

### Newsletter Signup
**`newsletter-signup`** — A horizontal form composed of a text input and a submit button joined at their edges. The input uses `{rounded.xs}` on the left corners only; the submit button uses `{rounded.xs}` on the right corners only, creating a unified control. The submit button is filled with `{colors.primary}` and matches the input's 48px height. Typically sits within the footer or a dedicated mid-page callout section.

### Accordion
**`accordion`** — Vertically stacked expandable sections using `{typography.title-md}` for headers and `{typography.body-sm}` in `{colors.body}` for content. Each section has a bottom border in `{colors.hairline-soft}`. A chevron or plus/minus icon indicates expand/collapse state. Used extensively on product detail pages for descriptions, specifications, reviews, and Q&A sections.

### Breadcrumbs
**`breadcrumb`** — A horizontal trail in `{typography.caption}` (12px) using `{colors.muted}` for ancestor links and `{colors.ink}` for the current page. Separators use `{colors.hairline}`. Placed at the top of product detail and category pages to expose the navigation hierarchy. No background or container — just inline text with `{spacing.xs}` gaps.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; utility bar may hide or collapse to icons only; nav-bar collapses to hamburger menu with slide-out drawer; mega-menu becomes accordion-style category navigation; product cards stack full-width; hero banner uses stacked image-over-text; spec table scrolls horizontally or restructures to label-above-value; footer columns stack vertically; search bar becomes full-width |
| Tablet | 744-1128px | Two-column product grid; nav-bar shows abbreviated category links with hamburger for overflow; mega-menu remains functional but with fewer columns; hero banner maintains side-by-side layout at reduced proportions; category cards display in a 2x2 or 3-across grid; footer shows 2-3 columns |
| Desktop | 1128-1440px | Three-to-four column product grid; full nav-bar with all category links visible; mega-menu at full width with lifestyle imagery; hero banner at full proportions with generous `{spacing.section}` padding; spec table spans comfortable width; footer shows 4 columns; search bar has fixed width in nav-bar |
| Wide | > 1440px | Maximum content width of 1440px centered on canvas; product grid may extend to 4-5 columns; hero banner and promotional areas maintain maximum width; all components hold desktop proportions within the centered container |

### Touch Targets
- All buttons maintain 48px minimum height on mobile and tablet
- Navigation hamburger icon and quantity selector buttons are 44x44px
- Product cards are full-card tap targets on mobile
- Accordion headers are minimum 48px tall for comfortable tapping
- Footer links have 44px vertical spacing on mobile for easy tapping

### Collapsing Strategy
- Utility bar condenses to essential icons at 744px; primary nav collapses to hamburger drawer
- Mega-menu transforms to nested accordion within the mobile drawer
- Product grid drops from 4 to 3 columns at 1128px, to 2 at 744px, to 1 at 480px
- Hero banner and category cards switch from multi-column to stacked layout at 744px
- Spec table switches to stacked label/value pairs below 744px; footer from 4 to 2 columns at 744px, then stacked at 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font was detected; Cuisinart may load proprietary typefaces via JavaScript or a deferred stylesheet
- Hover transition timing and easing curves for buttons, links, and mega-menu could not be extracted
- Box-shadow values for the mega-menu and dropdown components are estimated; production values may differ
- Carousel/slider behavior (auto-advance timing, swipe gestures, indicator dots) on hero banners could not be captured
- Focus ring styles for keyboard/accessibility navigation are not documented; a 2px solid outline in `{colors.primary}` with 2px offset is recommended
- Loading states (skeleton screens, spinner animations) are not defined
- Breakpoint values may differ from the standard 744/1128/1440 used here; the site may use Bootstrap-derived breakpoints
- Cart drawer/flyout panel specifications (overlay opacity, slide animation, z-index) could not be extracted
- The green accent colors (#008827, #00853e, #005518) appear in multiple contexts but their exact usage rules could not be fully mapped
- The warm yellow (#ffe8a1) and lavender (#ececf6) surface colors appear in the extraction but their exact component contexts could not be verified
