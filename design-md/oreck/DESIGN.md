---
version: alpha
name: "Oreck"
source_url: "https://www.oreck.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The #2585a4 teal Oreck uses as its primary does not decorate — it certifies. The hue sits in the register of water-filtration system labels and HEPA certification marks, and on a vacuum brand homepage it does exactly the work it looks like it should do: signals that the machine on the other side of the transaction will remove what you cannot see. Montserrat carries every word at weights that default heavy — 600 and 700 feel structural here, not emphatic — giving the brand an assertive, unambiguous cadence suited to a company whose legacy is built on engineering one lighter machine than everyone else. Behind the teal the palette is almost entirely achromatic: `{colors.surface-soft}` (#f3f5f6) and `{colors.surface-card}` (#f3f3f3) alternate as page canvas and card surface, with `{colors.hairline}` (#dedede) and `{colors.hairline-soft}` (#d9d9d9) handling dividers at sub-pixel-feeling weights. Ink descends through four near-blacks — #121212, #231f20, #242833, #4f4c4d — differentiating headline from body from subtext from muted label without pulling any warm or cool tint into the neutral register. A second blue, `{colors.secondary}` (#334fb4), surfaces only in sale badges and promotional chips: brighter, more saturated, unapologetically referential to discount-blue conventions. It is kept completely separate from the primary so that price urgency and product trust never share a color. Buttons use `{rounded.sm}` rather than pill shapes — the interface is functional, not playful. Product images render with `object-fit: contain` against white image zones, respecting the product silhouette the way a catalog would. Spacing between page sections is generous, while card interiors are tight, echoing the physical proposition of the product: engineered density inside, open air around it.

colors:
  primary: "#2585a4"
  primary-active: "#1a6e8a"
  primary-disabled: "#a8d4e2"
  secondary: "#334fb4"
  secondary-active: "#2940a0"
  ink: "#121212"
  body: "#242833"
  muted: "#4f4c4d"
  muted-soft: "#333f48"
  hairline: "#dedede"
  hairline-soft: "#d9d9d9"
  canvas: "#ffffff"
  surface-soft: "#f3f5f6"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  label-caps:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-strike:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through

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
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 40px
    scrollShadow: "0 2px 8px rgba(0,0,0,0.08)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 44px
    iconColor: "{colors.muted}"
    iconColorFocus: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageFit: contain
    imageBackground: "{colors.canvas}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    strikePriceTypography: "{typography.price-strike}"
    strikePriceColor: "{colors.muted}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    minHeight: 480px
    ctaBackgroundColor: "{colors.canvas}"
    ctaTextColor: "{colors.primary}"
    ctaRounded: "{rounded.sm}"
  promotion-strip:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    height: 36px
    padding: 0 {spacing.base}
  sale-badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
    gap: "{spacing.sm}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    chipBackgroundColor: "{colors.surface-card}"
    chipBackgroundColorActive: "{colors.primary}"
    chipTextColor: "{colors.body}"
    chipTextColorActive: "{colors.on-primary}"
    chipTypography: "{typography.button-sm}"
    chipRounded: "{rounded.full}"
    chipPadding: 6px 14px
    chipHeight: 36px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-soft}"
    headingTypography: "{typography.label-caps}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
    columnGap: "{spacing.xxl}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Solid #2585a4 teal fill, 48px tall, 8px radius (`{rounded.sm}`), Montserrat SemiBold 15px with 0.3px tracking. Handles all primary CTAs: "Add to Cart", "Shop Now", "Find a Dealer". On hover it shifts to `{colors.primary-active}` (#1a6e8a); the disabled state bleaches to `{colors.primary-disabled}` (#a8d4e2) with `cursor: not-allowed`. No drop shadow — the color is the signal, not the depth.

**`button-secondary`** — White canvas background with a 1.5px teal border and teal text, matching primary height and radius exactly. Border and text color both shift to `{colors.primary-active}` on hover. Used for "Learn More", "Compare", or modal secondary actions where the primary CTA is already occupied above the fold.

