---
version: alpha
name: "Corteiz"
source_url: "https://crtz.xyz"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The password gate that once guarded crtz.xyz — gone since 2023 but still the most cited design decision in British streetwear — established the entire visual contract before a single product was shown: access is earned, not browsed. That logic persists in the current system. #ffd500 detonates against a #121212 near-black field with a contrast ratio that reads as an alarm signal rather than a brand color; it appears on the announcement bar, countdown numerals, and active size tiles — never on backgrounds, never decoratively. Courier New carries every line of text site-wide, a typeface chosen for what it is not: it has no fashion precedent, no luxury association, no geometric warmth. It prints receipts and error logs. At 56px uppercase it reads like a placard; at 12px it reads like a terminal. The Alcatraz crest — a prison island, rendered white on black — anchors the brand mark, and the design system exists primarily to frame scarcity rather than promote availability. Hairlines at #323232 divide a grid that often has little to divide: sold-out badges outnumber add-to-cart buttons during the minutes following a drop. The palette occupies a narrow band from #121212 to #dedede, five tones in a near-monochrome range with a single voltage color that never gets a second use. No rounded corners of consequence — buttons, cards, inputs, and tiles all sit at `{rounded.none}`, the geometry matching the brand's refusal to soften. Navigation is stripped to logo, cart, and hamburger; the assumption is that visitors arrive via direct link during a drop, not via organic browse. Mobile is the primary surface. Every layout decision — the full-bleed hero, the full-screen cart overlay, the 48px touch targets on size tiles — is optimized for a 90-second checkout window under load.

colors:
  primary: "#ffd500"
  primary-active: "#e6bf00"
  primary-disabled: "#5a4b00"
  ink: "#dedede"
  body: "#dedede"
  muted: "#444444"
  hairline: "#323232"
  canvas: "#121212"
  surface-soft: "#1c1c1c"
  surface-card: "#1e1e1e"
  on-primary: "#121212"
  alcatraz-white: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -1px
    textTransform: uppercase
  display-md:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
    textTransform: uppercase
  body-md:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  mono-price:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0
  countdown:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: -2px
  badge:
    fontFamily: "'Courier New', courier, serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 13px 23px
    height: 48px
  button-sold-out:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
    cursor: not-allowed
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1:1"
    padding: "{spacing.sm}"
    priceTypography: "{typography.mono-price}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    accentColor: "{colors.primary}"
    minHeight: 100svh
    layout: full-bleed
  countdown-timer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.countdown}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    layout: 4-column row
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-badge-sold-out:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-badge-live:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    unavailableTextColor: "{colors.muted}"
    height: 48px
    minWidth: 48px
  cart-drawer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    checkoutButtonColor: "{colors.primary}"
    checkoutButtonText: "{colors.on-primary}"
  password-gate:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    layout: centered
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.base}"
    legalTypography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — #ffd500 fill with #121212 label text in 14px uppercase Courier New at 1.5px letter-spacing. The `{rounded.none}` geometry is deliberately uncompromising — no softness, no radius, the button shape is a rectangle. Active state pulls back to `{colors.primary-active}` (#e6bf00); disabled collapses to a near-invisible olive fill (`{colors.primary-disabled}`) that signals exhaustion rather than unavailability. This button appears on product pages when stock exists, which is rarely for long.

