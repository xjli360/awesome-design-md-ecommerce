---
version: alpha
name: "Arrae"
source_url: "https://arrae.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A muted, mineral palette anchored on #f3efe8 — a warm bone-white canvas that reads like unglazed porcelain, not sterile white — and punctuated by the deep, almost-black #1b1a1f that gives headlines their gravity. The brand lives in the gap between clinical and cozy: #e5e1d8 and #f7f5f0 layer as soft surfaces, while #acacac and #808080 handle secondary text with a whisper rather than a shout. Brandon Grotesque, a geometric sans with humanist warmth, carries the display weight at generous sizes, while Cardinal Fruit — a serif with calligraphic roots — appears in editorial moments that signal expertise and trust. The system avoids hard edges entirely: buttons use {rounded.full} pill shapes, cards round at {rounded.lg}, and the search bar melts into the header as a soft field rather than a rigid box. The single accent voltage is #e22828, a desaturated red that appears only in critical CTAs and sale badges — it reads as urgent but not alarmist, like a pharmacy sign in a quiet town. Product photography is the real color engine: supplement bottles in soft focus, ingredients shot on textured stone, and skin tones that span the spectrum. The typographic hierarchy is unusually flat — display and body sizes differ by only 6–8px — because the brand trusts spacing and surface contrast over size jumps to create hierarchy. The checkout flow, powered by Shopify, introduces a secondary palette of #6b3a5b (a muted plum) and #c7ccdb (a cool gray-blue) in trust badges and payment widgets, but these never bleed into the core brand experience. The overall effect is a supplement brand that feels less like a pill bottle and more like a ceramic jar on a bathroom shelf — warm, grounded, and deliberately un-loud.

colors:
  primary: "#e22828"
  primary-active: "#c41e1e"
  primary-disabled: "#f5c4c4"
  ink: "#1b1a1f"
  body: "#383635"
  muted: "#808080"
  muted-soft: "#acacac"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#f3efe8"
  surface-soft: "#f7f5f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-plum: "#6b3a5b"
  accent-slate: "#c7ccdb"
  badge-sale: "#e22828"
  star-rating: "#1b1a1f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Cardinal Fruit', 'Figtree', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Cardinal Fruit', 'Figtree', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.2px
  link:
    fontFamily: "'Cardinal Fruit', 'Figtree', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  nav-link:
    fontFamily: "'Brandon Grotesque', 'Figtree', Poppins, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.30
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-new:
    backgroundColor: "{colors.accent-plum}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-soft:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 16px 40px
    height: 56px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.surface-card}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button in the brand's desaturated red {colors.primary}. Used for "Add to Cart", "Subscribe", and primary checkout actions. On hover, shifts to {colors.primary-active} with no scale or shadow change — the brand avoids motion flourishes. Disabled state uses {colors.primary-disabled} with full opacity, signaling unavailability without hiding the button.

**`button-secondary`** — An outlined pill button on the {colors.canvas} background with a {colors.hairline} border. Used for "Learn More", "View Details", and secondary cart actions. Active state darkens the border to {colors.ink} and fills the background with {colors.surface-soft}. Never used as a primary CTA.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel", "Skip", and inline navigation. Relies on {typography.button-md} weight for affordance. Hover state adds underline via text-decoration.

**`button-pill-accent`** — A smaller pill button in the primary red, used for sale badges, promo CTAs, and sticky mobile cart buttons. Shares the same hover/disabled logic as button-primary but at a reduced height.

### Cards
**`product-card`** — A white card on {colors.canvas} with {rounded.lg} corners and no shadow — the brand relies on surface contrast rather than elevation. The image area occupies the top 60% with its own rounded corners (top-left and top-right only), and the content area below holds title, price, and a star rating. No border, no box-shadow. Hover state adds a 1px {colors.hairline} border to the card.

**`product-card-title`** — Uses {typography.title-md} in {colors.ink}, truncated to two lines. The brand avoids ellipsis overflow — instead, cards have a fixed height that accommodates the longest likely title.

**`product-card-price`** — Set in {typography.body-md} with {colors.body}. Sale prices appear in {colors.primary} with the original price struck through in {colors.muted-soft}.

### Badges
**`badge-sale`** — A small pill badge in the primary red, positioned absolutely on the top-left of product images. Uses uppercase {typography.badge} for legibility at small sizes. Never used outside of sale or discount contexts.

**`badge-new`** — A plum-colored pill badge ({colors.accent-plum}) for new product launches. Shares the same shape and typography as badge-sale but uses a different color to distinguish "new" from "sale" without relying on iconography.

**`badge-soft`** — A neutral badge on {colors.surface-soft} with {colors.muted} text, used for "Bestseller", "Doctor Recommended", or "Subscription" labels. The lowest visual priority — it reads as metadata rather than a promotion.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on {colors.canvas} with a subtle bottom border in {colors.hairline-soft}. Contains the logo (left), nav links (center), and cart icon (right). The logo uses {typography.display-md} weight but at a smaller custom size. On scroll, the bar gains a faint box-shadow (0 1px 4px rgba(0,0,0,0.06)).

