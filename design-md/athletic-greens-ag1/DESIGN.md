---
version: alpha
name: "Athletic Greens (AG1)"
source_url: "https://drinkag1.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep green wellness system that uses a single saturated accent — #0070f3, a vivid cobalt — to cut through an otherwise monochrome interface of black, white, and gray. The brand's visual identity is built on clinical precision: a dark ink (#000000) for headlines, a clean white canvas (#ffffff), and hairline-thin borders (#e5e7eb) that segment information without visual noise. Typography runs system-native (-apple-system, sans-serif) at modest sizes — body text sits at 16px with generous line-height (1.6), while display headlines scale to 36px with tight tracking (-0.5px). The cobalt primary appears exclusively in CTAs and interactive elements, never decorative; it's the single voltage that signals action. Cards use a soft 12px radius ({rounded.md}), buttons are pill-shaped at 8px ({rounded.sm}), and the overall spacing grid favors 24px and 48px increments ({spacing.lg}, {spacing.xxl}) — a rhythm that feels clinical but not cold. The brand trusts white space and scientific language over illustration or photography; there are no hero images, only structured content blocks. This is a supplement brand that behaves like a SaaS dashboard: clean, data-forward, and built for subscription conversion.

colors:
  primary: "#0070f3"
  primary-active: "#005cc5"
  primary-disabled: "#a0c4ff"
  ink: "#000000"
  body: "#1a1a2e"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#10b981"
  warning: "#f59e0b"
  error: "#ef4444"
  badge-green: "#059669"
  badge-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase

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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
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
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
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
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-lg}"
    textColor: "{colors.muted}"
  feature-list:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  feature-item:
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  pricing-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  pricing-card-featured:
    border: "2px solid {colors.primary}"
    boxShadow: "0 8px 24px rgba(0,112,243,0.12)"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in cobalt blue (#0070f3) with white text. Uses 12px horizontal padding and 48px height for comfortable tap targets. On hover, shifts to a darker shade (#005cc5). Disabled state fades to a pale blue (#a0c4ff) with reduced opacity. The 8px radius ({rounded.sm}) is consistent across all form controls.

**`button-secondary`** — Outlined variant with a 2px hairline border on white background. Text remains black (#000000). Active state thickens the border to black and adds a soft surface tint (#f9fafb). Used for "Learn More" and secondary subscription actions.

**`button-text`** — Borderless text button in primary blue. No background, no padding constraints — used for inline actions like "Skip this step" or "View details." Hover state adds a subtle underline.

**`button-pill-primary`** — Fully rounded variant for promotional badges or compact CTAs. Uses smaller font (14px) and tighter padding (10px 20px). Appears in subscription upsells and feature highlights.

### Form Controls
**`text-input`** — Standard 48px input with 1px hairline border and 12px horizontal padding. On focus, the border doubles to 2px and shifts to primary blue. Error state uses red (#ef4444). Placeholder text is muted-soft (#9ca3af). All inputs share the same 8px radius and consistent spacing.

**`select-input`** — Matches text-input dimensions exactly. Uses native dropdown styling with a custom chevron in primary blue. The dropdown panel inherits the same border and radius tokens.

**`checkbox`** — 20px square with 2px hairline border and 4px radius. Checked state fills with primary blue. Used in consent forms and subscription preference toggles.

### Cards
**`product-card`** — White card with 12px radius and a soft hairline border. Contains 24px padding on all sides. On hover, the border darkens and a subtle shadow (0 4px 12px rgba(0,0,0,0.08)) lifts the card. Used for product features, ingredient highlights, and subscription tier displays.

**`testimonial-card`** — Soft gray background (#f9fafb) with matching radius and padding. No border — relies on the surface contrast alone. Contains quote text, author name, and optional star rating.

**`pricing-card`** — White card with 32px padding and a hairline border. Featured variant gains a 2px primary-blue border and a blue-tinted shadow. Used in the subscription comparison table.

### Navigation
**`nav-bar`** — Fixed 72px white bar with a 1px bottom hairline. Contains logo (left), navigation links (center), and CTA button (right). Active links display a 2px primary-blue bottom border. On scroll, the bar gains a subtle shadow.

**`nav-link`** — 14px medium-weight text with 1.4 line-height. Inactive links are muted (#6b7280). Active links shift to primary blue with an underline indicator.

### Badges
**`badge`** — Green (#059669) pill with 11px uppercase bold text. Used for "New," "Best Seller," and "Limited Edition" labels. Tight padding (2px 8px) keeps them compact.

**`badge-outline`** — Transparent variant with a hairline border and muted text. Used for secondary labels like "Subscription" or "One-Time Purchase."

### Footer
**`footer`** — Full-width black (#000000) section with white text. Links are muted-soft (#9ca3af) and shift to white on hover. Uses 64px vertical padding and 24px horizontal. Contains four columns: product links, company info, support, and social icons.

### Progress & Feedback
**`progress-bar`** — 8px tall pill-shaped track in soft gray (#f3f4f6). Fill is primary blue. Used in onboarding flows and subscription progress indicators.

**`tooltip`** — Black background with white text, 4px radius, and minimal padding. Appears on hover for feature explanations and scientific claims.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero padding reduces to 32px; cards stack vertically; footer columns collapse to 2 |
| Tablet | 744–1128px | Two-column grid for features; nav links visible but condensed; hero uses 48px padding; pricing cards in 2-column layout |
| Desktop | 1128–1440px | Full layout with 3-column grids; nav bar at 72px with all links; hero uses 64px padding; pricing cards in 3-column layout |
| Wide | > 1440px | Max-width container at 1280px; content centered; increased whitespace around hero and feature sections |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain minimum 44px height for touch accessibility
- Checkboxes and radio buttons are 20px with 12px touch padding
- Nav links have 48px tap area even when text is smaller
- Accordion headers are 48px minimum height

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Multi-column feature grids collapse to single column below 744px
- Footer columns reduce from 4 to 2 below 744px
- Pricing cards stack vertically below 744px
- Hero section reduces padding from 64px to 32px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted from the live site; inferred from common patterns
- Error states for forms (validation messages, error icons) not observed
- Dark mode palette not present on the live site
- Sub-brand or seasonal color variants (e.g., limited edition packaging) not documented
- Animation and transition timing values (durations, easing curves) not extracted
- Icon set and illustration style not captured; only system fonts observed
- Modal/dialog overlay styling (scrim opacity, close button placement) not available
- Loading states (skeleton screens, spinners) not documented
- The extracted hex colors (#0070f3, #3291ff) appear to be a generic web palette (blue tones only) — the brand's true identity may include additional colors not captured in the extraction. The primary (#0070f3) is used as the most distinctive accent available.
