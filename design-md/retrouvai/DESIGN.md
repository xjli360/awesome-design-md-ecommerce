---
version: alpha
name: "Retrouvai"
source_url: "https://www.retrouvai.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Retrouvai plants its flag with a forest-sage primary (#5a8c6b) — a gambit almost never seen in fine jewelry, where nearly every competitor reaches for black, champagne, or millennial pink — and builds its entire visual vocabulary outward from that single botanical decision. The brand name derives from the French *retrouver*, to rediscover, and the palette enacts that etymology at every level: the ink is not #000000 but #0c271c, a hunter green so dark it barely registers as color until placed against the warm cream canvas (#f8f6f0), which is richer and more ambered than clinical white, giving stone photography the same glow as light through aged linen. Accents arrive in antique gold (#cfb56b) — closer to aged book binding than fresh bullion — and a terracotta copper (#c5682e) that delivers editorial warmth without reading as seasonal. Secondary emotional tones include a dusty blush (#f9dee5) and muted mauve (#af7b88) reserved for campaign imagery; a muted navy (#282d74) anchors focus states and selected UI elements. Corners run a deliberate split: form inputs and product cards take {rounded.sm} (6px), collection filter tags and editorial badges are fully pill-shaped ({rounded.full}), and primary CTAs hold a flat sharp corner — the geometry of something precision-made rather than friendly-rounded. Spacing breathes with intention; section breaks stack at 64px and the product grid gives each piece room to be examined rather than scrolled past. The typographic system was not extractable (fonts load via JavaScript), but the editorial positioning of "Modern Heirlooms" points to a weight-400 display serif for collection headings and a quiet geometric sans for prose and UI labels — the combination that distinguishes heirloom craft from trend-cycle fashion.

colors:
  primary: "#5a8c6b"
  primary-active: "#356645"
  primary-disabled: "#a5dab7"
  primary-dark: "#0c271c"
  accent-gold: "#cfb56b"
  accent-gold-dark: "#6a5e2c"
  accent-terracotta: "#c5682e"
  accent-mauve: "#af7b88"
  accent-blush: "#f9dee5"
  accent-navy: "#282d74"
  ink: "#0c271c"
  body: "#556860"
  muted: "#507c5f"
  hairline: "#dedede"
  hairline-soft: "#f2f2f2"
  canvas: "#f8f6f0"
  surface-soft: "#f0ecdf"
  surface-card: "#fafafa"
  surface-warm: "#f0dad7"
  on-primary: "#f8f6f0"
  on-dark: "#f8f6f0"
  error: "#721c24"
  error-bg: "#f8d7da"
  error-border: "#f5c6cb"

