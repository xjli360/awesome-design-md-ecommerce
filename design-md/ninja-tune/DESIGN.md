---
version: alpha
name: "Ninja Tune"
source_url: "https://www.ninjatune.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A black-and-white foundation (#222222 ink on #f5f5f5 surface) that lets the music do the coloring — the extracted palette is dominated by system grays and Bootstrap alert hues (#3c763d green, #8a6d3b gold, #a94442 red), suggesting the site leans heavily on a neutral canvas with occasional utility accents rather than a proprietary brand color. The typography stack is a hybrid of classic web sans-serifs (Helvetica Neue, Arial) and two proprietary faces — franklingothicbold and franklingothicregular — that carry the label's identity in headers and navigation, giving the interface a mid-century editorial weight that contrasts with the lightweight system fonts used for body copy. Buttons and interactive elements default to #337ab7 (a Bootstrap blue), indicating the site may not have fully customized its component library, but the overall impression is one of deliberate restraint: a dark header bar (#222222) with white text, generous whitespace in release grids, and small, tightly-kerned captions that defer to album artwork and track listings. The label's visual identity is carried more by its artists' imagery and the franklingothic typeface than by any single color — the design system is a quiet frame around loud music.

colors:
  primary: "#222222"
  primary-active: "#080808"
  primary-disabled: "#777777"
  ink: "#222222"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#9d9d9d"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  alert-success-bg: "#dff0d8"
  alert-success-text: "#3c763d"
  alert-info-bg: "#d9edf7"
  alert-info-text: "#31708f"
  alert-warning-bg: "#fcf8e3"
  alert-warning-text: "#8a6d3b"
  alert-error-bg: "#f2dede"
  alert-error-text: "#a94442"
  link-default: "#337ab7"
  link-hover: "#286090"

typography:
  display-xl:
    fontFamily: "'franklingothicbold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'franklingothicbold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'franklingothicbold', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'franklingothicregular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'franklingothicregular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
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
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'franklingothicregular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'franklingothicregular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
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
    fontFamily: "'franklingothicregular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'franklingothicregular', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
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
    padding: 10px 20px
    height: 40px
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
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link-default}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.link-default}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 0 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-meta:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.alert-error-text}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  alert-success:
    backgroundColor: "{colors.alert-success-bg}"
    textColor: "{colors.alert-success-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  alert-error:
    backgroundColor: "{colors.alert-error-bg}"
    textColor: "{colors.alert-error-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"

## Components

