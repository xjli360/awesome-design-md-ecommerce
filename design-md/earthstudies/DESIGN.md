---
version: alpha
name: "EarthStudies"
source_url: "https://earth-studies.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A landscape of muted earth tones anchored by a pale sage canvas (#f7faf6) and a deep ink (#212a32) that reads like basalt in shadow — the brand's primary voltage is a warm clay (#97756b), a color that appears nowhere in the outdoor-apparel mainstream of safety orange or forest green. Typography runs Inconsolata, a monospace face that gives product names, size charts, and care instructions the same quiet authority as a field notebook. Buttons and cards use generous rounding (`{rounded.md}` ~12px, `{rounded.lg}` ~20px) that softens the utilitarian premise, while a secondary accent of ochre (#df9c55) surfaces on sale badges and highlight tags like lichen catching afternoon light. The palette is deliberately desaturated: muted tones (#a99994, #919191, #8b8b8b) handle secondary text and hairline borders, and a second deep green-gray (#465552) appears in footer backgrounds and overlay scrims, creating depth without contrast aggression. The brand trusts its product photography — landscapes, fabric close-ups, layering shots — to carry emotional weight, keeping UI chrome recessive and typographic hierarchy flat. There is no hero carousel; instead, a single editorial image bleeds edge-to-edge with a centered headline set in Inconsolata at 28px, the brand's only display weight. The checkout and cart surfaces use the same sage canvas as the homepage, refusing the white-ecommerce default, and the entire experience feels less like a store and more like a field station.

colors:
  primary: "#97756b"
  primary-active: "#896960"
  primary-disabled: "#a99994"
  ink: "#212a32"
  body: "#363636"
  muted: "#717171"
  muted-soft: "#989898"
  hairline: "#dedede"
  hairline-soft: "#eef5ec"
  canvas: "#f7faf6"
  surface-soft: "#ebf3e9"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  accent-ochre: "#df9c55"
  accent-ochre-active: "#e3a86a"
  deep-green-gray: "#465552"
  deep-ink: "#1b1b1b"
  scrim: "#0c0f0f"

