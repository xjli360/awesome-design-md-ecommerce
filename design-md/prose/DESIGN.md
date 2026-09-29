---
version: alpha
name: "Prose"
source_url: "https://prose.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Prose is a direct-to-consumer haircare and skincare brand that feels like a quiet, bespoke apothecary translated into digital form. The brand's visual identity is rooted in a warm, earthy palette drawn from natural ingredients and botanical extracts, anchored by a soft, almost dusty beige (#b1a49c) and a muted sage green (#b9c2a6) that evoke raw herbs and unrefined clay. These sit against a canvas of off-white (#f9f7f2) and cream (#f1ece0), creating a gentle, unbleached backdrop that feels tactile and handmade. The primary action color is a deep, forest-like olive (#4d523c), used sparingly on buttons and key interactive elements, with a darker, almost charcoal variant (#323429) for active states. Accents of pale blush (#fcded3), dried coral (#f69371), and a whisper of lavender (#ead7f3) appear in ingredient photography overlays and badge treatments, while a vibrant chartreuse (#ecff92) and fresh green (#3ab549) signal clean, plant-based formulations. Typography leans on a refined serif, Saol, for display headings — lending a literary, editorial gravity — paired with Simplon Norm for body text and Simplon Mono for technical details like ingredient percentages. The overall spacing is generous, with large section padding ({spacing.section}) and soft, pill-shaped corners ({rounded.full}) on CTAs that feel more like a gentle invitation than a hard sell. Every design decision — from the low-contrast hairline (#e2d9c2) to the use of natural fiber textures in background imagery — reinforces the core promise: truly custom, made for you, not for the shelf.

colors:
  primary: "#4d523c"
  primary-active: "#323429"
  primary-disabled: "#b9c2a6"
  ink: "#161716"
  body: "#323429"
  muted: "#6c6c6c"
  muted-soft: "#a6a6a6"
  hairline: "#e2d9c2"
  hairline-soft: "#f1ece0"
  canvas: "#f9f7f2"
  surface-soft: "#f1ece0"
  surface-card: "#ffffff"
  on-primary: "#f9f7f2"
  accent-blush: "#fcded3"
  accent-coral: "#f69371"
  accent-coral-dark: "#c5765a"
  accent-lavender: "#ead7f3"
  accent-lavender-dark: "#bbacc2"
  accent-chartreuse: "#ecff92"
  accent-green: "#3ab549"
  accent-green-dark: "#2e844a"
  accent-sky: "#d0e2e8"
  accent-sky-dark: "#a2c6d1"
  accent-teal: "#88acb7"
  badge-error: "#b45446"
  badge-error-bg: "#e8cac6"
  badge-success: "#2e844a"
  badge-success-bg: "#bed9c7"
  badge-warning: "#fcb040"

