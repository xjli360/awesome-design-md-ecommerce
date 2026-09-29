---
version: alpha
name: "Soft Services"
source_url: "https://softservices.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Soft Services is a body care brand that speaks in the language of clinical efficacy wrapped in sensory warmth. The brand's canvas is a barely-there off-white (`#f8f8f5`), a shade that feels like clean cotton rather than sterile white, setting the stage for a palette that moves through warm stone (`#e8e5dc`), soft clay (`#f2f1ec`), and the muted taupe of a perfectly worn-in leather jacket (`#7e736d`). A single accent of warm amber (`#bc7b02`) acts as the brand's voltage, appearing sparingly on key CTAs and product highlights, lending a sense of preciousness without shouting. The typography is a deliberate study in contrast: the serif warmth of BellMT Pro for headlines, lending a editorial, almost literary gravity, paired with the clean, modern utility of GT Eesti Light and GT Eesti Pro for body and interface text. This marriage of a warm, slightly imperfect serif with a rational sans-serif creates a brand that feels both authoritative and approachable — like a trusted dermatologist who also happens to have impeccable taste. The interface is defined by generous whitespace, soft corners (`{rounded.sm}` for buttons, `{rounded.md}` for cards), and a reliance on subtle hairlines (`#e7e5dc`) rather than heavy borders to define space. The overall mood is one of quiet confidence: the brand trusts its product photography and copy to do the heavy lifting, using color and typography as a supporting cast rather than the main event. The deep near-blacks (`#1a1a1a`, `#111111`) for body text ensure readability without the harshness of pure black, while the mid-tone grays (`#999999`, `#aaaaaa`) handle secondary information and captions with a gentle hand. This is a design system built for a brand that sells ritual and results, not hype.

colors:
  primary: "#bc7b02"
  primary-active: "#a06a02"
  primary-disabled: "#e8d5a0"
  ink: "#1a1a1a"
  body: "#111111"
  muted: "#7e736d"
  muted-soft: "#aaaaaa"
  hairline: "#e7e5dc"
  hairline-soft: "#f2f1ec"
  canvas: "#f8f8f5"
  surface-soft: "#f2f1ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#f8f8f5"
  accent-warm: "#bc7b02"
  accent-stone: "#7e736d"
  badge-new: "#bc7b02"
  badge-sold-out: "#7e736d"
  star-rating: "#1a1a1a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'BellMT Pro', 'BellMT Pro Italic', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'BellMT Pro', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'BellMT Pro', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'BellMT Pro', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02px
  title-sm:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'GT Eesti Light', 'GT Eesti Pro', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  text-input-placeholder:
    textColor: "{colors.muted-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
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
    boxShadow: "0 1px 4px rgba(0,0,0,0.05)"
  nav-link-active:
    textColor: "{colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  hero-secondary-cta:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    border: "1px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "1px solid {colors.ink}"
  search-bar-icon:
    textColor: "{colors.muted-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.badge}"
    textColor: "{colors.muted-soft}"
    marginBottom: "{spacing.base}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"
  rating-stars:
    textColor: "{colors.star-rating}"
    fontSize: 14px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "0 12px"
  toast:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 4px 24px rgba(0,0,0,0.1)"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's warm amber (`{colors.primary}`) with white text. Used for "Add to Cart", "Subscribe", and primary checkout actions. On hover, it deepens to `{colors.primary-active}`. The disabled state uses a muted gold (`{colors.primary-disabled}`) with soft gray text, signaling unavailability without visual noise. The button uses uppercase tracking (`{typography.button-md}`) and a soft 8px radius (`{rounded.sm}`), balancing approachability with a sense of considered design.

