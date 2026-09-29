---
version: alpha
name: "Cabinet Health"
source_url: "https://cabinethealth.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A muted, clinical warmth defines Cabinet Health, where a primary of #0099ff — a clean, aqueous blue that reads more like a purified lab reagent than a lifestyle pastel — sits atop a grayscale spectrum anchored by #3c3c3c ink and #f7f7f7 canvas. The brand's visual language rejects the bright, frantic optimism of traditional OTC packaging in favor of a quiet, considered precision: secondary accents of #f39f52 (a warm, almost medicinal amber) and #fbf0a5 (a pale, buttery highlight) appear sparingly, like safety markings on a piece of laboratory equipment. Typography relies on Messina Sans Web, a geometric sans-serif with a subtle humanist warmth, set at modest weights — the brand trusts generous whitespace and a restrained palette to convey authority, not typographic volume. Rounded corners are present but never pill-like; {rounded.sm} (8px) on buttons and {rounded.md} (12px) on cards suggest a soft, approachable interface that still maintains a clinical edge. The color #cce3eb appears as a soft, icy blue surface tint, evoking the clean, sterile environment of a pharmacy counter, while #b1d3f2 and #5288ba provide a secondary blue hierarchy for links and secondary actions. The overall effect is one of a brand that has stripped away the noise of the medicine aisle — no bold claims, no bright reds or oranges — and instead presents a calm, trustworthy interface for a product that asks you to reconsider a mundane, everyday purchase.

colors:
  primary: "#0099ff"
  primary-active: "#007acc"
  primary-disabled: "#b1d3f2"
  ink: "#3c3c3c"
  body: "#5e5e5e"
  muted: "#b8b8b8"
  muted-soft: "#cce3eb"
  hairline: "#b8b8b8"
  hairline-soft: "#e0e0e0"
  canvas: "#f7f7f7"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#f39f52"
  accent-highlight: "#fbf0a5"
  accent-gold: "#cab667"
  link-blue: "#5288ba"

typography:
  display-xl:
    fontFamily: "'Messina Sans Web Regular', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Messina Sans Web Regular', 'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Messina Sans Web SemiBold', 'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Messina Sans Web SemiBold', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Messina Sans Web Regular', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Messina Sans Web Regular', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Messina Sans Web Regular', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Messina Sans Web Regular', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Messina Sans Web SemiBold', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Messina Sans Web SemiBold', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Messina Sans Web Regular', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Messina Sans Web Regular', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Messina Sans Web SemiBold', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
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
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-accent-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-badge:
    backgroundColor: "{colors.accent-highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-sale:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with {colors.primary} (#0099ff) and white text. Used for "Subscribe Now", "Add to Kit", and primary checkout flows. On hover, shifts to {colors.primary-active} (#007acc). The disabled state uses {colors.primary-disabled} (#b1d3f2), a pale, desaturated blue that signals unavailability without visual noise. Padding is generous at 14px 28px, with {rounded.sm} (8px) corners that feel soft but not overly friendly.

**`button-secondary`** — An outlined variant on a white canvas with {colors.ink} text. Used for "Learn More" and secondary actions. The border is 1px solid {colors.hairline} (#b8b8b8). Hover state adds a subtle shadow or a 2px border in {colors.primary}. The height matches the primary button at 48px for consistent alignment in forms.

**`button-tertiary-text`** — A text-only link styled as a button, using {colors.primary} for the text. Used for "View Details" and "See All" links within cards or sections. No background or border; the text color is the only affordance.

**`button-accent-amber`** — A warm accent button using {colors.accent-amber} (#f39f52) as the background with {colors.ink} text. Used sparingly for promotional CTAs or limited-time offers. Smaller padding (10px 20px) and {typography.button-sm} to differentiate it from the primary action.

### Cards
**`product-card`** — A white card on {colors.surface-soft} (#f2f2f2) canvas. The image area uses {rounded.md} (12px) on the top corners only, creating a subtle floating effect. The card body contains the product name in {typography.title-sm}, a short description in {typography.body-sm}, and a price in {typography.title-md}. A {colors.accent-highlight} (#fbf0a5) badge may appear for "Best Seller" or "Refill" labels.

**`product-card-badge`** — A small, uppercase label with {colors.accent-highlight} background and {colors.ink} text. Used to denote "New", "Best Seller", or "Refill". The {rounded.xs} (4px) corners and tight padding (4px 8px) keep it unobtrusive.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height, white background, with left-aligned logo and right-aligned navigation links. Links use {typography.nav-link} (15px, regular weight) with {colors.muted} (#b8b8b8) for inactive states and {colors.primary} for the active state. A "Shop" dropdown may appear on desktop, with a subtle {colors.hairline} divider.

### Forms
**`text-input`** — A standard input field with a 1px {colors.hairline} border, {rounded.sm} (8px) corners, and 12px 16px padding. On focus, the border thickens to 2px and switches to {colors.primary}. The placeholder text uses {colors.muted} (#b8b8b8). Used for email capture, search, and address forms.

**`search-bar`** — A dedicated search input with a magnifying glass icon on the left. The field is 48px tall with {rounded.sm} corners. On focus, the border becomes {colors.primary}. The placeholder reads "Search medications..." in {colors.muted}.

### Footer
**`footer`** — A dark footer with {colors.ink} (#3c3c3c) background and white text. Links use {colors.muted-soft} (#cce3eb) for a softer contrast against the dark background. The footer is divided into columns for "Products", "About", "Support", and "Connect". A {colors.accent-gold} (#cab667) divider line separates the main content from the copyright and legal links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to {typography.display-lg}; search bar becomes full-width |
| Tablet | 744–1128px | Two-column product grid; nav links remain but "Shop" becomes a dropdown; hero uses {typography.display-xl} at 28px; footer columns stack to 2x2 |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero uses 36px display; search bar is centered in the nav |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 4 columns; hero text scales to 40px; whitespace increases on the sides |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Nav links have a 48px tap target on mobile, even if the text is smaller.
- Search bar and text inputs are 48px tall for comfortable touch interaction.
- Badges and small labels are not interactive; they are purely decorative.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- The product card grid collapses from 4 columns (wide) to 1 column (mobile).
- The hero section reduces its padding from 64px to 32px on mobile.
- Footer columns collapse from 4 columns to 2 columns on tablet, then to a single column on mobile.
- The search bar moves from the nav bar to a dedicated full-width section below the hero on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary button hover was extracted. Secondary button, text-input, and nav-link hover states are inferred but not confirmed from the live site.
- **Error styling**: No error states for forms (red borders, error messages) were found. The extracted palette lacks a dedicated error red.
- **Focus states**: Only text-input focus was extracted. Button focus rings and keyboard navigation outlines are unknown.
- **Dark mode**: No dark mode variant was detected. The brand may not support it.
- **Sub-brand palettes**: Cabinet Health may have sub-brands or seasonal campaigns with additional accent colors not captured in the extraction.
- **Font weights**: The extraction returned "Messina Sans Web Regular" and "SemiBold" but did not confirm the exact numeric weights. 400 and 600 are assumed based on standard naming conventions.
- **Spacing scale**: The spacing tokens are inferred from common design patterns and may not exactly match the live site's grid system.
- **Component padding**: Specific padding values for components like product cards and footers are estimated based on visual inspection and may vary.
- **The extracted color list is heavily weighted toward grays and blues, with only two warm accents (#f39f52, #fbf0a5) and one gold (#cab667). The brand's true primary (#0099ff) is the most distinctive blue in the list, but the overall palette is conservative and clinical. The warm accents are used sparingly, suggesting a deliberate restraint rather than a vibrant secondary palette.