typography:
  display-xl:
    fontFamily: "'Saol', 'Times New Roman', Times, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Saol', 'Times New Roman', Times, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Saol', 'Times New Roman', Times, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Saol', 'Times New Roman', Times, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02px
  title-sm:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.01px
  body-md:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01px
  caption-sm:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Simplon Norm', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  mono:
    fontFamily: "'Simplon Mono', 'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
  section: 80px

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
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
    height: auto
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.badge-error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-name:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 56px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  badge-ingredient:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-custom:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  ingredient-swatch:
    width: 40px
    height: 40px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  ingredient-swatch-selected:
    border: "2px solid {colors.primary}"
  quiz-progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
    rounded: "{rounded.full}"
  quiz-progress-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  accordion:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep olive (#4d523c) with off-white text. Used for "Add to Cart", "Start Quiz", and "Subscribe" actions. The pill shape ({rounded.full}) and uppercase label give it a confident, editorial weight. On hover, it shifts to the darker charcoal variant (#323429). The disabled state uses the muted sage (#b9c2a6) to visually de-emphasize the action without breaking the palette.

**`button-secondary`** — An outlined variant with a transparent fill and a 2px solid border in the primary olive. Used for secondary actions like "Learn More" or "View Ingredients". On hover, the background fills with the soft cream surface tone (#f1ece0) and the border deepens to the active charcoal. The uppercase typography and pill shape maintain consistency with the primary button.

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Cancel" or "Skip". The label uses the primary olive color and the same uppercase button typography, but with no padding or fixed height, allowing it to sit naturally within body text or form layouts.

### Cards
**`product-card`** — A white card with soft rounded corners ({rounded.md}) and 16px padding, used to display individual product formulations in the shop grid and the "Your Custom Routine" section. The card contains a product image with its own smaller rounding ({rounded.sm}), a title in the semi-bold Simplon Norm ({typography.title-sm}), and a price in the primary olive. The card has no border or shadow, relying on the contrast between the white surface and the cream canvas (#f9f7f2) for separation.

**`hero-section`** — A full-width section with a soft cream background (#f1ece0) and generous vertical padding ({spacing.section}). The hero uses the serif display typography ({typography.display-xl}) for the headline, with a single pill-shaped CTA button. The background color and typography work together to create a calm, editorial opening that feels more like a magazine spread than a traditional e-commerce banner.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a white background and a subtle bottom hairline (#f1ece0). Navigation links use the uppercase Simplon Norm ({typography.nav-link}) in muted gray (#6c6c6c) for inactive states and the primary olive for the active or hovered state. The bar contains the brand logo, a set of category links, a search icon, and a cart icon.

**`nav-link-active`** — The active navigation link uses the primary olive color to signal the current page or section. The typography remains the same uppercase weight, creating a clear but understated distinction from the inactive state.

### Forms & Inputs
**`text-input`** — A standard text input with a cream background (#f9f7f2), 1px hairline border (#e2d9c2), and 8px border radius. Used for form fields in the quiz and account pages. On focus, the border switches to the primary olive. The error state uses the deep red (#b45446) border, paired with the error badge styling for inline validation messages.

**`search-bar`** — A pill-shaped search input with a white background and 1px hairline border. Used in the navigation and on the ingredient discovery page. The full rounding ({rounded.full}) and generous padding create a friendly, approachable entry point for browsing ingredients and products.

### Badges & Indicators
**`badge-ingredient`** — A small pill badge with a chartreuse background (#ecff92) and dark text, used to highlight key natural ingredients like "Biotin" or "Niacinamide" on product cards and ingredient pages. The uppercase badge typography keeps the label compact and readable.

**`badge-custom`** — A lavender-toned badge (#ead7f3) used to indicate "Custom Formulation" or "Personalized for You" on product cards and the quiz results page. The soft purple adds a subtle, personalized touch without competing with the primary olive.

**`badge-sale`** — A coral badge (#f69371) with white text, used for promotional pricing or limited-time offers. The warm coral creates urgency while staying within the brand's earthy palette.

### Footer
**`footer`** — A full-width footer with the primary olive background and off-white text. Contains links to "About Us", "Ingredients", "Our Process", "FAQ", and social media icons. The link typography uses the body size with standard weight, creating a calm, readable closing section. Padding is generous at 48px top and bottom.

### Quiz & Personalization
**`quiz-progress-bar`** — A thin, 4px progress bar used in the multi-step hair and skin quiz. The track is the soft cream hairline (#f1ece0), and the fill is the primary olive. The full rounding on both elements creates a smooth, continuous visual that matches the brand's soft aesthetic.

**`accordion`** — A border-bottom accordion used for ingredient details and FAQ sections. The header uses the semi-bold title typography with no background, and the content area opens with the body typography and 8px top padding. The only visual separator is the soft cream hairline, keeping the layout clean and airy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero section reduces to 48px vertical padding; product cards stack vertically; navigation collapses to hamburger menu; button padding reduces to 12px 24px; display-xl reduces to 32px; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; hero uses 64px vertical padding; navigation links remain visible but reduce font size to 13px; product cards use 12px padding; search bar remains in nav but reduces width |
| Desktop | 1128–1440px | Three-column product grid; full hero section with 80px vertical padding; all navigation links visible; standard component sizing applies |
| Wide | > 1440px | Maximum content width of 1440px with auto margins; hero section can extend full width with background color; product grid can expand to four columns if content allows |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px on mobile and tablet
- Navigation hamburger icon is 48x48px on mobile
- Product card CTAs are 48px tall on all breakpoints
- Accordion headers have 44px minimum tap height
- Ingredient swatches are 44x44px on touch devices

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Product grid collapses from 3 columns to 2 at 1128px, then to 1 column at 744px
- Hero section text and CTA stack vertically below 744px
- Footer links stack into a single column below 744px
- Ingredient detail accordions remain collapsed by default on mobile to save vertical space
- Search bar transforms from inline to full-width below 744px, appearing below the navigation

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons beyond the basic color shift (no extracted data for shadow, scale, or transition timing)
- Error state styling for forms beyond border color (no extracted data for error message typography, icon placement, or animation)
- Dark mode or high-contrast mode specifications (no extracted data for alternative palettes)
- Sub-brand or seasonal palette variations (e.g., holiday collections, limited editions)
- Focus ring styling for keyboard navigation (no extracted data for outline color, width, or offset)
- Loading states for buttons, cards, and images (no extracted data for spinner design or skeleton screens)
- Tooltip and popover styling (no extracted data for background, arrow, or z-index)
- Modal and overlay specifications (no extracted data for scrim opacity, animation, or close button placement)
- Specific font weights for Saol and Simplon variants beyond what was declared in CSS (no extracted data for weight 300, 700, or italic)
- Ingredient photography and illustration style guide (no extracted data for color treatment, composition, or aspect ratio)
- Video player styling (no extracted data for controls, progress bar, or fullscreen behavior)