**`button-secondary`** — A ghost-style button with a subtle hairline border (`{colors.hairline}`) on the canvas background. Used for "Learn More", "View Details", and secondary navigation actions. On active state, the border deepens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`, providing clear feedback without competing with the primary button.

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Cancel" or "Skip". Relies entirely on the typography's uppercase tracking and hover color shift to `{colors.primary}` for affordance.

**`button-pill`** — A fully rounded pill variant of the primary button, used sparingly for promotional badges, subscription CTAs, or "New" indicators. The full radius (`{rounded.full}`) gives it a friendly, tactile quality that stands out from the standard buttons.

### Cards
**`product-card`** — The core product display unit, a white card with a 12px radius (`{rounded.md}`). The image sits flush at the top with rounded top corners, while the title and price stack below with `{spacing.base}` padding. A small badge (`{typography.badge}`) can overlay the image for "New" or "Sold Out" states, using the brand's amber or stone accent colors respectively. The card has no border, relying on the contrast between the white surface and the `{colors.canvas}` background for definition.

**`hero-section`** — The full-width hero area, using the canvas background and the brand's largest serif display (`{typography.display-xl}`) for headline impact. The primary CTA sits alongside a secondary outline CTA, creating a clear hierarchy. The section uses `{spacing.section}` (80px) for vertical padding, giving the content room to breathe.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, using the canvas background with a soft bottom hairline (`{colors.hairline-soft}`). Navigation links use uppercase tracking (`{typography.nav-link}`) and shift to the brand amber on hover and active states. On scroll, a subtle box-shadow replaces the hairline for a more pronounced separation.

**`nav-link-active`** — The active navigation link uses the brand's amber (`{colors.primary}`) to indicate the current section, a subtle but clear signal that doesn't overwhelm the minimal nav bar.

### Forms
**`text-input`** — A standard text input with a soft 8px radius and a hairline border. On focus, the border shifts to `{colors.ink}` for clear state indication. Error states use the brand amber (`{colors.primary}`) as the border color, a deliberate choice that avoids the typical red and maintains brand cohesion. Placeholder text uses `{colors.muted-soft}`.

**`select-input`** — Mirrors the text-input styling for consistency, used for dropdown selections like size or frequency.

**`quantity-selector`** — A compact horizontal selector with increment/decrement buttons flanking a central value display. Uses a hairline border and soft radius, with the buttons remaining transparent to keep the focus on the quantity.

### Footer
**`footer`** — A dark footer using the brand's near-black (`{colors.ink}`) as background, with light text (`{colors.on-dark}`) for maximum contrast. Links are grouped under uppercase micro-label headings (`{typography.badge}`) in `{colors.muted-soft}`, creating a clear information hierarchy. Link hover states use the brand amber for a touch of warmth in the dark expanse.

### Feedback & Overlays
**`toast`** — A dark, compact notification bar that appears at the top or bottom of the viewport. Uses the ink background with on-dark text, ensuring it stands out against any page content.

**`modal`** — A centered dialog with a white background, 12px radius, and a soft shadow. The overlay uses a 60% opacity black scrim, providing focus without completely obscuring the background.

**`accordion`** — A vertically stacked disclosure component, with each item separated by a hairline border. The title uses `{typography.title-sm}` and the content area uses `{typography.body-md}`, maintaining the brand's typographic hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; product cards stack vertically; nav bar collapses to hamburger menu; hero text reduces to `{typography.display-lg}`; buttons become full-width; footer links stack; accordion becomes default for product details |
| Tablet | 744–1128px | Two-column product grid; nav bar shows condensed links; hero maintains two-column layout with reduced padding; search bar remains visible but compact |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero uses full `{typography.display-xl}`; standard padding and spacing applied |
| Wide | > 1440px | Max-width container (1440px) with centered content; product grid can expand to four columns; hero uses larger padding for breathing room |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons and quantity selector buttons use 40px minimum touch area
- Nav bar links use 48px touch height on mobile
- Product card CTAs are full-width on mobile for easy tapping

### Collapsing Strategy
- Top nav collapses to a hamburger menu on mobile (< 744px), with a slide-out drawer for navigation links
- Product filters collapse into a "Filter" button that opens a modal or bottom sheet on mobile
- Footer link groups collapse into accordions on mobile to save vertical space
- Product image galleries switch from row to single-image swipe on mobile
- Multi-column text layouts collapse to single column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary buttons have confirmed active states
- Error styling for form validation (beyond the text-input error border) is not confirmed; error messages, icons, and inline validation patterns are inferred
- Dark mode is not present on the live site; all tokens assume light mode only
- Sub-brand or seasonal palette variations (e.g., limited edition colors) are not captured
- Animation and transition timing values (ease, duration) were not extractable from static analysis
- Iconography system (stroke weights, sizes, icon set) is not documented; only functional icons (search, cart, menu) are assumed
- Typography scale for mobile (reduced sizes) is inferred from responsive behavior, not extracted
- Spacing values for specific components (e.g., product card internal padding) are estimated based on visual inspection
- The `BellMT Pro Italic` font declaration suggests an italic variant exists, but its usage (headlines, quotes, emphasis) is not confirmed
- Accessibility contrast ratios for text on colored backgrounds (e.g., `{colors.primary}` on `{colors.canvas}`) have not been verified
- Loading states (skeleton screens, spinners) are not documented
- The Shopify platform integration may introduce platform-specific components (cart drawer, checkout button) that are not captured
