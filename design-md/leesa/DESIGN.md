---
version: alpha
name: "Leesa"
source_url: "https://www.leesa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Leesa is a sleep-first brand that wraps itself in deep teal and warm rust, a palette that feels like dusk settling over a forest canopy. The primary brand voltage is `#0e3739` — a dark, almost-black teal that anchors headlines, buttons, and the top navigation with quiet authority. Against this, `#cc4d0f` and `#ff8347` pulse as accent oranges, used sparingly on sale badges, hover states, and secondary CTAs to create a warm counterpoint that reads as energetic but not aggressive. The canvas is a soft `#f7f5f4` rather than pure white, giving the entire experience a tactile, bedroom-warm quality, while `#e3e2e1` and `#c7c5c3` provide hairline and surface-soft boundaries that never feel harsh. Typography leans on a serif-display pairing: Lustria for headlines (a slab with humanist warmth) and Lato for body and UI — a clean, approachable sans that keeps long product copy legible. Buttons are generously padded and softly rounded at `{rounded.sm}` (8px), while product cards and the search bar use `{rounded.lg}` (20px) to echo the plushness of the product itself. The brand's signature move is the "Leesa Purple" `#2453ce` — a surprise cobalt used sparingly in the footer and legal links, a small jolt of cool that keeps the warm palette from feeling too heavy. Every surface, from the `{colors.surface-card}` to the `{colors.surface-soft}`, is designed to feel like a well-made bed: structured, inviting, and just soft enough to want to stay in.

colors:
  primary: "#0e3739"
  primary-active: "#1a4143"
  primary-disabled: "#3e5f61"
  ink: "#0c2f30"
  body: "#1a4143"
  muted: "#626262"
  muted-soft: "#757575"
  hairline: "#c7c5c3"
  hairline-soft: "#e3e2e1"
  canvas: "#f7f5f4"
  surface-soft: "#ececeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#cc4d0f"
  accent-orange-hover: "#b44b19"
  accent-orange-soft: "#ff8347"
  accent-gold: "#edcc6c"
  accent-red: "#e22747"
  accent-red-dark: "#b73432"
  accent-blue: "#2453ce"
  badge-sale: "#cc4d0f"
  badge-new: "#2453ce"
  star-rating: "#edcc6c"
  scrim: "#0c2f30"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Lustria', 'Lustria Fallback', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lustria', 'Lustria Fallback', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Lustria', 'Lustria Fallback', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Lato Fallback', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Lato Fallback', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Lato Fallback', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Lato Fallback', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Lato Fallback', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Lato', 'Lato Fallback', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Lato', 'Lato Fallback', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Lato', 'Lato Fallback', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', 'Lato Fallback', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Lato', 'Lato Fallback', 'Helvetica Neue', Arial, sans-serif"
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
    opacity: 0.5
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.accent-orange-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-pill:
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
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.accent-orange}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    opacity: 0.8
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 700
    color: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "12px 20px"
    height: 56px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.on-primary}"
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.on-primary}"
    opacity: 0.9
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
    opacity: 0.8
  footer-link-hover:
    color: "{colors.accent-gold}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    fontWeight: 600
  accordion-content:
    typography: "{typography.body-sm}"
    paddingTop: "{spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Leesa experience, rendered in the brand's deep teal `{colors.primary}` with white text. Used for "Shop Now", "Add to Cart", and primary checkout flows. On hover, shifts to `{colors.primary-active}` (`#1a4143`) for a subtle darkening effect. Disabled state uses `{colors.primary-disabled}` (`#3e5f61`) at 50% opacity. All primary buttons carry 8px rounded corners (`{rounded.sm}`) and 48px height with generous horizontal padding for a substantial, comfortable tap target.

**`button-secondary`** — An outlined variant on the same 48px frame, using a white `{colors.canvas}` background with a 2px `{colors.primary}` border and `{colors.ink}` text. Active state fills the background with `{colors.surface-soft}` (`#ececeb`) and darkens the border to `{colors.primary-active}`. Used for "Learn More" and secondary actions where the brand wants to preserve the teal outline without the full fill.

**`button-accent`** — The warm-orange accent button using `{colors.accent-orange}` (`#cc4d0f`), reserved for limited-time offers, sale CTAs, and promotional banners. Hover state deepens to `{colors.accent-orange-hover}` (`#b44b19`). This button signals urgency and warmth without competing with the primary teal.

**`button-pill`** — A fully rounded pill button (`{rounded.full}`) at 40px height, used for filter tags, size selectors, and compact utility actions. Uses the same `{colors.primary}` fill with `{typography.button-sm}` for tighter spacing.

