---
version: alpha
name: "Blomberg"
source_url: "https://www.blombergappliances.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Blomberg's digital storefront opens with a dark charcoal navigation bar (#1a1e21) that pins the brand's compact red wordmark against near-black, establishing an industrial register before a single pixel of product imagery loads. The signature red (#ce2129) appears sparingly — reserved for primary CTAs, sale callouts, and the occasional energy-rating badge — which gives each instance real voltage against the overwhelmingly neutral gray-and-white canvas. Typography inherits the browser's system stack with no custom web font; headings run medium-weight at restrained sizes (20–28px), trusting product photography and generous whitespace to carry visual hierarchy rather than typographic spectacle. Product cards sit on `{colors.surface-card}` with `{rounded.sm}` corners and a single `{colors.hairline}` border, stacking vertically on mobile with no box-shadow — a deliberate austerity that mirrors the stainless-steel appliances themselves. The palette is dominated by cool neutrals: `{colors.ink}` (#141619) for headlines, `{colors.body}` (#41464b) for running copy, `{colors.muted}` (#636464) for spec labels and metadata. A secondary dark blue (#084298) surfaces in informational badges and comparison-table headers, while the light surface tone `{colors.surface-soft}` (#f9fafb) provides alternating section contrast without warmth. Buttons are squared-off (`{rounded.xs}`) with firm 48px heights, echoing the rectilinear geometry of the washers and dryers themselves — nothing pill-shaped, nothing playful. The overall system communicates German-engineered precision for compact living: every element is flush, aligned, and dimensionally tight, much like a 24-inch appliance slotted into a European kitchen cabinet.

colors:
  primary: "#ce2129"
  primary-active: "#b02a37"
  primary-disabled: "#f8d7da"
  accent-blue: "#084298"
  accent-blue-light: "#cfe2ff"
  success: "#198754"
  success-light: "#d1e7dd"
  info: "#055160"
  info-light: "#cff4fc"
  warning-dark: "#664d03"
  warning-light: "#fff3cd"
  ink: "#141619"
  body: "#41464b"
  muted: "#636464"
  muted-soft: "#565e64"
  hairline: "#e2e3e5"
  hairline-soft: "#cbccce"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  surface-dark: "#1a1e21"
  nav-bg: "#1a1e21"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  meta-theme: "#3a3a3a"
  error: "#842029"
  error-light: "#f8d7da"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
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
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 48px
    border: 1px solid {colors.hairline-soft}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.ink}
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline-soft}
    focusBorder: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.lg}
  nav-bar-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    boxShadow: 0 4px 12px rgba(0,0,0,0.12)
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 480px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline}
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    boxShadow: 0 2px 8px rgba(0,0,0,0.08)
    border: 1px solid {colors.hairline-soft}
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline}
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    padding: "{spacing.md} {spacing.base}"
  comparison-header:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.xs} {rounded.xs} {rounded.none} {rounded.none}"
  info-badge:
    backgroundColor: "{colors.info-light}"
    textColor: "{colors.info}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  success-badge:
    backgroundColor: "{colors.success-light}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px 12px 40px
    height: 48px
    border: 1px solid {colors.hairline-soft}
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    opacity: 0.8
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    minHeight: 200px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline-soft}"
---

## Components

### Buttons

