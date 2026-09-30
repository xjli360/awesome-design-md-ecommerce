---
version: alpha
name: "Panini America"
source_url: "https://www.paniniamerica.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Panini America anchors every surface in #091d3d — a navy so dark it reads almost black at thumbnail scale, holding arena photography and foil-card close-ups without competing for visual dominance. The brand's emotional center is the randomized pack: a sealed product that could contain a rookie card worth thousands or a serial-numbered parallel, which means every CTA is pitched at the elevated moment of anticipation — "what's inside." Gold cuts across this midnight field the way foil does on a Prizm Holo, signaling premium, licensed, official. The page architecture is built for collector urgency: product drops surface near the top of the hierarchy, countdown timers and "limited edition" copy appear close to imagery, and the overall palette resists the bright-white retail default in favor of a dark-gallery treatment that lets photography deliver full contrast. Navigation carries the weight of a dozen licensed leagues — NBA, NFL, NHL, MLB, FIFA, College — so the top rail is dense with category depth organized by sport. Card imagery is presented at generous scale with tight cropping on athlete faces, reflecting the hobby's fundamental value: the player, the moment, the signature. Type scales skew toward bold condensed styles that match the energy of a draft-night broadcast rather than a lifestyle brand's understated weight. Display headings arrive in all-caps at high weight, compressed to occupy as little horizontal space as possible so photography can push through at full width. The result is a digital storefront closer to a collector's vault than a traditional retail grid — drama-forward, dark-field, and always one click away from a product drop. The single confirmed brand color (#091d3d) anchors the palette; all secondary values are inferred from brand knowledge and standard sports-collectibles conventions.

colors:
  primary: "#091d3d"
  primary-active: "#061228"
  primary-disabled: "#3a4e6b"
  accent-gold: "#c9a032"
  accent-gold-bright: "#f0c050"
  accent-gold-muted: "#8a6e20"
  accent-red: "#c8102e"
  accent-red-active: "#a30d24"
  ink: "#ffffff"
  body: "#e8eaf0"
  muted: "#9aa3b2"
  hairline: "#1e3558"
  hairline-soft: "#142847"
  canvas: "#060f1e"
  surface-soft: "#0d1f38"
  surface-card: "#0f2341"
  surface-card-hover: "#152b4a"
  surface-elevated: "#132040"
  on-primary: "#ffffff"
  on-gold: "#091d3d"
  badge-live: "#c8102e"
  badge-new: "#c9a032"
  foil-shimmer: "#e8d080"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Impact, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Impact, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
    textTransform: uppercase
  display-md:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Impact, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  display-sm:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Impact, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Barlow Condensed', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 800
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Barlow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  price-display:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: -0.3px
  countdown:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 800
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
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    hover:
      backgroundColor: "{colors.accent-gold-bright}"
  button-primary-active:
    backgroundColor: "{colors.accent-gold-muted}"
    textColor: "{colors.on-gold}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.accent-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-gold}"
    padding: 13px 27px
    height: 48px
    hover:
      backgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
    height: 40px
  button-cta-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    hover:
      backgroundColor: "{colors.accent-red-active}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    focus:
      border: "1px solid {colors.accent-gold}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "2px solid {colors.hairline}"
    logoHeight: 36px
    dropdownBackground: "{colors.surface-elevated}"
    dropdownTextColor: "{colors.body}"
  nav-mega-menu:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    columnGap: "{spacing.xl}"
    activeTextColor: "{colors.accent-gold}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-md}"
    accentColor: "{colors.accent-gold}"
    overlay: "linear-gradient(to right, rgba(9,29,61,0.92) 40%, transparent)"
    minHeight: 560px
    ctaComponent: "button-primary"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    imageBackground: "{colors.surface-soft}"
    priceColor: "{colors.accent-gold}"
    hover:
      border: "1px solid {colors.accent-gold}"
      backgroundColor: "{colors.surface-card-hover}"
      transform: "translateY(-2px)"
  product-card-featured:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.accent-gold}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.accent-gold}"
    badgeBackground: "{colors.accent-gold}"
    badgeTextColor: "{colors.on-gold}"
    badgeTypography: "{typography.badge}"
    badgeLabel: "FEATURED"
  pack-reveal-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    hover:
      border: "1px solid {colors.foil-shimmer}"
      boxShadow: "0 0 12px rgba(232,208,128,0.25)"
  sport-category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    iconSize: 48px
    hover:
      borderColor: "{colors.accent-gold}"
      textColor: "{colors.accent-gold}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-hot:
    backgroundColor: "{colors.badge-live}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-limited:
    backgroundColor: "{colors.foil-shimmer}"
    textColor: "{colors.on-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-exclusive:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.accent-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.accent-gold}"
    padding: "3px 8px"
  countdown-timer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-gold}"
    typography: "{typography.countdown}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    dividerColor: "{colors.hairline}"
    labelTypography: "{typography.caption-sm}"
    labelColor: "{colors.muted}"
  drop-announcement:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    accentColor: "{colors.accent-gold}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    height: 44px
    focus:
      border: "1px solid {colors.accent-gold}"
  license-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "4px 10px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    borderTop: "2px solid {colors.hairline}"
    padding: "{spacing.section} {spacing.lg}"
    logoFilter: "brightness(0) invert(1)"

