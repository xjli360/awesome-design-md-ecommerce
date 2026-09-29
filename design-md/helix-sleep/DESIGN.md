---
version: alpha
name: "Helix Sleep"
source_url: "https://helixsleep.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Helix Sleep is a direct-to-consumer mattress brand that positions itself as the sleep solution for every body type and sleeping style, built on a foundation of clinical clarity and warm approachability. The brand's visual language is anchored in a clean, predominantly white canvas (`#ffffff`) that conveys purity and simplicity, allowing product photography and sleep-related imagery to take center stage. The primary brand voltage comes from a deep, restful navy blue (`#1a2a3a`) that appears across primary CTAs, navigation elements, and key accents, evoking the calm of a night sky. This is paired with a softer, more approachable teal (`#3a7b8a`) used for secondary actions and hover states, creating a subtle but distinct color story that feels both trustworthy and rejuvenating. The typography leans on a clean, highly legible sans-serif stack — likely a system font like Helvetica Neue or a similar geometric sans — with display sizes staying moderate (24–32px) and body text at 16px for comfortable reading. Generous whitespace and soft corner radii (`{rounded.sm}` at 8px for buttons, `{rounded.md}` at 12px for cards) create a friendly, non-intimidating interface that invites exploration. The brand's signature design move is the "sleep quiz" — a multi-step, personality-driven questionnaire that uses large, tappable cards with illustrations and minimal text, all set against the white canvas with the navy and teal palette providing wayfinding and progress indicators. This quiz is the heart of the Helix experience, embodying the brand's promise of personalized comfort through a guided, reassuring digital journey. The overall mood is one of calm confidence — a clinical precision softened by human-centered design, where every pixel serves the goal of better sleep.

colors:
  primary: "#1a2a3a"
  primary-active: "#2a4a5a"
  primary-disabled: "#8a9aaa"
  ink: "#1a1a2e"
  body: "#2d2d44"
  muted: "#6b6b80"
  muted-soft: "#9a9aac"
  hairline: "#d0d0dc"
  hairline-soft: "#e8e8f0"
  canvas: "#ffffff"
  surface-soft: "#f4f6f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#3a7b8a"
  accent-teal-hover: "#4a9baa"
  accent-teal-soft: "#e0f0f4"
  badge-new: "#e8a838"
  badge-sale: "#c0392b"
  star-rating: "#e8a838"
  quiz-progress: "#3a7b8a"
  quiz-progress-bg: "#e0f0f4"
  footer-bg: "#1a2a3a"
  footer-text: "#c0c8d4"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
  section: 80px

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-tertiary-active:
    backgroundColor: "{colors.accent-teal-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.primary}"
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
    border: "2px solid {colors.badge-sale}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary-active}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4/3"
  quiz-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
    border: "2px solid {colors.hairline-soft}"
  quiz-card-selected:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-soft}"
  quiz-card-hover:
    border: "2px solid {colors.accent-teal}"
  quiz-progress-bar:
    backgroundColor: "{colors.quiz-progress-bg}"
    rounded: "{rounded.full}"
    height: 8px
  quiz-progress-fill:
    backgroundColor: "{colors.quiz-progress}"
    rounded: "{rounded.full}"
    height: 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-featured:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.base}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  section-heading:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    padding: "{spacing.base} {spacing.lg}"
    typography: "{typography.title-sm}"
  accordion-content:
    padding: "{spacing.base} {spacing.lg}"
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  testimonial-quote:
    typography: "{typography.body-md}"
    fontStyle: italic
    textColor: "{colors.body}"
  testimonial-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
  comparison-table-header:
    backgroundColor: "{colors.surface-soft}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
  comparison-table-row:
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.base}"
  comparison-table-row-hover:
    backgroundColor: "{colors.surface-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Helix site, rendered in the deep navy `{colors.primary}` with white text. Used for "Shop Now", "Take the Quiz", and "Add to Cart" actions. On hover, it shifts to `{colors.primary-active}` for a subtle depth cue. The disabled state uses `{colors.primary-disabled}` to indicate inactivity while maintaining brand consistency. All primary buttons use `{rounded.sm}` for a soft, approachable corner.

**`button-secondary`** — An outlined variant with a white fill and navy border, used for "Learn More" and "Compare" actions alongside primary buttons. The active state darkens the border and adds a light background fill. This button provides a clear visual hierarchy without competing with the primary action.

**`button-tertiary`** — A teal-filled button using `{colors.accent-teal}` that serves as an alternative CTA for actions like "Start Your Quiz" or "See Details". The teal provides a warm contrast to the navy primary, signaling a different but complementary action path. Hover shifts to `{colors.accent-teal-hover}`.

**`button-pill`** — Fully rounded pill buttons used for filter toggles, quiz navigation, and compact actions. Available in filled navy and outlined variants, these buttons use `{rounded.full}` and smaller padding for tighter layouts.

### Cards
**`product-card`** — The core product display card featuring a 4:3 image area, product name, price, and a short description. Uses a white background with a subtle shadow for depth. On hover, the shadow intensifies to signal interactivity. The card is designed to work in a grid layout with consistent spacing.