**`button-secondary`** — Transparent background with a 1px solid `{colors.ink}` (#dedede) border; ghosted against the dark canvas. Used for actions secondary to purchase: size guides, wishlist, share. On hover, border brightens toward `{colors.alcatraz-white}`.

**`button-sold-out`** — `{colors.hairline}` (#323232) fill, muted label, non-interactive cursor. Given Corteiz's chronic scarcity model this button is more frequently rendered than `button-primary`. It is the resting state of the site between drops.

### Text Input
**`text-input`** — Zero-radius field on `{colors.surface-card}` (#1e1e1e), 1px `{colors.hairline}` border. Courier New body text at `{colors.ink}` with `{colors.muted}` (#444444) placeholder. Static uppercase label sits above the field — no floating labels, no animation. Checkout forms and the legacy password gate both use this spec.

### Navigation
**`nav-bar`** — 56px-tall bar on `{colors.canvas}` (#121212), `{colors.hairline}` bottom border. Logo left, cart icon and hamburger right. `{typography.nav-link}` carries any visible link text at 13px uppercase Courier New. On mobile the bar shows only logo and icons — no inline navigation. There is no hover underline convention; the brand communicates that you either know where you are going or you do not.

### Product Card
**`product-card`** — Flush square image (1:1) on `{colors.surface-card}` (#1e1e1e), `{rounded.none}` corners, no border. Product name in `{typography.body-sm}` (14px Courier New), price in `{typography.mono-price}` (18px bold). A `product-badge-sold-out` tag overlays the top-right corner of images when stock is depleted. No quick-add mechanism — the card is deliberately passive, a catalog entry rather than a conversion surface.

### Hero
**`hero`** — Full-viewport-height, full-bleed image or video with zero internal padding. Drop headlines render in `{typography.display-xl}` (56px uppercase Courier New) at maximum `{colors.ink}` contrast or in `{colors.primary}` yellow against dark imagery. Drop announcements appear here more often than product photography: crowds, relay-run photography, and archive imagery are as common as flat lays. There is no carousel; a single decisive image fills the frame.

### Countdown Timer
**`countdown-timer`** — Four numeral blocks in `{typography.countdown}` (48px bold Courier New) tinted `{colors.primary}` (#ffd500), with uppercase four-letter labels ("DAYS", "HRS", "MIN", "SEC") in `{typography.caption}` at `{colors.muted}`. The yellow numerals on `{colors.canvas}` (#121212) are the most visually intense moment on the site outside a product drop page; they appear 24–72 hours before release and vanish the instant the drop goes live.

### Announcement Bar
**`announcement-bar`** — Solid #ffd500 strip at 36px across the full viewport, above the nav bar. Text in `{typography.caption}` (12px uppercase Courier New) in `{colors.on-primary}` (#121212). Carries drop dates, RTW declarations, and site-wide notices. It is the first element visible on every scroll-to-top and the visual signal that something is imminent.

### Product Badges
**`product-badge-sold-out`** and **`product-badge-live`** — Both are sharp-cornered (`{rounded.none}`) inline tags with 4px × 8px padding. SOLD OUT uses `{colors.hairline}` (#323232) fill with `{colors.muted}` label; DROP LIVE uses `{colors.primary}` (#ffd500) fill with `{colors.on-primary}` (#121212) label. These two states account for the overwhelming majority of inventory status on the site.

### Size Selector
**`size-selector`** — A grid of flat 48px × 48px tiles with 1px `{colors.hairline}` border and `{rounded.none}` corners. Active selection flips to `{colors.primary}` fill with `{colors.on-primary}` text. Unavailable sizes retain the border but their labels drop to `{colors.muted}` — no strikethrough, no diagonal line. The generous minimum dimensions reflect that these tiles absorb rapid, high-stakes taps during live drops under heavy server load.

### Cart Drawer
**`cart-drawer`** — 400px right-side panel on `{colors.surface-soft}` (#1c1c1c) with a 1px `{colors.hairline}` left border. Line items use `{typography.body-md}`; price totals use `{typography.mono-price}`. A full-bleed `{colors.primary}` CHECKOUT button anchors the bottom at 48px height. The drawer does not auto-open on add-to-cart — triggering it is an explicit action, keeping the checkout sequence fast and focused during drops.

### Password Gate
**`password-gate`** — Centered layout on `{colors.canvas}` (#121212): Alcatraz crest above a `{typography.display-md}` (32px uppercase) headline, a `{typography.body-md}` paragraph, then a stacked text-input and button-primary pair. The gate is archival now but remains the template for any future access-controlled drop or members-only experience. The proportions are deliberate — nothing competes with the ask.

### Footer
**`footer`** — Minimal layout on `{colors.canvas}`, 1px top border at `{colors.hairline}` (#323232). Navigation links in `{typography.body-sm}` at `{colors.muted}` (#444444). Social handles are rendered as plain text abbreviations (IG, TW, TK) rather than SVG icon glyphs — consistent with the site's plain-text register. Legal copy in `{typography.caption}`. No logo repeat, no newsletter form; the footer is deliberately spare.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to logo + cart + hamburger only; hero at 100svh; countdown stacks 2×2 grid; announcement bar truncates with marquee scroll; cart drawer becomes full-screen overlay |
| Tablet | 744–1128px | Two-column product grid; nav may expose 1–2 inline links; hero headline scales to ~40px; cart drawer at 400px side panel |
| Desktop | 1128–1440px | Three or four-column product grid; full nav visible; hero headline at full 56px display-xl; countdown timer on single row |
| Wide | > 1440px | Max-width container (~1400px) centered; gutters widen; grid remains 4-column; type sizes hold |

### Touch Targets
- All interactive tiles (size selector, buttons, nav icons) meet 48px minimum height
- Cart icon and hamburger maintain 44px × 44px minimum tap zone on mobile
- Size selector tiles are 48px × 48px minimum to handle rapid drop-day selection
- Announcement bar at 36px is display-only; no tap interaction required

### Collapsing Strategy
- Navigation: logo + icons only on mobile; hamburger reveals a full-screen link list
- Product grid: 2-up tight gutter on mobile, 3-up tablet, 4-up desktop
- Countdown: 2×2 grid on mobile below 375px; single 4-column row on tablet and up
- Announcement bar: scrolling marquee on mobile if text width exceeds viewport
- Cart drawer: full-screen bottom sheet or overlay on mobile instead of 400px side panel
- Hero: scales from 100svh with fixed headline position to content-height on tablet

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only five hex values extracted (#ffd500, #444444, #dedede, #323232, #121212); `surface-soft` (#1c1c1c) and `surface-card` (#1e1e1e) are derived by interpolation and were not directly sampled
- #ffffff (white) is almost certainly used for Alcatraz crest and logo rendering on dark fields but was not returned in extraction — documented as `alcatraz-white` but unconfirmed
- `{colors.muted}` (#444444) has very low contrast (~2.2:1) on `{colors.canvas}` (#121212); it likely functions as a border/divider color rather than inline body text — precise usage roles not extractable from static color sampling
- Font weight variants for Courier New are browser-default (400/700); the brand may use a custom or variable-weight version not surfaced in the font-family stack extraction
- Meta theme-color not set; mobile browser chrome color at drop time is unconfirmed
- Specific letter-spacing, line-height, and font-size values for display headings are estimated — the brand's compiled CSS may differ
- Component-level transition timing (hover states, drawer slide-in, countdown tick animation) not extractable via static analysis
- Grid gutter widths, column counts, and max-width container values not confirmed from extraction
- No confirmed secondary palette or seasonal color variants beyond the five extracted tones
