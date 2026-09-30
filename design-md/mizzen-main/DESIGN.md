---
version: alpha
name: "Mizzen+Main"
source_url: "https://mizzenandmain.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The dress shirt that sweats with you — Mizzen+Main built its entire brand identity on a single material contradiction, performance-engineered fabric cut into the silhouette of boardroom formalwear, and the visual language holds that tension throughout. A deep performance navy (#1a2b4a) anchors every primary CTA and headline treatment, while a compressed, military-inflected sans-serif with wide uppercase tracking projects confidence without stuffiness. The palette is deliberately restrained: navy, white, a light cool gray for surfaces, and a signal red reserved exclusively for sale and clearance states. There are no expressive accent colors competing for attention — the photography does that work, showing the same button-down worn through a red-eye flight, a client dinner, and a weekend hike. Corner radii are tight throughout ({rounded.xs} at 4px for badges and chips, {rounded.sm} at 6–8px for cards and inputs), reflecting the precision-cut garment aesthetic rather than the soft pill-shapes that populate most DTC playbooks. The nav organizes by occasion and fit — not by product type alone — signaling that the brand sells a lifestyle proposition first and SKUs second. Performance-feature callouts ("Moisture-Wicking," "Wrinkle-Resistant," "4-Way Stretch") appear as tight uppercase chips inline with product titles, reinforcing that technical differentiation is the primary value claim. Landing sections breathe at 80–96px vertical spacing with full-bleed photography, then the product grid tightens to 24px gutters to maximize density. The footer is dense and utility-first: fit guides, fabric explainers, and a size calculator alongside the standard nav links, because Mizzen+Main's customer is a rational optimizer who needs convincing with data before he replaces every dress shirt he owns.

