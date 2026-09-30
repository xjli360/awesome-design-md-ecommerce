---
version: alpha
name: "Hay"
source_url: "https://www.hay.com"
captured_at: "2026-09-28T04:10:42.006747+00:00"
evidence_status: "historical_partial_css_evidence"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Hay is a Danish design brand that speaks in a quiet, confident visual language — one built on soft contrasts, muted earth tones, and a deep respect for material honesty. The brand’s palette is anchored by a warm, dusty grey (`#d3d3d3`) that appears across surfaces, textiles, and product finishes, paired with a deep ink-like teal (`#223333`) that acts as the primary brand voltage — appearing on key CTAs, navigation accents, and editorial headers. A pale, airy blue-grey (`#d1dee7`) rounds out the trio, used sparingly as a secondary accent or background wash that evokes Scandinavian light. Typography is split between a clean, utilitarian sans-serif (Arial, used for body copy, captions, and interface labels) and a refined serif (ITC New Baskerville W01) reserved for editorial display and product storytelling — a deliberate tension between the rational and the romantic. Corners are soft but not pill-like: cards and buttons use `{rounded.sm}` (8px) and `{rounded.md}` (12px), while larger containers like hero sections and modals round at `{rounded.lg}` (20px). The overall feel is one of curated restraint — nothing shouts, but every detail has been considered. Hay’s design system mirrors its product philosophy: modular, tactile, and quietly expressive.

colors:
  primary: "#223333"
  primary-active: "#1a2929"
  primary-disabled: "#a3b3b3"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6b6b6b"
  muted-soft: "#999999"
  hairline: "#d3d3d3"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#d3d3d3"
  accent-cool: "#d1dee7"
  badge-new: "#223333"
  star-rating: "#223333"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'ITC New Baskerville W01', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ITC New Baskerville W01', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ITC New Baskerville W01', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'ITC New Baskerville W01', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 10px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    height: 36px
    border: "1px solid {colors.hairline}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-circle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 0
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid #c13515"
  select:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-cool:
    backgroundColor: "{colors.accent-cool}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the deep teal `{colors.primary}` (#223333) as background with white text. On hover, it shifts to `{colors.primary-active}` (#1a2929) for a subtle darkening effect. The disabled state uses `{colors.primary-disabled}` (#a3b3b3) to signal inactivity. All primary buttons use `{rounded.sm}` (8px) for a soft but not overly rounded corner, and uppercase `{typography.button-md}` for a clean, architectural feel.
