---
version: alpha
name: "Ryobi"
source_url: "https://www.ryobitools.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  That specific yellow — #e1e723, an electric chartreuse sitting exactly between safety marker and solar flare — is the organizing principle behind every Ryobi surface, and it arrives from physical reality rather than branding committee: the color must match the battery packs and mower decks that come out of the box. The digital system is therefore constrained by the object, which gives Ryobi's palette an unusual kind of discipline. Against the yellow, the site runs a near-black ground (#0c0c0c) and a dark teal ink (#141e23) that reads warmer than pure black — workshop-floor pragmatism rather than lifestyle aspiration. A muted teal (#4a6e78) surfaces in secondary UI chrome, providing information hierarchy without competing with the primary volt. The supporting grays — #b1b3b5, #bdbec0, #dddedf, #ececed, #cbcdce — form a tightly stepped neutral staircase that keeps product photography uncontested on pale canvases (#fdfdfd, #f7f7f8). The type system runs on futura-pt, a geometric sans with an industrial pedigree: display sizes are set in uppercase with wide tracking to land product names with the authority of a spec-sheet header. Body copy shifts to Roboto for legibility at small sizes. Buttons are nearly square-cornered (`{rounded.xs}`), consistent with the angular tool silhouettes they accompany — there is no softness for its own sake. Badges and ribbons are hard-edged (`{rounded.none}`), printed on the #e1e723 primary or the near-black, functioning more like stickers on a product box than digital adornment. Spacing is generous at section scale so that product photography breathes, but interactive elements stay dense enough for a buyer who already knows their battery platform and is shopping by specs, not story. The footer carries a 3px top border in #e1e723 — the yellow that starts on the tool ends the page.

colors:
  primary: "#e1e723"
  primary-hover: "#d4da00"
  primary-active: "#c8ce00"
  primary-disabled: "#f0f2a8"
  ink: "#0c0c0c"
  body: "#141e23"
  body-secondary: "#4a6e78"
  muted: "#b1b3b5"
  muted-soft: "#bdbec0"
  hairline: "#dddedf"
  hairline-soft: "#ececed"
  border-mid: "#cbcdce"
  border-light: "#b8b9bb"
  canvas: "#fdfdfd"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  surface-mid: "#ececed"
  on-primary: "#0c0c0c"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
    textTransform: uppercase
  display-md:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: 0
  display-sm:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0
  title-md:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  title-sm:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.2px
  body-md:
    fontFamily: "Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  badge-label:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'futura-pt', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body-secondary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: none
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.border-mid}"
    borderFocus: "2px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 48px
    border: "1px solid {colors.border-mid}"
    iconColor: "{colors.ink}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    logoAccentColor: "{colors.primary}"
    borderBottom: none
    activeIndicatorColor: "{colors.primary}"
  nav-utility-bar:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    padding: "{spacing.base}"
    badgePosition: top-left
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 560px
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    ctaButton: button-primary
    overlay: "linear-gradient(90deg, rgba(12,12,12,0.85) 0%, rgba(12,12,12,0.25) 100%)"
    padding: "{spacing.xxl} {spacing.section}"
  category-tile:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    labelTypography: "{typography.display-sm}"
    rounded: "{rounded.xs}"
    border: none
    hoverBorderColor: "{colors.primary}"
    hoverBorderWidth: 3px
    aspectRatio: "4/3"
    labelPosition: bottom-left
    padding: "{spacing.base}"
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  new-badge:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  sale-ribbon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    shape: diagonal-ribbon
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowBorder: "1px solid {colors.hairline}"
    headerBackground: "{colors.ink}"
    headerTextColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
    cellPadding: "{spacing.md} {spacing.base}"
  battery-compatibility-chip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    iconColor: "{colors.on-primary}"
  platform-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    activeBorderBottom: "3px solid {colors.primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  section-divider-accent:
    backgroundColor: "{colors.primary}"
    height: 4px
    width: 100%
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    headingColor: "{colors.on-dark}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The hard-cornered yellow CTA (`{rounded.xs}`, 48px tall, `{colors.primary}` fill) is the highest-contrast element on any page. Text is set in uppercase `{typography.button-md}` (futura-pt, 700 weight, 1px letter-spacing) in `{colors.on-primary}` near-black, which maintains WCAG contrast on the neon ground. Hover shifts the fill to `{colors.primary-hover}` (#d4da00), active to `{colors.primary-active}` (#c8ce00); disabled washes out to `{colors.primary-disabled}` with `{colors.muted}` text. Never pill-shaped — the square corner is load-bearing to the brand's tool-grade identity.

