---
version: alpha
name: "Kerf"
source_url: "https://www.kerfcase.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The first thing a visitor registers on kerfcase.com is absence — no gradient hero, no overlapping type lockup, no badge confetti. A single burnt-sienna mark (#B5452D), the exact red-oxide tone of freshly planed padauk heartwood, anchors the logotype at the top of an otherwise achromatic page and then steps back so that full-bleed walnut grain and cherry figure can flood the viewport unchallenged. The white canvas ({colors.canvas}) runs unbroken from a slim sticky nav through the product grid to a hard transition into a near-black footer ({colors.footer-bg}), producing the visual equivalent of clean joinery — two flat planes meeting at a precise line. Typography leans on the operating system's native sans-serif stack, arriving crisp at every weight without a custom webfont download; headlines land at weight 700 with negative tracking but never exceed 40 px, trusting generous whitespace rather than scale to command attention. Navigation labels carry light letter-spacing ({typography.nav-link}) that reads as engineered calm — appropriate for a brand named after the exact width of material a saw blade removes, measured in thousandths of an inch. Corner radii stay near zero: `{rounded.xs}` (2 px) on buttons and inputs, `{rounded.none}` on product cards, reinforcing the straight-edge workshop aesthetic. The single exception is the wood-species swatch, a `{rounded.full}` circle that previews each timber's natural color on the product detail page. Product imagery dominates every layout — cards show a 1:1 square crop, hero banners stretch to at least 560 px, and the collection grid leaves no decorative filler between frames. The palette is intentionally binary: deep ink (#1A1A1A) for text and primary buttons, white for everything behind them, with #B5452D reserved as a sparing signature on the logotype and the occasional sale tag. Feature cards separate on a warm off-white surface ({colors.surface-soft}, #F7F5F3) without introducing a competing hue. The result reads less like a tech-accessory store and more like a furniture maker's portfolio — serious about material, indifferent to trend.

colors:
  primary: "#B5452D"
  primary-active: "#963A24"
  primary-disabled: "#DBBAB2"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#757575"
  muted-soft: "#9E9E9E"
  hairline: "#E0E0E0"
  hairline-soft: "#ECECEC"
  canvas: "#FFFFFF"
  surface-soft: "#F7F5F3"
  surface-card: "#FFFFFF"
  surface-warm: "#F0EDE8"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  footer-bg: "#1A1A1A"
  footer-text: "#B0B0B0"
  wood-walnut: "#5C4033"
  wood-cherry: "#8B4513"
  wood-maple: "#C4A35A"
  wood-mahogany: "#4E2B1B"
  wood-padauk: "#B5452D"
  success: "#3A7D44"
  sale: "#B5452D"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  label-upper:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  price-lg:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  micro:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.ink}
  button-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: 1px solid {colors.hairline}
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: 1 / 1
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0 {spacing.xs} 0"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  wood-species-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: 2px solid {colors.hairline}
    borderSelected: 2px solid {colors.ink}
  wood-species-swatch-walnut:
    backgroundColor: "{colors.wood-walnut}"
    rounded: "{rounded.full}"
  wood-species-swatch-cherry:
    backgroundColor: "{colors.wood-cherry}"
    rounded: "{rounded.full}"
  wood-species-swatch-maple:
    backgroundColor: "{colors.wood-maple}"
    rounded: "{rounded.full}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  feature-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  feature-card-icon:
    height: 40px
    width: 40px
    textColor: "{colors.primary}"
  feature-card-body:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 40px
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
  breadcrumb-current:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: 1px solid {colors.hairline}
    padding: "{spacing.base} 0"
  accordion-body:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "0 0 {spacing.base} 0"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price-lg}"
  price-from-label:
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sustainability-badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  newsletter-input:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: 1px solid {colors.footer-text}
    focusBorder: 1px solid {colors.on-dark}
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  payment-icons:
    height: 24px
    textColor: "{colors.footer-text}"

## Components