**`button-primary`** — Solid Blomberg red (#ce2129) with white text, squared off at `{rounded.xs}` (4px). On hover the background darkens to `{colors.primary-active}` (#b02a37); disabled state fades to the light pink `{colors.primary-disabled}` with muted text. Height is a firm 48px with 12px vertical / 24px horizontal padding.

**`button-secondary`** — White background with a 1px `{colors.hairline-soft}` border and `{colors.ink}` text. On hover the border deepens to ink-black and the fill shifts to `{colors.surface-soft}`. Maintains the same 48px height and squared corners as the primary variant.

**`button-dark`** — Used in hero sections and dark-background contexts. Background `{colors.surface-dark}` (#1a1e21) with white text and the same 4px radius. Provides an alternative CTA weight without using brand red.

### Navigation

**`nav-bar`** — Fixed 64px tall bar with `{colors.nav-bg}` (#1a1e21) background. Logo sits left, nav links centered or right-aligned in `{typography.nav-link}` (14px, weight 500, white). Dropdown menus emerge on `{colors.canvas}` with subtle 4px radius and 12px box-shadow, creating separation from the dark header.

**`nav-bar-dropdown`** — White panel with `{rounded.xs}` corners housing product category links in `{typography.body-sm}`. Each link highlights with `{colors.surface-soft}` on hover. Shadows at 0 4px 12px rgba(0,0,0,0.12) provide adequate depth against the dark nav.

### Hero

**`hero-banner`** — Full-width section with a minimum height of 480px, typically featuring a large product photograph. Text overlays use `{typography.display-xl}` at 32px/700 weight. Background alternates between `{colors.surface-soft}` for lifestyle imagery and solid product-on-white for studio shots. CTAs within heroes use `button-primary` or `button-dark` depending on image lightness.

### Product Cards

**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.sm}` (8px) corners. Contains a product image (aspect-ratio constrained to 4:3), model name in `{typography.title-sm}`, and a brief feature list in `{typography.body-sm}`. On hover, the border softens and a subtle box-shadow (0 2px 8px) appears. No background color change.

**`product-badge`** — Small label overlaid top-left of product images for sale/new indicators. Uses `{typography.caption-bold}` (12px, uppercase, 700 weight) on `{colors.primary}` red background with 4px radius and tight 4px/8px padding.

### Specification Tables

**`spec-table-row`** — Alternating-row table for product specifications. Even rows sit on `{colors.canvas}`, odd rows on `{colors.surface-soft}`. Left column holds the spec name in `{typography.spec-label}` (13px, weight 500), right column holds the value in regular weight. Rows are separated by a 1px `{colors.hairline}` bottom border.

**`comparison-header`** — Dark blue (`{colors.accent-blue}` #084298) header row for comparison tables, with white text in `{typography.title-sm}`. Top corners are `{rounded.xs}`, bottom corners are flat to merge seamlessly with the table body below.

### Badges

**`info-badge`** — Light cyan background (`{colors.info-light}`) with dark teal text (`{colors.info}`). Used for energy ratings and capacity indicators.

**`success-badge`** — Light green background (`{colors.success-light}`) with green text (`{colors.success}`). Used for in-stock availability and feature confirmations.

### Search

**`search-bar`** — Standard 48px input field with left-padded search icon (40px left padding to accommodate the 16px icon). Border is 1px `{colors.hairline-soft}`, sharpening to `{colors.ink}` on focus. Placeholder text in `{colors.muted}`.

### Footer

**`footer`** — Dark panel matching the nav (`{colors.surface-dark}`) with white text. Organized in a multi-column grid: product categories, support links, company info. Links render at 80% opacity, rising to 100% on hover. Section padding is `{spacing.section}` (64px) top and bottom.

### Category Tiles

**`category-tile`** — Rectangular cards used on the homepage to link into product categories (Washers, Dryers, Dishwashers, Refrigerators). Light gray `{colors.surface-soft}` background, `{rounded.sm}` corners, with a centered product silhouette and category name in `{typography.title-md}`. Minimum height 200px ensures visual weight in grid layouts.

### Breadcrumbs

**`breadcrumb`** — Compact wayfinding element in `{typography.caption}` (12px) and `{colors.muted}` text. Separator chevrons use `{colors.hairline-soft}`. The final active crumb renders in `{colors.ink}` without a link.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero min-height drops to 320px; spec tables scroll horizontally; footer stacks into single column |
| Tablet | 744–1128px | Two-column product grid; nav remains collapsed or shows top-level links; hero maintains full height; comparison tables show 2 products side-by-side |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with dropdowns; hero at 480px+; comparison tables support 3–4 products |
| Wide | > 1440px | Content max-width caps at 1320px and centers; four-column product grid; hero imagery scales proportionally with padding increase |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch area on mobile
- Nav hamburger icon has 48px tap target with 8px padding around the 24px icon
- Product cards are fully tappable — the entire card surface is an anchor
- Filter chips in product listings use 40px height with 12px horizontal padding
- Footer links are spaced at `{spacing.md}` (12px) vertical intervals for thumb reach

### Collapsing Strategy

- Navigation collapses at 1128px into a slide-out drawer from the left, overlaying a scrim
- Product specification sections collapse into accordions on mobile, with `{spacing.md}` padding and `{colors.hairline}` dividers between groups
- Comparison mode is disabled below 744px; a "Compare" button is hidden and replaced with individual product detail links
- Category tiles shift from a 3-across grid to a vertical scrolling strip (horizontal overflow) on mobile
- Hero CTAs stack vertically below 744px with full-width buttons

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font family detected — the site uses `inherit` and relies on Bootstrap's system font stack. Blomberg may load a branded typeface via JavaScript or a deferred stylesheet not captured during extraction.
- Color palette is dominated by Bootstrap 5 defaults (#0d6efd, #198754, #0dcaf0, etc.) which are framework utility colors, not brand decisions. Only #ce2129 (red) and the dark grays (#1a1e21, #141619, #3a3a3a) appear brand-specific.
- No icon system detected beyond Bootstrap Icons. The site may use additional product-feature SVG icons loaded dynamically.
- Exact border-radius values could not be confirmed — the `{rounded.xs}` (4px) assignment is inferred from Bootstrap defaults and visual inspection of card/button geometry.
- Animation/transition timings not captured. Product card hover transitions and nav dropdown animations likely exist but could not be measured from static extraction.
- No dark-mode variant detected; the site appears to be light-only.
