---
version: alpha
name: "Fanatics Authentic"
source_url: "https://www.fanaticsauthentic.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The authentication hologram seal — not the athlete's signature — is the product. That founding premise shapes every visual decision: provenance must read as valuable as the object it certifies. A near-black canvas (#0a0a0a) absorbs ambient color from stadium photography, letting gold certification accents (estimated #c9a227) function as ink on a certificate of origin rather than promotional callouts. The dark-field approach suppresses competing visual noise so the trust-tier hierarchy — Fanatics Authentic first-party auth, then PSA, JSA, and Beckett partner certifications — registers in the scanning eye before price does. Player photography bleeds edge-to-edge across hero sections with minimal framing; jersey numbers and arena lights establish emotional register before any copy loads. Typography runs a condensed sans-serif in bold 700-weight for athlete names, generous tracking maintaining legibility across grid densities of 12–24 product cards; all-caps surnames and category labels create a uniform scanning cadence while mixed-case body copy slows the eye for provenance detail. The fixed navigation bar is near-black and minimal — a thin gold underline on the active category avoids the visual weight of filled pills and sustains the premium register without clutter. Product cards reserve a dedicated certification badge strip at the card's lower edge ({rounded.xs} corners, {colors.authentication-gold} fill for first-party auth, {colors.badge-partner} for third-party certifications), making trust tier legible before the price block. Generous {spacing.lg} gutters in the product grid prevent the visual sense of overstock that would undermine the collectibles premium. The footer is a quiet credential wall — partner authentication logos rendered in {colors.muted} against {colors.surface-card}, signaling institutional backing without competing with the product pages above. {rounded.sm} cards and {rounded.xs} badge geometry echo a display case rather than a retail shelf — built for collectors who read terms of provenance before they check price.

colors:
  primary: "#c9a227"
  primary-active: "#a8821d"
  primary-disabled: "#3a2f0e"
  ink: "#ffffff"
  body: "#e8e8e8"
  muted: "#9e9e9e"
  hairline: "#2e2e2e"
  canvas: "#0a0a0a"
  surface-soft: "#141414"
  surface-card: "#1c1c1c"
  on-primary: "#0a0a0a"
  authentication-gold: "#c9a227"
  badge-partner: "#6b7280"
  error: "#e53935"
  success: "#43a047"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  label-auth:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.authentication-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.authentication-gold}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderActive: "{colors.authentication-gold}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    activeUnderlineColor: "{colors.authentication-gold}"
    activeUnderlineHeight: 2px
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    borderHover: "{colors.authentication-gold}"
    rounded: "{rounded.sm}"
    imageBorderRadius: "{rounded.xs}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.base}"
  authentication-badge:
    backgroundColor: "{colors.authentication-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-auth}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  partner-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.badge-partner}"
    border: "1px solid {colors.badge-partner}"
    typography: "{typography.label-auth}"
    rounded: "{rounded.xs}"
    padding: 3px 7px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    overlayScrim: "linear-gradient(to right, {colors.scrim} 0%, transparent 60%)"
  category-pill-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    activeBackgroundColor: "{colors.authentication-gold}"
    activeTextColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.authentication-gold}"
    height: 48px
  price-block:
    primaryColor: "{colors.ink}"
    originalPriceColor: "{colors.muted}"
    primaryTypography: "{typography.price-display}"
    originalPriceTypography: "{typography.body-sm}"
  certification-tier:
    firstPartyColor: "{colors.authentication-gold}"
    partnerColor: "{colors.badge-partner}"
    typography: "{typography.label-auth}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  partner-badge-row:
    backgroundColor: "{colors.surface-card}"
    logoColor: "{colors.muted}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.section}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — Gold `{colors.authentication-gold}` fill with `{colors.on-primary}` (near-black) label in `{typography.button-md}` (uppercase, 700 weight), `{rounded.sm}` corners, 48px height. Carries all highest-intent purchase actions: "Add to Cart," "Buy Now," "Checkout." Active state transitions to `{colors.primary-active}` (#a8821d); disabled state fades fill to `{colors.primary-disabled}` with `{colors.muted}` label. Uppercase tracking reinforces the certification language — this button reads as a stamp of intent.

