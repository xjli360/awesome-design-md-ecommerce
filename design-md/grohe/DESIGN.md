---
version: alpha
name: "Grohe"
source_url: "https://grohe.us"
captured_at: "2026-09-28T10:14:23.232707+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Grohe's US storefront presents as a premium plumbing-fixtures catalog built on a
  navy-and-white foundation. The confirmed brand action color is a deep navy,
  `#0F2B4B`, set as the default primary-button background in the site's own CSS
  custom properties, paired with white on-primary text. Body copy and navigation
  favor near-black grays (`#000000`, `#272727`, `#1C1F2A`) over pure black,
  suggesting a softened, editorial ink rather than stark contrast. A cluster of
  blues (`#3984BE`, `#165788`, `#48CBFF`) appears in the wider palette and is
  interpreted here as an accent family for links, hover states, and water/spa
  imagery consistent with a bath-and-kitchen brand, though exact usage contexts
  were not confirmed in the supplied rules. A single red (`#EA0202`) and green
  (`#22973F`) are treated as inferred alert/success signals. Typography is
  confirmed split between "Univers" (body/description text, e.g., UGC feed
  copy) and "Univers Extended" (feed titles, letter-spaced 4px), both licensed
  Linotype faces layered over system sans fallbacks (Helvetica Neue, Arial,
  Segoe UI). Manrope appears in the extracted font stack without a captured
  selector and is used here only as an inferred secondary UI font. Hairline
  dividers use near-transparent black (`rgba(0,0,0,0.05)`), reinforcing a
  quiet, low-contrast structural grid typical of a technical product catalog.

colors:
  primary: "#0f2b4b"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#272727"
  muted: "#6b7280"
  hairline: "#0000000d"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#3984be"
  accent-strong: "#165788"
  accent-bright: "#48cbff"
  success: "#22973f"
  alert: "#ea0202"
  border: "#e5e7eb"
  overlay: "#00000080"
  ink-secondary: "#1c1f2a"
  surface-deep: "#121f36"
typography:
  display-xl: {fontFamily: "'Univers Extended', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: 4px}
  display-md: {fontFamily: "'Univers Extended', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: 2px}
  title-md: {fontFamily: "'Univers', sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Manrope', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "'Manrope', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Univers', sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1.4, letterSpacing: 1px}
  button-md: {fontFamily: "'Univers', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  xxl: 40px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-primary}"
    overlayColor: "{colors.overlay}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.section}"
  footer:
    backgroundColor: "{colors.ink-secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  finish-selector:
    backgroundColor: "{colors.canvas}"
    swatchBorderColor: "{colors.border}"
    swatchActiveBorderColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.full}"
    gap: "{spacing.sm}"

## Components

**button-primary** uses the site's own confirmed navy (`#0F2B4B`) as its
default background with white text, matching the `--button-primary-bg-default`
custom property found in the submenu CSS. This is the highest-confidence
component mapping in this document.

**button-secondary** is a proposed outline treatment — navy text and border
on a transparent fill — for lower-emphasis actions like "View All" links seen
throughout the mega-menu structure. Hover/active states are not observed and
are proposed as a filled-navy inversion.

**text-input** is a proposed field style using a light gray border and muted
placeholder text, appropriate for the site search and contact/registration
forms referenced in navigation ("Register & Warranty Info," "Contact Us").
Focus-state styling was not observed.

**nav-bar** reflects the observed header behavior: white/near-black text that
toggles between white-on-transparent and black-on-white depending on scroll
and menu-open states (`.is-scrolled-80`, `.is-desktop-menu-open` rules
explicitly force `color: #000000` or `#FFFFFF`). This confirms a scroll-aware
header but not its precise pixel thresholds beyond "80."

**product-card** is inferred for faucet/collection tiles (Bauloop, Concetto,
Eurocube, etc.) implied by the extensive collection navigation. Card border
and radius are proposed; no card-specific selector was captured in evidence.

**hero** is proposed for the homepage banner region, using the deep navy
surface tone and largest display type, consistent with the dark-header
overlay behavior (`.header-text { color: #FFFFFF }` pre-scroll) implying dark
imagery sits behind a light logotype.

**footer** is proposed using the darker ink-secondary tone (`#1C1F2A`) for
visual grounding beneath a white-background catalog, given the multi-column
link structure evident in navigation depth (Parts & Support, Professionals,
Inspiration).

**badge** is proposed for sale/new/in-stock labels using the observed red and
uppercase caption typography (`.header-desktop-submenu-heading` confirms
12px/700/uppercase/1px tracking as an existing pattern reused here).

**search** is proposed using the light gray surface tone for the site search
field implied by "Shop parts" and product-lookup flows.

**finish-selector** is a category-specific proposed component for choosing
fixture finishes (chrome, brushed nickel, matte black), a standard plumbing
e-commerce pattern; circular swatches with a navy active ring align with the
confirmed primary color and full-radius token.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width       | Notes                                  |
|------------|-------------|-----------------------------------------|
| mobile     | 0–639px     | single-column, mobile submenu drawer    |
| tablet     | 640–1023px  | 2-column product grid                   |
| desktop    | 1024–1439px | mega-menu with image cards enabled      |
| wide       | 1440px+     | max-width content container             |

Touch targets should be a minimum of 44×44px; the mobile submenu footer item
padding (`16px`) observed in CSS is consistent with this guidance. Desktop
mega-menu (`.header-desktop-submenu-*`) should collapse to an accordion-style
mobile submenu below 1024px, as suggested by the presence of distinct
`.header-mobile-submenu-*` selectors already in the codebase.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no live
rendering, interaction states (hover, focus, active, disabled), or JavaScript
behavior were observed. Scroll-triggered header color changes are confirmed
to exist but exact scroll offsets and animation timing are not verified.
Border-radius values are entirely proposed defaults, as no `border-radius`
declarations were present in supplied evidence. Spacing values map to
confirmed CSS custom properties where noted (4px, 8px, 32px, 40px); all
other scale steps are proposed. Font role assignment for Manrope and Lato is
inferred from their presence in the extracted font-family list without a
captured selector; Old Standard TT's role is unknown and was excluded from
token mapping. Licensing/availability of "Univers" and "Univers Extended" as
web fonts was not verified and should be confirmed before implementation.
Mobile layout, product-card visuals, and cart/checkout UI were not present in
the supplied evidence and are therefore proposed patterns only.
