---
version: alpha
name: "Heritage Guitars"
source_url: "https://www.heritageguitars.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Heritage Guitars never left the building. When Gibson relocated to Nashville in 1984, five craftsmen stayed behind in the original Kalamazoo, Michigan factory and continued hand-building guitars the same way — that founding refusal to follow the industry is the organizing logic behind every visual decision on the site. An antique gold (#9f8a46) — closer to worn brass than shining chrome — carries all primary calls to action and the brand's most visible hover states; it is the color of aged instrument hardware rather than a premium marketing badge. The canvas is warm cream (#f8f4e9), not clinical white, and the deepest surfaces read as rich near-black brown (#231e18) that evokes oiled mahogany rather than a tech-product's neutral charcoal. ff-tisa-web-pro, a high-contrast humanist serif, runs at every typographic scale — the stack never reaches for a sans-serif even at caption sizes, positioning every line of copy as part of the same deliberate editorial register as a vintage instrument catalog. A muted blue-gray (#b0c5cb) surfaces at tertiary moments — gallery borders, specification table headers, secondary badge strokes — providing cool relief against the dominant warm amber-and-cream register. The orange-red accent (#df5334) is reserved for urgency signals: in-stock alerts, limited-run callouts, and error states. Corner radii are minimal throughout; product cards carry just `{rounded.xs}` to `{rounded.sm}` clipping, hero images run edge-to-edge without rounding, and primary buttons hold `{rounded.sm}` — enough to soften without reading as consumer-casual. Section spacing is generous at `{spacing.section}` between major content areas while the product grid maintains tight gutters so guitar silhouettes can dominate the frame. The overall palette reads like the inside of a vintage instrument case: amber-lit, substantial, and distinctly Midwestern in its absence of coastal minimalism or luxury-brand cool.

colors:
  primary: "#9f8a46"
  primary-active: "#7a6835"
  primary-disabled: "#d4c8a0"
  ink: "#231e18"
  body: "#4a4a4a"
  muted: "#979797"
  hairline: "#d2d0cc"
  canvas: "#f8f4e9"
  surface-soft: "#fefefc"
  surface-card: "#ffffff"
  on-primary: "#f8f4e9"
  on-dark: "#f8f4e9"
  dark-canvas: "#0a0a0a"
  near-black: "#121212"
  gold-light: "#af9966"
  accent-rust: "#df5334"
  accent-steel: "#b0c5cb"
  warm-gray: "#dedede"
  warm-mid: "#444444"

typography:
  display-xl:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.02em
  spec-label:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  logo-display:
    fontFamily: "'ff-tisa-web-pro', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.04em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 28px
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
    padding: "12px 28px"
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "11px 27px"
    height: 44px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "11px 27px"
    height: 44px
    border: "1px solid {colors.on-dark}"
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "11px 27px"
    height: 44px
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid rgba(159,138,70,0.25)"
    logoColor: "{colors.primary}"
    logoTypography: "{typography.logo-display}"
  nav-dropdown:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    border: "1px solid rgba(159,138,70,0.2)"
    linkHoverColor: "{colors.gold-light}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageRounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    shadow: "0 2px 8px rgba(35,30,24,0.08)"
  hero-full:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    subheadColor: "{colors.gold-light}"
    padding: "120px {spacing.xl}"
    overlayGradient: "linear-gradient(to right, rgba(10,10,10,0.85) 40%, rgba(10,10,10,0.2))"
  section-header:
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    dividerColor: "{colors.primary}"
    dividerHeight: 2px
    dividerWidth: 48px
    marginBottom: "{spacing.xl}"
  collection-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  limited-badge:
    backgroundColor: "{colors.accent-rust}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rowBorderColor: "{colors.hairline}"
    headerBackgroundColor: "{colors.canvas}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
  guitar-gallery:
    backgroundColor: "{colors.near-black}"
    thumbnailBorder: "1px solid rgba(159,138,70,0.3)"
    thumbnailBorderActive: "2px solid {colors.primary}"
    thumbnailRounded: "{rounded.xs}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
  craftsmen-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    quoteMarkColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.muted}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    headingColor: "{colors.primary}"
    dividerColor: "rgba(159,138,70,0.2)"
    logoColor: "{colors.primary}"
    padding: "{spacing.section} 0"
    linkHoverColor: "{colors.gold-light}"

