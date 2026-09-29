---
version: alpha
name: "Camp Chef"
source_url: "https://www.campchef.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  That deep ember-red #b72c27 sitting in Camp Chef's header hits like the glow under a pellet hopper at two hundred degrees — not fire-engine bright but brick-kiln warm, a red that has absorbed heat rather than displaying it. It anchors every primary CTA, promotional banner, and navigation accent across a site that otherwise runs on stark dark-on-white contrast built for scanning BTU ratings and comparing griddle dimensions: #1a1617 ink, #232323 body text, and a functional gray ramp (#8d8d8d, #626262, #d2d2d2) that separates content tiers without introducing personality. Typography splits duties between two distinct voices. Saira, a geometric semi-condensed family, stamps display headings and button labels at weight 600–700 with an industrial-catalog energy — its squared-off counters and narrow letterforms suit a brand selling 36-inch flat-top griddles and commercial-grade pellet smokers. Instrument Sans handles body copy and product descriptions at weight 400–500, clean and readable at paragraph lengths without competing with hardware photography. Consolas surfaces in spec tables and model-number callouts, reinforcing an engineering-manual posture with monospaced precision. Corner radii stay tight: `{rounded.xs}` (4px) on buttons and inputs, `{rounded.sm}` (8px) on product cards — no pill shapes, no soft lifestyle circles. The grid is utilitarian, with `{spacing.lg}` gaps between card rows and `{spacing.section}` between content blocks, giving large product photography room to breathe. Sale prices punch in #d20000 against struck-through originals in `{colors.muted}`, while stock indicators use #1f873d — functional green, never decorative. The navigation sits on a near-black `{colors.nav-bg}` ground with white logotype and a `{colors.primary}`-tinted search icon, reading more like an equipment dashboard than a lifestyle storefront. A faint warm tint on `{colors.surface-warm}` (#fff8f8) touches certain promo sections, the only softness in a palette built for people who already know which smoker they want and need the specs to confirm it.

colors:
  primary: "#b72c27"
  primary-active: "#8d221e"
  primary-disabled: "#e6b3b0"
  ink: "#1a1617"
  body: "#232323"
  muted: "#626262"
  muted-soft: "#8d8d8d"
  hairline: "#d2d2d2"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-warm: "#fff8f8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale: "#d20000"
  sale-dark: "#ab0600"
  success: "#1f873d"
  success-dark: "#00730b"
  info-link: "#0774d7"
  nav-bg: "#1a1617"
  badge-new: "#0774d7"
  star-rating: "#b72c27"
  accent-charcoal: "#1d1d1d"
  accent-warm-gray: "#5f5054"
  scrim: "#1a1617"

typography:
  display-xl:
    fontFamily: "'Saira', 'Arial Narrow', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "'Saira', 'Arial Narrow', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Saira', 'Arial Narrow', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Saira', 'Arial Narrow', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Saira', 'Arial Narrow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Saira', 'Arial Narrow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Saira', 'Arial Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Saira', 'Arial Narrow', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  promo-label:
    fontFamily: "'Saira', 'Arial Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-mono:
    fontFamily: "Consolas, 'SF Mono', 'Fira Code', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 52px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.sale}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted-soft}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: 1 / 1
  product-card-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 36px
    height: 52px
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.promo-label}"
    height: 40px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-mono}"
    borderColor: "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — The main conversion driver, used for "Add to Cart", "Shop Now", and checkout CTAs. Rendered as a solid #b72c27 rectangle with white uppercase text in Saira 600, it uses tight 4px corners and generous horizontal padding to create a wide, confident click target. On hover, the background darkens to #8d221e; on press, it deepens further. The disabled state fades to a muted pink-gray (#e6b3b0), signaling unavailability without breaking the layout.

**`button-secondary`** — A white-fill button with dark ink text and a 1px hairline border, used for secondary actions like "View Details", "Compare", or "Learn More". It shares the same uppercase Saira treatment and 4px radius as the primary button but deliberately recedes against the canvas, creating clear visual hierarchy on pages where multiple actions compete.

