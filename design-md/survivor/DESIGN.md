---
version: alpha
name: "Survivor"
source_url: "https://www.survivorcase.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every Survivor product detail page opens not with a lifestyle image but with a grid of certification marks — MIL-STD-810G, tested drop heights, IP ratings — treating engineering documentation as the primary visual event on the screen. The brand's palette runs on a white canvas with a near-black header bar (#0f0f0f), and the single chromatic decision that carries all urgency is a burnt-orange primary (#e85d1a) — the exact register of industrial safety marking, not the polished coral of consumer electronics. This orange appears on the Add to Cart button, the protection-tier active state, the hover ring on compatibility chips, and nowhere else; there is no secondary accent diluting its signal authority.

  Typography divides into two registers. Display headings use a condensed sans-serif — tall, tightly tracked at weights above 700 — compressing product names and protection tiers into impact-poster blocks that reference gear catalogs and military procurement sheets rather than editorial lifestyle copy. Body and specification text drops to a regular-weight system sans at 15–16px with expanded leading, giving compatibility tables and drop-test footnotes breathing room. All classification labels and section headers print uppercase with `{typography.label-caps}` letter-spacing, reinforcing the nomenclature of a technical datasheet.

  Product cards carry a compatibility-first information hierarchy: device model sits at the top of the card above the product name, a reversal of typical marketplace logic that reflects Survivor's SKU architecture — the right fit matters more than the product line name. A protection tier chip styled with `{typography.badge-caps}` appears directly below the device identifier, color-coded in tiers against the white card field. Cards use `{rounded.xs}` corners and a one-pixel `{colors.hairline}` border, reading as precision panels rather than soft marketplace tiles.

  The device compatibility selector — always the first filter step — uses a segmented chip row with `{rounded.xs}` form, not a dropdown, making the filter gesture feel closer to hardware configuration than a standard e-commerce facet. The footer shifts to a full-width dark band at `{colors.surface-dark}`, with all-caps section labels at wide letter-spacing, mimicking the column headers of a product specification sheet and closing the page in the same register it opened.

colors:
  primary: "#e85d1a"
  primary-active: "#c54b14"
  primary-disabled: "#f5c5a8"
  ink: "#111111"
  body: "#3a3a3a"
  muted: "#6e6e6e"
  hairline: "#dedede"
  hairline-strong: "#c0c0c0"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-raised: "#e8e8e8"
  surface-dark: "#0f0f0f"
  surface-dark-card: "#1c1c1c"
  on-primary: "#ffffff"
  on-dark: "#e0e0e0"
  tier-extreme: "#f5c518"
  tier-advanced: "#e85d1a"
  tier-basic: "#6e6e6e"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', system-ui, sans-serif"
    fontSize: 52px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Barlow Condensed', 'Arial Narrow', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
    textTransform: uppercase
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge-caps:
    fontFamily: "'Barlow Condensed', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.9px
    textTransform: uppercase
  label-caps:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Barlow Condensed', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow Condensed', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 50px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 50px
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 50px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    height: 64px
    borderBottom: none
  nav-search:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    deviceLabel:
      typography: "{typography.badge-caps}"
      textColor: "{colors.muted}"
    productName:
      typography: "{typography.title-md}"
      textColor: "{colors.ink}"
    price:
      typography: "{typography.title-md}"
      textColor: "{colors.ink}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    certAccentColor: "{colors.tier-extreme}"
    minHeight: 520px
  protection-tier-badge:
    typography: "{typography.badge-caps}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
    variants:
      basic:
        backgroundColor: "{colors.surface-raised}"
        textColor: "{colors.tier-basic}"
      advanced:
        backgroundColor: "{colors.surface-raised}"
        textColor: "{colors.tier-advanced}"
      extreme:
        backgroundColor: "{colors.surface-raised}"
        textColor: "{colors.tier-extreme}"
  mil-spec-badge:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.tier-extreme}"
    border: "1px solid {colors.hairline-strong}"
    typography: "{typography.badge-caps}"
    rounded: "{rounded.none}"
    padding: 6px 12px
  device-filter:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.surface-dark}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.on-dark}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.surface-dark}"
    typography: "{typography.badge-caps}"
    rounded: "{rounded.xs}"
    padding: 8px 14px
  compatibility-selector:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  drop-rating-callout:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    headingTypography: "{typography.display-md}"
    labelTypography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  section-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.muted}"
    headingTypography: "{typography.label-caps}"
    bodyTypography: "{typography.body-sm}"
    accentColor: "{colors.primary}"

