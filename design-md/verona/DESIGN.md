---
version: alpha
name: "Verona"
source_url: "https://www.veronaappliances.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep-forest teal (#0c4242) poured over a near-white canvas (#f9f9f9) — that single, unexpected color pairing is what separates Verona's digital presence from the stainless-steel monotony of most appliance showrooms. The teal carries heritage weight: it reads as the enameled finish on a vintage Italian range, and the site extends this logic by pairing it with terracotta (#d8613c) accent moments and warm greige (#cfcabe) dividers that feel lifted from a Tuscan kitchen wall. Typography splits cleanly between Cardo, a high-contrast serif used for display headings and editorial moments, and Inter for all navigational and body work — the contrast between old-world serifs and a crisp geometric sans mirrors the brand's pitch of professional Italian engineering made accessible for residential kitchens. Buttons and CTAs land in `{rounded.xs}` rectangles, almost square-cornered, reinforcing the precision-appliance identity; product cards carry a gentle `{rounded.sm}` and sit on `{colors.surface-card}` white with a single `{colors.hairline}` border — no drop shadows, no gradient chrome, just enough structure to frame a range photograph. The muted sage palette (`{colors.sage}`, `{colors.meadow}`, `{colors.mint-soft}`) threads through secondary navigation, filter pills, and lifestyle-photography overlays, keeping the page atmosphere cool without going clinical. A navy accent (`{colors.navy}`) surfaces in footer links and legal-weight text, while the terracotta (`{colors.terracotta}`) fires only on promotional banners, sale badges, and the occasional hover state — used sparingly enough that each appearance reads as heat, not noise. Spacing is generous: `{spacing.section}` between page blocks, `{spacing.xl}` gutters on product grids, and a 1440px max-width container that prevents the wide, landscape-format hero images from losing their cinematic framing.

colors:
  primary: "#0c4242"
  primary-active: "#083232"
  primary-disabled: "#97aeae"
  ink: "#2f2f2f"
  body: "#444444"
  muted: "#949494"
  muted-soft: "#a4a4a4"
  hairline: "#eeeeee"
  hairline-strong: "#cfcabe"
  canvas: "#f9f9f9"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  navy: "#003366"
  sage: "#97aeae"
  meadow: "#b1c5a4"
  mint-soft: "#e7ede9"
  greige: "#cfcabe"
  warm-tan: "#c2a990"
  terracotta: "#d8613c"
  charcoal: "#43454b"
  deep-ink: "#111111"
  error: "#cc1818"
  success: "#4ab866"
  warning: "#f0b849"
  promo-red: "#cd2653"

typography:
  display-xl:
    fontFamily: "'Cardo', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cardo', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cardo', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  label-upper:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  price-display:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  spec-label:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  spec-value:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    borderWidth: 0
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
    textDecoration: underline
  button-terracotta:
    backgroundColor: "{colors.terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline-strong}"
    focusBorderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.error}"
    textColor: "{colors.ink}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline-strong}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottomWidth: 1px
    borderBottomColor: "{colors.hairline}"
    logoHeight: 40px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.08)"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.10)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    imageAspectRatio: "4:3"
    imageObjectFit: contain
    imageBackgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-subtitle:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(12,66,66,0.10)"
    borderColor: "{colors.sage}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    overlayGradient: "linear-gradient(135deg, rgba(12,66,66,0.85) 0%, rgba(12,66,66,0.4) 100%)"
  hero-lifestyle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-lg}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  category-tile:
    backgroundColor: "{colors.mint-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    height: 200px
    hoverBackgroundColor: "{colors.sage}"
    hoverTextColor: "{colors.on-primary}"
  badge-promo:
    backgroundColor: "{colors.terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-sale:
    backgroundColor: "{colors.promo-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-table:
    backgroundColor: "{colors.surface-card}"
    stripedRowColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.md} {spacing.base}"
    borderColor: "{colors.hairline}"
  color-swatch:
    rounded: "{rounded.full}"
    size: 36px
    borderWidth: 2px
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    selectedBorderWidth: 3px
  finish-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    iconColor: "{colors.muted}"
    placeholderColor: "{colors.muted-soft}"
  footer:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.sage}"
    linkHoverColor: "{colors.mint-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTopWidth: 4px
    borderTopColor: "{colors.primary}"
  footer-bottom:
    backgroundColor: "{colors.deep-ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.base} {spacing.xl}"
  newsletter-signup:
    backgroundColor: "{colors.mint-soft}"
    textColor: "{colors.primary}"
    headingTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    thumbnailSize: 72px
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorderColor: "{colors.hairline}"
    thumbnailActiveBorderColor: "{colors.primary}"
    thumbnailGap: "{spacing.sm}"
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.terracotta}"
    originalPriceTypography: "{typography.body-md}"
    originalPriceColor: "{colors.muted}"
    originalPriceTextDecoration: line-through
  toast-notification:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"

