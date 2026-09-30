---
version: alpha
name: "KiwiCo"
source_url: "https://www.kiwico.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fourteen extracted palette entries, ten of which are legitimate brand tokens — KiwiCo runs one of the widest hue spreads in DTC education, with orange-red (#d33600) functioning as the dominant CTA voltage while meta theme-color green (#07b261) claims browser-chrome territory before a single pixel of page loads. The subscription catalog is organized into named creature tiers — Panda Crate through Eureka and Doodle — each carrying its own accent, so the color system does wayfinding work that navigation labels alone could not. A second warm orange (#da532c) surfaces in promotional hero zones, warming the canvas without competing with the primary CTA button.

  Two typefaces divide the emotional load: Cherry (cursive display) runs at 36–48px on hero headlines and crate names, delivering the playfulness that an audience of 0–16-year-olds demands; Centra (a geometric sans) holds navigation, body copy, buttons, and labels, providing the structural clarity that builds parental confidence alongside the child appeal. Buttons are uniformly pill-shaped ({rounded.full}) — the shape appears on primary CTAs, ghost variants, and search inputs alike, leaving no hard corner anywhere a small hand might land.

  Cards float on a slightly sky-tinted off-white surface ({colors.surface-soft}, #f6fbfe) above pure-white card faces, creating a two-layer depth that makes product photography read as illustration rather than catalogue shot. Golden yellow (#dbb300) marks promotional badges, sale ribbons, and age-band callouts. The sky tint (#c5ecf4) appears as section fills behind hero modules and feature grids — large enough to register as a color field rather than an accent dot. Navy (#1c446b) anchors both body ink and the footer background, providing the dark mass that keeps the multi-hue system from reading as chaotic. The green family runs three stops — #1ab064 hover, #07b261 default, #008247 active — enough range to show state without introducing a new hue. Flat color does all the hierarchy work; no gradient appears in the primary UI.

colors:
  primary: "#d33600"
  primary-active: "#b82e00"
  primary-disabled: "#f0b3a0"
  brand-green: "#07b261"
  brand-green-dark: "#008247"
  brand-green-light: "#1ab064"
  accent-yellow: "#dbb300"
  accent-warm: "#da532c"
  accent-sky: "#c5ecf4"
  navy: "#1c446b"
  ink: "#1c446b"
  body: "#444444"
  muted: "#767676"
  hairline: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f6fbfe"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-green: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Cherry', cursive"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cherry', cursive"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  display-sm:
    fontFamily: "'Centra', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Centra', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Centra', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Centra', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Centra', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Centra', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Centra', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Centra', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'Centra', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  tag-label:
    fontFamily: "'Centra', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  crate-name:
    fontFamily: "'Cherry', cursive"
    fontSize: 24px
    fontWeight: 700
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-green:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.on-green}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-green-active:
    backgroundColor: "{colors.brand-green-dark}"
    textColor: "{colors.on-green}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: 12px 30px
    height: 52px
  button-ghost-green:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.brand-green}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.brand-green}"
    padding: 12px 30px
    height: 52px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    focusBorder: "2px solid {colors.brand-green}"
    padding: 12px 20px
    height: 52px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    shadow: "0 2px 12px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.navy}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
    rounded: "{rounded.none}"
  crate-tier-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.crate-name}"
    ageTypography: "{typography.tag-label}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.xl}"
    border: "2px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.brand-green}"
    padding: "{spacing.lg}"
  age-band-badge:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.navy}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  promo-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  subscription-ribbon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  gift-banner:
    backgroundColor: "{colors.brand-green}"
    textColor: "{colors.on-green}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Orange-red (#d33600) pill at 52px height with Centra Bold 16px and 0.5px letter-spacing. Used on every primary subscribe and shop CTA across the homepage, tier selector, and checkout entry points. Active state darkens to #b82e00 with no transition delay; disabled state washes to #f0b3a0 while retaining white text. No icon by default, but an arrow variant appears inside hero modules.

