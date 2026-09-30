---
version: alpha
name: "Gozney"
source_url: "https://www.gozney.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  That first thing gozney.com loads is not a product shot — it is a wall of #272c32, a soot-dark charcoal that reads like the inside of a dome oven after a thousand fires. Against that dark surface, every primary CTA detonates in #c8102e, a fire-engine red pulled from the temperature gauge of an industrial kiln rather than the playful warmth of a lifestyle brand. The tension between these two anchors — blackened steel and open flame — defines the entire visual system. A deep navy (#012169) appears as a third voice behind feature blocks and editorial sections, pulling the palette toward something maritime and British, fitting for a brand born on the Dorset coast. Neutral surfaces run from a light #dedede hairline through white cards and a clean canvas, never competing with the product photography of scorched crusts and glowing fireboxes. Typography is Maison Neue across three cuts: Book for body text at 400 weight, Demi for headings and buttons at 600–700, and Mono for the technical specs that oven buyers actually care about — maximum temperature, recovery time, cooking surface area. Display headings top out at 48px and carry negative letter-spacing to keep the silhouette tight and engineered. Corner radii stay modest at {rounded.sm} for buttons and {rounded.md} for cards, rejecting the pill-shaped friendliness of wellness DTC in favor of squared-off confidence. Spacing follows an 8px grid anchored at {spacing.base} (16px), with generous {spacing.section} (64px) gaps that give full-bleed hero images room to breathe. The overall effect is a digital showroom that feels like walking through a commercial kitchen outfitter: everything bolted down, nothing decorative, the product always centered under a single overhead light.

colors:
  primary: "#c8102e"
  primary-active: "#a00d24"
  primary-disabled: "#e8899a"
  ink: "#121212"
  body: "#272c32"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#dedede"
  hairline-soft: "#ececec"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#272c32"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-navy: "#012169"
  star-rating: "#f59e0b"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Maison Neue Book', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  mono:
    fontFamily: "'Maison Neue Mono', 'SF Mono', 'Fira Code', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "'Maison Neue Demi', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
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
    padding: 14px 28px
    height: 48px
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
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  button-ghost-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    border: "1px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.primary}"
    textColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  spec-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    padding: "{spacing.md} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  spec-label:
    typography: "{typography.uppercase-tag}"
    textColor: "{colors.muted}"
  spec-value:
    typography: "{typography.mono}"
    textColor: "{colors.ink}"
  fuel-type-toggle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
  fuel-type-toggle-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  comparison-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  comparison-card-featured:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
    padding: "{spacing.lg}"
  recipe-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  recipe-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  recipe-card-meta:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  footer-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-navy:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"

---

## Components

### Buttons
**`button-primary`** — The core conversion button across the site, rendered as a solid block of #c8102e red with white text in Maison Neue Demi at 600 weight. It uses `{rounded.sm}` (8px) corners and 48px height, creating a dense, structural hit area that reads more industrial equipment than lifestyle e-commerce. On hover, the background deepens to `{colors.primary-active}` (#a00d24); the disabled state fades to `{colors.primary-disabled}` (#e8899a), draining the heat out entirely.

**`button-secondary`** — A white canvas button with a 1px `{colors.hairline}` border, used for "Learn More", "View Details", and other secondary actions alongside the red primary. On active state, the background shifts to `{colors.surface-soft}` and the border darkens to `{colors.ink}`, creating clear hierarchy without color competition. The outline treatment keeps the page from feeling over-saturated when multiple CTAs appear in proximity.

**`button-ghost`** — A borderless, backgroundless button with `{colors.primary}` red text, used for tertiary actions like "Cancel", "Back", or inline links that need button-level click targets. On dark backgrounds, the `button-ghost-on-dark` variant swaps to `{colors.on-dark}` white text with a 1px white border, maintaining visibility against the charcoal hero sections.

### Product Cards
**`product-card`** — The primary container for oven listings and accessory grids. A white `{colors.surface-card}` background with `{rounded.md}` (12px) corners frames the product image, name, price, and a brief spec line. The image area uses top-only rounding (`{rounded.md} {rounded.md} 0 0`) so the photo bleeds to the card edges horizontally. Cards carry no drop shadow at rest — the white surface against the `{colors.surface-soft}` page background provides enough separation. A `product-card-badge` overlay in the top-left corner flags "Sale" items in the primary red.

