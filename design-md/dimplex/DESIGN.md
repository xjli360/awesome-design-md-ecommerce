---
version: alpha
name: "Dimplex"
source_url: "https://www.glendimplexamericas.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Steel-blue light at #005faa floods the interface the way halogen floods a showroom floor — it is the single dominant hue across navigation bars, CTAs, and product-category headers, lending a corporate precision to a company whose products produce actual warmth. Glen Dimplex Americas runs its digital presence on a tightly controlled blue spectrum: primary actions sit at #005faa, hover states deepen to #004b96, and deep-navy banners (#003782, #000083) anchor hero sections where electric fireplaces glow against near-black backgrounds. Against this cool authority, a warm brown (#85644f) surfaces in product lifestyle imagery and accent borders — the only chromatic nod on the page that visually acknowledges flame. A secondary teal (#15576f) distinguishes outdoor and ventilation product lines from the core indoor fireplace catalog, creating a wayfinding system that is color-coded rather than icon-driven. Typography loads through CSS custom-property aliases (`main`, `alt`) that resolve at runtime, making the actual typeface opaque to extraction, but the rendered result reads as a clean geometric sans-serif in the Helvetica Neue / Roboto lineage: moderate x-height, tight letterspacing on headlines, generous line-height on specification copy. Display headings run bold at 36–48px for hero headlines, dropping to 600-weight at 22–28px for section titles — nothing shouts, because the product photography (glowing ember beds, linear flame walls, outdoor patio scenes) carries the emotional register. Cards use `{rounded.xs}` corners and rest on `{colors.surface-soft}` (#f5f5f5) panels that keep the grid feeling architectural rather than playful; buttons are squared-off with `{rounded.xs}` to echo the rectilinear geometry of mantel surrounds and linear fireplaces. Spacing is generous but metronomic — `{spacing.section}` between major content blocks, `{spacing.lg}` between product cards — producing a vertical rhythm that gives large product images room to breathe. An amber accent (#d39e00) handles warning states and energy-rating badges, while red (#bd2130) marks form errors and out-of-stock flags, rounding out a palette that is overwhelmingly blue-and-gray with deliberate, product-motivated warm punctuation.

colors:
  primary: "#005faa"
  primary-active: "#004b96"
  primary-disabled: "#99bfdd"
  primary-deep: "#003782"
  navy: "#000083"
  navy-dark: "#09276c"
  ink: "#2d2d2d"
  ink-deep: "#1d2124"
  body: "#6d6d6d"
  muted: "#949494"
  muted-soft: "#757575"
  hairline: "#dae0e5"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-teal: "#15576f"
  accent-teal-active: "#117a8b"
  accent-brown: "#85644f"
  accent-amber: "#d39e00"
  accent-green: "#1e7e34"
  error: "#bd2130"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    borderColor: "{colors.primary}"
    borderWidth: 2px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    borderColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.error}"
    textColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-link-active:
    textColor: "{colors.primary}"
  nav-link-inactive:
    textColor: "{colors.body}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  mega-menu-heading:
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: "4 / 3"
  product-card-title:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  product-card-subtitle:
    textColor: "{colors.body}"
    typography: "{typography.caption}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-overlay:
    background: "linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.2) 100%)"
    textColor: "{colors.on-dark}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 36px
  hero-subtitle:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-lg}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  category-tile-icon:
    color: "{colors.primary}"
    size: 48px
  category-tile-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline-soft}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    padding: "{spacing.md} {spacing.base}"
  spec-table-cell:
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    padding: "{spacing.md} {spacing.base}"
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
  energy-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  product-line-badge-outdoor:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  product-line-badge-indoor:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  search-bar-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  footer-section:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  footer-legal:
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  comparison-table-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  comparison-table-cell:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderColor: "{colors.hairline-soft}"
  dealer-locator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  dealer-locator-pin:
    color: "{colors.primary}"
    size: 32px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The main conversion trigger, used for "Find a Dealer," "View Product," and "Get a Quote" actions. A solid #005faa rectangle with white text set in 600-weight at 16px, using `{rounded.xs}` (4px) corners that mirror the hard-edged geometry of the product line. On hover, the background darkens to #004b96; when disabled, it softens to a desaturated blue (#99bfdd) with reduced contrast.

