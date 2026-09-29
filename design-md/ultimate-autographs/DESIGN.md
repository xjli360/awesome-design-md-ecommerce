---
version: alpha
name: "Ultimate Autographs"
source_url: "https://ultimateautographs.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Gold on black is the language of trophies, championship rings, and sealed-pack foil — Ultimate Autographs builds its entire dark-mode interface from exactly this grammar, pressing #fec000 amber-gold against a #121212 canvas that never wavers into a light-mode variant. Four distinct dark-surface tiers — canvas (#121212), surface-soft (#18181a), surface-card (#2b2b2c), surface-raised (#343436) — give product cards and break-slot panels the dimensional lift of a glass display case without deploying drop shadows or hard borders as structural scaffolding; the depth is entirely chromatic. A second gold register, antique #d4af37, handles hover states and embellishment accents that signal collectibility rather than commodity retail; a brighter electric variant #f4d00e appears in spotlight moments where warmth must not soften into amber. Inter carries all type at compressed tracking — display headlines punch at 800 weight and −0.5px letter-spacing while body copy settles to 400 weight in #b4b4b8, a deliberate contrast that keeps the information hierarchy legible under live-break energy without competing with the gold for visual authority. The box-break model — live group openings of sealed sports-card packs, participants owning team or random slots — shapes the UI well beyond a standard Shopify storefront: countdown timers, LIVE badges, team-slot grids, and Swiper-powered hit carousels all demand real-time visual signals inside a commerce flow. The primary badge vocabulary is {rounded.full} amber-gold on dark surface, sharp enough to read across a streamed broadcast and immediate enough to convert a collector mid-scroll. Buttons take a minimal {rounded.xs} radius rather than pill shapes, signaling precision over approachability — these are serious hobbyists running valuations in their heads, not casual impulse buyers. Product cards float on {colors.surface-card} with gold price text and sport-category pills that fire from neutral surface-raised state to full #fec000 fill on activation, making filter navigation feel as decisive as a scoreboard flip. No gradients or photographic overlays introduce atmospheric noise — the brand's entire mood comes from darkness-level differentiation and the high-contrast gold flash on interaction.

colors:
  primary: "#fec000"
  primary-active: "#d4af37"
  primary-disabled: "#635200"
  gold-alt: "#f4d00e"
  gold-antique: "#d4af37"
  ink: "#dedede"
  body: "#b4b4b8"
  muted: "#757575"
  muted-light: "#c7c7c7"
  hairline: "#343436"
  hairline-soft: "#343333"
  canvas: "#121212"
  surface-soft: "#18181a"
  surface-card: "#2b2b2c"
  surface-raised: "#343436"
  on-primary: "#18181a"
  link: "#007aff"

typography:
  display-xl:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 40px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.15px
  label-upper:
    fontFamily: "Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "Inter, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  countdown-digit:
    fontFamily: "Inter, sans-serif"
    fontSize: 32px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -0.5px
  button-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    border: "1px solid {colors.primary}"
    textColor: "{colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    borderBottom: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoAccentColor: "{colors.primary}"
    height: 64px
    padding: 0 24px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.primary}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: 12px
    imageAspectRatio: "1/1"
    imageRounded: "{rounded.xs}"
    hoverBorder: "1px solid {colors.hairline-soft}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.label-upper}"
    badgeRounded: "{rounded.full}"
  break-slot-card:
    backgroundColor: "{colors.surface-card}"
    borderLeft: "3px solid {colors.primary}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.body-sm}"
    metaColor: "{colors.body}"
    soldOutTextColor: "{colors.muted}"
    availableAccentColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px
  live-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: 4px 10px
    dotColor: "{colors.on-primary}"
  countdown-timer:
    backgroundColor: "{colors.surface-raised}"
    digitColor: "{colors.primary}"
    digitTypography: "{typography.countdown-digit}"
    separatorColor: "{colors.muted}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  hit-showcase-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.gold-antique}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: 8px
    imageAspectRatio: "3/4"
    imageRounded: "{rounded.xs}"
  sport-category-pill:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.body}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  hero-section:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    overlayGradient: "linear-gradient(to bottom, transparent 40%, {colors.canvas})"
  price-tag:
    textColor: "{colors.primary}"
    typography: "{typography.price}"
  price-tag-sm:
    textColor: "{colors.primary}"
    typography: "{typography.price-sm}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    borderTop: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    padding: 48px 0

