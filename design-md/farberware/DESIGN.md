---
version: alpha
name: "Farberware"
source_url: "https://www.farberwareappliances.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  One hundred and twenty-six years of stamped-steel heritage distilled into a countertop-appliance portal — Farberware's digital presence leads with product photography at near-catalog scale, letting stainless-steel drums and matte-black control panels speak before a single headline loads. The palette anchors on a deep navy (#1a2b4a) pulled from the brand's long-standing wordmark, paired with a warm signal red (#c8102e) that marks CTAs and sale callouts the way a power indicator LED marks an appliance as "on." Body copy sits in a neutral charcoal (#333333) over a bright white canvas (#ffffff), while product cards float on a barely-warm gray surface (#f5f5f5) that reads like brushed aluminum under studio light. Typography leans on a geometric sans-serif stack — likely system-loaded via JS bundles that the crawler could not intercept — set at utilitarian weights: 600 for headlines, 400 for body, 700 for buttons. Corners stay conservative: `{rounded.sm}` on cards, `{rounded.xs}` on inputs and badges, `{rounded.none}` on the navigation bar itself, reinforcing a precision-engineered appliance identity rather than a lifestyle-soft one. Spacing is generous vertically (`{spacing.section}` between feature blocks, `{spacing.xl}` inside product grids) but compact horizontally, reflecting a layout optimized for spec-comparison shopping. The overall impression is a showroom floor rendered in HTML — clean sightlines, ample breathing room around hero product shots, and UI chrome that recedes behind the merchandise.

