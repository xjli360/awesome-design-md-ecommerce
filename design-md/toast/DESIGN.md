---
version: alpha
name: "Toast"
source_url: "https://www.toastmade.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A brand built on the warmth of natural wood grain, where the primary identity is anchored by a vivid orange #ff9900 — the same color as the meta theme-color and the most distinctive accent in a palette that otherwise leans toward cool blues (#85dcf8, #1dbbdf, #00ccff) and warm neutrals (#4d4d4d, #717171, #808080). This orange appears on primary CTAs, navigation highlights, and product badges, creating a consistent voltage that reads as handcrafted and approachable rather than industrial. The typography runs Exo and Exo 2 — geometric sans-serifs with subtle futuristic details in the terminals and apertures — giving the brand a precise, modern edge that contrasts beautifully with the organic material story of wood. Product cards use soft rounded corners (`{rounded.md}`) and generous whitespace (`{spacing.base}` to `{spacing.lg}`) to let the wood textures breathe, while the canvas stays clean white (`#ffffff`) with hairline borders (`#dddddd`) that feel like fine joinery. The extracted palette reveals a secondary story of playful accents — a cyan (#00ddbe), a magenta (#e73394), a lime (#3ae733), and a deep indigo (#221155) — suggesting a brand unafraid of color blocking or limited-edition drops. But the orange remains the anchor: it's the heat of a wood-fired kiln, the glow of a hand-oiled finish, the single color that says "this is Toast" before you read a single word.

colors:
  primary: "#ff9900"
  primary-active: "#ff6600"
  primary-disabled: "#f2a461"
  ink: "#4d4d4d"
  body: "#717171"
  muted: "#808080"
  muted-soft: "#a0a0a0"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#00ddbe"
  accent-magenta: "#e73394"
  accent-lime: "#3ae733"
  accent-indigo: "#221155"
  accent-deep-blue: "#091c4b"
  accent-sky: "#85dcf8"
  accent-ocean: "#1dbbdf"
  accent-coral: "#f37f35"
  accent-warm-brown: "#934400"
  accent-purple: "#ca37c9"
  accent-yellow: "#d6c81b"

typography:
  display-xl:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Exo 2', 'Exo', -apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary-active}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
    objectFit: "cover"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "2px solid {colors.primary}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
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
    padding: "16px 32px"
    height: 56px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's signature orange `{colors.primary}` (#ff9900). On hover, it deepens to `{colors.primary-active}` (#ff6600), and in its disabled state it fades to a softer peach `{colors.primary-disabled}` (#f2a461). The text is white `{colors.on-primary}` set in Exo 2 at 16px/600 weight with 0.5px letter spacing for a precise, confident read. Corners are softly squared at `{rounded.sm}` (8px), and the button maintains a consistent 48px height with 14px/28px padding for comfortable tap targets.