**`button-secondary`** — Transparent background, 1px `{colors.ink}` border, white label in `{typography.button-md}`. Used for "View Details," "Compare," and modal-dismiss actions at the same 48px height as primary. On hover, a 10% white fill overlay signals interactivity without breaking the dark-surface language.

**`button-ghost`** — Transparent background with `{colors.authentication-gold}` border and label. Signals authenticated sub-actions: "View Certificate of Authenticity," "Download COA," "Verify Hologram." Keeps gold in context of provenance workflows without competing with the primary CTA.

### Text Input

**`text-input`** — `{colors.surface-soft}` fill, `{rounded.xs}` corners, 1px `{colors.hairline}` border transitioning to `{colors.authentication-gold}` on focus. Placeholder in `{colors.muted}`. The gold focus ring ties form interaction back to the authentication visual language throughout search, filter panels, and checkout flows.

### Navigation

**`nav-bar`** — Fixed 64px bar in `{colors.canvas}` (#0a0a0a). Category links use `{typography.nav-link}` (uppercase, 14px, 600 weight). The active category carries a 2px `{colors.authentication-gold}` underline rather than a filled-pill state — a deliberate choice to prevent visual competition with the product-level gold authentication badges below the fold. On mobile, the bar collapses to a logo-left / hamburger-right layout triggering a full-height dark drawer overlay.

### Product Card

**`product-card`** — `{colors.surface-card}` (#1c1c1c) background, 1px `{colors.hairline}` border transitioning to `{colors.authentication-gold}` on hover, `{rounded.sm}` outer corners, `{rounded.xs}` on image. Image occupies the upper 60% of the card. A certification badge strip (`{components.authentication-badge}` or `{components.partner-badge}`) anchors to the lower image edge. Athlete name in `{typography.title-sm}`, price in `{typography.price-display}`, sub-descriptor line (item type, edition) in `{typography.caption}` and `{colors.muted}`. Card padding uses `{spacing.base}` on all sides.

### Authentication Badge

**`authentication-badge`** — `{colors.authentication-gold}` fill, `{colors.on-primary}` label in `{typography.label-auth}` (uppercase, 10px, 0.8px tracking), `{rounded.xs}` corners, 4px 8px padding. Appears on product cards, hero callouts, and PDPs as the first-party provenance mark. Reserved exclusively for Fanatics Authentic certifications — partner certifications use `{components.partner-badge}` to maintain tier differentiation.

### Partner Badge

**`partner-badge`** — `{colors.surface-soft}` fill with a 1px `{colors.badge-partner}` border and matching `{colors.badge-partner}` label in `{typography.label-auth}`. Distinguishes PSA, JSA, and Beckett certifications visually from the gold first-party badge while maintaining consistent capsule geometry. On dual-certified items, `{components.authentication-badge}` and `{components.partner-badge}` appear side by side, establishing the trust hierarchy at a glance.

### Hero Banner

**`hero-banner`** — Full-bleed athlete photography with a left-weighted scrim (linear-gradient from `{colors.scrim}` at 0% to transparent at 60%), preventing text legibility issues while preserving image drama. Title in `{typography.display-xl}` (uppercase, 48px, 700 weight), body copy in `{typography.body-md}`. Primary CTA renders as `{components.button-primary}`. Minimum 480px height; feature drops and signing-day announcements stretch to full viewport height. No border-radius — hero imagery bleeds flush to viewport edges.

### Category Pill Filter

**`category-pill-filter`** — Scrollable horizontal row beneath hero or category headers. Inactive pills: `{colors.surface-soft}` fill, `{colors.body}` label, `{rounded.full}`, 8px 16px padding. Active pill: `{colors.authentication-gold}` fill, `{colors.on-primary}` label in `{typography.button-sm}` (uppercase). Desktop renders overflow arrows at row edges; mobile uses momentum scroll with snap points.

### Search Bar

**`search-bar`** — 48px height, `{colors.surface-soft}` fill, `{rounded.xs}`, integrated into the nav row on desktop. Border transitions from `{colors.hairline}` to `{colors.authentication-gold}` on focus. Type-ahead suggestions panel uses `{colors.surface-card}` background with `{colors.hairline}` row separators; matched query text highlighted in `{colors.authentication-gold}`.

### Price Block

**`price-block`** — Current price in `{typography.price-display}` (22px, 700 weight) and `{colors.ink}` (white). When on sale, original price renders as strikethrough in `{typography.body-sm}` and `{colors.muted}` inline to the right. No red sale color is used — the strikethrough pattern communicates discount without introducing a color that would clash with the gold authentication system.

### Partner Badge Row (Footer)

**`partner-badge-row`** — Footer credential section displaying PSA, JSA, Beckett, and authentication partner logos at `{colors.muted}` opacity against `{colors.surface-card}`. Separated from content above by a 1px `{colors.hairline}` border-top. Logos rendered greyscale to avoid color conflict with the gold primary system; wide padding (`{spacing.xl}` vertical, `{spacing.section}` horizontal) provides breathing room against the dark canvas.

### Breadcrumb

**`breadcrumb`** — `{typography.caption}` size, inactive segments in `{colors.muted}`, separator hairlines in `{colors.hairline}`, active segment in `{colors.ink}`. Positioned below the nav bar on category and PDP pages. Assists deep-catalog navigation for collectors moving between sport > player > item-type hierarchies.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + full-height dark drawer; hero drops to 320px min-height with stacked title → badge → CTA overlay; category filter pills scroll horizontally with momentum; search bar moves to a second nav row |
| Tablet | 744–1128px | Two-column product grid; nav shows primary sport categories inline, sub-categories in a "More" dropdown; hero at 400px min-height; search bar returns to nav row |
| Desktop | 1128–1440px | Three to four-column product grid; full nav with all categories inline and 2px gold underline active indicator; hero stretches to 540px or viewport height on feature drops |
| Wide | > 1440px | Content max-width capped at 1440px, centered; four-column product grid retained; hero photography gains additional horizontal bleed; partner badge row logos spaced further apart |

### Touch Targets

- All interactive controls minimum 44×44px on mobile
- Authentication and partner badge taps expand hitbox to full card row — card tap navigates to PDP
- Category pill filter minimum 36px height with 8px horizontal gap between pills
- Nav drawer links minimum 48px row height with `{spacing.base}` vertical padding each

### Collapsing Strategy

- Navigation collapses tier-by-tier: secondary sub-categories fold into expandable drawer sections before primary sport categories collapse
- Product card certification badge strip maintains a fixed 32px height at all breakpoints — provenance hierarchy does not collapse or truncate
- Hero text reorders to title → auth badge → CTA on mobile, body copy deferred below the fold
- Category filter degrades from arrow-overflow (desktop) to scroll-snap momentum (mobile) — no pills truncated or hidden
- Footer partner badge row collapses from a 6-column logo grid to 3-column at tablet and 2-column at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted**: The site returned "Access Denied" during crawl. All palette values — #0a0a0a canvas, #c9a227 gold, surface grays, muted tones — are estimated from Fanatics brand patterns and premium-collectibles dark-mode conventions. Verify every hex against live CSS before production use.
- **No fonts extracted**: Typography stack defaults to `'Helvetica Neue', Arial, sans-serif`. Fanatics may use a licensed or proprietary typeface (Gotham, Futura, or a custom variant). Inspect live font-face declarations before committing.
- **Authentication badge geometry unverified**: Exact hologram seal shape, gradient stops, and co-branding lockup rules for PSA/JSA/Beckett partnerships could not be confirmed from live markup.
- **Navigation structure unconfirmed**: Category hierarchy depth, mega-menu behavior, and exact search-bar placement are estimated from observed Fanatics patterns; actual DOM structure may differ.
- **Light mode unknown**: Whether a light-mode variant exists is unconfirmed. All tokens assume a dark-primary interface; a light-mode palette would require a separate surface and ink token set.
- **Sale and promotional badge treatment**: Exact shapes, color fills, and positioning of sale percentage badges relative to the price block could not be confirmed without live site access.
- **Product grid column counts**: Exact breakpoint column rules (3 vs 4 on desktop, fluid vs fixed gutter) are estimated; inspect the live grid implementation for precise values.
