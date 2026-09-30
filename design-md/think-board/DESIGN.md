---
version: alpha
name: "Think Board"
source_url: "https://www.think-board.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The writable surface as aesthetic object — Think Board makes this argument by anchoring the entire UI to a deep jade-green (#108474) that belongs more to premium workspace accessories than to institutional supply catalogs. A single punch of golden yellow (#fbcd0a) appears exactly once per page: the announcement strip or a promotional badge, a warm disruption before the teal system resumes command. Everything else descends through a long achromatic staircase from #eeeeee through a dozen near-identical grays to #121212, providing the tonal scaffolding for a utility-first Shopify catalog that would collapse into visual noise without it.

  Montserrat carries all display and heading work: narrow horizontal proportions, flat geometry, no serif hedging — type that behaves like the flat writable surface the brand sells. Productive geometry over expressive personality. Nunito Sans handles body copy with its round terminals softening the otherwise tightly controlled grid, preventing the catalog from reading as purely industrial. Baskerville and Open Sans appear only as Shopify stack fallbacks and review-widget artifacts, not as deliberate editorial voices.

  The chromatic supporting cast is small and precise. A sage mid-green (#67ba94, identical to the site's meta theme-color) anchors secondary confirmation states and supporting CTAs. A soft lavender (#a89cc8) surfaces in filter pills and variant selectors — a tertiary accent that prevents the product grid from monotony without departing from the cool-neutral register. Pale cyan washes (#c1e6e6, #aadddd) fill feature-section backgrounds and surface gradients, pulling the palette toward the light-filled logic of focus-friendly workspaces.

  Corners sit at {rounded.sm} for cards and inputs — consumer-friendly without approaching the playful pill shapes of lifestyle brands. Buttons hold at {rounded.xs}, communicating tool-grade intentionality over expressive warmth. Section spacing is generous, card interiors tight, reflecting a catalog layout where dominant product photography is the primary conversion lever. The announcement bar renders {colors.on-accent-yellow} type on {colors.accent-yellow} fill: the loudest element on any page, a deliberate voltage before the teal hierarchy takes over and holds.

colors:
  primary: "#108474"
  primary-active: "#0a6358"
  primary-disabled: "#aadddd"
  accent-yellow: "#fbcd0a"
  accent-sage: "#67ba94"
  accent-lavender: "#a89cc8"
  accent-pale-cyan: "#c1e6e6"
  ink: "#121212"
  body: "#4f4f4f"
  muted: "#7b7b7b"
  muted-soft: "#bbbbbb"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#fcfcfc"
  surface-soft: "#f8f8f8"
  surface-card: "#f9fafb"
  on-primary: "#ffffff"
  on-accent-yellow: "#121212"

typography:
  display-xl:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  label-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  announcement:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px

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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent-yellow}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent-yellow}"
    typography: "{typography.announcement}"
    height: 40px
    paddingH: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageRadius: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 520px
    paddingV: "{spacing.section}"
    paddingH: "{spacing.xxl}"
  badge-promo:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent-yellow}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-bestseller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.primary}"
    height: 44px
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderDefault: "1px solid {colors.hairline}"
  feature-strip:
    backgroundColor: "{colors.accent-pale-cyan}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    labelTypography: "{typography.label-sm}"
    captionTypography: "{typography.body-sm}"
    paddingV: "{spacing.xl}"
    gap: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    linkHoverColor: "{colors.accent-sage}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    paddingV: "{spacing.section}"
    borderTop: "4px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — The workhorse CTA rendered in deep jade-green (#108474) with white lettering at `{typography.button-md}` (Montserrat 600, uppercased, 0.5px tracking). Corner radius holds at `{rounded.xs}` — just enough to read as consumer-facing without softening the tool-grade character. Hover deepens to `{colors.primary-active}` (#0a6358); disabled pulls back to the pale cyan `{colors.primary-disabled}`, which visually recedes without introducing a neutral gray.

