---
version: alpha
name: "Omnivore Books"
source_url: "https://www.omnivorebooks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A cookbook specialist’s library, where the warmth of a well-stocked kitchen shelf is translated into a digital storefront through a buttery canvas of #fffbf2 and a gilded accent of #ab8c52 that reads like aged brass or the spine of a vintage Le Cordon Bleu manual. The brand’s primary color, #ab8c52, appears on key interactive elements — the add-to-cart button, the search icon, and the footer’s newsletter signup — lending a sense of permanence and quality that resists the throwaway feel of generic e-commerce. Typography is set in Figtree for body and Fraunces for display, a pairing that balances Fraunces’s soft, ink-trap serifs (used for book titles and section headers at 24–32px) with Figtree’s clean, slightly condensed sans-serif for product descriptions and navigation. The site’s secondary palette is restrained: #222222 for ink, #444444 for body text, and #747474 for muted labels, all resting on the warm #fffbf2 canvas. Cards and surfaces use #ffffff for contrast, with hairline borders in #dedede and softer dividers in #eaeaea. A subtle #e7d2aa appears as a hover state on secondary buttons and as a background tint on featured collections, echoing the color of unbleached parchment. The overall mood is that of a serious but welcoming bibliophile’s corner — no aggressive sales tactics, just a quiet confidence in the curation. Signature design moves include a full-width hero section featuring a single cookbook cover at 60% of the viewport height, a persistent top nav with a search bar that expands on click, and a product grid that uses generous whitespace (48px between rows) to let each cover breathe. The checkout flow, while standard Shopify, is overlaid with the brand’s #fffbf2 canvas and #ab8c52 accents, avoiding the generic blue of default Shopify themes. The result is a site that feels less like a store and more like a personal recommendation from a trusted food historian.

colors:
  primary: "#ab8c52"
  primary-active: "#8e6f3a"
  primary-disabled: "#d4c49a"
  ink: "#222222"
  body: "#444444"
  muted: "#747474"
  muted-soft: "#b9b9b9"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#fffbf2"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-featured: "#e7d2aa"
  on-primary: "#ffffff"
  on-primary-hover: "#ffffff"
  error: "#d32f2f"
  success: "#9acd32"
  badge-new: "#d32f2f"
  badge-sale: "#9acd32"

typography:
  display-xl:
    fontFamily: "'Fraunces', 'Georgia', 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Fraunces', 'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Fraunces', 'Georgia', 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Inter', -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Figtree', 'Inter', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Figtree', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Figtree', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Inter', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Figtree', 'Inter', -apple-system, sans-serif"
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary-hover}"
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-featured}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-expanded:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
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
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-image:
    rounded: "{rounded.md}"
    maxHeight: "60vh"
  featured-collection:
    backgroundColor: "{colors.surface-featured}"
    padding: "{spacing.xl} {spacing.lg}"
    rounded: "{rounded.md}"
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 40px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart," "Checkout," and "Subscribe." Rendered in the brand's gilded #ab8c52 with white text and a soft 8px radius. On hover, it deepens to #8e6f3a (`{colors.primary-active}`) with no shadow — the brand avoids heavy elevation in favor of color shift. The disabled state fades to #d4c49a (`{colors.primary-disabled}`), maintaining readability but signaling inactivity. Height is 44px, a comfortable touch target that doesn't overwhelm the product grid.

**`button-secondary`** — Used for "View Details," "Continue Shopping," and secondary form actions. A white button with a 1px #dedede border and ink text. On hover, the background shifts to #e7d2aa (`{colors.surface-featured}`) and the border to #ab8c52, creating a subtle parchment effect that echoes the brand's warm canvas. Active state uses the same hover treatment but with a slightly thicker border.

**`button-tertiary-text`** — A text-only link styled as a button, used for "Learn More" and "Read Reviews." Rendered in #ab8c52 with no background or border, matching the brand's link color. Padding is minimal (8px vertical, 0 horizontal) to keep the text flush with surrounding content. Hover state adds an underline.

### Cards
**`product-card`** — The core product display unit, a white card with a 12px radius and no border — the card relies on the #fffbf2 canvas for separation rather than a hard stroke. The image occupies the top portion with rounded top corners (`{rounded.md} {rounded.md} 0 0`), while the title and price sit below with 8px horizontal padding. On hover, a subtle box-shadow lifts the card 4px, creating a gentle stacking effect. The price is always rendered in #ab8c52, reinforcing the brand's accent as a signal of value.

**`featured-collection`** — A highlighted section for curated book lists (e.g., "Staff Picks," "New Arrivals"). The background is #e7d2aa (`{colors.surface-featured}`), a warm parchment tone that contrasts with the white product cards placed inside. Padding is 32px horizontal and 24px vertical, with a 12px radius. The section header uses `{typography.display-md}` in Fraunces to distinguish it from standard product rows.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height, using the #fffbf2 canvas with a subtle bottom border in #eaeaea. Navigation links are set in Figtree at 15px weight 500, with the active page underlined by a 2px #ab8c52 bar. The search icon sits on the right, expanding into a pill-shaped input on click (`{rounded.full}`). On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

