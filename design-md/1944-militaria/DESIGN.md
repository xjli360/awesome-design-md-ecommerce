---
version: alpha
name: "1944 Militaria"
source_url: "https://www.1944militaria.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The year in the brand name is a credential, not a conceit — 1944 signals that every artifact in this store is calibrated to a specific historical moment, and the visual system honors that weight through a palette drawn directly from the era's material culture. Deep navy uniform blue (#2a2c6b) anchors primary surfaces: a color close enough to wartime officer dress blues to read as archival rather than invented. Military olive (#5a7d2c) functions as the secondary accent — not a trendy sage but a true field-drab green that sits alongside the navy the way a service ribbon sits against a jacket, the most brand-distinctive color in the extracted set. Warm amber cascading through rust (#f68721 through #d4612c) handles promotional heat — sale callouts, featured badges, urgency tiers — evoking aged brass hardware rather than generic e-commerce orange. Type runs in Lato, a humanist sans-serif that balances ledger-like legibility with enough warmth to feel like archival labels transcribed to screen; Open Sans handles secondary copy at 14–16px across dense catalog pages where condition grades, provenance notes, and lot numbers compete for attention. Button radii stay low at {rounded.xs}, avoiding the pill softness of lifestyle retail in favor of institutional precision. Product cards give photography maximum surface area on clean white canvas (#ffffff), with olive condition badges marking authenticated pieces and amber tags flagging featured lots. The nav carries deep navy as a full-width banner with reversed white type — visual shorthand for authority and provenance. Spacing inside individual product listings is generous to let object detail read clearly, while the category rail and filter sidebar compress to serve the collector who moves fast through deep inventory. The footer grounds in dark steel-blue (#194769), where authentication policies and shipping guarantees sit in small caption type that reads like fine print in an auction house catalog.

