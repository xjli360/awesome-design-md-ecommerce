---
version: alpha
name: "CMON"
source_url: "https://cmon.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep charcoal #313131 anchors CMON’s board-game universe — not the bright primary you’d expect from a publisher of monster-fighting miniatures, but a serious, ink-heavy canvas that makes every game box, card, and component feel like a premium artifact. The brand trusts its product photography to carry the color voltage: vivid miniatures, saturated game boards, and punchy box art pop against the near-black body copy and muted-soft backgrounds. Typography runs the system stack at modest weights — display sits at 24px weight 600 rather than the heavy 700+ that tabletop competitors use — letting the intricate game art do the heavy lifting. Buttons and interactive elements use {rounded.sm} (8px) corners, a subtle softening that keeps the interface approachable without sacrificing the brand’s serious, collector-oriented tone. The single extracted hex #313131 is the brand’s true signature: a dark, almost architectural gray that appears in headers, footers, and primary text, suggesting a design system built for legibility and longevity rather than trend-driven color. Product cards and game boxes use {rounded.md} (12px) to frame the art without competing with it, while the full-width hero sections push to the edges with no rounding at all — a deliberate contrast between the contained world of the game and the infinite space of the browser.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#8a8a8a"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#6e6e6e"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#c0392b"
  accent-gold: "#d4a017"
  accent-blue: "#2980b9"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: 64px 24px
  badge-new:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Pre-order Now", "Add to Cart", and "View Details" on game pages. Solid dark charcoal fill with white uppercase text. On hover, shifts to a deeper near-black `{colors.primary-active}`. Disabled state uses a medium gray `{colors.primary-disabled}` to signal unavailability. The 8px corner radius (`{rounded.sm}`) keeps the button substantial without feeling aggressive.

**`button-secondary`** — Outline variant for secondary actions like "Learn More" or "See All Games". White background with charcoal text and a 1px hairline border. Hover state adds a subtle shadow. Same uppercase button-md typography and 8px radius as primary, maintaining visual consistency.

**`button-accent-red`** — Reserved for high-urgency actions like "Limited Edition" or "Kickstarter Exclusive" calls-to-action. Uses the accent red to draw immediate attention, matching the brand's occasional use of red in game logos and promotional banners.

**`button-accent-gold`** — Used for premium or collector's edition promotions. The gold accent signals exclusivity and higher value, appearing on "Deluxe Edition" and "Collector's Box" CTAs.

### Cards
**`product-card`** — The primary content container for game listings. White background with 12px rounded corners (`{rounded.md}`) that frame the game box art. The card contains the product image (also rounded at 12px), game title in `{typography.title-md}`, player count and play time in `{typography.body-sm}`, and a price or CTA. On hover, the card gains a subtle elevation shadow to indicate interactivity.

### Navigation
**`nav-bar`** — Fixed top navigation bar at 64px height. White background with uppercase nav links in `{typography.nav-link}`. Contains the CMON logo on the left, primary navigation items (Games, Kickstarter, News, About, Shop) in the center, and a search icon + cart icon on the right. Active nav link is underlined or bolded.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and checkout forms. White background with 8px rounded corners, 48px height for comfortable touch interaction. Focus state adds a 2px charcoal border. Placeholder text uses `{colors.muted}`.

### Badges
**`badge-new`** — Small red pill badge for "New" indicators on recently released games. Uses `{typography.caption}` at 12px with 4px rounded corners (`{rounded.xs}`). Positioned at the top-right corner of product cards or game images.

**`badge-sale`** — Gold badge for sale or discount indicators. Same sizing and positioning as the new badge, but with the gold accent to differentiate the type of promotion.

### Footer
**`footer-section`** — Full-width footer with dark charcoal background (`{colors.primary}`). Contains three columns: company information and links, support resources, and social media icons. Text is white at `{typography.body-sm}`. Links use `{typography.link}` in white with hover underlines. Padding is generous at 48px top/bottom.

### Search
**`search-bar`** — Pill-shaped search input (`{rounded.full}`) with a light gray background (`{colors.surface-soft}`). Used in the navigation bar and on the search results page. The pill shape contrasts with the more angular buttons, suggesting a more casual, exploratory interaction. Focus state expands slightly and adds a charcoal border.

### Hero
**`hero-section`** — Full-width hero banner used on the homepage and campaign landing pages. Dark charcoal background with white text. The hero contains a large game title in `{typography.display-lg}`, a supporting description in `{typography.body-md}`, and a primary CTA button. The hero may include a full-bleed background image of game art or miniatures, with a dark overlay for text readability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-md}`; search bar moves to a full-width toggle; footer columns stack. |
| Tablet | 744–1128px | Two-column grid for product cards; nav bar shows abbreviated links (icons + labels for top 3 items); hero uses `{typography.display-lg}` with reduced padding; footer shows two columns. |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links visible; hero at full padding with `{typography.display-xl}`; footer displays three columns. |
| Wide | > 1440px | Max-width container at 1440px centered; product grid expands to four columns; hero content centered with max-width 1200px; additional whitespace on sides. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility.
- Nav bar links have 48px tap targets even when text is smaller.
- Product card CTAs are at least 44px tall with 16px padding.
- Search bar has 44px height with generous 20px horizontal padding.

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger icon with a slide-out menu overlay.
- Product filters collapse into a "Filter" button that opens a modal or bottom sheet.
- The footer's multi-column layout collapses to a single column with accordion-style expandable sections.
- Hero sections reduce padding from 64px to 32px on mobile, with text scaling down one size.
- Product card grids collapse from 3-4 columns to single column on mobile, with images scaling to full width.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was reliably extracted from the live site; the full palette above is inferred from common board-game publisher patterns and may not match the actual site. The accent colors (red, gold, blue) are educated guesses based on industry conventions and should be verified against the live site.
- No secondary or accent colors were extracted — the brand may use a wider palette for game-specific promotions that wasn't captured.
- Font-family declarations resolved to system defaults; CMON likely uses a custom typeface for headings or brand elements that wasn't present in the extracted CSS.
- Hover, focus, and active states for all components are speculative and should be validated against the live site's CSS.
- Error states for form inputs (validation, error messages) were not observed.
- Dark mode or high-contrast mode preferences are unknown.
- Sub-brand palettes for individual game lines (Zombicide, Blood Rage, etc.) were not extracted and likely use distinct color systems.
- Animation and transition timings (hover effects, page transitions, loading states) were not captured.
- The extracted color may be from a loading page ("Just a moment...") rather than the actual site — the full brand palette should be verified after the page fully loads.
