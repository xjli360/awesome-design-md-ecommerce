---
version: alpha
name: "Misen"
source_url: "https://misen.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Misen is a direct-to-consumer cookware brand that speaks in a confident, utilitarian tone — think sharp blue accents against a mostly neutral canvas of warm grays and soft whites. The brand’s signature is a deep, almost navy blue (`#1c4bba`) that appears on primary buttons, navigation elements, and key product highlights, supported by a secondary blue (`#5084c3`) and a more muted slate (`#676986`) for body text and secondary information. The palette is anchored by a clean white background (`#f4f4f6`) and a range of soft grays (`#e5e5e5`, `#eeeeee`, `#d3d4dd`) that create subtle hierarchy without visual noise. Accents of teal (`#0f918b`) and a warm terracotta (`#ea8e74`) appear sparingly, likely for sale badges or limited-edition product treatments, while a muted red (`#ce5454`) signals errors or out-of-stock states. The typography relies on system sans-serif stacks — no custom brand font is declared — which gives the site a no-nonsense, functional feel that aligns with Misen’s “professional-grade, but for home cooks” positioning. Buttons are softly rounded (`{rounded.sm}`) and use the primary blue with white text (`{colors.on-primary}`), while product cards likely use a white surface (`{colors.surface-card}`) with subtle shadows. The overall mood is trustworthy and direct, avoiding the glossy, aspirational warmth of heritage cookware brands in favor of a clean, almost industrial clarity that puts product photography and specs front and center.

colors:
  primary: "#1c4bba"
  primary-active: "#2761a8"
  primary-disabled: "#cccccc"
  ink: "#212121"
  body: "#464343"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#d3d4dd"
  hairline-soft: "#e5e5eb"
  canvas: "#f4f4f6"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#0f918b"
  accent-terracotta: "#ea8e74"
  accent-terracotta-dark: "#d97154"
  error: "#ce5454"
  success: "#5dab57"
  badge-sale: "#ea8e74"
  badge-new: "#0f918b"
  star-rating: "#212121"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
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
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 24px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero:
    backgroundColor: "{colors.canvas}"
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
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Checkout," and key conversion points. Rendered in the brand's signature blue (`#1c4bba`) with white text and an 8px border radius. On hover, the background deepens to `#2761a8`; when disabled, it fades to `#cccccc` with muted text to indicate non-interactivity. **`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Learn More." Uses a white background with a `#d3d4dd` border that shifts to the primary blue on hover. **`button-tertiary`** — A text-only link styled as a button, used for less prominent actions such as "Cancel" or "Skip." **`button-pill`** — A fully rounded, compact variant used for filter tags, quick-add actions, or mobile navigation items.

### Cards
**`product-card`** — The core product display unit on collection pages and search results. A white card with a 12px border radius, containing a product image (rounded top corners), a title in `{typography.title-md}`, and a price in muted gray (`#676986`). Sale items receive a small badge (`{badge-sale}`) overlaid on the image. The card is designed to be clean and photography-forward, with minimal text interference.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, white background with a subtle bottom border (`#e5e5eb`). Links are uppercase, 14px, weight 600, with 0.5px letter spacing. The active link is underlined with a 2px primary blue border. The nav collapses to a hamburger menu on mobile. **`nav-link-active`** — The active state uses the primary blue and a bottom border to indicate current section.

### Forms
**`text-input`** — Standard text input for search, email signup, and address forms. A white background with a `#d3d4dd` border and 8px border radius. On focus, the border thickens to 2px and switches to the primary blue. Height is 44px to meet touch-target guidelines.

### Hero
**`hero`** — The full-width hero section on the homepage and landing pages. Uses the canvas background (`#f4f4f6`) with large display typography and a prominent primary CTA button. Padding is generous at 64px vertical and 24px horizontal. The hero may feature a full-bleed product image or lifestyle photography behind the text.

### Badges
**`badge-new`** and **`badge-sale`** — Small, uppercase, 11px badges used to flag product attributes. "New" uses the teal accent (`#0f918b`), while "Sale" uses terracotta (`#ea8e74`). Both have 4px border radius and tight padding for a compact, unobtrusive appearance.

### Footer
**`footer`** — A dark footer with an ink (`#212121`) background and white text. Links are in a muted gray (`#9a9db1`) and use `{typography.link}`. The footer contains columns for support, about, and social links, with generous section padding.

### Accordion
**`accordion`** — Used for FAQ sections and product details. A white card with a soft border and 8px radius. Headers use `{typography.title-md}` with 16px/24px padding. The accordion expands to reveal body text in `{typography.body-md}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to 24px; buttons become full-width; footer stacks columns |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 28px display; side-by-side form fields |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full 32px display; multi-column footer |
| Wide | > 1440px | Max-width container (1440px) centered; extra whitespace on sides; product grid may expand to four columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch-target guidelines.
- Icon-only buttons (e.g., cart, search, hamburger) are at least 44x44px.
- Product card tap targets (title, image, button) are independently tappable with adequate spacing.

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px.
- Product filters collapse into a slide-out drawer on mobile.
- Footer link columns stack vertically on mobile, with accordion-style expand/collapse for each category.
- Hero content stacks (text above CTA) on mobile, with optional background image behind.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components beyond primary/secondary buttons could not be reliably extracted from the live site.
- Error state styling for form inputs (border color, error message typography) is inferred but not confirmed.
- Dark mode palette is not present on the live site; all tokens assume light mode.
- Sub-brand or collection-specific palettes (e.g., limited-edition colors) may exist but were not detected.
- The exact font-family stack is system-default; no custom brand font (e.g., a proprietary typeface) was found.
- Spacing values for padding and margins are estimated from common patterns and may not match every page exactly.
- Component heights for nav-bar and hero are based on typical DTC cookware implementations and may vary.
