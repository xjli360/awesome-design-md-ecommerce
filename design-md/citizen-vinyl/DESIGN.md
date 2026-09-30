---
version: alpha
name: "Citizen Vinyl"
source_url: "https://www.citizenvinyl.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A working record-pressing plant in Asheville, North Carolina, Citizen Vinyl’s digital presence is a clean, industrial-tinged storefront that lets the craft of vinyl manufacturing speak for itself. The site runs on Roboto across all weights — a utilitarian sans-serif that reads as no-nonsense and workmanlike, echoing the machinery and precision of the pressing floor. Without a single extracted brand color to anchor the palette (the live site returned no distinctive hexes beyond framework defaults), the design system defaults to a monochrome canvas of pure white `#ffffff` and near-black `#222222`, with warm gray `#6a6a6a` for body text and a softer `#929292` for muted labels. The absence of a signature brand color is itself a statement: Citizen Vinyl is not a lifestyle brand selling nostalgia, but a service provider selling quality, turnaround time, and audio fidelity. Buttons are squared off at `{rounded.sm}` (8px), cards at `{rounded.md}` (12px), and the hero section uses generous `{spacing.section}` (64px) vertical padding to create breathing room around product shots of raw vinyl and finished jackets. The nav bar is a thin, 64px strip with a logo lockup on the left and text links in `{typography.nav-link}` — no hamburger, no search bar, no cart icon cluttering the header. The overall feel is that of a precision workshop’s website: functional, trustworthy, and designed to get out of the way of the product.

colors:
  primary: "#222222"
  primary-active: "#000000"
  primary-disabled: "#c1c1c1"
  ink: "#222222"
  body: "#3f3f3f"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#d4a373"
  accent-vinyl: "#2b2b2b"

typography:
  display-xl:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-accent:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid #c13515"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    border-bottom: "2px solid {colors.ink}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "#c13515"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  section-heading:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    margin-bottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    margin-bottom: "{spacing.xl}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.xl} 0"
  loading-spinner:
    border: "3px solid {colors.hairline-soft}"
    borderTop: "3px solid {colors.ink}"
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Get a Quote," "Start Your Order," and "Contact Us." Solid near-black fill with white text, 8px rounded corners, and 44px height for a substantial but not bulky feel. On hover, the background deepens to pure black `{colors.primary-active}`. The disabled state uses a light gray `{colors.primary-disabled}` to visually remove the button from interactive consideration.

**`button-secondary`** — An outlined alternative for secondary actions like "Learn More" or "View Pricing." White background with a 1px hairline border, matching the primary button's height and typography. Hover state adds a subtle shadow or border darkening to `{colors.ink}`. Used alongside primary buttons in hero sections and service cards.

**`button-tertiary-text`** — A text-only button for inline actions such as "Read the FAQ" or "See All Services." No background, no border, using the same button typography weight for visual consistency. Hover state adds an underline or slight opacity shift.

**`button-accent`** — A warm accent button reserved for promotional or seasonal calls-to-action, such as "Limited Edition Pressing" or "Shop New Arrivals." Uses a warm terracotta `{colors.accent-warm}` background to draw attention without competing with the primary black button. Same dimensions and rounded corners as the primary button.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 64px height, pure white background with a subtle bottom hairline. The logo sits left-aligned, with uppercase nav links (About, Services, Pressing, Contact) spaced evenly to the right. No search bar, no cart icon — the nav is intentionally sparse to reflect the brand's no-frills industrial ethos. Active page links get a 2px bottom border in `{colors.ink}`.

**`nav-link-active`** and **`nav-link-inactive`** — Active links use the full ink color with a bottom border indicator; inactive links use `{colors.muted}` to recede. Hover state on inactive links transitions to `{colors.ink}`.

### Cards
**`product-card`** — Used for vinyl products, services, and case studies. A white card with 12px rounded corners, 16px padding, and a soft hairline border. The card contains a square-ratio image at the top with 8px rounded corners, followed by a title and price or description. Hover state adds a subtle elevation shadow and border darkening to `{colors.hairline}`.

### Forms
**`text-input`** — Standard text input fields for contact forms, quote requests, and order details. 48px height with 12px padding, 8px rounded corners, and a 1px hairline border. On focus, the border switches to `{colors.ink}` for clear visual feedback. Error state uses a red border `#c13515` with an optional error message below.

**`select-input`** — Dropdown select fields matching the text-input dimensions and styling. Used for order quantity, vinyl weight, and jacket options. The dropdown arrow is a custom SVG in `{colors.muted}`.

### Badges
**`badge-new`** — A small warm-accent badge for "New" or "Featured" labels on products. 11px uppercase bold text on a terracotta background with 4px rounded corners and 2px horizontal padding.

**`badge-sale`** — A red badge for sale or promotional items. Uses the same dimensions and typography as the new badge but with a red `#c13515` background for urgency.

### Footer
**`footer-section`** — A dark footer with near-black background and white text. Contains three columns: About, Services, and Contact. Links use `{colors.muted-soft}` with a hover transition to white. The footer includes the physical address of the Asheville pressing plant and social media icons in white.

### Loading & Feedback
**`loading-spinner`** — A 24px circular spinner with a light gray track and ink-colored top arc, used during form submissions and page transitions. The full rounded value creates the perfect circle.

**`tooltip`** — Dark tooltips with white text, 4px rounded corners, and minimal padding. Used for clarifying form labels and icon buttons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero padding reduced to 32px; product cards stack vertically; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 48px padding; footer uses two-column layout |
| Desktop | 1128–1440px | Full three-column product grid; expanded hero with side-by-side text and image; full nav bar with all links visible |
| Wide | > 1440px | Max-width container at 1280px; hero content centered with wider margins; product grid can expand to four columns if content allows |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Nav links have 48px touch targets even when text is smaller
- Form inputs are 48px tall to accommodate both desktop and mobile tap targets
- Icon buttons in the mobile hamburger menu are 44x44px

### Collapsing Strategy
- Navigation: On mobile (< 744px), the full nav link list collapses into a hamburger menu with a slide-down overlay
- Product grid: Drops from 3 columns on desktop to 2 on tablet to 1 on mobile
- Footer: Collapses from 3 columns on desktop to 2 on tablet to a single stacked column on mobile
- Hero section: Side-by-side text and image on desktop stacks vertically on mobile and tablet
- Form layouts: Multi-column form fields collapse to single column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted brand colors were available from the live site — the palette above is inferred from the brand's industrial positioning and the Roboto font choice. The true brand colors (if any exist beyond black and white) remain unknown.
- No hover, focus, or active states could be extracted for any component — all interaction states above are best-practice defaults for a monochrome system.
- Error styling for forms (red border, error message typography) is assumed from common patterns, not extracted from the live site.
- No data on the brand's logo usage (color vs. white version, minimum size, clear space) could be extracted.
- No information on the brand's photography style, image treatment (filters, overlays), or iconography system was available.
- The accent-warm color `#d4a373` is an assumption based on the vinyl/record aesthetic — it may not appear on the actual site.
- No dark mode preferences or alternative color schemes were detected.
- No data on the brand's use of shadows, elevation, or depth cues beyond basic borders.
- The site's actual typography scale may include additional sizes or weights not captured in the single Roboto declaration found.
- No information on the brand's use of animation, transitions, or micro-interactions was available.
