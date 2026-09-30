---
version: alpha
name: "Transcat"
source_url: "https://www.transcat.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Calibration is the science of knowing exactly where you stand — Transcat's interface extends that principle to its own visual ground truth, with the sole confirmed extraction being #313131, a warm near-black that reads like an instrument panel rather than a design affectation. The company straddles two distinct business lines: direct equipment sales across 130,000+ SKUs from Fluke, Keysight, and Tektronix, plus an ISO/IEC 17025-accredited calibration services division that makes Transcat one of the few metrology vendors that sells the tool and then certifies it afterward. That dual mandate shapes the interface's load — a product catalog must carry dense technical specifications, model comparators, and manufacturer facets simultaneously, while a services portal must communicate compliance authority to quality engineers and procurement managers who read certification marks the way consumers read star ratings.

  The system font stack — -apple-system, Roboto, Segoe UI, and generic sans-serif fallbacks — confirms no custom typeface loads through detectable channels, likely blocked behind the Cloudflare anti-bot layer that prevented full extraction. A system-native type strategy suits the B2B catalog context: legibility and information density over brand voice. Product cards carry exceptional payload in this category — a single SKU entry needs manufacturer logo, model number, short description, availability state, price, calibration-service flag, and rental indicator simultaneously. The badge system does critical semantic work here, distinguishing calibrated from non-calibrated stock with color-coded pills that procurement teams scan faster than label text. Corner radii stay modest — `{rounded.sm}` on cards, `{rounded.xs}` on badges, `{rounded.md}` on CTAs — enough softness to signal commercial approachability without erasing the clinical authority that metrology customers require. The top utility strip, almost certainly rendered in #313131, anchors the page hierarchy with account and phone links before the main nav takes over.

colors:
  primary: "#004EA8"
  primary-active: "#003882"
  primary-disabled: "#99BDE3"
  ink: "#313131"
  body: "#444444"
  muted: "#767676"
  hairline: "#D9D9D9"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F5F6F8"
  surface-card: "#FFFFFF"
  surface-dark: "#313131"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  accent-orange: "#E85D04"
  success: "#1A7F37"
  warning: "#F59E0B"
  danger: "#C0392B"
  badge-calibrated-bg: "#EAF3FF"
  badge-calibrated-text: "#004EA8"
  badge-rental-bg: "#FFF4E5"
  badge-rental-text: "#B45309"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-strong:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  price-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  model-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px

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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 10px 22px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-cta-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-top-strip:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  mega-nav-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    height: 48px
    padding: 0 14px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspect: "1/1"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
  product-card-model:
    typography: "{typography.model-number}"
    textColor: "{colors.muted}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-lg}"
    textColor: "{colors.ink}"
  badge-calibrated:
    backgroundColor: "{colors.badge-calibrated-bg}"
    textColor: "{colors.badge-calibrated-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-rental:
    backgroundColor: "{colors.badge-rental-bg}"
    textColor: "{colors.badge-rental-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rowAltBackground: "{colors.surface-soft}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 360px
    paddingVertical: "{spacing.section}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-sm}"
    rounded: "{rounded.none}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    iconSize: 48px
  calibration-service-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    accentBorderTop: "4px solid {colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeTextColor: "{colors.ink}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption-strong}"
    borderTop: "4px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Solid `{colors.primary}` fill with white text at `{typography.button-md}` weight, 48px tall, `{rounded.md}` corners. The standard CTA for "Add to Cart," "Request Quote," and "Schedule Calibration." Active state compresses to `{colors.primary-active}`; disabled fades to `{colors.primary-disabled}` with the same radius intact.

**`button-secondary`** — White background with a 2px `{colors.primary}` border and primary-colored text at `{typography.button-md}`. Appears alongside the primary button as a peer action: "Compare," "Save to List," "View Datasheet." Identical height (48px) to the primary button so pairs stack and sit flush on mobile without height mismatch.

