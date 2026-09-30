---
version: alpha
name: "Flylow Gear"
source_url: "https://flylowgear.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A backcountry workbench, not a fashion runway — Flylow Gear builds for the skier who wakes up at 4am for a hut traverse and doesn't want to think about their jacket until they're peeling it off by the woodstove. The brand's visual system is anchored on #b59258, a dry-brush gold that reads as aged brass or sun-bleached alpine grass rather than any kind of retail shine; it appears on primary CTAs, badge accents, and the occasional product-detail highlight, always against a canvas of #0c0c0d (near-black) or #ffffff depending on context. Secondary tones come from the extracted palette with a clear outdoor patina: #9d805a (weathered leather), #2d3f43 (deep pine), #597689 (slate sky), #5e9ca7 (ice melt), and #5f5b57 (trail dust). The typography stack pairs ChollaSlab — a sturdy, American-made slab serif with ranch-hand proportions — for display headings, with Open Sans and Source Sans 3 for body copy, creating a tension between frontier permanence and modern readability. Buttons use {rounded.sm} (8px) corners, not pills; the brand avoids softness in favor of a squared-off, tool-like honesty. Product cards sit on {surface-card} white with {hairline} borders at #dddddd, and the primary action — "Shop Men" or "Shop Women" — is always that #b59258 gold on black, a combination that feels like striking a match in the dark. The nav bar is fixed, full-width, black (#0c0c0d), with white nav links in Open Sans semibold, and the logo sits left in what appears to be a custom wordmark or ChollaSlab display. There is no gradient, no glassmorphism, no decorative illustration; every pixel earns its keep through utility and material reference.

colors:
  primary: "#b59258"
  primary-active: "#9d805a"
  primary-disabled: "#d1c352"
  ink: "#0c0c0d"
  body: "#3c323f"
  muted: "#5f5b57"
  muted-soft: "#6f6e6b"
  hairline: "#dddddd"
  hairline-soft: "#eceeef"
  canvas: "#ffffff"
  surface-soft: "#f1f3e3"
  surface-card: "#ffffff"
  on-primary: "#0c0c0d"
  on-dark: "#ffffff"
  accent-pine: "#2d3f43"
  accent-slate: "#597689"
  accent-ice: "#5e9ca7"
  accent-trail: "#5f5b57"
  badge-sale: "#c2552a"
  badge-new: "#9c5e2a"
  star-rating: "#b59258"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'ChollaSlab', 'Georgia', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ChollaSlab', 'Georgia', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ChollaSlab', 'Georgia', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'ChollaSlab', 'Georgia', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Sans 3', 'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans 3', 'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans 3', 'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Source Sans 3', 'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Source Sans 3', 'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-dark-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "2px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "3:4"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.badge-sale}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-eco:
    backgroundColor: "{colors.accent-pine}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: "500px"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "16px 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 16px 0"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in #b59258 gold on near-black text. Used for "Shop Men", "Shop Women", "Add to Cart", and primary checkout actions. On hover, shifts to #9d805a (weathered leather). Disabled state uses #d1c352 with muted text. All primary buttons use {rounded.sm} (8px) — never pills — and uppercase Open Sans 700 at 14px with 0.5px letter spacing.

**`button-secondary`** — An outlined variant with a 2px solid {ink} border on white canvas. Used for secondary actions like "View Details" or "Learn More". On hover, the background fills with {ink} and text inverts to white. Same typography and corner radius as primary.

**`button-dark`** — Solid {ink} background with white text, used on light backgrounds or hero sections where a dark CTA is needed. On hover, transitions to {primary} gold background with {on-primary} text — a signature brand move that swaps dark to gold.

**`button-pill`** — A rare pill-shaped variant used only for filter chips, category tags, or size selectors. Uses {button-sm} typography (12px uppercase) and {rounded.full}. Gold background on white.