**`button-secondary`** — White canvas fill with a 2px jade-green border and `{colors.primary}` text, establishing a clear visual hierarchy below the primary CTA without introducing a competing fill color. Matches primary height and padding exactly so the two can sit side by side without optical imbalance.

**`button-ghost`** — Transparent background, `{colors.body}` text at `{typography.button-sm}`. Used for lower-priority actions inside product configurators, filter panels, and modal footers. Does not carry a border, so it reads as a text link with button-scale padding.

**`button-accent-yellow`** — Reserved for hero-section CTAs and time-limited promotional moments. Golden yellow (`{colors.accent-yellow}`) fill with `{colors.on-accent-yellow}` near-black text creates the brand's highest-contrast button. Appears sparingly so the voltage is preserved; using it more than once per page view dissipates the effect.

### Nav Bar

**`nav-bar`** — 64px tall, canvas-white background with a 1px `{colors.hairline}` bottom border. The logo mark uses `{colors.primary}` for the brand color. Navigation links render in `{typography.title-sm}` (Montserrat 600, 15px). Cart and account icons sit right-aligned as `{colors.ink}` icon buttons with at least 44px tap targets. On scroll, the bar picks up a soft box-shadow rather than changing fill, preserving the clean white reading.

### Announcement Bar

**`announcement-bar`** — A 40px golden-yellow strip pinned above the navigation, the loudest element in the entire UI hierarchy. Uses `{typography.announcement}` (Montserrat 600, 13px) with `{colors.on-accent-yellow}` text. Typically carries free-shipping thresholds or time-limited discount codes. Because it sits atop the teal/neutral system, it should never be dismissed as a design afterthought — it is the brand's primary impulse-trigger surface.

### Product Card

**`product-card`** — The catalog grid unit: `{colors.surface-card}` fill, `{rounded.sm}` corners, a faint `{colors.hairline-soft}` border, and `{spacing.base}` internal padding. Product image fills the top portion with its own `{rounded.sm}` crop. Title renders in `{typography.title-sm}`, price in `{typography.price}` (Montserrat 700, 20px), supporting copy in `{typography.body-sm}`. Badge overlays (`badge-promo`, `badge-bestseller`) pin to the image top-left corner. Hover state lifts the card with a subtle box-shadow at 0 4px 16px rgba(0,0,0,0.08) — no border color shift.

### Hero Banner

