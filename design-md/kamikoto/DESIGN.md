---
version: alpha
name: "Kamikoto"
source_url: "https://kamikoto.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Kamikoto is a brand forged in the tradition of Japanese steel craftsmanship, where every pixel echoes the precision of a blade. The palette is anchored by a deep, almost-black ink (`#1e1e1e`) that serves as the primary canvas, creating a sense of gravity and focus. This is offset by a stark, pure white (`#ffffff`) for surfaces like cards and the main body, ensuring product imagery remains the hero. The primary action color is a restrained yet confident blue (`#1990c6`), with a deeper active state (`#136f99`) that feels like the patina on a well-used knife. Accents of a muted silver (`#a2a2a2`) and a warm, soft gray (`#dedede`) provide structure through hairline borders and subtle surface distinctions, while a single, sharp accent of crimson (`#dc143c`) is used sparingly for sale badges or critical alerts, mimicking the flash of a blade. The typography relies on the serifed elegance of 'Average', a choice that speaks to heritage and the written word of a master craftsman, rather than the cold efficiency of a modern sans-serif. Rounded corners are minimal and functional—the `{rounded.sm}` (8px) on buttons and `{rounded.md}` (12px) on cards provide a slight softening without compromising the brand's inherent sharpness. The overall feeling is one of a dimly lit, curated atelier: the `{colors.canvas}` is dark (`#1e1e1e`), the `{colors.surface-card}` is a lighter gray (`#252525`), and text is rendered in a clean white (`#dedede`) or a muted gray (`#a2a2a2`). This is not a brand of bright, airy spaces; it is one of focused, premium quality, where the product's own luster provides the light.

colors:
  primary: "#1990c6"
  primary-active: "#136f99"
  primary-disabled: "#424242"
  ink: "#1e1e1e"
  body: "#dedede"
  muted: "#a2a2a2"
  muted-soft: "#424242"
  hairline: "#424242"
  hairline-soft: "#252525"
  canvas: "#1e1e1e"
  surface-soft: "#252525"
  surface-card: "#252525"
  on-primary: "#ffffff"
  accent-sale: "#dc143c"
  accent-highlight: "#accef7"
  text-on-dark: "#dedede"
  text-on-light: "#121212"

typography:
  display-xl:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Average', Georgia, 'Times New Roman', serif"
    fontSize: 11px
    fontWeight: 400
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: 1px solid "{colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: 1px solid "{colors.body}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  sale-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: 1px solid "{colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for 'Add to Cart' and 'Shop Now'. It features a solid blue (`{colors.primary}`) background with white text and an uppercase label. On hover, it transitions to a deeper blue (`{colors.primary-active}`). The disabled state uses a dark gray (`{colors.primary-disabled}`) background with muted text.

**`button-secondary`** — An outlined button for secondary actions like 'Learn More' or 'View Details'. It has a transparent background with a subtle border (`{colors.hairline}`) and body-colored text. The active state fills the background with a soft surface color and strengthens the border to the body text color.

**`button-ghost`** — A minimal text button for tertiary actions, such as 'Cancel' or 'Close'. It has no background or border, relying solely on the body text color and a smaller uppercase typography.

### Cards
**`product-card`** — The primary container for product listings. It uses a dark surface (`{colors.surface-card}`) with a `{rounded.md}` corner radius. The card contains an image area with the same rounding, a title in `{typography.title-md}`, and a price in `{typography.body-md}` with a muted color. A `sale-badge` can be overlaid on the image, using a crimson (`{colors.accent-sale}`) background.

### Navigation
**`nav-bar`** — The main site navigation bar, fixed at the top. It has a solid `{colors.canvas}` background and a height of 72px. Navigation links use `{typography.nav-link}`, which is an uppercase, letter-spaced serif. The logo is typically left-aligned, with links and a cart icon on the right.

### Forms
**`text-input`** — Standard input fields for forms (e.g., email signup, address). They have a `{colors.surface-soft}` background, a `{colors.hairline}` border, and `{rounded.sm}` corners. On focus, the border changes to the primary blue (`{colors.primary}`).

### Footer
**`footer-section`** — The site footer, using the darkest ink (`{colors.ink}`) as the background. Text is rendered in the muted gray (`{colors.muted}`) for a hierarchical separation. It contains links, legal text, and social icons, all using `{typography.body-sm}`.

### Hero
**`hero-section`** — A full-width section for the homepage hero. It uses the `{colors.canvas}` background and features the `{typography.display-xl}` for the headline. The section padding uses `{spacing.section}` for top and bottom, creating a dramatic, immersive feel.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) used for filtering products. It has a `{colors.surface-soft}` background, a `{colors.hairline}` border, and body text. The rounded shape provides a subtle contrast to the otherwise angular design.

### Dividers
**`divider`** — A simple 1px horizontal line using the `{colors.hairline}` token, used to separate sections or content blocks.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single column product grid, hamburger menu replaces nav-bar, hero text scales down to `{typography.display-md}`, buttons become full-width, footer stacks vertically. |
| Tablet | 744–1128px | Two column product grid, nav-bar remains visible but links may collapse into a "More" dropdown, hero maintains two-column layout with image and text. |
| Desktop | 1128–1440px | Three column product grid, full nav-bar with all links visible, hero uses full `{typography.display-xl}` size, standard button widths. |
| Wide | > 1440px | Four column product grid, max-width containers (e.g., 1440px) are used to prevent content from stretching too wide, hero may feature a larger background image. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet accessibility standards.
- Icon buttons are 40px x 40px, providing a comfortable 44px touch target when including padding.
- Product cards have a minimum tap area of 48px for the title and price.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu, hiding all nav links.
- The product grid collapses from 3-4 columns on desktop to 1 column on mobile.
- The hero section's text and image stack vertically on mobile, with the image appearing first.
- The multi-column footer collapses into a single column, with accordion-style sections for links.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components (e.g., `text-input-focus`, `button-secondary-active`) are inferred from common patterns and may not match the exact live site implementation.
- Error styling for form inputs (e.g., red border, error message typography) was not extracted.
- The specific font weight for 'Average' is assumed to be 400 (Regular), as no other weights were found in the extracted hints.
- Sub-brand or promotional palettes (e.g., for holiday sales, specific product lines) are not captured.
- Dark mode is not applicable as the brand's default state is already a dark theme.
- The exact `letterSpacing` and `textTransform` values for typography tokens are best guesses based on the brand's editorial feel.
- Animation and transition timing functions (e.g., ease-in-out, duration) are not defined.