### Navigation
**`nav-bar`** — Fixed full-width bar at 64px height, solid {ink} (#0c0c0d). Logo sits left (likely ChollaSlab wordmark in white). Nav links are Open Sans 600, 14px uppercase, white default, gold on hover/active. A search icon and cart icon sit on the right. No dropdowns visible in extracted data — likely a simple top-level nav with mega-menu on hover for categories.

**`nav-link-active`** — Gold (#b59258) text color on the active page or section. No underline or background change — the color shift alone signals state.

### Cards
**`product-card`** — White background with {rounded.sm} corners, {hairline} border (#dddddd). Contains a 3:4 aspect-ratio product image at top, then title (Open Sans 600, 16px), price (Source Sans 3, 16px), and optional badges. On hover, a subtle box-shadow lifts the card 4px. No overlay or quick-add button on hover — the brand keeps it clean.

**`product-card-sale-price`** — When a product is on sale, the price renders in #c2552a (burnt orange) to signal discount. The original price is shown with a line-through in {muted}.

### Badges
**`badge-sale`** — Small uppercase badge in #c2552a with white text, {rounded.xs} (2px) corners, 2px vertical padding and 8px horizontal. Used on product cards for sale items.

**`badge-new`** — Same structure but in #9c5e2a (warm brown), used for new arrivals.

**`badge-eco`** — Same structure but in #2d3f43 (deep pine green), used for sustainable or eco-friendly product lines.

### Forms
**`text-input`** — Standard input with 1px {hairline} border, {rounded.sm}, 44px height, 10px vertical and 14px horizontal padding. On focus, border thickens to 2px and shifts to {primary} gold. No placeholder styling extracted — likely {muted} at body-md.

**`select-input`** — Same dimensions and border as text-input, with a custom dropdown arrow (likely SVG in {ink}). Used for size, color, and sorting selections.

### Hero
**`hero-section`** — Full-width section with minimum 500px height, {ink} background, white text using {display-xl} (ChollaSlab 48px 700). Contains a headline, optional subhead in {body-md}, and a single {hero-cta} button (gold on black, larger padding at 14px 32px). Background may feature a full-bleed product or landscape image with a dark overlay.

### Footer
**`footer-section`** — {ink} background with white and {muted-soft} text. Links use Source Sans 3 600 at 14px, defaulting to #6f6e6b and shifting to gold on hover. Contains newsletter signup with a text input and gold submit button side by side. Social icons likely present but colors not extracted — probably white/gold.

### Accordion
**`accordion-header`** — Used for product details, sizing info, and FAQ sections. White background, {title-sm} typography, 16px vertical padding, bottom border of 1px {hairline}. On click, toggles open to reveal {accordion-body} with {body-sm} text and 16px bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column (or 2-column grid); hero text scales down to {display-lg} (36px); buttons become full-width; footer stacks vertically; search bar moves to a slide-out drawer |
| Tablet | 744–1128px | Nav remains visible but may condense (hide secondary links under "More"); product cards in 2-3 column grid; hero maintains full-width with centered text; side-by-side footer columns |
| Desktop | 1128–1440px | Full nav with all links visible; product cards in 3-4 column grid; hero with left-aligned text and right-aligned image; multi-column footer with newsletter inline |
| Wide | > 1440px | Max-width container (likely 1440px) centered; product cards in 4 column grid; hero may feature split layout with larger imagery; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements minimum 44px height (meets WCAG 2.1 touch target guidelines)
- Nav links have minimum 44px tap area even if text is smaller
- Product card tap target is the entire card (not just text)
- Accordion headers have 44px+ tap area
- Search bar and form inputs at 44px height

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px; menu slides in from left or right
- Secondary nav links (size guides, fit finder, etc.) collapse into a "More" dropdown on tablet
- Product filters collapse into a "Filter" button that opens a modal/drawer on mobile
- Footer columns stack vertically on mobile; newsletter input and button become full-width stacked
- Hero image may crop or reposition on mobile to maintain focal point

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only button-primary and nav-link hover states were extractable. Button-secondary, footer links, and product-card hover states are inferred from common patterns.
- **Error states**: No form validation styling (error borders, error messages) could be extracted. Likely uses a red accent (#d9534f from extracted list) but unconfirmed.
- **Dark mode**: No dark mode detected. The brand uses {ink} backgrounds extensively, so dark mode may not be a priority.
- **Sub-brand palettes**: Flylow may have seasonal or collection-specific color variations (e.g., "Flylow Women's" vs "Flylow Men's") that weren't captured.
- **Loading states**: No skeleton screens, spinners, or loading animations extracted. Likely uses a simple spinner in {primary} gold.
- **Typography scale**: Font sizes for display-xl through display-sm are inferred from ChollaSlab's typical usage in outdoor brands. Actual extracted sizes may vary — the site uses responsive font sizing.
- **Color usage**: The extracted hex list includes many Shopify widget colors (#0275d8, #5cb85c, #f0ad4e, #d9534f) that are not brand colors. These have been excluded. The true brand palette centers on #b59258, #0c0c0d, #9d805a, #2d3f43, #597689, #5e9ca7, and #5f5b57.
- **Iconography**: No icon set was extracted. The brand likely uses custom SVG icons for cart, search, account, and social media in {ink} or {primary} gold.
- **Animation**: No animation timing or easing functions extracted. Transitions likely use 200-300ms ease-in-out for color and shadow changes.
- **Typography fallbacks**: ChollaSlab is a commercial font; fallbacks to Georgia and serif are assumed. Open Sans and Source Sans 3 are confirmed from extracted font-family declarations.