typography:
  display-xl:
    fontFamily: "Georgia, 'Cormorant Garamond', 'Playfair Display', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Georgia, 'Cormorant Garamond', 'Playfair Display', serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Georgia, 'Cormorant Garamond', 'Playfair Display', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.28
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Georgia, 'Cormorant Garamond', 'Playfair Display', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.01em
  label-caps:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Neue Haas Grotesk', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
    textTransform: uppercase
  price:
    fontFamily: "Georgia, 'Cormorant Garamond', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 6px
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: none
    padding: 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    border: "1px solid {colors.error}"
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.error}"
  form-label:
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    marginBottom: "{spacing.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary-dark}"
  announcement-bar:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    padding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    subtitleColor: "{colors.body}"
    gap: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 600px
    imageObjectFit: cover
    overlayColor: "rgba(12, 39, 28, 0.15)"
  collection-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  collection-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: none
  gold-accent-rule:
    color: "{colors.accent-gold}"
    height: 1px
    width: 48px
    display: block
  editorial-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.accent-gold}"
    padding: "{spacing.xxl}"
    rounded: "{rounded.none}"
  swatch-button:
    size: 24px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
    touchTarget: 40px
  pdp-image-gallery:
    backgroundColor: "{colors.surface-card}"
    thumbnailSize: 72px
    thumbnailGap: "{spacing.xs}"
    thumbnailBorderSelected: "2px solid {colors.primary}"
    mainAspectRatio: "1/1"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    activeTextColor: "{colors.ink}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    subtotalTypography: "{typography.title-md}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.accent-gold}"
    headingTypography: "{typography.label-caps}"
    bodyTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Flat sage-green fill (#5a8c6b) with `{rounded.none}`, cream text (`{colors.on-primary}`), and uppercase lettering at 0.1em tracking. The zero-radius corner signals heirloom precision rather than friendly consumer softness — a deliberate departure from the rounded CTA idiom common to DTC. On hover the fill deepens to `{colors.primary-active}` (#356645); the disabled state bleaches to pale mint `{colors.primary-disabled}` (#a5dab7). Fixed at 48px height with wide horizontal padding so stone-photography CTAs never feel cramped against imagery.

**`button-secondary`** — Transparent with a 1px `{colors.ink}` border and identical sharp corners. On hover, the fill inverts to hunter green with cream text, creating a clean press-into-the-brand moment. Uses the same uppercase type as `button-primary`, maintaining the system's formal register.

**`button-ghost`** — Text-only link button in `{colors.primary}` sage, no border, zero padding, underlined. Used inline for lower-hierarchy actions: "View all," "Learn more," material education links.

### Navigation

**`nav-bar`** — 64px tall, `{colors.canvas}` cream background with a hairline bottom border separating it from page content. Logo renders in `{colors.primary-dark}` (#0c271c). Primary links use 13px uppercase sans at 0.06em tracking — a quiet horizontal tier that does not compete with product photography below. The `announcement-bar` above the nav carries the hunter-green (#0c271c) fill with cream `{typography.label-caps}` text, acting as the primary carrier for shipping thresholds, new collection alerts, and editorial calendar moments.

### Product Card

**`product-card`** — Zero-radius cards on near-white `{colors.surface-card}` with a 4:5 portrait image crop that gives each piece a gallery-portrait quality. Title renders in `{typography.title-sm}`; price uses the serif `{typography.price}` (18px, weight-400) to mark it as a number worth pausing on rather than scanning. Material descriptors and subtitles sit in `{colors.body}` (#556860). A `product-card-badge` pill — "New", "Bestseller", "Limited" — can overlay the image corner in sage fill with cream label-caps; it uses `{rounded.full}` to contrast against the card's sharp frame.

### Hero

**`hero`** — Full-bleed editorial module, minimum 600px tall, with a translucent hunter-green scrim (`rgba(12, 39, 28, 0.15)`) that slightly cools photography without flattening stone color. Title runs `{typography.display-xl}` (52px, weight-400 serif) in `{colors.ink}`, communicating that the brand trusts imagery and does not need heavy weight to assert authority. A single `button-primary` CTA sits below the headline, left-aligned, never centered.

### Collection Tags / Filters

**`collection-tag`** — Pill-shaped filter chips (`{rounded.full}`) in warm `{colors.surface-soft}` with hairline borders in the default state; active state fills sage and drops the border entirely, creating a clean flip from background to brand-color. Label uses `{typography.label-caps}` (11px, 0.1em tracking, uppercase) so the filter rail reads as structured metadata rather than another headline. A `gold-accent-rule` — a 48px × 1px horizontal line in `{colors.accent-gold}` (#cfb56b) — appears beneath section headings as a calibrated decorative gesture that ties layout rhythm to the jewelry category without becoming ornamental noise.

### Editorial Callout

**`editorial-callout`** — Full-width warm-cream panel (`{colors.surface-soft}`, #f0ecdf) used for brand storytelling: "About the Heirloom," material education panels, or founder prose. Title in `{typography.display-md}` (28px, weight-400 serif); body copy in `{typography.body-md}`. A `gold-accent-rule` appears between heading and body as a fine-jewelry gesture. No border-radius; the flush full-width break reads as a chapter separator in an editorial sequence. Secondary accent tones — `{colors.accent-terracotta}` (#c5682e) or `{colors.accent-blush}` (#f9dee5) — can tint background variants for seasonal campaigns.

### Product Detail Page

**`pdp-image-gallery`** — Square main image on `{colors.surface-card}` with a horizontal thumbnail strip below: thumbnails at 72px, gap `{spacing.xs}`, with a 2px `{colors.primary}` ring marking the active thumbnail. **`swatch-button`** — 24px circular metal/stone swatches (`{rounded.full}`) padded to a 40px touch target; selected state carries a 2px `{colors.ink}` ring, unselected a 1px hairline ring. **`breadcrumb`** — caption-scale sans in `{colors.muted}` with hairline separators, so provenance (e.g. Rings > Engagement) reads as orientation without competing with product text.

### Cart & Footer

**`cart-drawer`** — 400px right-anchored panel on `{colors.canvas}` cream, separated from page content by a 1px hairline left border. The drawer header strip uses `{colors.surface-soft}` to visually anchor the title and close button above line items. Subtotal label uses `{typography.title-md}` (16px, weight-500). The checkout CTA inside the drawer follows `button-primary` specs exactly. **`footer`** — Hunter green (`{colors.primary-dark}` #0c271c) ground with cream `{colors.on-dark}` text; column headings in `{typography.label-caps}`; links in `{colors.surface-soft}` turning `{colors.accent-gold}` on hover, the one place the gold accent performs a functional role rather than a decorative one.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered wordmark; hero height reduces to 420px with stacked text; announcement bar shows one message at a time |
| Tablet | 744–1128px | Two-column product grid; nav links visible but overflow items hidden; hero at 520px; editorial callout stacks image above text block |
| Desktop | 1128–1440px | Three or four-column grid; full nav exposed with hover mega-menu for collections; hero at 600px with optional side-by-side layout; PDP shows thumbnail column beside main image |
| Wide | > 1440px | Grid content capped at 1440px, centered; section padding expands to `{spacing.xxl}`; hero can run full viewport width with constrained text column |

### Touch Targets

- All primary and secondary buttons: 48px minimum height
- Nav hamburger and close icons: 44px × 44px effective touch region
- Swatch buttons: padded to 40px touch target despite 24px visual diameter
- Cart drawer close button: 44px × 44px in upper-right corner
- Collection tag filter pills: minimum 36px height on mobile to prevent mis-taps

### Collapsing Strategy

- Nav: wordmark + hamburger icon on mobile; full link row on tablet and above; cart icon and search icon always visible at all breakpoints
- Product filters: horizontal scroll pill rail beneath nav on mobile; collapsible sidebar panel on desktop
- PDP gallery: single swipeable image on mobile; horizontal thumbnail strip on tablet; vertical thumbnail column left of main image on desktop
- Editorial callout: stacked (image above, text below) on mobile and tablet; 50/50 horizontal split on desktop
- Footer: single stacked column on mobile; two-column grid on tablet; four-column grid on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families extracted — the site loads custom typefaces via JavaScript (common Shopify async font pattern). Display serif and body sans identities are inferred from brand positioning; actual font names require browser network inspection at runtime.
- Color usage context (which entries are text vs. background vs. accent vs. error) is inferred from luminance, frequency, and meta theme-color confirmation; DOM-level role assignment was not confirmed. The navy entries (#282d74, #353c9a) appear in the extraction but their specific role — focus rings, editorial blocks, email templates — could not be confirmed from static extraction.
- Hover, focus, and transition animation values not captured; fine jewelry brands in this tier commonly use slow opacity fades (200–300ms ease-out) and restrained motion; none confirmed.
- Mobile breakpoint exact values estimated from Shopify Dawn/Sense theme conventions; actual CSS media query boundaries not confirmed from source.
- Mega-menu or flyout structure for collection navigation assumed from category breadth; actual flyout layout and depth unconfirmed.
- Grid column count and spacing multiplier inferred from common Shopify theme conventions; not confirmed from computed styles.
- The terracotta (#c5682e) and mauve (#af7b88) accent roles — whether used on-site or only in email/campaign assets — could not be confirmed from static extraction.
