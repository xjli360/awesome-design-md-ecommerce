---
version: alpha
name: "Shelflove Crate"
source_url: "https://www.shelflovebox.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A subscription box brand that wraps its bookish identity in a palette anchored on #f0523d — a warm, assertive coral-red that appears on primary buttons, badges, and accent elements against a canvas of #f6f6f6 and #ffffff. The brand's visual system leans heavily on grayscale layering: #3e3e3e for body text, #a1a1a1 for muted labels, and #e4e4e4 for hairline borders, creating a clean, editorial feel that lets the coral-red pop without competing. Typography runs Clarkson, a geometric sans-serif with a friendly, slightly condensed character, set at moderate weights — display sits at 24–32px in weight 500, trusting generous whitespace and the coral accent over heavy typographic muscle. Rounded corners are restrained: buttons use {rounded.sm} (8px), cards use {rounded.md} (12px), and only the search bar and avatar elements reach {rounded.full}. The nav bar is a fixed 64px strip with a subtle bottom hairline, housing a logo lockup and a coral-red CTA that reads "Get Your Box." Product cards stack a cover image, a title in {typography.title-md}, a one-line description, and a coral "Subscribe" button — the coral is the only color that moves the user forward. The footer is dense with links in {typography.body-sm} and a coral email-signup field, reinforcing the brand's direct-to-consumer subscription model. The overall feel is warm but not saccharine, structured but not rigid — a bookish marketplace that trusts its accent color to do the emotional work.

colors:
  primary: "#f0523d"
  primary-active: "#e4351e"
  primary-disabled: "#f6a89d"
  ink: "#3e3e3e"
  body: "#505050"
  muted: "#797979"
  muted-soft: "#a1a1a1"
  hairline: "#e4e4e4"
  hairline-soft: "#ebebeb"
  canvas: "#f6f6f6"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#a50000"
  link-blue: "#00549e"
  accent-blue: "#14aaff"
  star-rating: "#f0523d"

typography:
  display-xl:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
  micro-label:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Clarkson', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-md}"
  product-card-description:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.surface-card}"
  footer-email-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  avatar:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in coral-red `#f0523d` with white text. On hover, it shifts to `#e4351e` (primary-active). The disabled state uses `#f6a89d` (primary-disabled) with white text. All variants share `{rounded.sm}` (8px) and `{typography.button-md}` (16px, weight 600). Padding is 12px vertical, 24px horizontal, yielding a 44px height.

**`button-secondary`** — An outlined or ghost variant on the `{colors.canvas}` background with `{colors.ink}` text. Uses the same `{rounded.sm}` and `{typography.button-md}` as primary but with 11px vertical padding and 23px horizontal to account for the border. The hover state adds a 1px `{colors.hairline}` border.

**`button-tertiary-text`** — A text-only link styled as a button, with transparent background and `{colors.primary}` text. Used for "Learn More" or "Cancel" actions. Hover state adds a subtle underline.

**`button-pill-primary`** — A fully pill-shaped variant (`{rounded.full}`) for compact CTAs like "Subscribe Now" in cards. Uses `{typography.button-sm}` (14px, weight 600) with 10px vertical and 20px horizontal padding.

### Cards
**`product-card`** — The primary content container for subscription box listings. White background (`{colors.surface-card}`), `{rounded.md}` (12px), and `{typography.body-sm}` for body text. The card stacks a cover image (with `{rounded.md}`), a title in `{typography.title-md}`, a one-line description in `{colors.body}`, and a price in `{typography.title-sm}`. A `{colors.primary}` badge may appear for "New" or "Best Seller" tags.

**`product-card-badge`** — A small coral-red badge (`{colors.primary}`) with white text, `{rounded.xs}` (4px), and `{typography.badge}` (11px, weight 600, 0.5px letter-spacing). Padding is 2px vertical, 8px horizontal.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height, white background (`{colors.surface-card}`), with a subtle `{colors.hairline}` bottom border. Contains the logo lockup on the left, nav links in `{typography.nav-link}` (15px, weight 500), and a `{colors.primary}` CTA button on the right. Active links use `{colors.ink}`, inactive use `{colors.muted}`.

**`nav-link-active`** — Active navigation link with `{colors.ink}` text and transparent background. Hover state adds a 2px bottom border in `{colors.primary}`.

**`nav-link-inactive`** — Inactive navigation link with `{colors.muted}` text. Hover state transitions to `{colors.ink}`.

### Forms
**`text-input`** — Standard text input field with white background, `{colors.ink}` text, `{rounded.sm}` (8px), and 12px vertical / 16px horizontal padding. Height is 44px. The active state shows a 2px `{colors.primary}` border. Placeholder text uses `{colors.muted-soft}`.

