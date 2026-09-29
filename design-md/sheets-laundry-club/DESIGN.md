---
version: alpha
name: "Sheets Laundry Club"
source_url: "https://sheetslaundryclub.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy #18213f anchors the brand like a concentrated detergent cap — it’s the background for the entire header, footer, and every product-card frame, creating a dark, high-contrast stage for the electric green #34bd4d that signals “eco-friendly” without resorting to pastels. That green, a saturated lime with no yellow cast, appears on the primary CTA buttons, subscription badges, and the brand’s signature leaf icon, while a secondary accent of #19adde (a clean cyan) handles informational badges and secondary links. The typography runs on Archivo for display and Quicksand for body — Archivo Black at heavy weights (900) in the logo and section titles gives a bold, slightly compressed headline presence, while Quicksand at 400–600 in body copy keeps reading light and friendly. Cards and buttons use a consistent {rounded.sm} 8px radius — not pill-shaped, not sharp — a middle ground that feels approachable without being cute. The checkout flow and subscription toggle use a warm gold #eab000 for savings badges and price highlights, a deliberate warmth against the cool navy-green palette. White canvas (#ffffff) is reserved for product photography backgrounds and the main content area, while #efefef and #f1f3f5 provide soft surface alternates for tiered subscription cards and FAQ accordions. The brand’s voice is direct and slightly playful — “Laundry made simple” — and the design follows suit: generous whitespace, clear hierarchy, and a color system that never needs to explain itself.

colors:
  primary: "#34bd4d"
  primary-active: "#2a9e3e"
  primary-disabled: "#a3e0ad"
  ink: "#18213f"
  body: "#292929"
  muted: "#707070"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#19adde"
  accent-gold: "#eab000"
  accent-purple: "#7944a3"
  accent-red: "#da3c3c"
  badge-green: "#37b679"
  badge-pink: "#ff379c"
  footer-bg: "#18213f"
  footer-text: "#9ca3af"

typography:
  display-xl:
    fontFamily: "'Archivo Black', Archivo, 'Segoe UI', Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Archivo Black', Archivo, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Archivo', 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Quicksand', 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Quicksand', 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Quicksand', 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Quicksand', 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Quicksand', 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Quicksand', 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Quicksand', 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Quicksand', 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Quicksand', 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Quicksand', 'Segoe UI', Roboto, sans-serif"
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  badge-savings:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-eco:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.badge-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-lg}"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  subscription-toggle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 16px 0
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand’s signature green #34bd4d and white text. Used for “Subscribe Now”, “Add to Cart”, and “Get Started”. On hover, shifts to `{colors.primary-active}` (#2a9e3e). Disabled state uses a muted green `{colors.primary-disabled}` (#a3e0ad). All variants share an 8px `{rounded.sm}` radius.

**`button-secondary`** — White background with navy #18213f text, outlined by a 1px hairline. Used for “Learn More” and “View Details” alongside primary buttons. Hover adds a subtle shadow.

**`button-outline`** — Transparent background with a 2px green border matching `{colors.primary}`. Text is green. Used for secondary actions in dark hero sections where a white button would clash.

### Cards
**`product-card`** — White card with an 8px `{rounded.sm}` radius, a 1px `{colors.hairline}` border, and 16px padding. Contains a product image (full-width, `{rounded.sm}` top corners), title in `{typography.title-md}`, price in `{typography.body-md}`, and a row of badges. Hover state elevates with a subtle box-shadow.

**`product-card-image`** — The image container within a product card. Maintains a 1:1 aspect ratio for laundry sheet boxes. Background is white to handle transparent product renders.

### Badges
**`badge-savings`** — Gold #eab000 background, navy text. Used on subscription pricing to highlight “Save 20%” or “Best Value”. Compact at 2px 8px padding with `{rounded.xs}`.

**`badge-eco`** — Green #37b679 background, white text. Used for “Eco-Friendly”, “Plant-Based”, “Biodegradable” labels.

**`badge-new`** — Pink #ff379c background, white text. Used for new product launches or limited editions.