### Cards
**`product-card`** — The core product display unit, a white card (`{colors.surface-card}`) with 20px rounded corners (`{rounded.lg}`) and 16px padding. Product images sit within a `{rounded.md}` (12px) crop. The title uses `{typography.title-sm}` (18px Lato semibold), while the price is rendered in `{typography.body-md}` at 700 weight in `{colors.primary}`. Sale badges (`{colors.badge-sale}`) and new badges (`{colors.badge-new}`) overlay the top-left corner of the image area in small uppercase 11px labels with 4px rounding.

### Navigation
**`nav-bar`** — A fixed 72px bar in `{colors.primary}` (`#0e3739`), housing the Leesa logo, product category links, and utility icons (search, account, cart). Navigation links are uppercase 14px Lato semibold (`{typography.nav-link}`) with 0.5px letter-spacing. Active page links display a 2px `{colors.accent-orange}` bottom border; inactive links sit at 80% opacity. The bar uses `{spacing.lg}` horizontal padding.

### Forms
**`text-input`** — Standard form fields at 48px height with `{colors.canvas}` background, 1px `{colors.hairline}` border, and 8px rounding. Focus state thickens the border to 2px `{colors.primary}`. Error state uses a 2px `{colors.accent-red}` (`#e22747`) border. Input text is 16px Lato regular with 16px horizontal padding.

### Search
**`search-bar`** — A prominent 56px search field with white background, 20px rounded corners (`{rounded.lg}`), and a 1px `{colors.hairline}` border. Focus state uses a 2px `{colors.primary}` border. Used on the product listing pages and the site-wide search overlay. The generous rounding and height make it feel more like a piece of furniture than a form field.

### Footer
**`footer`** — A full-width section in `{colors.primary}` with white text, padded at `{spacing.xxl}` (48px) vertically. Links are 14px Lato regular at 80% opacity, shifting to `{colors.accent-gold}` (`#edcc6c`) on hover — a warm, unexpected highlight that echoes the brand's accent palette. The footer also contains the surprise cobalt `{colors.accent-blue}` (`#2453ce`) for legal links, a small but intentional departure from the teal ecosystem.

### Badges
**`badge-sale`** and **`badge-new`** — Small uppercase labels (11px Lato bold, 0.5px tracking) used to flag product cards and promotional sections. Sale badges use `{colors.accent-orange}` (`#cc4d0f`); new badges use `{colors.accent-blue}` (`#2453ce`). Both have 4px rounding and 2px/8px padding for a compact, confident presence.

### Accordion
**`accordion`** — Collapsible content panels used on product detail pages (specs, shipping, returns) and FAQ sections. Each panel has a `{colors.canvas}` background, 1px `{colors.hairline-soft}` border, and 8px rounding. The header uses 18px Lato semibold (`{typography.title-sm}`), and the body content is 14px Lato regular with 8px top padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces top nav, hero text reduces to `{typography.display-md}` (28px), buttons go full-width, search bar collapses to icon-only, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, top nav remains but with condensed spacing, hero uses `{typography.display-lg}` (36px), search bar is collapsible, footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links visible, hero at `{typography.display-xl}` (48px), persistent search bar, footer uses 3-column layout |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero remains at `{typography.display-xl}` with larger horizontal padding, all components use max spacing |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are at least 48px tall
- Accordion headers are 48px minimum tap height
- Star rating stars are 24px each with 8px gaps for easy tapping
- Badge labels are kept compact (20px height) as they are informational, not interactive

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px), with a slide-out drawer
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Hero section reduces font size and padding on mobile to avoid text overflow
- Search bar collapses from a full input field to an icon-only toggle on mobile and tablet
- Footer links collapse from 3 columns to a single vertical stack on mobile
- Accordion panels are always collapsed by default on mobile to save vertical space

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary button and text-input focus states were reliably observed
- Error state styling for forms (validation messages, error icons) was not captured from the live site
- Dark mode or high-contrast mode variants are not defined; the brand appears to use only a light theme
- Sub-brand or collection-specific palettes (e.g., Leesa Hybrid vs. Leesa Original) may exist but were not extracted
- Animation and transition timing values (e.g., button hover duration, accordion slide speed) are not specified
- Dropdown and select menu styling (native vs. custom) was not observed
- Modal and overlay component styling (e.g., cart drawer, search overlay) is not captured
- The exact font weights for Lustria (only 400 was found) and Lato (400, 600, 700 were found) may have additional weights in use
- Letter-spacing values for display typography are estimated based on common serif/sans-serif pairings
- The `{colors.accent-blue}` (`#2453ce`) usage appears limited to footer legal links and new badges; its full role in the system is unclear
- Star rating component sizing and spacing are estimated; exact values may vary across product cards
- The `{colors.accent-gold}` (`#edcc6c`) hover state for footer links is inferred from brand palette logic, not directly observed
