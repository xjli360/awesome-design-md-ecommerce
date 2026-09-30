---
version: alpha
name: "Skin Pharm"
source_url: "https://skinpharm.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Skin Pharm presents itself as a clinical yet approachable authority in cosmetic dermatology, balancing medical precision with a warm, human touch. The brand's canvas is a soft, almost papery off-white (`#f7f6f3`), a tone that feels less sterile than pure white and more like a luxury spa's waiting room. This is punctuated by a deep, almost-black ink (`#0c0c0c`) for primary text, creating a high-contrast, legible foundation. The signature accent is a muted, sophisticated clay-terracotta (`#c77743`), used sparingly for key CTAs and hover states, alongside a restrained gold (`#e2c36c`) that whispers of premium ingredients and results. A secondary palette of deep navies (`#272d45`) and muted sage greens (`#3d595b`) appears in badges and secondary elements, lending a clinical, trustworthy feel. The typography is a deliberate mix: the display and headings lean into the elegant, serifed 'Playfair Display', evoking a sense of heritage and bespoke care, while body copy and buttons use the clean, geometric 'Poppins' for readability and a modern edge. This creates a `{rounded.sm}` (8px) radius on buttons and cards, a subtle softening that prevents the clinical from feeling cold. The overall mood is one of quiet confidence — the brand doesn't shout; it reassures with clean lines, generous `{spacing.lg}` and `{spacing.xl}` whitespace, and a color story that feels both earthy and elevated.

colors:
  primary: "#c77743"
  primary-active: "#a85f2f"
  primary-disabled: "#e5d5c8"
  ink: "#0c0c0c"
  body: "#212529"
  muted: "#676986"
  muted-soft: "#888888"
  hairline: "#cccccc"
  hairline-soft: "#e5e5e5"
  canvas: "#f7f6f3"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#e2c36c"
  accent-green: "#70c497"
  accent-teal: "#b2f9e9"
  accent-red: "#ff5268"
  accent-navy: "#272d45"
  accent-sage: "#3d595b"
  badge-new: "#ffcf2a"
  star-rating: "#e2c36c"
  scrim: "#0e0e0e"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Poppins', -apple-system, system-ui, sans-serif"
    fontSize: 10px
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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
    height: auto
  button-tertiary-hover:
    textColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.display-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.sm} {spacing.base}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.base}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    padding: "{spacing.lg} 0"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 52px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-clinical:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-ingredient:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.canvas}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    border-bottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: "0 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Book Consultation", and "Shop Now". It features a warm terracotta (`{colors.primary}`) background with white text (`{colors.on-primary}`) and a subtle 8px (`{rounded.sm}`) radius. On hover, it deepens to a richer clay (`{colors.primary-active}`). The disabled state fades to a muted beige (`{colors.primary-disabled}`) with soft gray text, signaling unavailability without visual noise.

**`button-secondary`** — A ghost-like button with a transparent background and a thin hairline border (`{colors.hairline}`), used for "Learn More" or "View Details" actions. On hover, the border becomes solid black (`{colors.ink}`) and the background shifts to a soft surface tone (`{colors.surface-soft}`), providing a tactile feedback loop that feels deliberate and premium.

**`button-tertiary`** — A text-only link styled as a button, used for "See All" or "Read Reviews". It carries the brand's primary terracotta color and underlines on hover, offering a low-emphasis path that doesn't compete with primary actions.

### Cards
**`product-card`** — The core product display unit, a white card (`{colors.surface-card}`) with an 8px radius. The image sits flush to the top corners, while the title uses the serifed `{typography.display-sm}` for a editorial feel. Price is set in `{typography.body-md}` in the body color. The card has no shadow, relying on the contrast between the white surface and the soft canvas (`{colors.canvas}`) background for separation.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height, using a clean white background (`{colors.canvas}`) and a subtle bottom border (`{colors.hairline-soft}`). Navigation links are set in uppercase Poppins (`{typography.nav-link}`) with 1px letter-spacing. The active state is indicated by a 2px underline in the primary terracotta, a restrained but clear signal.

### Forms
**`text-input`** — Standard input fields for forms, with a white background, 8px radius, and a light gray border. On focus, the border switches to the primary terracotta (`{colors.primary}`). Error states are communicated with a red border (`{colors.accent-red}`), providing clear, color-coded feedback without additional iconography.

### Badges
**`badge-new`** — A bright yellow (`{colors.badge-new}`) pill badge used to flag new products or arrivals. The high-contrast yellow against the dark ink text creates immediate visual priority.
**`badge-clinical`** — A deep navy (`{colors.accent-navy}`) pill badge for "Clinical Strength" or "Dermatologist Recommended" labels, reinforcing the brand's medical authority.
**`badge-ingredient`** — A muted sage green (`{colors.accent-sage}`) pill badge for key ingredient callouts like "Vitamin C" or "Retinol", tying the product story back to its formulation.

### Footer
**`footer`** — A dark, anchored footer using the deepest ink (`{colors.ink}`) as the background. Links are set in a muted gray (`{colors.muted-soft}`) and transition to white on hover. The layout uses generous `{spacing.xxl}` padding, creating a grounded, stable base for the page.

### Accordion
**`accordion-trigger`** — Used for FAQ sections and product details. The trigger is a borderless, uppercase title with a bottom hairline separator. The content area uses body-sm text in the body color, maintaining readability and a clean, collapsible structure.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger menu, product cards stack full-width, hero text centers, buttons become full-width |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, hero retains left-aligned text with smaller display-xl (36px) |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with dropdowns, hero uses full display-xl (48px), sidebars appear on product pages |
| Wide | > 1440px | Max-width container (1440px) centers content, product grid can expand to four columns, larger hero imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon-only buttons (search, cart, menu) have a 44x44px tap area, even if the icon is smaller.
- Accordion triggers have a minimum 48px tap height for comfortable finger interaction.

### Collapsing Strategy
- The top navigation collapses into a hamburger menu below 744px, with a slide-in drawer for links.
- Product filters collapse into a "Filter" button that opens a modal or bottom sheet on mobile.
- The footer's multi-column link sections stack into a single column, with accordion-style toggles for each category.
- Hero sections reduce padding and font sizes, with CTA buttons stacking vertically.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for tertiary buttons (underline vs. color change) could not be fully confirmed.
- Error styling for form inputs (iconography, helper text color) is inferred from the accent-red but not verified.
- Sub-brand palettes for specific product lines (e.g., "Clinical" vs. "Daily Essentials") were not extracted.
- Dark mode is not present on the live site; all tokens assume a light theme.
- Specific shadow values (box-shadow) for cards or modals were not reliably extracted from the CSS.
- Active/focus ring styles for keyboard navigation are not defined.
- The exact font weight for 'Playfair Display' in headings is inferred from common web usage; the live site may use a different weight.
- Spacing values for `section` are a standard estimate; the live site may use 80px or 96px for major sections.
