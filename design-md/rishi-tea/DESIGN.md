---
version: alpha
name: "Rishi Tea"
source_url: "https://rishi-tea.com"
captured_at: "2026-09-28T10:04:07.505401+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation draws from CSS evidence for Rishi Tea & Botanicals, an
  online purveyor of direct-trade, organic loose leaf tea, sachets, matcha and
  teaware. The observed palette centers on a deep slate-navy (#233747, used
  explicitly as the reviews-widget button color with white text) alongside a
  closely related, more saturated ink (#283645) that recurs across many alpha
  variants, suggesting its use as a primary text/overlay color. Warm,
  botanical neutrals (#f7f5f0, #fbf9f7, #f8f7f3) supply soft canvas and card
  surfaces consistent with an organic, apothecary-leaning aesthetic, while
  muted blue-grays (#5e6874, #676986) are explicitly assigned to body and
  secondary text roles in the review-widget custom properties. Rust and tan
  tones (#af4f18, #a88667) appear in the palette and are inferred here as
  botanical accent colors for tags or highlights, though their exact usage
  context was not observed. Typography combines a light-weight serif,
  ivypresto-headline (weight 100), for display and section headings — with
  exact sizes (32px, 24px) and letter-spacing confirmed in CSS — and a
  grotesque sans, neue-haas-grotesk-text, for body copy, inputs, and
  uppercase buttons. Poppins is present in the font stack but its applied
  role could not be confirmed from the supplied rules. All layout structure
  below is proposed and inferred from typical e-commerce conventions, not
  measured from a live render.

colors:
  primary: "#233747"
  ink: "#283645"
  canvas: "#ffffff"
  body: "#5e6874"
  muted: "#676986"
  hairline: "#d4d7da"
  surface-soft: "#f7f5f0"
  surface-card: "#fbf9f7"
  on-primary: "#ffffff"
  accent-spice: "#af4f18"
  accent-tan: "#a88667"
typography:
  display-xl: {fontFamily: "ivypresto-headline, ui-serif, serif", fontSize: 48px, fontWeight: 100, lineHeight: 1.1, letterSpacing: 0.01em}
  display-md: {fontFamily: "ivypresto-headline, ui-serif, serif", fontSize: 32px, fontWeight: 100, lineHeight: 1, letterSpacing: 0.01em}
  title-md: {fontFamily: "ivypresto-headline, ui-serif, serif", fontSize: 24px, fontWeight: 100, lineHeight: 1.1, letterSpacing: 0.04em}
  body-md: {fontFamily: "neue-haas-grotesk-text, ui-sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: normal}
  body-sm: {fontFamily: "neue-haas-grotesk-text, ui-sans, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.4, letterSpacing: normal}
  caption: {fontFamily: "neue-haas-grotesk-text, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.02em}
  button-md: {fontFamily: "neue-haas-grotesk-text, ui-sans, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.96px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    mutedTextColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  taste-profile-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-spice}"
    borderColor: "{colors.accent-tan}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge:
    backgroundColor: "{colors.accent-spice}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    mutedTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

**button-primary** uses the explicitly observed `#233747` background with white text, matching the `.oke-button` CSS custom properties from the review widget; this is treated as the site's core interactive color for CTAs like "Add to Cart" and "Quick Add." Hover/active states are proposed to darken slightly, as the observed oke-button hover rule reuses the same background color rather than a distinct shade.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "View Details"), inverting the primary color to an outline treatment; no such outline button was directly observed in the CSS.

**text-input** and **search** are grounded in the observed `.header__search` rules: a `#f7f5f0` background, `#4b4f56`-adjacent border/text (approximated to `{colors.body}` for token consistency), 16px font-size on the input and 15px on the placeholder. Focus states are proposed, not observed.

**nav-bar** is inferred from the presence of extensive mega-menu taxonomy in the page text (Shop, Form, Tea Type, Garden Direct, Origin, Teaware, Taste Profile, Mood) but no header layout CSS was supplied; background, spacing, and hairline are proposed conventions.

**hero** is proposed as a full-width introductory band using the warm off-white surface and the large serif display type, reflecting the "Purveyor of Direct Trade, Organic Teas" messaging found in the page text; exact hero CSS was not supplied.

**product-card** is inferred to house tea product imagery, price tiers (e.g., "1 Pound / 1/4 Pound"), and taste descriptors seen in the excerpt (e.g., "Rich | Citrusy | Floral"); card background and radius are proposed, not measured.

**taste-profile-tag** is a category-specific component proposed to render the pipe-separated taste descriptors ("Malty | Jammy | Mellow") seen throughout the product listing text, using the inferred accent colors to distinguish flavor metadata from primary UI.

**badge** is proposed for merchandising flags such as "New Arrivals," "Fall Teas," or "Caffeine Free," using the rust accent color as an inferred highlight; no badge CSS was directly observed.

**footer** is proposed as a dark-ink band echoing the brand's navy tones, intended to house the extensive discovery/education links (Tea Education, Recipes & Inspiration, Origins & Travel) referenced in the page text; no footer-specific CSS was supplied.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <480px | Single-column product grid, collapsed hamburger nav, sticky search icon |
| Tablet | 480–1024px | 2-column product grid, mega-menu collapses to accordion |
| Desktop | >1024px | 3–4 column product grid, full mega-menu with taxonomy columns visible |

Touch targets are recommended at a minimum 44×44px for buttons and quick-add controls. Mega-menu categories (Form, Tea Type, Garden Direct, Origin, Teaware, Taste Profile, Mood) should collapse into a scrollable accordion below tablet width. This table is a recommendation based on common e-commerce patterns and was not measured from the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction provides only fragments of selectors (many are truncated mid-rule), so several declarations, especially for layout containers, grids, and the primary header/nav, were not available.
- The distinction between `#233747` and `#283645` as separate brand roles is inferred from repetition patterns (alpha-variant usage of `#283645`) rather than confirmed semantic labeling in source CSS.
- Accent colors (`accent-spice`, `accent-tan`) are drawn from the observed palette but their actual UI application (tags, badges, links) was not confirmed by any supplied selector.
- Font weights and letter-spacing for `display-xl` and `body-md` are proposed extrapolations from the smaller confirmed instances (24px/32px headings, 15–16px inputs); no explicit large hero or paragraph rule was supplied.
- No interaction states (hover, focus, active) beyond the review-widget button were observed; all such states elsewhere are proposed.
- No mobile/responsive CSS (media queries) was included in the supplied evidence; the breakpoint table above is a UX recommendation only.
- Custom font availability and licensing for `ivypresto-headline` and `neue-haas-grotesk-text/display` were not verified; these are third-party commercial webfonts referenced via `font-family` declarations only.
- Poppins appears in the supplied font list but no selector tying it to a specific role was found; it has been omitted from the typography scale pending further evidence.
