---
version: alpha
name: "Halios"
source_url: "https://www.haliosbrand.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every Halios watch ships without a retail partner between maker and buyer — Jason Lim's Vancouver studio closes the loop at checkout, which means the site itself must carry the full freight of brand trust. The UI answers that pressure through subtraction: a deep navy estimated at #12203a anchors hero sections the way a matte dial anchors a finished case, while an off-white canvas (#f7f5f2) provides the reading surface for product descriptions written with the economy of a spec sheet. No accent color competes for attention; `{rounded.none}` rules every interactive element — buttons, inputs, cards — because sharp corners signal that this object is not trying to be friendly, it is trying to be precise. Typography runs at light weights (300–400) in a clean geometric sans, sized modestly: headlines at 48px in the display tier feel unhurried rather than monumental. Product names appear in uppercase with tracked spacing (`{typography.model-name}`, 1px letter-spacing) above price figures at weight 300, an arrangement that reads like a catalogue entry rather than a retail pitch. The collection grid is strictly two-column with generous gutters, uniform card proportions, and no hover-overlay commerce tricks — clicking is the only affordance offered. Waitlist states, which appear frequently given the brand's limited-run production model, are rendered as muted off-white blocks that keep the page layout intact while communicating scarcity without urgency theater. The footer repeats the navy from the hero, closing the page as a visual bracket. Navigation holds fewer than five items; the absence of a search field suggests a catalog small enough to browse in two scrolls. Release windows and drop dates occasionally appear as a slim announcement bar above the nav — the only moment the brand allows itself to break the silence. Every decision reads as deliberate economy: fewer things, without ornament, communicate the quality of the object more reliably than any amount of styling.

colors:
  primary: "#12203a"
  primary-active: "#0a1628"
  primary-disabled: "#8a9ab5"
  ink: "#12203a"
  body: "#2d3a4a"
  muted: "#6b7a8d"
  hairline: "#d8dde5"
  canvas: "#f7f5f2"
  surface-soft: "#eeede9"
  surface-card: "#ffffff"
  on-primary: "#f7f5f2"
  accent-steel: "#9ba8b5"
  waitlist-bg: "#eef0f3"
  waitlist-text: "#8a9ab5"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.25px
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1
    letterSpacing: 0
  model-name:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  announcement:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.25px
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.75px
    textTransform: uppercase

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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderColor: "{colors.primary}"
    borderWidth: 1px
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-waitlist:
    backgroundColor: "{colors.waitlist-bg}"
    textColor: "{colors.waitlist-text}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
    cursor: not-allowed
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottomColor: "{colors.hairline}"
    borderBottomWidth: 1px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement}"
    padding: 10px 0
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageSizing: cover
    imageAspectRatio: "4/3"
    gap: "{spacing.sm}"
  product-model-label:
    textColor: "{colors.muted}"
    typography: "{typography.model-name}"
    marginBottom: "{spacing.xs}"
  product-price:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  waitlist-badge:
    backgroundColor: "{colors.waitlist-bg}"
    textColor: "{colors.waitlist-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 10px
    display: inline-block
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    minHeight: 80vh
    padding: "{spacing.section} {spacing.xl}"
  collection-grid:
    columns: 2
    columnsMobile: 1
    gap: "{spacing.xl}"
    padding: "{spacing.section} {spacing.xl}"
  detail-spec-table:
    borderColor: "{colors.hairline}"
    labelColor: "{colors.muted}"
    labelTypography: "{typography.spec-label}"
    valueColor: "{colors.ink}"
    valueTypography: "{typography.body-sm}"
    rowPadding: "{spacing.sm} 0"
    borderBottomWidth: 1px
  email-capture:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl} {spacing.lg}"
    inputTypography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.accent-steel}"
    padding: "{spacing.section} {spacing.xl}"
    columns: 3
  mobile-nav-drawer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    linkSpacing: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — Square-cornered (`{rounded.none}`), 48px tall, deep navy block with off-white label at `{typography.button-md}` weight 500 and 0.5px tracking. Hover darkens to `{colors.primary-active}`; no scale or shadow transformation. The absence of rounding is not an omission — it's the primary visual statement that this brand makes no attempt at softness.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` border, matching height and padding to `button-primary` for flush side-by-side pairing on product detail pages. Hover fills to navy; the border dissolves into the background.

**`button-waitlist`** — A muted, visually non-interactive block in `{colors.waitlist-bg}` with `{colors.waitlist-text}` label. Cursor is `not-allowed`. The shape and size match `button-primary` so the page layout does not shift when stock status changes — only color signals the state.

### Nav Bar
**`nav-bar`** — 64px bar on `{colors.canvas}`, separated from page content by a single `{colors.hairline}` line. Logo marks the left; a compact link list (Collections, About, Journal, Contact) anchors the right in `{typography.nav-link}`. No utility icon cluster, no persistent cart count. On mobile, links collapse to a full-screen `mobile-nav-drawer` in `{colors.primary}` with `{colors.on-primary}` text.

