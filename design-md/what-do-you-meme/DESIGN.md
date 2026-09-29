---
version: alpha
name: "What Do You Meme?"
source_url: "https://whatdoyoumeme.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A saturated marigold yellow (#ffc617) slams into near-black (#121212) before you even register the page — the visual equivalent of someone shouting the punchline first and letting the setup arrive late. This is a site that treats whitespace the way a party game treats silence: suspiciously, and only in small doses. Typography runs three distinct families deep — Maxx Display for shout-level headlines that borrow from marquee signage, Yellix for body copy with just enough geometric quirk to stay interesting on a product grid, and Maxx Mono for price tags and countdown timers that read like scoreboard tickers. The rounded corners stay tight ({rounded.xs} to {rounded.sm}) across cards and buttons, reinforcing a blocky, sticker-sheet aesthetic rather than the soft pill shapes of wellness DTC. A secondary electric blue (#002ee7) fires on hover states and link text, creating a two-voltage palette — yellow screams, blue clicks. Product cards stack on a pure-black or near-black canvas with bright badge overlays (green #38c172 for "New," blue for "Best Seller"), turning the collection page into something closer to a trading-card binder than a serene e-commerce grid. Navigation is minimal and dark, topped with a persistent announcement bar that frequently pulses promotions in the brand yellow. The overall system trades the muted restraint of lifestyle brands for arcade-cabinet energy: high contrast, dense information, and type that leans forward. Spacing runs tighter than industry norms — {spacing.sm} and {spacing.md} dominate card interiors — because the brand assumes you're scrolling fast and deciding faster.

colors:
  primary: "#ffc617"
  primary-active: "#e6b000"
  primary-disabled: "#ffe88a"
  secondary: "#002ee7"
  secondary-active: "#0022b3"
  ink: "#121212"
  ink-soft: "#232323"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#aeaeae"
  hairline: "#dedede"
  hairline-soft: "#dae1e7"
  canvas: "#ffffff"
  canvas-dark: "#121212"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  surface-card-dark: "#191919"
  surface-mid: "#c5c5c5"
  on-primary: "#121212"
  on-dark: "#ffffff"
  on-secondary: "#ffffff"
  success: "#38c172"
  accent-blue: "#2f70ee"
  accent-blue-light: "#dcebfc"
  nav-muted: "#606f7b"
  text-dark: "#3d4852"
  text-mid: "#3c3c3c"
  text-secondary: "#5a5a5a"
  badge-blue: "#334fb4"
  link: "#146ff8"

typography:
  display-xl:
    fontFamily: "'Maxx Display', 'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Maxx Display', 'Assistant', sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Maxx Display', 'Assistant', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Maxx Display', 'Assistant', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.2px
  mono-price:
    fontFamily: "'Maxx Mono', monospace"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  mono-sm:
    fontFamily: "'Maxx Mono', monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-lg:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  announcement:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Yellix', 'Assistant', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase

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
  section-lg: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-dark-active:
    backgroundColor: "{colors.text-mid}"
    textColor: "{colors.on-dark}"
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
  text-input-dark:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.text-mid}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement}"
    height: 40px
    padding: 10px 16px
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    imageRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.mono-price}"
    badgeOffset: "{spacing.sm}"
  product-card-dark:
    backgroundColor: "{colors.surface-card-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: 0
    imageRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.mono-price}"
  badge-new:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-bestseller:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-primary
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  hero-banner-yellow:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-dark
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  collection-header:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xl} {spacing.base}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    shadow: "0 4px 24px rgba(0,0,0,0.12)"
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.base}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 420px
    headerTypography: "{typography.display-sm}"
    itemTitleTypography: "{typography.title-sm}"
    itemPriceTypography: "{typography.mono-price}"
    rounded: "{rounded.none}"
  countdown-timer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary}"
    typography: "{typography.mono-price}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  star-rating:
    filledColor: "{colors.primary}"
    emptyColor: "{colors.hairline}"
    size: 16px
  quick-add-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    resultTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

---

## Components

### Buttons

