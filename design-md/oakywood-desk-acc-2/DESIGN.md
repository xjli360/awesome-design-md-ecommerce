---
version: alpha
name: "Oakywood"
source_url: "https://oakywood.shop"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric violet (#4500ff) against a near-black ink layer (#1a1a1a) is a jarring opening move for a brand that hand-finishes walnut and oak into desktop organizers — but that voltage gap is exactly how Oakywood marks every primary CTA, quick-add button, and cart confirmation. The surrounding palette is a long, deliberate grayscale column: from ink at #1a1a1a through mid-charcoal #222222, descending through six gray intervals (#bbbbbb, #d9d9d9, #e5e5e5, #eeeeee, #f2f2f2) before settling on a near-white canvas at #fafafa. Two material-coded accents break the gray run — deep teal #108474 marks eco-certification callouts and sustainability credentials, while warm amber #fbcd0a surfaces in star ratings and limited-offer flags. The dark panel #1c1d1d anchors the footer and hero sections, letting ivory product photography emerge against a near-black field. Type runs in Muli (now distributed as Mulish), a geometric sans-serif with low stroke contrast that signals machined precision without industrial coldness; Graphie, a softer geometric with slightly rounded terminals, handles section display headers. Both weights run lean — the brand trusts grain photography over typographic muscle. Pill-shaped material badges ({rounded.full}) label wood species at a glance on every product card, and the eco-certification strip uses {colors.eco-tint} as a barely-there teal wash so the credential reads as fact rather than claim. The announcement bar runs {colors.primary} end-to-end at 40px — electric violet as a horizontal stripe forces brand recognition before the product grid loads. Navigation is text-tight and light against {colors.canvas}, with a 1px {colors.hairline} underline separating it from the scroll context below.

colors:
  primary: "#4500ff"
  primary-active: "#3800cc"
  primary-disabled: "#c4b3ff"
  ink: "#1a1a1a"
  body: "#222222"
  muted: "#6f6f6f"
  muted-soft: "#7b7b7b"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#f9fafb"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  accent-gold: "#fbcd0a"
  eco-tint: "#edf5f5"
  dark-panel: "#1c1d1d"

typography:
  display-xl:
    fontFamily: "'Graphie', 'Muli', 'Mulish', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Graphie', 'Muli', 'Mulish', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Graphie', 'Muli', 'Mulish', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  label:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Graphie', 'Muli', 'Mulish', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  price-sm:
    fontFamily: "'Muli', 'Mulish', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1.5px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "none"
    typography: "{typography.button-sm}"
    padding: 0
    height: auto
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    borderRadius: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    height: 40px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    comparePriceTypography: "{typography.price-sm}"
    comparePriceColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    imageBorderRadius: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    badgeBackground: "{colors.ink}"
    badgeTextColor: "{colors.canvas}"
    badgeTypography: "{typography.label}"
    badgeRounded: "{rounded.xs}"
    badgePadding: 3px 8px
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  eco-badge:
    backgroundColor: "{colors.eco-tint}"
    textColor: "{colors.accent-teal}"
    border: "1px solid {colors.accent-teal}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero:
    backgroundColor: "{colors.dark-panel}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 580px
    contentMaxWidth: 620px
    paddingX: "{spacing.section}"
    paddingY: "{spacing.xxl}"
  collection-filter-pill:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
    height: 36px
  collection-filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
    height: 36px
  rating-star:
    fillColor: "{colors.accent-gold}"
    emptyColor: "{colors.hairline}"
    size: 14px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-md}"
    lineItemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-sm}"
    borderLeft: "1px solid {colors.hairline}"
    width: 420px
    paddingX: "{spacing.lg}"
    paddingY: "{spacing.lg}"
  sustainability-strip:
    backgroundColor: "{colors.eco-tint}"
    textColor: "{colors.accent-teal}"
    iconColor: "{colors.accent-teal}"
    typography: "{typography.body-sm}"
    paddingY: "{spacing.xl}"
    textAlign: center
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px
    buttonWidth: 40px
  footer:
    backgroundColor: "{colors.dark-panel}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label}"
    paddingY: "{spacing.section}"
  section-label:
    textColor: "{colors.accent-teal}"
    typography: "{typography.label}"
    marginBottom: "{spacing.sm}"