colors:
  primary: "#2a2c6b"
  primary-active: "#222d65"
  primary-disabled: "#9496b4"
  accent-olive: "#5a7d2c"
  accent-olive-hover: "#4a6a22"
  accent-amber: "#f68721"
  accent-amber-deep: "#d4612c"
  accent-rust: "#d15d2d"
  steel-blue: "#194769"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#555555"
  hairline: "#e2e8f0"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent-olive: "#ffffff"
  on-accent-amber: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  body-md:
    fontFamily: "'Open Sans', 'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-strong:
    fontFamily: "'Open Sans', 'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Lato', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Lato', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  lot-number:
    fontFamily: "monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-olive:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.on-accent-olive}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-olive-hover:
    backgroundColor: "{colors.accent-olive-hover}"
    textColor: "{colors.on-accent-olive}"
    rounded: "{rounded.xs}"
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-accent-amber}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-amber-hover:
    backgroundColor: "{colors.accent-amber-deep}"
    textColor: "{colors.on-accent-amber}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-bar-utility-strip:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "4/3"
    padding: "{spacing.md}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  product-card-lot:
    typography: "{typography.lot-number}"
    textColor: "{colors.muted}"
  condition-badge:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.on-accent-olive}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sale-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-accent-amber}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  featured-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  price-was-now:
    wasTypography: "{typography.body-sm}"
    wasColor: "{colors.muted}"
    nowTypography: "{typography.price-display}"
    nowColor: "{colors.accent-amber-deep}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    overlayOpacity: 0.55
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  category-rail:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    borderBottom: "2px solid {colors.hairline}"
    activeUnderlineColor: "{colors.primary}"
    activeUnderlineHeight: 3px
    padding: "{spacing.sm} 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.body}"
  filter-sidebar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.steel-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0 {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Deep navy (#2a2c6b) fill with all-caps Lato at 0.8px tracking and {rounded.xs} corners; the squared geometry signals institutional authority rather than consumer approachability. Active state shifts to #222d65 via `button-primary-hover`; disabled washes out to #9496b4. Primary use: Add to Cart, Checkout, account registration — any action with transactional weight.

**`button-secondary`** — White fill with a 2px navy border and matching navy text, sharing the uppercase Lato treatment of the primary. Pairs alongside primary buttons for "Save to Wishlist," "View Details," or "Compare Items." On hover the navy fill inverts and text reverses to white, maintaining visual parity without competing hierarchy.

**`button-olive`** — Military olive (#5a7d2c) fill for authentication-forward or provenance-related actions: "Request Appraisal," "View Certificate of Authenticity," "Contact Specialist." The green carries categorical meaning — it marks the expert layer of the catalog experience. Deepens to #4a6a22 on hover.

**`button-amber`** — Warm amber (#f68721) for promotional urgency: "Make an Offer," sale-page CTAs, featured-lot purchase prompts, limited-availability alerts. Transitions to the deeper rust-amber (#d4612c) on hover, maintaining warmth without flashing to red.

### Product Cards

**`product-card`** — White surface card with 1px hairline border and {rounded.sm} corners. A 4:3 image ratio preserves the horizontal framing needed for medal groups, documents, and uniform photography where width conveys context. Title runs in title-md (16px Lato 600), price in price-display (22px Lato 700 in primary navy), lot reference number below in monospace caption. The condition badge pins to the top-left corner of the image overlay; any sale badge pins top-right. Cards on hover lift with a subtle box-shadow rather than a color shift, keeping focus on the artifact photography.

### Badges

**`condition-badge`** — Olive green (#5a7d2c) rectangle on {rounded.xs} corners with all-caps 11px Lato at 0.8px tracking. Label values: MINT, EXC, VG, GOOD, FAIR, RELIC. The green reads as authenticated, graded provenance rather than a decoration — collectors scan for it first.

**`sale-badge`** — Amber (#f68721) at identical size and weight to the condition badge. Appears on cards for reduced-price lots and seasonal clearance inventory.

**`featured-badge`** — Primary navy (#2a2c6b) for "Staff Pick," editorially curated pieces, and showcase catalog entries. The navy badge against a product photo reads as a curator's stamp rather than a promotional shout.

### Navigation

**`nav-bar`** — Full-width navy (#2a2c6b) at 60px height with reversed white nav-link type (14px Lato 600 at 0.3px tracking). A thinner utility strip (`nav-bar-utility-strip`) at 32px in #222d65 sits above it carrying shipping notices, currency selectors, and sign-in links in 12px caption type. Active category links use a white bottom-underline at 2px; no animated tabs or pill indicators — the register is closer to a library directory than a consumer app.

**`search-bar`** — White input with a 2px navy border echoing the button-secondary outline treatment. Can be inset in the nav-bar or positioned in a dedicated full-width row directly below it. Placeholder text in #555555 muted gray; the submit button fills navy. The border-focus style upgrades to a 2px navy solid on keyboard focus.

### Hero Banner

**`hero-banner`** — Full-width image band with a navy (#2a2c6b) overlay at 0.55 opacity over a period photograph — typically a battlefield scene, military vehicle, or group portrait. Display-xl heading (32px Lato 700) in white, body-md subtitle copy below, and a `button-amber` CTA for "Shop Featured Lots" or current campaign. Vertical padding at {spacing.section}; horizontal at {spacing.xl}. The overlay density ensures text legibility even on high-contrast archival photographs.

### Category Rail

**`category-rail`** — Light gray (#f2f2f2) background with a 2px hairline bottom border. Category labels in title-sm (all-caps 13px Lato 700 at 0.6px tracking) aligned horizontally with {spacing.lg} gaps. Active category marks with a 3px navy underline anchored to the label baseline. On mobile the rail scrolls horizontally with momentum snapping.

### Filter Sidebar

**`filter-sidebar`** — Light gray (#f2f2f2) background panel with 1px hairline border and {rounded.xs} radius. Section labels in title-sm, individual filter options in body-sm. Checkboxes use the primary navy for checked state. Price range inputs share the `text-input` spec. Appears as an inline sidebar at ≥ 744px; collapses to a bottom sheet drawer on mobile triggered by a "Filter & Sort" button.

### Footer

**`footer`** — Dark steel-blue (#194769) background with white body-sm text and caption-sized links. Three to four columns on desktop: catalog categories, customer service, authentication policies, and payment/trust badges. Link groups use title-sm headers in white at reduced opacity to create visual hierarchy without a second color. Collapses to a stacked accordion on mobile with caption-strong toggle labels.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger revealing a full-screen slide-over drawer in primary navy; search bar moves full-width below logo row; category rail scrolls horizontally with snap points; hero text drops to display-sm; footer stacks to single-column accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only with "More ▾" overflow; hero text at display-md; filter sidebar becomes a top drawer rather than inline; footer two-column |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav with category rail below; filter sidebar inline; hero full-bleed; footer four-column |
| Wide | > 1440px | Content max-width 1440px centered on wider viewports; product grid up to five columns; hero image crops to widescreen 21:9 aspect ratio |

### Touch Targets

- All buttons and interactive controls minimum 44×44px on mobile
- Product card tappable area covers the full card surface, not just the title link
- Condition badge taps on mobile open a tooltip explaining the grading scale rather than navigating
- Category rail items minimum 48px tall with {spacing.base} horizontal padding per item
- Filter checkboxes expand to full row width for easy tap targeting

### Collapsing Strategy

- Category rail: horizontal momentum scroll on mobile with per-item snap points; no truncation
- Nav: hamburger icon at < 744px; opens a full-height slide-over overlay in primary navy with the full category tree and search bar at top
- Filters: inline sidebar at ≥ 744px; bottom sheet drawer on mobile triggered by sticky "Filter & Sort" bar
- Price range inputs: stack vertically on mobile (minimum above maximum)
- Footer columns: each section collapses to an accordion row with caption-strong +/– toggle; all collapsed by default on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; Lato and Open Sans are confirmed present via font-family extraction but weight variant availability (e.g., Lato 900 Black) is not verified beyond Google Fonts defaults
- The amber-to-rust orange cluster (#f68721 through #d4612c) may partially derive from PayPal CTA button styling rather than brand-owned design tokens; assignments should be audited against non-payment-page screenshots before finalizing
- #253b80 and #179bd7 are PayPal brand colors; #ff5f00 and #eb001b are Mastercard brand colors — all four excluded from the brand palette as they appear solely in the checkout payment widget layer
- No meta theme-color detected; status-bar and PWA icon colors are unspecified
- Exact product card border-radius not confirmed from live extraction; {rounded.sm} (8px) is an informed estimate based on category conventions
- Icon system and glyph set not extracted; assumed to use a generic library (Font Awesome or similar) with no confirmed custom iconography
- Dark mode behavior is unspecified; no prefers-color-scheme CSS variables detected
- Mobile navigation drawer animation timing and easing not confirmed
