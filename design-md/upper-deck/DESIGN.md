---
version: alpha
name: "Upper Deck"
source_url: "https://www.upperdeck.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Championship-banner navy (#003388) stacked against a sharp, almost electric gold (#fbbb19) is the visual shorthand Upper Deck has held since it disrupted the sports card market in 1989 with the first authenticated hologram sticker — and the site carries that same gravitational contrast into every primary CTA, section header, and badge. Montserrat runs the entire typographic stack, pushed to weight 700–800 at display sizes to match the kinetic energy of sport and the trophy-case weight of the memorabilia being sold; at body copy and utility sizes the weight drops to 400–600, keeping reading comfortable across dense product grids. The palette extends into a supporting cast of mid-range blues — #1863dc, #005396, #0056a7 — that give depth to navigation tiers and category selectors without departing from the navy family; a lime accent (#75c32c) and hot orange (#f37627) spike product badges and sale callouts the way rookie-card parallels spike a set. A secondary gold vein in #fcc216 signals premium series and authenticated items, functioning as a chromatic trust mark before the user ever reads authentication copy. Corners lean toward rectangular with modest radii ({rounded.sm} to {rounded.md}), echoing the physical card stock that defines the product — there are no liquid pill shapes or heavy-rounded containers here. Product cards carry a drop-shadow treatment and thin hairline borders on a {colors.surface-card} ground, deliberately evoking the experience of turning a graded slab over in your hands; each card surfaces its authentication badge and serial reference inline at the tile level, not hidden behind a detail-page click. The upper nav collapses sport and category menus into a deep-navy mega-dropdown at desktop width, with icon-forward category tiles at mobile. Authentication and grading are first-class UI primitives throughout: hologram-badge components and serial-number labels render at the product-card level because for Upper Deck, the provenance IS the product — a card without authenticated paperwork is just cardboard, and the interface hierarchy reflects that.

colors:
  primary: "#003388"
  primary-active: "#002152"
  primary-disabled: "#5fa0c9"
  primary-mid: "#005396"
  accent-blue: "#1863dc"
  accent-blue-bright: "#146ff8"
  accent-gold: "#fbbb19"
  accent-gold-bright: "#fcc216"
  accent-green: "#75c32c"
  accent-orange: "#f37627"
  ink: "#212121"
  body: "#32373c"
  muted: "#55595c"
  muted-light: "#69727d"
  muted-soft: "#818a91"
  hairline: "#d0d5d2"
  hairline-soft: "#e3e3e3"
  canvas: "#ffffff"
  surface-soft: "#e3e3e3"
  surface-card: "#ffffff"
  surface-dark: "#002152"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#1863dc"
  error: "#cf2e2e"

typography:
  display-xl:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 42px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  card-eyebrow:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  serial-number:
    fontFamily: "'Montserrat', Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px

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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    border: "2px solid {colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    border: "2px solid {colors.on-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.accent-blue}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    logoHeight: 40px
  nav-mega-dropdown:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    borderTop: "3px solid {colors.accent-gold}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    shadow: "0 2px 8px rgba(0,0,0,0.12)"
    padding: "{spacing.md}"
    imageAspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    overlayGradient: "linear-gradient(90deg, {colors.primary} 45%, transparent 100%)"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 520px
  badge-authenticated:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.accent-gold}"
    border: "1px solid {colors.accent-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-limited:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  series-banner:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    borderBottom: "3px solid {colors.accent-gold}"
    eyebrowTypography: "{typography.card-eyebrow}"
    titleTypography: "{typography.display-md}"
    padding: "{spacing.xl} {spacing.section}"
  graded-card-slab:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.md}"
    shadow: "0 4px 16px rgba(0,51,136,0.18)"
    labelBackgroundColor: "{colors.primary}"
    labelTextColor: "{colors.on-primary}"
    gradeTypography: "{typography.display-md}"
    serialTypography: "{typography.serial-number}"
  serial-number-label:
    textColor: "{colors.muted}"
    typography: "{typography.serial-number}"
    border: "1px dashed {colors.hairline}"
    padding: "{spacing.xs} {spacing.sm}"
    rounded: "{rounded.xs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    iconColor: "{colors.primary}"
    height: 44px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    borderTop: "4px solid {colors.accent-gold}"
    padding: "{spacing.xxl} {spacing.section}"
---

## Components

