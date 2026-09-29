---
version: alpha
name: "Three Wishes"
source_url: "https://threewishescereal.com"
captured_at: "2026-09-29T04:06:38.208397+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Three Wishes presents its low-sugar cereal and granola line with a warm,
  playful visual system built around a dark cocoa-brown (#3a1d00) paired with
  a soft cream (#fff0e2), evidenced directly in the site's brochure stylesheet
  as `--tw-brand-text` and `--tw-brand-cream`. These two tones anchor primary
  buttons, flavor-selector pills, and body text. A wider observed swatch set
  contributes playful accent colors — yellow, orange, red, and berry pink —
  consistent with cereal-box flavor branding, though the exact assignment of
  each accent to a specific flavor SKU is inferred rather than confirmed.
  Instrument Sans is the only font with a supplied @font-face declaration and
  is treated as the confirmed body/UI typeface. "bogart" and "sausage" appear
  in the site's font-family list without accompanying @font-face rules in the
  supplied evidence; they are used here for display headlines as an inferred,
  brand-appropriate choice, with availability and licensing unverified. Rounded
  pill buttons (999px) and 8px card corners are drawn directly from the
  flavor-buy-buttons CSS. Layout structure (sticky wave-divided header,
  centered logo grid) is inferred from CSS custom properties, not from a
  rendered screenshot.

colors:
  primary: "#3a1d00"
  ink: "#3a1d00"
  canvas: "#fff0e2"
  body: "#3a1d00"
  muted: "#984a00"
  hairline: "#d9d9d9"
  surface-soft: "#fff0e2"
  surface-card: "#ffffff"
  on-primary: "#fff0e2"
  accent-yellow: "#ffdb45"
  accent-orange: "#f7703c"
  accent-red: "#e20e23"
  accent-berry: "#d72788"
  header-dark-text: "#000000"
  header-light-text: "#ffffff"
typography:
  display-xl: {fontFamily: "bogart, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "bogart, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: 23px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Instrument Sans, sans-serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Instrument Sans, sans-serif", fontSize: 18px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Instrument Sans, sans-serif", fontSize: 12px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.02em}
  button-md: {fontFamily: "sausage, Instrument Sans, sans-serif", fontSize: 12px, fontWeight: 800, lineHeight: 1, letterSpacing: 0.02em}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  nav-bar:
    backgroundColor: "transparent"
    textColor: "{colors.header-light-text}"
    scrolledTextColor: "{colors.header-dark-text}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.header-light-text}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  flavor-buy-buttons:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** reflects the `.flavor-buy-buttons__trigger` rule directly: a fully-rounded (999px) dark-brown pill with cream text, lowercase bold label, used for primary calls to action like "shop now." Hover/focus filter transitions are referenced in CSS (`transition:filter .15s ease`) but the exact hover value is not supplied, so hover state is proposed.

**button-secondary** is an inferred outline variant for lower-emphasis actions (e.g. "learn more"), using the observed hairline gray for its border and the primary brown for text, keeping the same pill-adjacent rounding family but at `rounded.md` since no secondary-button CSS was supplied.

**text-input** supports the newsletter capture flow ("feeling@hungry.com / sign up") visible in the page copy. Styling (card-white background, hairline border, sm rounding) is proposed since no dedicated input CSS rule was included in evidence.

**nav-bar** is built from the header's custom properties: a three-column grid (`primary-nav logo secondary-nav`) with a sticky flag (`--header-is-sticky: 1`) and two text-color states — white when transparent over the hero, near-black once scrolled — both values taken directly from the supplied RGB custom properties.

**product-card** uses the confirmed `--tw-card-pad` clamp value for internal padding and an 8px radius consistent with the buy-button radius family, housing flavor imagery, name, and the nested flavor-buy-buttons component.

**hero** is inferred as a full-width section holding the "Sneaky Delicious. Sneaky Nutritious." headline and seasonal callout ("Pumpkin Spice is here!"). The scalloped wave divider is directly evidenced by the header's SVG mask-image transition into the page background.

**footer** groups the sitemap links (Cereal, Granola, Where to Buy, Our Story, Contact), social icons, and legal links observed in the page text, on the cream canvas background with brown ink text for contrast continuity with the header's non-transparent state.

**badge** approximates the sale/sold-out indicators referenced by `--on-sale-badge-background` and `--sold-out-badge-background` custom properties; since their literal RGB values aren't present in the supplied hex swatch list, the closest observed accent (accent-red) is substituted and flagged as an approximation.

**flavor-buy-buttons** (category-specific) directly reflects three supplied CSS classes — `__trigger`, `__pill`, `__btn`, and `__find` — modeling a flavor-selection dropdown with an inline "find in store" link, appropriate for a cereal brand selling multiple SKUs across retail and DTC channels.

## Responsive Behavior

This breakpoint table is a **recommendation**, not measured site behavior; no media queries were supplied in evidence.

| Breakpoint | Range | Nav | Product grid |
|---|---|---|---|
| Mobile | <640px | Collapsed hamburger; logo centered | 1 column |
| Tablet | 640–1024px | Condensed inline nav | 2 columns |
| Desktop | >1024px | Full three-column header grid (`primary-nav logo secondary-nav`) | 3–4 columns |

Touch targets should be no smaller than 44px; the flavor-buy-buttons `__btn` min-height of 3rem (48px) already satisfies this and is used as the baseline for other interactive controls. Secondary/tertiary nav items should collapse into a drawer or sheet below 640px; exact collapse behavior was not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/HTML extraction; no rendered screenshots, animations, or interaction states (hover, focus, active, error) were observed, so those are proposed.
- "bogart" and "sausage" appear only as font-family names in the supplied font list; no @font-face source, weight, or license was provided, so their availability and legal usability are unverified.
- Semantic color roles (muted, on-primary, badge) are inferred by matching supplied hex values to likely UI roles; the site's own RGB-based badge/status variables (success, warning, error, on-sale) do not correspond exactly to any hex in the supplied swatch list, so badge colors are approximated substitutions, not exact matches.
- All typography sizes beyond the four `--text-*` and `--button-font-size` custom properties are proposed estimates for a plausible type scale.
- Mobile navigation collapse, product grid column counts, and hero layout proportions are inferred from CSS custom-property names (e.g. header grid areas) rather than observed rendered layout.
- Spacing and rounding tokens follow a standard proposed scale except where a value (999px, 8px, 0px) is directly confirmed by supplied CSS.
