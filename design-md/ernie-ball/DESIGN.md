---
version: alpha
name: "Ernie Ball"
source_url: "https://www.ernieball.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A high-voltage pink — #ff10a4 — is the first thing you see on Ernie Ball’s site, and it’s a deliberate jolt. This is not a pastel or a blush; it’s a neon magenta that reads as electric, youthful, and unapologetically loud, sitting atop a near-black ink (#121212) and a deep royal blue (#003399) that recalls the brand’s California heritage and the cobalt of a perfect sky. The palette is lean and confrontational: the pink owns every primary CTA, every “Shop Now” button, every sale badge, while the grays (#d0d0d0, #c2c2c2, #aaaaaa) and warm browns (#403629, #241912) ground the system in the material world of guitar wood, leather straps, and road-worn cases. Type runs Gotham SSm, a geometric sans-serif that feels both muscular and precise — the same font that brands like Spotify and Airbnb use for its clean, no-nonsense readability. Display headlines sit at moderate weights (500–600) rather than heavy 700+, letting the pink and the product photography do the heavy lifting. Buttons are softly rounded (`{rounded.sm}` ~8px), never pill-shaped — the brand prefers a slight shoulder over a full radius, keeping things purposeful without feeling overly friendly. Product cards use a crisp white canvas (`{colors.canvas}`) with a thin hairline (`{colors.hairline}`) and generous padding, letting the strings, picks, and straps breathe. The overall mood is a backstage pass: loud where it needs to be, serious where it counts, and always, always in tune.

colors:
  primary: "#ff10a4"
  primary-active: "#d6008a"
  primary-disabled: "#ffb3dc"
  ink: "#121212"
  body: "#403629"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#d0d0d0"
  hairline-soft: "#ebebeb"
  canvas: "#fafafa"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#003399"
  accent-brown: "#241912"
  accent-warm: "#c2c2c2"
  star-rating: "#e91e63"
  sale-badge: "#ff10a4"

typography:
  display-xl:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham SSm A', 'Gotham SSm B', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    borderColor: "{colors.ink}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 48px
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-dark:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, filled with the signature pink `#ff10a4` and white uppercase Gotham text. On hover, it shifts to `{colors.primary-active}` (`#d6008a`) for a slightly deeper, more urgent tone. The disabled state uses `{colors.primary-disabled}` (`#ffb3dc`), a washed-out pink that signals unavailability without visual noise. **`button-secondary`** — An outlined or filled white button with black text, used for secondary actions like “Learn More” or “View Details.” The outline variant (`button-secondary-outline`) uses a 1px solid `{colors.ink}` border on a transparent background, inverting to a filled state on hover. **`button-tertiary-text`** — A text-only button in the primary pink, used for inline actions like “See All” or “Add to Cart” within product cards.

### Cards
**`product-card`** — A clean white card with `{rounded.sm}` corners and `{spacing.base}` padding. The product image sits at the top with matching corner radius, followed by the product title (`{typography.title-sm}`) and price (`{typography.body-sm}` in `{colors.body}`). A `sale-badge` component overlays the top-left corner of the image when applicable, using the signature pink background and uppercase white badge text. Cards are designed to sit in a responsive grid with `{spacing.base}` gaps between them.

### Navigation
**`nav-bar`** — A fixed-height 60px bar with a near-black background (`{colors.ink}`) and white uppercase nav links. The brand logo sits left-aligned, while links like “Strings,” “Accessories,” “Artists,” and “Shop” are spaced evenly. The active link uses the signature pink (`{colors.primary}`) for the text color. On mobile, the nav collapses into a hamburger menu with a full-screen overlay. **`category-strip`** — A secondary navigation bar below the hero, used for filtering product categories. Active tabs use pink text, inactive tabs use `{colors.muted}`.

### Forms
**`text-input`** — A standard input field with a white background, `{rounded.sm}` corners, and 12px/16px padding. On focus, the border switches from `{colors.hairline}` to `{colors.primary}`, providing a clear visual cue. Input text uses `{typography.body-md}` in `{colors.body}`. The height is fixed at 48px for comfortable touch targeting.

### Hero
**`hero-section`** — A full-width section with a near-black background (`{colors.ink}`) and white display text. The hero typically features a large product image or lifestyle shot on one side and a headline with a `hero-cta` button on the other. The CTA uses the signature pink and uppercase button text, with generous padding for visual weight.

### Footer
**`footer`** — A dark section (`{colors.ink}`) with white and muted-gray links. Links use `{typography.link}` in `{colors.muted-soft}` (`#aaaaaa`) and shift to white on hover. The footer is divided into columns for “Products,” “Support,” “Company,” and “Connect,” with a copyright line at the bottom.

### Badges & Dividers
**`sale-badge`** — A small, uppercase badge in the signature pink, used to flag discounted items. **`divider`** — A 1px horizontal line in `{colors.hairline}` (`#d0d0d0`), used to separate sections. **`divider-soft`** — A lighter variant in `{colors.hairline-soft}` (`#ebebeb`), used within cards or lists.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero stacks vertically; buttons go full-width; font sizes scale down 2-4px |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 60/40 split; side padding increases to 24px |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero uses 50/50 split; max-width container at 1200px |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero expands to full bleed with larger imagery |

### Touch Targets
- All interactive elements (buttons, inputs, links) have a minimum height of 44px to meet WCAG touch-target guidelines.
- Icon buttons are 40px × 40px with a `{rounded.full}` hit area.
- Nav links have a minimum 44px tap area, even when text is smaller.

### Collapsing Strategy
- The primary nav collapses into a hamburger menu below 744px, with a full-screen overlay for link selection.
- The category strip collapses into a horizontal scrollable row on mobile, with no visible overflow.
- The footer columns stack vertically on mobile, with each section expanding via accordion toggle.
- Product cards switch from a grid to a single-column list on mobile, with full-width images.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs, links, and secondary buttons could not be reliably extracted from the static HTML/CSS. The active states defined above are inferred from common patterns.
- Error and validation styling (e.g., red borders, error messages) is not present in the extracted data. A standard red (`#e91e63` from the extracted list) is used for star ratings but may not be the official error color.
- The extracted color list includes several grays (`#d0d0d0`, `#c2c2c2`, `#aaaaaa`, `#bbbbbb`, `#c1c1c1`) that may represent different border, background, or text-muted roles. The mapping above is an educated guess; the brand may use a more specific hierarchy.
- The `#e91e63` (pinkish-red) appears in the extracted list and is used here for star ratings, but its exact role (e.g., sale badge, error state, or accent) is unconfirmed.
- No dark mode or high-contrast mode tokens were found. The brand may not support these yet.
- Sub-brand or collection-specific palettes (e.g., “Cobalt” strings, “Slinky” series) are not captured.
- The font stack includes `inherit` as a fallback, which is unusual. The primary font is assumed to be Gotham SSm based on the extracted declarations, but the exact weight and style variations (e.g., italic, condensed) are unknown.
- Animation and transition durations (e.g., button hover, card lift) are not specified. A standard 200ms ease-in-out is recommended for all interactive states.
