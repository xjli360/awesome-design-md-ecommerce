---
version: alpha
name: "Elusive Disc"
source_url: "https://www.elusivedisc.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage audiophile marketplace that signals its passion through a raw, unapologetic palette anchored on signal yellow (#ffff00) — a color so loud it would be reckless in any other context, but here it reads as the visual equivalent of a needle drop onto virgin vinyl. The brand’s primary accent, a deep crimson (#a92504) that recalls vintage Marantz glow, appears on CTAs and price tags, while a teal (#6e9aa7) and a cooler cyan (#42ceed) add unexpected mid-century hi-fi flavor. The canvas is a near-black (#161015) — not a safe dark gray, but a true void that makes every album cover, SACD jewel case, and turntable photo float like an illuminated object in a listening room. Oswald, a condensed sans-serif with Germanic precision, runs across the site in all-caps navigation, product titles, and badge copy, lending a slight broadcast-engineering feel. Buttons are sharp-cornered rectangles (`{rounded.none}`), not friendly pills — this is a brand that values signal over softness. The product grid uses generous white borders (`{spacing.base}`) between items, creating a rhythm that mimics LP spines on a shelf. Search is a full-width bar with a yellow submit orb (`{rounded.full}`), the only pill in the system, acting as a tuning dial. The footer collapses into dense, monochrome link stacks — no decorative imagery, just information density. Elusive Disc doesn’t whisper; it sends a clean, hot signal straight to the amp.

colors:
  primary: "#ffff00"
  primary-active: "#e6bb25"
  primary-disabled: "#f6ea4c"
  ink: "#161015"
  body: "#222222"
  muted: "#444444"
  muted-soft: "#6e9aa7"
  hairline: "#b2b7bb"
  hairline-soft: "#d8503a"
  canvas: "#ffffff"
  surface-soft: "#f6ea4c"
  surface-card: "#ffffff"
  on-primary: "#161015"
  accent-crimson: "#a92504"
  accent-teal: "#6e9aa7"
  accent-cyan: "#42ceed"
  accent-orange: "#ff8710"
  accent-purple: "#330033"
  accent-blue-deep: "#1f2454"
  accent-blue-navy: "#002764"
  accent-green: "#07a80b"
  accent-red: "#e61d25"
  accent-gold: "#edc114"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Oswald', 'Impact', 'Arial Black', sans-serif"
    fontSize: 42px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Oswald', 'Impact', 'Arial Black', sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: 0
  display-md:
    fontFamily: "'Oswald', 'Impact', 'Arial Black', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0
  title-md:
    fontFamily: "'Oswald', 'Impact', 'Arial Black', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Oswald', 'Impact', 'Arial Black', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0
  badge:
    fontFamily: "'Oswald', 'Impact', 'Arial Black', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Oswald', 'Impact', 'Arial Black', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Oswald', 'Impact', 'Arial Black', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  nav-link:
    fontFamily: "'Oswald', 'Impact', 'Arial Black', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-accent-crimson:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-pill-search:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-crimson}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    height: 44px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-crimson}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-format:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a sharp-cornered rectangle in signal yellow (`{colors.primary}`) with dark ink text. On hover, it shifts to a deeper gold (`{colors.primary-active}`). The disabled state uses a paler yellow (`{colors.primary-disabled}`) with reduced contrast. All primary buttons use Oswald uppercase at 16px with 1px letter-spacing — no rounded corners, no shadows, just a flat, confident block of color.

**`button-secondary`** — An outlined or ghost variant on a white canvas with ink text and a 1px hairline border (`{colors.hairline}`). Active state fills with the soft yellow surface (`{colors.surface-soft}`). Used for "Add to Wishlist" and secondary product actions.

**`button-accent-crimson`** — A high-emphasis variant for "Buy Now" or limited-edition drops. Uses the deep crimson (`{colors.accent-crimson}`) background with white text. Same sharp-cornered geometry as the primary button, but the color signals urgency and premium status.

**`button-pill-search`** — The only pill-shaped element in the system, used exclusively for the search submit orb. Yellow background, dark text, `{rounded.full}`. This is the tuning dial — the one soft shape in an otherwise angular interface.

### Navigation
**`nav-bar`** — A fixed 60px white bar at the top, housing the logo (typically a text-based wordmark), category links, and a search icon. The bar has a 1px bottom hairline (`{colors.hairline}`). No background color change on scroll — the bar stays white for maximum legibility against the dark product grid.