**`button-ghost`** — Transparent background, `{colors.primary}` text at `{typography.button-sm}`, `{rounded.sm}`. Used for low-hierarchy actions — "See All in Category," filter reset links, inline "Learn More" triggers. No border; relies on text color alone for identity and should only appear where surrounding context provides sufficient contrast.

**`button-cta-orange`** — `{colors.accent-orange}` fill reserved for high-urgency commercial actions: "Request a Quote," "Speak to a Specialist," time-bound promotional deadlines. Maximum one instance per viewport. Draws the eye against the blue primary system without overriding it.

### Navigation

**`nav-top-strip`** — A 36px `{colors.surface-dark}` utility bar that confirms #313131 as a deliberate brand surface, not incidental text color. Carries account links, phone number, and location selectors at `{typography.caption}` in `{colors.on-dark}`. Collapses entirely at mobile, with phone number promoted into the hamburger drawer.

**`nav-bar`** — 72px white bar below the top strip. Logo anchored left, category links center, search bar and account icon right. A 1px `{colors.hairline}` bottom border marks the boundary without shadow weight. Typography at `{typography.nav-link}` — 14px, weight 600 — keeps the many category labels scannable without competing with page headlines.

**`mega-nav-panel`** — Drops below the nav rail on category hover with a 3px `{colors.primary}` top accent stripe and a directional box-shadow. Typically four columns: sub-category links, manufacturer filter shortcuts, featured instrument or calibration promo, and a services quick-link panel. White background; `{typography.body-sm}` for all links. Collapses to a full-screen drawer on mobile.

### Search

**`search-bar`** — Full-width 48px input with a 2px `{colors.primary}` border at rest — the most visually prominent interactive element above the fold. B2B buyers arrive knowing part numbers or manufacturer model strings, so the search field is the primary discovery path, not browse. Includes inline typeahead for model number prefix matching and manufacturer name resolution.

### Product Cards

**`product-card`** — White `{colors.surface-card}` card, 1px `{colors.hairline}` border, `{rounded.sm}` corners. Internal stack: square image (1:1 aspect), model number in `{typography.model-number}` (monospaced, `{colors.muted}`), title in `{typography.title-sm}`, badge row (calibrated/rental flags), price in `{typography.price-lg}`, and an "Add to Cart" primary button. On hover, shadow lifts to `0 4px 16px rgba(0,0,0,0.10)` and border subtly darkens. Cards sit in a 3–4 column grid at desktop, 2-column at tablet, 1-column at mobile.

**`badge-calibrated`** — Light-blue pill (`{colors.badge-calibrated-bg}`) with `{colors.badge-calibrated-text}` uppercase text at `{typography.badge}`. Appears on product cards and the product detail page to signal that calibration service is available for this instrument. Critical procurement signal — quality engineers filter by this.

**`badge-rental`** — Orange-tinted pill (`{colors.badge-rental-bg}`) with `{colors.badge-rental-text}` text. Marks units available through the rental program. Same scale and padding as `badge-calibrated` so mixed badge rows align without height shifts.

### Specification Table

**`spec-table`** — Two-column alternating-row table on product detail pages. Header column labels rendered in `{typography.spec-label}` — 12px, uppercase, letter-spaced — over `{colors.surface-soft}`. Values in `{typography.body-sm}`. Odd rows alternate to `{colors.surface-soft}` for scan rhythm. No rounded corners; the table reads as clinical data, not UI decoration. Horizontal scroll on mobile.

### Hero & Banners