### Navigation
**`nav-bar`** — Fixed top bar, 72px tall, filled with `{colors.ink}` (#18213f). Logo sits left (white text, Archivo Black), nav links center in `{typography.nav-link}` white, cart icon right. On mobile, links collapse into a hamburger menu with a white icon.

### Forms
**`text-input`** — White background, 48px height, 8px `{rounded.sm}`, 1px `{colors.hairline}` border. Focus state uses a 2px `{colors.primary}` border. Placeholder text in `{colors.muted}` (#707070). Used for email signup, search, and address fields.

### Footer
**`footer-section`** — Full-width navy #18213f background, text in `{colors.footer-text}` (#9ca3af). Contains logo, link columns, social icons, and a newsletter signup. Links use `{typography.link}` and turn white on hover.

**`footer-link`** — Standard footer link in muted gray, underlined on hover.

### Hero
**`hero-section`** — Full-width section with navy #18213f background and white text. Displays a headline in `{typography.display-lg}` (Archivo Black, 36px), a subheadline in `{typography.body-md}`, and a `button-primary` CTA. May include a background pattern or product photo overlay.

### Subscription Toggle
**`subscription-toggle`** — A segmented control for choosing between one-time purchase and subscription. Inactive segments use `{colors.surface-soft}` (#f9f9f9) with `{colors.body}` text. Active segment uses `{colors.primary}` green with white text. All segments share `{rounded.sm}` and 8px 16px padding.

**`subscription-toggle-active`** — The selected segment in the toggle, highlighted green.

### Accordion
**`accordion-header`** — Clickable header for FAQ or product details. Uses `{typography.title-md}` in `{colors.ink}`, with a plus/minus icon on the right. Padding 16px top and bottom, no horizontal padding within a container.

**`accordion-body`** — Expandable content area below the header. Uses `{typography.body-md}` in `{colors.body}`, with 16px bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav links collapse to hamburger menu. Product cards stack in single column. Hero text reduces to 28px. Subscription toggle becomes full-width. Footer columns stack. |
| Tablet | 744–1128px | Product cards display in 2-column grid. Nav links remain visible but condensed. Hero text at 32px. Footer in 2-column layout. |
| Desktop | 1128–1440px | Full layout: 3-column product grid, expanded nav, hero at 36px. Footer in 4-column layout. |
| Wide | > 1440px | Max-width container (1440px) centered. Product grid can expand to 4 columns. Hero text at 48px. |

### Touch Targets
- All buttons and links have a minimum touch target of 44x44px.
- Nav hamburger icon is 48x48px.
- Subscription toggle segments are at least 48px tall.
- Accordion headers are 48px tall for easy tapping.
- Cart icon in nav is 44x44px.

### Collapsing Strategy
- Primary nav links collapse into a hamburger menu below 744px.
- Product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile).
- Footer columns collapse from 4 → 2 → 1 as viewport shrinks.
- Hero section reduces font size and may stack CTA buttons vertically on mobile.
- Subscription toggle becomes a full-width stacked layout on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs, links, and secondary buttons could not be reliably extracted from the live site. The active state for `button-primary` (#2a9e3e) is an estimate based on a 15% darkening of the primary.
- Error styling for form validation (border colors, error message typography) is not available.
- Dark mode is not present on the live site and has not been designed.
- The exact font sizes for `display-xl`, `display-lg`, and `display-md` are inferred from typical Archivo Black usage at 48px, 36px, and 28px — the live site may use slightly different values.
- Line heights and letter spacing for typography tokens are estimated based on standard web typography best practices for these font families.
- The extracted color list includes many Shopify and third-party widget colors (e.g., #0070f3, #ff0080, #7928ca) that are not part of the brand’s design system. These have been excluded from the palette.
- The brand’s secondary accent colors (cyan #19adde, gold #eab000, purple #7944a3) appear in badges and links but their exact usage rules are inferred from context.
- The `subscription-toggle` component’s active/inactive states are based on common patterns — the live site may use a different visual treatment.
- The `accordion` component’s animation duration and icon rotation are not specified.
