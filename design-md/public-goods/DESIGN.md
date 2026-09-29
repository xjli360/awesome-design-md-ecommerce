---
version: alpha
name: "Public Goods"
source_url: "https://www.publicgoods.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Public Goods is a direct-to-consumer brand that strips away the noise of traditional consumer goods with a clean, utilitarian aesthetic. The brand's visual language is anchored on a near-black ink (#080808) and a warm off-white canvas (#f5f5f5), creating a high-contrast foundation that feels both premium and approachable. Signature design moves include generous use of negative space, thin hairlines (#d8d8d8) that define card boundaries without visual weight, and a restrained color palette where muted grays (#7d7d7d, #8c8c8c, #999999) carry secondary information while a single accent blue (#4469af) provides the only chromatic voltage across CTAs and links. The typography system blends a condensed display face (BebasNeue) for headlines with a clean, humanist sans-serif (Nunito Sans) for body copy, creating a distinctive rhythm where bold, all-caps headers sit above light-weight body text. Product photography is given maximum breathing room with `{spacing.section}`-scale padding, and every interactive element — from buttons to input fields — uses `{rounded.sm}` (8px) corners that feel intentional without being overly soft. The overall effect is one of quiet confidence: a brand that trusts its product quality over promotional noise, using `{colors.ink}` (#080808) typography on `{colors.canvas}` (#f5f5f5) backgrounds as its primary communication channel, with `{colors.primary}` (#4469af) reserved exclusively for moments of action.

colors:
  primary: "#4469af"
  primary-active: "#2c3e50"
  primary-disabled: "#9a9db1"
  ink: "#080808"
  body: "#333333"
  muted: "#7d7d7d"
  muted-soft: "#999999"
  hairline: "#d8d8d8"
  hairline-soft: "#e7e7e7"
  canvas: "#f5f5f5"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#c8232c"
  accent-blue-social: "#00aced"
  badge-new: "#676986"
  star-rating: "#272d45"
  footer-bg: "#1e1e1e"
  footer-text: "#c1c1c1"

typography:
  display-xl:
    fontFamily: "'BebasNeue', 'NB', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: 1px
  display-lg:
    fontFamily: "'BebasNeue', 'NB', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'BebasNeue', 'NB', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0.5px
  title-md:
    fontFamily: "'Nunito Sans', 'NeuzeitS-Book', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'NeuzeitS-Book', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'NeuzeitS-Book', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'NeuzeitS-Book', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'NeuzeitS-Book', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Nunito Sans', 'NeuzeitS-Book-Heavy', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Nunito Sans', 'NeuzeitS-Book-Heavy', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Nunito Sans', 'NeuzeitS-Book', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', 'NeuzeitS-Book', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Nunito Sans', 'NeuzeitS-Book-Heavy', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.20
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 36px
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
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.sm} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "8px"
    left: "8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: "400px"
  hero-banner-overlay:
    backgroundColor: "rgba(8, 8, 8, 0.3)"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.lg} 0"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  category-tile-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: "14px"
  social-icon:
    color: "{colors.muted}"
    fontSize: "20px"
  social-icon-hover:
    color: "{colors.accent-blue-social}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action button, rendered in `{colors.primary}` (#4469af) with white text and `{rounded.sm}` corners. Uses uppercase `{typography.button-md}` for a confident, editorial feel. On hover, transitions to `{colors.primary-active}` (#2c3e50) for a darker, more grounded state. The disabled state uses `{colors.primary-disabled}` (#9a9db1), maintaining the same dimensions and typography to preserve layout stability.

