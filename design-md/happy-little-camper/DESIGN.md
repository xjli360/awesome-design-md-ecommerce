---
version: alpha
name: "Happy Little Camper"
source_url: "https://happylittlecampercare.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The brand's central design tension lives in the name itself — "camping" conjures pine resin and open flame, while "little camper" collapses it into the most tender possible idiom for an infant. Happy Little Camper resolves this contradiction by reading the outdoors as a proxy for purity: the forest is referenced not for adventure but for what it withholds — no chlorine, no synthetic fragrances, no petrochemicals. The palette follows this logic. A deep forest green (#3d7a5a) carries every primary CTA and masthead moment without feeling clinical; it reads as botanical credibility rather than brand aggression. Against a warm cream canvas (#fffef9), the green feels grown in rather than applied. A sunshine yellow (#f5c842) appears as an accent — the "happy" half of the name given visual form — while a dusty blush (#fae8d8) softens the ingredient and certification callout zones. Cards sit on soft sage surfaces (`{colors.surface-soft}`) with gently rounded corners (`{rounded.lg}`) that mirror the swaddle curve of a wrapped infant rather than the sharp geometry of a pharma shelf. Type scale leans toward rounded humanist sans-serifs at modest weights; display text stays under 800 weight to signal warmth over authority. The subscription nudge — recurring delivery is core to the business model — lives in a distinct moss variant (`{colors.primary-moss}`) that reads as a value-tier signal, not just a recolored button. Ingredient storytelling panels use generous `{spacing.section}` breathing room and oversized display labels to let plant-origin claims land at a glance. The overall system is designed for a sleep-deprived parent reading one-handed at 3am: high-contrast ink on canvas, minimum 16px body text, full-width CTAs on mobile, and badge clusters that communicate certification status without requiring a click.

colors:
  primary: "#3d7a5a"
  primary-active: "#2d5e43"
  primary-disabled: "#a8ccb8"
  primary-moss: "#2a5c3f"
  ink: "#1e2d25"
  body: "#3a4a3e"
  muted: "#6b7d71"
  hairline: "#d0dfd4"
  hairline-soft: "#e8f0ea"
  canvas: "#fffef9"
  surface-soft: "#f3f8f4"
  surface-card: "#ffffff"
  surface-warm: "#fdf5ec"
  on-primary: "#ffffff"
  sunshine: "#f5c842"
  sunshine-soft: "#fdf3c0"
  blush: "#fae8d8"
  blush-dark: "#e8c4a8"
  sky-soft: "#dcedf5"
  star: "#f5a623"

typography:
  display-xl:
    fontFamily: "'Nunito', 'Poppins', 'Quicksand', -apple-system, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  caption-xs:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.15px
  label-uppercase:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  ingredient-hero:
    fontFamily: "'Nunito', 'Poppins', system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -1px

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
    padding: 14px 28px
    height: 50px
    hover:
      backgroundColor: "{colors.primary-active}"
    disabled:
      backgroundColor: "{colors.primary-disabled}"
      cursor: not-allowed

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: 12px 28px
    height: 50px
    hover:
      backgroundColor: "{colors.surface-soft}"

  button-subscribe:
    backgroundColor: "{colors.primary-moss}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 50px
    badgeText: "Save 15%"
    badgeBackgroundColor: "{colors.sunshine}"
    badgeTextColor: "{colors.ink}"
    badgeTypography: "{typography.caption}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px

  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoMaxHeight: 40px
    ctaVariant: button-primary
    announcementBar:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.caption}"
      height: 36px

  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    shadow: "0 2px 12px rgba(30,45,37,0.08)"
    imageBorderRadius: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    padding: "{spacing.base}"
    badgePosition: top-left
    hover:
      shadow: "0 6px 24px rgba(30,45,37,0.14)"
      translateY: -2px

  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.body}"
    primaryCtaVariant: button-primary
    secondaryCtaVariant: button-secondary
    imageAspect: "4/3 mobile, 16/9 desktop"
    leafAccentColor: "{colors.primary}"
    maxContentWidth: 600px

  certification-badge:
    backgroundColor: "{colors.surface-soft}"
    border: "1.5px solid {colors.hairline}"
    rounded: "{rounded.md}"
    iconColor: "{colors.primary}"
    labelTypography: "{typography.label-uppercase}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.caption}"
    valueColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
    layout: icon-left

  ingredient-spotlight:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.xl}"
    headlineTypography: "{typography.ingredient-hero}"
    headlineColor: "{colors.primary}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.xxl} {spacing.xl}"
    imageShape: "{rounded.full}"
    imageSize: 200px
    accentDotColor: "{colors.sunshine}"

  subscription-module:
    backgroundColor: "{colors.surface-soft}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.lg}"
    headlineTypography: "{typography.title-md}"
    headlineColor: "{colors.ink}"
    savingsTagBackgroundColor: "{colors.sunshine-soft}"
    savingsTagBorder: "1px solid {colors.sunshine}"
    savingsTagTypography: "{typography.caption}"
    savingsTagColor: "{colors.ink}"
    ctaVariant: button-subscribe
    toggleActiveColor: "{colors.primary}"
    toggleInactiveColor: "{colors.hairline}"
    padding: "{spacing.lg}"

  size-guide-chip:
    backgroundColor: "{colors.surface-card}"
    selectedBackgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    selectedBorder: "1.5px solid {colors.primary}"
    padding: 8px 18px
    minHeight: 44px

  trust-strip:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline-soft}"
    borderBottom: "1px solid {colors.hairline-soft}"
    iconColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.body}"
    padding: "{spacing.lg} 0"
    gap: "{spacing.xxl}"
    layout: horizontal-centered

  review-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    shadow: "0 1px 6px rgba(30,45,37,0.07)"
    starColor: "{colors.star}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    authorTypography: "{typography.caption}"
    authorColor: "{colors.muted}"
    verifiedBadgeColor: "{colors.primary}"
    padding: "{spacing.lg}"

  bundle-selector:
    backgroundColor: "{colors.surface-card}"
    selectedBorder: "2px solid {colors.primary}"
    defaultBorder: "1.5px solid {colors.hairline}"
    rounded: "{rounded.md}"
    headlineTypography: "{typography.title-sm}"
    headlineColor: "{colors.ink}"
    savingsTypography: "{typography.caption}"
    savingsColor: "{colors.primary}"
    padding: "{spacing.base}"

  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    linkColor: "rgba(255,255,255,0.80)"
    linkHoverColor: "{colors.on-primary}"
    headlineTypography: "{typography.title-sm}"
    headlineColor: "{colors.on-primary}"
    dividerColor: "rgba(255,255,255,0.20)"
    padding: "{spacing.section} 0 {spacing.xl}"
    socialIconColor: "{colors.on-primary}"
    socialIconHoverColor: "{colors.sunshine}"