### Announcement Bar
**`announcement-bar`** — A slim full-width strip in `{colors.primary}` that sits above the nav bar during active release windows. `{typography.announcement}` centered white text states the drop date or restock timing with no decoration. Not dismissible during active sale periods; removed entirely between releases rather than left as empty space.

### Product Card
**`product-card`** — No rounded corners, no drop shadows, no hover overlays. Product photograph at a fixed `4/3` aspect ratio fills the card top. Below: `product-model-label` in `{typography.model-name}` uppercase tracked text, then price in `{typography.price}` weight 300. Sold-out models show `waitlist-badge` in place of the price or beneath it. The entire card surface is the tap/click target — no separate "view" CTA.

### Hero
**`hero`** — Full-bleed navy block at minimum 80vh. Headline in `{typography.display-xl}` weight 300, `{colors.on-primary}`. Halios typically presents a single, centered or left-aligned product photograph against the dark background with copy in a separate zone — no text overlaid on image. No carousel, no autoplay. The composition holds as a still object.

### Collection Grid
**`collection-grid`** — Two columns on desktop, single column on mobile, `{spacing.xl}` gap, strict uniform aspect ratios. A section heading in `{typography.display-md}` weight 300 sits above the grid with `{spacing.section}` top padding. No masonry, no featured-large cards breaking the rhythm.

### Detail Spec Table
**`detail-spec-table`** — Technical specifications rendered as a two-column definition list: label in `{typography.spec-label}` (uppercase, tracked, `{colors.muted}`), value in `{typography.body-sm}` (`{colors.ink}`). Rows separated by 1px `{colors.hairline}` lines. Case diameter, lug-to-lug, lug width, case thickness, water resistance, crystal, movement caliber — listed without editorial framing. This component carries the most information density on the site and is deliberately styled to feel like a datasheet, not a feature list.

### Email Capture / Waitlist
**`email-capture`** — A `{colors.surface-soft}` container with a single `text-input` and `button-primary` in an inline row on desktop, stacked on mobile. Label copy is short: "Join the waitlist" or "Get notified." No social proof counts, no discount incentive, no checkbox array. The component appears on sold-out product pages and as a standalone section between collection grids during dry periods.

### Footer
**`footer`** — Full-width navy block mirroring the hero's `{colors.primary}`. Three columns: Collections, Company, and Contact. Navigation links render in `{colors.accent-steel}`, evoking the steel case material. Body text in `{colors.on-primary}`. No newsletter re-ask nested in the footer; no social icon row. The visual bracket between hero and footer encloses the page in the same dark tone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to full-screen drawer in `{colors.primary}`; hero headline drops to `{typography.display-md}`; spec table stacks to full-width label-above-value pairs; email capture stacks input above button |
| Tablet | 744–1128px | Two-column grid maintained; nav links visible if horizontal space permits; hero remains full-bleed with reduced padding |
| Desktop | 1128–1440px | Standard two-column collection grid; content container max-width ~1100px centered; full nav expanded; spec table in two columns |
| Wide | > 1440px | Container holds at ~1200px; surplus width absorbed as equal side margins; no additional grid columns added |

### Touch Targets
- All buttons minimum 48px height
- Nav hamburger tap area minimum 44×44px
- Product card entire surface is tappable — no micro "view" target
- Text inputs 48px height on mobile
- Footer links minimum 36px vertical hit area with padding

### Collapsing Strategy
- Nav collapses to full-screen overlay drawer on mobile; dark navy fill, off-white links, close icon top-right
- Spec table retains two-column layout to 480px; below that stacks to label above value with `{spacing.sm}` separation
- Hero switches from side-by-side image/text composition to image-above, text-below stacking on mobile
- Footer three-column layout collapses to single accordion-style column on mobile, each section toggleable
- Announcement bar text truncates with ellipsis below 375px if copy exceeds one line; never wraps to two lines

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (likely JS-rendered or anti-bot protected); all color values above are estimates derived from visual brand knowledge of haliosbrand.com and should be verified against production CSS before use
- No font families were extracted; the typography stack above defaults to Helvetica Neue as a plausible match for the brand's minimal sans aesthetic — whether a custom webfont (e.g. loaded via Adobe Fonts or a self-hosted WOFF2) is actually served is unknown
- Exact button and input border-radius values unconfirmed; sharp/zero-radius corners are inferred from visual inspection, not measured
- Specific spacing scale not extracted; values follow a standard 8px-base grid that matches observed visual rhythm
- Mobile nav drawer animation curve and overlay opacity not specified
- Product detail image gallery behavior (zoom on tap, swipe gallery, lightbox) not captured
- Any seasonal or colorway-specific palette variants (e.g. limited-edition dial color promotions) not documented
- Waitlist confirmation flow states (success message, duplicate-email handling) not captured
- Whether the brand uses any motion/animation tokens (transition durations, easing) is unknown — the site appears largely static
