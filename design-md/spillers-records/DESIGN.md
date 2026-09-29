---
version: alpha
name: "Spillers Records"
source_url: "https://spillersrecords.co.uk"
captured_at: "2026-09-29T04:18:12.779701+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Spillers Records is presented through a standard WordPress "Twenty Twelve" theme installation, extended with Gutenberg block-editor defaults and a handful of third-party plugin styles (YouTube embed, Facebook dialog). No custom brand stylesheet or bespoke typeface was found in the supplied evidence; the visual identity observed is therefore largely the WordPress default toolkit rather than a purpose-built Spillers brand system.
  The one deliberately-set brand signal is a custom body background color, a warm mustard/gold (#edb621), applied via `body.custom-background`. Buttons across the block editor consistently render as a dark slate (#32373c) with white text, which is treated here as the primary interactive color. Supporting grays (#444444 body text, #757575 muted, #f4f4f4/#ebebeb surfaces, #d2d2d2/#cccccc hairlines) come from the theme's block CSS for buttons, file downloads, and hover/focus states. A red (#e62117) appears only on a YouTube-subscribe plugin button and is treated as an inferred "badge/urgent" accent, not a core brand color.
  Typography is Open Sans with system sans-serif fallbacks (Arial, Helvetica Neue, Helvetica), per WordPress Twenty Twelve conventions — no proprietary or licensed display face is evidenced. This interpretation proposes a plain, list-driven, catalog-style layout suited to the site's actual content: dense weekly new-release listings, PDF links, and shop-info blocks.

colors:
  primary: "#32373c"
  accent: "#edb621"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#757575"
  hairline: "#d2d2d2"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge: "#e62117"
  border-soft: "#cccccc"
typography:
  display-xl: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  display-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 24px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  title-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.35, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.43, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.43, letterSpacing: 0px}
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
  xxl: 48px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.border-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  release-list-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"

## Components

**button-primary** reflects the observed `.wp-block-button__link` rule: dark slate background (#32373c), white text, fully-rounded pill shape, generous padding. This is the only consistently-styled call-to-action pattern in the evidence (e.g. "PDF List" links, store-day announcements).

**button-secondary** is proposed from the muted gray button-hover states (`#e6e6e6`/`#ebebeb` backgrounds, `#5e5e5e`/`#7c7c7c` text) seen on `.wp-block-file__button`. Used for secondary actions like "Download PDF" or "View Archive."

**text-input** is an inferred pattern for search/contact forms; no input styling was present in the evidence, so border and padding values are proposed defaults matching the theme's general spacing rhythm.

**nav-bar** represents the top navigation implied by the page-text menu items (Home, Contact, Dinked Forthcoming Releases, New Release Archive, Special Events). No nav CSS was supplied, so background/border are inferred from the theme's neutral palette.

**product-card** is proposed for individual release entries (artist, title, format, price) seen repeated throughout the new-release lists. Card chrome uses the theme's light hairline and soft radius; not an observed component, since the source is text/blog content rather than a templated shop grid.

**hero** uses the one clearly brand-intentional color, the custom gold background (#edb621), for a banner treatment — e.g. Record Store Day announcements. This is inferred from the `body.custom-background` rule rather than a dedicated hero block in evidence.

**footer** reuses the dark slate button color as a footer band, carrying contact info (email, phone, opening times) that appears at the top of the extracted content; footer placement/styling itself is not observed and is proposed for information architecture consistency.

**badge** repurposes the red (#e62117) from the YouTube-subscribe plugin button as a small tag component, useful for "New," "Dinked Exclusive," or "Limited" labels seen throughout the release copy (e.g. "Ltd. Coke Bottle Splatter LP").

**search** is a proposed pill-shaped input for the record catalog, styled consistently with button-primary's full radius; no search UI was present in the supplied CSS/text.

**release-list-row** is a category-specific component modeling the dense, repeated artist/title/format/price lines that dominate the actual page content (e.g. "AC/DC Let There Be Rock Gold LP £30.99"). It is the most content-representative pattern in the evidence, structured as a simple bordered row rather than a card grid, to match the list-heavy presentation observed in the text excerpt.

## Responsive Behavior

Proposed breakpoints (not measured from live site):

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | Single-column release list, nav collapses to a toggled menu |
| tablet | 600–960px | Two-column product-card grid where applicable; nav remains simplified |
| desktop | >960px | Multi-column layout; full nav-bar visible |

Touch targets for button-primary and search should maintain a minimum ~44px tap height, consistent with the padding scale defined above. Navigation collapse behavior (hamburger vs. inline) is a recommendation only — no responsive or interaction CSS was present in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built entirely from static CSS/text extraction of a WordPress Twenty Twelve theme site plus plugin fragments; no rendered layout, computed styles, or interaction states (hover, focus, active beyond the documented button rules) were observed. The distinction between genuinely brand-intentional colors (the gold custom background, the dark slate buttons) and default WordPress/Gutenberg editor palette swatches (e.g. the standard block-editor color list including `#cf2e2e`, `#fcb900`, `#9b51e0`, etc.) is inferred, not confirmed — many supplied hex values are WordPress defaults rather than deliberate brand choices, and were excluded from the token set accordingly. Typography is limited to the theme's Open Sans/system-sans stack; no proprietary or licensed font was evidenced, and font availability/licensing has not been verified. All component definitions beyond button-primary and the file-download button are proposed patterns inferred from page content (release lists, contact info, PDF links) rather than directly observed markup or styling. Breakpoints, spacing scale, and rounded-corner tokens beyond the two directly observed values (9999px pill buttons, ~3px file-button corners) are proposed conventions, not measurements from the live site.