## Components

### Buttons

**`button-primary`** — Solid #fec000 amber-gold fill with near-black #18181a text on a 4px-radius block, 44px tall. Hover state deepens to antique #d4af37 to reinforce the warm gold-register hierarchy. Disabled state mutes to dark #635200 fill with #757575 label so the element occupies its layout slot without implying interactability on the dark canvas.

**`button-secondary`** — Transparent background with a 1px `{colors.hairline}` border that transitions to a 1px gold border with `{colors.primary}` text on hover. Used for secondary actions — "Browse All Breaks", "View Schedule" — where visual weight must not compete with the primary gold CTA.

**`button-ghost`** — Text-only in `{colors.primary}` with no border or fill. Reserved for low-hierarchy actions such as "view details", "see more hits", and pagination affordances where adding a bordered box would create visual noise in dense card layouts.

### Inputs

**`text-input`** — `{colors.surface-card}` background with a 1px `{colors.hairline}` border that activates to a 1px gold focus ring. Placeholder text sits at `{colors.muted}`. The dark fill matches the card-surface tier so form fields feel structurally native rather than imported from a light-mode template.

**`search-bar`** — Matches text-input spec exactly with an inset magnifier icon in `{colors.muted}` that does not reposition on focus. Appears in the top nav and the break-catalog filter row. The icon color lightens to `{colors.body}` on focus to signal active state without adding a secondary accent color.

### Navigation

**`nav-bar`** — `{colors.surface-soft}` background with a 1px `{colors.hairline}` bottom rule, 64px tall. The brand wordmark uses `{colors.primary}` as its accent tone against the dark surface. Nav links use Inter 500 at 14px; the active link underlines in gold rather than using a background fill, keeping the bar visually lean while unambiguously marking the current section.

### Cards

**`product-card`** — Floats on `{colors.surface-card}` with 8px radius and 12px padding. Product title in Inter 600/15px; price in bold 20px `{colors.primary}` gold. Category/condition badges are `{rounded.full}` gold-fill with `{colors.on-primary}` text at 11px uppercase. On hover, the border transitions to `{colors.hairline-soft}` — no box-shadow on the dark canvas, depth comes entirely from the chromatic stack.

**`break-slot-card`** — Represents a single team or random slot in a live break event. Distinguished by a 3px left border in `{colors.primary}` that acts as a gold seam on the dark card face. Title at `{typography.title-md}`, slot metadata (sport, team, date) at `{typography.body-sm}`/`{colors.body}`. Sold-out slots desaturate to `{colors.muted}` text while preserving the card's layout footprint, maintaining the slot grid's visual rhythm.

**`hit-showcase-card`** — Portrait-aspect (3:4) card with a 1px `{colors.gold-antique}` border that reads as a specimen frame or display vault. Used in the hits reel after a break resolves — autograph, relic, and parallel cards surface here. Caption row shows player name, year, and card brand in `{typography.caption}`.

### Live Break UI

**`live-badge`** — `{rounded.full}` #fec000 pill with uppercase 11px/700-weight Inter label. The leading dot pulses at a 1s opacity cycle in `{colors.on-primary}` to mimic a broadcast LIVE indicator. Appears on break-slot listings and on the hero section when a break is actively streaming, giving the storefront a live-event tempo.

**`countdown-timer`** — `{colors.surface-raised}` tile grid with `{typography.countdown-digit}` digit pairs in `{colors.primary}` and colon separators in `{colors.muted}`. Unit labels (HRS / MIN / SEC) beneath each pair in `{typography.caption}`/`{colors.muted}`. Used on the hero and individual break listings to drive pre-break urgency. On mobile the tiles reflow from a horizontal row to a 2×3 grid to preserve legibility.

### Sport Filter

**`sport-category-pill`** — Inactive state: `{colors.surface-raised}` background, `{colors.body}` text. Active state: full `{colors.primary}` gold fill with `{colors.on-primary}` text. `{rounded.full}` across all states. Arranged in a momentum-scroll horizontal row on mobile, a wrapping flex row on desktop. The activation color change is binary — no halfway tint — so the selected sport reads unambiguously from across a scrolling product grid.

