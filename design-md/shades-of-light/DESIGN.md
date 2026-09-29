---
version: alpha
name: "Shades of Light"
source_url: "https://shadesoflight.com"
captured_at: "2026-09-28T04:50:05.947614+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Shades of Light is an online home-furnishings retailer spanning chandeliers, sconces,
  ceiling fans, lamps, mirrors, rugs and furniture. The only font evidence supplied is
  the Next.js-generated variable "--font-montserrat" mapped to the literal family tokens
  "__Montserrat_f56828" and its fallback "__Montserrat_Fallback_f56828"; no other
  proprietary typeface is present, so all type roles reuse these exact tokens with a
  sans-serif generic fallback. The observed palette is dominated by near-black text
  (#231f20, #333333), warm neutrals (#f7f6f0, #fafaf6, #f1ebde), and a soft brass/gold
  tone (#b19a6a) that reads as the most brand-appropriate accent for a lighting
  retailer, though this role is inferred rather than confirmed as an official brand
  color. Two near-identical reds (#da0f0f, #da100f) most plausibly serve sale/clearance
  messaging, and a blue (#2563eb) likely marks links or focus states — both semantic
  assignments are inferred. The single confirmed border-radius token (0.5rem/8px)
  anchors the rounded scale. Layout, spacing, and interaction states are proposed
  conventions for an e-commerce catalog, not measured observations, and are labeled
  accordingly throughout.

colors:
  primary: "#b19a6a"
  ink: "#231f20"
  canvas: "#ffffff"
  body: "#404040"
  muted: "#7f7f7f"
  hairline: "#d9d9d9"
  surface-soft: "#f7f7f7"
  surface-card: "#fafaf6"
  on-primary: "#ffffff"
  accent-alert: "#da0f0f"
  accent-link: "#2563eb"
  surface-alt: "#f1ebde"
  shadow-soft: "#00000033"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "\"__Montserrat_f56828\", \"__Montserrat_Fallback_f56828\", sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "\"__Montserrat_f56828\", \"__Montserrat_Fallback_f56828\", sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "\"__Montserrat_f56828\", \"__Montserrat_Fallback_f56828\", sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "\"__Montserrat_f56828\", \"__Montserrat_Fallback_f56828\", sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "\"__Montserrat_f56828\", \"__Montserrat_Fallback_f56828\", sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "\"__Montserrat_f56828\", \"__Montserrat_Fallback_f56828\", sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "\"__Montserrat_f56828\", \"__Montserrat_Fallback_f56828\", sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.lg}"

## Components
**button-primary** uses the inferred brass accent as its fill, appropriate for primary calls-to-action like "Add to Cart," with white text for contrast; hover/active states are proposed, not observed. **button-secondary** is an outlined variant on the canvas background for lower-emphasis actions such as "View Details." **text-input** models a bordered field for search and account forms, using the confirmed 8px-derived radius scale reduced to a tighter 2px for compact controls, since no distinct input radius was captured. **nav-bar** represents the top-level bar implied by the extensive category structure (Chandeliers & Pendants, Bath & Wall Lights, Ceiling Lights, Fans, Outdoor Lights, Lamps & Shades, Mirrors & Decor, Furniture, Rugs); its mega-menu sibling component proposes the dropdown surface needed to house this depth of navigation, though the mega-menu's actual visual treatment was not observed. **product-card** proposes a catalog-tile pattern with soft off-white background, suited to product photography-heavy grids typical of a lighting/decor storefront. **hero** proposes a warm-neutral banner zone using the beige surface-alt tone, appropriate for seasonal or collection promotion (e.g., "Erin & Ben Co." or "Chris Loves Julia" designer collections referenced in the copy). **footer** is proposed as a dark, ink-toned band for sitemap and legal links, inverted from body text for contrast. **badge** applies the observed red tones to sale/clearance labeling, since "Clearance Sale" appears repeatedly across nearly every category in the supplied text, making a dedicated badge component practically justified even though its exact styling wasn't captured in CSS.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:
| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <640px | Single-column product grid; nav collapses to a hamburger/drawer pattern given the mega-menu's category depth. |
| Tablet | 640–1024px | 2–3 column product grid; mega-menu may condense to accordion sections. |
| Desktop | 1024–1440px | Full mega-menu with multi-column flyouts; 4-column product grid. |
| Wide | >1440px | Increased gutter/spacing; content max-width constrained. |

Touch targets should be at least 44px in the compact/mobile nav drawer; the mega-menu's many category links suggest search should be prioritized above browsing on small screens. No mobile layout, menu collapse animation, or touch interaction was actually observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
Static CSS/text extraction provides no rendered layout, so grid structure, spacing rhythm, and breakpoint values above are proposed conventions, not measurements. Color-to-role mapping (brass as primary/brand accent, red as sale/alert, blue as link) is inferred from typical retail conventions and hue frequency, not from confirmed component usage in the supplied CSS. The only typography evidence is the Next.js-generated Montserrat variable and its fallback class names; actual font weights, license terms, and self-hosting status were not verified. Interactive states (hover, focus, disabled, mobile menu behavior) were not observed and are marked proposed throughout. The `--radius: 0.5rem` token was the only concrete radius value found; all other radius steps are extrapolated. Shadow color values reuse only alpha-blended black tones present in the supplied palette, since the site's actual box-shadow color token fell outside the observed palette list.
