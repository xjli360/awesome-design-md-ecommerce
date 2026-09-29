---
version: alpha
name: "Jaipur Rose"
source_url: "https://www.jaipurrose.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The rose in the name is less about petals and more about a specific magenta — #c6007e — that blazes through category badges and promotional CTAs like zardozi embroidery on silk. Jaipur Rose serves the South Asian diaspora in the United States with Indian wedding and festive jewelry, and every dominant hue in the palette reads as deliberate cultural register: deep teal (#108474) anchors the primary nav, main CTAs, and trust elements the way a peacock-blue dupatta grounds a bridal ensemble; marigold (#fbcd0a) flares across sale banners and price callouts the way it does strung at a mandap entrance; deep plum (#5c1e4b) carries footer grounds and overlay scrim with the gravity of polished amethyst on a velvet display tray. Soft lavender (#a89cc8) enters only in filter chips and hover-state washes, keeping the regal register without oversaturating. Type pairs Baskerville — a classical serif used for display headlines and product titles — with Nunito Sans for body copy, labels, and UI text, a combination that reads simultaneously as fine-jewelry heritage and accessible online retail. Rounded corners sit deliberately near-square: buttons at {rounded.xs}, cards at {rounded.sm}, inputs at {rounded.xs}. This restraint signals a structured, high-value context rather than the exuberant pill-shapes of lifestyle DTC; the formality suits a store where a single SKU may be a bridal set costing several thousand dollars. The canvas stays near-white (#f9fafb, #f9f9f9) throughout so that gold, kundan, polki, and enamel photography reads true rather than fighting a tinted ground. Promotional voltage — sale stickers, countdown banners, free-shipping bars — draws on both the magenta and the marigold depending on register: magenta for urgency, marigold for celebration. The secondary teal surface (#c1e6e6, #edf5f5) appears in informational callout boxes and category intro strips, diluting the primary brand teal into an ambient contextual tone.

colors:
  primary: "#108474"
  primary-active: "#0a6b5e"
  primary-disabled: "#a8d4cf"
  accent-magenta: "#c6007e"
  accent-magenta-active: "#ff0083"
  accent-gold: "#fbcd0a"
  accent-plum: "#5c1e4b"
  accent-lavender: "#a89cc8"
  teal-soft: "#c1e6e6"
  teal-wash: "#edf5f5"
  ink: "#121212"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  border-strong: "#bbbbbb"
  canvas: "#f9fafb"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  surface-strong: "#f2f2f2"
  on-primary: "#ffffff"
  on-accent-magenta: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Baskerville Old Face', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Baskerville Old Face', serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Baskerville, 'Baskerville Old Face', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-upper:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  price-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-magenta:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-accent-magenta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-magenta-active:
    backgroundColor: "{colors.accent-magenta-active}"
    textColor: "{colors.on-accent-magenta}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoFontFamily: "Baskerville, serif"
  promo-bar:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-accent-magenta}"
    typography: "{typography.label-upper}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1/1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-lg}"
    originalPriceTypography: "{typography.price-sm}"
    originalPriceColor: "{colors.muted}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-badge:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-accent-magenta}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 3px 8px
    position: "top-left"
  sale-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.accent-plum}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    overlayOpacity: 0.35
    ctaComponent: "button-magenta"
    minHeight: 480px
  occasion-strip:
    backgroundColor: "{colors.teal-wash}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    labelTypography: "{typography.label-upper}"
    labelColor: "{colors.primary}"
    padding: "{spacing.xl} 0"
  collection-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    labelTypography: "{typography.display-sm}"
    overlayColor: "{colors.accent-plum}"
    overlayOpacity: 0.5
    textOnOverlay: "{colors.on-dark}"
  filter-chip:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  info-callout:
    backgroundColor: "{colors.teal-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.primary-disabled}"
  trust-badge-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
  footer:
    backgroundColor: "{colors.accent-plum}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.teal-soft}"
    headingTypography: "{typography.label-upper}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"

## Components

### Buttons

