---
version: alpha
name: "Twelve South"
source_url: "https://www.twelvesouth.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, almost forest-green #121713 anchors the Twelve South canvas — not a sterile white but a rich near-black that makes every product shot of leather BookBook cases and polished aluminum stands feel like a still life on a dark walnut desk. The brand's signature voltage comes from a teal-cyan #045c7d, used sparingly on hover states, selectable highlights, and the thin underline on active navigation links; it reads as precision engineering rather than playfulness. A secondary accent of #ff4127 (a warm, urgent red-orange) appears on sale badges and limited-edition callouts, while #ffcf2a (a restrained marigold) marks loyalty or exclusive drops. The typography stack is freight-sans-pro in multiple cuts — condensed for display headlines, compressed for tight product titles, and a book weight for body copy — giving the system a tailored, editorial density that feels closer to a design magazine than an accessories storefront. Buttons use {rounded.sm} corners (8px) with a subtle lift, while product cards and feature modules take {rounded.md} (12px) — enough softness to feel approachable, not enough to feel casual. The primary CTA is a solid #121713 pill with white text, and on hover it inverts to a white fill with #121713 text and a thin #121713 border, a quiet reveal that rewards interaction. The footer and secondary navigation use a lighter ink #404041 on a #eff5f3 canvas (a pale, cool off-white), creating a clear hierarchy between the dark hero zone and the informational lower layers. Every component feels machined — the spacing is generous but never loose, the radii are present but never pillowy, and the color palette is restrained to three families: deep charcoal, teal-accent, and warm signal.

colors:
  primary: "#121713"
  primary-active: "#045c7d"
  primary-disabled: "#637473"
  ink: "#121713"
  body: "#404041"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#d3d2d1"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#045c7d"
  accent-red: "#ff4127"
  accent-gold: "#ffcf2a"
  accent-cyan: "#08a5df"
  accent-mint: "#b2f9e9"
  accent-teal-light: "#00caaa"
  accent-blue: "#1199ff"
  ink-light: "#495857"
  ink-mid: "#525252"
  ink-dark: "#1a1b18"
  ink-navy: "#272d45"
  ink-slate: "#2c3e50"
  ink-charcoal: "#282828"
  surface-warm: "#eff5f3"
  surface-cool: "#f4f4f6"
  surface-gray: "#dbdde4"
  surface-light: "#f7f7f7"
  border-soft: "#d3d4dd"
  border-mid: "#6d6e70"
  border-strong: "#3d4246"
  scrim: "#101010"

typography:
  display-xl:
    fontFamily: "'freight-sans-condensed-pro', 'freight-sans-compressed-pro', 'FreightSansProBook-Regular', 'roboto', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'freight-sans-condensed-pro', 'freight-sans-compressed-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'freight-sans-condensed-pro', 'freight-sans-compressed-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'freight-sans-condensed-pro', 'freight-sans-compressed-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.15px
  badge:
    fontFamily: "'freight-sans-condensed-pro', 'freight-sans-compressed-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'freight-sans-condensed-pro', 'freight-sans-compressed-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
  button-primary-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
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
    border: "2px solid {colors.hairline}"
    padding: 12px 26px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 12px 26px
    height: 48px
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-teal}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-red}"
    padding: 12px 16px
    height: 48px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  top-nav-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.accent-teal}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  mobile-nav-toggle:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 40px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.accent-teal}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-light:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  feature-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  feature-card-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.accent-teal}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  newsletter-submit:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link-active:
    typography: "{typography.caption}"
    textColor: "{colors.body}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.accent-teal}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  rating-star:
    textColor: "{colors.accent-gold}"
    fontSize: 14px
  rating-star-empty:
    textColor: "{colors.hairline}"
    fontSize: 14px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid #121713 rectangle with 8px corners and white text in freight-sans-pro 15px/600. On hover, the fill drops to white and a 2px #121713 border appears, creating a clean inversion. Disabled state uses #637473, a muted teal-gray that signals inactivity without visual noise. **`button-secondary`** — A white button with a #d3d2d1 hairline border; hover promotes the border to #121713 and adds a #f7f7f8 background wash. **`button-accent-teal`** — Uses #045c7d as fill for actions that need emphasis without the full weight of the primary — typically "Learn More" or "Explore" links in feature sections. **`button-accent-red`** — A compact 40px-tall button with #ff4127 fill, reserved for sale badges, limited-edition callouts, and urgency-driven CTAs. **`button-ghost`** — Transparent background with #121713 text; hover reveals a #f7f7f8 surface. Used for tertiary actions in dense layouts.

### Cards
**`product-card`** — A white card with 12px rounded corners, containing a square-ratio product image (also 12px radius), a 16px/600 title, and a 14px/400 price line. On hover, a subtle 4px-12px box shadow lifts the card. **`feature-card`** — A white card with 12px radius and 24px padding, used for editorial content blocks. A dark variant (`feature-card-dark`) inverts to #404041 background with white text, used in alternating sections. **`product-card-badge`** — A small #ff4127 pill with white uppercase 11px/700 text, placed at the top-left of product images. A gold variant (`product-card-badge-gold`) uses #ffcf2a with #121713 text for exclusive or loyalty-tagged items.

