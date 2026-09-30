---
version: alpha
name: "Vyrao"
source_url: "https://vyrao.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A fragrance house that feels more like a botanical apothecary than a perfume brand, Vyrao wraps its energetic, wellness-first philosophy in a palette drawn from the earth and its healing plants. The canvas is a warm, almost papery off-white (`#e9e8e0`) that reads as raw linen or unbleached cotton, not sterile gallery white. Against this ground, the brand’s signature green — a deep, mossy `#43b02a` that leans into `#56ad6a` for secondary accents — suggests chlorophyll and vitality, while a secondary olive range (`#949069`, `#aaa686`, `#a9a687`) and darker sage (`#767254`, `#58553f`) create a quiet, layered herbarium. A single red note (`#d02e2e`) appears sparingly, like a rare bloom, and a soft blush (`#f3cbcb`) tempers the green intensity. Typography pairs the clean, geometric humanism of Jost (used for navigation, buttons, and small labels) with the more literary, serifed warmth of Source Serif 4 for body copy, and a third, distinctly elegant display face — sangbleu_versaillesregular — for hero headings and product names, lending a bespoke, almost hand-lettered quality. The overall mood is grounded, intentional, and slightly mystical: rounded corners are generous (`{rounded.lg}` at 20px for cards, `{rounded.full}` for pill-shaped CTAs), spacing is ample (`{spacing.xxl}` at 48px between sections), and the interface breathes like a slow, deliberate ritual. There are no hard edges, no aggressive contrasts — just a quiet confidence that the product (and the plant) is the hero.

colors:
  primary: "#43b02a"
  primary-active: "#128522"
  primary-disabled: "#ecfef0"
  ink: "#222222"
  body: "#555555"
  muted: "#666666"
  muted-soft: "#6f6f6f"
  hairline: "#cccccc"
  hairline-soft: "#dedede"
  canvas: "#e9e8e0"
  surface-soft: "#d4d2c2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#56ad6a"
  accent-olive: "#949069"
  accent-olive-light: "#aaa686"
  accent-olive-dark: "#767254"
  accent-forest: "#58553f"
  accent-red: "#d02e2e"
  accent-blush: "#f3cbcb"
  accent-gold: "#ecbd5e"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  accent-purple: "#a89cc8"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'sangbleu_versaillesregular', 'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'sangbleu_versaillesregular', 'Source Serif 4', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'sangbleu_versaillesregular', 'Source Serif 4', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Source Serif 4', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Jost', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 10px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 0
  button-pill-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "3/4"
  product-card-badge:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    maxWidth: "600px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
  footer-link-hover:
    color: "{colors.primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-panel:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.base} {spacing.lg}"
  ingredient-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
  ingredient-swatch-green:
    backgroundColor: "{colors.accent-green}"
  ingredient-swatch-olive:
    backgroundColor: "{colors.accent-olive}"
  ingredient-swatch-gold:
    backgroundColor: "{colors.accent-gold}"
  ingredient-swatch-blush:
    backgroundColor: "{colors.accent-blush}"
  ingredient-swatch-blue:
    backgroundColor: "{colors.accent-blue}"
  ingredient-swatch-purple:
    backgroundColor: "{colors.accent-purple}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button in the brand's signature green (`{colors.primary}`). Uses Jost uppercase with 1px letter-spacing for a refined, intentional feel. On hover, shifts to a deeper green (`{colors.primary-active}`); when disabled, fades to a pale mint (`{colors.primary-disabled}`) with muted text. The full rounding (`{rounded.full}`) reinforces the brand's soft, organic character.

**`button-secondary`** — An outlined variant on the warm canvas background (`{colors.canvas}`) with a subtle hairline border. Active state darkens the border to ink and lightly fills the background with the soft surface tone (`{colors.surface-soft}`). Used for "Learn More" or "Add to Wishlist" actions where the primary green would be too assertive.

**`button-tertiary`** — A text-only link styled as a button, using the brand green and small uppercase Jost. No background or border — just a clean, minimal call-to-action for inline contexts like accordion panels or product descriptions.

**`button-pill-green`** — A smaller, lighter green pill (`{colors.accent-green}`) used for secondary CTAs within product cards or promotional banners. Shares the full rounding and uppercase treatment but at a smaller scale.

### Cards
**`product-card`** — The primary product display unit, a white card (`{colors.surface-card}`) with generous 20px rounding (`{rounded.lg}`) and 16px padding. The product image sits inside with a slightly tighter 12px rounding (`{rounded.md}`) and a 3:4 aspect ratio. A small badge in olive (`{colors.accent-olive}`) overlays the top-left corner for "New" or "Bestseller" labels. Text uses Source Serif 4 at body-sm for the product name and a muted price line.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on the warm canvas background. Links are set in Jost uppercase with 1px tracking, creating a deliberate, editorial rhythm. On scroll, the bar transitions to a white background with a subtle drop shadow. The brand logo (typically set in sangbleu_versaillesregular) sits centered or left-aligned, with a cart icon and search icon on the right.