**`button-ghost`** — Transparent background, `{colors.ink}` text, no border. Used for "View All" section header links and accordion toggles. Its low visual weight keeps section chrome recessive when a product grid is the real destination.

### Text Inputs

**`text-input`** — White canvas background, 1px `{colors.hairline}` border resting, stepping to 1.5px `{colors.primary}` teal on focus. 48px tall, `{rounded.sm}` (8px), Montserrat Regular 16px. Placeholder in `{colors.muted}` (#4f4c4d). Error state border color is not extractable from current data — see Known Gaps.

### Navigation

**`nav-bar`** — 64px white bar pinned at top, divided from page content by a single 1px `{colors.hairline}` line. Logo left at 40px max height. Category links render in `{typography.nav-link}` (Montserrat 600/13px, 0.1px tracking) in a horizontal list center or right of logo. Search icon and cart counter with item badge float to the far right. On scroll past approximately 40px, an 8px box shadow (`rgba(0,0,0,0.08)`) appears beneath the bar. Above the nav bar, a `{components.promotion-strip}` in `{colors.secondary}` (#334fb4) carries site-wide sale messaging in ALL-CAPS `{typography.label-caps}`.

**`search-bar`** — A 44px `{rounded.sm}` field with `{colors.surface-soft}` (#f3f5f6) background — visually recessed relative to the white nav — with a magnifying glass icon in `{colors.muted}` that shifts to `{colors.primary}` on focus. On mobile it drops into its own row beneath the nav bar; on desktop it collapses to an icon that expands to a full-width overlay on click.

### Product Card

**`product-card`** — `{colors.surface-card}` (#f3f3f3) ground with `{rounded.sm}` and no visible border. Image zone is white canvas with `object-fit: contain` so the product silhouette is preserved without cropping — particularly important for vacuum shapes that are tall and narrow against wide aspect ratios. Title in `{typography.title-sm}` (Montserrat 600/16px), current price in `{typography.price-display}` (700/24px, teal not used — price stays in `{colors.ink}`), strikethrough price in `{typography.price-strike}` (400/18px) in `{colors.muted}`. A `{components.sale-badge}` in `{colors.secondary}` overlays the image corner absolutely when a product is on promotion. Card padding is a uniform `{spacing.base}` (16px) with `{spacing.sm}` (8px) vertical gap between title, price, and CTA button.

### Hero Banner

**`hero-banner`** — Full-width section, `{colors.primary}` (#2585a4) teal background. Headline in `{typography.display-xl}` (Montserrat 800/48px) and subline in `{typography.body-md}` (400/16px), both `{colors.on-primary}` white. The CTA button inside the hero inverts: white background (`{colors.canvas}`), teal text (`{colors.primary}`), `{rounded.sm}` — avoiding a white-on-white ghost or a primary-on-primary merger. Minimum height 480px with `{spacing.xxl}` (48px) vertical padding; on mobile the layout stacks to text above, product image below, min-height drops to 320px.

### Sale Badge & Promotion Strip

**`sale-badge`** — `{colors.secondary}` (#334fb4) chip in the top-left corner of a product card image, 4px radius (`{rounded.xs}`), `{typography.label-caps}` (ALL-CAPS Montserrat 700/11px, 0.8px tracking). Carries percent-off or "SALE" copy only — never product specifications. **`promotion-strip`** is the same #334fb4 applied to a 36px full-width bar above the nav for site-wide announcements. Both uses of #334fb4 are kept completely distinct from the primary `{colors.primary}` teal so that promotional urgency and brand trust never share a color.

### Trust Badges

**`trust-badge`** — A `{colors.surface-soft}` (#f3f5f6) container with `{rounded.sm}`, an icon rendered in `{colors.primary}` teal beside a single line of `{typography.caption}` text. Used in a horizontal strip between the hero and the first product grid to surface warranty length, HEPA certification, free shipping threshold, and return window. The teal icon color ties the trust claims back to the primary brand signal without a redundant button.

### Filter Bar

**`filter-bar`** — A sticky row below the breadcrumb on collection pages. Inactive chips: `{colors.surface-card}` background, `{colors.body}` text, `{rounded.full}` pill radius (9999px), 36px height. Active chips: `{colors.primary}` background, `{colors.on-primary}` white text. The `{rounded.full}` pill shape is a deliberate contrast to the `{rounded.sm}` rectangles used on cards and buttons, creating a visual separation between navigation-layer controls and product-layer content.

### Breadcrumb

**`breadcrumb`** — Single-line text path in `{typography.caption}` (12px). Inactive ancestors in `{colors.muted}`, current page in `{colors.ink}`. Slash separator in `{colors.hairline}`. Sits above the page title and filter bar, below the nav bar, in all collection and product detail pages.

### Footer

**`footer`** — `{colors.body}` (#242833) dark band topped with a 3px `{colors.primary}` teal accent rule. Column headings in `{typography.label-caps}` (ALL-CAPS 700/11px, 0.8px tracking) at `{colors.on-dark}`; links in `{typography.body-sm}` (400/14px) at `{colors.surface-soft}` (#f3f5f6). Four-column desktop grid with `{spacing.xxl}` (48px) column gap collapses to a single-column accordion at mobile. The teal top rule ties the footer back to the primary brand signal in an otherwise fully dark context.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search bar drops below nav into its own full-width row; nav collapses to hamburger + centered logo + cart icon; hero headline drops to `display-md` (32px/700); hero min-height 320px with image below text; footer columns collapse to stacked accordions |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories in horizontally scrollable strip below logo row; filter bar chips scroll horizontally without wrapping; hero runs text-left, image-right at 50/50 split |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with dropdown mega-menus on hover; hero at full `display-xl` (48px/800) with image pane beside copy; filter bar may switch to sticky left-sidebar layout |
| Wide | > 1440px | Content capped at 1440px with auto side margins; four-column product grid; hero background extends edge-to-edge while content stays within 1280px max; nav logo and links scale up by 4px |

### Touch Targets

- All interactive controls minimum 44px height on mobile
- Filter chips minimum 36px height with `{spacing.sm}` (8px) gap between adjacent chips
- Nav hamburger tap area padded to 44×44px regardless of visual icon dimensions
- Cart, search, and account icons padded to 44px tap target via negative margins or pseudo-element expansion
- Product card acts as a single large tap target; internal CTA button remains visible for explicit intent

### Collapsing Strategy

- Hero: stacked (text above, image below) on mobile; side-by-side 50/50 on tablet and desktop
- Navigation: full horizontal menu with dropdowns at 1128px+; hybrid (top 3 categories visible + hamburger overflow) at 744–1128px; full hamburger drawer below 744px
- Footer: 4-column grid → 2-column grid at tablet → single-column tap-to-expand accordion at mobile
- Product grid: 1 → 2 → 3 → 4 columns across mobile / tablet / desktop / wide breakpoints
- Filter bar: horizontal scroll strip pinned below breadcrumb on mobile and tablet; optional sticky left sidebar at desktop 1128px+
- Promotion strip: full copy on desktop; truncates to single-line marquee or hides least-priority message on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was extracted; nav bar drop-shadow on scroll behavior is inferred from common Shopify patterns, not confirmed
- `primary-active` (#1a6e8a) and `primary-disabled` (#a8d4e2) are derived by adjusting lightness from `{colors.primary}` — not directly extracted from the live site
- Form validation error state colors (typically a red) were absent from the extracted palette and are not defined in this spec
- Hover underline behavior on text links and nav items is assumed; confirmed only that `{colors.primary}` is used for focus rings on inputs
- Exact button border-radius is inferred at 8px (`{rounded.sm}`); the live site may use 4px or 6px
- No custom icon set was identified — likely a bundled Shopify theme sprite (Dawn or similar) or Feather Icons
- Animation and transition timing data (hover fade duration, drawer slide speed, carousel interval) not extractable from static hints
- Product image aspect ratio per card not confirmed; `object-fit: contain` is inferred from the `object-fit: contain` string found in the font-stack extraction artifact
- Exact nav bar height and promotion strip height are estimated from typical Shopify Montserrat theme patterns; pixel measurements were not extracted
