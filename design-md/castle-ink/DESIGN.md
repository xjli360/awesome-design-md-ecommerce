---
version: alpha
name: "Castle Ink"
source_url: "https://www.castleink.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep seawater teal (#108474) anchors the Castle Ink storefront — an unusual choice for a printer-supply brand that typically defaults to corporate blue or warehouse gray, and a color that reads with specialist authority across a high-SKU cartridge catalog. The accent is #fbcd0a, a brass-coin yellow pressed into primary CTAs, promotional badges, and sale callouts, creating a two-tone signal system immediately legible in dense product grids. Ambient surface tones cool into #c1e6e6 (soft mint wash) and #edf5f5 (barely-there teal ground), giving rows of cartridge thumbnails room to breathe without abandoning hue coherence; the meta theme-color #557b97, a muted slate-blue, bridges the deeper teal and the neutral page grid in browser chrome and nav hover states. Nunito Sans carries the entire type stack — a geometric sans with rounded stroke terminals that keeps part-number listings and compatibility tables legible without the coldness of Arial or Helvetica — and display headings run at weight 700 while UI copy settles at 400–600, letting color carry hierarchy rather than typographic mass. Buttons sit on {rounded.sm} radii (8px) rather than full pills — the transaction is direct and functional, not a lifestyle gesture. Product cards use #dedede hairline borders over drop shadows, keeping the grid clean while thumbnail imagery carries visual weight. Pricing signals run three deep through an amber-gold progression — #fbcd0a for the sale price, #d2920f for savings callout text, #a36710 for original-price strike-through — communicating discount depth without red-alarm urgency. Free U.S. shipping, foregrounded in the page title itself, surfaces as a persistent teal promo bar that plants the core value proposition before the first scroll. A lavender accent (#a89cc8) appears selectively in trust-badge and feature-highlight contexts, adding a third hue that keeps the palette from reading as purely transactional.

