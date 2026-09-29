---
version: alpha
name: "CGE (Czech Games Edition)"
source_url: "https://czechgames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A board-game publisher whose identity is built on a deep, warm darkness — #16140e, a near-black brown that reads like a game-box interior or a well-worn tabletop, not the cold #111111 of digital-first brands. Against this ink, the brand deploys a tight, saturated palette of accents: #d80027 (a stop-sign red), #00a8c5 (a cyan that recalls ocean tiles in a strategy game), #fcc003 (a marigold yellow for highlights), and #ff7640 (a burnt orange for secondary energy). The canvas is #f0f0f0, a soft off-white that avoids the sterile glare of pure white, while #7a7a7a provides a muted middle ground for body text and secondary labels. The system uses generous {rounded.sm} (8px) on buttons and {rounded.md} (12px) on cards, a subtle softening that prevents the interface from feeling sharp or aggressive — appropriate for a brand that sells hours of focused, social play. The typography, while not fully extracted, likely favors a clean sans-serif for readability across rulebooks and digital storefronts. The overall mood is that of a well-lit game night: the tabletop is dark, the components are bright, and the focus is on the players, not the chrome.

colors:
  primary: "#d80027"
  primary-active: "#b0001f"
  primary-disabled: "#f0a0a8"
  ink: "#16140e"
  body: "#7a7a7a"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#d0d0d0"
  hairline-soft: "#e0e0e0"
  canvas: "#f0f0f0"
  surface-soft: "#f8f9f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#00a8c5"
  accent-yellow: "#fcc003"
  accent-orange: "#ff7640"
  accent-blue: "#0052b4"
  accent-green: "#466442"
  accent-purple: "#73447f"
  accent-maroon: "#632244"

typography:
  display-xl:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
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
    padding: 12px 24px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
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
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: 64px 24px
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-expansion:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  rating-stars:
    color: "{colors.accent-yellow}"
    size: 16px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 40px
  tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand's stop-sign red (#d80027) on a white label. On hover, it deepens to `{colors.primary-active}` (#b0001f). The disabled state uses `{colors.primary-disabled}` (#f0a0a8) — a pale pink that clearly signals inactivity without clashing. All buttons share `{rounded.sm}` (8px) for a soft, approachable feel.

**`button-secondary`** — A ghost-style button on the `{colors.canvas}` background, with `{colors.ink}` text. On hover, it gains a `{colors.hairline-soft}` background. Used for secondary actions like "View Details" or "Cancel."

**`button-ghost`** — A fully transparent button with `{colors.ink}` text, used for tertiary actions or in dense UI areas where a full button would be too heavy. Hover adds a subtle background tint.