**`button-secondary`** — An outlined alternative that sits on white canvas with a 2px hairline border `{colors.hairline}` (#dddddd). On active state, the border switches to `{colors.ink}` (#4d4d4d) and the background shifts to `{colors.surface-soft}` (#f7f7f7). This button is used for "Learn More" or "Customize" actions where the primary orange would compete with other orange elements on the page.

**`button-tertiary`** — A text-only button with no background or border, used for secondary actions like "Cancel" or "View Details." The text color matches `{colors.ink}` and inherits the same typography as primary buttons for visual consistency.

**`button-pill-primary`** — A smaller, fully rounded variant (`{rounded.full}`) used for filter tags, category pills, and compact CTAs. At 40px height with 10px/24px padding, it's more compact than the standard button while retaining the orange fill and white text.

### Cards
**`product-card`** — The core product display unit, a white card (`{colors.surface-card}`) with 12px rounded corners (`{rounded.md}`) and 16px padding (`{spacing.base}`). On hover, a subtle box shadow (0 4px 12px rgba(0,0,0,0.08)) lifts the card without breaking the clean grid. Product images use `object-fit: cover` at a 1:1 aspect ratio with 8px corner rounding (`{rounded.sm}`) to echo the card's own rounded language. Each card includes a product name in `{typography.title-md}`, a price in `{typography.body-md}`, and optional color swatches using `{rounded.full}` 32px circles.

**`product-badge`** — Small uppercase labels (11px/700 weight) that sit over product images or on card corners. The standard badge uses `{colors.primary}` orange, sale badges use the deeper `{colors.primary-active}` (#ff6600), and "New" badges use the brand's cyan accent `{colors.accent-cyan}` (#00ddbe). All badges have 4px corner rounding (`{rounded.xs}`) and 4px/8px padding.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, white background with a soft hairline bottom border (`{colors.hairline-soft}` #ebebeb). Navigation links use `{typography.nav-link}` (15px/500 weight with 0.3px letter spacing) and the active state underlines with a 2px orange border and orange text color. The nav bar contains the brand logo (left), product category links (center), and utility icons for search, cart, and account (right).

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) at 48px height with a light gray background (`{colors.surface-soft}`) and hairline border. On focus, the background returns to white and the border switches to a 2px orange stroke (`{colors.primary}`). The placeholder text uses `{colors.muted}` (#808080) in `{typography.body-md}`.

### Forms
**`text-input`** — Standard form inputs at 48px height with 12px/16px padding and 8px corner rounding (`{rounded.sm}`). The default state has a 1px hairline border (`{colors.hairline}`), focus state upgrades to a 2px orange border, and error state switches to a 2px deep orange border (`{colors.primary-active}`). Input text uses `{typography.body-md}` in `{colors.ink}`.

### Footer
**`footer-link`** — Text links in the footer set in `{typography.link}` (14px/500 weight) with `{colors.muted}` (#808080) as the default color. On hover, they shift to `{colors.primary}` orange, creating a warm interactive moment in an otherwise neutral zone. The footer typically spans the full width with a `{colors.hairline-soft}` top border and `{spacing.section}` (64px) padding top and bottom.

### Hero
**`hero-section`** — Full-width hero banners with a soft gray background (`{colors.surface-soft}`) and generous padding (`{spacing.section}` top/bottom, `{spacing.lg}` sides). The headline uses `{typography.display-xl}` (32px/700 weight) and the CTA button is a larger 56px variant of `button-primary` with 16px/32px padding. The hero often features a single product image or lifestyle shot on one side, with the headline and CTA on the other.

### Color Swatches
**`color-swatch`** — 32px circular swatches (`{rounded.full}`) used on product detail pages to show available wood finishes and case colors. The selected state adds a 2px `{colors.ink}` border around the swatch. These swatches are critical to the Toast shopping experience, as the wood grain and color are the primary product differentiators.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero stacks vertically (text above image); search bar moves to persistent bottom bar; product cards stack full-width |
| Tablet | 744–1128px | Two-column product grid; nav shows limited links (logo + 2 categories + hamburger); hero maintains side-by-side layout with smaller text; footer collapses to 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav bar visible; hero at full width with 50/50 split; footer in 4-column layout; search bar in nav |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with max-width 1200px; all elements scale proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Product cards have 48px minimum tap area for "Add to Cart" and "Customize" actions
- Color swatches at 32px are below the 44px minimum; on mobile, swatch containers expand to 44px with 6px invisible padding
- Nav bar links have 48px touch targets (72px nav height provides ample room)
- Search bar at 48px height meets touch target requirements

### Collapsing Strategy
- On mobile (< 744px), the full nav bar collapses to a hamburger menu with a slide-out drawer
- Product category links in the nav collapse to a horizontal scrollable strip below the nav on tablet
- The hero section's side-by-side layout collapses to vertical stacking on mobile
- Footer links collapse from 4-column grid to 2-column on tablet, single-column on mobile
- Product image galleries collapse from thumbnail grid to single-image carousel with dot indicators on mobile
- Color swatch selectors collapse from inline display to a horizontal scrollable row on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font list includes `Exo` and `Exo 2` but exact font weights and sizes used in production could not be determined from the extracted data alone; the typography scale above is an informed estimate based on common usage patterns for geometric sans-serif brands
- Hover states for buttons and cards are inferred from common patterns; actual production hover animations (ease, duration, shadow depth) were not extractable
- The extracted color palette includes 30+ colors, many of which are likely checkout-widget colors (Afterpay, Klarna, Shopify Pay), social media brand colors, or dominant tones from product photography; the true brand palette is likely smaller than listed
- The brand's wood grain textures and material finishes could not be extracted as CSS values; these are critical to the brand identity but require manual design reference
- Dark mode styling is not present in the extracted data; if Toast supports dark mode, the palette would need to be developed separately
- Error states for forms (validation messages, error icons) were not extractable
- The brand's icon system (cart icon, search icon, account icon, social icons) could not be extracted; icon style and stroke weight are unknown
- Loading states, skeleton screens, and animation timing were not extractable
- The checkout flow and cart drawer styling were not extractable from the provided data
- Accessibility contrast ratios between the orange primary (#ff9900) and white text need manual verification; the brand may use a darker orange for on-primary text in production
