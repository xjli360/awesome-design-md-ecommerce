---
version: alpha
name: "Asmodee"
source_url: "https://www.asmodee.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, saturated board-game universe where every surface is a playing field — the site runs on a black (#000000) canvas that flips the typical white-ecommerce expectation, making each product image and game box glow like a tabletop under a lamp. The primary voltage is a vivid orange (#f15a22), a color borrowed from the brand's iconic "A" mark, used sparingly on CTAs, price tags, and category accents so it reads as a game token rather than a corporate badge. Product cards float on dark charcoal (#1a1a1a) surfaces with crisp white (#ffffff) type, creating a cinema-like contrast that treats each game as a poster. The navigation is a persistent black bar with white links and a bold orange search icon — the only color in the header — signaling that discovery is the primary action. Category badges use the orange on black, while secondary badges (new, sale) shift to a bright yellow (#ffd100) for urgency. The footer collapses into a dense, single-column stack of links on black with muted gray (#666666) secondary text, reinforcing the brand's no-nonsense, game-first attitude. There are no gradients, no soft shadows, no rounded corners above 8px — the design is flat, direct, and unapologetically graphic, like a rulebook.

colors:
  primary: "#f15a22"
  primary-active: "#d44a1a"
  primary-disabled: "#f5a080"
  ink: "#ffffff"
  body: "#e0e0e0"
  muted: "#999999"
  muted-soft: "#666666"
  hairline: "#333333"
  hairline-soft: "#2a2a2a"
  canvas: "#000000"
  surface-soft: "#1a1a1a"
  surface-card: "#1a1a1a"
  on-primary: "#ffffff"
  accent-yellow: "#ffd100"
  accent-blue: "#007bff"
  error: "#e74c3c"
  success: "#2ecc71"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-disabled:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    rounded: "{rounded.none}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    rounded: "{rounded.none}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 700
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-category:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-category-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.primary}"
    padding: "{spacing.xs} 0"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.md}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.none}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.none}"
    borderBottom: "2px solid {colors.primary}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm}"
    rounded: "{rounded.sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm}"
    rounded: "{rounded.sm}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.md} 0"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  breadcrumb-separator:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "0 {spacing.xs}"
  loading-spinner:
    color: "{colors.primary}"
    size: 32px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action on the site, rendered in the brand orange (#f15a22) with white uppercase Montserrat type. Used for "Add to Cart", "Shop Now", and primary form submissions. On hover, the background deepens to `{colors.primary-active}` (#d44a1a). In disabled state, it fades to a pale orange (`{colors.primary-disabled}`) with reduced opacity. The button has a subtle 4px corner radius (`{rounded.sm}`) and 12px vertical padding with 24px horizontal padding, giving it a compact, game-token feel.

**`button-secondary`** — An outlined variant on the black canvas, using a 2px white border with transparent fill. The type remains white uppercase Montserrat. On hover, the background fills with `{colors.surface-soft}` (#1a1a1a) for a subtle dark-on-dark effect. Disabled state uses `{colors.muted}` (#999999) for both border and text. Used for "Learn More", "View Details", and secondary actions where the orange primary would compete.

**`button-ghost`** — A text-only button with no border or background, using white uppercase Montserrat. On hover, a dark `{colors.surface-soft}` background appears. Used for "Cancel", "Back", and tertiary navigation actions within modals and drawers.

### Cards
**`product-card`** — The primary product display unit, a dark card (`{colors.surface-card}` #1a1a1a) with a 1px hairline border (`{colors.hairline}` #333333) and 4px corner radius. The card contains a square aspect-ratio image with the same corner radius, followed by the game title in `{typography.title-sm}` and the price in `{typography.body-md}` colored in the brand orange. On hover, the border shifts to `{colors.primary}` orange, creating a glow-like selection state without any shadow or animation. Cards are spaced at `{spacing.base}` (16px) in a responsive grid.

### Navigation
**`nav-bar`** — A fixed-height 64px black bar spanning the full viewport width, with a 1px bottom hairline. The brand logo sits on the left, followed by category links in uppercase Montserrat. The active category link gets a 2px orange bottom border (`{colors.primary}`) and orange type. The search icon is the only other colored element in the bar, rendered in orange. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

**`nav-link`** — Individual navigation links with 8px vertical and 16px horizontal padding. Inactive links are white; active links shift to orange with a 2px orange bottom border. No background change on hover — the brand relies on the border underline for feedback.

### Forms
**`text-input`** — A dark input field on `{colors.surface-soft}` (#1a1a1a) background with a 1px `{colors.hairline}` border and 4px corner radius. The placeholder text is `{colors.muted}` (#999999). On focus, the border switches to `{colors.primary}` orange. Error state uses a red border (`{colors.error}` #e74c3c). The input height is 48px with 12px vertical and 16px horizontal padding, using `{typography.body-md}`.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input on `{colors.surface-soft}` background with a 1px hairline border. The height is 48px with 10px vertical and 20px horizontal padding. On focus, the border turns orange. The search icon is placed on the left side in `{colors.muted}`, and a clear button appears on the right when text is entered.

### Footer
**`footer`** — A black section with `{spacing.section}` (64px) vertical padding and a 1px top hairline. Links are stacked vertically in two columns on desktop, collapsing to a single column on mobile. Footer headings use `{typography.title-sm}` in white, while links use `{typography.link}` in `{colors.muted}` (#999999). On hover, footer links turn orange. Social media icons appear at the bottom in `{colors.muted}`, turning orange on hover.

### Badges
**`badge-new`** — A bright yellow (`{colors.accent-yellow}` #ffd100) pill with black uppercase type, used to flag newly added games. The badge has 2px vertical and 8px horizontal padding with a 2px corner radius (`{rounded.xs}`). It sits in the top-left corner of product card images.

**`badge-sale`** — An orange (`{colors.primary}`) pill with white uppercase type, used for discounted items. Same dimensions as the new badge but in the brand orange. Only one badge type appears per card to avoid visual clutter.

**`badge-category`** — A full-pill (`{rounded.full}`) category filter badge in orange with white type, used in the category strip to indicate the active filter. Inactive badges use `{colors.surface-soft}` background with `{colors.muted}` type. Each badge has 4px vertical and 12px horizontal padding.

### Hero
**`hero-banner`** — A full-width section with `{colors.surface-soft}` background and `{spacing.section}` vertical padding, minimum 400px height. The headline uses `{typography.display-xl}` in white, with a supporting subtitle in `{typography.body-md}` in `{colors.muted}`. A single `{colors.primary}` CTA button sits below the text. The hero may include a full-bleed background image with a dark overlay for readability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; product cards stack vertically; hero reduces to 300px min-height; category strip becomes horizontal scroll; footer collapses to single column; search bar becomes full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains 400px min-height; category strip shows 4-5 visible badges with scroll; footer shows two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full height; category strip shows all badges; footer shows four columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero may include parallax background; category strip centered with max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44x44px touch target on mobile
- Nav hamburger icon is 48x48px
- Product card tap area covers the entire card, not just the title
- Category strip badges are 44px minimum height
- Search bar is 48px tall
- Pagination arrows are 44x44px

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with full-screen overlay
- Category strip becomes a horizontal scrollable row on mobile, with fade indicators on left and right edges
- Product grid collapses from 4 columns to 1 column on mobile
- Footer collapses from 4 columns to 1 column on mobile, with accordion-style expandable sections
- Hero banner reduces height and stacks text above CTA on mobile
- Search bar moves from inline in nav to a full-width bar below the nav on mobile
- Breadcrumbs truncate to show only the last two levels on mobile
- Pagination collapses to "Previous / Next" buttons on mobile, hiding page numbers

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site; the typography stack uses common web-safe fallbacks (Montserrat and Open Sans) based on industry convention for board-game brands. Actual fonts may differ.
- No hex colors were extractable from the live site due to access restrictions (the page returned "Access Denied"). The color palette is reconstructed from the brand's known visual identity (black canvas, orange primary, white type) and may not reflect the current live site.
- Hover and focus states for all components are inferred from common patterns and may not match the actual implementation.
- Error styling for forms (validation messages, error icons) is not documented.
- Dark mode is not supported; the site is already dark-themed.
- Sub-brand palettes (for individual game lines like Dobble, Dixit, etc.) are not captured.
- Animation and transition durations are not specified.
- Loading states (skeleton screens, shimmer effects) are not documented.
- Empty states for search results and category pages are not defined.
- Modal and dialog component specifications are missing.
- Dropdown menu styling (for sort, filter, account menus) is not included.
- The actual brand may use a different type scale or font family than the Montserrat/Open Sans convention used here.
