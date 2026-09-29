---
version: alpha
name: "United Record Pressing"
source_url: "https://www.unitedrecordpressing.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A Nashville vinyl pressing plant that has been spinning records since 1949, United Record Pressing communicates through the warmth of physical media — its digital presence is a study in analog fidelity. The brand's primary color, `#e7762b`, is a burnt orange that reads like the glow of a tube amplifier or the label on a vintage 45 RPM single, not a generic web accent. It appears on CTAs and key navigation elements against a near-white canvas (`#fafafa`) and a secondary teal (`#2a7f89`) that echoes the patina of old recording studio equipment. The typography stack favors Montserrat and Open Sans — clean, geometric sans-serifs that balance readability with a slight mid-century modern feel, avoiding the overly decorative or the sterile. Cards and buttons use `{rounded.sm}` (8px) corners, a subtle nod to the rounded edges of record sleeves without going fully pill-shaped. The layout is generously spaced (`{spacing.section}` 64px between major content blocks), giving each product image and description room to breathe, much like the wide grooves on a 12-inch LP. A secondary accent of deep brown (`#744e45`) appears in footer and secondary text, grounding the palette in earthy, tactile tones. The overall impression is that of a well-loved record shop — organized, purposeful, and unpretentious, with every design decision deferring to the physical object at the center of the experience: the vinyl record itself.

colors:
  primary: "#e7762b"
  primary-active: "#c95f1f"
  primary-disabled: "#f5c8a3"
  ink: "#070909"
  body: "#3a3a3a"
  muted: "#808285"
  muted-soft: "#949494"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#fafafa"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  teal-accent: "#2a7f89"
  teal-accent-hover: "#1e6b73"
  brown-accent: "#744e45"
  blue-accent: "#0274be"
  star-rating: "#ff9900"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    padding: 12px 28px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-teal:
    backgroundColor: "{colors.teal-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-teal-active:
    backgroundColor: "{colors.teal-accent-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
  product-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-title:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 80px 0
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  badge-new:
    backgroundColor: "{colors.teal-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 36px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in burnt orange (`{colors.primary}`) with white text. Used for "Add to Cart", "Start Your Order", and "Get a Quote" actions. On hover, shifts to a deeper shade (`{colors.primary-active}`) for a tactile press feel. Disabled state uses a muted peach (`{colors.primary-disabled}`) to signal inactivity without visual noise.

**`button-secondary`** — An outlined variant with a white background and orange border. Used for secondary actions like "Learn More" or "View Details". On hover, fills with the primary orange, inverting the color relationship. Maintains the same 44px height and `{rounded.sm}` corners as the primary button for consistency.

**`button-tertiary-text`** — A text-only button with no background or border. Used for less prominent actions like "Cancel" or "Skip". The orange text color (`{colors.primary}`) maintains brand consistency while reducing visual weight. Hover state adds a subtle underline.

**`button-teal`** — A secondary accent button using the teal (`{colors.teal-accent}`) palette. Reserved for contextual actions like "View Pressing Details" or "Explore Vinyl Options" where the orange primary would create visual competition. On hover, darkens to `{colors.teal-accent-hover}`.

### Cards
**`product-card`** — A white card with `{rounded.sm}` corners and 16px padding, used to display vinyl products in grid layouts. The card contains a square aspect-ratio image with `{rounded.xs}` corners, a product title in `{typography.body-md}`, and a price in `{typography.title-sm}` colored with `{colors.primary}`. On hover, a subtle box shadow lifts the card from the canvas. The card background is `{colors.surface-card}` (#ffffff) against the `{colors.canvas}` (#fafafa) page background.

### Navigation
**`nav-bar`** — A fixed-height (72px) top navigation bar with a white background and a thin bottom border (`{colors.hairline-soft}`). Navigation links use `{typography.nav-link}` — Montserrat at 14px with 0.5px letter spacing and uppercase transformation. Active or hovered links switch to `{colors.primary}`. The bar contains the brand logo on the left, primary navigation links in the center, and utility icons (search, cart) on the right.

### Forms
**`text-input`** — Standard text input fields with a white background, `{rounded.sm}` corners, and a 1px hairline border. On focus, the border switches to `{colors.primary}` orange. Error states use the same orange border to indicate validation issues. Height is 44px with 10px vertical padding for comfortable touch interaction.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input with a white background and hairline border. Used in the navigation and on search results pages. On focus, the border transitions to `{colors.primary}`. The pill shape provides a distinct visual cue that differentiates search from other text inputs.

### Badges
**`badge-new`** — A small teal badge (`{colors.teal-accent}`) used to indicate new product arrivals or recently added vinyl pressings. Uses `{typography.badge}` — uppercase Montserrat at 11px with 0.5px letter spacing. Padding is minimal (2px 8px) with `{rounded.xs}` corners.

**`badge-sale`** — An orange badge (`{colors.primary}`) used to indicate sale items or promotional pricing. Same typography and sizing as the new badge, but uses the primary orange for visual urgency.

### Footer
**`footer`** — A dark footer section with `{colors.ink}` (#070909) background and muted gray text (`{colors.muted-soft}`). Links use `{typography.link}` and shift to `{colors.primary}` on hover. The footer is organized in columns with section headers in `{typography.title-sm}`. Vertical padding is 48px with a 64px section spacing above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-lg}`; search bar moves to expandable icon; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero section uses `{typography.display-xl}` at smaller scale; sidebar content moves below main content |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero section at full scale; sidebar remains visible; search bar is always expanded |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero section uses wider padding; additional whitespace between sections |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Navigation links have 48px touch targets (padding extends hit area)
- Product cards have full-card tap targets for navigation
- Search bar has 44px height with expanded touch area
- Quantity selector buttons are 36px minimum with adequate spacing

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Footer columns stack vertically below 744px
- Hero section text reduces in size and padding below 744px
- Sidebar content (filters, related products) moves below main content on tablet and mobile
- Search bar collapses to icon-only on mobile, expanding on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors include many framework defaults and generic web colors (grays, blues) that may not be brand-specific — the primary (`#e7762b`), teal (`#2a7f89`), and brown (`#744e45`) are the most distinctive and likely brand colors
- Font-family declarations are inferred from the site's CSS but exact hierarchy and weights for each typography token are estimated based on common usage patterns for Montserrat and Open Sans
- Hover and active states for most components are estimated based on standard darkening/lightening patterns rather than extracted values
- Error, success, and warning color states for forms are not extracted — orange is used as a fallback for error states based on brand color usage
- Dark mode is not supported and no dark mode colors were extracted
- Sub-brand or seasonal color palettes (if any) are not captured
- Exact border radii for specific components (cards, buttons, inputs) are estimated based on common patterns — the extracted data does not include specific radius values
- Animation and transition timing values (ease-in-out durations, spring animations) are not available
- Iconography style and sizing guidelines are not extracted
- The extracted color list includes `#00d084` (a bright green) and `#0693e3` (a bright blue) which are likely WordPress/plugin defaults and should be ignored for brand purposes