**`button-secondary`** — A 2px `{colors.ink}` border outline on transparent, matching height and type scale of primary. Used on light surfaces only. On dark hero backgrounds, `button-secondary-on-dark` swaps both border and text to `{colors.on-dark}`. The pairing of yellow primary + black outline secondary is the standard CTA/secondary split across all product pages.

**`button-ghost`** — Transparent, no border, `{colors.body-secondary}` teal text in `{typography.button-sm}`. Reserved for low-hierarchy actions like "View all" links at the bottom of category carousels and spec-detail toggles.

### Search Bar

**`search-bar`** — A `{rounded.xs}` field with a `{colors.primary}` submit button flush to the right edge, creating a contained unit. The yellow submit button serves double duty as a brand signature within a utility component. Border is `{colors.border-mid}` at rest, thickens to 2px `{colors.ink}` on focus. Placeholder copy in `{colors.muted}`.

### Navigation

**`nav-bar`** — The global nav sits on `{colors.ink}` (#0c0c0c), establishing a persistent dark band at the top of every page. The Ryobi wordmark appears in white with the `{colors.primary}` yellow mark. Nav links use `{typography.nav-link}` (uppercase futura-pt, 600 weight) in `{colors.on-dark}`. The active category shows a bottom indicator in `{colors.primary}`. Above it, `nav-utility-bar` sits on `{colors.body}` (#141e23) in `{typography.spec-label}` for account links, store finder, and promo notices.

### Product Card

**`product-card`** — White (`{colors.surface-card}`) with a `{colors.hairline}` border and `{rounded.xs}` corners. Product image area uses `{colors.surface-soft}` as a neutral stage. Product name renders in `{typography.title-md}` (futura-pt, 600, 18px), price in `{typography.price}` (futura-pt, 700, 22px). `promo-badge` and `new-badge` chips stack in the top-left corner as hard-edged rectangles in yellow or near-black respectively — they never share corner radius with the card. Cards gain a soft shadow on hover.

### Hero Banner

**`hero-banner`** — Full-bleed `{colors.ink}` background with a directional overlay gradient that preserves image texture on the right while keeping headline legibility on the left. Headline in `{typography.display-xl}` (56px uppercase futura-pt 700), sub-line in `{typography.body-md}` Roboto. The primary CTA button sits below with no additional decoration. On mobile, the image shifts to a top-fill arrangement and headline size drops to `{typography.display-lg}`.

### Category Tile

**`category-tile`** — Dark `{colors.body}` backgrounds with label text anchored bottom-left in `{typography.display-sm}`. On hover, a 3px `{colors.primary}` border traces the `{rounded.xs}` perimeter — a sharper, more mechanical hover state than a shadow or overlay. Tiles are used in 2-up, 3-up, and 4-up grid configurations depending on breakpoint.

### Badges and Ribbons

**`promo-badge`** / **`new-badge`** / **`sale-ribbon`** — All set in uppercase `{typography.badge-label}` (10px futura-pt, 1px tracking). Hard `{rounded.none}` corners throughout. Promo and sale use `{colors.primary}` yellow; new-product uses `{colors.body}` near-black. The ribbon variant uses a diagonal cut geometry applied via CSS clip-path, anchored to the top-left corner of the product card image.

### Spec Table

**`spec-table`** — Row-striped on `{colors.surface-soft}` with a `{colors.hairline}` row divider. Labels in `{typography.spec-label}` (uppercase, 700, 1.2px tracking); values in `{typography.body-sm}` Roboto. The header row inverts to `{colors.ink}` background with `{colors.on-dark}` text, providing a strong section anchor. The spec table is the primary informational component on PDP pages and is never collapsed on desktop.

### Battery Compatibility Chip

**`battery-compatibility-chip`** — A `{rounded.full}` pill in `{colors.primary}` carrying a battery icon and platform label in `{typography.spec-label}`. These chips cluster below the product title to signal ONE+ / LINK / HP compatibility at a glance — they are one of the few `{rounded.full}` shapes in the system, deliberately contrasting with the square geometry elsewhere to draw the eye to compatibility information.

### Platform Selector

**`platform-selector`** — A row of tabs for filtering by battery platform (ONE+, LINK, HP, 48V). Inactive tabs sit on `{colors.surface-soft}` with `{colors.ink}` text; the active tab flips to `{colors.ink}` background with `{colors.on-dark}` text and a 3px `{colors.primary}` bottom border. Uses `{typography.title-sm}` futura-pt. Behaves as a horizontal scroll row on mobile.

### Footer

**`footer`** — Full-width `{colors.ink}` background with a 3px `{colors.primary}` top border — the yellow that opens the nav closes the page. Section headings in `{typography.spec-label}` (uppercase futura-pt, `{colors.on-dark}`); link text in `{typography.body-sm}` Roboto at `{colors.muted}`. Newsletter input and submit CTA use `button-primary` at reduced height within the footer column grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero headline drops to `display-lg`; category tiles 2-up; product grid 1-up or 2-up; nav collapses to hamburger on `{colors.ink}` ground; spec table horizontally scrollable; platform-selector becomes horizontal scroll row |
| Tablet | 744–1128px | Nav retains icon links, drops secondary labels; product grid 2–3 up; hero uses top-fill image layout with overlay; category tiles 2–3 up; spec table full-width |
| Desktop | 1128–1440px | Full nav bar with all category labels visible; product grid 3–4 up; hero returns to side-by-side layout with gradient overlay; category tiles 4-up; spec table two-column label/value layout |
| Wide | > 1440px | Max content width capped at ~1440px; hero background bleeds full width with content centered; product grid stays 4-up with larger card padding; side gutters expand with `{colors.ink}` or `{colors.surface-soft}` fill |

### Touch Targets

- All primary buttons minimum 48px tall, minimum 44px wide
- Nav hamburger icon minimum 44×44px tap target
- Battery compatibility chips minimum 36px tall with 8px lateral padding
- Product card tap target covers full card surface, not just title
- Platform selector tabs minimum 44px tall on mobile

### Collapsing Strategy

- Global nav collapses to hamburger + wordmark + search icon on mobile; utility bar hides entirely
- Spec table scrolls horizontally rather than stacking, preserving label/value pairing
- Category tiles reduce from 4-up to 2-up; hero image moves from side panel to top background
- Footer column grid stacks to single column; section headings become accordion toggles on mobile
- Battery compatibility chip row wraps to two rows if more than three platforms apply

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom Ryobi icon set could be extracted; icon style (stroke weight, corner style) is unconfirmed — assumed to match futura-pt geometry (geometric, moderate stroke)
- Exact nav height on mobile and breakpoint-specific logo scaling not confirmed from extraction
- Hover and focus animation durations (transition timing) not captured; assumed 150–200ms ease-out
- Product image aspect ratio on cards (likely 1:1 or 4:3) not confirmed
- Exact letter-spacing values for display-xl and display-lg are estimated from futura-pt defaults — live site may differ
- Dark-mode or high-contrast mode support is unknown; extraction shows no alternate color scheme
- Calibri appeared in the font stack but is almost certainly a Windows system fallback for futura-pt — not a secondary brand typeface
- Price display for sale/was-now states (strikethrough color, reduced price color) not confirmed from extraction