**`nav-link`** — Oswald uppercase at 15px with 1px letter-spacing. Hover state adds a subtle underline or a color shift to the crimson accent (`{colors.accent-crimson}`). Active page links use the same crimson. Links are spaced with `{spacing.base}` padding on each side.

### Cards
**`product-card`** — A white card with no border radius, containing a product image (typically a high-res album cover or equipment photo), the title in Oswald uppercase (`{typography.title-sm}`), the price in crimson (`{colors.accent-crimson}`), and optional badges. Cards sit in a grid with `{spacing.base}` gaps, creating a shelf-like rhythm. No box shadow — the white card against the dark canvas (`{colors.canvas}`) provides enough separation.

**`badge-new`** — A small yellow rectangle (`{colors.primary}`) with dark text, placed in the top-left corner of a product card. Used for new arrivals. No rounding.

**`badge-sale`** — A crimson rectangle (`{colors.accent-crimson}`) with white text, signaling a discount or clearance item.

**`badge-format`** — A teal rectangle (`{colors.accent-teal}`) with white text, indicating the format (SACD, Vinyl, DVD-A, etc.). This is a brand-specific token that helps users quickly scan for their preferred medium.

### Forms
**`text-input`** — A sharp-cornered white input with a 1px hairline border (`{colors.hairline}`). Focus state uses a 2px crimson border (`{colors.accent-crimson}`) and removes the default outline. Used for search, newsletter signup, and checkout fields. Height is 44px with 10px 12px padding.

**`search-bar`** — A full-width white input field with no rounding, placed in the header or hero area. The submit button is the pill-shaped yellow orb (`button-pill-search`). The input itself uses body-md typography (Helvetica Neue, 15px) for readability.

### Hero
**`hero-banner`** — A full-width section with a near-black background (`{colors.ink}`) and white text, featuring a large Oswald display headline (`{typography.display-lg}`). Often includes a single product image or a stylized graphic. The hero CTA is a yellow button (`{hero-cta}`) with generous padding (14px 32px).

### Footer
**`footer-section`** — A dense, dark footer (`{colors.ink}`) with white headings in Oswald uppercase (`{typography.title-sm}`) and teal-tinted body links (`{colors.muted-soft}`). Links are stacked vertically in columns (Customer Service, My Account, Quick Links, Newsletter). No decorative imagery — just information density. The newsletter signup uses a standard text input with a yellow submit button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items per row), nav collapses to hamburger, hero text reduces to 24px, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but reduced padding, hero maintains 32px headline |
| Desktop | 1128–1440px | Three-column product grid, full nav with all category links, hero at 42px display-xl, footer in 4-column layout |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero may include side panel for featured product |

### Touch Targets
- All buttons and links maintain a minimum 44px height for touch accessibility.
- Search bar is full-width on mobile (no pill submit, replaced by a keyboard return action).
- Nav hamburger icon is a 44x44px tap target with adequate spacing from other elements.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu. The search bar moves below the nav or into a slide-down panel.
- The product grid collapses from 4 columns (wide) to 1 column (mobile). Badges remain visible but may stack vertically on very small cards.
- The footer collapses from 4 columns to a single vertical stack on mobile, with accordion-style expandable sections for link groups.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states** for most interactive elements (buttons, links, cards) could not be reliably extracted from static CSS. The active states provided are best guesses based on color relationships.
- **Error and validation styling** for forms (red borders, error messages) is not present in the extracted data. A crimson accent (`{colors.accent-crimson}`) is a reasonable candidate for error states.
- **Focus ring styles** are not defined. The system likely uses a 2px crimson outline or a subtle yellow glow, but this is unconfirmed.
- **Dark mode** is not supported. The brand uses a near-black canvas (`{colors.ink}`) for hero sections and footer, but the main interface is white.
- **Sub-brand or promotional palettes** (e.g., holiday sales, genre-specific landing pages) are not captured. The extracted colors include many accents (orange, purple, green, gold) that may belong to promotional banners or third-party widgets.
- **Typography scale** for body text is inferred from common e-commerce patterns. The exact font sizes for body-md and body-sm may vary on the live site.
- **Spacing values** are based on common grid systems. The actual `{spacing.section}` may be 80px or 96px on the live site.
- **The extracted color list is unusually large (27 hex values)** and includes many that are likely from third-party widgets (payment badges, social icons, stock images). The primary yellow (`#ffff00`) and crimson (`#a92504`) are the most distinctive and brand-consistent colors. The teal (`#6e9aa7`) and cyan (`#42ceed`) are used for format badges and secondary accents. The remaining colors (blues, greens, oranges, purples) are noted as potential promotional or widget colors but are included in the palette for reference.