---

## Components

### Buttons

**`button-primary`** — The primary CTA is deep teal (#0c4242) with white text set in Inter 600 weight at 16px. Corners are nearly square at `{rounded.xs}` (4px), signaling the precision engineering the brand trades on. On hover, the background darkens to `{colors.primary-active}` (#083232); disabled state drops to 60% opacity with the muted sage fill. Minimum touch width is 120px to accommodate appliance-catalog labels like "View Specifications" and "Find a Dealer."

**`button-secondary`** — White fill with a 1px teal border and teal text. On hover, the entire button inverts to solid teal with white text — a clean, decisive transition rather than a gradual fade. Shares the same 48px height and `{rounded.xs}` radius as the primary, so the two sit comfortably side by side on product detail pages.

**`button-tertiary`** — A text-only link-style button with an underline, used in product comparison rows and breadcrumb-adjacent actions. No background, no border — just teal text that darkens on hover.

**`button-terracotta`** — Reserved for promotional CTAs (seasonal sale banners, limited-edition finishes). Terracotta (#d8613c) fill with white text. Appears sparingly — typically one per page at most — so it reads as urgency against the cool teal/sage palette.

### Navigation

**`nav-bar`** — A 72px-high white bar pinned to the top of the viewport. Logo at 40px height sits left; category links ("Ranges," "Cooktops," "Ovens," "Ventilation") run center in Inter 500 at 14px. A single hairline border at the bottom separates nav from content. On scroll, the bottom border drops away and a subtle 1px box-shadow replaces it. The right cluster holds search icon, dealer-locator link, and a hamburger trigger on mobile.

**`nav-dropdown`** — Category flyouts open on hover with a 4px rounded white panel and a gentle shadow. Links are grouped by product line (e.g., "36-inch Pro," "30-inch Designer") in `{typography.body-sm}` with `{spacing.lg}` padding. An optional lifestyle image fills the right third of the dropdown for key categories.

### Product Cards

**`product-card`** — White card on a `{colors.surface-soft}` image bed, 1px `{colors.hairline}` border, `{rounded.sm}` corners. Product images render at 4:3 with `object-fit: contain` so the full silhouette of a range or cooktop is always visible — no cropping. Title sits below in `{typography.title-sm}`, subtitle (fuel type, size) in `{typography.body-sm}` muted gray. On hover, the border shifts to `{colors.sage}` and a soft teal-tinted shadow lifts the card. No price is shown on the card itself; Verona drives users to the product detail page or dealer network.

### Hero Sections

**`hero-banner`** — Full-bleed photographic hero with a diagonal gradient overlay from 85% teal to 40% teal, allowing the background image (typically a styled kitchen) to breathe on the right while headline and body text sit legibly on the left in white. Minimum height 560px. Heading uses Cardo at `{typography.display-xl}` (48px, weight 700), body in Inter `{typography.body-lg}` (18px). A single CTA button sits below, usually `button-primary` in its inverted-on-dark form (white background, teal text) for contrast.

**`hero-lifestyle`** — A lighter hero variant with no overlay: the image fills one half, and the heading/body/CTA fill the opposite half on `{colors.canvas}`. Used for collection landing pages and editorial content.

### Category Tiles

**`category-tile`** — Rectangular tiles at 200px minimum height with `{colors.mint-soft}` backgrounds and centered `{typography.title-md}` text in teal. On hover, the background deepens to `{colors.sage}` and text flips to white. These anchor the homepage product grid, one tile per appliance category.

### Badges

**`badge-promo`** — Terracotta fill, white uppercase text at 11px with wide letter-spacing. Used atop product cards for "Limited Edition" or "Best Seller" labels. **`badge-new`** — Same geometry, teal fill. **`badge-sale`** — Promo-red (#cd2653) fill for clearance or seasonal promotions.

### Specification Table

**`spec-table`** — Alternating-row table with `{colors.surface-soft}` stripes. Label column in `{typography.spec-label}` (13px, 600 weight, muted color), value column in `{typography.spec-value}` (13px, 400 weight, ink color). Rows have `{spacing.md}` vertical padding. This is the workhorse component for appliance detail pages, housing dimensions, BTU ratings, electrical specs, and certifications.

### Color/Finish Selectors

**`color-swatch`** — 36px circles with 2px hairline borders. The selected swatch gains a 3px teal border. Swatches represent appliance finishes (Matte Black, Stainless, Burgundy, Antique White, etc.), so the fill color is the literal finish color.

**`finish-selector`** — A pill-row alternative for text-based finish selection (e.g., "Stainless Steel," "Matte Black"). Default state is `{colors.surface-soft}` with body-colored text; selected state inverts to teal fill with white text.

### Search

**`search-bar`** — A 44px input field with `{colors.surface-soft}` background, `{rounded.xs}` corners, and a muted search icon on the left. Placeholder text in `{colors.muted-soft}` reads "Search ranges, cooktops, ovens…" On focus, the border highlights to `{colors.primary}`.

### Image Gallery

**`image-gallery`** — Product detail image viewer with a primary image area on `{colors.surface-soft}` and a horizontal row of 72px thumbnails below. Active thumbnail gains a 2px teal border. The gallery is critical for this category — buyers need to see burner layouts, control panels, oven interiors, and finish details from multiple angles.

### Pricing

**`price-block`** — Price set in `{typography.price-display}` (Inter 700 at 24px) in ink black. Sale prices display in `{colors.terracotta}` with the original price struck through in muted gray to the right. Since Verona uses dealer networks, some pages may show "Contact Dealer for Pricing" in `{typography.body-md}` instead.

### Footer

**`footer`** — Dark charcoal (#43454b) background with a 4px teal stripe at the top edge, establishing the brand's signature color even in the page's lowest real estate. Link columns (Products, Support, About, Dealer Locator) use `{typography.title-sm}` headings and `{typography.body-sm}` link text in `{colors.sage}`, hovering to `{colors.mint-soft}`. The bottom sub-footer bar drops to `{colors.deep-ink}` (#111111) for copyright, legal, and certification logos.

### Newsletter Signup

**`newsletter-signup`** — A `{colors.mint-soft}` banner with `{rounded.sm}` corners housing a heading in `{typography.title-lg}`, a short body line, and an inline email input paired with a `button-primary`. Appears above the footer on key landing pages.

### Toast / Notification

**`toast-notification`** — A `{colors.charcoal}` pill with white text at `{typography.body-sm}`, soft shadow, and `{rounded.sm}` corners. Appears bottom-center for add-to-comparison confirmations, dealer-locator results, and form submission feedback.

### Breadcrumbs

**`breadcrumb`** — Muted gray text at `{typography.caption}` size with chevron separators. The final (active) crumb renders in `{colors.ink}`. Appears immediately below the nav bar on product and category pages.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks vertically (image top, text below); nav collapses to hamburger + slide-out drawer; spec table scrolls horizontally; category tiles stack 1-up; footer columns collapse to accordion; image gallery thumbnails become a horizontal scroll strip |
| Tablet | 744–1128px | Two-column product grid; hero remains side-by-side at reduced min-height (400px); nav shows top-level categories, dropdown triggers on tap; spec table fits without scroll; category tiles run 2-up |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with hover dropdowns; hero at full 560px height; footer columns display inline; newsletter signup sits full-width above footer |
| Wide | > 1440px | Content max-width caps at 1440px, centered; product grid may expand to four columns; hero image scales but text column widths remain capped at ~600px to preserve line length |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch area on mobile and tablet
- Color swatches expand to 44px on touch devices with increased gap spacing
- Nav drawer links have 48px row height with full-width tap targets
- Finish selector pills gain `{spacing.sm}` additional vertical padding on mobile

### Collapsing Strategy
- Navigation: top-level links collapse into a left-anchored slide-out drawer with category accordions; search moves to a full-width bar at the top of the drawer
- Product grid: from 3/4 columns to 2 (tablet) to 1 (mobile), maintaining card aspect ratios
- Footer: column layout collapses to stacked accordions with `{typography.title-sm}` headers as toggle triggers
- Spec tables: fixed first column with horizontal scroll on smaller viewports
- Hero banners: overlay gradient shifts to a solid teal background behind the text block on mobile, with the image appearing above at 16:9

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font definitively confirmed for display use; Cardo appeared in the extracted font stacks alongside system fonts, but it may be loaded conditionally via a JS-based type loader or WordPress plugin — verify against the live `@font-face` declarations before implementation
- Meta theme-color was not set, so mobile browser chrome color is unknown — recommend setting to `#0c4242` for Android/Safari consistency
- No extracted border-radius values from computed styles; the `{rounded.xs}` (4px) assignment is inferred from the angular, precision-appliance visual language rather than measured
- E-commerce pricing model is unclear — the site may route to dealer networks rather than direct checkout, which could affect whether cart, checkout, and pricing components are needed
- No dark-mode tokens were detected; the palette is light-only
- WooCommerce platform confirmed via font-stack artifacts, but cart/checkout component styling was not extractable from the hints — these likely inherit WooCommerce defaults and may need custom overrides
- Exact logo dimensions, safe-area spacing, and favicon specifications were not available in the extracted data
- Animation/transition timing values (hover durations, scroll-triggered reveals) were not captured