**`hero-banner`** — Full-width teal (#108474) block with white display type at `{typography.display-xl}`. Subhead drops to `{typography.body-md}` in the same white. The primary CTA uses `button-accent-yellow` to create a warm contrast jolt against the cool background — the only place in the UI where yellow sits on teal rather than on white. Minimum height 520px with `{spacing.section}` vertical padding; lifestyle photography or product illustration is positioned to the right on desktop, collapsing below the text stack on mobile.

### Badges

**`badge-promo`** — Golden yellow chip with near-black Montserrat uppercase label at `{typography.label-sm}`, `{rounded.xs}` corners, 3px 8px padding. Used for sale percentages and active promo codes pinned over product card images.

**`badge-bestseller`** — Same construction as `badge-promo` but in `{colors.primary}` with white text. Marks high-volume SKUs and top-rated products in the catalog grid; the teal fill reads as a system endorsement rather than a promotional push.

**`badge-new`** — Soft lavender (`{colors.accent-lavender}`) fill with `{colors.ink}` text. Introduces new product lines without competing chromatically with the teal/yellow system. Used for seasonal additions and recently launched board formats.

### Search Bar

**`search-bar`** — Soft surface fill (`{colors.surface-soft}`), 1px `{colors.hairline}` border, `{rounded.sm}` corners. Magnifier icon renders in `{colors.primary}`. On focus, the border upgrades to 2px solid jade-green and the background shifts to `{colors.canvas}`. Can appear inline within the nav on desktop or expand as a full-width overlay on mobile via a slide-down animation.

### Color Swatch

**`color-swatch`** — A 24px circular dot (`{rounded.full}`) for board surface color and film variant selection on product detail pages. Default state shows a 1px `{colors.hairline}` border; selected state adds a 2px `{colors.primary}` ring offset 2px from the swatch edge. Hit area expands to 40×40px invisibly for touch. Used in configurator flows where customers specify board finish, frame color, or film variant.

### Feature Strip

**`feature-strip`** — A full-width band in pale cyan (`{colors.accent-pale-cyan}`) carrying three to four icon-plus-label blocks (e.g., "Dry Erase Surface," "Ships in 3–5 Days," "Custom Sizes Available"). Labels use `{typography.label-sm}`, supporting copy uses `{typography.body-sm}`. Icon fill matches `{colors.primary}`. Blocks are spaced with equal `{spacing.xl}` gaps; on mobile they collapse to a 2×2 grid. Positioned immediately below the hero or above the product grid as a trust-signal layer.

### Footer

**`footer`** — Near-black (`{colors.ink}`) fill with a 4px `{colors.primary}` top border that anchors the brand color at page end. Column headings use `{typography.label-sm}` (Montserrat 700, uppercase). Body links render in `{colors.on-primary}` by default, shifting to `{colors.accent-sage}` on hover. An email newsletter input follows the `text-input` spec adapted for a dark background — placeholder text uses `{colors.muted-soft}`, border uses `{colors.muted}`, focus ring remains `{colors.accent-sage}`. Social icons appear as `{colors.muted-soft}` fill, brightening to `{colors.on-primary}` on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero switches to stacked text-over-image with headline at `display-md`; feature strip stacks to 2×2 grid; announcement bar wraps to two lines at 375px |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links inline with secondary links in an overflow menu; hero maintains split layout at reduced horizontal padding |
| Desktop | 1128–1440px | Three-column product grid; full nav visible with all links; hero at full 520px minimum height with side-by-side text and lifestyle image |
| Wide | > 1440px | Content constrained to ~1400px max-width, centered; product grid may extend to four columns; section padding increases by 1.25× |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44×44px tap target
- Color swatches expand their invisible hit area to 40×40px despite 24px visual size
- Nav links in the mobile drawer expand to full-width rows with `{spacing.lg}` vertical padding
- Cart and account icons in the nav maintain 44px height regardless of icon visual size

### Collapsing Strategy
- Navigation collapses to hamburger below 744px; opens a slide-in drawer at full viewport height with a `{colors.ink}` scrim at 60% opacity behind it
- Product filters move from a left-side panel on desktop to a bottom sheet on mobile, triggered by a "Filter & Sort" pill button styled with `button-secondary`
- Announcement bar is maintained at all breakpoints; copy marquee-scrolls at widths below 375px if it exceeds one line
- Hero image drops below the text stack on mobile with height capped at 280px; text alignment shifts from left-aligned to center-aligned

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Logo typeface not confirmed — Montserrat is used for headings but the wordmark may use a custom lockup or Baskerville variant; verify against supplied brand assets
- Button corner-radius not extracted from live CSS; `{rounded.xs}` (4px) inferred from the functional, tool-grade visual register of the site
- `primary-active` (#0a6358) derived by darkening primary (#108474) — not extracted from production; confirm hover state color against live CSS
- Exact footer column count, link hierarchy, and social icon set not determinable from color/font extraction alone
- Product configurator UI pattern for custom board sizing (multi-step vs. single-page) not captured; likely uses a stepped form or accordion
- Icon set and illustration style not extractable from color/font signals; brand may use line icons or custom illustrated assets
- Review widget typefaces (JudgemeIcons, JudgemeStar, JudgemeIcons !important) are Judge.me app artifacts and are intentionally excluded from the design system typography
- No motion or animation timing tokens could be extracted; transitions should be prototyped against the live site