**`button-secondary`** — An outlined variant with a 2px #005faa border, white fill, and blue text. Used for secondary actions like "Compare Products" and "Download Brochure." On hover, the background fills with `{colors.surface-soft}` and the border deepens to `{colors.primary-active}`.

**`button-ghost`** — A borderless, fill-less button rendered in primary blue text. Used for tertiary actions like "Back to Results" or inline navigation. An underline appears on hover to signal interactivity.

**`button-dark`** — A dark-background variant using `{colors.ink}` (#2d2d2d) fill with white text, deployed inside hero sections and dark banners where the primary blue would lack sufficient contrast against the background imagery.

### Cards
**`product-card`** — The primary content unit for product listings. A `{colors.surface-card}` (#fafafa) container with `{rounded.xs}` corners, no visible border, and a subtle elevation shadow on hover. The image area uses a 4:3 aspect ratio with a soft gray (#f5f5f5) placeholder. Product name renders in `{typography.title-sm}` (16px, 600-weight), with the product category in `{typography.caption}`. A colored badge in the top-left distinguishes indoor (`{colors.primary}` blue) from outdoor (`{colors.accent-teal}` teal) products.

**`category-tile`** — A square tile used on the homepage and category landing pages to represent product families (Electric Fireplaces, Outdoor Heating, Baseboard Heaters, etc.). A 48px icon in `{colors.primary}` sits above the category title in `{typography.title-md}`. On hover, the entire tile inverts to a primary-blue background with white text and icon, providing a strong visual cue.

### Navigation
**`nav-bar`** — A fixed 80px header on a white background with a 1px bottom border in `{colors.hairline}`. The Dimplex logo sits left, with nav links in `{typography.nav-link}` (15px, 600-weight). Active links are colored `{colors.primary}`; inactive links use `{colors.body}` gray. A dark variant (`nav-bar-dark`) appears on landing pages where the hero image extends behind the header — here the bar is transparent over the image, with white text that transitions to the light variant on scroll.

**`mega-menu`** — A dropdown panel triggered by hovering over top-level nav links. It uses a white background with a top border in `{colors.hairline}`, and organizes products into columns. Column headings are styled in `{typography.title-sm}` colored `{colors.primary}`, with individual links in `{typography.body-sm}`. Product thumbnail images may appear alongside links for high-priority categories.

### Hero
**`hero-section`** — A full-bleed banner using a dark background image (typically a fireplace or patio scene) overlaid with a gradient scrim from 55% black at top to 20% at bottom. Headline text runs in `{typography.display-xl}` (48px, 700-weight) in white, with a subtitle in `{typography.body-lg}`. The CTA button uses `{typography.button-md}` with extra-wide padding (16px 36px) for prominence. On mobile, the headline scales down to `{typography.display-md}` and the CTA stretches to full width.

### Specification Tables
**`spec-table`** — A striped data table used on product detail pages to display technical specifications (BTU output, dimensions, weight, voltage, flame technology). Header cells use `{typography.spec-label}` (13px, 600-weight) on a `{colors.surface-soft}` background; data cells use `{typography.spec-value}` (14px, 400-weight). Alternating rows use `{colors.surface-soft}` for readability. Borders are 1px in `{colors.hairline-soft}`.

**`comparison-table`** — A side-by-side product comparison layout with a `{colors.primary}` header row bearing product names in white `{typography.title-sm}`. Cell borders use `{colors.hairline-soft}`, and each row represents a specification dimension. Checkmarks render in `{colors.accent-green}` and dashes in `{colors.muted}`.

### Badges
**`product-card-badge`** — A compact label positioned absolutely in the top-left of a product card. Solid `{colors.primary}` background with white uppercase text in `{typography.badge}` and `{rounded.xs}` corners.

**`energy-badge`** — An amber (#d39e00) badge with dark text, used to highlight energy-efficiency ratings and certifications on product cards and detail pages.

**`product-line-badge-outdoor` / `product-line-badge-indoor`** — Color-coded category badges: teal (#15576f) for outdoor products, primary blue (#005faa) for indoor. Both share the same structure — uppercase `{typography.badge}` text, `{rounded.xs}` corners, and tight padding.

### Search
**`search-bar`** — A rectangular input with a 1px `{colors.hairline}` border and `{rounded.xs}` corners. Placeholder text appears in `{colors.muted}`. On focus, the border thickens to 2px in `{colors.primary}` with no box-shadow, keeping the interaction clean. A magnifying-glass icon sits inside the right edge of the field.

### Footer
**`footer-section`** — A dark footer using `{colors.ink-deep}` (#1d2124) as background. Column headings are white in `{typography.title-sm}`, links are `{colors.muted}` gray in `{typography.link}`, and lighten to white on hover. The bottom row contains legal text in `{typography.caption-sm}` and corporate logos. Newsletter signup uses a text input and primary button inline.

### Breadcrumbs
**`breadcrumb`** — A horizontal trail rendered in `{typography.caption}` with `{colors.muted}` for inactive segments, `{colors.ink}` for the current page, and a right-chevron separator in `{colors.muted-soft}`. Used on product detail and category pages to reinforce the product hierarchy.

### Accordion
**`accordion-header`** — A borderless collapsible header using `{typography.title-sm}` with a bottom hairline in `{colors.hairline}`. A plus/minus icon in `{colors.primary}` sits right-aligned and animates on toggle. Used for FAQ sections, product features, and specification groups on detail pages.

### Dealer Locator
**`dealer-locator`** — A map-and-list component on a `{colors.surface-soft}` background with `{rounded.xs}` corners. The map panel uses `{colors.primary}` pins. The list panel displays dealer names in `{typography.body-md}` with address details in `{typography.caption}`, and a "Get Directions" ghost button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger with slide-in drawer; hero headline scales to display-md (28px); product cards stack vertically at full width; CTAs expand to full-width blocks; comparison table scrolls horizontally; spec table cells stack label-over-value; mega-menu becomes an accordion within the drawer |
| Tablet | 744–1128px | Two-column product grid; nav links condense or collapse to hamburger depending on count; hero uses display-lg (36px); category tiles arrange in a 2×3 grid; footer stacks into two columns; dealer locator shows map above list |
| Desktop | 1128–1440px | Three- to four-column product grid; full mega-menu dropdowns on hover; hero at display-xl (48px); sticky nav with 1px bottom border appearing on scroll; side-by-side dealer locator (map left, list right); multi-column footer |
| Wide | > 1440px | Max-width container at 1440px, centered; additional whitespace in section padding; four-column product grids; hero imagery can extend full bleed while content stays contained |

### Touch Targets
- All buttons maintain a minimum 48px tap height, matching the defined button heights.
- Nav links and footer links have 44px hit areas even when text is smaller.
- Accordion headers are padded to at least 48px tall for easy tapping.
- Product card badges and category tiles are sized for comfortable touch interaction at 44×44px minimum.
- Search bar and form inputs are 48px tall across all breakpoints.

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon below 744px, opening a full-height slide-in drawer with accordion sub-menus.
- Product grids collapse from four columns to two on tablet and one on mobile, maintaining consistent card proportions.
- Comparison tables switch to horizontal scroll on screens below 1128px, with the first column (spec label) pinned.
- The dealer locator stacks vertically on mobile with the map on top and the list below.
- Category tiles drop from a 4-across row to 2×3 on tablet and a vertical stack on mobile.
- Footer columns collapse into accordions on mobile, with headings acting as toggle triggers.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The actual brand typeface could not be extracted — the site loads fonts via CSS custom-property aliases (`main`, `alt`) that resolve at runtime. The system font stack used here is a placeholder; the real typeface may be a licensed geometric sans-serif.
- No web-font files or @font-face declarations were found in static assets; the font may be injected via JavaScript or a tag manager.
- Shadow tokens (box-shadow values for cards, modals, dropdowns) were not present in static CSS.
- Animation and transition timing values (easing curves, durations) are not documented.
- Dark mode or alternate theme palettes were not detected.
- Icon set and sizing guidelines are unknown — the site likely uses an icon font or SVG sprite that was not captured in extraction.
- Exact z-index hierarchy for modals, sticky nav, and mega-menu overlays could not be determined.
- Focus ring styles (color, width, offset) for keyboard accessibility are not specified.
- Mobile-specific typography scale adjustments (if different from proportional scaling of the desktop values) could not be verified.
- Several extracted colors (#ff04ee, #721c6f, #8181cd, #3e3fa4, #1b1e6d, #3c2e61, #330c6d, #0c0d6b) appear to be framework defaults, product-category indicators, or development artifacts — their precise role could not be confirmed without JavaScript execution.
- The meta theme-color tag was absent, so mobile browser chrome color is unset.
- Loading states (skeleton screens, spinners) and empty states were not captured.
