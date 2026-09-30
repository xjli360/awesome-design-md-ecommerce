---
version: alpha
name: "Print Club London"
source_url: "https://printclublondon.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Royal blue #003388 stakes a gallery-quality claim on every page — not the corporate navy that financial services defaults to, but the dense, ink-saturated hue of a Dalston screen-printing studio that treats its own identity mark with the same precision it brings to a hand-pulled artist edition. The serif font stack leads all editorial moments: print titles, artist credits, and section headers inherit a serif at display scale, then the page steps down to system UI for body copy and navigation — a typographic split that maps onto the site's dual nature as both a commerce destination and an art-world publication. The extracted color set is unusually chromatic for a gallery-adjacent brand: amber #fbb102, scarlet #ab2e31, grass-green #00a901, and hot pink #e94c89 appear alongside the primary blue, signalling that each print drop and editorial campaign temporarily colonises the accent system rather than locking down to a fixed two-colour brand. Product imagery is presented edge-to-edge with minimal border radius — flat frames that foreground the art — while muted grays from #4f4f4f through #949494 carry supporting text so the canvas never competes with what's on it. Surface tones shift from exhibition white (#ffffff) to a soft warm lift (#f4f4f4) that differentiates card zones without introducing shadow depth. Calls to action sit on the royal blue reversed in white, legible and direct: the shop's equivalent of a gallery price label — no softness, no rounded friendliness, just the fact of availability. The nav uses low-contrast hairline separators (#f0f0f0) and quiet uppercase labelling, letting limited-edition scarcity messaging and hero artwork do the work of urgency.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#7a9dd4"
  ink: "#1e1f26"
  body: "#32373c"
  muted: "#6d6c6c"
  muted-light: "#949494"
  hairline: "#f0f0f0"
  hairline-strong: "#4f4f4f"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#fbb102"
  accent-red: "#ab2e31"
  accent-green: "#00a901"
  accent-pink: "#e94c89"
  accent-orange: "#f45800"
  dark-surface: "#1e1f26"

typography:
  display-xl:
    fontFamily: "serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

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
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.primary-active}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline-strong}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-light}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    focus-border: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    border: none
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 60px
    logoColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageRadius: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    gap: "{spacing.sm}"
  hero-editorial:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  edition-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  edition-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  edition-badge-new:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  artist-credit:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    textTransform: uppercase
    letterSpacing: 0.06em
  category-filter:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    active-backgroundColor: "{colors.primary}"
    active-textColor: "{colors.on-primary}"
  drop-announcement:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    padding: "10px {spacing.base}"
    textAlign: center
  print-run-label:
    textColor: "{colors.muted-light}"
    typography: "{typography.label-caps}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.sm} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Flat-cornered rectangular button (#003388 fill, white `{typography.button-md}` label, 48px tall, 28px horizontal padding). The zero-radius corners (`{rounded.none}`) carry the deliberateness of a silkscreen annotation — nothing softened. Active state deepens to `{colors.primary-active}` (#002266); disabled state replaces the fill with `{colors.primary-disabled}`, a washed mid-blue that signals unavailability without visual noise.

**`button-secondary`** — Same geometry as primary, canvas background with a 1px `{colors.primary}` border and blue label text. Used for secondary actions such as "Add to Wishlist" or filter resets where the primary page action is already claimed by the blue fill.

**`button-ghost`** — Transparent background, `{colors.ink}` text with an underline. No border, no radius. Used for low-emphasis navigation prompts like "See all artists" or "Back to prints" — the minimum viable CTA.

### Form Inputs

**`text-input`** — Hard-cornered, 1px `{colors.hairline-strong}` border at rest. Focus replaces the border colour with 1px `{colors.primary}` — no animated ring or box-shadow glow, just the brand blue as a cursor signal. Placeholder text in `{colors.muted-light}`.

**`search-bar`** — Wider input used in the nav or atop collection pages. `{colors.surface-soft}` fill, no visible border, search icon in `{colors.muted}`. The flat corners and recessive fill integrate it as a nav utility rather than a primary UI feature.

### Navigation

**`nav-bar`** — White canvas bar, 60px tall, with a 1px `{colors.hairline}` bottom separator. The wordmark renders in `{colors.primary}` blue. Nav links use `{typography.nav-link}` in `{colors.ink}` without underlines; hover states are CSS-layer concerns not encoded in tokens. On mobile the nav collapses to a hamburger trigger that opens a full-width overlay.

