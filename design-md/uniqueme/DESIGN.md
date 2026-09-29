---
version: alpha
name: "UniqueMe"
source_url: "https://www.uniqueme.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The name is the first design decision — "UniqueMe" presses the possessive first person directly against the promise of distinction, and every surface in the interface exists to honor that contract. Phone cases and screen protectors are commodity objects; UniqueMe's design language works to de-commodify them by leaning into personalization cues: individual product cards framed like portraits, category filters styled as identity chips rather than flat tabs, and a primary violet that reads as creative rather than corporate. Without live color or font extraction (the site appears to load tokens via client-side JavaScript, defeating static analysis), the palette below is reconstructed from brand positioning rather than measured pixels — a vibrant #7b2ff7 anchors CTAs and active states, pulling away from the navy-and-orange patterns saturating the accessories category. Canvas stays pure white (#ffffff), and a whisper of lavender bleeds into soft surfaces (#f6f3ff) so even background planes carry a faint brand signature. Typography follows a modern geometric sans approach — high x-height, generous letter-spacing on labels — suited to product names that often run long (model-specific strings like "iPhone 15 Pro Max compatible" demand compression without loss of legibility). Rounded corners are deliberately friendly: `{rounded.lg}` on product cards, `{rounded.full}` on pill filters and the search bar. The category — Cell Phones & Accessories — demands fast scannable grids, trust signals (compatibility badges, material callouts), and a checkout funnel that stays unobstructed by decorative weight. Spacing is compact at the product grid level but opens up generously in the hero, where lifestyle imagery earns room to breathe at `{spacing.section}` padding. The overall register is confident and youthful without shouting — a brand that believes personalization is a serious act of self-expression, not a novelty upsell.

colors:
  primary: "#7b2ff7"
  primary-active: "#6020d4"
  primary-disabled: "#c9a8fb"
  primary-light: "#ede5ff"
  accent: "#ff6b6b"
  accent-active: "#e54f4f"
  ink: "#1c1c2e"
  body: "#3d3d5c"
  muted: "#8080a0"
  muted-soft: "#adadc4"
  hairline: "#e0dff0"
  hairline-soft: "#ececf5"
  canvas: "#ffffff"
  surface-soft: "#f6f3ff"
  surface-card: "#ffffff"
  surface-strong: "#efecfa"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  success: "#22c97a"
  warning: "#f5a623"
  error: "#e53e3e"
  badge-new: "#7b2ff7"
  badge-sale: "#ff6b6b"
  badge-text: "#ffffff"
  star-fill: "#f5a623"
  scrim: "#1c1c2e"

typography:
  display-xl:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  category-chip:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  price-display:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-strike:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  compat-label:
    fontFamily: "'Inter', 'DM Sans', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.15px

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
    rounded: "{rounded.lg}"
    padding: 13px 28px
    height: 48px
    transition: background 150ms ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    border: "1.5px solid {colors.primary}"
    padding: 12px 27px
    height: 48px
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 13px 28px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-pill-filter:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.category-chip}"
    rounded: "{rounded.full}"
    padding: 7px 16px
    height: 36px
  button-pill-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.category-chip}"
    rounded: "{rounded.full}"
    padding: 7px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoArea: 160px
    shadow: "0 1px 4px rgba(28,28,46,0.06)"
  nav-item-active:
    textColor: "{colors.primary}"
    fontWeight: 600
    borderBottom: "2px solid {colors.primary}"
  mobile-nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
    iconSize: 22px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline-soft}"
    shadow: "0 2px 12px rgba(123,47,247,0.06)"
    padding: "{spacing.md}"
    imageAspect: "1:1"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    strikePriceTypography: "{typography.price-strike}"
    strikePriceColor: "{colors.muted}"
    compatTypography: "{typography.compat-label}"
    compatColor: "{colors.muted}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    shadow: "0 6px 24px rgba(123,47,247,0.14)"
    transition: box-shadow 180ms ease, border 180ms ease
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xl}"
    imageMaxWidth: 560px
    ctaStack: vertical
    minHeight: 480px
    rounded: "{rounded.none}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-compat:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  category-chip-row:
    display: flex
    gap: "{spacing.sm}"
    overflowX: scroll
    paddingY: "{spacing.sm}"
    scrollbarDisplay: none
  star-rating:
    fillColor: "{colors.star-fill}"
    emptyColor: "{colors.hairline}"
    size: 14px
    gap: 2px
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  trust-badge-bar:
    backgroundColor: "{colors.surface-soft}"
    borderTop: "1px solid {colors.hairline-soft}"
    borderBottom: "1px solid {colors.hairline-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    padding: "{spacing.md} {spacing.xl}"
    gap: "{spacing.xl}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    headerTypography: "{typography.title-md}"
    itemTitleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.none}"
    shadow: "-4px 0 32px rgba(28,28,46,0.10)"
  product-image-gallery:
    thumbnailSize: 72px
    thumbnailRounded: "{rounded.sm}"
    thumbnailBorderActive: "2px solid {colors.primary}"
    thumbnailBorderInactive: "1px solid {colors.hairline}"
    mainImageRounded: "{rounded.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary-light}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl} {spacing.xl}"
    borderTop: "3px solid {colors.primary}"
    legalTypography: "{typography.caption-sm}"
    legalColor: "{colors.muted}"