## Components

### Buttons
**`button-primary`** — The antique gold fill (#9f8a46) on warm cream text ({colors.on-primary}) runs at 44px height with near-sharp {rounded.sm} corners, pairing the {typography.button-md} stack at 0.08em letter-spacing in uppercase — the tracking and case give it the feel of a hand-stamped catalog label rather than a digital CTA. On hover the fill drops to `{colors.primary-active}` (#7a6835), deepening like tarnished brass under pressure. The disabled state uses `{colors.primary-disabled}` with `{colors.muted}` text to signal unavailability without alarm.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` stroke and matching gold text; padding mirrors `button-primary` exactly so the pair can sit side-by-side without height misalignment. Used for "Learn More" and compare-model actions where a gold fill would compete with nearby product photography.

**`button-ghost`** — Reserved for CTAs placed over dark hero imagery or the `{colors.dark-canvas}` background. White 1px border and white text maintain legibility on dark overlays; hover adds a 10% white fill behind the label. Used on the full-bleed hero section for secondary actions like "View Collection."

**`button-ghost-dark`** — Same ghost structure but for use on `{colors.canvas}` or light editorial sections — ink border, ink text via `{colors.ink}`. Prevents the gold CTA from visually crowding lighter backgrounds where two buttons share a row.

### Navigation
**`nav-bar`** — 72px tall on `{colors.dark-canvas}`, making Heritage's horizontal nav read as a stage curtain rather than a utility strip. The wordmark renders in `{colors.primary}` using `{typography.logo-display}`. Nav links use `{typography.nav-link}` in `{colors.on-dark}` with a thin gold underline on hover; a bottom hairline at 25% gold opacity separates the bar from hero content without breaking the dark-surface continuity. Dropdowns expand against `{colors.near-black}` with subtle gold-tinted borders and `{colors.gold-light}` link hover states.

### Product Cards
**`product-card`** — White card with a 1px `{colors.hairline}` border and `{rounded.xs}` clipping; on hover the border transitions to `{colors.primary}` gold for selection feedback without animation overhead. Model name in `{typography.title-md}` `{colors.ink}`, price in `{typography.body-md}`, and the series or tonewood specification in `{typography.body-sm}` `{colors.muted}`. A subtle drop shadow (0 2px 8px warm-brown) lifts the card from the grid background. The entire card surface is tappable.

### Hero
**`hero-full`** — Full-viewport hero with a directional gradient overlay (rgba(10,10,10,0.85) left to rgba(10,10,10,0.2) right) letting guitar photography breathe on the right while the headline holds legibility on the left. Headline uses `{typography.display-xl}` in `{colors.on-dark}`; the subhead drops to `{typography.display-sm}` in `{colors.gold-light}` (#af9966), a slightly lighter gold that reads as warm ambient tone against near-black rather than competing with the CTA. The primary button sits at `{spacing.xl}` below the subhead text block.

### Section Headers
**`section-header`** — Collection and editorial headings use `{typography.display-md}` in `{colors.ink}` with a 2px × 48px `{colors.primary}` rule beneath the text as a divider — the gold rule functions as a letterpress slug rather than a decorative flourish. Margin below is `{spacing.xl}` before grid content begins.

### Badges
**`collection-badge`** — Square-cornered ({rounded.none}), antique gold fill, cream text in the `{typography.spec-label}` uppercase stack. Applied as a card overlay to mark series membership (CORE, MADE IN USA, ARTISAN). The absence of radius reinforces a stamp or hallmark character.

**`limited-badge`** — Same geometry as `collection-badge` but uses `{colors.accent-rust}` (#df5334) fill for urgency — limited runs, low-stock warnings, discontinued notices. The rust orange reads as a distinct contrast signal against the gold-dominant palette without introducing an inharmonious hue.

### Specification Table
**`spec-table`** — Two-column specification grid for product detail pages. Labels in `{typography.spec-label}` uppercase `{colors.muted}`; values in `{typography.body-sm}` `{colors.ink}`. Rows separated by 1px `{colors.hairline}` rules on a `{colors.surface-soft}` background. A section header strip above in `{typography.title-sm}` sits on `{colors.canvas}`. This component is central to Heritage's value proposition — builders specify tonewoods, binding type, nut material, and neck profile the same way a factory spec card would.

### Guitar Gallery
**`guitar-gallery`** — `{colors.near-black}` stage with a horizontal thumbnail strip beneath; the active thumbnail carries a 2px `{colors.primary}` border, inactive thumbnails a 1px 30%-opacity gold border. Captions in `{typography.caption}` `{colors.muted}` sit below the stage rail. The dark field isolates guitar silhouettes without background removal, allowing natural studio photography to display as if under a focused instrument light.

### Craftsmen Strip
**`craftsmen-strip`** — Full-width editorial block on `{colors.ink}` background featuring a founding-story pull-quote or master-builder profile. Opening quotation marks render in `{colors.primary}` gold; headline in `{typography.display-md}` `{colors.on-dark}`; body copy in `{typography.body-md}` `{colors.on-dark}`. Appears between collection sections as a narrative breather that reinforces the Kalamazoo factory provenance without reducing it to a banner callout.

### Footer
**`footer`** — `{colors.near-black}` background, four-column layout on desktop. Column headings in `{typography.spec-label}` `{colors.primary}` uppercase; links in `{typography.body-sm}` `{colors.on-dark}` with hover shift to `{colors.gold-light}`. A 20%-opacity gold divider separates the link columns from the legal strip below. The wordmark repeats in `{colors.primary}` at reduced `{typography.logo-display}` scale, anchoring brand identity at page bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen `{colors.dark-canvas}` overlay; hero headline drops to `{typography.display-md}`; spec table scrolls horizontally; guitar gallery thumbnails scroll in horizontal rail; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links with overflow into hamburger; hero at 60vh; craftsmen strip copy wraps to two columns; spec table and gallery stack vertically on PDP |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with dropdown panels; hero at 80vh; spec table and gallery sit side-by-side on PDP; section-header gold rules appear |
| Wide | > 1440px | Max-width container at 1440px centered; four-column product grid on collection pages; hero photography expands without crop; craftsmen strip copy constrained to 720px max-width for legibility |

### Touch Targets
- All buttons minimum 44×44px per WCAG 2.1 AA
- Nav links in mobile drawer minimum 48px tap height with 1px hairline separators
- Guitar gallery thumbnails minimum 56px height with `{spacing.sm}` gaps
- Product card entire surface tappable on mobile; price and title not separately linked

### Collapsing Strategy
- Nav: full horizontal with dropdowns → primary two links + hamburger → full hamburger overlay at < 744px
- Product grid: 4-col (wide) → 3-col (desktop) → 2-col (tablet) → 1-col (mobile)
- Hero: full-bleed cinematic at desktop → 60vh at tablet → 50vh with text stacked above image at mobile
- Footer: 4-col → 2-col (tablet) → 1-col stacked (mobile); logo moves to top of footer stack
- Spec table: side-by-side with gallery on desktop PDP → stacked below gallery on tablet and mobile with horizontal scroll enabled

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specific icon set identified; custom guitar-hardware iconography (headstock, tuning peg, pickup illustrations) not extractable from static color scan
- Font weight range for ff-tisa-web-pro not confirmed — variable font axes unknown; weights above are inferred from common Tisa Pro licensing tiers
- Exact nav dropdown interaction (hover vs. click, animation duration, column layout) not confirmed from extracted data
- Product card hover shadow depth not measured — stated values are approximations from visual pattern inference
- Mobile navigation drawer blur or translucency level not confirmed
- Whether hero sections use video loops or static photography at desktop breakpoint not confirmed
- Cart and checkout color overrides on Shopify native flows not captured — may diverge from brand palette on payment pages
- Exact letter-spacing values for ff-tisa-web-pro at display sizes not measured; values are editorial estimates matching Tisa's known optical behavior
- Accent steel blue (#b0c5cb) precise usage context not confirmed beyond secondary surface appearances — may be a Shopify framework default bleeding into extraction
- `{colors.warm-gray}` (#dedede) and `{colors.warm-mid}` (#444444) usage contexts not mapped to specific components from scan data
