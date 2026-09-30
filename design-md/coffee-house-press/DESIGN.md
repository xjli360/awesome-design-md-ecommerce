---
version: alpha
name: "Coffee House Press"
source_url: "https://www.coffeehousepress.org"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A literary publisher whose identity is built on the warmth of a deep, roasted brown — `#77471f` — a color that reads as book-cloth, coffee stain, and library shelf all at once. The palette is grounded in earthy browns (`#40220a`, `#3e220c`, `#855935`) and softened by a dusty rose (`#9a6372`) and a pale stone (`#d6c8bc`), creating a mood that is serious but not severe, literary but not academic. The canvas is a clean `#f7f7f7` rather than pure white, lending a slightly tactile, paper-like quality to the background. Typography leans on a single, readable sans-serif stack, with display sizes kept modest — the brand trusts its words and the space around them over typographic spectacle. Navigation is minimal: a simple left-aligned logo, a compact menu, and a search icon. The site structure prioritizes books and authors, with generous vertical spacing (`{spacing.section}`) between content blocks and soft card containers (`{rounded.sm}`) for book covers and author photos. There are no hard corners on interactive elements — buttons and inputs use `{rounded.sm}` — but the overall feel is restrained and editorial, not playful. The extracted palette includes a range of grays (`#616161`, `#5d5d5d`, `#424242`) that serve as text and border colors, maintaining readability without harsh contrast. The brand's voice is one of quiet authority: it does not shout, but it is unmistakably present.

colors:
  primary: "#77471f"
  primary-active: "#40220a"
  primary-disabled: "#a07e62"
  ink: "#1d1d1d"
  body: "#424242"
  muted: "#616161"
  muted-soft: "#686868"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f7f7f7"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rose: "#9a6372"
  accent-stone: "#d6c8bc"
  accent-warm: "#a7876d"
  accent-dark: "#1f1919"
  accent-deep: "#121212"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 0"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 0"
    borderBottom: "2px solid {colors.primary}"
  search-icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
    opacity: 0.85
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  badge:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for key actions like "Add to Cart" or "Subscribe." Background is `{colors.primary}` with white text in uppercase. On hover, shifts to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}`. All states share `{rounded.sm}` and a 44px height for touch accessibility.

**`button-secondary`** — An outlined alternative for secondary actions. Uses a white background with a 2px `{colors.primary}` border and primary-colored text. Hover state fills the background with `{colors.primary}` and inverts text to white. Disabled state uses `{colors.hairline}` border and `{colors.muted}` text.

**`button-text`** — A text-only button for inline actions like "Read More" or "View All." No background or border, uses `{colors.primary}` text. Hover adds an underline. Used sparingly within body copy or card footers.

### Cards
**`product-card`** — The standard container for book listings. White background with `{rounded.sm}`, subtle shadow on hover. Contains a book cover image (with `{rounded.xs}`), the title in `{typography.title-md}`, and the author name in `{typography.body-sm}` with `{colors.muted}`. Padding is `{spacing.base}` around all content.

**`product-card-image`** — The book cover image within a card. Uses `{rounded.xs}` for a slight softening of corners, maintaining the brand's gentle but not overly rounded aesthetic.

### Navigation
**`nav-bar`** — The top navigation bar, fixed at 72px height. Background is `{colors.canvas}` with left-aligned logo and right-aligned navigation links and search icon. Links use `{typography.nav-link}` in uppercase with 0.5px letter spacing.

**`nav-link`** — Individual navigation items. Default state is `{colors.ink}` text. Active state uses `{colors.primary}` text with a 2px bottom border in the same color. Hover state subtly darkens the text.

**`search-icon-button`** — A circular icon button for the search function. Uses `{rounded.full}` and a muted icon color. On focus, expands into a `{text-input}` style search bar.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and contact forms. White background with `{colors.hairline}` border and `{rounded.sm}`. On focus, border shifts to `{colors.primary}`. Height is 48px for comfortable touch interaction.

### Hero
**`hero-section`** — The primary hero banner, typically on the homepage. Uses `{colors.primary}` as background with white text. Vertical padding is `{spacing.section}`, creating a generous, immersive space. May include a background pattern or subtle texture.

**`hero-title`** — The main headline in the hero, using `{typography.display-xl}`. White text on the dark background ensures high contrast and readability.

**`hero-subtitle`** — Supporting text below the hero title. Uses `{typography.body-md}` with 85% opacity for a softer, secondary feel.

### Footer
**`footer`** — The site footer, using `{colors.ink}` as background for a strong visual anchor. Text is `{colors.muted-soft}` for readability without harsh contrast. Links use `{colors.muted-soft}` and lighten on hover. Contains copyright, social links, and navigation.

### Badges
**`badge`** — Small informational badges for labels like "New Release" or "Award Winner." Uses `{colors.accent-rose}` background with white text. Compact padding (2px 8px) and `{rounded.xs}` for a subtle, non-distracting presence.

### Section Headers
**`section-header`** — Headers for content sections (e.g., "Featured Books," "Upcoming Events"). Uses `{typography.display-md}` with `{colors.ink}`. Bottom margin of `{spacing.lg}` separates it from the content below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; hero padding reduces to `{spacing.xl}`; product cards stack vertically; font sizes reduce by 2px for display levels |
| Tablet | 744–1128px | Two-column grid for product cards; nav remains visible but compact; hero uses `{spacing.section}` padding; font sizes at default |
| Desktop | 1128–1440px | Three-column grid for product cards; full nav with all links visible; hero uses full `{spacing.section}` padding; maximum content width of 1128px |
| Wide | > 1440px | Content max-width of 1440px with centered layout; additional whitespace on sides; four-column grid for product cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum height of 44px for touch accessibility
- Icon buttons (search, social) are at least 40px × 40px
- Navigation links have 8px vertical padding for comfortable tapping
- Product cards have 16px padding around touchable content

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu icon
- The search bar collapses to an icon on mobile, expanding to full width on tap
- Multi-column grids collapse to single column on mobile
- Hero content stacks vertically on mobile (title above subtitle)
- Footer links collapse from inline to stacked on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found on the live site; the typography block uses a generic sans-serif stack (`'Helvetica Neue', Helvetica, Arial, sans-serif`) as a best-guess fallback. The actual brand font may differ.
- Hover and focus states for most components (beyond buttons) could not be reliably extracted from the live site CSS.
- Error states for form inputs (validation, error messages) are not documented.
- Dark mode or high-contrast mode styling is not present in the extracted data.
- Sub-brand or series-specific color palettes (e.g., for specific book collections or events) are not captured.
- The extracted color list includes many neutral grays that may be framework defaults rather than intentional brand choices; the most distinctive colors (`#77471f`, `#9a6372`, `#d6c8bc`) are treated as the core brand palette.
- Animation and transition timings (e.g., hover fade duration, menu slide speed) are not available.
- The Shopify checkout widget colors (if present in extraction) have been excluded from the brand palette.
- Social media icon colors (e.g., Facebook blue, Twitter blue) have been excluded from the brand palette.