colors:
  primary: "#108474"
  primary-active: "#0d7265"
  primary-disabled: "#c1e6e6"
  accent: "#fbcd0a"
  accent-dark: "#a36710"
  accent-mid: "#d2920f"
  ink: "#121212"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#fafafa"
  surface-teal-light: "#edf5f5"
  surface-teal-mid: "#c1e6e6"
  on-primary: "#ffffff"
  on-accent: "#121212"
  nav: "#557b97"
  lavender: "#a89cc8"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  price-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  label-compat:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 44px 10px 14px
    height: 44px
    submitButtonColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoAccentColor: "{colors.primary}"
  promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    padding: 0 16px
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-lg}"
    priceColor: "{colors.primary}"
    originalPriceTypography: "{typography.price-sm}"
    originalPriceColor: "{colors.muted}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
  badge-sale:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-compat}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-compatible:
    backgroundColor: "{colors.surface-teal-light}"
    textColor: "{colors.primary}"
    typography: "{typography.label-compat}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-free-shipping:
    backgroundColor: "{colors.surface-teal-mid}"
    textColor: "{colors.primary-active}"
    typography: "{typography.label-compat}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  price-display:
    saleColor: "{colors.accent}"
    savingsTextColor: "{colors.accent-mid}"
    originalPriceColor: "{colors.accent-dark}"
    originalPriceDecoration: line-through
    saleTypography: "{typography.price-lg}"
    originalTypography: "{typography.price-sm}"
  compatibility-table:
    backgroundColor: "{colors.surface-teal-light}"
    borderColor: "{colors.surface-teal-mid}"
    rounded: "{rounded.sm}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    padding: "{spacing.base}"
  star-rating:
    filledColor: "{colors.accent}"
    emptyColor: "{colors.hairline}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-teal-mid}"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The teal (#108474) primary button handles every principal CTA: "Add to Cart," "Checkout," and "Shop Now." It sits at 44px height with `{rounded.sm}` corners and Nunito Sans 15px/700; hover transitions to `{colors.primary-active}` (#0d7265), a perceptibly darker teal. Disabled state falls to the mint wash `{colors.primary-disabled}` with `{colors.muted}` label text.

**`button-accent`** — The brass-coin yellow (#fbcd0a) variant with dark `{colors.on-accent}` text is reserved for sale-event CTAs and promotional landing banners where the yellow carries the urgency signal that the teal primary does not. Identical dimensions and `{rounded.sm}` radius keep layout interchangeable with `button-primary`.

**`button-secondary`** — A 2px `{colors.primary}` outlined button with transparent fill and matching teal label, used for secondary actions such as "View Details" or "Compare Cartridges." The border-and-text-only treatment provides clear hierarchy below the filled primaries without introducing a new color.

**`button-ghost`** — Transparent background with `{colors.body}` gray text in `{typography.button-sm}`, used for dismissals, "Continue Shopping" links, and low-priority navigation actions in dense UI regions.

### Search
**`search-bar`** — Full-width input with 44px height, `{rounded.sm}` radius, and a `{colors.primary}` focus ring replacing the resting `{colors.hairline}` border. Right-side submit icon button carries the teal fill. Placeholder text in `{colors.muted}` prompts printer model or cartridge part number input. Prominent placement in the nav area reflects the catalog's depth — part-number search is the fastest path to conversion.

### Navigation
**`nav-bar`** — 64px white canvas bar with a soft `{colors.hairline-soft}` bottom border. `{typography.nav-link}` (14px/600) renders category links in `{colors.ink}`; the logo mark uses `{colors.primary}` as its accent hue. A "Shop by Printer" or category dropdown surfaces as the primary nav affordance. Cart and account icons sit right-aligned with 44px tap targets.

**`promo-bar`** — A 36px strip in `{colors.primary}` pinned above the nav, carrying the "Free U.S. Shipping" message in `{colors.on-primary}` caption type. This element is the first brand impression at every page load and anchors the value proposition before the hero or product grid is visible.

### Product Cards
**`product-card`** — White canvas card with `{rounded.sm}` radius, `{colors.hairline}` border, and `{spacing.base}` internal padding. The thumbnail sits on `{colors.surface-soft}` for neutral contrast behind white-background packaging imagery. Title in `{typography.title-sm}` / `{colors.ink}`, sale price in `{typography.price-lg}` / `{colors.primary}`, original price in `{typography.price-sm}` / `{colors.muted}` with strikethrough. Compatible printer model listed in `{typography.caption}` / `{colors.muted}` below the title — a critical trust signal for ink SKUs. An "Add to Cart" `button-primary` appears below the price block or on hover.

### Badges
**`badge-sale`** — Brass-coin yellow (`{colors.accent}`) ground with `{colors.on-accent}` dark text, `{typography.label-compat}` uppercase 11px, `{rounded.xs}` corner radius, 3px×8px padding. Flags marked-down cartridges on product cards and search results.

**`badge-compatible`** — Teal-tint surface (`{colors.surface-teal-light}`) with `{colors.primary}` label text. Applied to OEM-compatible and remanufactured SKUs as a product-type classifier — the most information-dense badge in the system given ink's compatibility complexity.

**`badge-free-shipping`** — Mint ground (`{colors.surface-teal-mid}`) with `{colors.primary-active}` text, reinforcing the free-shipping promise at the product level without visually competing with the sale badge on the same card.

### Pricing
**`price-display`** — Three-stop amber-gold system: sale price in `{colors.accent}` at `{typography.price-lg}`, savings amount or percentage in `{colors.accent-mid}`, original price in `{colors.accent-dark}` with line-through at `{typography.price-sm}`. The warm progression from bright yellow through amber to brown communicates discount depth on a single hue axis without introducing red tension.

### Compatibility Table
**`compatibility-table`** — Appears on product detail pages listing compatible printer makes and models. Rendered as a `{rounded.sm}` card on `{colors.surface-teal-light}` with a `{colors.surface-teal-mid}` border, keeping the teal brand hue present in a utility context. Header row uses `{typography.title-sm}` in `{colors.primary}`; body rows use `{typography.body-sm}` in `{colors.body}` with `{spacing.base}` padding.

### Reviews
**`star-rating`** — Powered by the Judge.me third-party widget; star fill mapped to `{colors.accent}` (#fbcd0a) for visual coherence with the sale and pricing palette. Empty stars use `{colors.hairline}`. Review count and score displayed in `{typography.caption}` / `{colors.muted}` inline with the stars.

### Quantity & Cart Controls
**`quantity-stepper`** — 40px height, `{rounded.xs}` corners, `{colors.surface-soft}` background with `{colors.hairline}` border. Minus and plus buttons flank a centered numeric input in `{typography.body-md}` / `{colors.ink}`. Minimum 40×40px touch target per button cell.

### Footer
**`footer`** — Dark `{colors.ink}` (#121212) ground anchors the page bottom. Body links in `{colors.surface-teal-mid}` provide the brand's secondary hue on dark; hover shifts to full `{colors.on-primary}` white. Section headings in `{typography.title-sm}` (white). Four-column desktop layout: Shop by Printer, Shop by Brand, Customer Service, About. `{spacing.section}` vertical padding and `{spacing.xl}` horizontal padding.

### Breadcrumb
**`breadcrumb`** — `{typography.caption}` / `{colors.muted}` inactive links, `{colors.ink}` for the active (current) page segment, `{colors.hairline}` separator chevrons. Appears on all category and product detail pages to orient users in the deep SKU tree.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; search expands to full width below logo row; promo-bar truncates to icon + short label; compatibility tables scroll horizontally; footer collapses to stacked accordions |
| Tablet | 744–1128px | Two-column product grid; nav shows logo, search, and cart with category links in a horizontal scroll strip; product card hover states suppressed in favor of persistent add-to-cart button |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with category dropdowns visible; product card hover reveals add-to-cart overlay; compatibility table displays in full inline layout |
| Wide | > 1440px | Content container caps at ~1280px and centers; grid holds at four columns; hero section uses wider aspect ratios with more generous whitespace margins |

### Touch Targets
- All primary and accent buttons: minimum 44×44px
- Quantity stepper buttons: 40px square minimum per control
- Nav links: 44px tap height on mobile
- Product card: entire card surface is tappable on touch devices
- Badge and label elements: 8px invisible padding expansion for tap accuracy
- Search submit icon button: 44×44px minimum

### Collapsing Strategy
- Category navigation collapses to a hamburger icon below 744px, revealing a full-screen slide-in drawer with accordion-style sub-category expansion
- Compatibility tables become horizontally scrollable containers below 744px rather than truncating data
- Footer four-column layout reflows to two-column at tablet, single-column accordion (collapsed by default) at mobile
- Promo-bar text shortens to icon + abbreviated label below 375px viewport width; hides text entirely on very narrow viewports
- Product grid: 4-col desktop → 3-col at 1128px breakpoint → 2-col tablet → 1-col mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact nav bar height not confirmed from extraction; 64px is a visual estimate
- Primary active hex (#0d7265) is a derived approximation — no direct CSS value extracted for hover/active state
- Typography scale assignments (which heading levels use which size/weight) are inferred from Nunito Sans web conventions, not extracted CSS rules
- Exact button border-radius not confirmed; 8px (`{rounded.sm}`) inferred from visual style of Shopify default theme customizations
- Footer background color not directly extracted; #121212 (`{colors.ink}`) assumed from the near-black in the palette
- Lavender (#a89cc8) usage context is unconfirmed — may be a promotional or seasonal accent rather than a core system color
- The pure yellow values (#ffff00, #fffb00) in the extraction appear to be text-highlight or hover-overlay states, not standalone brand colors; the named accent is #fbcd0a
- Baskerville is listed in extracted font stacks but its usage context is unclear — may be a fallback or legacy heading font not actively used in the current theme
- Judge.me review widget webfonts (JudgemeIcons, JudgemeStar) are third-party and outside the native Castle Ink type stack
- Social platform colors (#3b5998, #1da1f2, #dd4b39, #e60023, #0073b1) in the extraction represent footer share-icon fills, not Castle Ink brand tokens
- Canvas white (#ffffff) not directly present in extraction; assumed as the base page background from context
- Hover transition durations and easing curves not extractable; standard 150ms ease assumed
