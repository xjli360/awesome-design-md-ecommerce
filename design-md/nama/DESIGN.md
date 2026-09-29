---
version: alpha
name: "Nama"
source_url: "https://namawell.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Cold-press green — not sage, not mint, but the saturated #21a641 of a just-separated celery juice — is the first thing that registers on Nama's storefront, and it stays in your eye through every "Add to Cart" button, every product-tier badge, and every wellness-benefit icon. The palette fans out into an entire orchard of greens: a deep forest #28724f for secondary emphasis on comparison-table headers and educational content blocks, a bright lime #7bdb56 for freshness cues and ingredient callouts, and a muted teal #47897e that surfaces in lifestyle photography overlays and category accents. Against this chlorophyll spectrum, the canvas defaults to white with a warm cream alternative (#f8f2e9) that appears on recipe sections and lifestyle editorial panels — a deliberate warmth that keeps the appliance photography from feeling clinical. Typography pairs Circular Std (Book and Medium weights) for all UI, body, and navigation text with Rockwell Nova as a slab-serif display face for hero headlines and promotional banners; the contrast between a geometric sans and a sturdy serif gives the brand a voice that reads as both wellness-forward and mechanically confident about its cold-press engineering. Display sizes stay modest — 32–40px for heroes, 18–22px for section titles — trusting large product photography and generous `{spacing.section}` vertical rhythm over typographic muscle. Product cards sit in `{rounded.md}` containers with soft shadows, and primary CTA buttons use `{rounded.full}` pill shapes that echo the rounded housings of the J2 and C2 juicer lines. A coral accent (#f06652) handles sale badges and urgency signals, while a sky blue (#00b3ff) marks informational tooltips and comparison highlights. The overall grid maxes at 1440px, with comparison tables — the core conversion tool for a brand selling three juicer tiers — using `{colors.hairline}` borders and alternating `{colors.surface-soft}` rows to make spec differences scannable at a glance.

colors:
  primary: "#21a641"
  primary-active: "#1b8735"
  primary-disabled: "#abaeab"
  ink: "#3a3a3a"
  body: "#4a5464"
  muted: "#75787b"
  muted-soft: "#999998"
  hairline: "#d0d3d4"
  hairline-soft: "#dcdfe5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-warm: "#f8f2e9"
  surface-cool: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-green-deep: "#28724f"
  accent-lime: "#7bdb56"
  accent-teal: "#47897e"
  accent-coral: "#f06652"
  accent-blue: "#00b3ff"
  accent-pink: "#dd497a"
  accent-raspberry: "#bf3f67"
  accent-dusty-rose: "#cc7e80"
  accent-steel: "#5d8da4"
  star-rating: "#21a641"
  success: "#21a641"
  error: "#f06652"
  warning: "#f06652"
  scrim: "#23282f"
  footer-bg: "#23282f"
  footer-text: "#d0d3d4"