**`button-ghost`** — A borderless, transparent button with text rendered in the primary red. Used for tertiary actions like "Cancel", "Clear Filters", or inline text links that need button-level hit targets. On hover, an underline appears to confirm interactivity.

**`button-add-to-cart`** — A taller variant (52px) of the primary button, given extra vertical presence on product detail pages where it sits below spec tables and configuration selectors. The increased height and wider padding (14px 32px) ensure the CTA dominates the purchase decision zone.

### Cards
**`product-card`** — The workhorse content container for category and collection pages. A white surface with 8px corners frames a square-aspect product photo at top, a Saira title-sm product name, Instrument Sans body-sm for the short description, and a price block where the original price strikes through in muted gray and the sale price renders in #d20000 at Saira weight 700. Badges overlay the top-left of the image for "Sale" or "New" flags. The card casts no shadow — separation comes from the canvas background and hairline borders on hover.

**`category-card`** — A clickable tile used on the homepage and navigation landing pages to route users into product categories (Pellet Grills, Flat Top Griddles, Pizza Ovens, Camp Stoves). It uses a soft #f4f4f4 fill, 8px radius, and a centered category image with a Saira title-sm label below. On hover, a subtle border in the primary red appears.

### Navigation
**`nav-bar`** — A fixed 72px header bar on a near-black (#1a1617) ground. The Camp Chef logotype sits left in white, category links run center in Instrument Sans uppercase at 14px weight 600, and utility icons (search, account, cart) align right. The dark bar creates a strong dashboard-like horizon line that separates brand chrome from product content below.

**`mega-menu`** — A dropdown panel that opens below the nav on category hover, rendered on a white canvas with 8px rounded corners and a subtle drop shadow. Content is organized in columns: product sub-categories on the left in title-sm, featured products with thumbnail images center, and promotional callouts (new arrivals, seasonal deals) on the right. The panel spans the full nav width on desktop.

**`nav-link-active`** — The currently active category link in the nav bar, distinguished by a bottom border in the primary red and text shifted from muted-soft to the same red. The underline is 2px thick, inset by 4px from the link edges.

### Forms
**`text-input`** — A standard form field with white fill, 1px hairline border, and 4px corner radius. Body text renders in Instrument Sans at 16px. On focus, the border transitions to the primary red (#b72c27) with no box-shadow — a single-signal focus indicator consistent with the utilitarian posture. Error states swap the border to #d20000 with a caption-size error message below in the same red.

**`search-bar`** — A text input variant at 44px height, placed inside the nav bar or mobile menu. It uses the same 4px radius and hairline border as text-input but adds a search icon (magnifying glass in primary red) aligned right. Placeholder text reads in muted gray.

### Promotional
**`promo-strip`** — A full-width 40px banner pinned above the nav bar, using the primary red background with white uppercase text in Saira 700 at 14px. It announces site-wide promotions, free shipping thresholds, or seasonal sales. The strip scrolls away on mobile or can be dismissed with an "X" icon.

**`hero-section`** — A full-bleed hero module with a dark ink (#1a1617) background or a full-width lifestyle photograph of outdoor cooking scenes overlaid with a dark scrim for text legibility. The headline renders in display-xl Saira (48px, weight 700), the subhead in body-md Instrument Sans, and the CTA in the hero-cta button variant. On mobile, content stacks vertically with the headline scaling down to display-sm.

### Footer
**`footer-section`** — A full-width footer on the same near-black (#1a1617) as the nav bar, creating a visual bookend. Content is organized in four to five columns: product categories, support links, company info, social icons, and a newsletter signup form. Column headings render in title-sm Saira in white; link text uses Instrument Sans body-sm in muted-soft gray (#8d8d8d), brightening to white on hover.

### Badges
**`badge-sale`** — A compact uppercase label in Saira 11px weight 700, white text on a #d20000 background with 4px corners. It overlays product card images in the top-left corner to flag clearance, percentage-off, or seasonal sale items. Padding is tight (3px 8px) to keep the badge subordinate to the product image.

**`badge-new`** — Same dimensions and typography as badge-sale, but with a blue (#0774d7) background to differentiate new arrivals from price promotions. The blue is functional — it separates informational flags from urgency-driven sale flags without adding a third brand hue.

### Spec Table
**`spec-table`** — A striped or bordered table used on product detail pages to present technical specifications (BTU output, cooking surface area, hopper capacity, weight, dimensions). Data renders in Consolas monospace at 14px for precise alignment of numeric values. Row headers are in Saira title-sm weight 600, values in the monospace stack. Alternating rows use surface-soft (#f4f4f4) and white for scanability.

### Star Rating
**`star-rating`** — Product ratings rendered as filled/empty star icons at 16px in the primary red (#b72c27). The rating count appears beside the stars in caption-size Instrument Sans. Used on product cards and product detail pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with slide-in drawer; hero headline scales to display-sm (24px); promo-strip text truncates or scrolls; buttons expand to full-width; mega-menu becomes accordion navigation; search bar moves into mobile menu |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses display-md (32px); category cards shift to 2×2 grid; footer stacks into two rows; mega-menu opens as a simplified dropdown |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with mega-menu on hover; hero uses display-xl (48px); multi-column footer; sticky nav with scroll-triggered shadow; spec tables display at full width |
| Wide | > 1440px | Max-width container at 1440px centered; extra whitespace on margins; hero imagery expands to fill; four-column product grid standard; footer columns spread with additional spacing |

### Touch Targets
- All interactive elements (buttons, links, inputs) meet a minimum 44x44px touch target per Apple HIG guidelines.
- Icon buttons in the nav bar (search, cart, account) maintain 44px hit areas even when the icon is 24px.
- Product card tap areas cover the full card surface, not just the title text.
- Accordion headers on mobile are 48px tall for reliable tapping.
- Mega-menu links on tablet have 40px vertical spacing between items.

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon below 744px, triggering a full-height slide-in drawer from the left with accordion-style category expansion.
- Product filters collapse into a "Filter & Sort" button that opens a bottom-sheet modal on mobile with checkbox-style filter groups.
- Multi-column footer stacks into a single column with collapsible sections — each column heading becomes an accordion trigger.
- Hero content stacks vertically on mobile: image fills the top, text content and CTA sit below with full-width button.
- Spec tables on product detail pages scroll horizontally on mobile with a fade-out edge indicator, or collapse into a vertical key-value list.
- Promo strip either truncates with an ellipsis or cycles through messages on a timed interval on narrow viewports.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Primary-disabled color (#e6b3b0) is derived — no light red tint was present in the extracted palette.
- Star rating color assumed to match primary (#b72c27); no dedicated rating color was extracted.
- Exact font weights and sizes for Saira and Instrument Sans are inferred from typical Google Fonts usage — the live site may load specific optical sizes or variable-font instances not captured in extraction.
- Consolas usage context (spec tables vs. general monospace) is assumed from the font stack presence alongside the product-catalog nature of the site.
- Box-shadow tokens for cards, dropdowns, mega-menu, and modals are not defined — the site likely uses subtle shadows that were not captured.
- Animation and transition timing values (ease curves, durations for hover/focus/menu) are not extracted.
- Dark mode palette and component overrides are not present.
- Z-index hierarchy for sticky nav, mega-menu, modals, and promo-strip overlay stacking is not specified.
- Icon set (line weight, size grid, stroke vs. fill style) is not documented.
- Mobile-specific typography scale may differ from desktop — all values above are desktop-first.
- Loading states (skeleton screens, product image placeholders, spinner style) are not defined.
- Focus ring styles (color, width, offset) for keyboard accessibility are not extracted.
- Form validation patterns beyond text-input error state (select, radio, checkbox, textarea) are not specified.
- Cart drawer / mini-cart component styling is not captured.
- Product comparison table layout and interaction patterns are not defined.
