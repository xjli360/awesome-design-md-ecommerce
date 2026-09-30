---
version: alpha
name: "Super7"
source_url: "https://super7.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A sage-green (#aaccaa) backdrop sets Super7 apart from the typical black-and-neon action-figure store — this is a collector's destination that reads more like a gallery than a toy aisle. The brand's visual system runs on a restrained palette of near-whites (#f0f0f0, #dedede) and deep charcoals (#1a1a1a, #121212), with the sage acting as the single atmospheric note that signals "this is Super7." Product photography and large-format character art carry the energy; typography stays out of the way, with Inter at modest weights and sizes that let the figures command attention. The checkout and navigation feel intentionally quiet — a soft gray (#e1e3e4) for dividers and secondary surfaces, pill-shaped buttons (`{rounded.full}`) for add-to-cart actions, and a persistent top bar that keeps the brand mark and cart visible without competing with the product grid. The overall mood is that of a well-curated vinyl-toy shop: clean, slightly muted, with the color coming from the merchandise itself.

colors:
  primary: "#aaccaa"
  primary-active: "#8fb88f"
  primary-disabled: "#d4e6d4"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#6a6a6a"
  muted-soft: "#9a9a9a"
  hairline: "#e1e3e4"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#121212"
  on-dark: "#ffffff"
  accent-charcoal: "#1a1a1a"
  accent-light-gray: "#dedede"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0

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
    padding: 12px 28px
    height: 44px
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
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  badge-sold-out:
    backgroundColor: "{colors.accent-charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 40px
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.accent-charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-dark}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button with a sage-green (`{colors.primary}`) background and dark text (`{colors.on-primary}`). On hover/active, it shifts to a deeper sage (`{colors.primary-active}`). The disabled state uses a lighter sage (`{colors.primary-disabled}`) with muted text. Used for "Add to Cart," "Checkout," and primary form submissions.

**`button-secondary`** — A white pill button with a thin hairline border (`{colors.hairline}`) and dark text. On active, the border becomes solid ink and the background shifts to `{colors.surface-soft}`. Used for "View Details," "Pre-Order," and secondary actions alongside the primary button.

**`button-ghost`** — A text-only pill button with no background or border. Used for "Cancel," "Back," and tertiary actions in modals or dropdowns. Hover state adds a subtle `{colors.surface-soft}` background.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height with a white background and a single hairline bottom border. Contains the brand logo on the left, navigation links in the center, and cart/search icons on the right. The nav links use `{typography.nav-link}` at 14px with 500 weight.

**`nav-link-active`** — Active navigation link with a 2px solid underline in `{colors.ink}`. The text remains `{colors.ink}` for the active page.

**`nav-link-inactive`** — Inactive navigation link in `{colors.muted}`. On hover, the text shifts to `{colors.ink}`.

### Cards
**`product-card`** — A white card with subtle rounded corners (`{rounded.sm}`) and 16px padding. Contains a square product image with matching corner rounding, a title below in `{typography.title-sm}`, and a price in `{typography.body-md}`. Cards sit in a responsive grid with `{spacing.base}` gaps.

**`product-card-image`** — The product photo area, forced to a 1:1 aspect ratio with `{rounded.sm}`. Images are centered and cover the container.

### Badges
**`badge-sold-out`** — A small charcoal badge with white text, used to overlay sold-out items on product cards. Uses uppercase `{typography.badge}` at 11px.

**`badge-new`** — A small sage-green badge with dark text, used to highlight newly added items. Same typography as the sold-out badge but with brand color.

### Forms
**`text-input`** — A standard text input with a white background, 1px hairline border, and `{rounded.sm}` corners. On focus, the border switches to `{colors.ink}`. Used for search, email signup, and checkout forms.

**`search-bar`** — A pill-shaped search field with a soft gray background (`{colors.surface-soft}`) and muted placeholder text. On focus, the background becomes white and a solid ink border appears. Used in the mobile nav and header.

### Footer
**`footer`** — A dark charcoal (`{colors.accent-charcoal}`) footer with white text. Contains link columns, social icons, and legal text. Links use `{typography.link}` in white with hover underlines.

### Hero
**`hero-section`** — A full-width hero area with a soft gray background (`{colors.surface-soft}`) and generous padding. Contains a large headline in `{typography.display-xl}` and a supporting subtitle in `{typography.body-md}`. Used on category pages and promotional sections.

### Icons
**`icon-button`** — A circular icon button at 40x40px with no background. Used for social media icons, cart, and user account. Hover adds a `{colors.surface-soft}` background.

**`cart-badge`** — A small circular badge (20px minimum) with sage background, used to display cart item count. Positioned at the top-right of the cart icon.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product grid goes single-column; hero padding reduces to `{spacing.lg}`; search bar moves to a full-width expandable row |
| Tablet | 744–1128px | Nav links remain visible but condensed; product grid shows 2-3 columns; footer stacks into two rows |
| Desktop | 1128–1440px | Full nav with all links; product grid shows 4 columns; hero uses full `{spacing.section}` padding |
| Wide | > 1440px | Max-width container at 1440px; product grid can show 5 columns; hero content centers with larger type |

### Touch Targets
- All interactive elements (buttons, links, icons) have a minimum tap target of 44x44px
- Cart icon and search icon in the nav are wrapped in `{icon-button}` at 40px, with additional padding to meet the 44px target
- Product card links are the full card area, not just the title text
- Mobile nav hamburger menu button is 44x44px minimum

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Product grid reduces from 4 columns to 2 columns on tablet, to 1 column on mobile
- Footer link columns collapse from 4 columns to 2 columns on tablet, to a single vertical stack on mobile
- Hero section reduces padding and stacks title/subtitle vertically on mobile
- Search bar becomes a full-width expandable field on mobile, triggered by a search icon tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is dominated by grays (#3a3a3a, #e1e3e4, #dedede, #f0f0f0, #1a1a1a, #121212) with one distinctive sage (#aaccaa). This sage is used as the primary brand color, but its exact usage (buttons, badges, accents) is inferred from common DTC patterns rather than extracted from the live site.
- Font weights for Inter are estimated based on common web usage (400 for body, 500-600 for headings, 600 for buttons). The live site may use different weight values.
- Hover and active states for buttons and links are based on standard interaction patterns, not extracted from the site's CSS.
- Error states, form validation styling, and disabled input styling are not available from the extraction.
- Dark mode support is unknown; the extracted palette suggests a light-only system.
- The `#aaccaa` hex may be a seasonal or promotional color rather than the permanent brand primary. If the site undergoes a redesign, this color may change.
- Sub-brand or collection-specific color palettes (e.g., for Godzilla, Teenage Mutant Ninja Turtles, or other licensed lines) are not captured.
- The extracted font-family list only shows "Inter, sans-serif" — no fallback stack or variable font settings are available.
- Spacing values (padding, margins, gaps) are estimated from common e-commerce patterns and may differ from the actual site implementation.
- The product card aspect ratio (1:1) is assumed based on typical action-figure product photography; the actual site may use different ratios.
- The footer's dark background color (#1a1a1a) is inferred from the extracted charcoal hexes; the actual footer may use a different shade or include gradient overlays.
