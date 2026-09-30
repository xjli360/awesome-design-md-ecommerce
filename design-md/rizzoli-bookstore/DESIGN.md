---
version: alpha
name: "Rizzoli Bookstore"
source_url: "https://www.rizzolibookstore.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep blue anchor of #003cc5 — the color of a New York evening sky just after the streetlights come on — grounds a bookstore that calls itself "the most beautiful bookstore in New York" and means it. The palette is built on a crisp white canvas (#f9fafb) and warm neutrals (#eeeeee, #aaaaaa, #888888, #777777, #555555, #444444, #111111) that let the books themselves provide the color. A secondary blue (#003399) and a deeper navy (#002476) create hierarchy, while the extracted palette reveals unexpected accents — a sage green (#c9e1bd), a pale gold (#f4daa6), a blush pink (#f9c9bf), and a muted olive (#7c7f12) — that likely appear in seasonal displays, event signage, or the store's iconic green awning and marble interior. The typography defaults to system sans-serif (Arial, Helvetica) with Font Awesome icons for navigation and social links, suggesting a site that prioritizes legibility and load speed over typographic spectacle. Buttons use a generous {rounded.sm} corner radius, and the search bar — a critical entry point for a bookstore — takes a pill shape ({rounded.full}) that echoes the classic reading lamp or the curve of a bookshelf. The overall feeling is of a well-edited library: restrained, confident, and designed to get out of the way of the merchandise.

colors:
  primary: "#003cc5"
  primary-active: "#00309e"
  primary-disabled: "#809ee2"
  ink: "#111111"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#888888"
  hairline-soft: "#eeeeee"
  canvas: "#f9fafb"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#c9e1bd"
  accent-gold: "#f4daa6"
  accent-blush: "#f9c9bf"
  accent-olive: "#7c7f12"
  deep-navy: "#002476"
  secondary-blue: "#003399"
  success: "#198754"
  info: "#0dcaf0"
  warning: "#664d03"
  danger: "#842029"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px rgba(0, 60, 197, 0.2)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-md}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-event:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  section-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action button, used for "Add to Cart", "Checkout", and "Subscribe". Rendered in the brand's deep blue {colors.primary} with white text and a comfortable {rounded.sm} corner radius. On hover/active, shifts to {colors.primary-active} for a subtle darkening effect. The disabled state uses {colors.primary-disabled} to signal unavailability without visual noise.

**`button-secondary`** — An outlined-style button for secondary actions like "View Details" or "Learn More". Uses a white background with {colors.primary} text and a 1px solid border of the same blue. Active state inverts to {colors.surface-soft} background. Height matches the primary button at 44px for consistent alignment in forms and action bars.

### Navigation
**`nav-bar`** — A clean, fixed-position top navigation bar at 64px height on white canvas. Navigation links use uppercase {typography.nav-link} at 14px with 0.5px letter-spacing for a refined, editorial feel. The active page or section link adopts {colors.primary} to anchor the user. The nav bar includes the Rizzoli logo (typically left-aligned) and a search icon (Font Awesome) on the right.

**`nav-link-active`** — The active state for navigation items, switching text color to {colors.primary} to indicate the current section or page. No underline or background change — the color shift alone provides the signal.

### Search
**`search-bar`** — A pill-shaped search input ({rounded.full}) at 48px height, styled as the primary discovery tool for the bookstore. The white background with {colors.body} text keeps the focus on the query. A magnifying-glass icon (Font Awesome) sits inside the left padding. On focus, the border shifts to {colors.primary} with a subtle blue glow (2px rgba ring) to match the text-input focus state.

### Product Cards
**`product-card`** — The standard book display card, used in grid and list views. A white background with {rounded.sm} corners, containing a book cover image (also softly rounded), the title in {typography.title-md}, author name, and price in {colors.body}. Cards sit on a {colors.surface-soft} background in grid layouts, creating a subtle separation without hard lines.

**`product-card-title`** — Book titles are set in {typography.title-md} (18px, weight 600) to stand out from the body copy. No underlines or link styling on the title itself — the entire card is clickable.

**`product-card-price`** — Prices use {typography.body-md} in {colors.body} to avoid competing with the title. Currency symbols and decimal points are included as standard.

### Badges
**`badge-new`** — A small, blush-pink ({colors.accent-blush}) badge for new arrivals. Uppercase 11px text on a compact pill shape ({rounded.xs}) with 2px vertical padding. Sits at the top-left corner of product card images.

**`badge-sale`** — A pale gold ({colors.accent-gold}) badge for discounted titles. Same dimensions and typography as the new-arrival badge, but the warm gold signals value without the urgency of a red sale tag.

**`badge-event`** — A sage green ({colors.accent-sage}) badge for books tied to in-store events, signings, or readings. The muted green connects to the brand's physical space and the idea of growth and literary community.

### Forms
**`text-input`** — Standard text input for newsletter signups, search filters, and account forms. White background, {colors.body} text, 44px height, and {rounded.sm} corners. On focus, the input gains a {colors.primary} border and a 2px blue outer ring (rgba(0, 60, 197, 0.2)) for clear keyboard focus indication.

### Footer
**`footer-link`** — Footer navigation links in {colors.muted} at 14px. On hover, they shift to {colors.primary} to maintain brand consistency. The footer typically includes sections for About, Events, Newsletter, and Social links (Font Awesome icons).

### Hero
**`hero-section`** — The full-width hero area on the homepage, typically featuring a large book display, the store's tagline, and a primary CTA. Uses the white canvas background with {spacing.section} vertical padding to create breathing room. The hero may include a subtle background pattern or texture extracted from the store's interior photography.

**`section-title`** — Section headings across the site, set in {typography.display-md} (24px, weight 700) with {spacing.lg} bottom margin. The bold weight and tight letter-spacing give headings a confident, editorial presence.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger menu; search bar reduces to icon-only; product cards stack vertically; hero section reduces padding to 32px |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; search bar full-width in header; hero uses 48px padding |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; search bar integrated into nav; hero uses 64px padding |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero may feature larger imagery |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Search bar at 48px height provides comfortable tap target
- Nav links have minimum 44px tap area even when text is smaller
- Product cards are fully tappable with no minimum height constraint

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Search bar collapses to an icon-only toggle below 744px, expanding to full-width overlay on tap
- Product grid reduces from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer links collapse into accordion-style sections below 744px
- Hero section reduces vertical padding from 64px to 32px on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for buttons and links are inferred from the primary-active color but not extracted from live CSS
- **Error styling** for form validation (red borders, error messages) not observed; danger color (#842029) is a framework default
- **Focus ring styles** inferred from common patterns; exact box-shadow values not extracted
- **Typography hierarchy** is an educated reconstruction — the site uses system fonts (Arial, Helvetica) but exact sizes, weights, and line heights are estimated from common bookstore patterns
- **Spacing system** is a standard scale; exact margins and paddings between sections not extracted
- **Dark mode** not present on the live site
- **Sub-brand palettes** for events, children's books, or rare editions not observed
- **The extracted color palette is heavily weighted toward blues and grays** — the distinctive accents (sage, gold, blush, olive) are present but their exact usage context is inferred. The brand's true primary (#003cc5) is clear, but secondary colors may be more or less prominent than estimated here
- **Font Awesome icon set** is used but specific icon choices and sizes not extracted
- **Checkout flow colors** (#198754, #0dcaf0, #5897fb) are likely from payment widgets (Shopify Pay, Klarna) and are not brand colors — they are included in the palette for reference but should not be used in brand UI