### Buttons
**`button-primary`** — Solid black rectangle (#222222) with white uppercase franklingothicregular text. The primary action button for adding items to cart, submitting forms, or confirming purchases. On hover, shifts to near-black (#080808). Disabled state uses muted gray (#777777) to signal inactivity. No border radius beyond 4px — the label favors sharp corners that match its editorial grid.

**`button-secondary`** — White button with a 1px hairline border (#e5e5e5) and black text. Used for secondary actions like "View Details" or "Cancel." Maintains the same 40px height and uppercase franklingothicregular typography as the primary button, ensuring visual consistency in paired button groups.

**`button-link`** — Text-only link styled in Bootstrap blue (#337ab7). Used for "Read More" or "Learn More" inline actions within release descriptions or artist bios. No background, no border — pure text with hover darkening to #286090.

### Cards
**`product-card`** — A minimal, borderless card for displaying album releases, merchandise, or artist entries. The card itself has no rounding and no background color (inherits white canvas), relying entirely on the album artwork and typography for hierarchy. The title sits below the image in franklingothicregular at 16px, with a caption-style meta line (artist name, format, price) in 12px Helvetica Neue at muted gray (#777777). No shadow, no border — the design trusts the content.

**`product-card-image`** — Square aspect ratio (1:1) by default, with no border radius. The artwork is the hero element; the card frame is intentionally invisible.

### Navigation
**`nav-bar`** — A fixed-height 60px bar in solid black (#222222) with white uppercase nav links in franklingothicregular. Links are spaced at 16px padding and use a 2px white bottom border for the active state. The bar spans full viewport width and carries the Ninja Tune logo (typically a wordmark or the "N" icon) on the left, with links to Releases, Artists, Shop, and Events on the right.

**`nav-link`** — Uppercase franklingothicregular at 14px with 0.5px letter spacing. Active state adds a 2px white bottom border. No background change on hover — the label keeps navigation clean and typographic.

### Forms
**`text-input`** — White input field with a 1px hairline border (#e5e5e5) and 4px border radius. Body text in Helvetica Neue at 14px. On focus, the border switches to the link blue (#337ab7) to indicate active state. Used for search, newsletter signup, and checkout forms.

**`search-bar`** — A dedicated search input with the same styling as text-input but with 16px horizontal padding and a magnifying glass icon (typically a Glyphicon Halflings icon, given the extracted font stack). The search bar appears in the nav bar on desktop and as a full-width element on mobile.

### Alerts
**`alert-success`** — Light green background (#dff0d8) with dark green text (#3c763d). Used for success messages after adding to cart or completing a purchase. 4px border radius, 12px vertical padding, 16px horizontal padding.

**`alert-error`** — Light red background (#f2dede) with dark red text (#a94442). Used for error states like failed payment or out-of-stock notifications. Same structural styling as alert-success.

### Footer
**`footer`** — Light gray background (#f5f5f5) with body text in Helvetica Neue at 14px (#555555). Footer links are in muted gray (#777777) and use the same link typography as the rest of the site. The footer typically contains columns for About, Help, Social Links, and Newsletter Signup, with generous padding (64px top/bottom, 24px sides).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for releases; nav bar collapses to hamburger menu; search bar becomes full-width below nav; product cards stack vertically with full-width images |
| Tablet | 744–1128px | Two-column release grid; nav bar shows top-level links (Releases, Artists, Shop) with "More" dropdown; search bar remains in nav but shrinks width |
| Desktop | 1128–1440px | Three-column release grid; full nav bar with all links visible; search bar in nav with 400px max-width; footer columns display in 4-column layout |
| Wide | > 1440px | Four-column release grid; max-width container (1440px) centered; nav bar and footer extend full width with content constrained |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px tap target height on mobile
- Nav bar hamburger icon is 48px × 48px
- Product card images are tappable with no minimum size constraint (artwork drives interaction)
- Search bar height remains 40px on all breakpoints (meets 44px guideline with padding)

### Collapsing Strategy
- Nav bar collapses to hamburger menu below 744px; all links move to a slide-out drawer
- Release grid collapses from 4 columns (wide) → 3 (desktop) → 2 (tablet) → 1 (mobile)
- Footer columns collapse from 4 → 2 at 744px, then stack vertically below 480px
- Search bar moves from inline nav position to full-width below nav on mobile
- Product card meta (artist, format, price) collapses to single line on mobile, hiding format label

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is heavily dominated by Bootstrap default colors (#337ab7, #5cb85c, #d9534f, etc.) and system grays — the brand's true primary color may be more distinctive (e.g., a specific red or yellow from the Ninja Tune logo) but was not reliably extracted from the live site's CSS/HTML. The current `primary: "#222222"` is an educated guess based on the dark header bar.
- Font sizes and line heights are inferred from common editorial patterns and the extracted font families — actual values may differ on the live site.
- No hover, focus, or active states were extracted for most components beyond the primary button.
- Dark mode support is unknown — the site appears to be light-mode only based on extracted colors.
- Sub-brand or artist-specific color palettes (e.g., for specific album campaigns) are not captured.
- The `franklingothicbold` and `franklingothicregular` font faces may be served as web fonts with specific weights and formats — the exact `@font-face` declarations were not extracted.
- Glyphicons Halflings is present in the font stack but its usage (icon set) is inferred — exact icon mappings are unknown.
- Checkout flow components (payment forms, address inputs, cart summary) may use Shopify defaults that were not fully extracted.
- The site may use a sticky nav bar on scroll — behavior was not confirmed from extracted data.
