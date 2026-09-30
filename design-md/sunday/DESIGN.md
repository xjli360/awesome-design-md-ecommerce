---
version: alpha
name: "Sunday"
source_url: "https://www.getsunday.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep chlorophyll-dark green (#001c0e) floods the header and hero panels of getsunday.com the way a healthy lawn overtakes bare soil — completely, without apology. Where most outdoor brands default to sunny yellows or sky blues, Sunday anchors its entire interface in this near-black green, letting it serve as both navigation chrome and emotional signal: this is a brand that lives in the biology of grass, not the lifestyle photography around it. Typography splits into two clear voices — Lora, a bracketed serif, handles display headlines with an editorial warmth that echoes seed-catalog typography, while Inter carries every UI label, body paragraph, and call-to-action with Swiss neutrality. The pairing reads as "science journal meets garden journal," which maps precisely to Sunday's positioning as a soil-test-driven, custom-nutrient-plan lawn service. Buttons wear the brand's dark green at full saturation with white text (`{colors.on-primary}`), rounded to `{rounded.sm}` — not pill-shaped, not sharp, just enough softness to feel approachable without drifting into playful. Product cards for nutrient pouches and pest-control bottles sit on a warm off-white canvas (`{colors.canvas}`) with generous `{spacing.lg}` gutters, and the overall density is deliberately low: Sunday sells a subscription that replaces dozens of hardware-store trips, so the page itself must feel unhurried. Accent greens (`{colors.accent-leaf}`) appear sparingly on badges, progress indicators, and plan-status chips, providing a lighter counterpoint to the dominant dark. Photography dominates above-fold real estate — overhead shots of lawns, close-ups of soil, macro grass blades — and the UI recedes behind generous whitespace and restrained type scale, trusting the imagery to carry desire while the system handles clarity.

colors:
  primary: "#001c0e"
  primary-active: "#002e17"
  primary-disabled: "#6b8a7a"
  accent-leaf: "#3d8c5c"
  accent-leaf-soft: "#d4eadd"
  ink: "#001c0e"
  body: "#2c3e35"
  muted: "#5f7a6d"
  muted-soft: "#8fa89a"
  hairline: "#d6ddd9"
  hairline-soft: "#e8edea"
  canvas: "#faf9f7"
  surface-soft: "#f2f1ee"
  surface-card: "#ffffff"
  surface-dark: "#001c0e"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#c13515"
  success: "#1a7a3d"
  warning: "#b8860b"

typography:
  display-xl:
    fontFamily: "'Lora', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 44px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.1px
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  button-lg:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  label:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  overline:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
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
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: 2px solid {colors.primary-active}
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-label:
    typography: "{typography.label}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.xs}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    height: 64px
    boxShadow: 0 1px 3px rgba(0,28,14,0.12)
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    boxShadow: 0 1px 4px rgba(0,28,14,0.06)
  product-card-hover:
    boxShadow: 0 4px 16px rgba(0,28,14,0.10)
    transform: translateY(-2px)
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: 1 / 1
    objectFit: cover
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 560px
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
    maxWidth: 680px
  hero-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-dark}"
    opacity: 0.85
    maxWidth: 520px
  lawn-plan-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: 2px solid {colors.accent-leaf}
  lawn-plan-badge:
    backgroundColor: "{colors.accent-leaf}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  soil-quiz-step:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    maxWidth: 600px
  progress-bar-track:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 6px
  progress-bar-fill:
    backgroundColor: "{colors.accent-leaf}"
    rounded: "{rounded.full}"
    height: 6px
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs}"
    height: 40px
  subscription-toggle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
  testimonial-avatar:
    rounded: "{rounded.full}"
    height: 48px
    width: 48px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    opacity: 0.75
  badge-organic:
    backgroundColor: "{colors.accent-leaf-soft}"
    textColor: "{colors.accent-leaf}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons

**`button-primary`** — Full dark-green (#001c0e) background with white text set in Inter 600. The default height is 48px with 8px border radius, giving a grounded, confident feel without the playfulness of a pill shape. On hover, the background lightens slightly to `primary-active`; disabled state desaturates to a grey-green at reduced opacity. Used for all primary conversion actions: "Get My Plan," "Add to Cart," "Start Quiz."

**`button-secondary`** — White/canvas background with a 2px dark-green border and matching text color. Same dimensions as primary. Used alongside primary buttons for lower-priority actions like "Learn More" or "See Ingredients." On hover, the background shifts to `surface-soft` and the border darkens.

**`button-tertiary`** — Text-only with underline, no background or border. Compact padding, used inline within content blocks for navigational links that need more emphasis than a plain anchor but less weight than a bordered button.

### Navigation

**`nav-bar`** — Full-bleed dark green (#001c0e) bar at 72px height. Logo sits left in white; navigation links in Inter 500 at 15px appear center or right. The dark-on-dark treatment means the nav blends with hero sections that share the same background, creating a seamless top-of-page experience. On scroll, height compresses to 64px with a subtle shadow appearing beneath.

### Product Cards

**`product-card`** — White card with 12px radius, a barely-visible border in `hairline-soft`, and a whisper of box shadow. Product imagery fills a 1:1 square at the top with `rounded-sm` corners. Below the image: product name in `title-sm`, a one-line description in `body-sm` at `muted` color, and price in `title-md`. On hover, the card lifts 2px with an expanded shadow, signaling interactivity without animation excess.

### Hero Section

**`hero-section`** — Immersive dark-green background panel, typically full-viewport or near it (min 560px height). Large serif headlines in Lora 700 at 56px anchor the left or center, with a subheading in Inter at reduced opacity beneath. A primary CTA button sits below with generous top margin. Background photography (lawn aerial shots, soil close-ups) may underlay with a dark gradient overlay to maintain text legibility.

### Lawn Plan Card

**`lawn-plan-card`** — The signature conversion component. White card with a 2px accent-leaf green border that distinguishes it from standard product cards. Contains a personalized plan summary — lawn size, nutrient recommendations, shipment schedule. A small pill badge (`lawn-plan-badge`) in solid green marks the plan tier. Interior spacing is generous at 24px padding to let the data breathe.

### Soil Quiz / Onboarding Steps

**`soil-quiz-step`** — Centered card (max 600px) on the warm canvas background. Each quiz step contains a question in `display-sm` Lora, answer options as large tappable tiles (not radio buttons), and a progress bar at top. The progress bar uses `accent-leaf` for the filled portion against a light gray track, both pill-shaped at `rounded-full`.

### Subscription Toggle

**`subscription-toggle`** — Segmented control for one-time vs. subscription pricing. Inactive segments sit on `surface-soft`; the active segment snaps to `primary` with white text and full-pill radius. The component is 40px tall and compact enough to sit inline with pricing information on product pages.

### Testimonials

**`testimonial-card`** — White card with soft border, holding a quote in `body-md` italicized, a circular avatar at 48px, and attribution in `caption`. Cards arrange in a horizontal scroll on mobile or a 3-column grid on desktop.

### Footer

**`footer`** — Matches the nav's dark-green background, creating a visual bookend. Four columns of links in `body-sm` at 75% opacity, a newsletter signup input with `button-primary` inline submit, and legal/certification badges along the bottom row. Generous vertical padding (`section` spacing) keeps it from feeling cramped.

### Badges

**`badge-organic`** — Small uppercase label (Inter 700, 12px, 1px letter-spacing) on a soft green background with darker green text. Used on product cards and plan details to flag certifications, ingredient highlights, or seasonal availability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Hero headline drops to `display-md` (32px). Nav collapses to hamburger with slide-out drawer. Product cards stack vertically at full width. Soil quiz steps remain centered but gain more vertical padding. Footer columns stack to single column with accordion expand. |
| Tablet | 744–1128px | Two-column product grid. Hero headline at `display-lg` (44px). Nav links may partially show or remain in hamburger depending on count. Lawn plan card sits at ~80% width centered. Testimonials show 2-up. |
| Desktop | 1128–1440px | Three-column product grid. Full nav links visible. Hero section gains side-by-side text+image layout. Footer shows all four columns inline. Soil quiz remains max-width 600px centered. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Additional lateral whitespace on canvas background. Hero imagery may extend full-bleed while text content stays within max-width container. |

### Touch Targets

- All interactive elements maintain 44px minimum touch target on mobile, even if visually smaller
- Product card tap zones extend to full card area, not just the text or image
- Quiz answer tiles are at minimum 56px tall for comfortable thumb tapping
- Nav hamburger icon padded to 48×48px hit zone

### Collapsing Strategy

- Navigation links collapse into a hamburger menu below 744px, with a full-height slide-out panel on dark green background
- Product grids move from 3 → 2 → 1 columns as viewport narrows
- Hero layouts shift from side-by-side (text + image) to stacked (image above, text below) at tablet breakpoint
- Footer columns collapse into expandable accordions on mobile, with section headers as toggle triggers
- Subscription toggle maintains its pill shape but expands to full container width on mobile for easier tapping

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only a single hex color (#001c0e) was extracted from the live site; the full palette (accent greens, canvas warmth, muted tones) is inferred from the dark-green primary and standard UI needs — these should be verified against the live rendering
- No additional brand colors (e.g., seasonal accent, error/warning states) could be confirmed from extraction
- Font weights and specific size scales for Inter and Lora are estimated from typical usage patterns — the site likely loads these via JS bundles that were not captured
- Icon system (line weight, size grid, custom vs. library) could not be determined
- Motion/animation tokens (easing curves, transition durations) are not documented
- Exact spacing values between components on the live site could not be measured from extraction alone
- Whether Lora is used purely for display or also for longer editorial content is uncertain
- Dark-mode or alternate theme existence could not be confirmed
