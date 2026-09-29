---
version: alpha
name: "Liberty Puzzles"
source_url: "https://www.libertypuzzles.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Thick-cut maple and hand-painted whimsy pieces translate into a digital palette that refuses to shout over the artwork. The canvas rests at #f3f3f3 — warmer than clinical white, cooler than cream — a neutral paper-stock tone that lets full-bleed puzzle photography command the viewport without chromatic competition. Against that muted ground, a single saturated stroke of craft blue (#07529d) marks every actionable surface: add-to-cart buttons, link hovers, and category navigation underlines. It reads less like tech-product blue and more like the pigment in a woodblock print. A golden amber (#ffc863) arrives sparingly as a secondary voltage — star ratings, sale callouts, and hover highlights that warm the interface the way afternoon light hits a puzzle table. Type runs in Assistant, a geometric sans-serif from Google Fonts with open apertures and a softness that avoids both the sterility of Helvetica and the quirkiness of display faces. Headlines land at weight 700 in modest sizes (28–32px), trusting the product imagery to carry visual weight rather than oversized type. Body copy at 16px/1.6 in weight 400 breathes generously — puzzle descriptions can run long, and the line-height rewards readers who linger. Corners land at `{rounded.sm}` (8px) on cards and buttons, friendly without trending toward the pill-shaped playfulness of consumer apps; this is a brand that sells to adults who frame their finished puzzles. The dark ink (#121212) pairs with a secondary charcoal (#242833) for navigation and metadata, creating subtle hierarchy without resorting to pure black. Spacing is generous throughout — `{spacing.section}` (64px) separates content blocks, giving each puzzle collection room to be appreciated as a gallery rather than a feed.

colors:
  primary: "#07529d"
  primary-active: "#044a8c"
  primary-disabled: "#a3c4e0"
  ink: "#121212"
  body: "#242833"
  muted: "#808080"
  muted-soft: "#a0a0a0"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f3f3f3"
  surface-soft: "#eaeaea"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-warm: "#ffc863"
  accent-warm-active: "#e6b045"
  accent-warm-soft: "#fff3d6"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Assistant', -apple-system, system-ui, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Assistant', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.17
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: 1.5px solid {colors.ink}
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    padding: 12px 16px
    height: 48px
    focusBorder: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: 0 1px 4px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    overflow: hidden
    boxShadow: 0 1px 3px rgba(0,0,0,0.06)
    hoverBoxShadow: 0 4px 12px rgba(0,0,0,0.1)
    imageAspectRatio: 1 / 1
    padding: "{spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-cta:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  category-nav-item:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: 2px solid transparent
    activeColor: "{colors.primary}"
    activeBorder: 2px solid {colors.primary}
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    padding: 12px 16px 12px 44px
    height: 48px
    iconColor: "{colors.muted}"
  difficulty-badge:
    backgroundColor: "{colors.accent-warm-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  piece-count-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  star-rating:
    color: "{colors.accent-warm}"
    emptyColor: "{colors.hairline}"
    size: 16px
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.accent-warm}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  image-zoom-overlay:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    boxShadow: 0 8px 32px rgba(0,0,0,0.15)
    padding: "{spacing.lg}"
---

## Components

### Buttons

