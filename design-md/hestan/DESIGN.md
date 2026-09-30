---
version: alpha
name: "Hestan"
source_url: "https://hestanculinary.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Twelve appliance finishes hang on the showroom wall — Bora Bora turquoise, Matador red, Lush purple — yet the digital storefront commits to a single deep teal (#226d7a) that recalls the glassy enamel coating on a professional range door. That teal saturates every primary CTA, active nav indicator, and promotional badge, while a brighter cyan (#22b8d1) surfaces for hover states and interactive highlights, as if the color is warming under the cursor. The broader palette fans outward through progressively lighter washes: #b0e0e9 for soft informational surfaces, and an almost-white #e4f5fa that tints the canvas just enough to distinguish card backgrounds from the pure white (#ffffff) page. Typography runs entirely through Open Sans with Roboto and Arial as system fallbacks — a utilitarian stack that defers to the photography of brushed stainless steel and high-BTU burner rings rather than competing for attention. Display headlines land at 44px weight-700 for hero moments, but the system quickly steps down to 18px/600 for section titles and 16px/400 for body copy, creating a hierarchy that reads as confident restraint rather than typographic drama. Buttons follow a `{rounded.sm}` (8px) treatment with uppercase 14px labels and generous horizontal padding, giving CTAs a machined-metal precision that mirrors the product aesthetic. Product cards use the same `{rounded.sm}` corners with zero container padding, letting full-bleed imagery of ranges, cooktops, and outdoor grills fill the frame before a tight stack of title, price, and finish-swatch dots appears below. The navigation bar is a clean 72px white rail with a single-pixel teal underline on the active link — the kind of minimal chrome you would expect from a brand that builds appliances designed to be seen, not the interface selling them. Spacing is disciplined: `{spacing.section}` (64px) between major content blocks, `{spacing.lg}` (24px) between cards in a grid, and `{spacing.base}` (16px) as the atomic unit of internal padding. The overall effect is a cool, polished showroom — stainless surfaces, controlled lighting, and one unmistakable streak of color.

colors:
  primary: "#226d7a"
  primary-active: "#1e6d7a"
  primary-disabled: "#a3cdd4"
  accent: "#22b8d1"
  accent-active: "#1da3ba"
  accent-soft: "#b0e0e9"
  ink: "#1a1a1a"
  body: "#4a4a4a"
  muted: "#7a7a7a"
  muted-soft: "#b0b0b0"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-tint: "#e4f5fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#c4392a"
  success: "#2a7d4f"
  star-rating: "#d4930a"
  badge-new: "#22b8d1"
  badge-sale: "#c4392a"
  badge-finish: "#226d7a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price-lg:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
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
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.accent}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.10)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.price-lg}"
    color: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-finish-dots:
    height: 16px
    width: 16px
    rounded: "{rounded.full}"
    gap: "{spacing.xs}"
    padding: "0 {spacing.base} {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 560px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.35
  hero-cta:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 40px
    height: 52px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    aspectRatio: "1/1"
  category-tile-hover:
    backgroundColor: "{colors.surface-tint}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    color: "{colors.muted}"
  spec-table-value:
    typography: "{typography.spec-value}"
    color: "{colors.ink}"
  finish-swatch:
    height: 32px
    width: 32px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  finish-swatch-active:
    border: "2px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.canvas}, 0 0 0 4px {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-dark}"
    marginBottom: "{spacing.md}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-finish:
    backgroundColor: "{colors.badge-finish}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  btu-indicator:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.primary}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center

## Components

