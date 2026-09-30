---
version: alpha
name: "Manduka"
source_url: "https://www.manduka.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, quiet studio presence built on a near-black ink (#141414) and a single shot of deep teal (#011f31) that reads like the color of a yoga mat after a hot class — dark, calm, and slightly wet. The brand's primary accent is a muted gold (#8e8733), not a bright CTA color, used sparingly on sale badges and small highlights; it feels like a brass gong rather than a digital button. The canvas is a warm off-white (#f6f6f6) that avoids the sterile hospital white of most DTC sites, and the entire layout breathes through generous whitespace and a restrained typographic system built on Assistant and Inter at modest weights. Product cards use soft rounded corners (`{rounded.sm}` ~8px) and thin hairlines (#dedede) that suggest a premium mat unrolled on a clean floor. There are no hard edges, no aggressive CTAs, no urgency — the site trusts the product photography (yogis in deep poses, mat textures, studio light) to do the selling. The nav bar is a thin, fixed strip with the logo centered, category links in lowercase, and a small cart icon; the search icon is a simple line glyph, not a pill. The footer runs dark (#141414) with gold links, a newsletter signup, and a sustainability badge. The overall mood is "the studio before class starts" — hushed, intentional, and built for longevity.

colors:
  primary: "#011f31"
  primary-active: "#0a2e42"
  primary-disabled: "#7a8d99"
  accent-gold: "#8e8733"
  accent-gold-hover: "#a69e3d"
  ink: "#141414"
  body: "#545454"
  muted: "#a1a1a1"
  muted-soft: "#e2e2e2"
  hairline: "#dedede"
  hairline-soft: "#f3f3f3"
  canvas: "#f6f6f6"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  on-gold: "#141414"
  footer-bg: "#141414"
  footer-text: "#a1a1a1"
  footer-link: "#8e8733"
  badge-sale: "#8e8733"
  badge-new: "#011f31"
  star-rating: "#8e8733"
  error: "#c13515"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  footer-link:
    fontFamily: "'Assistant', 'Inter', arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
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
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-gold-hover:
    backgroundColor: "{colors.accent-gold-hover}"
    textColor: "{colors.on-gold}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-text-gold:
    backgroundColor: transparent
    textColor: "{colors.accent-gold}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: 2px solid "{colors.primary}"
  nav-link-inactive:
    color: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: 1/1
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-sale-price:
    color: "{colors.accent-gold}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: 1px solid "{colors.hairline}"
  search-icon:
    color: "{colors.muted}"
    size: 20px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.footer-link}"
    typography: "{typography.footer-link}"
  newsletter-input:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: 1px solid "{colors.footer-text}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    maxWidth: 500px
  collection-grid:
    gap: "{spacing.base}"
    padding: "{spacing.section} {spacing.lg}"
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid "{colors.hairline-soft}"
  review-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: 1px solid "{colors.hairline}"
  accordion:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: 1px solid "{colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and "Subscribe". Rendered in deep teal (#011f31) with white text and soft 8px corners. On hover, shifts to a slightly lighter teal (#0a2e42). Disabled state uses a muted gray-blue (#7a8d99) to signal inactivity without visual noise.