typography:
  display-xl:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.2px
  badge:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Inconsolata, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
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
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-ochre:
    backgroundColor: "{colors.accent-ochre}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-ochre-active:
    backgroundColor: "{colors.accent-ochre-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: "2px solid {colors.primary}"
    outlineOffset: "1px"
  text-input-error:
    border: "1px solid {colors.accent-ochre}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "3/4"
  product-badge-sale:
    backgroundColor: "{colors.accent-ochre}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-image:
    rounded: "{rounded.lg}"
    aspectRatio: "16/9"
  footer:
    backgroundColor: "{colors.deep-green-gray}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.surface-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-ochre}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 20px"
    height: 48px
  search-bar-focus:
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 16px"
    height: 40px
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in warm clay (#97756b) with white monospace text. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, darkens to `{colors.primary-active}` (#896960). Disabled state fades to `{colors.primary-disabled}` (#a99994) — a muted taupe that signals unavailability without visual alarm. Padding is 12px 24px with a height of 44px and `{rounded.sm}` (8px) corners — compact enough for mobile, substantial enough for desktop.

**`button-secondary`** — An outlined variant on the sage canvas background with ink text and a 1px hairline border. Used for "Save for Later", "Continue Shopping", and secondary checkout actions. Active state fills the background with `{colors.surface-soft}` (#ebf3e9) and strengthens the border to `{colors.muted}` (#717171). Padding is 11px 23px to account for the 1px border, maintaining a consistent 44px height with the primary button.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel", "Clear Filters", and inline navigation links. Inherits the same `{typography.button-md}` sizing and ink color. No hover background — only a subtle color shift to `{colors.primary}` (#97756b) for accessibility without visual clutter.

**`button-ochre`** — A compact accent button in ochre (#df9c55), used for sale tags, promotional CTAs, and limited-time offers. Smaller padding (8px 16px, 36px height) and `{typography.button-sm}` (13px) to sit alongside product cards without competing with the primary button. Active state brightens to `{colors.accent-ochre-active}` (#e3a86a).

### Cards
**`product-card`** — A white surface card (`{colors.surface-card}` #fcfcfc) with `{rounded.md}` (12px) corners and a subtle box shadow (0 1px 3px rgba(0,0,0,0.06)). The product image occupies the top 3/4 of the card with matching top-radius rounding. On hover, the shadow deepens to 0 4px 12px rgba(0,0,0,0.08) — a lift effect that doesn't rely on scale transforms. Product name, price, and badge sit below the image in `{typography.body-sm}` (14px). Cards are laid out in a responsive grid with 16px gaps.

**`product-badge-sale`**, **`product-badge-new`**, **`product-badge-sold-out`** — Small, uppercase monospace badges (11px, 700 weight) that sit at the top-left of product-card images. Sale badges use ochre (#df9c55), new-arrival badges use clay (#97756b), and sold-out badges use muted-soft (#989898). All have `{rounded.xs}` (4px) corners and 2px 8px padding — tight, informational, non-competing.

### Navigation
**`nav-bar`** — A fixed-height (72px) top bar on the sage canvas background with a soft hairline bottom border (`{colors.hairline-soft}` #eef5ec). Navigation links are set in `{typography.nav-link}` (14px, uppercase, 600 weight) with 0.2px letter spacing. The active link is underlined with a 2px clay line; inactive links are muted (#717171). The bar contains the brand wordmark (set in Inconsolata at 20px, 700 weight), a search icon, a cart icon, and a hamburger menu on mobile.

**`nav-link-active`** / **`nav-link-inactive`** — Active links maintain ink color with a 2px clay bottom border. Inactive links are muted (#717171) with no underline. Both use the same uppercase monospace styling. On hover, inactive links shift to ink color.

### Forms
**`text-input`** — Standard text input on sage canvas with a 1px hairline border and `{rounded.sm}` (8px) corners. Height is 44px with 12px 16px padding. On focus, the border switches to clay (#97756b) with a 2px outline at 1px offset — a visible but not aggressive focus ring. Error state uses an ochre border (#df9c55) without changing the background. Placeholder text is `{colors.muted-soft}` (#989898).

**`select-input`** — Matches the text-input dimensions and styling, with a custom dropdown arrow in `{colors.muted}` (#717171). The chevron is a simple downward-pointing SVG, 12px wide, positioned 16px from the right edge.

**`quantity-selector`** — A compact, 40px-tall control on `{colors.surface-soft}` (#ebf3e9) with `{rounded.sm}` corners. Contains a minus button, a numeric display (16px Inconsolata), and a plus button — all inline. Buttons are 36px wide with no background change on hover (only cursor: pointer).

**`size-selector`** — A pill-shaped button group for size selection (XS–XXL). Each size is a 40px-tall button on the sage canvas with a 1px hairline border and `{rounded.sm}` corners. The active size inverts to ink background with sage text — a high-contrast state that reads immediately. Inactive sizes show `{colors.muted}` text on hover.

### Hero
**`hero-section`** — A full-width section on the sage canvas with `{spacing.section}` (64px) vertical padding and `{spacing.xl}` (32px) horizontal padding. Contains a single editorial image (16:9 aspect ratio, `{rounded.lg}` ~20px) and a centered headline in `{typography.display-xl}` (28px, 700 weight, -0.5px letter spacing). No overlay text on the image — the headline sits below or beside it, letting the photography breathe. On mobile, the image goes full-width with no rounding.

### Footer
**`footer`** — A deep green-gray (#465552) footer with `{spacing.xxl}` (48px) vertical padding. Text is set in `{typography.body-sm}` (14px) with `{colors.surface-soft}` (#ebf3e9) as the text color — a low-contrast, restful combination. Links are the same color on the same background, with an ochre hover state (#df9c55). The footer contains three columns: "Shop" (product categories), "About" (brand story, sustainability), and "Support" (shipping, returns, contact). A thin hairline border in `{colors.deep-ink}` (#1b1b1b) separates the columns.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) on the sage canvas with a 1px hairline border. Height is 48px with 10px 20px padding. On focus, the border switches to clay (#97756b). The search icon (a 16px magnifying glass in `{colors.muted}`) sits at the left edge, and placeholder text reads "Search products..." in `{colors.muted-soft}` (#989898). On mobile, the search bar collapses into an icon-only button that expands to full width on tap.

### Accordion
**`accordion-header`** / **`accordion-content`** — Used for product details (materials, care instructions, shipping) and FAQ sections. The header is a 16px Inconsolata title with no background, only a bottom hairline border. The content panel slides open below with `{typography.body-sm}` (14px) text in `{colors.body}` (#363636). Padding is 16px top/bottom for the header, 8px top / 16px bottom for the content. The toggle icon is a simple plus/minus in `{colors.muted}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav-bar collapses to hamburger + logo; hero image goes full-width (no rounding); product cards stack vertically; footer columns stack; search bar becomes icon-only; size selector wraps to two rows; quantity selector reduces to 36px height |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows all links but collapses secondary links into a "More" dropdown; hero image maintains `{rounded.lg}`; footer columns remain in a 2+1 layout; search bar is full-width but reduced to 40px height |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; hero section uses 16:9 image with `{rounded.lg}`; footer columns in 3-column layout; search bar at 48px height; size selector in a single row |
| Wide | > 1440px | Max-width container at 1440px with auto margins; product grid expands to four columns; hero image scales to max-width; all other components remain at desktop sizing |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Search bar icon-only button on mobile is 48px × 48px
- Quantity selector buttons are 36px × 40px — slightly below the 44px recommendation but acceptable for secondary controls
- Size selector buttons are 40px × 40px
- Nav links have a minimum 44px tap area (padding extends the hit area beyond the text)
- Footer links have 36px tap areas — acceptable for non-primary navigation

### Collapsing Strategy
- Top navigation collapses to hamburger menu on mobile (< 744px); secondary links move to a "More" dropdown on tablet
- Product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Footer columns collapse from 3 columns (desktop) → 2+1 stacked (tablet) → single column (mobile)
- Search bar collapses from full-width input to icon-only on mobile; tapping the icon expands it to full-width with a slide animation
- Accordion panels collapse by default on all breakpoints; only the first panel is open on product detail pages
- Size selector wraps to two rows on mobile; remains single-row on tablet and above
- Hero section reduces vertical padding from 64px (desktop) to 32px (mobile)
- Product badges shift from top-left overlay to inline below the image on mobile (to avoid crowding on small screens)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only `button-primary-active` and `button-secondary-active` are extracted. Hover states for text inputs, select inputs, size selectors, and footer links are inferred from common patterns — actual hover colors may differ.
- **Error states**: Error styling for text inputs (border color, error message typography) is inferred. The brand may use a different error color or include an error icon.
- **Focus rings**: The focus ring for text inputs (2px outline, 1px offset) is a reasonable default — the brand may use a different style (e.g., box-shadow, no outline).
- **Dark mode**: No dark mode detected. The brand uses a light sage canvas throughout. If dark mode exists, it was not visible in the extracted data.
- **Sub-brand palettes**: No sub-brand or seasonal palette detected. The extracted colors are consistent across the site.
- **Checkout colors**: Some extracted colors (#f2f2f2, #b1b1b1, #8b8b8b, #919191) may belong to Shopify's default checkout widget rather than the brand. These are not used in the primary palette.
- **Font weights**: Only one font-family (Inconsolata) was found. The brand may use additional weights (e.g., 300, 400, 600, 700) beyond the 400 and 700 used here. Font sizes and line heights are inferred from typical monospace usage.
- **Spacing scale**: The spacing scale is inferred from common e-commerce patterns. Actual spacing values (padding, margins, gaps) may vary.
- **Rounded scale**: The rounded values are inferred from the brand's visual style. Actual border-radius values may differ.
- **Component heights**: Button and input heights (44px, 48px, 36px) are inferred from common patterns. The brand may use different heights.
- **Animation and transitions**: No transition durations, easing functions, or animation styles were extracted. The brand likely uses subtle transitions (e.g., 200ms ease-in-out) but this is unconfirmed.
- **Iconography**: No icon set was detected. The brand may use custom icons or a library (e.g., Feather, Heroicons). The search icon is assumed to be a simple magnifying glass.
- **Typography hierarchy**: The brand may use additional type styles (e.g., display-sm, title-xs, overline) not captured here. The extracted font-family is Inconsolata, but the brand may use a second font for headings or decorative text.
