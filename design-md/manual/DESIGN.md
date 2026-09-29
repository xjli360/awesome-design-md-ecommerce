---
version: alpha
name: "Manual"
source_url: "https://manual.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep teal canvas, #0b3b3c, wraps Manual's healthcare storefront in the calm authority of a doctor's study — not the sterile white of a clinic. This single color choice, carried from the meta theme-color through every nav bar, footer, and section background, signals that men's health here is serious, private, and handled without embarrassment. Against that dark backdrop, a warm coral accent (#db5d4b) ignites every primary CTA, badge, and progress indicator, creating a voltage that says "start here." The brand's typography splits personality: Bressay, a serif with editorial weight, appears in display roles (headlines, hero text) to borrow the credibility of a legacy men's magazine, while BasisGrotesquePro handles body copy, buttons, and labels with a clean, no-nonsense sans-serif utility. Buttons use a compact {rounded.sm} radius — friendly but not pill-soft — and sit at 48px height for confident tap targets. The product-card system layers a white surface ({colors.surface-card}) over the teal canvas, with a soft hairline (#cad7d1) that defines edges without shouting. Illustrations and iconography lean toward flat, approachable line art in #6d8a83 (a muted sage), avoiding the cartoonish or the clinical. The overall feel is that of a members' club for health: dark, warm, trustworthy, with the coral acting as the concierge who points you where to go.

