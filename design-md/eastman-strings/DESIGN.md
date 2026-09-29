---
version: alpha
name: "Eastman Strings"
source_url: "https://www.eastmanstrings.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, warm brown at #251f17 anchors the Eastman Strings identity — not a black, not a charcoal, but a near-ebony earth tone that reads as the color of aged rosin, varnished fingerboards, and the shadow inside a violin case. Against this sits a muted sage-gray #7f9299 (the meta theme-color, pulled from the live site) that appears in secondary text, decorative borders, and the brand’s quiet secondary palette — a color that evokes the patina of old brass tuning pegs and the soft light of a practice room. The canvas is a warm off-white #fbfaf8, not a cold digital white, and it’s paired with a pale stone #d4d0ca for card surfaces and muted backgrounds. A single accent of amber #a26300 — the color of aged shellac and maple neck wood — appears sparingly in hover states and decorative underlines. The typography stack is unexpectedly technical: monospace fonts (Consolas, Courier, Roboto Mono) dominate the extracted declarations, suggesting a brand that treats instrument specifications, serial numbers, and build details as primary content. Headlines likely sit in a serif or a heavier sans, but the body and data layer lean into the precision of monospaced type — a design choice that reads as workshop documentation rather than lifestyle copy. Corners are soft but not pill-like: `{rounded.md}` on cards, `{rounded.sm}` on buttons, with the only `{rounded.full}` reserved for badge indicators and instrument-family icons. The overall mood is that of a luthier’s notebook — warm, precise, material-focused, with a color palette drawn from wood, metal, and shellac rather than from digital convention.

colors:
  primary: "#251f17"
  primary-active: "#1a150f"
  primary-disabled: "#8a857e"
  ink: "#251f17"
  body: "#505054"
  muted: "#7f9299"
  muted-soft: "#99948b"
  hairline: "#d4d0ca"
  hairline-soft: "#e5e2dd"
  canvas: "#fbfaf8"
  surface-soft: "#f5f3f0"
  surface-card: "#ffffff"
  on-primary: "#fbfaf8"
  accent-amber: "#a26300"
  accent-amber-hover: "#c87a00"
  accent-gold: "#d3b17b"
  badge-warning: "#ffff00"
  badge-new: "#7f9299"
  star-rating: "#a26300"
  scrim: "#26130c"

typography:
  display-xl:
    fontFamily: "'Source Sans Pro', 'Roboto Mono', 'Consolas', monospace, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Source Sans Pro', 'Roboto Mono', 'Consolas', monospace, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Source Sans Pro', 'Roboto Mono', 'Consolas', monospace, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto Mono', 'Consolas', 'Courier', monospace"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Roboto Mono', 'Consolas', 'Courier', monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  body-md:
    fontFamily: "'Source Sans Pro', 'Roboto Mono', 'Consolas', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', 'Roboto Mono', 'Consolas', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto Mono', 'Consolas', 'Courier', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Roboto Mono', 'Consolas', 'Courier', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Roboto Mono', 'Consolas', 'Courier', monospace"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Source Sans Pro', 'Roboto Mono', 'Consolas', monospace, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Source Sans Pro', 'Roboto Mono', 'Consolas', monospace, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Source Sans Pro', 'Roboto Mono', 'Consolas', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Source Sans Pro', 'Roboto Mono', 'Consolas', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.muted}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-amber-hover:
    backgroundColor: "{colors.accent-amber-hover}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    border: "1px solid {colors.accent-amber}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(37, 31, 23, 0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    height: 240px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-subtitle:
    backgroundColor: transparent
    textColor: "{colors.accent-gold}"
    typography: "{typography.title-md}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 20px"
    height: 52px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 20px"
    height: 52px
    border: "1px solid {colors.primary}"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    height: 32px
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    height: 32px
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.accent-gold}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  badge-warning:
    backgroundColor: "{colors.badge-warning}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table-row:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-circle-hover:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the deep brown `{colors.primary}` and set in `{typography.button-md}`. On hover, darkens to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}`, a muted taupe. All primary buttons use `{rounded.sm}` (4px) — a crisp, workshop-grade corner that avoids the friendliness of pills.

