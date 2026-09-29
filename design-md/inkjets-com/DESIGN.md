---
version: alpha
name: "Inkjets.com"
source_url: "https://www.inkjets.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep teal (#108474) dominates every primary CTA and brand-facing navigation anchor in a product category where every major competitor settles for corporate navy or commodity blue — the distinction is deliberate, reading as precise and confident rather than generically technical. Coral (#e66c41) supplies urgency at promotional moments: sale ribbons, limited-offer alerts, and accent marks on high-priority callouts. Warm amber (#fbcd0a) handles deal highlights and star-rating fills, completing a three-color promotional register that communicates savings without visual noise. Ink tones descend from near-black (#242833) at display headings through working-text gray (#555555) to supporting muted gray at #7b7b7b — exactly the minimum hierarchy needed for pages that carry the densest information load: multi-SKU variant pickers, OEM compatibility tables, and page-yield spec blocks stacked beneath cartridge photography. A lavender accent (#a89cc8) surfaces in loyalty and rewards-program UI, keeping repeat-customer flows visually separated from the standard purchase path without requiring a second brand system. Light-teal washes (#c1e6e6, #edf5f5) carry primary chromatic identity through feature strips and compatibility-confirmation banners that do not host a colored CTA. Nunito Sans drives the type system — a rounded, geometrically open sans-serif that keeps product-dense pages legible without the industrial coldness of the Roboto fallback. Compatibility pills and savings tags resolve to {rounded.full}; product cards and input fields use {rounded.sm} throughout. The white canvas — #ffffff card surfaces over #f9fafb page backgrounds — ensures that OEM cartridge artwork from HP, Canon, and Epson reads without color interference from surrounding UI chrome.

colors:
  primary: "#108474"
  primary-active: "#0b6259"
  primary-disabled: "#8ec7bf"
  primary-light: "#c1e6e6"
  primary-surface: "#edf5f5"
  accent: "#e66c41"
  accent-active: "#c4522b"
  deal: "#fbcd0a"
  on-deal: "#121212"
  lavender: "#a89cc8"
  sky: "#00bbf7"
  error: "#dd0000"
  ink: "#242833"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  surface-muted: "#f5f5f5"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Roboto, Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  price-sm:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  nav-top:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Nunito Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-deal:
    backgroundColor: "{colors.deal}"
    textColor: "{colors.on-deal}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-sm-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 6px 14px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  nav-utility-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-top}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline-soft}"
    height: 64px
    logoMaxHeight: 40px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    submitBackground: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
    height: 46px
    width: "100%"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageBgColor: "{colors.surface-muted}"
    imageRounded: "{rounded.xs}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 320px
    ctaBackground: "{colors.deal}"
    ctaTextColor: "{colors.on-deal}"
    ctaTypography: "{typography.button-md}"
    accentStripe: "{colors.primary-light}"
  savings-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  deal-badge:
    backgroundColor: "{colors.deal}"
    textColor: "{colors.on-deal}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  compatibility-tag:
    backgroundColor: "{colors.primary-surface}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    border: "1px solid {colors.primary-light}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  ink-type-badge-oem:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  ink-type-badge-compatible:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  ink-type-badge-reman:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  category-tab-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  category-tab-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid transparent"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.body}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary-light}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} 0"
---

## Components

### Buttons