**`search-bar`** — A pill-shaped search field (`{rounded.full}`) at 48px height, white background, with a `{colors.primary}` search icon on the left. Uses `{typography.body-md}` (16px) for input text. The active state adds a 2px `{colors.primary}` border.

### Footer
**`footer`** — A dark footer section with `{colors.ink}` background and white text. Padding is 48px vertical, 24px horizontal. Contains link columns, social icons, and an email signup form. Links use `{colors.muted-soft}` and transition to white on hover.

**`footer-email-input`** — An email input field within the footer, styled as a white rectangle (`{colors.surface-card}`) with `{rounded.sm}` (8px) and 44px height. The adjacent submit button uses `{colors.primary}` with `{colors.on-primary}` text.

### Badges & Tags
**`badge-new`** — A coral-red badge (`{colors.primary}`) with white text, `{rounded.xs}` (4px), and `{typography.badge}` (11px, weight 600). Used for "New Arrivals" or "Just Added" labels on product cards.

**`badge-sale`** — A dark red badge (`{colors.error}`) with white text, same styling as `badge-new`. Used for "Sale" or "Limited Edition" labels.

**`category-tag`** — A pill-shaped filter tag (`{rounded.full}`) with `{colors.surface-soft}` background and `{colors.ink}` text. Uses `{typography.caption}` (13px, weight 500) with 6px vertical and 16px horizontal padding. The active state switches to `{colors.primary}` background with white text.

### Hero
**`hero`** — The primary hero section on the homepage, with `{colors.canvas}` background and `{colors.ink}` text. Uses `{typography.display-xl}` (32px, weight 500) for the headline, with generous padding (64px vertical, 24px horizontal). A `{colors.primary}` CTA button (`hero-cta`) sits below the headline at 48px height with 14px vertical and 32px horizontal padding.

### Misc
**`avatar`** — A circular avatar (`{rounded.full}`) at 40px height, with `{colors.muted-soft}` background and white text. Used for user profile icons in the nav bar.

**`icon-button`** — A circular icon button (`{rounded.full}`) at 40px height, with transparent background and `{colors.muted}` icon color. The active state uses `{colors.surface-soft}` background and `{colors.ink}` icon color.

**`divider`** — A 1px horizontal rule in `{colors.hairline}` (`#e4e4e4`). Used between sections and card elements.

**`divider-soft`** — A 1px horizontal rule in `{colors.hairline-soft}` (`#ebebeb`). Used for subtle separation within cards or lists.

**`loading-spinner`** — A 24px circular spinner in `{colors.primary}`. Used for async loading states on buttons and content areas.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero padding reduces to 32px vertical; search bar moves to a full-width overlay; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav bar shows 4-5 links; hero uses 48px vertical padding; search bar remains in nav but shrinks to 40px height; footer links in two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero uses 64px vertical padding; search bar at 48px height; footer links in three columns |
| Wide | > 1440px | Max-width container at 1440px; three-column product grid with increased whitespace; hero uses 80px vertical padding; search bar at 48px height; footer links in four columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons and avatars are 40px minimum
- Category tags are 32px minimum height
- Nav bar links have 48px tap targets (padding + height)
- Product card CTAs are 44px height

### Collapsing Strategy
- Nav bar: On mobile (< 744px), the full nav collapses to a hamburger menu icon; the logo and CTA button remain visible
- Product grid: Shifts from 3 columns (desktop) to 2 columns (tablet) to 1 column (mobile)
- Footer: Link columns collapse from 4 (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Search bar: On mobile, the pill-shaped search bar becomes a full-width overlay with a back button
- Hero: Padding reduces progressively; on mobile, the hero CTA button becomes full-width
- Category tags: On mobile, the tag strip becomes horizontally scrollable with snap points

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (button-secondary, text-input, footer links) are inferred from common patterns, not extracted from the live site
- Error styling for form inputs (border color, error message typography) is not documented from the live site
- The extracted color list contains many generic blues (#14aaff, #00549e, #004079, #2fbbea, #33ccff, #3064e1, #4777ed, #008fe0) that are likely checkout-widget colors (Shopify Pay, Klarna, Afterpay) or social-icon defaults — these are not included in the brand palette
- The extracted font list only shows "Clarkson, Helvetica, inherit, sans-serif" — no fallback stack for system fonts is confirmed
- Dark mode or high-contrast mode styles are not documented
- Sub-brand or seasonal color palettes (e.g., holiday editions) are not captured
- Animation and transition timing values (e.g., hover fade duration, card lift on hover) are not extracted
- Focus ring styles for keyboard navigation are not documented
- The extracted data comes from an expired Squarespace site — the live brand may have changed significantly since the extraction
