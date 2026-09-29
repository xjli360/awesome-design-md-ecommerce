---
version: alpha
name: "Foreo"
source_url: "https://www.foreo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A Swedish beauty-tech brand that lives in the tension between clinical precision and playful indulgence, anchored on a deep slate #313f49 that reads as dermatological authority against a shock of #f53794 — a fuchsia that feels less like a brand color and more like a heartbeat monitor gone rogue. The typography runs exclusively in Montserrat’s full weight spectrum, from ExtraLight (used for airy product descriptions that whisper rather than shout) to Bold (reserved for benefit-driven headlines that land like a clinical finding). Every product card sits on a pure white canvas with a soft shadow, the device rendered in 3D against gradients that shift from #78278b to #dbc088, suggesting the iridescence of high-end silicone rather than flat e-commerce photography. Buttons are pill-shaped ({rounded.full}) and use the fuchsia as primary voltage, while secondary actions adopt the slate or a clean outline. The checkout flow introduces unexpected accents — #2aa9f6, #25d7ff, #00c7b1 — that signal payment success or subscription tiers with the same saturated confidence as the hero pink. The brand’s signature move is the “before/after” slider: a vertical split that uses #ff6dac as the active handle, inviting the user to drag across skin texture with a single finger. There is no hard corner on any interactive element; even the footer accordion uses {rounded.sm} on its expanded panels. The overall effect is a clinic that serves champagne — sterile enough to trust, vivid enough to remember.

colors:
  primary: "#f53794"
  primary-active: "#ef508c"
  primary-disabled: "#facce0"
  ink: "#313f49"
  body: "#54636d"
  muted: "#99a5af"
  muted-soft: "#abb7c0"
  hairline: "#d7d7d7"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f4f5f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-purple: "#78278b"
  accent-gold: "#dbc088"
  accent-blue: "#2aa9f6"
  accent-cyan: "#25d7ff"
  accent-teal: "#00c7b1"
  accent-red: "#ea4335"
  accent-pink-light: "#efbae1"
  accent-pink-hot: "#ff0062"
  accent-pink-soft: "#ff6dac"
  accent-pink-warm: "#ea4398"
  social-facebook: "#3b59b4"
  social-twitter: "#00aced"
  social-linkedin: "#6d84b4"
  social-google: "#ea4335"
  scrim: "#122330"

typography:
  display-xl:
    fontFamily: "'Montserrat-Bold', 'Montserrat', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat-Bold', 'Montserrat', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.19
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat-SemiBold', 'Montserrat', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat-Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat-SemiBold', 'Montserrat', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat-Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat-Regular', 'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat-Light', 'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat-Regular', 'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Montserrat-Light', 'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat-SemiBold', 'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat-Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Montserrat-SemiBold', 'Montserrat', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat-Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Montserrat-Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Montserrat-Regular', 'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat-Medium', 'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
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
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
  button-pill-accent:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-title:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-red}"
    rounded: "{rounded.sm}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  checkbox:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  radio:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  radio-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  toggle:
    backgroundColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 16px 40px
    height: 56px
  hero-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 12px
  before-after-slider:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  before-after-handle:
    backgroundColor: "{colors.accent-pink-soft}"
    rounded: "{rounded.full}"
    height: 40px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-accordion:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 32px
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  modal-overlay:
    backgroundColor: "{colors.scrim}"
  modal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  snackbar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
  snackbar-success:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  snackbar-error:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, rendered in the signature fuchsia #f53794 with white text and a pill shape ({rounded.full}). On hover, it shifts to a slightly deeper pink #ef508c; the disabled state uses a soft pastel #facce0. Padding is generous (14px 32px) to accommodate both single-word CTAs like “Shop” and longer strings like “Add to Bag.” The secondary variant uses a white fill with a 1px slate border, while the ghost button keeps the fuchsia text on a transparent background for use in tight layouts like product quick-adds. An accent pill variant in purple #78278b is reserved for limited-edition drops and subscription upsells.

### Cards
**`product-card`** — Every device card sits on a white background with a soft shadow and {rounded.md} corners. The product image area uses a light gray #f4f5f6 backdrop that makes the silicone textures pop. A small badge in the top-left corner carries the fuchsia primary for “NEW” or “BESTSELLER” labels, while sale badges use the accent-red #ea4335. The title runs in {typography.body-md} (Montserrat Regular, 16px), the price in {typography.title-sm} (Montserrat Medium, 16px), and the star rating in {typography.caption} (Montserrat Regular, 13px) with a muted gray. On hover, the card lifts slightly with a 4px shadow and the CTA button appears.

### Navigation
**`top-nav`** — A 72px white bar with uppercase Montserrat Medium nav links at 14px, letter-spaced 0.3px for a crisp, editorial feel. The logo sits left-aligned, typically in the slate #313f49 or the fuchsia primary. A search icon and cart icon sit on the right, both using the icon-button-circle pattern (40px, {rounded.full}, light gray background). On mobile, the nav collapses into a hamburger menu with a full-screen overlay; the dropdown panels use {rounded.sm} and a white background with slate text.

