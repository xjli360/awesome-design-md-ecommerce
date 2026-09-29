---
version: alpha
name: "Courant"
source_url: "https://staycourant.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Espresso brown (#50280f) behaves here the way premium leather behaves on a product — it grounds every primary CTA, selected state, and category header in a color with material memory rather than digital convention. Courant's wireless charging category carries a peculiar design tension: the products photograph as warm and analog (leather charging pads, woven desk organizers), yet the brand name and page architecture lean into precision — "Wireless Charging, Perfected" announces craft as engineering. That tension resolves through a warm off-white canvas (#f9f8f4) that reads more like cream paper than a web-standard white, with priori-sans typography giving body copy and product labels a humanist authority — neither the coldness of geometric sans-serif nor the expressiveness of editorial type. The palette carries a secondary amber layer (#b15019) that bridges the deep primary brown toward product photography tones, while the near-black ink (#1c1a1a) — warmer than neutral #000 by just enough — runs all editorial copy. Accents emerge in two registers: a muted slate (#676986) for secondary navigation links and subdued UI states, and a teal (#0e7a82) that surfaces as a product-line signifier for charging-capable SKUs — the single cool note in an otherwise all-warm vocabulary. Surface treatment distinguishes Courant from competitors working in colder grays: the soft cream (#f5efe7) used for content blocks carries the warmth of undyed paper, making product photography land without contrast manipulation. Corners stay at {rounded.xs} to {rounded.sm} for inputs and cards — just enough softness to mirror the stitched edges of leather goods — while pill forms using {rounded.full} appear only on badges and promotional tags, creating deliberate contrast with the squared primary button system. Error and sale states draw on a high-contrast crimson (#d0011b) used as a functional signal, the brand's closest approach to alarm, kept structurally separate from the warm-neutral register that aligns charging technology with the premium desk aesthetic it targets.