## Components

### Buttons

**`button-primary`** — The primary CTA runs in burnt orange (#e85d1a) with uppercase condensed type at 16px/700 weight and a tight 4px radius, reading as a stamped-metal label rather than a rounded consumer pill. Hover steps down to `{colors.primary-active}` (#c54b14) with no shadow transition; the brand does not use elevation to signal interactivity. Disabled state fills with `{colors.primary-disabled}` (#f5c5a8), a washed-out tone that clearly removes affordance without introducing a new color. The button appears at full width on mobile, fixed width (min 220px) on desktop — always the tallest element in any CTA cluster at 50px.

**`button-secondary`** — Ghost style with a 1px `{colors.hairline-strong}` border and `{colors.ink}` uppercase text on a white canvas. Used for secondary actions like "Compare," "Save," and "Find My Model." Shares the same 50px height and 4px radius as button-primary so the two sit flush in side-by-side CTA rows.

**`button-dark`** — A solid dark fill (#0f0f0f) with `{colors.on-dark}` text, used in hero sections and footer calls to action where the orange primary would disappear against a dark background. Same condensed uppercase typography and 4px radius.

### Text Input

**`text-input`** — White fill, 1px `{colors.hairline}` border at rest, 2px `{colors.primary}` orange border on focus — the only moment orange appears in a form context. Placeholder sits in `{colors.muted}` at body-md size. Used in the site search flyout (inside the dark nav-search variant with a dark card background) and in email capture fields in the footer.

### Navigation

**`nav-bar`** — Full-width dark band (#0f0f0f) at 64px height. Logo left-aligned in white, primary links center or right, cart icon and search field right-aligned. The darkness of the bar creates an immediate separation from the white product canvas below, functioning as a command-line header rather than a branded identity billboard. No border-bottom.

**`nav-search`** — Search input rendered inside the dark nav in `{colors.surface-dark-card}` (#1c1c1c) with white text and muted placeholder. 4px radius, 40px height, no external border — recessed into the nav bar.

### Product Card

**`product-card`** — White fill with a 1px `{colors.hairline}` border and minimal 4px radius. The card's top element is always the device model name in `{typography.badge-caps}` (muted gray, all-caps, letter-spaced), above the product line name in `{typography.title-md}`. A `protection-tier-badge` sits between device label and product name. Price appears below the product name. No shadow — cards are flush-bordered panels in a specification grid, not floating marketplace tiles. Image occupies the top 60% of card area with no rounding.

### Hero

**`hero`** — Full-bleed dark background (#0f0f0f) with display-xl condensed heading in white and a subtitle at body-md. A row of mil-spec-badge elements (MIL-STD-810G, drop height, IP rating) appears as a certification strip between heading and CTA button. The cert accent color is `{colors.tier-extreme}` (#f5c518), the only yellow on the page, reserved for extreme-tier signaling. Minimum height 520px; background can hold a product image composited at low opacity or edge-cropped right-side position.

### Protection Tier Badge

**`protection-tier-badge`** — A flat, zero-radius pill in `{colors.surface-raised}` with text in one of three accent colors: Basic (`{colors.tier-basic}`), Advanced (`{colors.tier-advanced}`), Extreme (`{colors.tier-extreme}`). Uses `{typography.badge-caps}` — all-caps, 11px, 0.9px letter-spacing. The color of the text alone differentiates tiers; the background chip is always the same light gray. Appears inside product cards and on the PDP directly below the device compatibility line.

### MIL-SPEC Badge

**`mil-spec-badge`** — A rectangular (zero radius) badge in `{colors.surface-dark}` with a 1px `{colors.hairline-strong}` border and `{colors.tier-extreme}` yellow accent text for the standard identifier (e.g., "MIL-STD-810G"). Secondary text (e.g., "6FT DROP TESTED") runs in `{colors.on-dark}` at `{typography.badge-caps}`. These badges cluster in a horizontal strip on the hero and PDP, functioning as a certification row rather than a promotional callout.

### Device Filter

**`device-filter`** — Chip-style filter buttons in `{colors.surface-soft}` at rest, flipping to a solid `{colors.surface-dark}` fill on active selection. Uses `{typography.badge-caps}` for all labels. 4px radius. The chip row replaces a dropdown for the device brand selector — tapping a chip reveals the model sub-filter as a second chip row beneath it, stacked vertically on mobile.

### Compatibility Selector

**`compatibility-selector`** — A list of selectable model rows inside a bordered container. Each row uses `{typography.body-sm}` in `{colors.ink}`, with a 1px `{colors.hairline}` border at rest and a 2px `{colors.primary}` orange border on selection. Used inside the PDP to confirm exact device fit before add-to-cart unlocks. 4px radius on the container; rows themselves carry no rounding.

### Drop Rating Callout

**`drop-rating-callout`** — A section block in `{colors.surface-raised}` that displays the tested drop height as a large display-md number (e.g., "6 FT") in condensed uppercase, with a `{typography.label-caps}` descriptor below ("DROP TESTED"). The number color steps to `{colors.primary}` when the tier is Advanced or Extreme. Used on category and landing pages as a credibility banner between the product grid and the footer.

### Section Label

**`section-label`** — All-caps label-caps text in `{colors.muted}` with a 1px `{colors.hairline}` bottom border, functioning as a column header or category divider. Padding-bottom `{spacing.sm}`. Applied to grid section headers ("SHOP BY DEVICE," "PROTECTION LEVEL," "FEATURES") to maintain the datasheet register across the page.

### Footer

**`footer`** — Full-width `{colors.surface-dark}` band that closes the page in the same dark register as the nav. Section headings in `{typography.label-caps}` with `{colors.on-dark}` text; body links and legal copy in `{typography.body-sm}` at `{colors.muted}`. The Survivor logo or wordmark repeats in white. Orange (`{colors.primary}`) is used for one footer CTA link ("FIND YOUR CASE") to maintain brand signal even in the dark zone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; device-filter chips wrap to two rows; compatibility-selector expands full-width; nav collapses to hamburger + logo + cart icon; sticky Add to Cart bar appears fixed at viewport bottom; hero heading drops to 34px |
| Tablet | 744–1128px | Two-column product grid; device-filter chips in a scrollable horizontal row; nav shows top-level links, hamburger for sub-menus; sidebar filter panel at 280px width |
| Desktop | 1128–1440px | Three-column product grid; left sidebar at 240px for device and tier filters; hero restores display-xl at 52px; mil-spec badge strip displays inline in one row |
| Wide | > 1440px | Content constrained to 1380px max-width, centered; four-column product grid; hero background image expands edge-to-edge behind centered content column |

### Touch Targets

- All chip filters (`device-filter`, `protection-tier-badge` interactive) minimum 44px tall on mobile
- Nav hamburger and cart icon minimum 44×44px tap area
- Compatibility selector rows minimum 44px height
- CTA buttons fixed at 50px height across all breakpoints

### Collapsing Strategy

- Device filter and tier filter collapse into a "Filter" bottom sheet drawer on mobile, triggered by a fixed toolbar above the sticky cart bar
- Nav sub-menus collapse to a full-screen slide-in panel on mobile
- Product spec accordion on PDP collapses to expand/collapse sections on mobile, open by default on desktop
- Drop rating callout stacks vertically (number above label) on mobile, inline on desktop
- Certification badge strip in hero wraps to two rows on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors could be extracted from the live site; all palette values are inferred from brand-knowledge of rugged protection case aesthetics and are unverified against the actual site implementation
- No font-family stacks were extracted; typography uses Barlow Condensed (a common choice for military/industrial brands) as a best-guess display font with system-ui fallback — actual fonts may differ entirely
- No meta theme-color was found, so nav and hero background darkness level (#0f0f0f) is assumed rather than confirmed
- Protection tier color coding (Extreme = #f5c518 yellow, Advanced = #e85d1a orange, Basic = gray) is inferred from industry conventions, not extracted from Survivor's actual UI
- The platform was confirmed as non-Shopify but the actual platform is unknown, which may affect cart, filter, and PDP component patterns
- Whether Survivor uses a dark-header / light-body split or a fully light or fully dark theme is unconfirmed; the split approach here is a plausible inference only
- Specific drop heights, certification identifiers, and tier names ("Basic / Advanced / Extreme") are assumed from category conventions — actual Survivor tier names may differ
