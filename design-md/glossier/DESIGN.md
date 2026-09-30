---
version: alpha
name: "Glossier"
source_url: "https://www.glossier.com"
captured_at: "2026-09-28T04:09:52.674350+00:00"
evidence_status: "historical_partial_css_evidence"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand that lives in the gap between #dedede and #121212 — a pale, almost-warm gray and a near-black that together create a system of extreme restraint. Glossier’s canvas is not white but a soft, foggy gray that reads as a studio backdrop, making every product the hero. The near-black ink (#121212) appears sparingly: in body copy, in the single bold headline on a product page, in the thin stroke of a line drawing. There are no gradients, no drop shadows, no decorative flourishes — the visual language is flat, clean, and deliberately unpolished in a way that suggests a friend’s bathroom shelf rather than a department store counter. Buttons are pill-shaped (`{rounded.full}`), product cards are softly rounded (`{rounded.md}`), and the entire experience breathes through generous whitespace (`{spacing.section}`). The brand’s voice is direct, personal, and slightly irreverent — copy often runs in sentence case with a lowercase brand name, and the typography favors a single, clean sans-serif that never competes with the product photography. The result is a digital storefront that feels more like a personal recommendation than a retail transaction.

colors:
  primary: "#dedede"
  primary-active: "#c4c4c4"
  primary-disabled: "#f0f0f0"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f5f5f5"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#121212"
  on-dark: "#ffffff"
  accent-pink: "#f4a2b8"
  accent-sage: "#b8c9b8"
  accent-terracotta: "#d4a574"
  badge-new: "#121212"
  badge-sold-out: "#dedede"

typography:
  display-xl:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'GT America', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px

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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.accent-terracotta}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-image:
    rounded: "{rounded.md}"
    aspectRatio: "16:9"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    borderTop: "1px solid {colors.hairline-soft}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.ink}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "1px solid {colors.hairline}"
  color-swatch-selected:
    border: "2px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    height: 24px
    width: 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button in the brand's signature pale gray (#dedede). Text appears in near-black (#121212) with medium weight. On hover, the background shifts to a slightly darker gray (#c4c4c4). The disabled state uses a lighter gray (#f0f0f0) with muted text (#7a7a7a). Used for "Add to Bag," "Checkout," and primary form submissions.

**`button-secondary`** — An outlined variant with a transparent background and a thin hairline border. The pill shape is maintained, but the visual weight is lighter, making it suitable for secondary actions like "View Details" or "Save for Later." On hover, the border darkens to the ink color.

**`button-tertiary-text`** — A text-only button with no background or border. Used for subtle actions like "Cancel" or "Learn More." The text color matches the ink, and the button has no padding on the sides, relying on the surrounding layout for spacing.

**`button-pill-ink`** — A high-contrast pill button with a near-black background and white text. Used sparingly for the most important actions, such as "Subscribe" or "Get the Kit." The dark background creates a visual anchor against the pale gray canvas.

### Cards
**`product-card`** — The primary product display unit, featuring a square image with soft rounded corners (`{rounded.md}`) and a two-line layout below: the product name in title-sm and the price in body-sm with muted color. The card has a white background and no border, relying on the surrounding canvas (#f5f5f5) for separation. On hover, a subtle shadow may appear, but the default state is flat.

**`product-card-image`** — The image container within a product card. Maintains a 1:1 aspect ratio and uses the same rounded corners as the card itself. Images are typically clean, well-lit product shots on a white or pale gray background.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar with a canvas background and a thin bottom border. The height is 64px, accommodating the brand logo on the left, navigation links in the center, and utility icons (search, account, bag) on the right. The typography uses nav-link with medium weight.

**`nav-link-active`** — The active navigation link state, indicated by a 2px bottom border in the ink color. The link text remains in ink. Used to indicate the current page or section.

**`nav-link-inactive`** — The default navigation link state, with muted text color. On hover, the text color shifts to ink, but no underline or border is added.

### Forms
**`text-input`** — A standard text input field with a canvas background, a thin hairline border, and soft rounded corners (`{rounded.sm}`). The input has 12px vertical padding and 16px horizontal padding, with a height of 48px. On focus, the border changes to the ink color. Error states use the terracotta accent color for the border.

**`search-bar`** — A pill-shaped search input with a full border and a search icon on the left. The input has 12px vertical padding and 20px horizontal padding. On focus, the border changes to the ink color. Used in the navigation bar and on search result pages.

### Badges
**`badge-new`** — A small, uppercase badge with a near-black background and white text. Used to indicate new product launches or limited-edition items. The badge has full rounded corners and tight padding.

**`badge-sold-out`** — A small, uppercase badge with a pale gray background and near-black text. Used to indicate out-of-stock items. The visual weight is lighter than the "new" badge, signaling unavailability without drawing attention.

### Footer
**`footer-section`** — The site footer, with a canvas background, muted text, and a thin top border. Links are styled with the link typography and muted color, shifting to ink on hover. The footer typically includes columns for customer service, about, and social links.

### Accordion
**`accordion`** — A collapsible content panel used for product descriptions, ingredients, and shipping information. The header uses title-sm typography with a bottom border. The content area uses body-sm typography with muted color and appears on click with a smooth animation.

### Color Swatches
**`color-swatch`** — A circular swatch used to display product color options. Each swatch is 32px in diameter with a thin hairline border. The selected state adds a 2px ink-colored border around the swatch.

### Quantity Selector
**`quantity-selector`** — A compact input group for adjusting product quantities. The container has a hairline border and soft rounded corners. The buttons on either side are transparent with muted icons, and the center displays the current quantity in body-md.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to 32px; search bar moves to a dedicated overlay; footer collapses to single column |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links (logo, search, account, bag); hero section maintains 48px padding; footer shows two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links; hero section at full padding (64px); footer shows four columns |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; hero section remains centered with max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44px x 44px
- Product card images are tappable and navigate to the product detail page
- Color swatches are 32px with a 44px tap area (achieved through padding)
- Quantity selector buttons are 24px with a 44px tap area
- Accordion headers are tappable across their full width

### Collapsing Strategy
- Navigation links collapse to a hamburger menu below 744px
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport shrinks
- Footer columns collapse from 4 to 2 to 1
- Hero section collapses from side-by-side (image + text) to stacked on mobile
- Search bar collapses from inline to overlay on mobile
- Product description sections collapse from visible to accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Font family could not be extracted from the live site; "GT America" is used as a best-guess based on the brand's known typography. The actual font may differ.
- Hover and active states for most components could not be verified from the extracted data; they are inferred from common design patterns.
- Error states for forms (validation messages, error icons) could not be extracted.
- Dark mode or high-contrast mode styles are not available.
- The brand's accent colors (pink, sage, terracotta) are inferred from product imagery and marketing materials; their exact hex values may vary.
- Sub-brand or limited-edition color palettes are not captured.
- Animation durations, easing curves, and transition properties are not specified.
- The exact spacing between product cards in a grid could not be determined.
- The brand's icon set and illustration style are not documented.
- The checkout flow (Shopify Pay, Klarna, Afterpay) styling is not included as it is handled by third-party widgets.