colors:
  primary: "#50280f"
  primary-active: "#4f2810"
  primary-hover: "#6b3515"
  primary-disabled: "#979797"
  ink: "#1c1a1a"
  body: "#444444"
  muted: "#707070"
  muted-soft: "#979797"
  hairline: "#e5e5e5"
  hairline-soft: "#dedede"
  canvas: "#f9f8f4"
  surface-soft: "#f5efe7"
  surface-card: "#f7f7f8"
  surface-strong: "#f4f4f6"
  on-primary: "#ffffff"
  amber: "#b15019"
  slate: "#676986"
  navy: "#272d45"
  teal: "#0e7a82"
  error: "#d0011b"
  error-dark: "#a40900"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  caption-upper:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  price:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  price-sm:
    fontFamily: "'priori-sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 0px
    textDecoration: underline
  badge-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 8px rgba(28,26,26,0.08)"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    gap: "{spacing.sm}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(80,40,15,0.08)"
    imageScale: 1.02
  material-swatch:
    size: 28px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderUnselected: "2px solid transparent"
    gap: "{spacing.xs}"
  charging-indicator:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.teal}"
    iconColor: "{colors.teal}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    contentMaxWidth: 640px
    padding: "{spacing.section}"
  hero-dark:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
  collection-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    captionTypography: "{typography.body-sm}"
    gap: "{spacing.xl}"
  pdp-section:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    priceTypography: "{typography.price}"
    bodyTypography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    gap: "{spacing.lg}"
  reviews-widget:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    starColor: "{colors.amber}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-primary}"
    mutedTextColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.nav-link}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The primary CTA renders as a flat rectangle with no border radius in espresso brown (#50280f), with label text in {typography.button-md} at 0.5px tracking. The no-curve choice separates Courant from pill-shaped DTC defaults, reading as precision hardware rather than friendly lifestyle. Hover deepens to #6b3515; disabled falls to neutral gray (#979797) at reduced opacity, stepping cleanly away from the warm palette to signal unavailability without ambiguity.

**`button-secondary`** — A 1px outline variant in {colors.primary} against a transparent ground, sharing the square corners of the primary. On hover, background fills to {colors.surface-soft} to introduce warmth without adding a new color. Width is content-driven with consistent 27px horizontal padding.

**`button-ghost`** — Text-only underlined link-button used for "View All", "Learn More", and breadcrumb-adjacent actions. No container, no radius. Color uses {colors.ink} in editorial zones and {colors.on-primary} over dark hero fields.

### Badges

**`badge-pill`**, **`badge-new`**, **`badge-sale`** — Pill-shaped labels in {typography.caption-upper} (11px, 600 weight, 1.2px tracking, uppercase) are the only {rounded.full} elements in the vocabulary, creating deliberate contrast with the squared button system. Primary espresso for featured/wireless labels; near-black for "NEW"; error crimson (#d0011b) for sale pricing. All three share identical padding and height for consistent card overlay stacking.

### Forms & Inputs

**`text-input`** — Light hairline border ({colors.hairline}) on warm canvas ground shifts to a 1px primary-brown border on focus. The {rounded.xs} (4px) radius is the only curvature — just enough to signal interactivity. Placeholder text in {colors.muted}; error state uses {colors.error} border with inline message in {typography.caption} below the field.

### Navigation

**`nav-bar`** — 64px header in {colors.canvas} with the Courant wordmark in {colors.primary} at left and primary links in {typography.nav-link} (14px, 400 weight) at right. A single hairline bottom-border separates content at rest; on scroll, a faint brown-tinted shadow replaces it. Mega-menu panels drop full-width on hover with a {colors.canvas} background and tightly spaced category links in {typography.body-sm}.

**`promo-banner`** — A 40px espresso-brown announcement bar above the nav for promotional periods. Label text renders in {colors.on-primary} via {typography.caption-upper}, centered, with no close control by default.

### Product Cards

**`product-card`** — Square-cropped imagery (1:1 aspect) in a minimal card with no border at rest, {rounded.sm} radius, and title/price stacked below with {spacing.sm} gap. Title in {typography.title-sm}, price in {typography.price-sm}. On hover, a faint brown-tinted shadow lifts the card and the image scales to 1.02×. Badge overlays (NEW, SALE) sit at top-left of the image at {spacing.sm} inset.

**`material-swatch`** — 28px circles with a 2px selected-state ring in {colors.primary}. Used on PDPs and collection filters to communicate color and material variants. The swatch ring doubles as the only non-badge use of {rounded.full}.

### Product Detail Page

**`pdp-section`** — Two-column layout on desktop (imagery left, purchase module right) with {typography.display-md} title (28px, 400 weight), {typography.price} below, and {typography.body-md} description. Charging compatibility is surfaced via a `charging-indicator` chip using teal (#0e7a82) for the icon and label — the single place color branches from the warm-brown palette, reserved exclusively for technical capability communication.

**`charging-indicator`** — Small contextual chip appearing in the PDP purchase module and on product cards for charging-enabled SKUs. Background is {colors.surface-soft}; icon and label in {colors.teal}; typography is {typography.caption-upper}. Isolation to this component keeps the teal signal legible and non-decorative.

### Reviews

**`reviews-widget`** — Soft-surface card in {colors.surface-card} with star icons in amber (#b15019) — the same amber that bridges product photography tones. Rating number in {typography.title-sm}, review body in {typography.body-sm}. The amber star choice echoes leather tone rather than convention gold, keeping the review block inside the brand's warm register.

### Hero

**`hero`** — Full-bleed or large banner sections use cream ({colors.surface-soft}) as background for editorial contexts, with headline in {typography.display-xl} (48px, 300 weight) and subhead in {typography.body-md}. Light weight at large size gives editorial headlines a premium feel rather than heavy marketing energy. **`hero-dark`** inverts to {colors.scrim} background with {colors.on-primary} text for collection launches and seasonal campaigns.

### Footer

**`footer`** — Deep near-black ({colors.scrim}) ground with {colors.on-primary} navigation links in {typography.nav-link} and secondary legal text in {colors.muted-soft}. Columns separated by whitespace alone — no decorative rules or dividers.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with slide-out drawer; hero headline scales to display-md (28px); PDP goes single-column with sticky add-to-cart bar pinned to bottom; promo banner truncates to short text only |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links with overflow hamburger for secondary items; PDP stays single-column with purchase module below gallery; hero gains wider content padding |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with hover mega-menu panels; PDP activates two-column layout; hero uses side-by-side text and media split |
| Wide | > 1440px | Max-width container (1440px) centered with gutters; four-column product grid with increased card spacing; hero text constrained to 640px max-width with imagery filling remainder |

### Touch Targets

- All interactive controls minimum 44×44px on mobile
- `button-primary` and `button-secondary` fixed at 48px height across all breakpoints
- `material-swatch` circles expand to 36px minimum tap area on mobile despite 28px visual size
- `nav-bar` hamburger minimum 44px touch area
- Product card entire surface is tappable with no isolated action button

### Collapsing Strategy

- Navigation: full horizontal → primary links + overflow hamburger → full hamburger slide-out drawer
- Product grid: 4-col → 3-col → 2-col → 1-col at mobile
- PDP layout: 2-col media/purchase → 1-col stacked, purchase module moves below full-width gallery
- Hero: side-by-side text and media → stacked media above, text below on tablet and mobile
- Footer: multi-column grid → 2-col → single-column accordion on mobile
- Promo banner persists across all breakpoints; text truncates to essential claim

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font weight ladder unconfirmed**: priori-sans is identified from font-family stacks but its available weight range (300/400/500/600) and optical sizing behavior could not be verified from extraction; weights here follow premium DTC convention for humanist sans-serif display hierarchies.
- **Exact border-radius values not extracted**: Courant's actual CSS radius tokens were not available; values ({rounded.xs} = 4px, {rounded.sm} = 8px) are inferred from the brand's visual language and category conventions.
- **Spacing scale not confirmed**: No spacing system was extractable; values follow an 8px base grid standard to Shopify-built stores.
- **Teal usage scope**: Whether #0e7a82 is isolated to charging-feature UI or used more broadly as a secondary accent or product-line color could not be confirmed from static extraction alone.
- **Nav transparency behavior**: Whether the nav becomes transparent over hero imagery or maintains opaque canvas at all scroll positions was not determinable.
- **Animation and transition tokens**: No easing curves or duration values were available from the live site.
- **Icon system**: Courant likely maintains custom icons for product feature callouts (charging compatibility, material type); no SVG or icon font details were extractable.
- **Secondary image swap on product cards**: Whether cards reveal an alternate product angle on hover — a common DTC pattern — could not be confirmed from static extraction.
- **Slate (#676986) and navy (#272d45) usage**: These colors appear in the extracted palette but their specific component roles (navigation states, footer accents, or UI chrome) could not be precisely attributed without live interaction.
