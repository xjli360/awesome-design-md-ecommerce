---
version: alpha
name: "PowerXL"
source_url: "https://www.powerxlproducts.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep navy (#002873) dominates every header bar, hero banner, and call-to-action on a site that sells sizzle as much as it sells countertop hardware. PowerXL's digital presence channels the energy of a live cooking demo — oversized product photography bleeds edge-to-edge, price callouts land in bold white-on-navy lockups, and "Add to Cart" buttons punch through the layout like the satisfying click of an air-fryer lid. Typography runs on Rubik, a geometric sans-serif whose slightly rounded terminals soften what would otherwise be a purely industrial palette of navy, near-black (#121212), and cool gray (#dedede). Display headlines land at weight 700 in the 36–48px range, large enough to compete with product imagery for attention, while body copy drops to weight 400 at 16px — functional, readable, never precious. Corner radii stay tight: product cards and input fields sit at `{rounded.sm}` (8px), buttons at `{rounded.xs}` (4px), giving the interface a confident, squared-off posture that mirrors the boxy silhouettes of the appliances themselves. Spacing is generous vertically — hero sections breathe with `{spacing.section}` or more — but the grid packs product cards shoulder-to-shoulder on desktop, three or four across, reinforcing the "wall of options" merchandising strategy common to infomercial-heritage brands. A single accent orange (#f26522) fires on sale badges and urgency messaging, providing the only warm interruption in an otherwise cool-toned system. The overall effect is a high-contrast, high-energy retail environment where navy establishes authority, white space gives the eye a rest between product pitches, and every interactive element is sized for confident thumb taps on mobile — because most of this traffic arrives via social ads on a phone screen.

colors:
  primary: "#002873"
  primary-active: "#001d5c"
  primary-disabled: "#7a9bc4"
  accent: "#f26522"
  accent-active: "#d9541a"
  ink: "#121212"
  body: "#333333"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#002873"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent: "#ffffff"
  sale: "#f26522"
  star-rating: "#f5a623"
  success: "#2e7d32"
  error: "#d32f2f"

typography:
  display-xl:
    fontFamily: "'Rubik', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
    textDecoration: line-through
  badge:
    fontFamily: "'Rubik', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
  hero: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 50px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 50px
    border: 2px solid {colors.primary}
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 50px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
    height: 54px
    width: 100%
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.lg}
  nav-bar-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    boxShadow: 0 4px 12px rgba(0,0,0,0.12)
  announcement-bar:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption}"
    height: 36px
    padding: "{spacing.sm} {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.hero} {spacing.xl}"
    minHeight: 520px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    hoverShadow: 0 4px 16px rgba(0,40,115,0.1)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: 1/1
    objectFit: contain
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  collection-grid:
    gap: "{spacing.lg}"
    columns: 4
    padding: 0 {spacing.xl}
  price-block:
    currentTypography: "{typography.price-display}"
    currentColor: "{colors.ink}"
    compareTypography: "{typography.price-compare}"
    compareColor: "{colors.muted}"
    gap: "{spacing.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 48px
    border: 1px solid {colors.hairline}
    buttonWidth: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: 0 {spacing.base}
    border: 1px solid {colors.hairline}
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-newsletter:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  rating-stars:
    filledColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: "{spacing.xxs}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    gap: "{spacing.sm}"

---

## Components

### Buttons

**`button-primary`** — Full navy background with white uppercase text at weight 600. Corners are sharply defined at `{rounded.xs}` (4px), reinforcing the industrial appliance aesthetic. Hover darkens to `{colors.primary-active}`; disabled state washes out to `{colors.primary-disabled}` with reduced opacity. Minimum tap area is 50px tall with generous horizontal padding for confident mobile interaction.

**`button-secondary`** — White background with a 2px navy border and navy text. Shares the same dimensions and radius as primary but visually recedes, used for secondary actions like "View Details" or "Compare." On hover, fills with `{colors.primary}` and text flips to white.