### Navigation
**`top-nav`** — A 72px white bar with uppercase 14px/600 condensed freight-sans links. Active links get a 2px #045c7d underline. On scroll, the bar shrinks to 64px and gains a faint 1px-3px shadow. **`nav-link-active`** — Inherits the nav typography but adds the teal underline; inactive links render in #676986. **`mobile-nav-toggle`** — A compact 40px square with 4px radius, used to reveal the mobile menu.

### Forms
**`text-input`** — A 48px-tall white input with 8px radius and a #d3d2d1 border. On focus, the border switches to #045c7d. Error state uses #ff4127 border. **`select-input`** — Same dimensions and border treatment as text-input, with a custom dropdown arrow. **`textarea`** — Same styling as text-input but with no fixed height, used for contact forms and product reviews. **`newsletter-input`** — A 44px-tall input paired with a 44px #045c7d submit button, used in the footer.

### Footer
**`footer-section`** — A #121713 background section with white text in 14px/400. Links are white by default and shift to #045c7d on hover. The section uses 48px vertical padding and 24px horizontal padding. **`footer-link`** — Uses `typography.link` (14px/500) with white color; hover transitions to the teal accent.

### Other Components
**`search-bar`** — A pill-shaped 44px-tall input with #f7f7f8 background and #d3d2d1 border. On focus, the border turns #045c7d and the background goes white. **`hero-section`** — A full-width section with #121713 background and 48px/700 white display text, padded 64px vertically and 24px horizontally. A light variant uses #eff5f3 background with #121713 text. **`breadcrumb-link`** — 13px/400 text in #676986; the active (current page) breadcrumb uses #404041. **`pagination-button`** — 36px-tall buttons with 8px radius and #d3d2d1 border; active page uses #121713 fill with white text. **`accordion-header`** — A 16px/600 title with a 1px #e5e5e5 bottom border; content area uses 16px/400 body text with 8px top and 16px bottom padding. **`tab-active`** — Uppercase 14px/600 text with a 2px #045c7d underline; inactive tabs render in #676986. **`rating-star`** — 14px stars in #ffcf2a; empty stars use #e5e5e5. **`divider`** — A 1px line in #d3d2d1; a softer variant uses #e5e5e5. **`tooltip`** — A #404041 background with white 13px/400 text, 4px radius, and 6px-10px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack vertically; hero text reduces to 28px; footer links stack; search bar moves to full-width below nav; accordion replaces tabbed navigation; buttons go full-width. |
| Tablet | 744–1128px | Two-column product grid; top-nav shows 4-5 links; hero uses 36px display; footer splits into 2-column grid; search bar remains in nav; feature cards use 2-column layout. |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero uses 48px display; footer uses 4-column grid; feature cards use 3-column layout; side-by-side hero content. |
| Wide | > 1440px | Max-width container at 1440px; product grid can show 4 columns; hero content centered with max-width; whitespace scales proportionally; feature cards use 4-column grid. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility.
- Product card tap targets use the full card surface area.
- Mobile nav toggle is 40px × 40px with 8px padding around the icon.
- Accordion headers are 48px minimum height to accommodate touch.
- Pagination buttons are 36px × 36px with 12px padding between them.

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px; the hamburger icon is a 40px square with 4px radius.
- Product grid collapses from 3 columns (desktop) to 2 columns (tablet) to 1 column (mobile).
- Footer grid collapses from 4 columns (desktop) to 2 columns (tablet) to stacked (mobile).
- Feature cards collapse from 3 columns (desktop) to 2 columns (tablet) to 1 column (mobile).
- Tabbed navigation collapses to accordion below 744px.
- Hero section collapses from side-by-side text/image to stacked layout on mobile.
- Search bar collapses from inline in the nav to a full-width element below the nav on mobile.
- Breadcrumbs truncate on mobile, showing only the current page and a "Back" link.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product-card-badge, newsletter-submit, and accordion-header were not reliably extracted from the live site; the hover behaviors described are inferred from common patterns in the brand's design language.
- Error styling for forms (validation messages, error iconography) was not observed; the text-input-error border color is an assumption based on the accent-red.
- Dark mode is not present on the live site; no dark-mode palette has been defined.
- The exact font weights for freight-sans-pro cuts (light, book, medium, semi-bold, bold) were not fully extractable; the weights used in the typography block are best guesses based on observed text rendering.
- Sub-brand or collection-specific color palettes (e.g., BookBook, HiRise, Compass) were not extracted; the brand may use secondary palettes for product lines.
- The `boxShadow` values for product-card-hover and top-nav-scrolled are approximations; the exact shadow tokens were not extractable from the live CSS.
- The accent-gold (#ffcf2a) and accent-mint (#b2f9e9) colors appeared infrequently; their usage patterns (loyalty badges, eco-friendly callouts) are inferred.
- The extracted color list includes several generic web colors (#3d4246, #6d6e70, #282828, #f7f7f7, #86d8f7) that may be Shopify framework defaults or stock-image tones; they have been mapped to the most likely brand roles (border-strong, border-mid, ink-charcoal, surface-light, accent-cyan-light) but should be verified against the brand's actual design tokens.
- No animation or transition timing tokens (duration, easing) were extractable; the brand likely uses consistent motion patterns that are not captured here.
- The font stack includes "Font Awesome 5 Brands" and "Font Awesome 5 Free" which are icon fonts; these are not reflected in the typography block but are used throughout the UI for social icons and utility symbols.
- The "oke-widget-icons" font family suggests the brand uses Okendo for product reviews; the review widget styling (stars, text, layout) was not extracted.