**`button-secondary`** — Outlined variant on `{colors.canvas}` with a `{colors.hairline}` border. Active state shifts the border to `{colors.muted}` and background to `{colors.surface-soft}`. Used for "Compare Models" and "Add to Wishlist" actions.

**`button-amber`** — The accent button, filled with `{colors.accent-amber}` (#a26300). Used sparingly for high-signal actions like "Book a Trial" or "Request a Quote." Hover shifts to `{colors.accent-amber-hover}` (#c87a00).

**`button-tertiary`** — Text-only button, transparent background, `{colors.ink}` text. Used for "Learn More" links and dismiss actions. No border, no background — pure typographic action.

### Cards
**`product-card`** — White surface (`{colors.surface-card}`) with `{rounded.md}` (8px) and a soft `{colors.hairline-soft}` border. The image area occupies the top 240px with `{rounded.md}` applied to the top corners only. Title uses `{typography.title-sm}` (uppercase monospace), price uses `{typography.body-md}`. On hover, the card gains a subtle box-shadow and a `{colors.hairline}` border — the only elevation in the system.

**`product-card-badge`** — A pill-shaped (`{rounded.full}`) indicator in `{colors.badge-new}` (#7f9299) with `{typography.badge}` (10px uppercase monospace). Used for "New Arrival," "Limited Edition," and "Hand-Selected" labels.

### Navigation
**`nav-bar`** — Fixed top bar at 64px on `{colors.canvas}` with a `{colors.hairline-soft}` bottom border. On scroll, shrinks to 56px and the border strengthens to `{colors.hairline}`. Links use `{typography.nav-link}` (14px uppercase, 600 weight, 0.5px letter-spacing). Active link has a 2px `{colors.primary}` bottom border.

**`nav-link-inactive`** — Muted to `{colors.muted}` (#7f9299), the sage-gray that signals secondary navigation. No underline or border.

### Forms
**`text-input`** — Standard input on `{colors.canvas}` with `{typography.body-md}` and a `{colors.hairline}` border. Focus state swaps the border to `{colors.primary}`. Error state uses `{colors.accent-amber}` border — the amber signals attention without the alarm of red.

**`select-input`** — Same dimensions and typography as text inputs, with a custom dropdown arrow in `{colors.muted}`.

### Search
**`search-bar`** — A 52px-high input with `{rounded.md}` (8px), `{colors.canvas}` background, and `{colors.hairline}` border. Focus shifts border to `{colors.primary}`. Used for product search and catalog filtering.

**`filter-tag`** — Pill-shaped (`{rounded.full}`) filter chips at 32px height. Default state is `{colors.surface-soft}` background with `{colors.body}` text. Active state fills with `{colors.primary}` and white text. Used for instrument family (Violin, Viola, Cello, Bass) and category filters.

### Footer
**`footer-section`** — Full-width dark footer on `{colors.primary}` with `{colors.on-primary}` body text. Links render in `{colors.accent-gold}` (#d3b17b) — the warm brass tone — and shift to white on hover. The footer uses generous `{spacing.xxl}` vertical padding.

### Badges
**`badge-warning`** — Yellow badge (`{colors.badge-warning}` #ffff00) with `{colors.ink}` text. Used for "Backordered" or "Low Stock" indicators. Sharp `{rounded.sm}` corners — urgency should not feel friendly.

**`badge-new`** — Sage-gray pill badge (`{colors.badge-new}`) with white text. Used for new arrivals and curated selections.

### Specification Tables
**`spec-table`** — A bordered table on `{colors.surface-card}` with `{rounded.sm}`. Headers use `{typography.title-sm}` (uppercase monospace) on `{colors.surface-soft}`. Rows alternate with `{colors.hairline-soft}` bottom borders. Used for instrument dimensions, materials, and build details — the monospace typography reinforces the technical, workshop-document feel.

### Iconography
**`icon-circle`** — 40px circular containers on `{colors.surface-soft}` with `{colors.primary}` icons. Used for instrument-family icons (violin, viola, cello, bass) and utility icons (search, cart, account). Hover shifts background to `{colors.hairline}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row). Nav collapses to hamburger. Hero section reduces to 320px min-height. Filter tags stack horizontally with scroll. Search bar moves below hero. Footer stacks links vertically. |
| Tablet | 744–1128px | Two-column product grid (2 cards per row). Nav shows top-level links (Instrument Families, Shop, About). Hero shows 400px min-height. Filter tags display in a single row with overflow scroll. |
| Desktop | 1128–1440px | Three-column product grid (3 cards per row). Full nav with all links visible. Hero at 500px min-height. Filter tags display in a wrap row. Search bar in nav. |
| Wide | > 1440px | Four-column product grid (4 cards per row). Max-width container at 1440px. Hero at 600px min-height with parallax image. Additional whitespace around product cards. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Filter tags are 32px height — below the 44px recommendation but acceptable for desktop; on mobile, they expand to 40px with increased padding.
- Icon circles (`icon-circle`) are 40px — meets the 44px recommendation for touch when used standalone; when inside a nav context, the parent container provides the additional touch area.
- Product card CTAs ("View Details," "Add to Cart") are 48px height on all breakpoints.

### Collapsing Strategy
- **Mobile (< 744px):** Full nav collapses to a hamburger icon. Product filters collapse into a "Filter" button that opens a bottom sheet. Specification tables collapse into accordion rows. Footer link columns collapse into a single vertical stack with expandable sections.
- **Tablet (744–1128px):** Secondary nav links (Support, Blog, Events) collapse into a "More" dropdown. Product image galleries collapse from thumbnails to a single swipeable carousel. Footer link columns reduce from 4 to 2 columns.
- **Desktop (1128–1440px):** No structural collapse. Filter tags that exceed the viewport width scroll horizontally with fade indicators on each side.
- **Wide (> 1440px):** No collapse. Content is centered within a 1440px max-width container. Additional whitespace appears on the sides.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states:** Only `button-primary-active` and `button-amber-hover` are confirmed from extracted data. Hover states for `button-secondary`, `nav-link`, `footer-link`, and `icon-circle` are inferred from common DTC patterns — not verified from the live site.
- **Error states:** `text-input-error` uses `{colors.accent-amber}` as the border color, but the actual error message styling (color, typography, icon placement) could not be extracted.
- **Focus states:** Focus ring styling (color, offset, width) for keyboard navigation was not found in extracted CSS. Assumed to use `{colors.primary}` with a 2px offset, but unconfirmed.
- **Dark mode:** No dark mode tokens were found. The brand may not support dark mode, or it may be gated behind a user preference not present in the extracted data.
- **Sub-brand palettes:** Eastman may have sub-brands or collections (e.g., "Eastman Classics," "Eastman Modern") with distinct accent colors. None were found in the extraction.
- **Typography hierarchy:** The extracted font-family declarations include only monospace and sans-serif options. The actual headline font (likely a serif for display) could not be determined. `display-xl` through `display-md` use `Source Sans Pro` as a fallback — the actual display font may differ.
- **Spacing scale:** The spacing tokens are inferred from common DTC patterns. The actual spacing values (especially `section` and `xxl`) may differ on the live site.
- **Component heights:** Button and input heights (44px, 48px, 52px) are estimated based on common orchestral-instrument e-commerce patterns. The live site may use different values.
- **Product card image aspect ratio:** The 240px height for `product-card-image` is an estimate. The actual aspect ratio (likely 4:3 or 3:2 for instrument photography) could not be determined.
- **Animation and transition:** No transition durations or easing functions were extracted. The brand likely uses subtle transitions (200–300ms, ease-in-out) for hover and focus states, but this is unconfirmed.
- **Icon set:** The extracted data does not include SVG or icon font references. Instrument-family icons (violin, viola, cello, bass) are assumed but not confirmed.
