---
version: alpha
name: "JennAir"
source_url: "https://www.jennair.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Obsidian first — the entire digital experience opens into a field of near-black (#0b0b0b), inverting the white-canvas convention that dominates kitchen appliance marketing and turning every product photograph into a cinematic still. Stainless ranges and column refrigerators float in darkness, each control knob and burner ring lit against negative space with the precision of a gallery installation. This is the visual logic of the 2018 "Bound by Nothing" rebrand carried into every pixel: absence as a design material, darkness as a statement of confidence rather than a void to fill. Primary call-to-action surfaces arrive as stark white (#ffffff) rectangles — the contrast voltage is absolute, with no gradient, shadow, or glow to soften the edge. Buttons carry near-zero rounding at `{rounded.xs}`, just enough to feel intentional rather than browser-default, and the lack of pill shapes or playful curves underscores the brand's architectural severity. A secondary warm accent (#b08d57) surfaces sparingly — in promotional highlights, hover underlines, and the occasional badge — borrowing the matte brass tone of JennAir's physical hardware finishes without ever dominating the palette. Typography runs in a geometric sans-serif stack at restrained weights: display headlines at `{typography.display-xl}` set weight 300 against the dark canvas, trusting the backdrop and generous `{spacing.section}` gutters to supply visual mass. Body copy sits at #999999 on the dark field, readable but deliberately dimmed so that product imagery remains the loudest element on every page. Navigation labels and category headers favor tracked uppercase at `{typography.nav-label}`, reinforcing the architectural register without decorative type. The layout operates in two distinct design expressions — NOIR (all-black hardware, jet surfaces, maximum drama) and RISE (warm stainless, softer metallics, slightly approachable) — yet both share the same dark digital shell. Product grids step from single-column on mobile to three-across on desktop at a 1128px breakpoint, with hero modules filling the viewport behind autoplay video loops and a single display-weight headline. Cards and product tiles elevate slightly off the canvas at #161616, separated by 1px borders at #2a2a2a — the distinction is felt more than seen, a paper-thin lift that preserves the seamless dark field while providing enough structure for scannable grids.