## Components

### Buttons

**`button-primary`** — Flat electric violet (#4500ff) fill with white uppercase Muli text, 8px radius, 48px height. The uppercase tracking (0.8px) reinforces a product-company register rather than a lifestyle-brand softness. Hover deepens to `{colors.primary-active}` (#3800cc) with no animation delay; disabled state washes to `{colors.primary-disabled}` with white text preserved. Used for Add to Cart, Checkout, and primary hero CTAs throughout.

**`button-secondary`** — Transparent fill with a 1.5px ink border and ink uppercase text. On hover the fill inverts to `{colors.ink}` with white text — a hard swap rather than a fade, matching the brand's direct material language. Used for secondary hero actions, email opt-ins, and alternative product options.

**`button-ghost`** — No border, no fill; violet text in the smaller uppercase Muli scale. Used inline for "View all", wishlist toggles, and filter reset links where a box button would crowd the layout.

### Announcement Bar

**`announcement-bar`** — A 40px full-bleed violet band that sits above the nav, making `{colors.primary}` the very first thing the viewport renders. Uppercase 11px Muli label type in white carries promotional copy (free shipping thresholds, seasonal offers). The violence of the color against the calm wood product imagery is intentional — it reads as a designed system signal, not a sale sticker.

### Navigation

**`nav-bar`** — 64px white bar on `{colors.canvas}` with a 1px `{colors.hairline}` bottom edge. Nav links run in 14px semi-bold Muli with 0.2px tracking; the wordmark sits left. Cart and search icons anchor right. No mega-menu borders — category dropdowns float against white with hairline separators. On scroll the bar remains fixed and light, letting product photography scroll underneath without tinting.

### Product Card

**`product-card`** — Light `{colors.surface-card}` shell with an 8px radius and 1px `{colors.hairline-soft}` border. Product title in 16px semi-bold Muli, price in 22px Graphie bold. A discount badge (ink fill, white `{typography.label}`) sits over the image top-left. Below the price row, `material-badge` pills (Walnut, Oak, Bamboo, Cork) identify the available wood variant at a glance. On hover the card lifts with a subtle box-shadow and the primary CTA button slides up from below the image.

### Material Badges

**`material-badge`** — Pill-shaped ({rounded.full}) tokens in `{colors.surface-soft}` with a `{colors.hairline}` border and `{typography.caption}` text. These are the product card's primary filtering surface — wood species, finish type (natural, dark stain), and size options all appear as scannable pills rather than dropdown selects. Keeping them visible shortens time-to-decision for a returning buyer who already knows they want walnut.

### Eco Badge

**`eco-badge`** — Pill-shaped like `material-badge` but uses `{colors.eco-tint}` fill and `{colors.accent-teal}` text and border. Appears on product cards when items carry FSC certification or are made from recycled materials. The teal ink is the only place `{colors.accent-teal}` appears at component scale, reserving its credibility signal.

### Hero

**`hero`** — Near-black `{colors.dark-panel}` (#1c1d1d) full-bleed section, minimum 580px tall. Display heading in 52px Graphie 700 in ivory-white; supporting copy in `{typography.body-md}` at 65% opacity of white. Primary CTA button sits below the sub-copy. Photography is set to the right half of the desktop layout as an object-fit cover panel, letting grain and finish details speak at large scale. On mobile the image collapses below the text block.

### Collection Filter Pills

**`collection-filter-pill`** / **`collection-filter-pill-active`** — A row of rounded pill filters above the product grid for categories like "Desk Organizer", "Monitor Stand", "Cable Management". Default state: transparent fill, `{colors.muted}` text, `{colors.hairline}` border. Active state: `{colors.primary}` fill with white text, same border radius. Multiple filters can be active simultaneously; each fires a Shopify collection filter parameter.

### Sustainability Strip

**`sustainability-strip`** — A full-bleed `{colors.eco-tint}` band (barely-there teal wash) between sections, carrying three icon+text credential blocks: "FSC Certified Wood", "Carbon-Neutral Shipping", "Lifetime Warranty". Icon and text both in `{colors.accent-teal}`, `{typography.body-sm}`. The muted background prevents it from reading as a promotional module — it functions as verified fact, not marketing copy.

### Cart Drawer

**`cart-drawer`** — 420px slide-in panel from the right with a 1px left border in `{colors.hairline}`. Header "Your Cart" in `{typography.title-md}`. Line items show product thumbnail (8px radius), name in `{typography.body-sm}`, and price in `{typography.price-sm}`. Quantity selector (`{quantity-selector}`) uses the outlined variant. Checkout CTA is a full-width `button-primary` pinned to the drawer bottom.

### Rating Stars

**`rating-star`** — 14px amber (#fbcd0a) filled stars rendered by the JudgeMeStar widget. Empty state uses `{colors.hairline}`. Appears on product cards (row beneath title) and on the PDP review section. The amber is the only warm color in an otherwise cool-neutral + violet palette; it reads immediately as social proof without clashing.

### Footer

**`footer`** — Full `{colors.dark-panel}` background matching the hero, creating a dark bookend around the page's light body. Four columns: brand/newsletter, Shop, About, Social links. Column heads in `{typography.label}` (white uppercase), links in `{typography.body-sm}` with `{colors.hairline}` muted-white color. Newsletter input uses the standard `text-input` on dark with an inverted border.

### Section Label

**`section-label`** — 11px uppercase Muli in `{colors.accent-teal}` used above section headings ("Our Materials", "Sustainability", "Workshop"). Functions as a category tag rather than a heading level; the teal ink visually separates it from the main Graphie heading beneath.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer; hero image moves below text; announcement bar truncates to one line; filter pills scroll horizontally; buttons full-width; cart drawer fills 100vw |
| Tablet | 744–1128px | 2-column product grid; nav retains icon links but drops category sub-labels; hero switches to 50/50 text-image split; sustainability strip stacks to single-column icons |
| Desktop | 1128–1440px | 3-column product grid; full nav with category dropdowns; hero at full 580px with right-panel photography; filter pill row visible above grid; cart drawer at 420px fixed width |
| Wide | > 1440px | Content capped at 1440px max-width with centered layout; product grid optionally expands to 4 columns on collection pages; hero photography scale increases |

### Touch Targets

- All primary and secondary buttons minimum 48px height
- Filter pills minimum 36px height with 18px horizontal padding to ensure tap area
- Nav icons (cart, search, hamburger) minimum 44×44px tap zone
- Quantity selector increment/decrement buttons each 40×40px
- Material badge pills on mobile expand vertical padding to 8px for thumb comfort

### Collapsing Strategy

- Product description tabs (Details, Dimensions, Materials) collapse to accordion on mobile
- Sustainability strip three-column icon grid collapses to vertical stack below 744px
- Footer four-column layout collapses to single-column accordion on mobile
- Collection sidebar filters (if present on desktop) move to a modal sheet on mobile triggered by a "Filter" pill button
- Nav category dropdowns convert to nested drawer items within the hamburger menu

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color set — mobile browser chrome color unspecified; violet (#4500ff) is the most defensible inference but unconfirmed
- `{colors.on-primary}` (#ffffff) and `{colors.primary-active}` (#3800cc) are computed or inferred — not present in the extracted color list
- Exact component border-radius values are inferred from design conventions; Shopify theme CSS custom properties are not extractable at crawl time
- Graphie font hosting and full weight/style range unknown — may be self-hosted or via a licensed CDN; fallback chain uses Muli/Mulish
- Dark mode support unverified — palette has plausible dark-mode tokens but no confirmed @media prefers-color-scheme override was detected
- Hover and transition timing (duration, easing) not extractable; values throughout are conventional defaults
- Product card hover behavior (CTA slide-up, shadow lift) inferred from Shopify theme conventions, not confirmed via interaction recording
- Mobile breakpoint pixel values are Shopify Dawn/OS2 convention defaults — actual theme overrides may differ