colors:
  primary: "#1a2b4a"
  primary-active: "#0f1d36"
  primary-disabled: "#8d95a5"
  accent: "#c8102e"
  accent-active: "#a30d24"
  accent-disabled: "#e8a0aa"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#eeeeee"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  star-rating: "#f5a623"
  success: "#2e7d32"
  warning: "#f57c00"
  error: "#d32f2f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.1px
  caption-bold:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  spec-value:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  price:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-strike:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0

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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-disabled}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.accent}"
    typography: "{typography.button-sm}"
    padding: 8px 0
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
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 2px 8px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    hoverShadow: 0 4px 16px rgba(0,0,0,0.1)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 1 / 1
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  hero-banner-cta:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    aspectRatio: 4 / 3
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline-soft}
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.ink}"
  badge-sale:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
    gap: "{spacing.xxs}"
  price-block:
    currentPrice:
      typography: "{typography.price}"
      textColor: "{colors.ink}"
    originalPrice:
      typography: "{typography.price-strike}"
      textColor: "{colors.muted}"
      textDecoration: line-through
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline}
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    opacity: 0.85
    hoverOpacity: 1
  comparison-toggle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: 1px solid {colors.primary}
  comparison-toggle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — A solid red (#c8102e) rectangle with `{rounded.xs}` corners, uppercase 14px Montserrat bold lettering in white. Hover darkens to `{colors.accent-active}`; disabled state fades to a muted rose. The red draws from Farberware's power-indicator visual language — every primary action reads like pressing a physical appliance button.

**`button-secondary`** — White fill with a 2px navy border and navy uppercase text. On hover the fill inverts to `{colors.primary}` with white text, creating a satisfying binary toggle. Used for "Compare," "Add to Wishlist," and secondary cart actions.

**`button-tertiary`** — Text-only link-style button in accent red, no background, no border. Used inline within product descriptions for "View Full Specs" or "See All Reviews" actions.

### Navigation
**`nav-bar`** — A 72px-tall white strip with a subtle bottom hairline. The Farberware wordmark sits left; category links ("Dishwashers," "Countertop Ovens," "Coffee Makers") use `{typography.nav-link}` at 600 weight. On scroll, the hairline drops away and a soft box-shadow takes over. A compact search icon and cart counter live at the right edge.

**`breadcrumb`** — Muted gray caption text with slash separators. The final segment renders in `{colors.ink}` without a link, grounding the user in the product hierarchy.

### Product Display
**`product-card`** — A white card with `{rounded.sm}` corners and a 1px `{colors.hairline-soft}` border. The top half holds a square product image on a light gray field; the bottom carries the product name in `{typography.title-sm}`, a star rating row, and a price block. Hover lifts the card with a 4px 16px shadow transition. Sale badges overlay the top-left corner of the image area.

**`price-block`** — Current price in 20px bold Montserrat; when discounted, the original price renders in 16px muted text with a line-through beside it. The visual weight difference makes savings immediately legible at scanning speed.

**`spec-table-row`** — Alternating-implicit rows (no zebra striping — the hairline-soft bottom border provides rhythm). Labels in 13px semibold, values in 13px regular. Used on PDP pages for capacity, dimensions, noise level, energy rating, and cycle count.

### Hero & Marketing
**`hero-banner`** — Full-bleed navy block (`{colors.primary}`) with centered white display text and a red CTA button. Minimum height 480px ensures the hero commands the viewport on desktop. Product photography typically bleeds from the right edge at 50% width.

**`category-tile`** — A 4:3 soft-gray rectangle with `{rounded.sm}` corners, a centered product silhouette, and a `{typography.title-sm}` label below. Used in grid layouts for top-level category navigation on the homepage.

### Utility
**`search-bar`** — A 44px-tall input on a `{colors.surface-soft}` background with `{rounded.xs}` corners. Placeholder text reads "Search dishwashers, parts & accessories" in `{colors.muted}`. Focus state swaps the border to `{colors.primary}`.

**`badge-sale`** — Compact red pill with white bold caption text ("SALE," "−20%"). Sits inside product-card image areas or beside prices on listing pages.

**`badge-new`** — Same geometry as sale badge but in navy, used for recently launched SKUs.

**`comparison-toggle`** — A small outlined chip that users click to add a product to the comparison tray. Active state fills navy with white text. Appears at the bottom-right of each product card in grid views.

### Footer
**`footer`** — Navy background matching the primary brand color, white text at 85% opacity for links, full opacity on hover. Four-column layout on desktop: Products, Support, Company, Legal. A secondary row below carries social icons and the copyright line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero banner stacks text above image; nav collapses to hamburger + logo + cart icon; spec tables scroll horizontally; footer stacks to single column; section spacing reduces to `{spacing.xl}` |
| Tablet | 744–1128px | Two-column product grid; hero maintains side-by-side layout at reduced image scale; nav shows top 4 categories with overflow in "More" dropdown; footer renders two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all categories visible; hero at full 480px height; comparison tray docks at bottom of viewport |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid holds four columns; generous `{spacing.section-lg}` between feature blocks |

### Touch Targets
- All interactive elements maintain a minimum 44×44px tap area on mobile
- Product cards expand their hit area to the full card surface
- Nav hamburger icon padded to 48×48px touch zone
- Comparison toggles enlarge to 40px height on touch devices

### Collapsing Strategy
- Product spec tables convert from two-column key-value to full-width stacked rows below 744px
- Category tiles shift from 4-up grid to horizontal scroll strip on mobile
- Hero CTA button stretches to full width on mobile, stays inline on desktop
- Footer columns collapse into expandable accordions on mobile with `{rounded.xs}` section dividers
- Search bar moves from inline nav element to full-width overlay triggered by icon tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable from the live site — the palette above is reconstructed from widely-documented Farberware brand guidelines (navy wordmark, red accent) and standard appliance-industry UI conventions. Actual implementation hex values may differ.
- No font-family stacks were detected — the site likely loads fonts via JavaScript bundles or deferred CSS. Montserrat and Open Sans are educated approximations based on the geometric-sans visual style common to appliance brands in this tier; the actual typeface may be a proprietary or licensed alternative.
- No meta theme-color or manifest data was available, suggesting the PWA/mobile-chrome integration layer could not be audited.
- Interaction motion curves (easing, duration) could not be captured — transitions above assume standard 200ms ease-in-out.
- Dark-mode tokens are not defined; the site does not appear to ship a dark theme.
- Icon system (stroke weight, grid size, asset format) could not be determined from extraction.