**`hero-banner`** — Dark (#313131) `{colors.surface-dark}` background with `{colors.on-dark}` headline at `{typography.display-xl}` and subtitle at `{typography.body-md}`. Minimum 360px height. Carries promotional or category messaging — new manufacturer partnerships, seasonal calibration campaigns, rental fleet expansion — with a primary CTA. Instrument or lab photography typically set as background behind a dark scrim.

**`promo-banner`** — Full-bleed `{colors.primary}` stripe, no radius, `{colors.on-primary}` headline at `{typography.display-sm}`. Used as a visual break between catalog sections or to surface service upsells (free shipping threshold, calibration turnaround time guarantee). Never stacked — one per page at most.

### Calibration Service Cards

**`calibration-service-card`** — White card with a 4px `{colors.primary}` top accent border — the visual differentiator from product cards. Internal padding at `{spacing.xl}` gives service descriptions room to breathe. Used in the calibration services section to present service types: lab drop-off, on-site calibration, rush turnaround, and certificate retrieval portal. The top accent stripe signals authority — these cards carry ISO/IEC 17025 credential weight.

### Footer

**`footer`** — Full-width `{colors.surface-dark}` background (confirming #313131 as a bookend surface), 4px `{colors.primary}` top border. Four-column layout at desktop: company links, services links, resource links, and contact/newsletter. Column headings in `{typography.caption-strong}`, links in `{typography.body-sm}` with `{colors.on-dark}` base color. ISO/IEC 17025 accreditation seal and NIST traceable calibration badge typically displayed here for compliance credibility. Collapses to single-column accordion at mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger replaces mega-nav; search bar full-width below nav strip; spec tables scroll horizontally; category tiles 2-up; top utility strip hidden |
| Tablet | 744–1128px | 2-column product grid; condensed mega-nav or top-level accordion; search bar inlined in nav; hero text scales to `display-md`; footer 2-column |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-nav with columns; top utility strip visible; hero at full `display-xl`; footer 4-column |
| Wide | > 1440px | Content max-width ~1400px, auto side margins; grid holds at 4-column; hero allows wider photography bleed |

### Touch Targets

- All buttons minimum 44px height; primary and secondary CTAs set to 48px
- Search bar 48px height for prominent mobile tap
- Nav drawer rows minimum 48px for accordion category links
- Badges non-interactive on mobile; full product card is the tap target
- Pagination buttons 36×36px with `{spacing.sm}` gaps for thumb accuracy

### Collapsing Strategy

- Mega-nav collapses to hamburger at < 744px; category tree becomes a full-screen slide-in drawer with accordion sub-levels
- Spec table converts from two-column side-by-side to label-above-value stacked layout at mobile
- Product card badge row wraps to second line if multiple badges present; price and Add to Cart remain on their own row
- Top utility strip (#313131 bar) hidden at mobile; phone number and account link promoted into hamburger drawer header
- Footer 4-column grid collapses to single-column accordion at mobile, 2-column at tablet; accreditation badges remain visible at all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Cloudflare anti-bot blocked full extraction.** The site returned a "Just a moment..." challenge page; only one hex value (#313131) and system font stacks were extractable. All other color tokens are inferred from B2B industrial brand conventions, not live site data.
- **Primary accent color unconfirmed.** `{colors.primary}` (#004EA8) is an inferred professional blue consistent with industrial instrumentation brands. The actual brand blue may differ — verify against Transcat's brand guide or browser DevTools computed styles once the live site is accessible.
- **Accent orange unconfirmed.** `{colors.accent-orange}` (#E85D04) is inferred for high-urgency CTA contrast; actual usage, presence, and hex are unknown.
- **No custom web font detected.** All font stacks are system defaults. Either Transcat uses no custom web font, or one is loaded via JavaScript after Cloudflare grants access. If a custom font exists (common in rebrands of B2B catalog vendors), update all `typography.*` fontFamily values.
- **Badge color semantics unverified.** Calibrated/rental badge color assignments are inferred from common metrology e-commerce patterns. Actual Transcat badge palette, labels, and icon usage require live site inspection.
- **Logo color variants unknown.** No SVG or raster logo assets were extractable; logo treatment on light vs. dark backgrounds is unconfirmed.
- **Dark mode support unknown.** No `prefers-color-scheme` media query signals or `theme-color` meta tag were present in the blocked response.
- **Navigation structure inferred.** Mega-nav column count, category taxonomy depth, and services routing hierarchy are estimated from Transcat's known business model, not observed from live markup.