**`button-secondary`** — An outlined variant with a white background, `{colors.primary}` text, and a 1px solid border in `{colors.primary}`. The active state inverts the background to `{colors.surface-soft}` (#f5f5f5) with the darker `{colors.primary-active}` border. Used for less prominent actions like "Save" or "Learn More".
**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` text. On hover, it shifts to `{colors.primary-active}`. Used for inline actions like "View all" or "Cancel".
**`button-pill`** — A fully rounded (`{rounded.full}`) compact button using `{colors.primary}` background and `{typography.button-sm}`. Used for filter tags, quick actions, or promotional badges. The outline variant (`button-pill-outline`) uses a white background with a `{colors.hairline}` border for a lighter touch.

### Cards
**`product-card`** — The core product display unit, with a white background (`{colors.canvas}`), `{rounded.sm}` corners, and a 1:1 aspect ratio image area. The title uses `{typography.title-sm}` in `{colors.ink}`, while the price sits below in `{typography.body-sm}` with `{colors.muted}` for a secondary hierarchy. A `product-card-badge` can be overlaid on the image, using `{colors.badge-new}` (#223333) background and `{typography.badge}` for "New" or "Sale" labels.
**`hero`** — A full-width section with `{colors.surface-soft}` (#f5f5f5) background, using `{typography.display-xl}` for the headline and `{spacing.section}` (80px) for vertical padding. The `hero-cta` button mirrors `button-primary` but with larger horizontal padding (32px) for visual weight.

### Navigation
**`top-nav`** — A fixed-height (64px) white bar with a subtle `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` (uppercase, 14px, weight 500) with `{colors.ink}` text. The active state (`nav-link-active`) adds a 2px `{colors.primary}` bottom border and shifts text to `{colors.primary}`.
**`search-bar`** — A compact search input with `{colors.surface-soft}` background, `{rounded.sm}` corners, and a `{colors.hairline}` border. On focus, the background shifts to white and the border becomes `{colors.primary}`.

### Forms
**`text-input`** — Standard text input with white background, `{rounded.sm}` corners, and a `{colors.hairline}` border. Focus state uses `{colors.primary}` border. Error state uses a red border (#c13515) for validation feedback.
**`select`** — Dropdown selector matching the `text-input` styling for visual consistency across form elements.

### Footer
**`footer`** — A full-width footer using `{colors.primary}` (#223333) as background, with white text (`{colors.on-primary}`). Links use `{typography.link}` and maintain the white color. Vertical padding uses `{spacing.xxl}` (48px) for generous breathing room.

### Badges & Chips
**`badge`** — A small label using `{colors.accent-warm}` (#d3d3d3) background with `{colors.ink}` text, `{rounded.xs}` (4px), and `{typography.badge}`. The `badge-cool` variant uses `{colors.accent-cool}` (#d1dee7) for a different tonal accent.
**`filter-chip`** — A pill-shaped (`{rounded.full}`) filter option with white background, `{colors.hairline}` border, and `{typography.body-sm}`. Active state fills with `{colors.primary}` and white text.

### Accordion
**`accordion`** — A collapsible section with a white background, `{colors.hairline-soft}` bottom border, and `{spacing.base}` vertical padding. The header uses `{typography.title-sm}` and the content area uses `{typography.body-sm}` with `{colors.body}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for product cards (1 column), hero padding reduced to 40px vertical, top-nav height reduces to 56px, search bar collapses to icon-only, footer stacks vertically, filter chips wrap to multiple rows |
| Tablet | 744–1128px | Two-column product grid, hero uses `{typography.display-lg}` (36px), top-nav maintains 64px height but reduces link spacing, search bar remains full-width but with reduced padding |
| Desktop | 1128–1440px | Three-column product grid, hero uses `{typography.display-xl}` (48px), full top-nav with all links visible, search bar in center of nav, footer columns in 4-column layout |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero expands to full viewport height with larger imagery, additional whitespace in margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44x44px tap target on mobile
- Filter chips and badges are at least 32px tall with 16px horizontal padding
- Icon buttons are 40x40px minimum
- Product card tap targets extend to full card area

### Collapsing Strategy
- Top navigation collapses secondary links into a hamburger menu on mobile (< 744px)
- Product grid reduces from 4 columns to 1 column on mobile
- Footer columns stack vertically on mobile
- Search bar collapses to an icon that expands on tap
- Filter chips wrap to multiple rows instead of a single horizontal scroll
- Accordion sections are collapsed by default on mobile, with only the first section expanded

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Hover states for all components (only primary and secondary buttons have defined hover colors)
- Error styling for forms beyond the red border (error messages, iconography, focus ring styles)
- Dark mode palette and component adjustments
- Sub-brand or collection-specific color variations (e.g., Hay x Sonos, Hay x IKEA)
- Animation and transition timing values (ease curves, durations)
- Focus ring styles and accessibility states (keyboard navigation outlines)
- Loading states (skeleton screens, spinners)
- Dropdown menu styles (country selector, account menu)
- Modal and overlay component specifications
- Tooltip and popover styling
- Table and data display components
- Icon library and sizing guidelines
- Photography and imagery treatment (aspect ratios, filters, overlays)
- Print stylesheet specifications
- Typography scale for mobile (all sizes currently use desktop values)
- Specific color values for the "New" badge background (approximated with primary)