**`nav-link`** — Individual navigation items with 8px vertical and 16px horizontal padding. Inactive links use #222222, while the active link shifts to #ab8c52 with a bottom border. Hover state uses a subtle opacity shift to #444444.

### Forms
**`text-input`** — Standard form input for checkout fields and account forms. A white background with a 1px #dedede border and 12px radius. On focus, the border thickens to 2px and switches to #ab8c52, with no outline — the brand uses border-color and thickness as the sole focus indicator. Height is 48px with 12px vertical padding for comfortable typing.

**`search-bar`** — A pill-shaped input (`{rounded.full}`) used in the nav and on the search page. At rest, it's 44px tall with a 1px #dedede border. On focus or expansion, it grows to 48px with a 2px #ab8c52 border, signaling active input. The placeholder text uses #b9b9b9 (`{colors.muted-soft}`).

**`newsletter-input`** and **`newsletter-button`** — A paired input and button in the footer. The input is 40px tall with a 1px #dedede border and 8px radius, while the button uses the primary #ab8c52 at the same height. The two elements sit side-by-side with no gap, creating a seamless join.

### Footer
**`footer`** — A dark footer in #222222 with white text and links in #b9b9b9. The newsletter signup is the primary interactive element, with the input in white and the button in #ab8c52. Links use `{typography.link}` at 14px weight 500, with hover states shifting to #ffffff. The footer is padded 48px vertically and uses a 64px section spacing above it.

### Badges
**`badge`** — Used for "NEW" labels on recently added books. Rendered in #d32f2f with white text, 4px radius, and 2px vertical / 8px horizontal padding. The type is uppercase Figtree at 11px weight 700 with 0.5px letter-spacing.

**`badge-sale`** — Used for discounted items. Rendered in #9acd32 with #222222 text, maintaining the same dimensions and typography as the standard badge. The green tone is the brand's only bright accent, used sparingly.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes single-column (1 card per row); hero image reduces to 40vh; search bar becomes a full-width input below the nav; footer stacks vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product grid uses 2 columns; hero image at 50vh; search bar remains pill-shaped but narrower |
| Desktop | 1128–1440px | Full nav with all links; product grid uses 3 columns; hero image at 60vh; search bar in nav expands on click |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grid uses 4 columns; hero image at 60vh with wider margins |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (48px for primary inputs) to meet WCAG touch target guidelines.
- Nav links have 16px horizontal padding, ensuring a comfortable tap area even on dense nav bars.
- Product card images are tappable as links, with the entire card surface acting as a click target (no small "View" buttons).
- Search bar expands to 48px height on focus, providing a larger tap area for text input.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger icon that opens a full-screen overlay menu. The search bar moves below the nav as a standalone full-width input.
- The product grid collapses from 3 columns (desktop) to 2 columns (tablet) to 1 column (mobile), with cards stacking vertically.
- The hero section reduces its image height from 60vh to 40vh on mobile, with text overlay adjusting to a single-column layout.
- The footer collapses from a multi-column layout (desktop) to a single vertical stack on mobile, with the newsletter signup remaining at the top of the stack.
- Featured collection sections maintain their background color but reduce horizontal padding from 32px to 16px on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states for product cards**: The extracted data shows a box-shadow on hover, but the exact shadow values (spread, color opacity) could not be reliably determined. Assumed 0 4px 12px rgba(0,0,0,0.08) based on common patterns.
- **Error and validation styling**: The extracted list includes #d32f2f (likely error red) and #9acd32 (likely success green), but their exact usage in form validation (border colors, icon placement, message typography) is inferred, not extracted.
- **Dark mode**: No evidence of a dark mode variant. The brand's warm canvas (#fffbf2) is likely the only mode.
- **Sub-brand or seasonal palettes**: The site may use different accent colors for special collections (e.g., holiday themes), but these were not captured in the extraction.
- **Loading states**: Skeleton screens, spinner styles, and loading animation details are absent from the extraction.
- **Focus-visible styles**: While focus states are inferred for text inputs (2px primary border), other interactive elements (buttons, links) may have additional focus-visible outlines not captured.
- **Checkout flow**: The Shopify checkout may override some brand colors (e.g., payment button colors from Shopify Pay, Klarna, Afterpay). The extracted list includes #d32f2f and #9acd32 which may be checkout-widget colors rather than brand colors — these are noted as potential false positives.
- **Font weights for Fraunces**: The exact font weights used (e.g., 600 vs 700 for display) are inferred from common usage; the extraction only confirmed the font family name.
- **Spacing values for specific components**: While global spacing tokens are defined, component-specific padding and margin values (e.g., product card internal padding) are estimated based on visual analysis of the extracted colors and layout patterns.