**`button-green`** — Brand-green (#07b261) pill, identical geometry to button-primary. Deployed when the page context is already warm with orange accents — gift flows, age-finder results, and the green-tinted hero variant. Active state steps to brand-green-dark (#008247).

**`button-secondary`** — White-fill pill with a 2px orange border and orange text. Appears in two-button hero rows (e.g., "Subscribe Now" paired with "Explore All Crates"), where the primary action is already occupied by button-primary and a lower-emphasis option sits beside it.

**`button-ghost-green`** — White-fill pill with a 2px green border. Used inside the gift-banner section where a solid green button would disappear against the green background, and in the footer CTA row for newsletter sign-up.

### Text Input

**`text-input`** — Pill-shaped (rounded.full) at 52px, matching button height so form rows stay optically level. Hairline border (#e2e2e2) at rest; focus state replaces the border with a 2px brand-green ring. Used in gift-card code entry, email capture modals, and the search overlay. Placeholder text in Centra Regular at body-md sizing.

### Navigation

**`nav-bar`** — White canvas, 72px tall, hairline bottom border. Logo mark left; subscription tier links center in Centra Semibold 15px; account, gift, and cart icons right. A drop shadow adds on scroll to communicate layer separation from page content. Collapses to logo + hamburger below ~1128px.

### Cards

**`product-card`** — White surface-card on the off-white canvas (#f6fbfe), rounded.lg corners, 16px padding, 10% black shadow at 12px blur. Title in title-sm, age range in tag-label uppercase, price in body-sm. Used across subscription tier grids, gift-finder results, and "Best For" recommendation modules.

**`crate-tier-card`** — Larger selector card for the subscription chooser flow. Crate name renders in Cherry (typography.crate-name) at 24px; age range in tag-label uppercase; price and cadence details in body-sm. Unselected state uses the hairline border; selected state snaps to a 2px brand-green border. No animation — the selection switch is instant and communicates via border color alone.

### Badges and Labels

**`age-band-badge`** — Sky-blue pill (#c5ecf4) with navy text in uppercase tag-label. Displays ranges like "Ages 0–36 months" on product cards and crate-tier-cards. Passive informational element — no tap/hover state.

**`promo-badge`** — Golden-yellow (#dbb300) rectangular badge with rounded.sm corners, ink-colored uppercase tag-label. Used for "Best Seller", "Gift Favorite", and seasonal callouts overlaid on product card top-left corners.

**`subscription-ribbon`** — Narrow orange-red strip overlaid at card corners with copy like "Save 30%". Typography.caption, rounded.xs, very tight padding. Communicates promotional urgency without covering the product image.

### Sections

**`hero-banner`** — Full-width section with sky-blue (#c5ecf4) fill, Cherry display-xl headline in navy, Centra body-md subhead, and a button-primary below. Color-field approach means the section is complete without image load; photography or illustration slots in as a right-aligned panel on desktop.

**`gift-banner`** — Full-width brand-green (#07b261) strip used for "Give the Gift of KiwiCo" modules near the footer. Centra display-sm headline and body-md body in white, CTA in button-ghost-green. Wide horizontal padding (spacing.section) at desktop collapses to spacing.xl on mobile.

### Footer

**`footer`** — Navy (#1c446b) background with white text. Four-column link grid at desktop: Shop, Learn, Company, Support. Column headings in title-sm (Centra Semibold), links in body-sm at reduced opacity on hover. Social icon row sits bottom-center. Compressed to two columns at tablet and single column at mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav; hero headline drops to display-md (36px Cherry); crate-tier-cards stack vertically; footer collapses to single column; gift-banner padding reduces to spacing.xl |
| Tablet | 744–1128px | Two-column product grid; partial nav (logo + hamburger or abbreviated link set); hero maintains full-width with reduced side padding; crate-tier-cards scroll horizontally |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav-bar with all tier links visible; hero two-column layout (text left, image right); footer four-column grid |
| Wide | > 1440px | Content max-width capped at ~1200px; side gutters expand proportionally; no structural change from desktop |

### Touch Targets
- All buttons minimum 52px height, minimum 44px wide
- Nav hamburger tap zone: 44×44px
- Product card: entire card face is tappable, not just the embedded CTA
- Age-band badges and promo-badges are passive labels with no required tap target

### Collapsing Strategy
- Top nav: full link row → logo + hamburger at < 1128px
- Crate-tier selector: horizontal radio-style row → vertical stacked cards on mobile
- Hero: two-column text-plus-image → single column with text above visual on mobile
- Footer: four columns → two columns at tablet → one column at mobile
- Gift-banner: horizontal padding steps from spacing.section (64px) to spacing.xl (32px) to spacing.lg (24px) across breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Cherry typeface weight range and OpenType features not confirmed from extraction — only a single display weight observed at large sizes
- Centra typeface full weight set not confirmed; Bold and Regular inferred from usage patterns; Light/Medium weights may exist
- Per-tier accent colors for each named crate (Panda, Koala, Atlas, Eureka, Tinker, Doodle, Da Vinci) not extractable without navigating individual sub-pages
- Exact box-shadow values not confirmed; `0 2px 12px rgba(0,0,0,0.10)` is inferred from visual density
- Social-platform blues (#1877f2, #4267b2, #007aff, #1d5fbf, #174a95) excluded from brand palette as third-party SDK colors from Facebook and Apple sign-in buttons
- Kiwi Icons glyph set and usage conventions not catalogued; present in font-family stack but not mapped
- Dark mode palette not observed; assumed unimplemented
- Animation/transition timing values not extractable from static extraction pass