**`nav-link-active`** — The currently active page link, underlined with a 2px {colors.ink} border. No background change — the brand signals location through underline alone.

**`nav-link-inactive`** — Default nav links in {colors.muted} with uppercase tracking. Hover state shifts to {colors.ink} with no underline.

### Forms
**`text-input`** — A standard text input on white background with a {colors.hairline} border and {rounded.sm} corners. Focus state swaps the border to {colors.ink}. Error state uses {colors.primary} border with a red error message below. Disabled state drops to {colors.surface-soft} background with {colors.muted-soft} text.

**`search-bar`** — A pill-shaped search field on white background with a soft border. Used in the header and on collection pages. Focus state darkens the border to {colors.ink} and may reveal a dropdown of recent searches or suggestions.

**`quantity-selector`** — A compact horizontal control with minus/plus buttons flanking a numeric display. Uses {colors.surface-soft} background and {rounded.sm} corners. Buttons are 40px tall with 32px width, and the numeric display is center-aligned.

### Footer
**`footer`** — A dark footer on {colors.ink} background with white text. Contains four columns: brand description, quick links, support links, and social icons. Links use {colors.muted-soft} and hover to white. The bottom bar holds copyright and payment method icons.

**`footer-link`** — Standard footer link in {colors.muted-soft}. Hover state transitions to {colors.surface-card} with no underline.

### Accordion
**`accordion`** — A vertically stacked disclosure component used on product pages for ingredient details, usage instructions, and FAQs. Each item has a {typography.title-md} header with a plus/minus icon on the right. Content area uses {typography.body-md} with {spacing.sm} top padding and {spacing.base} bottom padding. No animation — content appears/disappears instantly.

**`accordion-content`** — The expandable body of an accordion item. Uses {typography.body-md} in {colors.body} with generous line-height for readability.

### Trust Elements
**`rating-stars`** — Five inline star icons in {colors.star-rating} (black). Empty stars use {colors.hairline}. Stars are 16px with 2px gap. The numeric rating (e.g., "4.8") appears to the right in {typography.caption}.

**`trust-badge`** — A small rounded rectangle on {colors.surface-soft} with {colors.muted} text, used for "Free Shipping", "30-Day Guarantee", and "Made in USA" claims. These appear near the add-to-cart button and in the footer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards go single-column; hero text reduces to {typography.display-lg}; buttons become full-width; footer stacks to single column; accordions remain unchanged |
| Tablet | 744–1128px | Nav links remain visible but reduce font size to 13px; product cards display in 2-column grid; hero uses {typography.display-xl} at 30px; footer uses 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at full {typography.display-xl} size; footer in 4-column layout; maximum content width of 1128px centered |
| Wide | > 1440px | Content remains at 1128px max-width with increased side padding; hero may include background imagery at full viewport width; product cards remain 3-column but with increased gap |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and minimum width of 44px on mobile.
- Nav hamburger icon is 48px × 48px.
- Quantity selector buttons are 44px × 44px on mobile.
- Accordion headers are 48px tall to accommodate tap.
- Close buttons on modals are 44px × 44px.

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px; the hamburger icon opens a full-screen overlay menu with the same links plus account and cart.
- Product filters collapse to a "Filter" button that opens a bottom sheet on mobile.
- Footer columns collapse to a single vertical stack below 744px, with each section becoming an accordion.
- Hero section reduces padding from {spacing.section} to {spacing.xxl} on mobile, and the CTA button becomes full-width.
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile.
- Multi-step checkout collapses to a single-page layout on mobile, with sections stacked vertically.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for buttons, links, and cards were inferred from common patterns — the live site's actual hover transitions (color, shadow, scale) could not be extracted.
- **Error and validation styling** for forms (error messages, success states, tooltips) is based on convention rather than extraction.
- **Focus ring styles** (outline color, width, offset) were not visible in the extracted data — assumed to use a 2px {colors.ink} outline with 2px offset.
- **Dark mode** is not supported by the brand — no dark mode colors or media queries were found.
- **Typography scale** for body text uses Cardinal Fruit as the primary serif, but the exact fallback stack and font-weight variations (italic, bold) were not fully extractable.
- **Spacing values** for specific components (accordion padding, card gaps, grid margins) were estimated from the extracted palette and common Shopify patterns — the actual spacing tokens may differ.
- **Animation and transition durations** (button hover, accordion expand, nav scroll shadow) were not extractable — assumed 150ms ease-in-out for micro-interactions.
- **Sub-brand or collection-specific palettes** (e.g., "Bloat", "Mood", "Sleep" product lines) may have their own accent colors — only the global palette was extracted.
- **Checkout-specific styling** (Shopify checkout, Afterpay/Klarna badges) uses colors like {colors.accent-plum} and {colors.accent-slate}, but these are widget defaults and may not be brand-controlled.
- **Iconography** (cart, search, hamburger, social) was not analyzed — the brand likely uses custom SVG icons in {colors.ink} with 24px default size.
- **Typography for Cardinal Fruit** could not be fully resolved — the exact font weight (400 vs 450) and italic variant are unknown.