### Forms
**`text-input`** — Standard input fields use a white background, 1px hairline border #d7d7d7, and {rounded.sm} corners. On focus, the border shifts to the primary fuchsia. Error states turn the border and label text to #ea4335. The newsletter-specific input uses a pill shape ({rounded.full}) with a fuchsia submit button nested inside — a pattern used across the footer and popup modals. Checkboxes and radios use the fuchsia for checked states, with a 2px white dot or checkmark inside the filled circle or square.

### Footer
**`footer-section`** — The footer inverts the palette entirely: a slate #313f49 background with white and light gray #abb7c0 text. Links use {typography.link} (Montserrat Regular, 14px) and sit in a multi-column grid. Accordion panels on mobile expand with {rounded.sm} corners. Social icons are 32px circles with transparent backgrounds and light gray icons, turning fuchsia on hover. The newsletter input at the bottom uses the same pill-plus-button pattern as the hero, but on the dark background the input is white and the button is fuchsia.

### Hero
**`hero-section`** — Full-width sections that alternate between a light gray #f4f5f6 background and a white one. The headline uses {typography.display-xl} (Montserrat Bold, 42px) in the slate ink, with a subhead in {typography.body-md} (Montserrat Regular, 16px) in the muted gray. The primary CTA is a large pill (56px tall, 16px 40px padding) in fuchsia. A secondary badge in gold #dbc088 may appear for awards or clinical claims. The hero often includes a 3D product render on the right, floating above a subtle gradient that echoes the accent palette.

### Before/After Slider
**`before-after-slider`** — A signature Foreo component: a split-screen image comparison with a vertical divider. The handle is a 40px circle in the soft pink #ff6dac, draggable left and right. The slider track uses a 2px white line. The entire component sits inside a white card with {rounded.md} corners and a 1px hairline border. Labels (“BEFORE” / “AFTER”) appear in {typography.micro-label} (Montserrat Medium, 10px, uppercase) at the top corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text shrinks to {typography.display-md} (24px); before/after slider reduces to 100% width; footer accordions replace columns; buttons go full-width |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 50/50 split with text left and image right; footer shows 2-column grid; search bar appears in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero uses 60/40 split; footer shows 4-column grid; before/after slider sits at 80% max-width |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to 4 columns; hero uses 50/50 split with larger typography; all components center within the container |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain a minimum 44px tap target on mobile.
- Product card CTAs are at least 48px tall.
- Before/after slider handle is 40px — borderline for mobile; consider increasing to 48px on touch devices.
- Accordion headers are 48px tall for easy tapping.
- Search bar and newsletter input fields are 48px tall.

### Collapsing Strategy
- Top nav collapses to a hamburger menu below 744px; the full menu appears as a full-screen overlay with a close button.
- Footer columns collapse to accordion panels below 744px; each section (Support, Company, Social) becomes an expandable row.
- Product filters collapse to a “Filter” button that opens a bottom sheet on mobile.
- Before/after slider collapses to full-width on mobile, removing the outer card padding.
- Hero section stacks vertically on mobile: text above, image below.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only primary and primary-active colors; secondary hover states (e.g., button-secondary:hover, link:hover) were not reliably captured from the live site CSS. Assumed a 10% darken or lighten pattern where missing.
- **Error styling**: Only the error text color (#ea4335) was extracted; error icon, border width, and helper text styling are inferred from common patterns.
- **Dark mode**: No dark mode tokens were found on the live site. The brand may not support it; if it does, the palette would need a full inversion with adjusted contrast ratios.
- **Sub-brand palettes**: Foreo may have sub-brands (e.g., UFO, Luna, ISSA) with distinct accent colors. The extracted list includes many blues and pinks that could belong to sub-brand pages, but the mapping is unclear.
- **Typography scale**: Font sizes and line heights are estimated from the extracted font families and common Montserrat usage patterns; exact values from the live site CSS were not available.
- **Spacing scale**: The spacing tokens follow a standard 4px grid; actual site spacing may vary by component.
- **Animation tokens**: No transition durations, easing curves, or keyframe animations were extracted. The brand likely uses smooth 0.3s ease transitions on hover and focus states.
- **Shadow tokens**: Box-shadow values were not extracted; product cards and modals likely use subtle shadows (e.g., 0 2px 8px rgba(0,0,0,0.08)) that would need manual inspection.
- **Checkout flow**: The extracted color list includes several payment-widget colors (e.g., #003399 for PayPal, #00aced for Twitter, #ea4335 for Google) that are not part of the Foreo brand palette. These should be isolated to the checkout integration layer.