### Buttons
**`button-primary`** — Deep navy (#003388) fill with white Montserrat uppercase text at 700 weight and 0.5px letter-spacing that reads as confident rather than shouty. Hover state darkens to `{colors.primary-active}` (#002152); disabled washes to `{colors.primary-disabled}`. Use for primary CTAs: "Add to Cart," "Shop Now," "Buy Now."

**`button-secondary`** — Transparent background with a 2px solid navy border and navy text, matching primary button dimensions. Signals an alternative action — "Save for Later," "View Details" — without competing visually with the primary CTA.

**`button-ghost`** — White outline on transparent fill, designed exclusively for hero banners and dark-surface placements where a navy-fill button would vanish into the background. White border and text maintain legibility against `{colors.surface-dark}` and gradient overlays.

**`button-gold`** — Accent CTA using `{colors.accent-gold}` (#fbbb19) fill with dark ink text. Reserved for promotional urgency moments — "Shop the Drop," "Claim This Deal" — where the gold-on-navy proximity scores maximum visual contrast.

### Navigation
**`nav-bar`** — Full-width navy (#003388) header at 64px height with white Montserrat nav links at 13px/600 weight. Logo sits left-aligned at 40px height; utility icons (search, account, cart) right-aligned in white. The mega-dropdown (`nav-mega-dropdown`) activates on hover with a darker navy field and a 3px accent-gold top border marking the panel boundary — the gold line is the only warm note in an otherwise all-cool-blue navigation system.

### Product Card
**`product-card`** — White surface with a 1px hairline border and a subtle 2px/8px drop shadow that lifts imagery off the page. Image fills a 3:4 portrait ratio mirroring physical card proportions. Title renders in `{typography.title-sm}` ink text below the image; price in `{typography.price}` primary navy. Badge overlays — authenticated, limited, sale, new — stack top-left on the card image and are the first thing the eye hits before reading the title.

### Hero Banner
**`hero-banner`** — Full-bleed navy panel with right-side photography and a 90° gradient fade from solid navy to transparent, keeping headline text legible across all screen widths. Headline uses `{typography.display-xl}` at 800 weight; sub-copy uses `{typography.body-md}` in on-dark white. Minimum height 520px to establish visual authority at desktop. On mobile, image moves below the text block and the gradient is suppressed.

### Badges
Four badge variants handle the four key product states. `badge-authenticated` uses navy fill with gold text and a gold border — the hologram color-pair that Upper Deck made synonymous with authenticity. `badge-limited` inverts to gold fill with ink text for print-run and edition-limited items. `badge-sale` uses `{colors.error}` (#cf2e2e) for price-reduction urgency. `badge-new` uses `{colors.accent-green}` (#75c32c) for freshly listed releases. All four share `{typography.badge}` at 10px/700/uppercase with tight 3px vertical padding at `{rounded.xs}` corners — small enough to stack without overwhelming the card face.

### Graded Card Slab
**`graded-card-slab`** — The most brand-specific component on the site: a white-surfaced panel with a 2px hairline border, a navy-tinted directional shadow (18% opacity at `{rounded.md}`), and a top label strip in `{colors.primary}` carrying the grade in `{typography.display-md}`. A dashed-border `serial-number-label` sits below the grade, using `{typography.serial-number}` at 11px/600 to communicate provenance at a glance. This component functions as the premium product tile format for graded-card SKUs and authenticated memorabilia.

### Series Banner
**`series-banner`** — Full-width dark navy section divider with a 3px accent-gold bottom border. Uses `{typography.card-eyebrow}` at 10px/700/uppercase/1px tracking for the series eyebrow (e.g., "2024–25 SERIES") and `{typography.display-md}` for the set name. Appears as a row between product grid sections to organize the catalog by release.

### Search Bar
**`search-bar`** — A 44px-tall input with a heavier-than-standard 2px solid primary navy border to signal search as a primary browsing mode. Icon renders in `{colors.primary}`. Border weight remains on focus — no color shift needed, as the weight itself communicates interaction state without adding visual noise.

### Category Pills
**`category-pill`** / **`category-pill-active`** — Horizontal filter row for narrowing by sport, player, year, or set. Inactive state uses `{colors.surface-soft}` fill with `{colors.body}` text; active state flips to navy fill with white text. Both share full-radius `{rounded.full}` treatment — the one place where pill shapes appear, contained to this filter context only.

### Footer
**`footer`** — Dark navy (`{colors.surface-dark}`) field with a 4px accent-gold top border as the sole visual separator from page content. Column links render in `{colors.accent-gold}` against the dark field; body copy in on-dark white at `{typography.body-sm}`. The gold-on-navy footer mirrors the primary button color language, closing the page with the same brand voltage it opens with.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces full bar; hero banner shifts to stacked layout with image below headline; category pills scroll horizontally off-screen; graded-card-slab collapses to single-column with grade label above image |
| Tablet | 744–1128px | Two-column product grid; nav bar persists but mega-dropdown becomes a slide-in drawer; hero banner uses landscape crop at reduced min-height (~360px) |
| Desktop | 1128–1440px | Three- to four-column product grid; full mega-dropdown on hover; hero banner at full 520px height; series banners span gutter-to-gutter |
| Wide | > 1440px | Grid content caps at 1440px centered with passive side gutters; hero imagery extends edge-to-edge behind a max-width content overlay |

### Touch Targets
- All buttons and nav links minimum 44×44px touch area
- Category pills meet 44px height via vertical padding expansion on mobile
- Product card tap target covers full card face; badge overlays are decorative and do not create nested tap conflicts
- Serial-number labels are display-only, not interactive

### Collapsing Strategy
- Nav drops to hamburger at < 1024px; mega-dropdown becomes a full-screen slide-over with accordion sport/category tiers and back-navigation
- Hero sub-copy truncates to 2 lines on mobile; primary CTA button moves below the headline block
- Series banners reduce padding from `{spacing.section}` to `{spacing.lg}` on mobile and reduce eyebrow font tracking
- Footer columns stack to a single column with social icons row above legal link row

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values from live CSS extraction — `{rounded.*}` scale inferred from the physical-card aesthetic and common sports-collectible site patterns
- Font weights for specific heading levels not confirmed via extraction; Montserrat weight ladder (600/700/800) inferred from visual hierarchy norms for the brand tier
- Exact line-height and letter-spacing values not extracted — values are best-practice estimates for Montserrat at the given sizes
- Mega-dropdown column count, icon usage, and sport-tier grouping structure not confirmed
- Presence or styling of a promotional announcement bar above the nav not confirmed
- Dark-mode or alternate theme not confirmed from extraction
- Exact hero treatment (static image, video loop, parallax) not confirmed
- Graded-card-slab grade label formatting (grading service name, grade scale, label color variants by grade) not fully extractable from site data alone
