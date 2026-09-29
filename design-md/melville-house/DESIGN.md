---
version: alpha
name: "Melville House"
source_url: "https://www.mhpbooks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A small press that wraps its books in a single, unapologetic #313131 — a near-black so dense it reads as literary authority rather than corporate gray. The extracted palette offers no accent color, no warm secondary, no brand voltage; the site trusts the weight of its own words and the quiet prestige of its covers. Typography defaults to the system stack — -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif — a deliberate non-choice that says the content, not the chrome, is the product. There are no pill buttons, no soft cards, no generous radii; the interface is rectilinear and unadorned, with `{rounded.none}` as the default posture and `{rounded.sm}` as the only concession for form elements. The nav bar sits at a compact 48px, the body copy runs at 16px with 1.5 line-height, and the entire experience feels like a well-printed page migrated to screen — no shadows, no gradients, no decorative flourishes. Melville House does not sell a lifestyle; it sells the book in your hand, and the site is designed to disappear.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d4d4d4"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#313131"
  link-hover: "#1a1a1a"
  error: "#c13515"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
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
    padding: 10px 24px
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 23px
    height: 40px
    border: 1px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: 1px solid "{colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 10px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    borderBottom: 1px solid "{colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: 1px solid "{colors.hairline}"
  product-card-hover:
    border: 1px solid "{colors.primary}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 1px solid "{colors.primary}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    borderTop: 1px solid "{colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
  footer-link-hover:
    color: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-header:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in `{colors.primary}` (#313131) with white text and `{rounded.sm}` corners. On hover, the background deepens to `{colors.primary-active}` (#1a1a1a). The disabled state uses `{colors.primary-disabled}` (#a0a0a0) with white text. Text is set in `{typography.button-md}` — 14px, weight 600, uppercase with 0.5px letter-spacing — giving it a crisp, editorial feel.

**`button-secondary`** — An outlined variant with a transparent background, `{colors.primary}` text, and a 1px solid border. On hover, the background fills with `{colors.surface-soft}` (#f5f5f5) and the border deepens to `{colors.primary-active}`. Same typography as primary for visual consistency.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` text. Used for secondary actions like "View all" or "Cancel" where visual weight should be minimal.

### Cards
**`product-card`** — A rectilinear card with no border-radius, a 1px `{colors.hairline}` border, and white background. On hover, the border switches to `{colors.primary}`. The card contains an image (no rounding), a title in `{typography.title-sm}`, and a price in `{typography.body-sm}` colored `{colors.muted}`. No shadow, no elevation — the card is a flat container for content.

**`badge-sale`** — A small, uppercase badge in `{colors.primary}` with white text, `{rounded.sm}` corners, and tight padding. Used to flag discounted titles.

**`badge-new`** — A light gray badge (`{colors.surface-soft}`) with `{colors.ink}` text, same shape and typography as the sale badge. Used for new releases.

### Navigation
**`nav-bar`** — A compact 48px header bar with white background, a 1px bottom border in `{colors.hairline}`, and navigation links set in `{typography.nav-link}` (14px, weight 500, uppercase). Active links get a 2px bottom border in `{colors.primary}`; inactive links render in `{colors.muted}`.

**`nav-link-active`** — The active state for top-level navigation items, distinguished by a bottom border rather than background color change. Text remains `{colors.ink}`.

**`nav-link-inactive`** — Inactive navigation items use `{colors.muted}` text with no border. On hover, they may transition to `{colors.ink}`.

### Forms
**`text-input`** — A standard input field with white background, `{colors.body}` text, `{rounded.sm}` corners, and a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.primary}`. Error state uses a `{colors.error}` border. Height is 40px with 10px/12px padding.

**`search-bar`** — A search-specific input with the same styling as `text-input` but with a search icon positioned at the left. Focus state mirrors the text input pattern.

### Footer
**`footer-section`** — A full-width footer in `{colors.surface-soft}` (#f5f5f5) with `{colors.body}` text, a 1px top border in `{colors.hairline}`, and generous padding (`{spacing.section}` vertical, `{spacing.lg}` horizontal). Links are set in `{typography.link}` (14px, weight 400, underlined) and hover to `{colors.primary}`.

**`footer-link`** — Standard footer link with underline decoration. On hover, color shifts from `{colors.body}` to `{colors.primary}`.

### Dividers
**`divider`** — A full-width 1px line in `{colors.hairline}` (#d4d4d4). Used to separate major sections.

**`divider-soft`** — A lighter 1px line in `{colors.hairline-soft}` (#e5e5e5). Used within cards or between related content blocks.

### Section Headers
**`section-header`** — A display-level heading in `{typography.display-md}` (24px, weight 600) with `{colors.ink}` text and `{spacing.lg}` bottom margin. Used to introduce content sections like "New Releases" or "Featured Titles."

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero padding reduces to 32px; body text remains 16px; section padding reduces to 32px |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero uses 48px padding; side margins at 24px |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero uses 64px padding; max-width container at 1128px centered |
| Wide | > 1440px | Max-width container at 1128px centered; additional whitespace on sides; no layout changes beyond container constraint |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Nav links in mobile menu have 48px tap targets
- Product card images are tappable across full card width
- Search bar has 44px minimum height

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Product grid reduces from 3 columns to 2 at tablet, to 1 at mobile
- Hero section reduces vertical padding by 50% on mobile
- Footer link columns stack vertically below 744px
- Sidebar or secondary navigation (if present) collapses to accordion or disappears on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extractable from the live site; the palette above is constructed from that single value plus reasonable neutrals for a text-heavy publisher. True secondary colors, accent colors, and brand-specific tones could not be verified.
- No font-family declarations beyond system defaults were found; the site likely uses a system font stack intentionally, but a custom typeface (e.g., for book titles or branding) may exist in non-extracted CSS.
- Hover and focus states for most components are inferred from common patterns rather than extracted from the live site.
- Error, success, and warning color tokens are estimated; no form validation styling was observed.
- Dark mode support status is unknown; no dark-mode media queries or color-scheme meta tags were detected.
- The site may use a custom Shopify or e-commerce theme; checkout-specific colors (Shopify Pay, Klarna, etc.) were filtered out but may appear in production.
- Button disabled states, loading spinners, and skeleton screens were not observed.
- Sub-brand or series-specific color palettes (e.g., for "Art of the Novella" series) could not be extracted.
- The site appeared behind a Cloudflare challenge page during extraction; some design tokens may be missing if the page did not fully render.