### Forms
**`text-input`** — Standard input fields with a white background, 12px rounding, and a light hairline border. On focus, the border switches to the brand green. Height is 48px with comfortable 12px/16px padding. Used for email signup, search, and checkout forms.

### Footer
**`footer`** — A full-width section on the soft surface tone (`{colors.surface-soft}`) with body-colored links in Source Serif 4. Links hover to the brand green. The footer typically contains three columns: customer care, about, and social links, with a newsletter signup form using the standard text-input.

### Accordion
**`accordion`** — Collapsible panels for FAQ and product details. The header uses the warm canvas background with title-md typography and 12px rounding. The expanded panel reveals body text in Source Serif 4 with comfortable padding. A subtle chevron icon rotates on open.

### Hero
**`hero-section`** — The top-of-page banner, typically full-width on the canvas background. The heading uses the display face at 48px with tight letter-spacing, while the subheading sits below in body-md at a max-width of 600px for readability. A primary button and a secondary button sit below the text. The hero may feature a full-bleed product image or a botanical illustration on the right side.

### Badges
**`product-card-badge`** — Small, pill-shaped labels in olive (`{colors.accent-olive}`) with white uppercase Jost text at 10px. Used to denote "New," "Limited Edition," or "Bestseller" status on product cards. The full rounding and tight padding keep them unobtrusive.

### Search
**`search-bar`** — A full-rounded, white search field with a hairline border, 56px height, and comfortable padding. On focus, the border turns green. The placeholder text uses body-md in Source Serif 4. A search icon sits at the left or right edge.

### Ingredient Swatches
**`ingredient-swatch`** — Small, 32px circular color swatches used in product detail pages to represent key botanical ingredients. Each swatch is a solid circle (`{rounded.full}`) with a specific brand color: green for chlorophyll-rich notes, olive for woody bases, gold for warm resins, blush for floral top notes, blue for aquatic elements, and purple for rare or mystical ingredients.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero text centers and reduces to display-lg; search bar moves below hero; footer links stack in a single column; accordion panels remain full-width; ingredient swatches display in a horizontal scrollable strip. |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows 4–5 links; hero uses display-lg with side-by-side text and image; search bar sits inline in the nav; footer uses two columns; accordion panels have 16px padding. |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; hero uses display-xl with generous whitespace; search bar is a prominent element in the nav; footer uses three columns; product cards show hover states with subtle shadow. |
| Wide | > 1440px | Max-width container at 1440px centered; hero may feature a full-bleed background image; product grid can expand to four columns; all spacing scales up slightly (section padding increases to 96px); typography remains at the same sizes for readability. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and a minimum width of 44px per WCAG guidelines.
- Icon buttons (cart, search, hamburger) are 48px × 48px with a 32px icon inside.
- Product card tap targets (image, title, add-to-cart) are at least 48px tall.
- Accordion headers are 56px tall for easy tapping.
- Ingredient swatches are 44px × 44px on mobile to meet touch target requirements.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu below 744px, hiding all links except the logo and cart icon.
- The product grid collapses from three columns to two at tablet, and to a single column on mobile.
- The hero section stacks vertically on mobile, with the image moving below the text.
- The footer collapses from three columns to two at tablet, and to a single column on mobile.
- Accordion panels are always full-width but collapse their content on tap.
- The search bar collapses from an inline element in the nav to a standalone, full-width component below the hero on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary button active states are inferred from the brand's color logic.
- Error styling for form inputs (red borders, error messages) is not present in the extracted data; a red accent (`{colors.accent-red}`) is available but its usage pattern is unknown.
- Dark mode is not supported; the brand appears to use a light, warm canvas exclusively.
- Sub-brand or collection-specific palettes (e.g., limited edition fragrances) may exist but were not captured.
- The exact font weights and sizes for sangbleu_versaillesregular are assumed based on typical display face usage; the actual font file may have different metrics.
- Spacing values for specific components (e.g., product card gap, hero padding) are estimated based on the brand's generous, editorial feel.
- The ingredient swatch colors are inferred from the extracted palette but may not correspond to actual product ingredients.
- The `textTransform: uppercase` on button and nav-link typography is inferred from the brand's editorial tone but not explicitly confirmed in the extracted CSS.
- The `boxShadow` on the scrolled nav-bar is a common pattern for the brand category but was not directly observed.