## Components

### Buttons

**`button-primary`** — Full-bleed violet (#7b2ff7) at 48px height with `{rounded.lg}` corners, carrying `{typography.button-md}` weight 600 in white. Hover deepens to `{colors.primary-active}` (#6020d4) with a 150ms ease transition; disabled state drops to `{colors.primary-disabled}` and sets `cursor: not-allowed`. This button handles all primary e-commerce actions: Add to Cart, Buy Now, Apply Coupon.

**`button-secondary`** — White canvas with a 1.5px violet border and violet text; matches primary geometry exactly so paired stacks align cleanly. Use for secondary actions like Save to Wishlist or Compare.

**`button-accent`** — Coral (#ff6b6b) variant at the same 48px height, reserved for promotional triggers and limited-time offer CTAs where urgency needs a distinct hue from the default violet.

**`button-ghost`** — Transparent background with violet text and no border. Used inside product cards for secondary links (View Details), and inline in content areas where a full button would overpower.

**`button-pill-filter`** and **`button-pill-filter-active`** — `{rounded.full}` chips at 36px height, sitting in a horizontal scroll row (`category-chip-row`). Inactive chips use `{colors.surface-strong}` fill; active chips flip to solid primary violet. These drive device-model filtering (iPhone 15, Samsung S24, etc.) — the highest-frequency interaction pattern on an accessories site.

### Search Bar

**`search-bar`** — Pill-shaped (`{rounded.full}`) on a `{colors.surface-soft}` lavender-tinted background, with a muted magnifier icon left-aligned. On focus the border transitions to 1.5px primary violet to confirm interaction. Sits center-stage in the desktop nav and full-width below the mobile hamburger. Placeholder text in `{colors.muted-soft}` reads "Search by model or accessory type" to coach users past generic queries.

### Navigation

**`nav-bar`** — 64px tall on desktop, white canvas with a 1px `{colors.hairline-soft}` underline and a subtle 4px box-shadow. Logo area reserves 160px left; nav links in `{typography.nav-link}` weight 500 cluster center-right with categories (Cases, Screen Protectors, Charging, Bundles). Active nav items underline with a 2px solid primary violet. The cart icon badge uses `{colors.badge-new}` fill with `{typography.badge}` count.

**`mobile-nav-bar`** — Collapses to 56px with a hamburger left, centered wordmark, and cart + search icons right. Category navigation moves into a full-screen drawer overlay on `{colors.canvas}`.

### Product Card

**`product-card`** — White card at `{rounded.lg}` with a faint lavender-tinted shadow (`0 2px 12px rgba(123,47,247,0.06)`) and a 1px `{colors.hairline-soft}` border. The product image occupies a 1:1 aspect ratio region with `{rounded.md}` clipping. Below: compatibility label in `{typography.compat-label}` muted gray (e.g., "For iPhone 15 Pro"), product name in `{typography.title-sm}`, star rating row, then price in `{typography.price-display}` primary violet with struck-through original in `{typography.price-strike}` muted. On hover, border transitions to primary violet and shadow deepens — signaling interactivity without an add-to-cart overlay that would slow scanning.

### Badges

**`badge-new`** and **`badge-sale`** — 10px all-caps labels at `{rounded.xs}`, positioned absolute top-left on product card images. New uses primary violet; Sale uses coral accent. Both maintain a minimum 32px tap clearance from image interactive areas. A third variant, **`badge-compat`**, appears inline below product titles in a neutral `{colors.surface-strong}` chip to surface device compatibility without urgency connotations.

### Hero Banner

**`hero-banner`** — Split layout: copy left, lifestyle/product image right, on a `{colors.surface-soft}` lavender ground. Title in `{typography.display-xl}` ink, body copy in `{typography.body-md}` at `{colors.body}`. CTA stack runs vertically — primary button above ghost link — with `{spacing.section}` vertical padding giving the zone room to breathe. On mobile the image stacks below copy at full width.

### Trust Badge Bar

**`trust-badge-bar`** — A slim horizontal strip (or 2×2 grid on mobile) bridging the hero and the product grid. Four slots: Free Shipping, Easy Returns, Secure Checkout, 2-Year Warranty — each a primary violet icon plus caption text. Background `{colors.surface-soft}` with hairline borders top and bottom keeps it present without competing with the hero CTA.

### Cart Drawer

**`cart-drawer`** — 400px slide-in from the right on canvas white, with a -4px left shadow creating elevation. Header "Your Cart" in `{typography.title-md}`, line items with thumbnail, compat label, variant selector, and `{typography.price-display}` price. Sticky footer holds the primary checkout button full-width. Scrim behind uses `{colors.scrim}` at 40% opacity.

### Footer

**`footer`** — Deep `{colors.ink}` (#1c1c2e) background with a 3px solid primary violet top-border as the sole decorative accent. Four-column link grid on desktop (Shop, Support, Company, Social) collapses to a single-column accordion on mobile. Heading labels in `{typography.title-sm}` canvas white; links in `{typography.body-sm}` at `{colors.muted-soft}`, lifting to `{colors.primary-light}` on hover. Legal strip beneath a `{colors.hairline}` divider in `{typography.caption-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to icon bar + drawer; hero stacks vertically; category chip row scrolls horizontally; cart drawer goes full-width; trust badge bar becomes 2×2 grid |
| Tablet | 744–1128px | 2-column product grid; nav retains wordmark + search + icons, categories in secondary row; hero maintains split layout at reduced padding |
| Desktop | 1128–1440px | 3–4 column product grid; full nav-bar at 64px; hero at full `{spacing.section}` vertical padding; sidebar filters may appear on category pages |
| Wide | > 1440px | Content max-width 1440px centered; product grid up to 5 columns; hero image scales freely; footer remains 4-column with added breathing room |

### Touch Targets

- All interactive elements minimum 44×44px tap target (Apple HIG / Google Material baseline)
- Category filter chips at 36px height padded to 44px vertical tap zone via negative-margin wrapper
- Cart icon and nav icon buttons: 48×48px touch box regardless of visual icon size (22px)
- Product card is fully tappable as a block element, not just the title text

### Collapsing Strategy

- Navigation: hamburger drawer at < 744px; search icon expands inline input on tap
- Product grid: 1 col → 2 col → 3–4 col at breakpoints; card padding reduces from `{spacing.md}` to `{spacing.sm}` on mobile
- Hero: horizontal split → stacked (image below fold) on mobile; headline drops from `display-xl` to `display-md` scale
- Footer: 4-column link grid → single-column expandable accordion on mobile; legal strip always remains visible
- Trust badge bar: single horizontal row → 2×2 grid on mobile with equal-weight cells

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted** — the site appears to load design tokens via client-side JavaScript, defeating static CSS analysis. The entire palette above is inferred from brand positioning ("UniqueMe" / personalization / accessories category) and is unverified against actual brand assets. Treat all hex values as placeholder estimates requiring QA against the live site or brand guidelines.
- **No font families extracted** — the typography stack defaults to Inter/DM Sans system fallbacks. The actual brand may use a licensed typeface (e.g., Gilroy, Outfit, Nunito) not detectable without JS rendering or a brand guide.
- **No theme-color meta tag** — prevents confirmation of the primary brand color via the browser chrome signal; corroborates the JS-loaded token hypothesis.
- **No Shopify confirmation** — platform is flagged False; actual e-commerce stack is unknown, which may affect component naming conventions and checkout flow patterns.
- **Logo geometry unknown** — wordmark shape, whether logotype or icon+text lockup, and whether the primary violet is used in the logo cannot be confirmed without visual inspection.
- **Dark mode support unknown** — no `prefers-color-scheme` tokens were extractable; a dark variant may or may not exist.
- **Promotional/sale rhythm unknown** — cadence and visual treatment of sales events (flash sales, bundle deals) cannot be confirmed from static extraction.