typography:
  display-xl:
    fontFamily: "'Rockwell Nova', 'rockwell-nova', Georgia, serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Rockwell Nova', 'rockwell-nova', Georgia, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Rockwell Nova', 'rockwell-nova', Georgia, serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Rockwell Nova', 'rockwell-nova', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Circular Std', 'CircularStd-Medium', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Circular Std', 'CircularStd-Medium', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Circular Std', 'CircularStd-Book', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Circular Std', 'CircularStd-Book', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Circular Std', 'CircularStd-Book', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Circular Std', 'CircularStd-Book', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Circular Std', 'CircularStd-Medium', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Circular Std', 'CircularStd-Medium', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Circular Std', 'CircularStd-Medium', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Circular Std', 'CircularStd-Medium', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.31
    letterSpacing: 0.2px
  link:
    fontFamily: "'Circular Std', 'CircularStd-Book', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Circular Std', 'CircularStd-Medium', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  price-display:
    fontFamily: "'Circular Std', 'CircularStd-Medium', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  price-sm:
    fontFamily: "'Circular Std', 'CircularStd-Medium', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  slab-accent:
    fontFamily: "'Rockwell Nova', 'rockwell-nova', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-green-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
    border: "2px solid {colors.primary}"
  button-green-outline-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 24px
    height: 48px
  button-pill-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    border: "1px solid {colors.hairline}"
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
    border: "1px solid {colors.error}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  search-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-logo:
    height: 28px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.accent-green-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
    backgroundColor: "{colors.surface-cool}"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.price-sm}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    typography: "{typography.badge}"
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
    position: "absolute top-{spacing.sm} left-{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 480px
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 560px
  hero-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.25
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
  comparison-table-header:
    backgroundColor: "{colors.accent-green-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  comparison-table-row:
    padding: "{spacing.md} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  comparison-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
  comparison-table-highlight:
    backgroundColor: "{colors.surface-warm}"
    border: "2px solid {colors.primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-bestseller:
    backgroundColor: "{colors.accent-green-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
    border: "1px solid {colors.hairline}"
  recipe-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  recipe-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4:3"
  recipe-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  recipe-card-meta:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  sticky-atc-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    height: 72px
    padding: "{spacing.md} {spacing.lg}"
    borderTop: "1px solid {colors.hairline-soft}"
    boxShadow: "0 -2px 8px rgba(0,0,0,0.06)"
  sticky-atc-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  review-summary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  review-stars:
    textColor: "{colors.star-rating}"
    fontSize: 16px
  review-stars-empty:
    textColor: "{colors.hairline}"
  newsletter-section:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "10px 24px"
    height: 44px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.base} {spacing.lg} {spacing.base}"
  benefit-icon-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    textAlign: center
  benefit-icon:
    textColor: "{colors.primary}"
    fontSize: 40px
    marginBottom: "{spacing.md}"
  benefit-icon-title:
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.xs}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 44px
    width: 44px
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"

## Components