**`button-primary`** — Teal (#108474) fill on a 44px-tall container with `{rounded.sm}` corners and weight-700 Nunito Sans at 15px. Hover shifts to `{colors.primary-active}` (#0b6259) in place; disabled lightens to `{colors.primary-disabled}` (#8ec7bf) with no opacity hack. This button carries every primary in-page CTA: "Add to Cart," "Find My Cartridges," and search submission.

**`button-secondary`** — White canvas with a 2px teal border and teal text; matches the primary button's 44px height and padding so the two align cleanly in side-by-side layouts. Used for secondary actions: "Compare," "View All Compatible Models," and "Back to Results."

**`button-deal`** — Amber (#fbcd0a) fill with near-black `{colors.on-deal}` text; same geometry as button-primary. Reserved for promotional landing pages and flash-sale CTAs where teal would not signal urgency differentiation against a teal hero background.

**`button-sm-ghost`** — 32px-tall ghost button with a 1px teal border; used for secondary in-card actions like "Quick View" or "Add to Wishlist" that must fit inside a product card's tight padding without visual dominance.

### Search Bar

**`search-bar`** — Full-width input with a teal submit button functioning as a styled inline suffix. The input takes `{rounded.xs}` on the left corners; the submit button closes the right corners, producing a compound capsule without a wrapper border. Placeholder text runs at `{colors.muted-soft}` (#888888). On mobile the search bar drops below the logo row into a full-width strip; on tablet and desktop it lives in the center of the nav bar.

### Navigation

**`nav-utility-bar`** — A 36px teal (#108474) strip sitting above the main nav; hosts shipping-threshold copy, phone number, account links, and trust markers in white `{typography.nav-top}` text. This is the first element sighted on page load, establishing the primary brand color before the logo renders.

**`nav-bar`** — White canvas, 64px tall, with a 1px `{colors.hairline-soft}` bottom border. Logo anchors left; search bar occupies the center region; account, cart, and help icons sit right. Category links occupy a second row on desktop and collapse into a hamburger drawer below 744px.

### Product Card

**`product-card`** — White surface with 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners. The image zone uses `{colors.surface-muted}` background to isolate cartridge photography from the card surface. Title runs `{typography.title-md}` in `{colors.ink}`; price runs `{typography.price-display}`; spec text (page yield, compatible models, ink volume) runs `{typography.body-sm}` in `{colors.muted}`. Savings and ink-type badges stack in the upper-left corner of the image zone. An "Add to Cart" button-primary spans full card width at the bottom.

### Hero Banner

**`hero-banner`** — Full-width teal (#108474) background with white heading at `{typography.display-xl}` and an amber `{colors.deal}` CTA button to create readable contrast against the teal field. A `{colors.primary-light}` (#c1e6e6) accent stripe can texture the right side without breaking the monochrome field. Minimum height 320px on desktop; collapses to a stacked text-above-image layout on mobile.

### Badges and Tags

**`savings-badge`** — Coral (#e66c41) pill with white uppercase text at `{typography.badge}` and `{rounded.full}` shape. Communicates percentage or dollar savings on promotion-eligible SKUs; sits in the product card image corner and in search results.

**`deal-badge`** — Amber (#fbcd0a) pill with near-black text; same geometry as savings-badge. Used for "Best Value," "Bundle Deal," and non-percentage promotions where the coral accent would misread as a simple discount signal.

**`compatibility-tag`** — Light-teal surface (`{colors.primary-surface}`) with teal text and a teal border; `{rounded.full}` pill shape. Labels printer model compatibility — e.g., "HP OfficeJet Pro 9015e" — and stacks horizontally below a product title in PDP layouts.

**`ink-type-badge-oem`** / **`ink-type-badge-compatible`** / **`ink-type-badge-reman`** — Three flat `{rounded.xs}` labels that classify cartridge origin: near-black (#242833) for OEM originals, teal (#108474) for compatible third-party new, lavender (#a89cc8) for remanufactured. These appear in the product card image corner and alongside product titles in list views, letting buyers filter by type at a glance.

### Category Tabs

**`category-tab-active`** — White background with teal text and a 2px teal bottom border; no fill change so the tab strip adds zero visual weight to an already-dense product grid. The underline alone indicates selection state.

**`category-tab-inactive`** — Identical structure to active, but text is `{colors.body}` and the bottom border is transparent. Hover darkens text toward `{colors.ink}` without adding a border.

### Trust Strip

**`trust-strip`** — `{colors.surface-soft}` background with teal icon glyphs and gray body text across a 4-column icon-and-label grid. Carries compatibility guarantee, free shipping threshold, secure checkout, and return policy. The teal icons reinforce the primary color without adding a CTA. Sits directly below the hero banner or nav, above the product grid.

### Footer

**`footer`** — Near-black (#242833) background with a 4px teal top border as the primary brand signal entering the footer zone. Column headings in `{typography.title-sm}` white; links in `{colors.primary-light}` (#c1e6e6) for legibility against dark. Social-sharing icons appear at small mark scale in their native platform colors — Facebook #3b5998, Twitter #1da1f2 — functioning as affordances, not brand vocabulary.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar drops below logo into full-width strip; nav collapses to hamburger drawer; hero stacks text above image; trust strip becomes 2×2 grid |
| Tablet | 744–1128px | 2-column product grid; search bar remains in nav center; filter panel becomes a top-filter drawer; hero shows text left, image right |
| Desktop | 1128–1440px | 3–4 column product grid; left-sidebar filter panel available; full category mega-menu on nav hover; utility bar visible |
| Wide | > 1440px | Content capped at ~1440px max-width with auto margins; product grid holds at 4 columns; hero background extends edge-to-edge while text container stays constrained |

### Touch Targets
- All primary buttons minimum 44px tall on touch viewports
- Cart, account, and hamburger icons minimum 44×44px tap target
- Compatibility tags are display-only on mobile; no tap-target requirement
- Add-to-cart and search submit are highest-priority touch targets — never let adjacent elements shrink them below 44px

### Collapsing Strategy
- Category mega-menu collapses to a hamburger drawer with nested accordion at < 744px
- Filter sidebar converts to a bottom-sheet modal on mobile, triggered by a sticky "Filters" chip above the grid
- Product card titles clamp to 2 lines on mobile to preserve image-to-info ratio
- Trust strip collapses from 4-column row to 2×2 grid on mobile
- Nav utility bar hides on mobile; its content (phone, account) moves into the hamburger drawer

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; browser chrome color on mobile cannot be confirmed
- Exact Nunito Sans weight subset (300/400/600/700/800) not confirmed from extraction; 400/600/700 assumed as most common web deployment
- The last five extracted hex values (#3b5998, #1da1f2, #dd4b39, #e60023, #0073b1) are Facebook, Twitter, Google, Pinterest, and LinkedIn platform colors — they are social-sharing widget colors, not Inkjets.com design tokens
- Baskerville found in font-stack extraction but no evidence it appears in primary product UI; possibly a vendor widget or legacy element — excluded from typography system
- Animation timing, easing curves, and transition durations not extractable from static analysis
- Exact container max-width and grid gutter widths not confirmed
- Lavender (#a89cc8) context is presumed loyalty/rewards UI based on color character; actual usage context unverified
- Mega-menu layout, hover states, and dropdown structure not visible from static extraction
- Dark-mode or high-contrast variant: no evidence found in extraction; assumed absent
