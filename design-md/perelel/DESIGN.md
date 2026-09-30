---
version: alpha
name: "Perelel"
source_url: "https://perelelhealth.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A warm, doctor-informed vitamin brand that wraps reproductive health in a palette anchored on #c07859 — a sun-baked terracotta that reads as both clinical authority and maternal warmth, never clinical white. The brand pairs this with #f8f7f5 (a barely-there ivory canvas), #374151 (charcoal ink for body copy), and #676986 (a muted slate for secondary text), creating a system that feels like a calm, well-lit consultation room rather than a supplement aisle. Typography leans on Ogg Text for editorial display — a serif with soft, rounded terminals that carries the brand’s “stages of you” narrative — and Inter for UI, giving the checkout and subscription flows a clean, trustworthy rhythm. Buttons and cards use {rounded.sm} (8px) corners, a subtle softening that avoids the clinical sharpness of straight 90° edges. The subscription quiz, a signature brand moment, surfaces as a stepped modal with progress dots, each stage framed by {colors.f2e9da} (a warm almond) backgrounds and {colors.primary} accent highlights. Product cards stack a hero image, a short-form title in Ogg Text, a one-line benefit caption, and a pill-shaped “Add” CTA — the terracotta button sits on {colors.canvas} with {colors.on-primary} white text, never competing with the photography. The footer runs a dense three-column layout with legal links in {colors.muted} and a newsletter signup that mirrors the quiz’s soft, stepped interaction. There is no hard edge anywhere — even the hairline (#cdcac2) is a warm gray, not a cold silver. The brand’s visual system trusts that a woman navigating fertility, pregnancy, or postpartum doesn’t need aggressive urgency; she needs clarity, warmth, and the quiet confidence of a doctor who’s also a friend.