**`button-accent-cyan`** — A secondary accent button using `{colors.accent-cyan}` (#00a8c5), used for actions related to expansions or digital components. Text is white.

**`button-accent-yellow`** — A high-energy accent button using `{colors.accent-yellow}` (#fcc003), used for promotional actions or "Add to Cart" on sale items. Text is `{colors.ink}` for contrast.

### Cards
**`product-card`** — The core product display unit, a white card (`{colors.surface-card}`) with `{rounded.md}` (12px) and 16px padding. The product image sits at the top with `{rounded.sm}`, followed by the title, a `{typography.badge}` for status (new, sale, expansion), and the price in `{colors.primary}`. The card is designed to feel like a game box on a shelf.

**`product-card-badge`** — A small, uppercase label pinned to the top-left of the product image. Uses `{colors.accent-yellow}` for "New" or "Sale" and `{colors.accent-cyan}` for "Expansion." The `{rounded.xs}` (4px) keeps it sharp but not aggressive.

### Navigation
**`nav-bar`** — A dark, full-width bar using `{colors.ink}` (#16140e) as the background, with white nav links. The height is 64px, providing a solid, grounded top edge. The logo sits on the left, and navigation links are spaced with `{spacing.lg}`.

**`nav-link`** — White text on the dark nav bar. The active state uses `{colors.primary}` (#d80027) as the text color, creating a clear visual anchor for the current page.

### Forms
**`text-input`** — A standard input field on `{colors.canvas}` with `{colors.ink}` text. The focus state gains a `{colors.primary}` border. The error state also uses `{colors.primary}` as a border, paired with an error message in the same red. Height is 48px for comfortable tap targets.

### Hero
**`hero-section`** — A full-width hero using `{colors.ink}` as the background, creating a dramatic, immersive entry point. The heading uses `{typography.display-xl}` in white, and the subheading uses `{typography.body-md}` in `{colors.muted-soft}` (#a0a0a0). Padding is 64px top/bottom, 24px sides.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) on a white background, used for filtering games by name or mechanic. The 48px height and 12px/20px padding make it feel generous and easy to use.

### Footer
**`footer`** — A dark footer matching the nav bar (`{colors.ink}`), with links in white and body text in `{colors.muted-soft}`. Links use `{typography.link}` (14px, regular weight). Padding is 48px top/bottom.

### Badges & Tags
**`badge-new`** — A cyan badge for newly released games. Uses `{colors.accent-cyan}` background with white uppercase text.
**`badge-sale`** — A red badge for discounted games. Uses `{colors.primary}` background with white uppercase text.
**`badge-expansion`** — A purple badge for expansion packs. Uses `{colors.accent-purple}` background with white uppercase text.
**`tag`** — A pill-shaped tag (`{rounded.full}`) on `{colors.surface-soft}` with `{colors.ink}` text, used for game mechanics, player counts, or play times.

### Dividers
**`divider`** — A standard 1px line in `{colors.hairline}` (#d0d0d0), used between sections.
**`divider-soft`** — A lighter 1px line in `{colors.hairline-soft}` (#e0e0e0), used within cards or lists.

### Icons
**`icon-button`** — A transparent circular button (40px) with a white icon, used on dark backgrounds like the hero or nav bar.
**`icon-button-dark`** — A dark circular button (40px) with a white icon, used on light backgrounds like the product card.

### Rating
**`rating-stars`** — A 5-star rating display using `{colors.accent-yellow}` (#fcc003) for filled stars. Each star is 16px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero padding reduces to 48px 16px; search bar becomes full-width. |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero text scales down to `{typography.display-lg}`; search bar is 60% width. |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero uses `{typography.display-xl}`; search bar is 40% width. |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with max-width 1200px. |

### Touch Targets
- All buttons and interactive elements are at least 48px tall to meet WCAG touch-target guidelines.
- Icon buttons are 40px, with 8px padding around the icon.
- Nav links have a minimum tap area of 44px x 44px.
- Product card images are tappable, with a minimum height of 200px.

### Collapsing Strategy
- On mobile, the top nav collapses into a hamburger menu. The logo remains centered.
- The category filter strip (if present) collapses into a horizontal scrollable row on mobile.
- The footer link columns collapse into a single vertical stack on mobile.
- Product card badges remain visible on all breakpoints, but their text may truncate on very small screens.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The exact font family could not be extracted from the live site (only "swiper-icons" was found). The typography block uses "Inter" as a reasonable, clean sans-serif assumption for a board-game publisher. The actual brand font may differ.
- Hover states for most components (beyond buttons) were not extracted and are inferred from common patterns.
- Error styling for forms (beyond the red border) was not extracted. Error message typography and iconography are assumed.
- Dark mode is not defined. The brand's heavy use of `{colors.ink}` (#16140e) suggests a natural dark-mode affinity, but no explicit dark-mode tokens were found.
- Sub-brand palettes (e.g., for specific game lines like "Codenames" or "Galaxy Trucker") were not extracted. These likely exist as distinct accent colors within the system.
- The extracted hex list includes many colors that may be from third-party widgets (e.g., social icons, payment buttons). The primary palette was curated to the most distinctive and frequently used brand colors.
- Animation and transition durations were not extracted. A default of 200ms ease-in-out is assumed for state changes.
- Shadow tokens (box-shadow for cards, modals, etc.) were not extracted. A subtle, dark shadow (e.g., 0 2px 8px rgba(22, 20, 14, 0.1)) is assumed for elevation.