## Components

### Buttons

**`button-primary`** — Gold-fill CTA (`{colors.accent-gold}`) with navy text (`{colors.on-gold}`) in all-caps `{typography.button-md}`. This is the primary commerce action: "Shop Now", "Add to Cart", product drop entry points. Hover brightens to `{colors.accent-gold-bright}`; active press dims to `{colors.accent-gold-muted}`. The inversion of dark-on-gold (rather than light-on-dark) gives it maximum contrast against the dark canvas.

**`button-secondary`** — Transparent background with a 1px `{colors.accent-gold}` border and matching text. Sits alongside primary CTAs on product and landing pages where a second action is needed without competing hierarchy. Background fills `{colors.surface-soft}` on hover to provide depth without obscuring the border.

**`button-cta-red`** — Red urgency button (`{colors.accent-red}`) for flash sales, last-chance copy, and time-bounded promotions. The red maps directly to NFL/NBA licensed brand colors in product lines like Donruss, giving it contextual resonance beyond generic urgency. Darkens to `{colors.accent-red-active}` on press.

**`button-ghost`** — Minimal utility button with `{colors.hairline}` border and `{colors.body}` text. Used for low-priority secondary actions — "View Details", "See All", "Filter" — where gold would compete with primary commerce CTAs.

### Navigation

**`nav-bar`** — 64px `{colors.primary}` rail carrying the Panini logo at 36px height. Links render in `{typography.nav-link}` at `{colors.ink}`. A 2px `{colors.hairline}` rule along the bottom edge separates the nav from page content. On sport/category hover, a full-width `nav-mega-menu` drops below with multi-column sport grids.

**`nav-mega-menu`** — Full-width panel on `{colors.surface-elevated}` with league-organized columns (NBA, NFL, NHL, MLB, FIFA, College, Soccer). Active sport category highlights in `{colors.accent-gold}`. Column headers use `{typography.title-sm}`; links use `{typography.body-sm}`.

### Hero

**`hero-banner`** — Full-bleed panel at minimum 560px height. A directional overlay (deep `{colors.primary}` to transparent, right-facing) protects headline legibility over dark arena photography. Headline in `{typography.display-xl}` at `{colors.ink}`; subhead in `{typography.display-md}` with key words accented at `{colors.accent-gold}`. A `button-primary` CTA sits below copy with `{spacing.lg}` gap.

### Product Cards

**`product-card`** — Dark `{colors.surface-card}` card at `{rounded.md}` with 1px `{colors.hairline}` border. Upper region holds product photography on `{colors.surface-soft}`. Title in `{typography.title-md}`; price in `{typography.price-display}` colored `{colors.accent-gold}`. On hover, border transitions to `{colors.accent-gold}` and card lifts 2px — the gold border mirrors the foil-edge sensation of a physical premium card.

**`product-card-featured`** — Homepage spotlight variant with a persistent 2px `{colors.accent-gold}` border and `{colors.surface-elevated}` background. A "FEATURED" `badge-new` in `{typography.badge}` marks the top-left corner. Title uses `{typography.display-sm}` for added hierarchy.

**`pack-reveal-card`** — Sealed pack product variant. Hover triggers a `{colors.foil-shimmer}` border and a soft gold glow shadow, echoing the physical sensation of a holographic parallel. Signals that the product contains randomized collectibles with variable value.

### Badges

**`badge-new`** — Gold label (`{colors.badge-new}`, `{colors.on-gold}` text) for newly released sets. Applied top-left over card imagery in `{typography.badge}` at 10px.

**`badge-hot`** — Red label (`{colors.badge-live}`) for trending or high-demand items. Can stack vertically beneath `badge-new` when both conditions apply.

**`badge-limited`** — Foil-shimmer fill (`{colors.foil-shimmer}`) for serialized or numbered editions — /25, /99, print run language. Echoes physical card scarcity signals.

**`badge-exclusive`** — Dark `{colors.primary-active}` background with `{colors.accent-gold}` text and border; reserved for Panini Direct exclusives and site-only drops where the channel exclusivity is the selling proposition.

### Sport Category Tiles