**`button-primary`** — Teal (#108474) fill on a 2px-radius near-square shape, white label in 14px bold Nunito Sans with 0.5px tracking. On hover the fill shifts to the active teal (#0a6b5e); disabled state renders the background at the pale teal (#a8d4cf) so the shape remains visible without conveying affordance. Height is 44px throughout to match the touch target floor.

**`button-secondary`** — White fill with a 1px teal border and teal label text, matching the primary's geometry. Used for secondary actions like "View Details" on product cards and "Continue Shopping" in the cart — it pairs cleanly with `button-primary` without competition.

**`button-magenta`** — #c6007e fill, activating to #ff0083 on hover. Reserved for high-urgency calls to action: limited-time offers, bridal consultation CTAs, and the "Add to Cart" action on PDPs during promotional windows. Its brightness against the near-white canvas creates immediate focal pull.

**`promo-bar`** — Full-width magenta bar above the nav, 36px tall, rendering announcement text in the `label-upper` style (11px, uppercase, 0.8px tracking). Used for free-shipping thresholds, festival sale countdowns, and new-collection announcements.

### Inputs

**`text-input`** — White fill, 1px #dedede border resting, shifts to 1px #108474 on focus. 44px height, 10px vertical padding, 14px horizontal. Placeholder in `{colors.muted}`. Used in search, address forms, and the newsletter signup in the footer.

**`filter-chip`** / **`filter-chip-active`** — Pill-shaped (#full) chips for category and metal filters. Resting state uses #f2f2f2 fill with muted label; active flips to teal fill with white label. The pill shape here is the only full-radius element in the system — it signals a toggleable selection rather than a navigation destination.

### Navigation

**`nav-bar`** — White, 64px tall, 1px #dedede bottom border. Brand name in Baskerville serif at the left; navigation links in 13px bold Nunito Sans; search icon, wishlist, and cart at the right. On scroll-past, the bar gains a subtle drop shadow. A separate `promo-bar` sits above it at full magenta.

### Product Cards

**`product-card`** — White fill, 1px soft hairline (#eeeeee) border, 4px radius. Square 1:1 image region fills the top; below, product name in 14px bold Nunito Sans, price in 18px bold, original price struck through in 13px muted when on sale. Badges (`product-card-badge`, `sale-badge`, `new-badge`) are zero-radius stamps positioned top-left over the image. Card hover elevates with a light drop shadow without any translate animation — appropriate to a premium register.

### Hero and Collections

**`hero-banner`** — Full-width image with a plum (#5c1e4b) color overlay at 35% opacity. Display headline in Baskerville at 36px white, supporting subtitle in 15px Nunito Sans white, and a `button-magenta` CTA. Minimum height 480px; on mobile it collapses to 320px with the heading scaling to `display-md`.

**`occasion-strip`** — A teal-wash (#edf5f5) band housing a row of occasion thumbnails (Bridal, Festive, Office, Casual). Section label appears in `label-upper` teal above the row. This component maps to the Indian wedding-season shopping pattern: filtering by occasion rather than metal or gemstone.

**`collection-card`** — Aspect-ratio image cards (roughly 3:4) for collection landing tiles. A plum semi-transparent overlay (#5c1e4b at 50%) covers the lower third on hover, revealing the collection name in Baskerville `display-sm` white. Used in the "Shop by Collection" grid on the homepage.

### Information and Trust

**`info-callout`** — Soft teal background (#c1e6e6) with a teal border, used for shipping notes, hallmark-certification callouts, and return-policy snippets on the PDP. Typography is `body-sm` in the dark primary teal (#0a6b5e) for accessible contrast.

**`trust-badge-row`** — A horizontal strip of 3–4 icon+label pairs (Certified Hallmark, Free Shipping, Easy Returns, Secure Payment) anchored in `surface-soft` with a top hairline. Icons draw in the primary teal; labels in `caption` muted gray.

### Footer

**`footer`** — Deep plum (#5c1e4b) background across a full-width block with heading labels in the `label-upper` style (white, uppercase, tracked) and body links in small teal-soft (#c1e6e6) text. Social icons render in white at 24px. Padding is section-scale (64px) top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces full link row; hero scales to 320px min-height; promo bar stacks to two lines if needed; filter panel becomes a bottom drawer |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + search + cart, all categories in a mega-menu off a hamburger; hero at 400px |
| Desktop | 1128–1440px | Three or four-column product grid; full nav bar with all top-level categories visible; hero at 480px; occasion strip shows 5–6 tiles |
| Wide | > 1440px | Max content width capped at 1440px, centered with auto side margins; product grid stays at four columns; hero may expand to viewport width with content constrained |

### Touch Targets
- All buttons, chips, and icon buttons maintain a minimum 44px tap height
- Filter chips on mobile expand horizontal padding to 18px to improve tap precision
- Cart and wishlist icons in the mobile nav bar each occupy a 44×44px touch zone
- Product card tap target is the entire card face, not just the title text

### Collapsing Strategy
- Top navigation collapses to logo + hamburger icon at < 744px; mega-menu becomes a slide-in drawer with accordion subcategories
- The promo bar persists on mobile but hides on scroll-down (re-appears on scroll-up)
- Occasion strip becomes a horizontally scrollable single row on mobile rather than a grid
- Footer columns stack vertically on mobile with each heading acting as an accordion toggle
- PDP image gallery switches from side-by-side main+thumbs to a full-width swipeable carousel on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; Baskerville is assumed from the font stack but its exact weight ranges and display usage on the live site were not confirmed
- Arsenal font was present in the stack but no clear role in the hierarchy was identifiable from extraction data alone; it may be used in a specific banner or promotional context
- No confirmed border-radius values from computed styles — all rounded values are inferred from Shopify defaults and Indian jewelry brand conventions
- Exact nav bar height and sticky-scroll behavior not confirmed
- No dark-mode tokens observed; unclear if the site supports a dark scheme
- Social colors (#3b5998, #1da1f2, #dd4b39, #e60023, #0073b1) are platform-standard and excluded from brand token set
- #ffff00 and #fffb00 appear in the extracted palette but their precise use context (possibly promotional countdown or highlight text) is unconfirmed
- Product badge placement, size, and exact corner radius on the live PDP not verified