colors:
  primary: "#db5d4b"
  primary-active: "#c44a3a"
  primary-disabled: "#f0b0a6"
  ink: "#0b3b3c"
  body: "#3d5c56"
  muted: "#6d8a83"
  muted-soft: "#91ab9f"
  hairline: "#cad7d1"
  hairline-soft: "#d4eae4"
  canvas: "#0b3b3c"
  surface-soft: "#f3f1ee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#f3f1ee"
  accent-coral-light: "#ff8d7d"
  accent-coral-soft: "#ff7763"
  badge-error: "#cd2026"
  badge-error-dark: "#81171b"
  badge-success: "#47bc96"
  badge-success-soft: "#d4eae4"
  star-rating: "#ffff00"
  link-blue: "#007aff"
  social-facebook: "#4267b2"
  social-warning: "#f1c40f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'bressay-display', 'bressay', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'bressay-display', 'bressay', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'bressay-display', 'bressay', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  micro-label:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'BasisGrotesquePro', 'HelveticaNeue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-error}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
    border: "1px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    border: "1px solid {colors.hairline}"
  radio-checked:
    border: "6px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-bar-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-bar-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 20px
    height: 36px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 40px
  section-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xl} 0"
  section-header-subtitle:
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  badge-status:
    backgroundColor: "{colors.badge-success-soft}"
    textColor: "{colors.badge-success}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-error:
    backgroundColor: "{colors.badge-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 8px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: "0.6"
  modal-dialog:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  modal-close:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in coral (#db5d4b) on white text. Used for "Start your visit," "Subscribe," and "Order now" actions. On hover, shifts to a deeper coral (#c44a3a). Disabled state uses a pale coral (#f0b0a6) to indicate non-interactivity. Height is 48px with 14px/28px padding, giving a solid, confident tap target.

**`button-secondary`** — An outlined variant with transparent background and a 2px coral border. Text remains coral. Used for secondary actions like "Learn more" or "View details." On hover, fills with coral and inverts text to white. Same 48px height as primary for visual alignment.

**`button-tertiary-text`** — A text-only link styled as a button, with no background or border. Used for less prominent actions like "Cancel" or "Skip." Text color is coral, and hover adds an underline effect.

**`button-ghost`** — A transparent button with white text, designed specifically for use on the dark teal canvas (#0b3b3c) in the hero and nav bar. Used for "Sign in" or "Log in" actions. On hover, adds a subtle white border.

### Forms & Inputs
**`text-input`** — Standard text input with a white background, 1px hairline border (#cad7d1), and 8px corner radius. On focus, the border thickens to 2px and turns coral. Error state swaps to a red border (#cd2026). Height is 48px with 12px/16px padding for comfortable typing.

**`select-dropdown`** — Matches the text-input styling for visual consistency. Uses a custom chevron icon in coral. The dropdown menu itself uses the same white surface with a subtle shadow.

**`checkbox`** — A small 20px square with 4px radius and a hairline border. When checked, fills with coral and shows a white checkmark icon. The label sits 8px to the right in body-md.

**`radio`** — A 20px circle with a hairline border. When selected, the inner 6px coral dot appears. The label follows the same spacing as checkboxes.

### Navigation
**`nav-bar`** — A fixed 72px bar on the deep teal canvas (#0b3b3c). Logo sits left-aligned in white, navigation links are uppercase BasisGrotesquePro at 14px/600 weight. Active links appear in coral. A primary CTA button ("Get started") sits at the far right.

**`nav-bar-link`** — Uppercase, 14px, weight 600, in white. On hover, text shifts to coral. Active state is coral. Links are padded 8px/16px for generous tap targets.

**`nav-bar-cta`** — A compact 36px primary button embedded in the nav bar. Uses button-sm typography (13px/600) and 8px/20px padding. Same coral background, white text.

### Cards
**`product-card`** — A white card with 12px radius and 24px padding, sitting on the teal canvas or a soft surface (#f3f1ee). Contains a product image (also 12px radius), title in title-md, price in coral title-sm, and a primary CTA. An optional badge sits in the top-left corner for "Best seller" or "New" labels.

**`product-card-badge`** — A small coral rectangle with 4px radius, 2px/8px padding, and uppercase 11px/700 white text. Used to flag product status.

### Badges & Indicators
**`badge-status`** — A pill-shaped badge with a soft green background (#d4eae4) and green text (#47bc96). Used for "In stock" or "Available" indicators. The full radius and compact padding make it feel like a sticker.

**`badge-error`** — A pill-shaped badge with a red background (#cd2026) and white text. Used for "Out of stock" or "Limited availability" warnings.

**`progress-bar`** — A thin 8px bar with a full radius, used in multi-step flows (e.g., quiz or checkout). The track is hairline (#cad7d1), and the fill is coral. Animates smoothly between steps.

### Accordion
**`accordion`** — A white card with 8px radius, 1px hairline border, and 16px/24px padding. The header uses title-sm (16px/600) in ink (#0b3b3c). On click, the body expands with a smooth height transition. A coral chevron icon rotates to indicate open/closed state.

### Tooltip
**`tooltip`** — A small dark bubble (#0b3b3c) with white text, 8px radius, and 6px/12px padding. Appears on hover over icons or information buttons. Positioned above or below the trigger element with a 4px arrow.

### Modal
**`modal-overlay`** — A full-screen scrim at 60% opacity, darkening the background to focus attention on the dialog.

**`modal-dialog`** — A white card with 12px radius and 32px padding. Contains a close button (a 32px circle with a soft gray background) in the top-right corner. Used for confirmations, forms, and detailed product views.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero text reduces to display-lg (36px); buttons become full-width; accordions replace tabbed content |
| Tablet | 744–1128px | Two-column product grid; nav bar shows condensed links (icons + short labels); hero uses display-xl (48px) with subheadline; side-by-side form layouts |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero uses display-xl with larger imagery; multi-column footer with link groups |
| Wide | > 1440px | Max-width container at 1280px; hero uses larger display sizes; additional whitespace around cards and sections; footer expands to four columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Nav bar links have 8px/16px padding, ensuring a 30px+ tap area
- Checkboxes and radios are 20px with an invisible 44px tap extension via padding
- Close buttons and icon buttons are 32px minimum
- Accordion headers are 48px tall for easy tapping

### Collapsing Strategy
- On mobile, the nav bar collapses to a hamburger icon; the menu slides in from the right as a full-height overlay
- Product cards stack vertically on mobile, shifting to 2-column on tablet and 3-column on desktop
- Multi-step forms collapse to a single-page scroll on mobile, with progress indicated by a compact step counter
- Footer link groups collapse into accordions on mobile, expanding on tap
- Hero sections reduce image height on mobile, prioritizing text and CTA above the fold

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components are inferred from common patterns; exact transition durations and easing curves not extracted
- Error state styling for text inputs (red border) is assumed from the badge-error color; actual error message typography and placement not confirmed
- Dark mode is not present on the live site; no dark palette tokens exist
- The extracted color list includes several likely third-party widget colors (e.g., #4267b2 for Facebook, #007aff for Apple Pay, #ffff00 for star ratings, #cd2026 for Klarna/Afterpay errors); these are included as social/utility tokens but may not be part of Manual's core palette
- Font weights for BasisGrotesquePro are inferred from the extracted font-family declarations (TTNorms-Bold, TTNorms-Medium, TTNorms-Regular suggest a weight range of 400-700); exact weight values may vary
- The serif font "bressay" and "bressay-display" are used in headlines but their exact weight and style variations are not fully documented
- Spacing values for section padding and component margins are estimated from common grid systems; exact values may differ
- The nav bar's hamburger menu icon and animation style are not extracted
- Product card shadow depth and elevation are not captured
- Loading states (spinners, skeletons) are not documented
- The checkout flow uses Shopify's default styling; Manual's custom checkout components may differ from the extracted widget colors