**`sport-category-tile`** — Square `{colors.surface-card}` tile with centered sport icon at 48px and `{typography.title-md}` label below. Border and label text transition to `{colors.accent-gold}` on hover. Arranged as a 6-up grid on desktop, collapsing to a swipeable horizontal row on mobile with edge-fade indicating overflow.

### Drop Announcements

**`countdown-timer`** — Number blocks in `{typography.countdown}` colored `{colors.accent-gold}` on `{colors.surface-soft}` panels. `{colors.hairline}` dividers separate hours, minutes, seconds. `{typography.caption-sm}` labels (HOURS, MINS, SECS) sit below each block in `{colors.muted}`.

**`drop-announcement`** — Full-width module for upcoming release events. Wraps `countdown-timer` alongside product key-art and a `{typography.display-md}` headline. A `button-primary` CTA sits below the countdown. Border: 1px `{colors.hairline}` at `{rounded.md}`. Gold accent words distinguish the product name from descriptive copy.

### Search

**`search-bar`** — `{colors.surface-card}` field at `{rounded.sm}` with a left-aligned search icon in `{colors.muted}`. Placeholder text in `{colors.muted}`. Focus ring: border transitions to `{colors.accent-gold}`. Appears in the nav bar at compressed width and as a full-width panel on category-landing pages.

### License Badges

**`license-badge`** — Small inline pill (NFL PA, NBPA, MLB, NHLPA, FIFA) in `{typography.caption}` with `{colors.hairline}` border and `{colors.body}` text. Kept subordinate to product imagery while confirming official licensing — critical in the trading card market where counterfeit risk affects collector confidence.

### Footer

**`footer`** — `{colors.primary}` background matching the nav, with a 2px `{colors.hairline}` top border. Body links in `{colors.body}` shift to `{colors.accent-gold}` on hover. Logo inverted to white via `brightness(0) invert(1)`. Column layout: Shop by Sport, Products, Company, Legal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero at 320px with stacked copy and full-width CTA; mega-menu becomes full-screen slide-in drawer; sport-category tiles collapse to swipeable horizontal row with edge fade; countdown digits scale down to `{typography.display-md}` |
| Tablet | 744–1128px | 2-column product grid; hero at 420px; mega-menu in two-column drawer; sport-category tiles in 4-up grid; nav links visible up to overflow point |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-menu dropdown on hover; hero at 560px with gradient overlay; countdown at full `{typography.countdown}` scale; license badges visible inline |
| Wide | > 1440px | Container max-width 1440px centered; hero image bleeds full viewport behind contained copy; 4–5 column product grid; footer three-column layout with logo lockup at left |

### Touch Targets

- All interactive elements minimum 44×44px tap area (buttons, nav links, sport-category tiles, card CTAs)
- Product card tap zone covers the full card surface — not limited to title or button region
- Countdown timer digits are non-interactive; the accompanying CTA button stretches full width on mobile
- Badge overlays occupy the top-left image quadrant only and do not intercept card taps

### Collapsing Strategy

- Top nav collapses to hamburger at < 744px; mega-menu becomes animated left-side drawer with sport accordion sections
- Sport-category row switches from fixed grid to swipeable horizontal scroll at < 744px; edge-fade gradient indicates overflow
- Hero copy stacks vertically on mobile (image as background or below text block) to guarantee CTA stays above the fold at 320px viewport width
- Footer link groups collapse to accordion expand-on-tap on mobile; single column layout
- Badge priority on mobile when multiple apply: Limited > Hot > New > Exclusive — display only the highest-priority badge per card to prevent overlap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color was extracted (#091d3d); all other palette values — gold accent, red urgency, dark canvas tones, surface layers — are inferred from brand knowledge and sports-collectibles visual conventions, not confirmed from live site extraction
- Zero font families were captured; all typography stacks (Barlow Condensed, Barlow) are inferred from the bold condensed aesthetic typical of trading card brand design — actual site fonts may differ and should be verified via browser DevTools
- No meta theme-color was present, suggesting JS-rendered design tokens or anti-bot blocking during extraction
- Button and card border-radius values are estimated (`{rounded.sm}` = 4px, `{rounded.md}` = 8px) from sports-adjacent brand conventions — actual values unconfirmed
- Hover/transition timing (duration, easing curves) not captured
- Exact gold hex (#c9a032) is inferred brand knowledge — the specific value used in the live logo and UI may differ by a few ticks toward orange or toward yellow
- Licensed-league logo usage rules, clearspace requirements, and co-branding constraints are not reflected
- Mobile nav behavior (drawer animation direction, accordion vs. flat list) is inferred, not observed from live site
- Foil/shimmer animation specifics for premium product lines (Prizm, Select, National Treasures tier) — keyframe details, shimmer angle, duration — are not captured
- Dark-mode vs. light-mode variant availability is unknown; the dark canvas treatment may be the only mode or may coexist with a lighter product-detail view
