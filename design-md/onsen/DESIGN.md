---
version: alpha
name: "Onsen"
source_url: "https://onsentowel.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Onsen is a bath brand that brings the calm, mineral-rich spirit of a Japanese hot spring into the daily ritual of drying off. The palette is anchored by a deep, oceanic navy (`#0f4c81`) that reads as both luxury and tranquility — it appears on primary buttons, the site header, and key product accents. A warm gold (`#dea439`) provides the brand's voltage, used sparingly for star ratings, sale badges, and hover states on secondary elements. The canvas is a soft, almost paper-like off-white (`#fefbf1`) rather than a stark white, giving the entire experience a tactile, spa-like warmth. Supporting tones include a muted sage (`#909762`) for botanical or sustainability callouts, a dusty rose (`#f0e7da`) for soft dividers and background sections, and a restrained slate (`#466993`) for secondary text and subtle UI borders. The typography system pairs a refined serif, P22Mackinac, for display and heading roles — lending editorial gravitas to product storytelling — with the clean, modern sans-serif Assistant for body copy, captions, and navigation. Rounded corners are generous but not pill-like: cards use `{rounded.md}` (12px), buttons use `{rounded.sm}` (8px), and the search bar uses `{rounded.full}` (9999px) for a friendly, approachable feel. The brand avoids harsh contrasts; even the darkest ink (`#292929`) is a soft charcoal rather than pure black, and the primary red (`#b82e2e`) is reserved for error states or limited-edition accents. Every design decision — from the `{spacing.section}` (64px) breathing room between product rows to the `{colors.muted-soft}` (#d0dae3) hairline that gently separates footer links — reinforces a sense of unhurried, premium self-care.

colors:
  primary: "#0f4c81"
  primary-active: "#136f99"
  primary-disabled: "#9db2ca"
  ink: "#292929"
  body: "#466993"
  muted: "#9db2ca"
  muted-soft: "#d0dae3"
  hairline: "#dedede"
  hairline-soft: "#dedbd3"
  canvas: "#fefbf1"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#dea439"
  accent-sage: "#909762"
  accent-dusty-rose: "#f0e7da"
  accent-red: "#b82e2e"
  accent-dark-red: "#bb1d2b"
  accent-brown: "#703412"
  accent-sky: "#cee5fa"
  accent-mid-sky: "#1990c6"
  accent-deep-sky: "#007aff"
  accent-dark-navy: "#46759d"
  accent-charcoal: "#121212"
  star-rating: "#dea439"
  error: "#b82e2e"
  success: "#55745b"

typography:
  display-xl:
    fontFamily: "'P22Mackinac', 'Georgia', 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'P22Mackinac', 'Georgia', 'Times New Roman', serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'P22Mackinac', 'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'P22Mackinac', 'Georgia', 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-gold-active:
    backgroundColor: "#c88d2e"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  text-input-placeholder:
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.body}"
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
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  footer-link-hover:
    textColor: "{colors.accent-gold}"
  footer-hairline:
    borderTop: "1px solid {colors.muted-soft}"
  badge-new:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  badge-best-seller:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  testimonial-quote:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    fontStyle: italic
  testimonial-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and key conversion points. Rendered in the brand's deep navy (`{colors.primary}`) with white text (`{colors.on-primary}`) and an 8px rounded corner (`{rounded.sm}`). On hover, the background shifts to a slightly lighter navy (`{colors.primary-active}`) for a subtle lift. The disabled state uses a muted blue-gray (`{colors.primary-disabled}`) and maintains the same typography and padding. Text is uppercase with 0.5px letter spacing for a refined, editorial feel.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". Uses a white canvas background with a 2px solid navy border and navy text. On hover, the background fills with a soft surface tint and the border shifts to the active navy. Padding is 13px 27px to account for the border width, maintaining a consistent 48px height with the primary button.

**`button-gold`** — A special accent button reserved for limited-edition drops, loyalty rewards, or premium upsells. Uses the warm gold (`{colors.accent-gold}`) with dark ink text for high contrast. On hover, the gold deepens to a richer amber. This button signals exclusivity and should be used sparingly.

**`button-ghost`** — A text-only button for tertiary actions like "Cancel" or "Skip". No background or border, just the primary navy text with the same uppercase button typography. Padding is vertical only (14px top/bottom) to align with other buttons in a row.

### Cards
**`product-card`** — The core product display unit, used on collection pages and search results. A white card (`{colors.surface-card}`) with a 12px rounded corner (`{rounded.md}`) and no shadow — the brand relies on generous whitespace and the soft canvas background (`{colors.canvas}`) for separation. The image area has rounded top corners only, creating a clean visual break. The title uses `{typography.title-sm}` in ink, while the price sits below in `{typography.body-md}` in the muted body color. A badge can be overlaid on the image area for "New", "Sale", or "Best Seller" indicators.