colors:
  primary: "#1a2b4a"
  primary-active: "#0f1c33"
  primary-disabled: "#8a9bb8"
  ink: "#111827"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  surface-navy-tint: "#eef1f6"
  on-primary: "#ffffff"
  accent-red: "#c0392b"
  accent-red-soft: "#fde8e8"
  sale: "#c0392b"
  on-sale: "#ffffff"
  star: "#f59e0b"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  overline:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.4px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-category:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1.2px
    textTransform: uppercase
  price-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 50px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 50px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-navy-tint}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 40px
  button-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-sale}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 50px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    border: "1px solid {colors.accent-red}"
    backgroundColor: "{colors.accent-red-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    height: 36px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    categoryLabelTypography: "{typography.nav-category}"
    linkTypography: "{typography.nav-link}"
    borderTop: "1px solid {colors.hairline}"
    padding: 32px 0
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageBg: "{colors.surface-soft}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-md}"
    salePriceColor: "{colors.sale}"
    originalPriceColor: "{colors.muted}"
    padding: "16px 0"
    gap: "{spacing.sm}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-sale}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  performance-chip:
    backgroundColor: "{colors.surface-navy-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    fontSize: 10px
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderUnselected: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.primary}"
    bgSelected: "{colors.primary}"
    textColorSelected: "{colors.on-primary}"
    height: 40px
    minWidth: 48px
    outOfStockOpacity: 0.35
    outOfStockDecoration: line-through
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 580px
    contentMaxWidth: 640px
    padding: "80px 48px"
  collection-hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    rounded: "{rounded.none}"
    padding: "64px 0"
  fit-guide-strip:
    backgroundColor: "{colors.surface-navy-tint}"
    textColor: "{colors.primary}"
    labelTypography: "{typography.overline}"
    bodyTypography: "{typography.body-sm}"
    padding: "32px 24px"
    rounded: "{rounded.xs}"
  product-detail-sticky-bar:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "16px 24px"
    productNameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-md}"
    ctaComponent: "button-primary"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.overline}"
    linkTypography: "{typography.body-sm}"
    linkColor: "#b0bcc9"
    linkHoverColor: "{colors.on-primary}"
    borderTop: "none"
    padding: "64px 0 32px"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.title-md}"
    itemNameTypography: "{typography.body-sm}"
    itemPriceTypography: "{typography.price-md}"
    borderLeft: "1px solid {colors.hairline}"
    width: 420px
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 40px
    width: 120px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    height: 36px
    dismissible: true
  rating-stars:
    filledColor: "{colors.star}"
    emptyColor: "{colors.hairline}"
    size: 14px
    gap: 2px
  review-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    ratingComponent: "rating-stars"
    bodyTypography: "{typography.body-sm}"
    authorTypography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — Navy (#1a2b4a) fill with white uppercase text at 0.6px letter-spacing, 50px height, tight 4px radius. Hover darkens to `{colors.primary-active}`; disabled state desaturates to `{colors.primary-disabled}` with `cursor: not-allowed`. Used for every primary conversion action: Add to Cart, Checkout, Shop Now.

**`button-secondary`** — White fill with a 2px navy border and matching navy uppercase text. Mirrors primary sizing exactly so the two can sit side by side without height mismatch. Active state fills with `{colors.surface-navy-tint}`. Used for secondary CTAs like Save to Wishlist or View Fit Guide.

**`button-ghost`** — Transparent fill with a 1px hairline border. Lower visual weight for tertiary actions like "Load More" or filter chips. Text remains `{colors.ink}` rather than navy, signaling non-conversion intent.

**`button-sale`** — Red (#c0392b) fill, same dimensions as primary. Used exclusively during promotional events; swaps in for `button-primary` on sale-flagged product pages to reinforce urgency without adding an extra button.

### Navigation

**`nav-bar`** — 64px white bar with a 1px hairline bottom border. Logo anchors left in `{colors.primary}` navy. Top-level category links use `{typography.nav-link}` (14px, weight 500) with a subtle hover underline. Cart icon with item count badge and account icon anchor right. On scroll, the bar gains a soft box-shadow without changing height or color.

**`nav-promo-bar`** — 36px navy strip above the main nav carrying promotional copy in `{typography.overline}` (11px, 700, 1.4px letter-spacing, uppercase, white). Dismissible via an ×. Collapses to zero on scroll past 100px to reclaim viewport real estate.

**`nav-mega-menu`** — Full-width dropdown panel on desktop, white background with a hairline top border. Column headers use `{typography.nav-category}` (uppercase, 1.2px tracking) in navy; links beneath use `{typography.nav-link}`. One column reserved for a featured editorial image with an overlaid CTA.

### Product Cards

**`product-card`** — Zero border radius on the card container itself; the image fills edge-to-edge with a soft `{colors.surface-soft}` background for transparent/white product photography. Name in `{typography.title-sm}`, price in `{typography.price-md}`. Sale price renders in `{colors.sale}` red with original price struck through in `{colors.muted}`. Color swatches (20px circles, `{rounded.full}`) appear on hover on desktop, always visible on mobile. Quick-add button fades in on image hover.

**`product-badge`** — Small navy chip (4px radius) with white uppercase text at 10px/0.8px tracking. Appears top-left on the product image. Variants include "NEW," "BEST SELLER," and occasion labels like "WEDDING SEASON."

**`sale-badge`** — Same geometry as `product-badge` but red fill (`{colors.sale}`). Never appears simultaneously with `product-badge` — sale state replaces the editorial badge.

**`performance-chip`** — Light navy-tint background with primary navy text, uppercase 10px label. Applied inline below the product name on PDP to call out fabric features ("MOISTURE-WICKING," "WRINKLE-FREE," "FOUR-WAY STRETCH"). Up to three chips per product, rendered in a flex-wrap row with 8px gap.

### Product Detail Page

**`size-selector`** — Flat rectangular buttons (40px height, min 48px wide) with hairline borders in deselected state; selected state fills with navy and flips text to white. Out-of-stock sizes are shown at 35% opacity with strikethrough text rather than hidden, so customers can see the full size run and register interest.

**`color-swatch`** — 20px circles with full border-radius. Selected state gains a 2px navy outline with a 2px white gap between swatch and outline (box-shadow technique). Adjacent swatches sit 4px apart.

**`product-detail-sticky-bar`** — Fixed bottom bar on mobile, sticky top-offset bar on desktop. Shows truncated product name, current price, and a full-width Add to Cart CTA. Appears after the primary ATC button scrolls out of view.

### Hero & Editorial

**`hero-banner`** — Full-bleed photography with a navy overlay gradient on the left half, ensuring text legibility against varied photography. Headline in `{typography.display-xl}` (white, 48px, weight 700), subhead in `{typography.body-md}` (white, 16px). Min-height 580px. CTA uses `button-primary` but white-inverted variant (white fill, navy text) when placed over the dark overlay.

**`collection-hero`** — Lighter editorial header at the top of collection pages. Soft surface background (`{colors.surface-soft}`), navy headline in `{typography.display-lg}`, optional breadcrumb above. No photography — gives the page a clean grid entry before product cards begin.

**`fit-guide-strip`** — A navy-tint callout band (surface-navy-tint background) placed mid-page on PDPs, directing customers to the size and fit guide. Overline label in primary navy, body copy in 14px. Rounded at 4px. This is one of the brand's key conversion tools given that fit uncertainty is the primary objection.

### Cart & Checkout

**`cart-drawer`** — 420px right-side drawer with a 1px left border. Header ("Your Cart") in `{typography.title-md}`. Line items show product image (64px square, 4px radius), name in `{typography.body-sm}`, variant details in `{typography.caption}` muted, and price in `{typography.price-md}`. `quantity-stepper` appears inline per item. Drawer footer is sticky with order summary and a full-width primary CTA.

### Footer

**`footer`** — Navy fill (`{colors.primary}`) with white headlines in `{typography.overline}` and subdued link text (#b0bcc9). Four-column layout on desktop: Shop, Help, Company, and a newsletter signup column. Newsletter input uses a white-border-on-navy variant of `text-input`. Legal and social links in the sub-footer row at 12px. The all-navy footer creates a strong bookend that reinforces brand identity at scroll terminus.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart; `hero-banner` min-height reduces to 420px, headline drops to 32px; `product-detail-sticky-bar` pins to bottom; size selector scrolls horizontally; `cart-drawer` goes full-width overlay |
| Tablet | 744–1128px | Two-column product grid; nav retains logo + cart + hamburger (mega-menu not triggered); hero layout shifts to 50/50 split; fit-guide-strip collapses to single column |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with mega-menu dropdowns; hero returns to full-bleed with left-rail text overlay; sticky PDP bar activates on scroll past primary ATC |
| Wide | > 1440px | Four-column product grid; content areas max out at 1440px with auto side margins; hero photography scales to fill without stretching content layer |

### Touch Targets

- All interactive size selectors minimum 44×44px on mobile regardless of label length
- Color swatches expand from 20px to 28px on mobile
- Nav hamburger and cart icon hit areas are 48×48px
- Quantity stepper buttons minimum 44px wide per side
- Footer links minimum 40px vertical height with increased line-height

### Collapsing Strategy

- Mega-menu converts to accordion-style drawer panels inside the mobile nav
- Performance chips below product title stack vertically if they exceed two rows on narrow viewports
- Fit guide strip collapses to a single centered CTA link on mobile rather than full content block
- Announcement bar reduces to a single rotating line (no manual dismiss on mobile — auto-rotates if multiple messages)
- Product card hover states (quick-add button, color swatch reveal) convert to always-visible tap targets on mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Full palette unextracted**: The site was blocked by a Vercel Security Checkpoint during crawl; the colors #0070f3 and #3291ff are Vercel's own verification UI, not Mizzen+Main brand tokens. All hex values in this file are derived from widely-documented brand knowledge and visual inspection, not live extraction — treat as approximations requiring verification against the live stylesheet.
- **Exact brand typeface unknown**: The font stacks extracted are all system defaults from the Vercel checkpoint page. Mizzen+Main may use a licensed display or sans-serif; the Helvetica Neue stack used here is a documented fallback consistent with premium menswear conventions but should be verified.
- **Primary navy exact value unconfirmed**: #1a2b4a is an estimate based on brand photography analysis. The live site may use a slightly different navy (e.g., #162236, #1d2f50).
- **Component-level spacing unverified**: All padding, height, and gap values are inferred from category norms and brand aesthetic — live CSS inspection is needed to confirm PDP, cart, and nav exact measurements.
- **Promotional/sale color frequency**: It is unclear whether the brand runs persistent sale states or only seasonal promotions; the `button-sale` and `sale-badge` components should be validated against live site behavior.
- **Custom icon set**: Mizzen+Main likely uses a custom icon set for nav, product features, and fit guides; no icon tokens have been specified here.
- **Animation and transition tokens**: Hover and transition timing values were not extractable; a standard 200ms ease is assumed throughout.