## Components

### Buttons
**`button-primary`** — Forest-green pill (`{rounded.full}`) at 50px tall, carrying "Add to Cart," "Shop Now," and checkout CTAs. On hover the fill deepens to `{colors.primary-active}` (#2d5e43); disabled state washes to `{colors.primary-disabled}` with `cursor: not-allowed`. The pill shape is consistent across all primary actions to reinforce the soft, rounded design language throughout the brand.

**`button-secondary`** — White fill with a 2px forest-green border and matching green text. Used for secondary actions like "Learn More" or "View All." On hover the background shifts to `{colors.surface-soft}`, giving a gentle sage tint that signals interactivity without competing with the primary CTA in the same viewport zone.

**`button-subscribe`** — A darker moss fill (`{colors.primary-moss}`, #2a5c3f) reserved exclusively for subscription and recurring delivery CTAs, visually distinct from one-time purchase actions. Carries a small sunshine-yellow badge chip reading "Save 15%" positioned over the button to communicate the financial benefit inline without a separate line of copy.

**`button-ghost`** — Transparent background, forest-green text, no border. Tertiary usage for "See All Reviews," "View Full Ingredients," and similar low-priority navigation actions. Its minimal visual weight lets it coexist with heavier components without creating hierarchy noise.

### Inputs
**`text-input`** — White card background, 1.5px hairline border, 12px radius. On focus the border upgrades to 2px primary green with no fill shift, preserving readability. Label sits above in `{typography.caption}` muted text. Used across email capture, checkout forms, and subscription management screens.

### Navigation
**`nav-bar`** — 68px tall on a warm white canvas with a soft hairline underline. Logo anchors left, navigation links centered in `{typography.nav-link}`, and a "Shop Now" `button-primary` pill anchors right. Stacks into a full-height hamburger drawer on mobile. Sits below a 36px forest-green `announcementBar` carrying shipping-threshold and promotional copy in white caption text.

### Product Cards
**`product-card`** — Softly rounded white cards (`{rounded.lg}`) with a diffuse shadow that lifts and intensifies on hover, translating 2px upward. Product image occupies the top portion with `{rounded.md}` corners. Title in `{typography.title-md}`, price in `{typography.price}` forest green, descriptor in `{typography.body-sm}`. Certification badge cluster stacks top-left over the product image at small scale.

### Hero
**`hero-banner`** — Full-width section on sage canvas (`{colors.surface-soft}`) with headline in `{typography.display-xl}`, subline in `{typography.body-md}`, and a stacked button pair (primary + secondary). Photography shows infants in natural-light outdoor or home settings — no sterile studio white, no clinical blue. On mobile the image stacks below the text block and both CTAs expand to full width.

### Certification Badges
**`certification-badge`** — Compact horizontal tiles with a brand icon, an uppercase label ("PLANT-BASED," "DERMATOLOGIST TESTED," "FRAGRANCE FREE"), and a brief descriptor in `{typography.caption}`. Border at 1.5px hairline, background in surface-soft sage, icon in primary green. Displayed in a horizontal scrolling row beneath the product hero image on the PDP.

### Ingredient Spotlight
**`ingredient-spotlight`** — Full-width editorial panels with oversized display text (`{typography.ingredient-hero}`, 56px, weight 800) naming the hero ingredient in primary green on warm cream (`{colors.surface-warm}`). A circular ingredient photograph (`{rounded.full}`) sits opposite the body copy. Sunshine-yellow accent dots mark supporting callout points. The XL panel radius (`{rounded.xl}`) echoes the pill-button language and separates these panels visually from the standard content grid.

### Subscription Module
**`subscription-module`** — A 2px primary-bordered toggle panel that lives on the PDP above the add-to-cart zone, distinguishing itself from surrounding product information without a modal overlay. Contains a one-time vs. subscribe toggle (active state in `{colors.primary}`), a sunshine-soft savings chip, a frequency dropdown, and a `button-subscribe` CTA. The border color matches the primary exactly, reinforcing that subscription is the recommended path.

### Size Guide Chips
**`size-guide-chip`** — Full-radius pill chips for diaper and wipe sizes (NB, S, M, L, XL). Inactive: white fill, hairline border, ink text. Active: primary green fill, white text, green border. Arranged in a horizontal chip row on the PDP, minimum 44px tall on all screen sizes for reliable touch targeting.

### Trust Strip
**`trust-strip`** — A full-width horizontal band between the hero and product grid, carrying four to five icon-and-label pairs: free shipping threshold, plant-based formula, dermatologist tested, money-back guarantee, and subscription flexibility. Primary-green icons, `{typography.caption}` labels in `{colors.body}`. Hairline borders top and bottom separate it from adjacent sections without competing visual weight. Scrolls horizontally with snap behavior on mobile.

### Reviews
**`review-card`** — White cards with a diffuse one-pixel shadow, a yellow star row in `{colors.star}`, body copy in `{typography.body-sm}`, and author attribution plus a verified-purchase badge in `{typography.caption}`. Three-column grid on desktop collapses to a single-column scrollable list on mobile.

### Bundle Selector
**`bundle-selector`** — Horizontal card options for pack sizes (1-pack, 2-pack, Subscribe & Save) positioned above the add-to-cart zone on the PDP. Selected state indicated by a 2px primary-green border; savings callout text in `{typography.caption}` primary green. Unselected state uses the default 1.5px hairline border.

### Footer
**`footer`** — Full primary-green background with white type, creating a strong chromatic bookend to the page. Navigation links at 80% white opacity shift to full white on hover. Logo rendered in white tint. Social icons in white, shifting to `{colors.sunshine}` on hover as a subtle warmth signal. Four-column grid on desktop collapses to a single-column accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero image stacks below headline; nav collapses to hamburger drawer; all primary CTAs expand to full width; trust strip becomes horizontal scroll with snap; footer becomes single-column accordion |
| Tablet | 744–1128px | Two-column product grid; hero splits 50/50 text and image; nav shows top-level links and hides tertiary items; trust strip shows three items; certification badge row fits without scroll |
| Desktop | 1128–1440px | Three-column product grid; hero content constrained to 600px max-width; full nav with CTA pill anchored right; trust strip displays all five items; ingredient spotlight panels show side-by-side layout |
| Wide | > 1440px | Four-column product grid; all sections constrained to 1440px max-width with centered content; ingredient spotlight panels constrained to 1280px inner width |

### Touch Targets
- All buttons minimum 50px height on mobile
- Size guide chips minimum 44px tall × 56px wide on mobile
- Nav hamburger touch target 44 × 44px
- Subscription toggle minimum 44px height
- Product cards fully tappable surface (no tap-only-on-text behavior)

### Collapsing Strategy
- Footer: four-column grid → single-column accordion with expand/collapse per section heading
- Navigation: horizontal link row → full-height overlay drawer triggered by hamburger icon
- Trust strip: static horizontal row → horizontal scroll with scroll-snap and partial next-item peek at right edge
- Product grid: 4 → 3 → 2 → 1 column across breakpoints
- Ingredient spotlight: text + circular image side-by-side → circular image above text on mobile
- Certification badge row: static row → horizontal scroll with scroll-snap on mobile
- Bundle selector: horizontal card row → vertical stacked list on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (likely JS-injected tokens or anti-bot protection); all palette values are inferred from documented brand materials and visual conventions for plant-based baby care — treat as provisional and verify against live brand assets
- No font families were extracted; typography stack uses Nunito/Poppins as category-appropriate rounded humanist sans-serifs, but the actual webfonts served by the live site may differ
- No meta theme-color was present; iOS and Android browser chrome accent color is unconfirmed
- Exact motion and animation specifications (easing curves, transition durations, scroll behavior) are not available from extraction
- Dark-mode support is unknown; no evidence of a dark-mode variant from the extraction pass
- Exact CSS breakpoints used in the live theme are unconfirmed; values above follow a common Shopify/DTC convention and should be verified
- Icon style, stroke weight, and fill treatment not confirmed; assumed 1.5px stroke-style icons based on category conventions
- Actual subscription savings percentage ("Save X%") not confirmed from extraction; 15% used as a common category placeholder
- Announcement bar copy, shipping threshold amount, and promotional cadence not available