**`button-primary`** — The primary action button uses craft blue (#07529d) fill with white text at weight 600. Corners sit at `{rounded.sm}` (8px), giving a clean but warm presence. On hover, the background darkens to `{colors.primary-active}` (#044a8c) with a subtle 150ms ease transition. Disabled state desaturates to a pale sky blue (#a3c4e0) with no cursor interaction. Used for add-to-cart, checkout, and form submissions.

**`button-secondary`** — A ghost-style button with a 1.5px solid ink border on a white fill. Text matches ink color at the same weight-600 button typography. On hover, the button inverts: ink fill with white text, creating a satisfying toggle effect. Used for secondary actions like "View Collection" or "Continue Shopping."

**`button-accent`** — A warm golden (#ffc863) fill with dark ink text, deployed sparingly for promotional CTAs and hero call-to-actions where the blue would blend into surrounding navigation. The amber warmth draws the eye toward seasonal features and gift-guide entries.

### Text Input

**`text-input`** — White background with a 1px hairline border (#dedede). On focus, the border transitions to primary blue and gains a subtle 2px box-shadow ring in rgba(7,82,157,0.15). Placeholder text renders in `{colors.muted}`. Error state swaps the border to a warm red with matching helper text below. Height standardized at 48px for touch accessibility.

### Navigation

**`nav-bar`** — Fixed top navigation with a clean white background and a single hairline bottom border. Logo sits left, search centered on desktop, cart/account icons right. Navigation links use `{typography.nav-link}` at weight 600. Active category is indicated by a 2px bottom border in primary blue rather than background color change — minimal and confident.

**`nav-bar-scrolled`** — On scroll, the nav compresses from 72px to 64px height, drops the bottom border, and gains a shallow box-shadow for depth separation without visual weight.

### Product Card

**`product-card`** — White card with `{rounded.sm}` corners and a barely-there box-shadow (0 1px 3px rgba(0,0,0,0.06)). Puzzle artwork fills a 1:1 aspect-ratio image container at the top. Below the image: title in `{typography.title-sm}`, piece count as metadata in `{typography.caption}`, and price in `{typography.price-sm}`. On hover, shadow deepens to 0 4px 12px and the card lifts 2px with a 200ms transition, inviting click-through. No border — shadow alone defines the card edge.

### Hero Banner

**`hero-banner`** — Full-width section with a dark charcoal (#242833) background and large puzzle artwork as a background image with a 40% dark overlay. Display text in `{typography.display-xl}` at white renders over the overlay. CTA uses the accent-warm button style for maximum contrast against the dark field. Minimum height 480px, vertically centered content.

### Category Navigation

**`category-nav-item`** — Horizontal scrollable row of puzzle categories (Artist, Theme, Piece Count, New Arrivals). Each item uses `{typography.nav-link}` with a transparent bottom border that fills to primary blue on active state. Hover triggers the same blue underline at 50% opacity. Horizontal padding keeps items scannable without crowding.

### Search Bar

**`search-bar`** — Full-width input with a magnifying glass icon inset left at `{colors.muted}`. Rounded at `{rounded.sm}` with hairline border. On focus, expands slightly (2px height increase) and border transitions to primary blue. Autocomplete dropdown renders as a `{colors.surface-card}` panel with `{rounded.sm}` corners and medium box-shadow.

### Badges

**`difficulty-badge`** — Small uppercase label with a warm amber-tinted background (#fff3d6) and dark body text. Used alongside puzzle listings to indicate difficulty level (Beginner, Intermediate, Expert). `{rounded.xs}` corners keep it compact.

**`piece-count-badge`** — Neutral gray background (`{colors.surface-soft}`) with the same badge typography. Displays piece counts (250, 500, 750, 1000+) as a quick scanning aid on collection pages.

### Star Rating

**`star-rating`** — Five-star display using `{colors.accent-warm}` (#ffc863) for filled stars against `{colors.hairline}` for empty. Size 16px inline with product cards, scales to 20px on product detail pages. Half-star fills supported via SVG clip-path.

### Footer

**`footer`** — Dark charcoal (#242833) background creating clear content termination. Text in `{typography.body-sm}` at the hairline color for comfortable contrast without harsh white. Link hover transitions to accent-warm (#ffc863), creating a golden warmth on interaction. Organized in a 4-column grid on desktop collapsing to stacked accordion on mobile.

### Announcement Bar

**`announcement-bar`** — Thin 40px bar pinned above the nav in primary blue with white text. Used for shipping thresholds, seasonal promotions, or production-time notices. Text centered in `{typography.caption}` with optional dismiss "×" icon right-aligned.

### Image Zoom Overlay

**`image-zoom-overlay`** — Modal overlay for puzzle detail imagery. White card with `{rounded.md}` corners and a generous box-shadow floating above a semi-transparent scrim. Allows pinch-zoom on mobile and scroll-zoom on desktop to inspect individual whimsy piece shapes.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces horizontal links, hero min-height drops to 320px, search moves into slide-down panel, footer collapses to accordion |
| Tablet | 744–1128px | 2-column product grid, nav stays horizontal but truncates to top 5 categories with "More" overflow, hero scales to 400px, category nav becomes horizontally scrollable |
| Desktop | 1128–1440px | 3-column product grid (occasionally 4 for collection pages), full nav visible, search bar expands inline, hero at full 480px+ height, footer renders full 4-column layout |
| Wide | > 1440px | Content max-width caps at 1440px with centered layout, product grid expands to 4 columns, increased `{spacing.section}` between content blocks, hero can extend to 560px |

### Touch Targets

- All interactive elements maintain minimum 44×44px touch area on mobile
- Product cards have full-surface tap target — entire card is clickable, not just the title
- Close buttons (modals, announcement bar) padded to 48×48px hit area despite smaller visual icon
- Category nav items have 16px horizontal padding ensuring finger-friendly gaps

### Collapsing Strategy

- Navigation collapses to hamburger icon below 744px; slide-in drawer from left with full-height overlay
- Product filters collapse from sidebar to a sticky bottom sheet with "Filter" toggle button
- Footer columns collapse to titled accordion sections; only one open at a time to save vertical space
- Piece-count and difficulty badges stack vertically below product title on mobile rather than inline
- Announcement bar text truncates with ellipsis on very narrow screens; link preserved

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one font family (Assistant) confirmed via extraction; the site may load additional display or decorative faces via JavaScript or web-font loaders not captured in static analysis
- No meta theme-color defined — mobile browser chrome color is unspecified
- Exact button padding, heights, and component border-radius values are inferred from visual conventions of Shopify Dawn-derived themes rather than directly extracted
- Animation timing functions and durations (easing curves, transition speeds) not available from static extraction
- Icon set details (line weight, grid size, custom vs. library) could not be determined
- Exact breakpoint values are estimated from common Shopify theme patterns; actual theme may use slightly different thresholds
- No dark-mode tokens detected — the site likely does not implement a dark theme variant