**`quiz-card`** — Large, tappable cards used in the sleep quiz flow. Each card contains an illustration, a title, and a brief description. The default state shows a light border, which shifts to navy on selection and teal on hover, providing clear visual feedback for the multi-step selection process.

**`testimonial-card`** — A review card featuring a quote, author name, and star rating. Uses a white background with a soft shadow and italicized quote text for visual distinction. Designed to build trust through social proof.

### Navigation
**`nav-bar`** — A fixed top navigation bar with a white background and subtle bottom border. Contains the Helix logo, primary navigation links (Mattresses, Accessories, Quiz, Reviews), and utility icons (search, cart, account). On scroll, a light shadow replaces the border for depth. Active nav links are underlined with the primary navy color.

**`nav-link`** — Navigation text links using `{typography.nav-link}` at 15px with medium weight. Active state shows a 2px navy underline. Hover state transitions to `{colors.primary-active}` for a subtle color shift.

### Forms
**`text-input`** — Standard text input fields with a white background, light border, and 48px height for comfortable touch targets. On focus, the border thickens to 2px and shifts to navy. Error states use a red border (`{colors.badge-sale}`) for clear validation feedback.

**`select-dropdown`** — Dropdown selectors styled consistently with text inputs, used for mattress size selection and filter options. Maintains the same height and border treatment for visual consistency.

### Progress & Badges
**`quiz-progress-bar`** — A horizontal progress indicator used in the sleep quiz flow. The background is a soft teal (`{colors.quiz-progress-bg}`) with the fill in the accent teal (`{colors.quiz-progress}`). Both use `{rounded.full}` for a smooth, pill-shaped appearance.

**`badge-new`** — A gold badge (`{colors.badge-new}`) used to highlight new products or features. Uses uppercase typography at 11px with tight tracking for a premium, attention-grabbing appearance.

**`badge-sale`** — A red badge (`{colors.badge-sale}`) for sale or discount indicators. Follows the same typography and corner treatment as the new badge for consistency.

### Footer
**`footer`** — A dark navy footer (`{colors.footer-bg}`) containing link columns, social icons, and legal text. Text is rendered in a light gray (`{colors.footer-text}`) for readability against the dark background. Links shift to white on hover for clear interaction feedback.

### Accordion
**`accordion`** — Collapsible content sections used for FAQ and product details. Each accordion has a clickable header with a title and expand/collapse icon, followed by a content area. Uses a white background with a light border and soft corners.

### Comparison Table
**`comparison-table`** — A structured table used to compare mattress models side-by-side. Headers have a light gray background for visual separation, and rows have subtle bottom borders. Hover states add a light background tint for row-level interaction.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layouts, stacked product cards, hamburger menu replaces top nav, quiz cards become full-width, hero sections reduce padding to 32px, buttons become full-width, footer columns stack vertically |
| Tablet | 744–1128px | Two-column product grids, top nav collapses to show key links only, quiz cards display in 2-column grid, hero padding at 48px, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grids, full top nav with all links, quiz cards in 3-column grid, standard hero padding at 80px, footer uses 4-column layout |
| Wide | > 1440px | Max-width container at 1440px with centered content, product grids can expand to 4 columns, hero sections use larger typography scales |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px touch target height
- Quiz cards have a minimum 120px height for easy tapping
- Accordion headers have 48px minimum height for touch accessibility
- Navigation links have 44px minimum touch area, even when text is smaller
- All form inputs maintain 48px height for comfortable mobile interaction

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile, revealing a full-screen overlay with all links
- Product detail sections (specs, reviews, shipping) collapse into accordion panels on mobile and tablet
- Comparison tables convert to stacked card layouts on mobile, showing one product per row
- Multi-column footers stack to single column on mobile
- Hero sections reduce imagery size and stack text below images on mobile
- Quiz progress indicators become compact dots instead of full bars on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font-family declarations could not be extracted from the live site; the system font stack used here is an educated approximation based on common DTC bedding brand patterns
- Hover and active states for many components (especially footer links, accordion headers, and comparison table rows) are inferred from common UX patterns rather than extracted from live CSS
- Error styling for form validation (error messages, icon placement, animation) is not captured
- The sleep quiz flow has complex multi-step logic and animations that are not fully documented here
- Sub-brand palettes for different mattress models (e.g., Helix Midnight, Helix Dawn) may have distinct accent colors not captured
- Dark mode styling is not present on the live site and is not documented
- Loading states, skeleton screens, and spinner animations are not defined
- Mobile-specific navigation patterns (hamburger menu animation, overlay behavior) are high-level and lack detailed styling
- Print stylesheets and accessibility-focused high-contrast modes are not documented
- The exact hex values for the navy and teal palettes are inferred from common DTC bedding brand patterns and may not match the live site exactly
- Custom checkbox and radio button styling is not captured
- Tooltip and popover component styling is not documented
- Video player controls and styling for product videos are not defined
- The "Compare" feature's modal or overlay styling is not captured
- Newsletter signup form error and success states are not documented
- Internationalization and RTL layout support are not addressed