**`button-secondary`** — An outlined variant with `{colors.canvas}` background and a 2px `{colors.ink}` border. Shares the same `{typography.button-md}` and `{rounded.sm}` as the primary button, but the active state fills the background with `{colors.surface-soft}` (#ebebeb) while keeping the dark border. Used for secondary actions like "Learn More" or "Cancel" where visual hierarchy is needed without competing with the primary CTA.

**`button-tertiary-text`** — A text-only button with transparent background and `{colors.primary}` text. No border or rounded corners — relies entirely on typography and color for affordance. Used for inline actions like "View All" or "See Details" where a full button would be visually heavy.

**`button-pill`** — A compact, fully rounded variant (`{rounded.full}`) using `{colors.primary}` background and `{typography.button-sm}`. Shorter at 36px height with tighter padding, designed for tag-like actions, filter toggles, or subscription badges. The pill shape signals a lightweight, dismissible interaction.

### Cards
**`product-card`** — The primary product display component, built on a white `{colors.surface-card}` background with `{rounded.sm}` corners. The card contains a square aspect-ratio image with top-rounded corners (`{rounded.sm} {rounded.sm} 0 0`), followed by the product title in `{typography.title-sm}` and price in `{typography.body-sm}` with `{colors.body}` (#333333). A `{colors.badge-new}` (#676986) badge can be positioned absolutely at the top-left of the image area for new arrivals or limited editions.

**`category-tile`** — A navigational card for product categories, using `{colors.surface-card}` with a subtle `{colors.hairline-soft}` border and `{rounded.sm}`. The active state inverts to `{colors.primary}` background with white text, creating clear visual distinction for the selected category. Padding of `{spacing.lg}` (24px) provides comfortable touch targets.

### Navigation
**`nav-bar`** — The primary site navigation, 72px tall with white background and a thin `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` — uppercase, 14px, weight 600 — with the active link distinguished by a 2px bottom border in `{colors.ink}`. On scroll, the nav collapses to a 56px sticky variant, reducing visual footprint while maintaining accessibility.

**`nav-link-active` / `nav-link-inactive`** — Active links use `{colors.ink}` with an underline border; inactive links use `{colors.muted}` (#7d7d7d) with no border. Both share the same typography and transparent background, ensuring the active state communicates through color and line rather than shape or weight changes.

### Forms
**`text-input`** — Standard text input with `{colors.canvas}` background, `{colors.hairline}` border, and `{rounded.sm}` corners. At 48px height with 12px/16px padding, it provides comfortable typing space. The focus state thickens the border to 2px in `{colors.primary}`, while the error state uses 2px `{colors.accent-red}` (#c8232c) for clear validation feedback.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with `{colors.surface-soft}` (#ebebeb) background and subtle `{colors.hairline}` border. At 44px height with 10px/20px padding, it's more compact than the standard text input, designed for utility rather than data entry. The pill shape signals a search-specific interaction pattern.

### Footer
**`footer`** — A dark section using `{colors.footer-bg}` (#1e1e1e) background with `{colors.footer-text}` (#c1c1c1) for body copy. Links use the same muted gray with hover transitions to white (`{colors.on-primary}`). The footer carries `{spacing.section}` (64px) vertical padding, creating a substantial visual anchor at the bottom of every page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero banners reduce to 300px min-height; category tiles stack vertically; font sizes scale down 20% for display typography; search bar moves to persistent bottom bar |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero banners at 400px min-height; category tiles in 3-column grid; side-panel navigation for account pages |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero banners at 500px min-height; category tiles in 4-column grid; sticky sidebar for filter panels |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px with centered content; hero banners at 600px min-height with wider typography scale; additional whitespace in card layouts |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets extend to full card width for easy selection
- Category tiles use 24px minimum padding to ensure comfortable finger placement
- Mobile nav hamburger icon uses 48x48px tap area with 8px internal icon padding

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px, with full-height slide-out panel
- Product filters collapse to accordion panels on mobile, with "Apply Filters" button at bottom
- Footer link columns collapse to single-column accordion on mobile, preserving all links
- Hero banner text overlay collapses to single line on mobile, with CTA button below image
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted — only primary button hover was confirmed from the live site
- Error and validation styling for forms beyond the text-input error border is inferred from common patterns rather than extracted
- Dark mode palette is not present on the live site and would need to be designed from scratch
- Sub-brand or seasonal color palettes (holiday, limited edition) were not observed
- Animation timing and easing curves were not extractable from static HTML/CSS analysis
- Focus ring styles for keyboard navigation were not visible in the extracted styles
- Loading states (skeleton screens, spinners) were not present in the extracted data
- Dropdown and select menu styling was not captured in the extraction
- Modal and dialog overlay styling (backdrop, close button, animation) is absent
- Tooltip and popover design patterns were not observed on the live site