**`button-accent`** — Orange (#f26522) background reserved for urgency-driven CTAs: flash sales, limited-time bundles, and "Shop Now" prompts in promotional banners. Active state deepens to `{colors.accent-active}`. Used sparingly to maintain its signal strength.

**`button-add-to-cart`** — Full-width variant of the primary button appearing on product detail pages. Taller (54px) and wider than standard buttons, it anchors the purchase decision at the bottom of the product info stack. Text is uppercase "ADD TO CART" in `{typography.button-lg}`.

### Navigation

**`nav-bar`** — Solid navy bar spanning the full viewport width at 64px height. Logo sits left, navigation links center or right in white `{typography.nav-link}` text. Dropdown menus appear on hover with white backgrounds, subtle box shadows, and `{rounded.xs}` corners. Mobile collapses to a hamburger icon triggering a full-screen navy overlay.

**`announcement-bar`** — Slim 36px orange strip above the nav carrying promotional copy (free shipping thresholds, sale countdowns). White text in `{typography.caption}` ensures legibility against the warm orange. Dismissible on mobile with an × icon.

### Product Cards

**`product-card`** — White card with a 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners. Product image sits in a square container with `{colors.surface-soft}` background and `contain` fit — appliances are shown in full, never cropped. Title appears below in `{typography.title-sm}`, followed by the price block. On hover, a subtle box shadow (navy-tinted at 10% opacity) lifts the card, and a "Quick View" overlay may appear on desktop. Sale badges position absolute in the top-left corner of the image area.

**`product-card-image`** — Square aspect ratio container. Background is `{colors.surface-soft}` to give white/silver appliances enough contrast. Images use `object-fit: contain` with ~8% internal padding so the product never touches the frame edge.

### Hero

**`hero-banner`** — Full-bleed section with navy background, minimum 520px tall. Large product photography occupies 50–60% of the width on desktop, with headline text (`{typography.display-xl}`) and a CTA button stacked on the opposite side. On mobile, image stacks above text. Hero padding uses `{spacing.hero}` (80px) vertically to give the composition room to breathe.

### Pricing

**`price-block`** — Current price in `{typography.price-display}` (24px, bold) next to a struck-through compare-at price in `{typography.price-compare}` (16px, regular weight, `{colors.muted}`). When a sale badge is present, the current price may render in `{colors.sale}` for emphasis.

### Form Elements

**`text-input`** — 48px tall with 1px `{colors.hairline}` border, `{rounded.xs}` corners. On focus, border transitions to `{colors.primary}`. Error state swaps border to `{colors.error}` and shows helper text below in `{typography.caption}` colored `{colors.error}`.

**`quantity-selector`** — Inline stepper with minus/plus buttons flanking a numeric input. Same border treatment as text-input. Button regions are 48×48px for easy touch targeting.

### Search

**`search-bar`** — 44px tall input with a magnifying-glass icon in `{colors.muted}` at the left. Appears in the nav on desktop (inline, right-aligned) and as a full-width overlay on mobile. Border is `{colors.hairline}`; focus state mirrors text-input behavior.

### Footer

**`footer`** — Navy background matching the nav, with white text organized in 3–4 columns on desktop: product categories, support links, company info, and a newsletter signup. Headings use `{typography.title-sm}` in white; links use `{typography.body-sm}`. Generous `{spacing.section}` padding top and bottom.

**`footer-newsletter`** — Slightly darker navy (`{colors.primary-active}`) inset block containing an email input and submit button. Rounded at `{rounded.xs}`, padded with `{spacing.lg}`.

### Utility

**`sale-badge`** — Compact orange pill (4px radius) carrying "SALE" or percentage-off text in `{typography.badge}`. Positioned absolutely over product card images.

**`rating-stars`** — Five-star display using filled `{colors.star-rating}` (#f5a623) and empty `{colors.hairline}` states. Each star is 16px with `{spacing.xxs}` gap. Often paired with a review count in `{typography.caption}`.

**`breadcrumb`** — Slash-separated path in `{typography.caption}`, muted gray for ancestors, ink for the current page. Sits below the nav with `{spacing.base}` vertical margin.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen overlay; hero stacks image above text; Add to Cart button becomes sticky at bottom of viewport; announcement bar text truncates with marquee on long messages |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links but categories collapse to dropdowns; hero shifts to 60/40 image-text split; footer goes to 2-column layout |
| Desktop | 1128–1440px | Three- to four-column product grid at `{spacing.lg}` gap; full horizontal nav with dropdowns on hover; hero at full 50/50 composition; footer in full 4-column layout |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid holds 4 columns with increased card size; hero imagery scales proportionally with `max-height: 640px` |

### Touch Targets

- All interactive elements maintain a minimum 44×44px tap target on mobile
- Quantity selector buttons are 48×48px with clear visual boundaries
- Nav links in mobile overlay are spaced at `{spacing.lg}` (24px) vertically for thumb-friendly access
- Add to Cart sticky bar on mobile is 54px tall with full-width tap area

### Collapsing Strategy

- Product filters collapse to a slide-out drawer on mobile, triggered by a "Filter" button above the grid
- Mega-menu category navigation becomes an accordion within the hamburger overlay
- Product description tabs (features, specs, reviews) stack vertically as expandable accordions
- Footer columns collapse to accordion sections with `{typography.title-sm}` headers as toggle triggers
- Comparison tables scroll horizontally with a sticky first column for product names

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only three colors were extractable from the live site (#002873, #dedede, #121212); the accent orange (#f26522) is inferred from PowerXL's widely-used promotional materials and TV-heritage branding but could not be confirmed from static page extraction
- No CSS custom properties or design-token files were accessible — Shopify theme likely loads styles via compiled assets or JS injection
- Exact border-radius values could not be extracted; `{rounded.xs}` (4px) and `{rounded.sm}` (8px) are estimated from visual inspection of the Shopify theme patterns
- Icon system (line weight, size grid, stroke vs. fill) is undocumented
- Exact box-shadow values on hover states are approximated
- Animation/transition timing (hover effects, mobile menu slides) could not be extracted
- The site may use additional weights of Rubik (300, 500, 700, 900) but only the family name was detectable in font-stack declarations