### Hero

**`hero-section`** — Full-bleed dark canvas with a bottom-fade gradient into `{colors.canvas}` so the first product row emerges from the imagery rather than hard-cutting. Headline at `{typography.display-xl}`, sub-text at `{typography.body-md}`/`{colors.body}`, CTA following `button-primary` spec with `{rounded.xs}` radius. On mobile the hero compresses to 60vh and the headline drops to `{typography.display-md}`.

### Pricing

**`price-tag`** — Standalone price display at 20px/700-weight `{colors.primary}` gold. Used in product cards and break-listing headers where the price is the primary conversion signal.

**`price-tag-sm`** — 16px/600-weight variant for metadata contexts — slot pricing within a break grid, secondary line-item prices on the cart page.

### Footer

**`footer`** — `{colors.surface-soft}` with a 1px `{colors.hairline}` top rule, padding 48px vertical. Section headings at `{typography.title-sm}`/`{colors.ink}`, link lists at `{typography.body-sm}`/`{colors.body}`. Link hover fires to `{colors.primary}`. The surface-soft fill keeps the footer anchored within the dark-layering system rather than breaking to true black or a contrasting tone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; sport-category pills scroll horizontally with momentum; nav collapses to hamburger + logo + cart icon; hero compressed to 60vh; countdown timer reflows to 2×3 tile grid |
| Tablet | 744–1128px | 2-column product grid; sport-category pills wrap to 2 rows; break-slot listings go side-by-side; hero at 70vh with CTA left-aligned |
| Desktop | 1128–1440px | 3–4 column product grid; persistent full top nav; countdown timer displays as single horizontal row; hit-showcase Swiper shows 5 cards |
| Wide | > 1440px | Max-width container ~1400px centered on canvas; 4-column product grid; hero background image extends full-bleed beyond the container edge |

### Touch Targets

- All buttons and pills minimum 44px tall to meet WCAG 2.5.5
- Break-slot cards minimum 56px tall on mobile for reliable tap across the full row
- Nav links minimum 44px tap zone via vertical padding that extends beyond the visible 14px label
- Sport-category pills minimum 36px height; horizontal scroll container uses `-webkit-overflow-scrolling: touch` for momentum
- Hit-showcase cards minimum 48px tap zone on the caption row for "view card" action

### Collapsing Strategy

- Nav collapses to hamburger at < 744px; cart and logo always visible
- Hit-showcase Swiper reduces visible slides from 5 (desktop) → 3 (tablet) → 1.2 (mobile, partial bleed signals scroll)
- Countdown timer tiles condense from a horizontal row to a 2×3 grid below 480px rather than reducing font size
- Hero subtext hidden below 400px to preserve headline and CTA without reflow
- Footer link columns collapse from 4-column to 2-column at tablet, single-column at mobile
- Sport-category filter switches from wrapped flex row to horizontal scroll at < 744px to avoid orphaned pills

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom heading or display font detected — Inter is the only font stack present; a decorative or condensed typeface may load via a Shopify theme app or late-binding JS after initial page parse
- Meta theme-color is unset — OS-level browser chrome color (address bar, PWA status bar) is undefined and will default to system behavior
- Animation and motion tokens are unextractable from static inspection — LIVE badge pulse duration, card hover transition timing, and countdown tick animation are undocumented
- Exact nav link active-state underline thickness, offset, and transition duration could not be confirmed from extracted data
- Modal, drawer, and overlay scrim opacity is not present in the extraction — likely a mid-opacity dark overlay on `{colors.canvas}` but unconfirmed
- Icon set source and sizing grid (sport icons, social share icons, cart/bag glyphs) not confirmed — likely inline SVGs bundled with the Shopify theme
- Whether `#007aff` is an intentional brand link color or a residual iOS/WebKit system default is ambiguous; treat with caution and prefer `{colors.primary}` or `{colors.ink}` for interactive text in generated UI
- Shopify-native elements (cart drawer, collection filters sidebar, checkout) will carry framework defaults that may not honor the dark-surface stack — custom CSS overrides required for full fidelity