**`testimonial-card`** — Used on the homepage and product detail pages to display customer reviews. A soft background (`{colors.surface-soft}`) with 12px rounded corners and generous padding (`{spacing.lg}`). The quote is set in italic body copy, with the author's name in caption style below. No border or shadow — the tonal background provides enough distinction.

### Navigation
**`nav-bar`** — The persistent top navigation, 72px tall with a white canvas background and a soft hairline border at the bottom. Navigation links use `{typography.nav-link}` (uppercase, 14px, weight 600) in the body color. The active link is underlined with a 2px navy bar and the text shifts to the primary navy. The nav bar is fixed on desktop and collapses to a hamburger menu on mobile.

### Forms
**`text-input`** — Standard text input for search, email signup, and checkout forms. A white canvas background with a 1px hairline border and 8px rounded corners. On focus, the border thickens to 2px and turns navy. Error states use a 2px red border (`{colors.error}`). Placeholder text is in the muted blue-gray (`{colors.muted}`). Height is 48px to match button heights for aligned form rows.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) used in the header and on mobile. Slightly more padding than the standard text input (12px 20px) for a more generous feel. On focus, the border becomes a 2px navy line. The search bar is always 48px tall.

### Badges
**`badge-new`** — A small sage-green badge for new product arrivals. Uses `{typography.badge}` (11px, uppercase, weight 700) with 3px 6px padding and 4px rounded corners. The sage color (`{colors.accent-sage}`) signals freshness and aligns with the brand's natural, spa-like identity.

**`badge-sale`** — A red badge for discounted items. Uses the brand's accent red (`{colors.accent-red}`) with white text. Same typography and sizing as the new badge, but the red creates urgency and visual contrast.

**`badge-best-seller`** — A gold badge for top-performing products. Uses the warm gold (`{colors.accent-gold}`) with dark ink text. This badge carries prestige and should be used for products with proven popularity.

### Footer
**`footer`** — The site footer uses the primary navy as a background, creating a strong visual anchor at the bottom of every page. Links are white with the same `{typography.link}` style as the body, and they shift to gold on hover. A subtle hairline separator (`{colors.muted-soft}`) divides link groups. Padding is generous at 48px top/bottom with 24px sides.

### Quantity Selector
**`quantity-selector`** — A compact input for adjusting product quantities on the cart and product detail pages. Uses a soft background (`{colors.surface-soft}`) with 8px rounded corners and 40px height. The typography matches `{typography.body-md}` for consistency with surrounding price and button text.

### Accordion
**`accordion`** — Used on product detail pages for "Details", "Care Instructions", and "Shipping & Returns" sections. Each accordion item has a title in `{typography.title-sm}` with a soft hairline border below. The content area uses `{typography.body-sm}` in the body color with 8px top/bottom padding. No icon is specified — the brand may use a plus/minus or chevron toggle.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, full-width hero, stacked footer links, search bar collapses to icon |
| Tablet | 744–1128px | Two-column product grid, horizontal nav with dropdowns, two-column footer, search bar visible but compact |
| Desktop | 1128–1440px | Three-column product grid, full horizontal nav, three-column footer, full search bar with placeholder text |
| Wide | > 1440px | Max-width container (1440px) centered, four-column product grid, expanded hero with larger typography |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines.
- Product card images are tappable and link to the product detail page.
- Accordion headers have a minimum tap area of 48px height.
- Navigation links have 16px horizontal padding for comfortable tapping.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu on mobile (< 744px). The logo remains centered, and the cart icon is always visible.
- The product grid collapses from four columns on wide screens to a single column on mobile.
- The footer collapses from a multi-column layout on desktop to a stacked single column on mobile.
- The search bar collapses to a magnifying glass icon on mobile, expanding to a full input on tap.
- Hero sections reduce padding and font sizes on mobile, with the title dropping from `{typography.display-xl}` (42px) to `{typography.display-md}` (28px).

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons, ghost buttons, and text inputs could not be reliably extracted from the live site. The values provided are based on common patterns and the brand's color system.
- Error styling for forms (error messages, error icon placement) was not observed. The error border color is inferred from the brand's accent red.
- Focus ring styles (outline, box-shadow) were not consistently visible. A 2px navy outline is assumed for accessibility but not confirmed.
- Dark mode is not supported on the live site. All colors are light-mode only.
- Sub-brand or collection-specific palettes (e.g., limited-edition drops) were not observed. The main palette should cover all standard use cases.
- Typography scale for mobile (smaller font sizes) was not explicitly observed. The responsive behavior section includes reasonable reductions.
- Animation and transition durations (e.g., button hover, accordion expand) were not extracted. A standard 200ms ease-in-out is assumed.
- The `swiper-icons` font family was observed but not used in any component. It may be used for carousel navigation arrows.
- The `Block Quote` and `Cadiz` font families were observed but not used in any primary component. They may be used in editorial content or legacy pages.
- The `T5` and `T6` font families were observed but not mapped. They may be internal Shopify theme references.