### Buttons
**`button-primary`** — The workhorse CTA, used for "Add to Cart", "Shop Now", and configurator submit actions. Deep teal (#226d7a) background with white uppercase text at `{typography.button-md}` (Open Sans 14px/600, 0.8px tracking). Corners are `{rounded.sm}` (8px), height is 48px with 14px 32px padding. On hover the background darkens to `{colors.primary-active}` (#1e6d7a); the disabled state lightens to `{colors.primary-disabled}` (#a3cdd4) with white text at reduced contrast.

**`button-secondary`** — Outlined variant for "Learn More", "View Specs", and comparison actions. White background with a 2px solid teal border and teal text. On hover the fill shifts to `{colors.surface-tint}` (#e4f5fa) and the border darkens, creating a subtle color-fill animation. Matches primary button dimensions.

**`button-tertiary`** — Text-only button for inline actions like "See All Finishes" or "Read Reviews". No background or border; just teal text with uppercase tracking. Padding is vertical-only (14px 0) so it aligns flush with surrounding body copy.

**`button-accent`** — A brighter variant using `{colors.accent}` (#22b8d1) for high-energy promotional CTAs such as "Build Your Range" or limited-time offers in hero banners. Same dimensions as primary but the lighter cyan reads as more inviting, less institutional.

### Navigation
**`nav-bar`** — A 72px white bar anchored to the top of the viewport with a single-pixel `{colors.hairline-soft}` (#e8e8e8) bottom border. The Hestan wordmark sits left; primary category links (Outdoor, Kitchen, Commercial, Cookware, Hestan Napa) run center in `{typography.nav-link}` (13px/600 uppercase, 0.8px tracking). The active link gets a 2px teal underline flush to the bar's bottom edge. Icon buttons for search, account, and cart cluster right at 40px diameter with `{rounded.full}` hit areas.

**`mega-menu`** — Drops below the nav-bar on hover with a 24px-padded white panel and a soft 8px/24px box shadow. Interior columns list product subcategories in `{typography.body-sm}` with featured product images at `{rounded.sm}` corners. The menu spans full viewport width on desktop.

### Product Cards
**`product-card`** — The core commerce component. White card, `{rounded.sm}` corners, no container padding. The product image fills the top at a 4:3 aspect ratio with top-radius corners only. Below the image: the product name in `{typography.title-sm}` (16px/600) with `{spacing.base}` horizontal padding, followed by the price in `{typography.price-lg}` (24px/700). A row of small finish-swatch dots (16px circles, `{rounded.full}`) sits at the bottom, showing available appliance colors as filled circles with a `{colors.hairline}` border. The active finish swatch gains a double-ring focus indicator using box-shadow.

### Hero
**`hero-banner`** — Full-bleed hero with a dark (#1a1a1a) fallback behind a large lifestyle photograph of a Hestan range in a professional kitchen. A 35% scrim overlay ensures text readability. Headline uses `{typography.display-xl}` (44px/700) in white; a subhead in `{typography.body-md}` (16px/400) sits below with `{spacing.md}` gap. The hero CTA uses the `hero-cta` component — a slightly taller (52px) accent-cyan button with wider padding (16px 40px) for prominence. Minimum height is 560px on desktop.

### Specification Table
**`spec-table-row`** — Used on product detail pages to display appliance specifications (BTU output, dimensions, fuel type, finish options). Each row is a two-column layout: the label in `{typography.spec-label}` (12px/600 uppercase, muted) on the left, the value in `{typography.spec-value}` (14px/400, ink) on the right. Rows are separated by a 1px `{colors.hairline-soft}` border. No zebra striping — the monochrome treatment keeps the focus on the data.

**`btu-indicator`** — A small inline badge used within spec tables and product cards to highlight BTU power ratings. Light teal background (`{colors.surface-tint}` #e4f5fa), teal text, `{rounded.sm}` corners, and `{typography.caption}` sizing. Communicates professional-grade performance at a glance.

### Finish Selector
**`finish-swatch`** — A 32px circle (`{rounded.full}`) representing one of Hestan's 12 appliance finishes. Each swatch is filled with the finish color and bordered by a 2px `{colors.hairline}` ring. The active swatch switches to a teal border with a double-ring box-shadow treatment (`0 0 0 2px white, 0 0 0 4px teal`), creating a clear selection indicator without relying on checkmarks.

### Category Tiles
**`category-tile`** — Square (1:1 aspect) tiles used on the homepage and category landing pages to link to product lines (Ranges, Cooktops, Outdoor Grills, Ventilation). Soft gray background (`{colors.surface-soft}` #f5f5f5) with `{typography.title-md}` (18px/600) label and `{rounded.sm}` corners. On hover the background tints to `{colors.surface-tint}` (#e4f5fa), revealing the brand teal subtly.

### Forms
**`text-input`** — Standard 48px input with `{rounded.sm}` corners and a 1px `{colors.hairline}` border. On focus, the border thickens to 2px teal. Error state uses 2px `{colors.error}` (#c4392a) instead. Used in dealer locator search, contact forms, and product registration.

**`search-bar`** — Pill-shaped (`{rounded.full}`) variant with a `{colors.surface-soft}` fill and `{colors.hairline}` border. On focus, the background flips to white and the border turns teal. The rounded shape signals exploratory intent, contrasting with the rectangular action buttons.

### Footer
**`footer`** — Dark ink (#1a1a1a) background spanning full width. Organized in four columns: brand info, product categories, customer support, and social/legal links. Column headings use `{typography.title-sm}` (16px/600) in white; links use `{typography.link}` (14px/500) in `{colors.muted-soft}` (#b0b0b0), brightening to white on hover. Vertical padding is `{spacing.xxl}` (48px).

### Badges
**`badge-new`** — Bright cyan (#22b8d1) pill with white uppercase text at `{typography.badge}` (10px/700). Positioned absolutely over product card images.

**`badge-sale`** — Red (#c4392a) variant for clearance and promotional pricing. Same dimensions and placement as badge-new.

**`badge-finish`** — Teal (#226d7a) badge used to label limited-edition or exclusive finish options on product cards.

### Accordion
**`accordion-header`** — Expandable section headers for product descriptions, FAQ pages, and mobile navigation. White background, `{typography.title-sm}`, `{spacing.base}` padding, separated by a 1px bottom border. A 40px icon button (chevron) sits right-aligned and rotates 180 degrees on open.

### Promotional Banner
**`promo-banner`** — A slim, full-width bar pinned above the nav-bar in `{colors.primary}` (#226d7a) with white `{typography.caption}` text, centered. Used for sitewide promotions, free-shipping thresholds, and event announcements. Padding is `{spacing.sm}` vertical and `{spacing.base}` horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger with slide-in drawer; product cards stack vertically at full width; hero headline drops to `{typography.display-md}` (28px); finish-swatch row scrolls horizontally; spec table goes full-width with stacked label/value; search bar fills nav as a sticky element; footer columns stack with accordion toggles. |
| Tablet | 744-1128px | Two-column product grid with `{spacing.lg}` gap; nav links remain visible but category count may truncate behind a "More" dropdown; hero headline uses `{typography.display-lg}` (36px); mega-menu shows two columns instead of four; footer switches to a two-column layout. |
| Desktop | 1128-1440px | Three-column product grid; full nav with all category links; hero at full `{typography.display-xl}` (44px); mega-menu at full four-column width; spec table in a two-column side panel alongside the product image; footer at four columns. |
| Wide | > 1440px | Max-width container (1440px) centered on canvas; hero image can extend full-bleed behind the container; product grid may expand to four columns; generous side margins emerge. |

### Touch Targets
- All buttons maintain a minimum 48px touch height on mobile.
- Icon buttons are 40px visible diameter with a 44px minimum touch area via padding.
- Finish swatches expand from 32px to 40px on mobile for easier selection.
- Accordion headers and nav drawer links have 48px minimum row height.
- Search bar input is 48px tall across all breakpoints.

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon at < 744px; the full nav slides in as a left-anchored drawer with stacked category links.
- Mega-menu disappears on mobile; its content moves into the nav drawer as nested accordion sections.
- Product filters collapse into a "Filter & Sort" button that opens a full-screen modal on mobile.
- Spec tables switch from side-by-side label/value layout to stacked single-column at < 744px.
- Footer columns stack vertically with each section collapsible via accordion.
- Hero CTA width goes to 100% on mobile, filling the container.
- Finish-swatch rows switch from wrapping to horizontal scroll with fade-edge indicators.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The primary site (hestan.com) returned a 403 Forbidden during extraction; the hex colors (#226d7a, #b0e0e9, #1e6d7a, #e4f5fa, #22b8d1) may represent a restricted-access page's partial rendering rather than the full production palette.
- Font families extracted (Arial, Open Sans, Roboto) are generic sans-serif stacks; the production site likely loads a custom or licensed typeface via JavaScript that was blocked by the 403. Open Sans is used here as the most designed option in the extracted stack.
- No custom web font (e.g., a proprietary Hestan display face) could be confirmed; display typography weights and sizes are estimated from comparable premium appliance brand patterns.
- Hover transition timings (duration, easing) were not extractable; a 200ms ease-in-out is assumed for all interactive states.
- Dark mode tokens are undefined; the site appears to operate in light mode only.
- Focus-visible ring styles (outline offset, color) could not be confirmed; a 2px teal outline at 2px offset is recommended for accessibility.
- Loading states (skeleton screens, spinners) were not observed in the extracted data.
- Mega-menu animation specifics (slide vs. fade, duration) were not captured.
- Cart drawer / side panel styling (width, overlay opacity, animation) was not extractable.
- Sub-brand palettes for Hestan Outdoor, Hestan Commercial, and Hestan Vineyards may diverge from the teal palette documented here but could not be separately extracted.
- The 12 appliance finish hex values (Steeletto, Citra, Matador, Grove, Stealth, Froth, Lush, Tin Roof, Bora Bora, Pacific Fog, Prince, Sol) were not extractable from CSS; swatch colors would need to be sourced from product imagery or a brand asset guide.