**`category-filter`** — Pill-shaped (`{rounded.full}`) filter chips used on shop and collection pages — the only `{rounded.full}` elements in the entire system. Default: canvas background, thin hairline border, muted uppercase label. Active: fills with `{colors.primary}`, text inverts to white. The pill shape is explicitly reserved for filtering; every other interactive element is sharp-cornered.

### Product Cards

**`product-card`** — Zero-radius image frame filling the full grid column width, compact text block below. Title in `{typography.title-sm}` serif, artist credit in `{typography.caption}` uppercase and `{colors.muted}`, price in `{typography.price}`. No shadow, no hover-lift animation in tokens — the print image itself carries attention. Edition badges overlay the top-left corner of the image.

**`print-run-label`** — A small print-run or edition-size annotation sitting below the price, separated by a 1px `{colors.hairline}` rule. Uses `{typography.label-caps}` in `{colors.muted-light}` — the typographic equivalent of an edition stamp on a physical print.

### Badges & Labels

**`edition-badge`** — Flat rectangular chip in `{colors.primary}` with `{typography.label-caps}` white text. Marks "Limited Edition," print-run numbers, or "Available Now." Sold-out swaps the fill to `{colors.muted}`; new arrivals and drop announcements use `{colors.accent-red}`.

**`artist-credit`** — Not a chip — a standalone uppercase caption beneath the print title. Sits in `{colors.muted}` at `{typography.caption}` scale with extra letter-spacing. Models the convention of exhibition wall labels: present, precise, unobtrusive.

### Editorial & Marketing

**`hero-editorial`** — Full-bleed section on `{colors.dark-surface}` (#1e1f26) near-black. `{typography.display-xl}` headline in white, subtext in `{typography.body-md}`. Used for drop campaigns and artist features. The dark field provides high contrast without using the primary blue for large fills, which would dilute its CTA signal.

**`drop-announcement`** — Full-width bar above the nav in `{colors.accent-amber}` (#fbb102). Text in `{colors.ink}` at `{typography.label-caps}`. Amber is the warmest and most insistent accent in the palette and is reserved for time-critical drop moments — edition launches, countdown copy, sell-out warnings.

### Footer

**`footer`** — Near-black background (`{colors.ink}`), white links in `{typography.body-sm}`, section headings in `{typography.label-caps}`. The body-to-footer transition from white canvas to dark field acts as a clear editorial close, no decorative divider needed.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger overlay; hero headline reduces to `{typography.display-md}`; category filter chips scroll horizontally without wrapping |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links with secondary items in dropdown; hero remains full-bleed |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with search bar visible; announcement bar full-width |
| Wide | > 1440px | Container max-width ~1440px centred; side padding increases to `{spacing.section}`; grid holds at 4 columns |

### Touch Targets

- All buttons are minimum 48px tall to meet touch guidelines
- Product card tap area covers image and text block as a single target
- Nav hamburger trigger is at least 44×44px
- Category filter chips have enough padding to reach 40px height on mobile

### Collapsing Strategy

- Nav: text links collapse at tablet breakpoint; search moves to expanded overlay on mobile
- Product grid steps 4 col → 3 col → 2 col → 1 col at each breakpoint
- Hero headline steps from `{typography.display-xl}` (52px) to `{typography.display-md}` (36px) on mobile
- Category filters scroll horizontally on mobile with no wrapping; two-row layout available tablet+
- Footer multi-column link grid stacks to single column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font name identified — the site reports `inherit, serif` in the stack, suggesting the display typeface loads via a JS font service (likely Adobe Fonts or Google Fonts). The serif stack used here is a best-effort approximation; the actual family cannot be confirmed without JS execution.
- Social platform colours contaminate the extracted palette (#5865f2 Discord, #0866ff/#0461dd Facebook, #0a7aff) and are excluded from brand tokens.
- No meta theme-color extracted; mobile browser chrome colour is undefined.
- Hover and focus animation curves (duration, easing) are not capturable from static extraction and are not encoded in this spec.
- Exact product-card hover behaviour (image zoom, quick-add overlay) could not be verified from static extraction.
- Accent colours (#fbb102, #ab2e31, #00a901, #e94c89, #f45800) appear in the extracted palette but their precise semantic assignments across specific badge types, campaign modules, and states cannot be confirmed without a full JS render.