colors:
  primary: "#c07859"
  primary-active: "#a86445"
  primary-disabled: "#e5c5b5"
  ink: "#374151"
  body: "#4b5563"
  muted: "#676986"
  muted-soft: "#9da1a0"
  hairline: "#cdcac2"
  hairline-soft: "#e5e5eb"
  canvas: "#f8f7f5"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#f2e9da"
  accent-rose: "#a27990"
  accent-teal: "#0e7a82"
  accent-lavender: "#decde7"
  badge-new: "#805ad5"
  badge-sale: "#ff5742"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Ogg Text', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Ogg Text', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Ogg Text', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  display-serif-sm:
    fontFamily: "'Ogg Text', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono:
    fontFamily: "'DecimaMono', 'Courier New', monospace"
    fontSize: 13px
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
    opacity: 0.5
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-add:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  text-input-error:
    borderColor: "{colors.badge-sale}"
    textColor: "{colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.display-serif-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  product-card-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-stage:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  quiz-step:
    backgroundColor: "{colors.accent-warm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  quiz-progress-dot-active:
    backgroundColor: "{colors.primary}"
    height: 8px
    rounded: "{rounded.full}"
  quiz-progress-dot-inactive:
    backgroundColor: "{colors.hairline}"
    height: 8px
    rounded: "{rounded.full}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 42px
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 42px
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  search-icon:
    color: "{colors.muted}"
  accordion-trigger:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  accordion-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for “Subscribe Now,” “Add to Cart,” and quiz progression. Renders as a solid terracotta rectangle with 8px rounded corners and white Inter 600 text at 15px. On hover, shifts to `{colors.primary-active}` (#a86445). Disabled state uses `{colors.primary-disabled}` at 50% opacity, signaling an incomplete quiz step or out-of-stock variant. **`button-secondary`** — An outlined variant for “Learn More” and “Compare” actions, using the ivory canvas background with charcoal ink text and a 1px `{colors.hairline}` border. Active state fills with `{colors.surface-soft}`. **`button-tertiary-text`** — A text-only link styled as a button, used for “Skip this step” in the quiz and “View all” in product grids. Color is `{colors.primary}` with no background or border. **`button-pill-add`** — A compact, fully rounded pill for quick-add on product cards. Smaller padding (8px 20px) and 13px font size keep it unobtrusive next to product imagery.

### Cards
**`product-card`** — A white card with 8px rounded corners and no padding at the container level (image fills top). The image area uses `{rounded.sm}` on top corners only, creating a clean break between photo and text. Title renders in Ogg Text 18px serif for editorial warmth, price in Inter 16px muted slate. The quick-add CTA (`{button-pill-add}`) floats at the bottom-right of the image area on hover. **`quiz-step`** — A stepped modal card used in the subscription quiz. Background is `{colors.accent-warm}` (#f2e9da), a soft almond that distinguishes quiz content from product pages. Padding is 32px, with a progress bar of 8px pill dots (`{quiz-progress-dot-active}` for current step, `{quiz-progress-dot-inactive}` for remaining). Each step contains a serif heading, body copy, and a set of radio-style option cards.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on ivory canvas. Logo sits left (Ogg Text or wordmark), nav links center in Inter 14px medium weight. The active page or section underlines with a 2px `{colors.primary}` border. On mobile, the nav collapses into a hamburger with a slide-out drawer. **`nav-link-active`** — Underlined state for the current section (e.g., “Shop,” “Quiz,” “About”). Color shifts to `{colors.primary}`.

### Forms & Inputs
**`text-input`** — Standard form field for email, name, and address. Uses ivory background, 8px rounded corners, 16px padding, and 48px height. Focus state adds a 2px `{colors.primary-disabled}` ring. Error state swaps the ring to `{colors.badge-sale}` (#ff5742) and text to the same red. **`newsletter-input`** — A compact variant for the footer signup, 42px tall with 10px padding. Paired with `{newsletter-submit}`, a 42px terracotta button that sits flush to the right.

### Badges
**`badge-new`** — A purple (#805ad5) pill badge for new product launches. 11px uppercase Inter 600, 2px 8px padding, fully rounded. **`badge-sale`** — A red (#ff5742) pill for sale or limited-time offers. Same typography and shape. **`badge-stage`** — A warm almond (#f2e9da) badge used on the quiz to indicate life stage (e.g., “Prenatal,” “Postpartum”). Ink text for readability.

### Hero
**`hero-section`** — The top-of-page hero for landing and category pages. Full-width ivory background with 64px vertical padding. Heading uses `{typography.display-xl}` (36px Ogg Text), subheading in Inter 16px muted. A single `{hero-cta}` button (48px tall, 14px 32px padding) anchors the layout. No background image — the brand trusts product photography or a single editorial photo below the fold.

### Accordion
**`accordion-trigger`** — Used in FAQ and product detail sections. A full-width clickable row with Inter 18px semibold title, 16px vertical padding, and a chevron icon that rotates on open. **`accordion-panel`** — The expanded content area, with 16px bottom padding and Inter 14px body text.

### Search
**`search-bar`** — A fully rounded pill input for the site search (if implemented). Ivory background, 44px height, 10px 20px padding. The search icon sits left in `{colors.muted}`. On focus, the pill gets a `{colors.primary}` ring.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; quiz steps become full-screen modals; hero padding reduces to 32px; footer stacks to single column; button-pill-add becomes full-width on product cards |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; quiz steps remain modal but narrower; hero heading reduces to 28px; footer splits into 2 columns |
| Desktop | 1128–1440px | Full nav with active underline; product cards in 3-column grid; quiz steps at 600px max-width; hero at 36px heading; footer in 3-column layout |
| Wide | > 1440px | Max-width container at 1440px; hero and product grids center with generous margins; quiz steps remain centered at 600px |

### Touch Targets
- All buttons and links: minimum 44px height for tap targets (per WCAG 2.1)
- Mobile nav hamburger: 48px x 48px hit area
- Quiz option cards: 48px minimum height with 12px padding
- Accordion triggers: 48px minimum height
- Search bar: 44px height with 16px padding on mobile

### Collapsing Strategy
- Top nav: hamburger menu at < 744px; slide-out drawer from left with full nav links and a “Shop” CTA
- Product grid: 3 columns → 2 columns → 1 column
- Footer: 3 columns → 2 columns → stacked single column
- Quiz steps: modal → full-screen overlay on mobile (no background scroll)
- Hero: side-by-side text + image → stacked text above image on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components beyond primary/secondary buttons could not be reliably extracted from the live site; the above uses reasonable inferences from the extracted palette and common patterns.
- Error styling for forms (validation messages, input error icons) was not observed; the text-input error state is inferred from the extracted `#ff5742` (badge-sale) color.
- Dark mode is not present on the live site; no dark palette tokens are defined.
- Sub-brand or collection-specific palettes (e.g., “Prenatal” vs. “Postpartum” product lines) may exist but were not extracted; the accent colors (`{accent-rose}`, `{accent-teal}`, `{accent-lavender}`) are inferred from extracted hex values and may correspond to stage-specific theming.
- The extracted font list includes `Brown`, `DecimaMono`, `Helvetica`, `Inter`, `Ogg Text`, and `Poppins`; `Ogg Text` and `Inter` are used as the primary editorial and UI faces respectively, but `Brown` and `Poppins` may appear in legacy or marketing-specific contexts.
- The extracted color list includes several generic web and checkout-widget colors (e.g., `#805ad5`, `#ff5742`, `#0e7a82`); the brand’s true primary is `#c07859` (terracotta), which appears consistently across product cards, CTAs, and the quiz interface. The palette above prioritizes this and the warm ivory `#f8f7f5` as the core canvas.
- Animation and transition durations (e.g., accordion open/close, quiz step transitions) were not extracted; a default of 200–300ms ease-in-out is assumed.
