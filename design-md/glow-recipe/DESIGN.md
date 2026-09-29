---
version: alpha
name: "Glow Recipe"
source_url: "https://www.glowrecipe.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Glow Recipe is a fruit-powered skincare brand that feels like a farmer's market for your face—vibrant, juicy, and unapologetically playful. The palette is anchored by a soft, airy canvas of `#f4f4f6` and `#e5e5e5`, with pops of electric energy from `#992ae3` (a bold purple) and `#ffcf2a` (a sunny yellow), evoking the brand's signature watermelon, blueberry, and avocado ingredients. Deep navy `#272d45` and `#2c3e50` provide grounding contrast, while teal accents like `#0e7a82` and `#1990c6` hint at hydration and dewiness. The typography leans on Josefin Sans, a geometric sans-serif with a touch of elegance, used at modest weights to keep the focus on product photography and ingredient storytelling. Rounded corners are generous—cards use `{rounded.lg}` (20px) and buttons use `{rounded.sm}` (8px)—creating a soft, approachable feel that mirrors the brand's "clinically effective, fruit-powered" ethos. The overall mood is fresh, optimistic, and slightly whimsical, with a clean grid that lets colorful product shots and playful badges (like "NEW" or "Best Seller") take center stage. Every design choice whispers "glow," from the muted `#d3d4dd` hairlines to the `#b2f9e9` accent that recalls a dewy finish.

colors:
  primary: "#992ae3"
  primary-active: "#7a1fb5"
  primary-disabled: "#d4a3f1"
  ink: "#272d45"
  body: "#2c3e50"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#d3d4dd"
  hairline-soft: "#e5e5eb"
  canvas: "#f4f4f6"
  surface-soft: "#e5e5e5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffcf2a"
  accent-teal: "#0e7a82"
  accent-teal-light: "#b2f9e9"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  badge-new: "#992ae3"
  badge-best-seller: "#ffcf2a"
  star-rating: "#ffcf2a"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: 0
  badge:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
  link:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
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
    padding: 14px 24px
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
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
    border: "1px solid {colors.hairline}"
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
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-best-seller:
    backgroundColor: "{colors.badge-best-seller}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and "Subscribe". It uses a bold purple `{colors.primary}` background with white text, soft 8px rounded corners, and a 48px height for easy tapping. On hover, it shifts to `{colors.primary-active}` for a subtle depth cue. The disabled state uses `{colors.primary-disabled}` to signal inactivity without losing brand identity.

**`button-secondary`** — A ghost-like alternative for less prominent actions like "Learn More" or "View Details". It sits on a white canvas with ink text and a thin hairline border, maintaining the same 48px height and 8px radius for consistency. Hover adds a subtle background tint from `{colors.surface-soft}`.

**`button-tertiary`** — A text-only button for inline actions like "Cancel" or "Skip". It uses transparent background and primary purple text, with no border or padding changes. Hover adds an underline to reinforce clickability.

**`button-pill`** — A playful, fully rounded variant used for promotional badges, "Quick Add", or filter tags. It uses the same purple background but with a compact 40px height and 10px horizontal padding, making it feel like a sticker or tag.

**`button-pill-outline`** — The outlined counterpart to the pill button, used for "Size" selectors or "Variant" toggles. It has a white background, ink text, and a hairline border, with the same full-round shape.

### Cards
**`product-card`** — The core product display unit, used in grid layouts and carousels. It features a white background, 20px rounded corners, and 16px padding. The image area is a 1:1 square with 12px rounded corners, ensuring a consistent crop for product photography. The title uses `{typography.title-sm}` and the price uses `{typography.body-md}` in `{colors.body}`. On hover, a subtle shadow or border change (not yet defined) could be added.

**`hero-banner`** — A full-width promotional section for new launches or seasonal campaigns. It uses the soft `{colors.surface-soft}` background and large `{typography.display-lg}` text, with generous padding of 64px top/bottom and 32px sides. The CTA button sits below with extra margin, inviting interaction.

### Navigation
**`nav-bar`** — The persistent top navigation bar, 72px tall with a white background and a thin bottom border. Links use `{typography.nav-link}` in uppercase with 0.5px letter spacing. The active link is underlined with a 2px purple border, and the logo sits on the left with a cart icon on the right.

**`nav-link-active`** — The active state for navigation links, using primary purple text and a 2px bottom border. This creates a clear visual anchor for the current page or section.

### Forms
**`text-input`** — Standard input fields for search, email signup, and checkout forms. They have a white background, 8px rounded corners, 48px height, and a thin hairline border. On focus, the border switches to `{colors.primary}` purple for clear visual feedback.

**`search-bar`** — A specialized pill-shaped input for site search, with full 9999px rounding and a 48px height. It sits on a white background with a hairline border, and the placeholder text uses `{colors.muted}`.

### Badges
**`badge`** — Used for "NEW", "Limited Edition", or "Bestseller" labels on product cards. It's a small, fully rounded pill with purple background and white uppercase text. The compact padding (4px top/bottom, 10px left/right) ensures it sits neatly on product images without overwhelming the design.

**`badge-best-seller`** — A yellow variant for "Best Seller" badges, using `{colors.accent-yellow}` background and ink text. This creates a visual hierarchy where purple signals novelty and yellow signals popularity.

### Footer
**`footer`** — The site footer uses a dark navy `{colors.ink}` background with white text for maximum contrast. Links are muted to `{colors.muted-soft}` and turn white on hover. The layout typically includes columns for "Shop", "Learn", "Support", and social links, with generous padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid, nav collapses to hamburger menu, product cards stack vertically, hero banner reduces padding to 32px, buttons become full-width |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, hero banner uses 48px padding, search bar collapses to icon-only |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with all links, hero banner at full 64px padding, search bar expands with input field |
| Wide | > 1440px | Max-width container (1440px) centered, product grid expands to four columns, hero banner uses larger typography (display-xl) |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for tap targets on mobile.
- Product card CTAs are at least 48px tall to meet accessibility guidelines.
- Nav bar links have 16px padding on all sides for easy tapping.
- Search bar and text inputs are 48px tall for comfortable touch interaction.

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu with a slide-out drawer.
- The product filter sidebar (if present) collapses to a bottom sheet or modal on mobile.
- The footer collapses from a multi-column layout to a single column with accordion-style sections.
- Hero banners reduce image height and text size to avoid vertical overflow.
- Product carousels switch from multi-item to single-item scroll on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow, border, or overlay) were not reliably extracted from the live site.
- Error styling for form inputs (red borders, error messages) is not defined; assume standard red (`#c13515`) for error text.
- Dark mode palette is not available; the brand currently uses a light-only theme.
- Sub-brand or seasonal palettes (e.g., holiday, limited edition) are not captured.
- Typography weights for Josefin Sans are assumed based on common usage; exact font files and weights (e.g., 300, 400, 500, 600, 700) need verification.
- Animation and transition durations (e.g., button hover, card lift) are not specified; a default of 200ms ease-in-out is recommended.
- Iconography style (line vs. filled, stroke width) is not defined; assume a consistent 2px stroke for outlined icons.
- Spacing values for specific components (e.g., product card gap in grid) are inferred from common patterns; exact values may vary.
