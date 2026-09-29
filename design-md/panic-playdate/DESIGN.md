---
version: alpha
name: "Panic (Playdate)"
source_url: "https://play.date"
captured_at: "2026-09-28T04:57:56.157478+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Playdate's site evidence points to a bright, toy-like palette layered over a neutral, near-monochrome UI shell. The dominant accent is a warm brand yellow (#ffc833, close to the device's own #fbc651 shell color), paired with a dark warm-black ink (#312f28, the CSS "screen-black") used for both body text and, inverted, as button fill. Backgrounds sit on a soft off-white/gray (#efefef, #f5f5f5) rather than pure white, with true white (#ffffff) reserved for cards and inputs. A vivid purple (#6c00ff) and an orange-red (#ef5023) appear as secondary/link and negative-state accents respectively, echoing the playful multi-color game icons visible in the evidence. Typography is set in "Roobert" with Helvetica/sans-serif fallback — a single observed family used here across all scales via weight and size variation, since no distinct display face was supplied.
  This interpretation treats yellow as the primary brand accent (not the default button color, which the CSS actually keys to ink-on-white), ink as body/on-primary text, and purple as the interactive/link color, all explicitly inferred mappings. Corner radii, spacing, and component states are proposed conventions calibrated loosely to observed rem/em radii, not measured pixel values.

colors:
  primary: "#ffc833"
  ink: "#312f28"
  canvas: "#efefef"
  body: "#312f28"
  muted: "#7a8085"
  hairline: "#bbbbbb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#312f28"
  link: "#6c00ff"
  negative: "#ef5023"
  device-yellow: "#fbc651"
  interactive: "#9d70db"
  tomato: "#ff004e"
  dark-canvas: "#000000"
  dark-card: "#212223"
typography:
  display-xl: {fontFamily: "Roobert, Helvetica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Roobert, Helvetica, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Roobert, Helvetica, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Roobert, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roobert, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Roobert, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roobert, Helvetica, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 0px}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  button-cta-order:
    backgroundColor: "{colors.link}"
    textColor: "{colors.surface-card}"
    typography: "{typography.title-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.tomato}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  spec-card:
    backgroundColor: "{colors.dark-card}"
    textColor: "{colors.device-yellow}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** follows the CSS pattern where `--button-bg` resolves to the ink/text color and `--button-text` resolves to the card/white color — an inverted, high-contrast pill button. It is proposed as the default action button (e.g., "Sign In", "Add to Cart") using a fully rounded pill shape, matching the `border-radius: 1em`–`0.6rem` values seen on `div.button` and form buttons.

**button-secondary** is a proposed outline variant for lower-emphasis actions, reusing the ink color as both text and border on a transparent fill, keeping the same pill radius for visual consistency with the primary button.

**button-cta-order** is grounded directly in the `div#button-order a` rule, which shows a purple gradient background, white text, heavy weight, large font-size (1.78em), and a fully rounded pill with inset highlight/shadow styling. This is modeled as the flagship "Preorder"-style call to action seen on the homepage hero.

**text-input** is proposed for newsletter/search/account forms; the CSS confirms `--input-bg: var(--page-bg)` and `--input-text: var(--text)`, so the light canvas background with ink text is directly evidenced, while border and radius values are inferred conventions.

**nav-bar** reflects the `#navbar` selector inheriting `background-color: var(--page-bg)` and `color: var(--text)`, plus the internal-nav button link rule showing a card-background pill with hover color shifting to the link/purple token — a state that is proposed as a hover treatment, not confirmed via live interaction testing.

**product-card** is proposed for game/product tiles (e.g., Season games grid, shop items), using the white card background and ink border implied by `--card-bg` and `--card-border: var(--text)` tokens, with a moderate radius consistent with the site's generally rounded, friendly geometry.

**hero** models the large yellow-forward introductory section implied by the page copy ("It's yellow...") and the `h1#logotype` block, which reserves substantial vertical space (40rem height) for a centered logo image; the yellow fill and dark ink text are an inferred brand-forward treatment, not a captured background rule.

**footer** is proposed as a dark, inverted-mode section, drawing on the site's documented dark-mode `:root` override where `--page-bg: var(--black)` and `--text: var(--white)`, appropriate for a closing/legal area contrasted against the light main canvas.

**badge** is a proposed small pill label (e.g., "New", "Free") using the tomato-red accent color present in the palette but not tied to a specific captured selector — its role is inferred from typical e-commerce badge conventions.

**search** reflects the dedicated `search.b31b56dffef0.css` file, which overrides `--subtle`/`--subtler` tokens; the pill shape and card-like background are proposed to match the nav's rounded, friendly interaction style, and the cancel-button SVG icon confirms a live search field exists in the markup.

**spec-card** is a category-appropriate component for a specialty-gadget storefront: a dark panel highlighting hardware specs (screen, crank, Wi-Fi) using the dark-mode card color (`--psd-darkest-gray`) with device-yellow text for emphasis, inferred from the product's dark, screen-like presentation described in the page copy rather than a captured spec-block selector.

## Responsive Behavior

This is a recommended, non-measured breakpoint scheme, since no media queries or live layout were supplied:

| Breakpoint | Range | Layout guidance |
|---|---|---|
| Mobile | <600px | Single-column stack; nav collapses to a menu button ("Show menu" text observed in page copy); hero logo scales down proportionally from the 40rem reference height. |
| Tablet | 600–1024px | Two-column game/product grids; nav-bar shows condensed horizontal links. |
| Desktop | >1024px | Multi-column grids (3–4 across) for Season game cards; full horizontal nav with search field visible inline. |

Touch targets for buttons and nav-bar links should maintain a minimum 44×44px hit area, consistent with the pill-shaped buttons' generous padding (`0.25em–0.35em` vertical, `0.7em` horizontal) observed in the CSS. All of the above is proposed guidance, not measured from the live site.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to static CSS custom properties and rule fragments; no computed styles, DOM structure, or rendered screenshots were available, so real layout, grid systems, and exact component boundaries are not confirmed.
- Color **roles** (e.g., "primary" = brand-yellow, "link" = purple) are inferred from CSS variable names like `--accent`, `--link`, `--interactive`; the site also defines an alternate dark-mode `:root` block with different role-to-color mappings (accent becomes purple, link becomes yellow) that this document does not fully model as a separate theme.
- All typography sizes, weights, and letter-spacing values beyond the single confirmed `font-family: "Roobert", Helvetica, sans-serif;` on `body` are proposed conventions, not measured from rendered text.
- Rounded and spacing scales are standardized proposals loosely inspired by observed `em`/`rem` radius values (e.g., `1em`, `0.6rem`, `3em` pill), not literal conversions.
- Interaction states (hover, focus, active, disabled) beyond the single documented `nav.internal-nav li.button a:hover` color change are proposed and unverified.
- Mobile menu behavior, cart/checkout flow, and Catalog/SDK sub-pages were not present in the supplied evidence.
- "Roobert" is a licensed proprietary typeface (Displaay Type Foundry); its availability, licensing terms, and fallback rendering are not verified by this extraction and must be confirmed before implementation.