**`button-secondary`** — An outlined or ghost variant used for "Learn More" and secondary actions on product pages. Uses the warm canvas background (#f6f6f6) with dark ink text (#141414) and a thin hairline border. Active state fills with the softest gray (#f3f3f3).
**`button-gold`** — Reserved for sale events, limited drops, and promotional banners. Uses the muted gold accent (#8e8733) with dark text (#141414). Hover brightens to (#a69e3d). Never used as a primary CTA — it's a signal of value, not urgency.
**`button-text`** — A text-only link styled as a button, used for "View Details" and "Read Reviews". No background, no border — just the ink color and the button typography weight. A gold variant (`button-text-gold`) exists for footer and dark-background contexts.

### Navigation
**`nav-bar`** — A fixed 64px strip with white background (#f6f6f6) and a thin bottom border (#f3f3f3). The Manduka logo sits centered; category links (Mats, Props, Apparel, etc.) are rendered in uppercase 14px weight-500 type. Active nav links get a 2px teal underline. The cart icon is a simple line drawing, and the search icon sits to the right — both in muted gray (#a1a1a1). On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Cards
**`product-card`** — A clean, minimal card with a 1:1 product image (soft top corners at 8px) and text below. The title uses 16px weight-600, the price is 16px weight-400 in body gray (#545454). Sale prices switch to gold (#8e8733). No badge by default — sale and new badges (`badge-sale`, `badge-new`) are applied as overlays on the image. Cards have no border; they rely on the white surface against the warm canvas background for separation.
**`review-card`** — A bordered card (1px #f3f3f3) with 8px corners, used in product review sections. Contains a star rating in gold (#8e8733), the reviewer name, and a short body-sm excerpt. Padding is 16px all around.

### Forms
**`text-input`** — Standard input field with 8px corners, 48px height, and a thin hairline border (#dedede). Focus state swaps the border to teal (#011f31). Error state uses a warm red (#c13515). Used for search, newsletter signup, and checkout forms.
**`newsletter-input`** — A footer-specific input on the dark background (#141414). Border is the muted footer text (#a1a1a1). The placeholder text is also muted. The submit button is the gold variant.
**`quantity-selector`** — A compact 40px input with +/- buttons, used on product detail pages for cart quantity. Same styling as text-input but narrower padding.

### Badges
**`badge-sale`** — A small uppercase label in gold (#8e8733) with dark text (#141414). 2px horizontal padding, 2px vertical. Used as a corner overlay on product images.
**`badge-new`** — Same shape and size as sale badge, but in teal (#011f31) with white text. Used for new arrivals and limited collections.

### Footer
**`footer`** — A full-width dark section (#141414) with three columns: customer service links, about links, and a newsletter signup. Text is muted gray (#a1a1a1) at 14px. Links use gold (#8e8733) on hover. The newsletter input matches the footer's dark theme. A thin gold line separates the link columns from the copyright row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes 1 column; hero text centers; footer stacks vertically |
| Tablet | 744–1128px | Nav shows 4-5 categories; product grid 2 columns; hero text left-aligned; footer 2 columns |
| Desktop | 1128–1440px | Full nav with all categories; product grid 3 columns; hero has full-width image; footer 3 columns |
| Wide | > 1440px | Max-width container (1440px) centered; product grid 4 columns; larger hero typography |

### Touch Targets
- All buttons and links: minimum 44x44px touch target
- Nav links: 48px tap area (64px nav bar height ensures this)
- Quantity selector +/- buttons: 40x40px minimum
- Product card tap target: entire card is clickable
- Accordion headers: 48px minimum tap height

### Collapsing Strategy
- Nav bar: categories collapse into hamburger menu below 744px
- Footer: 3-column layout collapses to 2 columns at tablet, 1 column at mobile
- Product grid: 4 columns on wide → 3 on desktop → 2 on tablet → 1 on mobile
- Hero section: full-width image on desktop becomes stacked (image above text) on mobile
- Accordion: all product detail accordions start collapsed on mobile; first accordion open on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors include several grays and one distinctive gold (#8e8733) and teal (#011f31) — these are likely the true brand colors, but the extraction may have missed secondary accents (e.g., a specific green for sustainability messaging, or a warm tone for "studio" photography backgrounds). The gold appears only in sale badges and small highlights; its full usage (e.g., hover states, loading spinners) is inferred.
- Font-family declarations found: Assistant, Inter, arial, europa — "europa" may be a legacy or fallback font; the primary system appears to be Assistant for headings and Inter for body. Exact font-weight mapping (e.g., 600 vs 700 for display) is inferred from common DTC patterns and may differ on the live site.
- No meta theme-color was extracted; the brand may use a browser chrome color that wasn't captured.
- Hover states for text inputs, accordion headers, and footer links are inferred from common patterns — not extracted.
- Error styling (input validation, form errors, toast messages) is not present in extracted data; colors for error/success are estimated from industry standards.
- Dark mode: not detected on the live site; the brand may not support it.
- Sub-brand or collection-specific palettes (e.g., "PRO" series mats, "eKO" sustainable line) may use distinct accent colors not captured in the top hex extraction.
- Star rating color (#8e8733) is inferred from the gold accent; the actual rating component may use a different gold or a filled/empty star pattern not captured.
- The extracted hex list includes #0f3d81 (a blue) which may be a Shopify widget or social icon color — not used in the brand palette.
