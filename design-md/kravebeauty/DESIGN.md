---
version: alpha
name: "KraveBeauty"
source_url: "https://kravebeauty.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  KraveBeauty is a skincare brand that lives in the tension between gentle efficacy and radical transparency, a philosophy they call #PressReset. The palette is anchored by a soft, almost herbal green `#aaccaa` that feels like a breath of fresh air, used as a primary accent against a clean, off-white canvas of `#f4f4f6`. This is not a brand that shouts; its energy comes from unexpected, playful jolts of neon—a lime green `#c1d22f` and a highlighter-yellow `#eaf586`—that appear in badges, icons, and interactive elements, suggesting a youthful, optimistic spirit. The typography leans on the clean, geometric lines of `Inter` and `Karla`, creating a readable, approachable interface that feels more like a trusted friend's advice than a clinical directive. Deep, muted navies like `#272d45` and `#2c3e50` provide grounding for headers and footers, while a spectrum of purples—from the soft `#c8c2ff` to the electric `#6c5cff` and deep `#1300c2`—adds a layer of digital-native, almost playful sophistication to buttons and links. The overall mood is that of a well-lit, minimalist studio: clean, honest, and quietly confident, with pops of color that reward exploration. Rounded corners are generous but not pillowy, with `{rounded.md}` at 12px for cards and `{rounded.sm}` at 8px for buttons, creating a tactile, friendly feel without sacrificing the brand's clean, editorial edge.

colors:
  primary: "#aaccaa"
  primary-active: "#8fb88f"
  primary-disabled: "#d4e8d4"
  accent-green: "#c1d22f"
  accent-yellow: "#eaf586"
  accent-purple: "#6c5cff"
  accent-purple-light: "#c8c2ff"
  accent-purple-dark: "#1300c2"
  ink: "#141414"
  body: "#333333"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#e1e3e4"
  hairline-soft: "#f7f7f8"
  border-strong: "#d3d4dd"
  canvas: "#f4f4f6"
  surface-soft: "#f6f5ff"
  surface-card: "#ffffff"
  surface-strong: "#e5e5eb"
  on-primary: "#141414"
  on-dark: "#ffffff"
  nav-bg: "#272d45"
  footer-bg: "#2c3e50"
  star-rating: "#141414"
  error: "#c13515"
  success: "#b2f9e9"

typography:
  display-xl:
    fontFamily: "'Inter', 'Karla', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Karla', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-accent:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-purple-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    color: "{colors.accent-yellow}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-dark}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-strong}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  accordion-active:
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature soft green `#aaccaa`. It uses `{typography.button-md}` for a clear, weighty label and `{rounded.sm}` for a friendly but not overly rounded corner. On hover, it shifts to `{colors.primary-active}` (`#8fb88f`), and in its disabled state it fades to `{colors.primary-disabled}` (`#d4e8d4`) with muted text to signal inactivity. **`button-secondary`** — A clean, outlined alternative on the `{colors.canvas}` background, with a subtle `{colors.hairline}` border. It maintains the same sizing and typography as the primary button, offering a less visually dominant option for secondary actions. **`button-accent`** — The brand's high-energy action button, using the electric purple `{colors.accent-purple}` (`#6c5cff`) against white text. It's used for special promotions, sign-ups, or any action that needs to stand out from the green primary. **`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Learn More" or "Cancel" within a card or modal.

### Cards
**`product-card`** — The core product display unit, a white card (`{colors.surface-card}`) with `{rounded.md}` (12px) corners and `{spacing.base}` padding. The product image sits at the top with `{rounded.sm}`, followed by the product name in `{typography.title-sm}` and price in `{typography.body-md}`. A **`product-card-badge`** is a small, pill-shaped (`{rounded.full}`) label using the lime green `{colors.accent-green}` and uppercase `{typography.badge}`, used to denote "New," "Bestseller," or "Limited Edition." The card has a subtle hover state that elevates it with a drop shadow.

### Navigation
**`nav-bar`** — A dark, full-width navigation bar with a deep navy background (`{colors.nav-bg}`) and white text. Links use `{typography.nav-link}` in uppercase with generous letter-spacing, and the active state is highlighted in the brand's neon yellow (`{colors.accent-yellow}`). The bar is fixed at 64px height. On mobile, this collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — Standard text input fields use the light canvas background (`{colors.canvas}`) with a `{colors.hairline}` border and `{rounded.sm}`. On focus, the border switches to the primary green `{colors.primary}`. Error states use a red border (`{colors.error}`). The `{typography.body-md}` ensures readability. Search inputs use a **`search-bar`** variant with `{rounded.full}` (pill shape) and a slightly taller height of 48px.

### Footer
**`footer-section`** — A deep, dark section using `{colors.footer-bg}` (`#2c3e50`) as a grounding element. Text is white, and links are a muted gray (`{colors.muted-soft}`) that brighten to white on hover. The layout typically includes columns for "Shop," "Learn," "About," and "Social," with generous `{spacing.section}` padding top and bottom.

### Accordion
**`accordion`** — Used for FAQ sections and product descriptions. Each item is a white card on the `{colors.canvas}` background with a `{colors.hairline-soft}` border and `{rounded.sm}`. The header uses `{typography.title-sm}` and toggles open to reveal content in `{typography.body-sm}`. An active item gets a `{colors.primary}` border to indicate its open state.

### Hero
**`hero-section`** — The primary landing banner, using a soft purple-tinted background (`{colors.surface-soft}`) to create a gentle, welcoming entry point. The headline uses `{typography.display-xl}` in the dark ink color (`{colors.ink}`), often paired with a supporting image or a short description in `{typography.body-md}`. The section has generous `{spacing.section}` padding to create a sense of spaciousness.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero text scales down to `{typography.display-md}`; search bar becomes full-width; accordions are always stacked. |
| Tablet | 744–1128px | Two-column product grid; nav-bar remains visible but links may be condensed; hero uses a two-column layout with text and image side-by-side; footer links stack into two columns. |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; hero uses full `{typography.display-xl}`; multi-column footer layout; maximum content width is constrained. |
| Wide | > 1440px | Content is centered with a max-width container; extra whitespace on sides; product grid can expand to four columns if content allows. |

### Touch Targets
- All interactive elements (buttons, links, icons) have a minimum touch target of 44x44px.
- Mobile nav hamburger icon is 48x48px.
- Product card "Add to Cart" button is 48px tall.
- Accordion headers are 48px tall for easy tapping.

### Collapsing Strategy
- Primary navigation collapses into a hamburger menu on mobile (< 744px).
- Product filter sidebar (if present) collapses into a dropdown or bottom sheet on mobile.
- Multi-column footer collapses into a single column on mobile, with accordion-style sections.
- Hero section image stacks below text on mobile.
- Product image galleries collapse from a row of thumbnails to a single swipeable carousel on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components (only primary button and footer links have reliable extracted data).
- Error styling for forms beyond the border color (no extracted error message typography or iconography).
- Dark mode palette (not present on the live site).
- Sub-brand or campaign-specific palettes (e.g., limited edition drops).
- Specific font weights for `Inconsolata` (used sparingly, likely for code or monospaced elements).
- Detailed animation and transition timing curves.
- Focus ring styles for accessibility (not reliably extracted).
- Dropdown menu and modal component specifications.
- Star rating component sizing and spacing beyond color.
- Specific icon library and sizing guidelines.