colors:
  primary: "#ffffff"
  primary-active: "#d9d9d9"
  primary-disabled: "#4a4a4a"
  accent-warm: "#b08d57"
  accent-warm-active: "#97783f"
  ink: "#ffffff"
  body: "#999999"
  muted: "#666666"
  muted-soft: "#4a4a4a"
  hairline: "#2a2a2a"
  hairline-soft: "#1e1e1e"
  border-strong: "#3d3d3d"
  canvas: "#0b0b0b"
  canvas-elevated: "#111111"
  surface-soft: "#161616"
  surface-card: "#1a1a1a"
  surface-strong: "#222222"
  on-primary: "#0b0b0b"
  on-accent: "#0b0b0b"
  on-dark: "#ffffff"
  error: "#cf4444"
  success: "#3a8a5c"
  star-rating: "#b08d57"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Knockout', 'Barlow Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: 1.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Knockout', 'Barlow Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 1.2px
    textTransform: uppercase
  display-md:
    fontFamily: "'Knockout', 'Barlow Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Knockout', 'Barlow Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  title-lg:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  title-md:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  link:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  product-price:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "'Gotham', 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
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
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-accent:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-warm-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: 12px 0
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline}"
  nav-bar-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-label}"
    padding: 8px 16px
  nav-bar-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    border-bottom: "2px solid {colors.ink}"
  mega-menu:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xxl}"
    border-bottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 0
    border: "1px solid {colors.hairline}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs} {rounded.xs} 0 0"
  product-card-content:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.product-price}"
    color: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  hero-module:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 100vh
    padding: "{spacing.section} {spacing.xl}"
  hero-module-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.4)"
    textColor: "{colors.on-dark}"
  hero-module-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 40px"
    height: 48px
  design-expression-toggle:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "10px 24px"
  design-expression-toggle-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "10px 24px"
  category-nav:
    backgroundColor: "{colors.canvas-elevated}"
    textColor: "{colors.body}"
    typography: "{typography.nav-label}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  spec-table-label:
    typography: "{typography.spec-label}"
    color: "{colors.muted}"
  spec-table-value:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
  spec-table-row:
    border-bottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
  comparison-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  feature-highlight:
    backgroundColor: "{colors.canvas-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
  promo-banner:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    border-top: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.micro-label}"
    color: "{colors.body}"
  badge-noir:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"
  badge-rise:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    border-bottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  modal-overlay:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    scrim: "{colors.scrim}"
  breadcrumb:
    typography: "{typography.caption-sm}"
    color: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption-sm}"
    color: "{colors.ink}"
  video-hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    minHeight: 100vh
  video-hero-play-button:
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    height: 64px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a white (#ffffff) solid rectangle on the dark canvas with near-black text (#0b0b0b). The contrast is absolute — no gradients, no shadows, no glow. Uppercase label at `{typography.button-md}` with 1.2px letter-spacing gives each word the weight of an engraved nameplate. Corners carry a minimal `{rounded.xs}` (4px), just enough to distinguish from a raw browser default. On hover, the surface dims to #d9d9d9 (`{colors.primary-active}`); when disabled, it drops to #4a4a4a with muted text, nearly dissolving into the dark field.

**`button-secondary`** — A ghost button with a 1px white border and white text on the dark canvas, used for "Compare," "View Details," and secondary navigation alongside the solid primary. On hover, the fill inverts — white background floods in and text switches to the dark on-primary tone. The border disappears into the fill, creating a satisfying state change that rewards interaction.

**`button-accent`** — A warm brass-toned button (#b08d57) used sparingly for promotional CTAs, limited-edition callouts, and RISE design expression highlights. Dark text on the warm surface reads as premium without pulling attention from the primary white system. The active state deepens to #97783f.

**`button-tertiary-text`** — A borderless, backgroundless text link for inline actions like "Learn More" or "See All Specifications." Uses the smaller `{typography.button-sm}` weight to sit comfortably within body copy without disrupting the reading flow.

### Navigation
**`nav-bar`** — The persistent top navigation bar sits at 72px on a #0b0b0b canvas, separated from the page body by a single hairline border (#2a2a2a). The logo occupies the left third, with navigation links centered and utility icons (search, account, location) right-aligned. The bar is visually indistinguishable from the page background — the only separation is the thin lower border, maintaining the unbroken dark field.

**`nav-bar-link` / `nav-bar-link-active`** — Navigation labels use tracked uppercase at `{typography.nav-label}` in a muted #999999 tone. The active state brightens to full white (#ffffff) and adds a 2px white underline, providing clear wayfinding without introducing any new color. Hover states transition the text from muted to white.

**`mega-menu`** — A full-width dropdown panel on the slightly elevated surface (#161616), containing product category columns, featured imagery, and promotional links. The panel is bounded by a hairline border at the bottom and uses `{spacing.xl}` padding for generous breathing room between columns.

### Cards
**`product-card`** — The primary product listing container: a #1a1a1a surface with 1px hairline border (#2a2a2a) and minimal `{rounded.xs}` rounding. The image region occupies the top two-thirds on a slightly lighter #161616 background, with product details stacked below in `{spacing.base}` padded content area. The title uses `{typography.title-sm}` in full white, the price in `{typography.product-price}`, and any badge overlays the image in the top-left corner. Cards have no box shadow — elevation is achieved solely through the fractional lightness difference between card and canvas.

**`product-card-badge`** — A compact brass-toned badge (#b08d57) with dark text, used to flag "New," "NOIR," or "RISE" design expressions. The uppercase `{typography.badge}` label with tight padding keeps badges small and architectural rather than decorative.

### Hero
**`hero-module`** — Full-viewport height, full-width, often backed by a slow-panning video of a kitchen interior or product detail shot. A single display headline at `{typography.display-xl}` — uppercase, weight 300, tracked at 1.5px — sits centered or left-aligned over a 40% black scrim overlay. Below, a single primary CTA button with wider horizontal padding (40px) anchors the composition. The module has no lower border — it bleeds directly into the next content section.

**`video-hero`** — A variant of the hero module optimized for autoplay video content. The play button overlay uses a translucent white circle (`rgba(255, 255, 255, 0.15)`) at 64px diameter with a `{rounded.full}` radius, visible enough to invite interaction without obscuring the footage.

### Design Expression Toggle
**`design-expression-toggle`** — A binary toggle control for switching product displays between NOIR and RISE design expressions, the two hardware finish families that define JennAir's product line. Inactive state sits on a #222222 surface with muted text; the active state fills with full white background and dark text, creating an on/off contrast that mirrors the brand's light-dark polarity.

### Specifications
**`spec-table`** — Appliance specification panels rendered on the #161616 surface with alternating row borders at #2a2a2a. Labels use the tracked uppercase `{typography.spec-label}` in muted text, while values use `{typography.body-sm}` in full white. Rows carry `{spacing.md}` vertical padding. The table has minimal rounding (`{rounded.xs}`) and no outer border, relying on the surface difference alone for containment.

**`comparison-card`** — A bordered card variant for side-by-side product comparisons. Each card contains a product image, model name, key specifications, and a CTA button. The 1px hairline border and `{spacing.lg}` internal padding keep comparisons scannable across two or three columns.

### Feature Highlight
**`feature-highlight`** — A full-width section on the `{colors.canvas-elevated}` surface pairing a large product detail photograph with a `{typography.title-md}` headline and `{typography.body-md}` description. No rounding, generous `{spacing.section}` vertical padding. Typically alternates image-left/text-right and image-right/text-left in a storytelling scroll.

### Search
**`search-bar`** — A dark-surfaced input field (#1a1a1a) with a hairline border and `{rounded.xs}` rounding. Placeholder text appears in `{colors.muted}`. On focus, the border thickens to 2px and shifts to white (#ffffff), the highest-contrast focus indicator possible on the dark canvas. The search icon sits inside the left padding, matching the muted text color.

### Footer
**`footer`** — A full-width section on the same #0b0b0b canvas as the page body, separated only by a 1px hairline top border. Footer headings use `{typography.micro-label}` — 10px, tracked uppercase, weight 700 — in #999999 to establish column hierarchy. Links below use `{typography.link}` in the muted #666666 tone, brightening to white on hover. The footer contains product categories, customer service links, social icons, and legal notices. Generous `{spacing.xxl}` vertical padding maintains the brand's preference for breathing room.

### Badges
**`badge-noir`** — A dark-themed badge with a #0b0b0b fill, white text, and a hairline border, used to tag products in JennAir's NOIR design expression. The uppercase `{typography.badge}` label reads as a material swatch rather than a promotional tag.

**`badge-rise`** — A warm brass badge (#b08d57) with dark text for products in the RISE design expression. The warmth of the metallic accent distinguishes it from the monochrome NOIR badge at a glance.

### Accordion
**`accordion-header`** — Used in product detail pages for collapsible specification sections, feature descriptions, and installation requirements. The header sits on a #161616 surface with a hairline bottom border, using `{typography.title-sm}` in white. An expand/collapse chevron icon right-aligns in the muted tone. Content panels beneath use the base canvas color with standard body text.

### Promo Banner
**`promo-banner`** — A slim 40px bar across the top of the page in the warm brass accent (#b08d57) with dark text, used for site-wide promotions, financing offers, or event announcements. The `{typography.caption}` sizing keeps the message compact and scannable without disrupting the dark atmosphere below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger icon with full-screen slide-out menu on the dark canvas; hero module reduces to 80vh with smaller display type (`{typography.display-md}`); mega-menu converts to stacked accordion panels; product comparison is disabled or reduced to single-card scrolling; spec-table rows stack label-above-value; footer columns stack vertically; promo banner text may truncate with ellipsis |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows abbreviated links with "More" overflow; hero module at 90vh; mega-menu uses two-column layout; product comparison shows two cards side-by-side; spec-table remains horizontal; footer uses two-column layout; design-expression toggle remains inline |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all category links visible; hero module at 100vh with full display typography; mega-menu at full width with three or four columns; product comparison shows three cards; feature highlights alternate image/text layout; footer at three columns |
| Wide | > 1440px | Three-column product grid within a 1440px max-width container, centered; hero module maintains 100vh but imagery may extend beyond container; additional canvas-colored gutters at edges; all components respect the max-width constraint; product card sizing increases slightly for comfortable viewing at large displays |

### Touch Targets
- All buttons maintain a minimum 48px touch target height on mobile and tablet
- Nav-bar links use 16px horizontal padding for comfortable tap spacing
- Product cards are tappable across their entire surface area, not just the title
- Accordion headers extend full width with `{spacing.base}` vertical padding for easy expansion
- Design-expression toggle buttons maintain 44px minimum height with 24px horizontal padding
- Search bar uses 48px height across all breakpoints
- Footer links maintain at least 44px vertical tap targets through line-height and padding

### Collapsing Strategy
- Top navigation collapses from full link bar to hamburger at < 744px; the slide-out menu fills the viewport on the dark canvas
- Product grid collapses from 3 columns (desktop) to 2 (tablet) to 1 (mobile)
- Hero module reduces from 100vh to 80vh on mobile, with display type stepping down two scale levels
- Mega-menu converts from multi-column dropdown to stacked accordion on mobile
- Product comparison collapses from 3-up to 2-up to single-card horizontal scroll
- Feature-highlight sections stack image-above-text on mobile instead of side-by-side
- Footer collapses from 3 columns to 2 to 1 as viewport narrows
- Spec-table rows maintain horizontal label-value layout on tablet but stack vertically on mobile
- Promo banner remains a single line at 40px across all breakpoints; text truncates rather than wraps

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All color values are inferred from widely-documented brand knowledge (2018 rebrand), not extracted from the live site.** The jennair.com site returned "Access Denied" during extraction, likely due to anti-bot protections or JavaScript-gated rendering.
- **No font stacks were extracted.** The typography families listed (Knockout for display, Gotham for UI) are educated estimates based on the brand's documented visual identity; the actual web fonts served may differ significantly.
- **Exact hex values for canvas, surface, and border tones are approximations.** The specific grays used on the live site could not be sampled.
- **The warm accent (#b08d57) is inferred from JennAir's brass/copper hardware finishes** (particularly the RISE collection); the digital palette may use a different accent or no warm accent at all.
- **NOIR vs. RISE design expression differentiation** is documented for physical products but the digital implementation (separate color tokens, themed sections, or toggle-based rendering) could not be verified.
- Hover states, focus rings, and transition timing values are entirely unknown
- Animation and motion design specifications (hero video transitions, card hover lifts, accordion expand/collapse easing) were not observed
- Icon library and illustration system (SVG sprites, icon font, or inline paths) could not be determined
- Loading states (skeleton screens, spinners, progress indicators) are unverified
- Modal and dialog component styling, including the scrim opacity and close-button treatment, is estimated
- Dark-on-dark surface hierarchy (the specific gray steps between canvas, elevated, soft, card, and strong) may not match the actual visual progression
- Z-index stacking order for modals, mega-menu, sticky nav, and promo banner is unknown
- Exact breakpoint values are estimated from common appliance/luxury-brand patterns; the actual responsive behavior may use different thresholds
- Print stylesheet and reduced-motion preference handling were not observed
- Product configurator or build-your-kitchen interactive components, if they exist, were not captured
- Form validation messaging patterns (inline vs. summary, icon usage, animation) could not be verified