### Navigation
**`nav-bar`** — A fixed 72px white header with a `{colors.hairline-soft}` bottom border, housing the Gozney logo, uppercase nav links in Maison Neue Demi, and cart/account icons. The uppercase `{typography.nav-link}` with 0.5px letter-spacing gives the header a technical, catalog-like feel. Active links switch to `{colors.primary}` red; inactive links sit in `{colors.muted}`. The `nav-bar-dark` variant uses `{colors.surface-dark}` (#272c32) as the background with white text, appearing on hero-heavy landing pages where the header overlays a dark image.

**`announcement-bar`** — A narrow 40px strip above the nav in `{colors.ink}` (#121212), used for shipping promotions and seasonal offers. Text runs in `{typography.caption}` at 13px in white, keeping the messaging compact and scannable. The bar is the darkest element on the page, anchoring the top edge.

### Hero
**`hero-section`** — A full-bleed section with `{colors.surface-dark}` (#272c32) background and white display text, typically overlaying a lifestyle photograph of an oven in use — flames visible, dough stretching, stone floor glowing. The headline uses `{typography.display-xl}` at 48px with -1px tracking. The CTA (`hero-cta`) is a red `{colors.primary}` button with extra-wide 16px 32px padding, scaled up from the standard button-primary to match the hero's visual weight.

### Specification Components
**`spec-row`** — A horizontal row used in oven detail pages to present technical data: maximum temperature, cooking surface dimensions, fuel type, weight, and recovery time. Each row sits on `{colors.surface-soft}` with a 1px `{colors.hairline}` bottom border. The label uses `{typography.uppercase-tag}` in `{colors.muted}` — tiny, tracked-out, all-caps — while the value uses `{typography.mono}` (Maison Neue Mono) in `{colors.ink}`, giving numerical data the precision formatting it deserves.

**`fuel-type-toggle`** — A segmented control for switching between wood-fired, gas, and multi-fuel oven variants on product pages. Each segment is a `{rounded.sm}` pill in `{colors.surface-soft}` with `{colors.muted}` text; the active segment inverts to `{colors.ink}` background with `{colors.on-dark}` white text. The toggle uses `{typography.button-sm}` at 14px and sits within the product detail sidebar, often above the Add to Cart button.

### Comparison
**`comparison-card`** — Used on the "Compare Ovens" page, each card presents a single oven model with its image, key specs, and price inside a `{colors.surface-card}` container with `{rounded.md}` corners and a 1px `{colors.hairline}` border. The `comparison-card-featured` variant replaces the hairline border with a 2px `{colors.primary}` red border to highlight the recommended or best-selling model, drawing the eye without adding extra graphic elements.

### Recipe Cards
**`recipe-card`** — A content card for the recipe section, structurally identical to the product card but carrying different metadata. The image area shows the finished dish with top-only rounding. Below the image, the recipe title uses `{typography.title-sm}` and the metadata line (cook time, difficulty, oven type) uses `{typography.caption}` in `{colors.muted}`. Cards link through to full recipe pages with step-by-step instructions.

### Badges
**`badge-sale`** — A compact uppercase label in `{colors.primary}` red with white text, used on product cards and listing pages to flag discounted items. The `{rounded.xs}` (4px) corners and tight 2px 6px padding keep the badge small enough to overlay a product image without obscuring the product.

**`badge-navy`** — A navy (#012169) variant used for "New" or "Exclusive" flags, providing visual separation from the sale badge so shoppers can distinguish promotional pricing from new arrivals at a glance. Same sizing and typography as `badge-sale`.

### Forms
**`text-input`** — Standard form fields for checkout, account creation, and contact forms. A white background with a 1px `{colors.hairline}` border and `{rounded.sm}` corners at 48px height. On focus, the border thickens to 2px and switches to `{colors.primary}` red, creating a strong, accessible focus indicator. Error states also use a 2px red border, with error message text rendered in `{colors.primary}` below the field.

**`newsletter-input`** — A footer-specific email input paired with the `newsletter-submit` button. Matches the standard input styling but sits against the dark `{colors.surface-dark}` footer background, making the white input field pop. The red submit button creates a high-contrast capture point at the bottom of every page.

### Accordion
**`accordion-header`** — A clickable row for collapsible FAQ and product detail sections, using `{typography.title-sm}` in `{colors.ink}` with a chevron icon that rotates on open. The `{colors.hairline-soft}` bottom border separates sections without heavy visual weight. Content panels use `{typography.body-md}` in `{colors.body}`, providing enough contrast to read comfortably without competing with the header.

### Footer
**`footer-section`** — A full-width dark section in `{colors.surface-dark}` (#272c32), mirroring the hero palette and bookending the page in charcoal. Text runs in `{colors.muted-soft}` (#9ca3af) for body copy and links, with column headings in `{typography.title-sm}` at `{colors.on-dark}` white. Links lighten to `{colors.canvas}` white on hover. The footer houses navigation columns, the newsletter signup, social icons, and legal text.

### Search & Breadcrumbs
**`search-overlay`** — A white full-width panel that drops below the nav bar when the search icon is activated. The input field and results list both use `{typography.body-md}` against `{colors.canvas}`, with `{spacing.lg}` padding to keep the overlay airy. Search suggestions appear as a simple text list with `{colors.muted}` helper text.

**`breadcrumb`** — A horizontal trail using `{typography.caption}` in `{colors.muted}`, with the current page in `{colors.ink}`. Breadcrumbs appear on product detail and category pages, sitting between the nav bar and the page title.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger with full-screen drawer; hero text scales to `{typography.display-md}`; product cards stack vertically; buttons become full-width; fuel-type toggle stacks vertically; spec rows remain full-width; footer columns collapse into accordion sections |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed with overflow into "More" dropdown; hero uses `{typography.display-lg}`; comparison cards display two-up; footer shows two-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with mega-menu dropdowns; hero uses `{typography.display-xl}`; comparison shows three-up; four-column footer; sticky nav with scroll shadow; spec table renders as a two-column grid |
| Wide | > 1440px | Max-width container at 1440px centered; expanded whitespace on sides; product grid can stretch to four columns on category pages; hero imagery scales to fill viewport with content capped at max-width |

### Touch Targets
- All interactive elements maintain a minimum 44px touch target per Apple HIG
- Nav bar icon buttons (cart, search, account) are 48px square for reliable tapping
- Fuel-type toggle segments are 40px tall with full-width hit areas on mobile
- Accordion headers are 48px tall with the full row acting as the tap target
- Product cards use the entire card surface as a tap target on mobile
- Footer links maintain 44px vertical spacing through padding

### Collapsing Strategy
- Primary nav collapses to a hamburger menu below 744px, with a slide-in drawer from the left containing all nav links, account, and search
- Product filters collapse into a sticky "Filter" bar that opens a bottom sheet on mobile
- Comparison cards collapse to a swipeable horizontal carousel on mobile, one card visible at a time
- Multi-column footer stacks into accordion-style expandable sections, with each column heading as a toggle
- Hero content stacks vertically on mobile with the CTA button expanding to full width
- Spec tables reflow from a two-column grid to a single-column stack, each row showing label above value
- Search transitions from an overlay panel to a full-screen takeover on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only five hex colors (#c8102e, #272c32, #012169, #dedede, #121212) were reliably extracted from the live site; all derived tones (muted, surface-soft, hairline-soft, primary-active, primary-disabled) are inferred from those anchors
- Star rating color (#f59e0b) is a standard gold assumed from common e-commerce patterns, not extracted from the site
- Hover and active states for most components are inferred; actual transition timing values (duration, easing) were not extractable
- The site may use additional accent colors loaded via JavaScript or Shopify theme settings that were not visible in the static CSS extraction
- Dark mode palette is not present on the live site; all tokens assume light mode only
- Shadow tokens (box-shadow values for cards, dropdowns, modals) were not observed in extraction
- Sub-brand or product-line-specific palettes (Dome, Arc, Roccbox) may exist but were not extractable from global styles
- Modal and overlay specifications (backdrop opacity, animation, close button placement) were not observed
- Focus-visible ring styles for keyboard navigation are assumed as 2px `{colors.primary}` outline; actual implementation may differ
- Loading states (skeleton screens, spinners) and empty states are not documented
- Video player control styling for product and recipe videos is not captured
- The exact Maison Neue font weights and OpenType features in use could not be verified from extraction; Book/Demi/Mono mapping is based on the font-family stack names found in the CSS