### Buttons
**`button-primary`** — The main conversion driver across the site, used for "Add to Cart", "Shop Now", and "Buy the J2" actions. It uses the brand's signature green (`{colors.primary}`, #21a641) with white text and a fully rounded pill shape (`{rounded.full}`) that mirrors the curved housings of Nama's juicer line. On hover/active, it darkens to `{colors.primary-active}` (#1b8735). When disabled, it desaturates to `{colors.primary-disabled}` (#abaeab), losing the green entirely.

**`button-secondary`** — An outlined pill for secondary actions like "Learn More", "Compare Models", or "View Recipes". It holds a white background with a 2px hairline border and dark text (`{colors.ink}`). On hover, the border shifts to `{colors.ink}` and the background moves to `{colors.surface-soft}`, giving a subtle filled effect without competing with the green primary.

**`button-green-outline`** — A green-bordered variant used for mid-priority actions where the primary green should register but a solid fill would be too dominant — "See All Recipes", "Download Guide", or "Watch Video". On hover, it inverts to a solid green fill with white text, creating a satisfying state transition.

**`button-ghost`** — A text-only button with no background or border, reserved for tertiary actions like "Cancel", "Skip", or inline text links that need button-level tap targets. It matches primary button padding for alignment in button groups.

**`button-pill-sm`** — A compact pill used for filter tags, quick-select options on the product page (color variants, bundle sizes), and promotional micro-CTAs. Uses `{typography.button-sm}` at 13px.

**`button-pill-outline`** — The outlined companion to `button-pill-sm`, used for unselected filter states and category tags on recipe and blog pages. A 1px hairline border keeps it subtle until selected.

### Cards
**`product-card`** — The primary product display on collection and search pages. White background with a subtle box shadow and 12px rounded corners (`{rounded.md}`). The image area fills the top half with a 1:1 aspect ratio and a light cool-gray fallback (`{colors.surface-cool}`) for loading states. Title, price, and optional badge stack below with `{spacing.base}` padding. Product badges (New, Best Seller) are absolutely positioned in the top-left corner of the image area.

**`recipe-card`** — A warm-toned card (`{colors.surface-warm}`, #f8f2e9) used in the recipe carousel and recipe index pages. It uses a 4:3 image aspect ratio to showcase food photography, with the recipe title in `{typography.title-md}` and meta info (prep time, difficulty) in `{typography.caption}` below. The warm background distinguishes recipe content from product content at a glance.

**`benefit-icon-card`** — A centered, icon-led card used in feature grids that communicate juicer benefits (slow-press technology, quiet motor, easy cleanup). The icon renders at 40px in `{colors.primary}` green, followed by a bold title and body-small description. These typically appear in 3- or 4-column grids.

### Navigation
**`nav-bar`** — A sticky top navigation at 72px height with a white background and a subtle bottom border in `{colors.hairline-soft}`. The Nama wordmark sits left at 28px height. Navigation links use `{typography.nav-link}` at 15px/500 weight. Active links gain `{colors.primary}` green text with a 2px bottom border. Hover states transition text to green. The bar includes a search icon, account icon, and cart indicator on the right.

**`announcement-bar`** — A narrow 40px bar above the nav using `{colors.accent-green-deep}` (#28724f) as background with white text in `{typography.caption}`. Used for shipping thresholds ("Free shipping on orders $100+"), promotional codes, and seasonal sale callouts. It auto-rotates messages on a timer.

### Product Page
**`comparison-table`** — The primary decision-making component for a brand that sells three juicer tiers (J2, C2, Vitality). Wrapped in `{rounded.md}` with a 1px hairline border. Headers use the deep green (`{colors.accent-green-deep}`) with white text. Rows alternate between white and `{colors.surface-soft}` for scannability. The recommended model column gets a warm highlight (`{colors.surface-warm}`) with a 2px primary green border to draw the eye.

**`sticky-atc-bar`** — A bottom-anchored bar that appears on scroll past the main Add to Cart section. It shows product name, price, and a pill-shaped green CTA button. A top border and upward box shadow separate it from page content. Height is 72px with internal padding that keeps the button vertically centered.

**`quantity-selector`** — A compact input group for adjusting product quantities, with a central numeric display flanked by minus/plus buttons. Each button is 44×44px for comfortable tapping. The container uses `{rounded.sm}` and a 1px hairline border.

### Badges
**`badge-new`** — A small fully rounded badge in `{colors.primary}` green for new product launches and recently added accessories. Uses uppercase `{typography.badge}` at 11px with 0.5px letter spacing.

**`badge-sale`** — A coral badge (`{colors.accent-coral}`, #f06652) for discount and sale indicators. Same dimensions and typography as `badge-new` but the warm color creates urgency contrast against the green palette.

**`badge-bestseller`** — A deep green badge (`{colors.accent-green-deep}`) for top-selling items. The darker green differentiates it from the primary-green "New" badge while staying within the brand's green family.

**`badge-outline`** — A subtle outlined badge for secondary metadata like "BPA-Free", "Easy Clean", or capacity indicators. Uses muted text and a 1px hairline border on a transparent background.

### Social Proof
**`review-summary`** — A soft-gray container (`{colors.surface-soft}`) with `{rounded.md}` corners housing the aggregate rating, star distribution bar chart, and total review count. Stars render in `{colors.star-rating}` (the brand green) rather than the typical gold, reinforcing brand identity throughout the trust-building section.

### Newsletter & Footer
**`newsletter-section`** — A full-width section with the warm cream background (`{colors.surface-warm}`) used for email capture. The input and button pair both use `{rounded.full}` pill shapes, often arranged inline on desktop and stacked on mobile. Headline typically uses `{typography.display-sm}` in Rockwell Nova for editorial contrast.

**`footer`** — A dark footer using `{colors.footer-bg}` (#23282f) with muted light text (`{colors.footer-text}`). Links use `{colors.muted-soft}` and brighten to white on hover. Organized in 4-column grids (Shop, Support, Company, Social) on desktop, collapsing to accordions on mobile. The Nama wordmark appears in white at the top of the footer block.

### Utility Components
**`accordion-header`** — Used for FAQ sections and mobile navigation drawers. White background with a bottom hairline border and `{typography.title-sm}` text. The expand/collapse chevron icon sits right-aligned.

**`modal-overlay`** — A dark scrim (`{colors.scrim}` at 50% opacity) behind modals for size guides, quick-view, and video players. The modal content container uses `{rounded.md}` with `{spacing.lg}` padding.

**`tooltip`** — Small, dark tooltips (`{colors.ink}` background, white text) for spec explanations in comparison tables and feature callouts. Uses `{typography.caption}` with `{rounded.sm}` corners.

**`progress-bar`** — A thin 4px bar with fully rounded ends, used for free-shipping threshold indicators in the cart. The track is `{colors.hairline-soft}` and the fill is `{colors.primary}` green.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger with full-screen drawer; product cards in 1-column grid; hero banners reduce to 320px min-height with stacked text below image; comparison table scrolls horizontally with sticky first column; sticky ATC bar always visible; recipe cards in horizontal scroll carousel; footer columns collapse to accordion sections |
| Tablet | 744–1128px | Two-column product grid; nav shows abbreviated links with "More" dropdown; hero banners at 400px min-height with side-by-side text/image; comparison table fits 3 columns without scroll; recipe cards in 2-column grid; footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav visible with mega-dropdown for product categories; hero banners at 480px min-height; comparison table at full width; persistent sidebar filters on collection pages; recipe cards in 3-column grid; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px with centered layout; four-column product grid on collection pages; additional whitespace on sides; hero banner can extend to 560px; larger product imagery |

### Touch Targets
- All interactive elements maintain minimum 44×44px touch target size
- Pill buttons have minimum 44px height via padding even when text is smaller
- Product card tap targets extend to full card area
- Quantity selector buttons are 44×44px
- Announcement bar links have 40px tap height
- Accordion headers are 48px tall for comfortable tapping
- Comparison table cells have minimum 44px row height on mobile

### Collapsing Strategy
- Top navigation collapses to hamburger below 744px, opening a full-screen drawer with stacked links and nested accordions for product categories
- Product filters collapse to a sticky "Filter & Sort" button that opens a bottom sheet on mobile
- Comparison table switches to horizontal scroll with a sticky first column below 744px; a "Swipe to compare" hint appears on first visit
- Footer columns collapse to accordion sections on mobile
- Benefit icon grids move from 4-column to 2-column at tablet, then 1-column on mobile
- Recipe carousel uses horizontal scroll with peek on mobile, grid layout on tablet+
- Newsletter input and button stack vertically on mobile, sit inline on tablet+
- Hero banner content moves from side-by-side to stacked (image on top, text below) on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact transition durations and easing curves for button hover states and page transitions
- Focus ring styles and keyboard navigation outlines not extracted
- Loading/skeleton screen designs for product cards and comparison tables
- Empty state designs for search results, cart, and wishlist
- Dark mode color palette (not present on current site)
- Mega menu dropdown structure and animation behavior for desktop nav
- Mobile bottom navigation bar presence or absence not confirmed
- Specific image optimization breakpoints and responsive image sizes
- Video player component styling for product demo videos
- Color-swatch selector styling on product pages (if applicable to juicer color variants)
- Cookie consent banner and promotional popup modal styling
- Accessibility contrast ratios for green-on-white combinations (primary #21a641 on white may need verification)
- Social media icon set and specific platform colors used in footer
- Animation behavior for the announcement bar message rotation
- Cart drawer/slideout panel styling vs. dedicated cart page
- Breadcrumb component styling
- Pagination or infinite scroll behavior on collection pages
- Exact Rockwell Nova weight availability (extracted as font stack, specific loaded weights unconfirmed)