### Buttons
**`button-primary`** — A near-black (`#1A1A1A`) rectangle with sharp `{rounded.xs}` (2 px) corners, used for "Add to Cart," "Shop Now," and all primary commerce actions. Text is set in `{typography.button-md}` (15 px, weight 600, 0.3 px letter-spacing) — not uppercase, maintaining the understated workshop register. On hover, the fill lightens to `{colors.body}` (#3D3D3D); disabled state drops to `{colors.hairline}` with `{colors.muted}` text, visually receding without disappearing.

**`button-secondary`** — A white-fill outlined variant with a 1 px `{colors.ink}` border and matching ink text. Used for "View Details," secondary navigation CTAs, and the wood-species filter resets. On hover, the background tints to `{colors.surface-soft}` (#F7F5F3), adding warmth without changing the border. Padding is inset 1 px from primary (13 px 27 px) to maintain optical alignment when the two sit side by side.

**`button-accent`** — The only button that carries the brand's burnt-sienna (#B5452D). Reserved for high-emphasis moments: featured collection CTAs, promotional banners, and the "Customize Your Case" entry point on the Kerf Select page. On hover it deepens to `{colors.primary-active}` (#963A24). Used sparingly — most pages contain zero instances.

### Navigation
**`nav-bar`** — A fixed white bar at 64 px height with a 1 px `{colors.hairline}` bottom border. Logo sits left-aligned; center holds the primary links (Slim, Solid, Select, Our Story) in `{typography.nav-link}` (14 px, weight 500, 0.5 px tracking); right side carries account and cart icons. The bar has no background tint, no shadow — it separates from the hero purely through the hairline and the whitespace above the first content block.

**`mega-menu`** — A full-width dropdown triggered by hovering "Solid" or similar category links. White background with a top hairline border, containing sub-links organized by phone model (iPhone, Galaxy, Pixel) in `{typography.body-sm}`. Padding uses `{spacing.lg}` vertically and `{spacing.xl}` horizontally for generous breathing room between columns.

### Cards
**`product-card`** — A borderless, shadowless card with `{rounded.none}` corners sitting directly on the white canvas. The 1:1 square image fills the top edge to edge — no inset padding, no rounded corners on the image. Below the image, the title appears in `{typography.title-sm}` (16 px, weight 600) with `{spacing.md}` top margin. Price follows in `{typography.body-md}` with `{colors.body}` text. Cards in the collection grid carry no hover elevation; the product image may crossfade to an alternate angle on hover.

**`feature-card`** — A `{colors.surface-soft}` (#F7F5F3) block with `{rounded.sm}` (4 px) corners used to present product attributes: FlexResin bumper protection, clickable metal buttons, integrated MagSafe, and the KerfCare lifetime warranty. Each card holds a 40 px icon tinted in `{colors.primary}`, a `{typography.title-sm}` heading, and a `{typography.body-sm}` description in `{colors.body}`. Padding is `{spacing.lg}` (24 px) on all sides.

### Wood Species Selector
**`wood-species-swatch`** — A 32 px circle (`{rounded.full}`) filled with a representative color for each timber species. Default border is 2 px `{colors.hairline}`; selected state switches to 2 px `{colors.ink}`, creating a definitive ring without adding a checkmark or overlay. The swatch row appears on every product detail page, sitting between the title and the Add to Cart button. Species include walnut (#5C4033), cherry (#8B4513), maple (#C4A35A), mahogany (#4E2B1B), padauk (#B5452D), and others. Selecting a swatch updates the product image to show the corresponding wood grain.

### Hero
**`hero-banner`** — A full-width section with a minimum height of 560 px, typically backed by a close-up wood-grain photograph or a lifestyle shot of a case on a workbench. Text overlay uses `{typography.display-xl}` (40 px, weight 700, −0.5 px tracking) for the headline and `{typography.body-md}` for a one-line subtitle. The hero carries no scrim or gradient over the image — text is positioned over a naturally light or dark region of the photograph, relying on art direction rather than code to ensure contrast.

### Accordion
**`accordion`** — Used on the product detail page for Shipping, Warranty, and Returns information. Each row has a `{typography.title-sm}` label with `{colors.ink}` text and a 1 px `{colors.hairline}` bottom border. Expanded state reveals `{typography.body-sm}` content in `{colors.body}`. Padding is `{spacing.base}` (16 px) top and bottom, zero horizontal. The chevron icon rotates 180 degrees on open, with no animation on the content reveal.

### Badges
**`sale-badge`** — A compact `{colors.sale}` (#B5452D) rectangle with `{rounded.xs}` corners and white uppercase text (`{typography.badge}`: 11 px, weight 700, 0.5 px tracking). Positioned over the product card image top-left. The badge shares its color with the brand primary, keeping the page within its two-color system even during promotions.

**`sustainability-badge`** — A green (#3A7D44) variant used on the sustainability page to tag certifications: FSC Certified, Carbon Free Shipping, No Plastic Packaging. Same typography and sizing as the sale badge, swapping `{colors.sale}` for `{colors.success}`.

### Announcement Bar
**`announcement-bar`** — A 40 px tall strip pinned above the nav bar with a `{colors.ink}` background and `{colors.on-dark}` text in `{typography.caption}`. Typically carries a single message: free shipping threshold, production lead time ("Handmade — ships in 2-3 days"), or a seasonal promotion. No close button — the bar is persistent.

### Footer
**`footer`** — A `{colors.footer-bg}` (#1A1A1A) block with `{spacing.section}` (64 px) vertical padding. Organized into columns: Shop (by phone model), Company (About, Sustainability, Reviews), and Support (FAQ, Returns, Contact). Column headings use `{typography.title-sm}` in `{colors.on-dark}`; links use `{typography.link}` in `{colors.footer-text}` (#B0B0B0) with underline on hover. A newsletter email input sits at the bottom with a 1 px `{colors.footer-text}` border and transparent fill. Payment icons (Visa, Mastercard, PayPal, Apple Pay, Shop Pay, Amazon) render at 24 px height in `{colors.footer-text}`.

### Forms
**`text-input`** — A 48 px tall input with `{rounded.xs}` corners, 1 px `{colors.hairline}` border, and `{typography.body-md}` text. Focus state replaces the border with `{colors.ink}`, producing a definitive black outline. Placeholder text uses `{colors.muted}`. Used for the quantity field, newsletter signup, and the country/region selector on the cart page.

**`newsletter-input`** — A variant of text-input designed for the dark footer context: transparent background, `{colors.on-dark}` text, 1 px `{colors.footer-text}` border. Focus state brightens the border to `{colors.on-dark}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Nav collapses to hamburger with slide-out drawer. Hero banner reduces to 360 px min-height with smaller `{typography.display-md}` headlines. Wood-species swatches shrink to 28 px. Footer stacks into a single column with collapsible section headings. Announcement bar text may truncate. |
| Tablet | 744–1128px | Two-column product grid. Nav retains logo and hamburger but adds cart icon. Hero banner runs full width at 480 px min-height. Feature cards shift to a 2×2 grid. Footer shows 2–3 columns. Mega-menu becomes a stacked accordion inside the mobile drawer. |
| Desktop | 1128–1440px | Three- to four-column product grid. Full horizontal nav with all links visible and mega-menu dropdowns on hover. Hero banner at full 560 px. Feature cards in a 4-up row. Footer in 4 columns. Accordion sections on PDP may default to first panel open. |
| Wide | > 1440px | Content max-width caps at 1440 px, centered with auto margins. Four-column product grid. Hero imagery may extend beyond content max-width as a full-bleed background. All other components remain unchanged from Desktop. |

### Touch Targets
- All buttons meet a 48 px minimum height with internal padding ensuring the tap area covers at least 44×44 px.
- Nav icons (account, cart, hamburger) render at 24 px with a 44 px tap area via padding.
- Wood-species swatches are 32 px circles with 8 px gaps, meeting minimum tap target with spacing.
- Product cards are entirely tappable — the full card surface is a link.
- Accordion rows have `{spacing.base}` (16 px) vertical padding, yielding a ~48 px touch strip.

### Collapsing Strategy
- On mobile (< 744 px), the nav collapses to a hamburger icon that opens a full-height slide-out drawer with stacked links.
- The mega-menu becomes nested accordions inside the mobile drawer, grouped by phone model.
- The product grid collapses from 4 columns to 1 column, with images remaining at 1:1 aspect ratio.
- Feature cards stack vertically in a single column.
- The footer collapses from 4 columns to a single stack with headings as accordion triggers.
- The wood-species swatch row scrolls horizontally if more than 5 species are available on a narrow viewport.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were returned by the automated extraction pipeline (0 colors). The brand primary `#B5452D` was identified via AI-assisted page fetch as the logotype accent; all other palette values (ink, body, muted, hairline, surface, footer tones) are inferred from observed page structure and common ecommerce patterns rather than extracted CSS custom properties.
- No font-family stacks were returned by extraction. The site appears to rely on system sans-serif fonts loaded via Shopify's theme engine or CSS `system-ui` fallback. The exact webfont (if any) could not be confirmed without JavaScript execution or DevTools inspection.
- The platform detection flagged `platform-shopify: False`, but multiple web sources confirm the site is hosted on Shopify. The extraction may have been blocked by anti-bot measures or SSL certificate issues.
- Button hover transitions (duration, easing), focus ring styles, and exact disabled-state opacities are not extracted — values here follow common Shopify theme conventions.
- The wood-species swatch colors (`wood-walnut`, `wood-cherry`, `wood-maple`, `wood-mahogany`, `wood-padauk`) are representative approximations of each timber's heartwood tone, not extracted from the site's CSS or swatch image pixels.
- Error states (form validation, out-of-stock messaging, empty cart) are not present in extracted data.
- Dark mode is not supported — the site uses a white canvas with a dark footer consistently.
- Product image hover behavior (crossfade to alternate angle vs. zoom) could not be confirmed without JavaScript execution.
- Exact breakpoint values are inferred from common Shopify theme conventions — the site may use slightly different viewport widths.
- The mega-menu structure (sub-links by phone model) is inferred from the navigation labels observed (Slim, Solid, Select) and product collection structure.