**`button-primary`** — Bold yellow (#ffc617) background with near-black text, uppercase Yellix lettering at 700 weight with tight letter-spacing. Corners are barely softened at `{rounded.xs}` (4px), keeping the shape punchy and blocky. On hover, background darkens to `{colors.primary-active}`; on press, a slight 1px inset shadow appears. Disabled state washes out to `{colors.primary-disabled}` with muted text.

**`button-secondary`** — Transparent fill with a 2px solid ink border. Text matches the border in near-black, uppercase. On hover, the fill inverts to solid black with white text, creating a satisfying snap between empty and full states. Used for secondary CTAs like "View All" on collection rows.

**`button-dark`** — Solid black fill with white text. Deployed on yellow hero backgrounds where the primary button would disappear. Hover lightens the background slightly to `{colors.text-mid}`. Same uppercase typography and 4px radius as all other buttons.

### Navigation

**`nav-bar`** — 64px tall, white background with a thin 1px hairline bottom border. Logo sits left, nav links center or left-aligned in Yellix 600-weight, 14px. Right side holds account icon, cart icon with item count badge, and search trigger. On dark-mode pages (collections, hero zones), the nav swaps to `nav-bar-dark` with a solid #121212 background and white text.

**`announcement-bar`** — A persistent 40px yellow strip above the nav, cycling promotional messages (free shipping thresholds, new launches). Text is 13px Yellix 600 in ink-black. On mobile, text truncates with an ellipsis; on desktop, multiple messages rotate on a timer.

**`mega-menu`** — Drops below nav on hover, full-width white panel with `{spacing.lg}` padding. Category headings use `{typography.title-sm}`, item links use `{typography.body-sm}`. Product thumbnails appear inline for featured collections. No border-radius — it sits flush against the nav.

### Product Cards

**`product-card`** — Square image ratio (1:1) on a light gray (#f3f3f3) background with `{rounded.sm}` corners. Title below in `{typography.title-sm}`, price in `{typography.mono-price}` using Maxx Mono. Badges (New, Best Seller, Sale) float in the top-left with `{spacing.sm}` offset. On hover, a quick-add button slides up from the card bottom. Card has no border or shadow — color contrast alone creates separation.

**`product-card-dark`** — Identical layout but on `{colors.surface-card-dark}` (#191919) background with white text. Used on dark collection pages. Badge colors remain consistent across both variants.

### Badges

**`badge-new`** — Green (#38c172) background, white uppercase text at 11px/700. Padding is tight at 4px 8px with `{rounded.xs}` corners. Positioned absolute, top-left of card image.

**`badge-bestseller`** — Electric blue (#002ee7) background. Same size and positioning pattern as badge-new.

**`badge-sale`** — Yellow (#ffc617) background with black text. Used for percentage-off callouts.

### Hero Sections

**`hero-banner`** — Full-bleed section with dark background (#121212), minimum 480px height. Headline in Maxx Display at 48px/800 weight, subhead in Yellix 16px regular. Primary yellow CTA button anchors the composition. Background images or video fill the section with a dark overlay for text legibility.

**`hero-banner-yellow`** — Inverted energy: full yellow (#ffc617) background with black text. The CTA becomes `button-dark` to maintain contrast. Used for marquee product launches where the yellow acts as the hero's visual shout.

### Collection Header

**`collection-header`** — Dark band at the top of collection pages. Collection name in `{typography.display-lg}` (36px Maxx Display, white). Padding keeps the text breathing at `{spacing.xl}` top/bottom. Optional subtitle in `{typography.body-md}` with reduced opacity.

### Cart & Commerce

**`cart-drawer`** — Slides in from the right at 420px width on desktop. Header uses `{typography.display-sm}` for "Your Cart." Each line item shows a small thumbnail, title in `{typography.title-sm}`, and price in Maxx Mono. Quantity stepper is a simple inline input with ± buttons. Checkout CTA is a full-width `button-primary` pinned to the drawer bottom.

**`countdown-timer`** — Black background with yellow monospace numerals (Maxx Mono, 18px). Used in announcement bars or hero sections for flash sales. Each digit group (HH:MM:SS) sits in its own rounded-xs container with `{spacing.sm}` padding.

### Star Rating

**`star-rating`** — 16px star icons, filled in brand yellow (#ffc617), empty in hairline gray. Displayed inline next to review count text. On product cards, sits below the price.

### Search

**`search-overlay`** — Full-screen or drawer overlay with a prominent text input. Results appear as a vertical list with product thumbnails, title, and price. Background is white with `{rounded.sm}` on the container. Input uses `{typography.body-md}` with an ink-colored placeholder.

### Footer

**`footer`** — Dark (#121212) full-width section. Column layout with link groups headed by `{typography.title-sm}` in white. Links are `{colors.muted-soft}` (#aeaeae) in `{typography.body-sm}`, brightening to white on hover. Bottom row holds payment icons, copyright in `{typography.caption}`, and social media icon links.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-up cards), hamburger nav replaces link row, hero headline drops to `{typography.display-md}` (28px), cart drawer becomes full-screen sheet, announcement bar single-line with marquee scroll |
| Tablet | 744–1128px | 3-column product grid, nav links visible but condensed, hero maintains full height with smaller type (36px), mega-menu becomes accordion inside drawer |
| Desktop | 1128–1440px | 4-column product grid, full mega-menu on hover, hero at designed 48px headline, cart drawer at 420px, two-row footer grid |
| Wide | > 1440px | Content max-width caps at 1440px and centers, product grid may expand to 5-up, additional whitespace in section padding (`{spacing.section-lg}`), hero image scales while text zone stays fixed-width |

### Touch Targets

- All tappable elements minimum 44×44px on mobile
- Product card quick-add button expands to full card-width on touch devices
- Quantity steppers in cart use 44px square hit areas
- Nav hamburger icon padded to 48×48px tap zone
- Badge tap targets inherit card tap (entire card is the link)

### Collapsing Strategy

- Desktop mega-menu collapses to slide-out drawer with accordion sections on mobile/tablet
- Footer columns stack vertically on mobile, two-up on tablet
- Product grid reflows: 4 → 3 → 2 columns as viewport narrows
- Hero dual-column layouts (text + image) stack to single column with image on top at mobile
- Announcement bar trims to single message with horizontal scroll indicator on mobile
- Search overlay shifts from centered modal (desktop) to full-screen takeover (mobile)

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font weights for Maxx Display and Yellix could not be confirmed beyond what is rendered — the site loads these via Shopify's font pipeline and the precise weight map (whether 800 vs 900 for display, etc.) may differ from what is specified here
- Maxx Mono character-width and OpenType features (tabular figures, slashed zero) were not extractable
- Transition/animation timing functions (easing curves for drawer slides, hover badge reveals) are not captured
- Dark mode vs. light mode logic — the site appears to use dark canvas for collection pages and light for PDP/cart, but the switching logic and any user-preference detection are unknown
- Exact shadow values on mega-menu and modal overlays are estimated; the site may use Shopify theme variables that differ
- Icon set (line weight, stroke width, icon grid size) not extracted — the site uses custom SVG icons whose design specs are not available from CSS alone
- Whether Yellix or Assistant serves as the primary body stack could not be definitively ordered from rendered output alone; both appear in font-family declarations
