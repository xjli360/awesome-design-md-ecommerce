---
version: alpha
name: "Little Toy Tribe"
source_url: "https://littletoytribe.com.au"
captured_at: "2026-09-28T09:21:11.422225+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Little Toy Tribe is a Brisbane-based Shopify storefront selling open-ended,
  educational toys and children's books from brands like Grimm's, Grapat,
  Connetix and BRIO. The observed CSS shows a soft, pastel-forward palette:
  a blush pink (#f6bdbe) drives the header overlay background and is reused
  as the review-star fill color in the Judge.me widget variables, making it
  the strongest evidence-backed candidate for a primary brand accent. Neutral
  grays (#242424, #4f4f4f, #757575, #e6e6e6, #f2f2f2) form the text and
  surface scale typical of a clean product-grid storefront. A muted red
  (#d02e2e) and green (#3d7f4e) appear in the palette and are inferred here
  as sale/promo and reassurance-messaging accents respectively — these role
  assignments are inferred, not confirmed by selector context. Montserrat is
  the only clearly brand-authored font family observed (site theme.min.css
  references a button font stack without literal values); Consolas/monospace
  and swiper-icons are utility/icon fonts, not brand typography. This
  interpretation proposes a warm, rounded, toy-shop aesthetic: soft pink
  accents, generous whitespace, and card-based product/brand browsing
  consistent with the site's deep age/occasion/collection taxonomy. Rounded
  corners and spacing are proposed conventions layered onto the observed
  color and type evidence, not measured from live layout.

colors:
  primary: "#f6bdbe"
  accent: "#d02e2e"
  reassurance: "#3d7f4e"
  teal-soft: "#9ccfc9"
  ink: "#242424"
  canvas: "#ffffff"
  body: "#4f4f4f"
  muted: "#757575"
  hairline: "#e6e6e6"
  surface-soft: "#f2f2f2"
  surface-card: "#fefefe"
  on-primary: "#ffffff"
  dark-surface: "#292929"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.6, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  age-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
    typography: "{typography.caption}"

## Components

**button-primary** uses the blush pink observed in the header overlay
(`#f6bdbe`) as its fill, with dark ink text for contrast, since no
white-on-pink button was directly observed. **button-secondary** is a
proposed outline variant reusing the primary hue for border and label,
matching the `.btn--secondary` pattern in theme.min.css which derives its
border/text color from the same CSS variable as the filled button.

**text-input** and **search** are proposed form patterns using the light
neutral surface and hairline border colors observed across the gray scale,
with a fully rounded search field to suit a playful toy-shop tone; rounding
value is proposed, not measured.

**nav-bar** reflects the confirmed `.header-section` and `.overlay-header`
selectors, which set a semi-transparent and solid pink background
(`rgba(246,189,190,.88)` and `#f6bdbe`) — the design collapses this to the
flat primary token for simplicity.

**product-card** and **hero** are proposed compositional patterns typical of
Shopify toy storefronts; card border and radius values are inferred defaults
since no `.product-card` selector was present in the supplied CSS excerpt.

**footer** is inferred to use the dark neutral (`#292929`) seen on the
wishlist/"add to list" button as a plausible dark-surface footer treatment,
since no footer-specific selector was supplied — this is a stylistic
extrapolation, not an observation.

**badge** reuses the red (`#d02e2e`) as a sale/promo indicator, appropriate
given the site's "On Sale" navigation entries, though the red's original CSS
role was not disclosed in the evidence.

**search** and **age-filter-chip** are category-appropriate additions
reflecting the site's extensive "By Age" (Newborn through 8+ Years)
navigation; chip styling with an active pink fill is proposed to mirror the
Judge.me star color reuse pattern already present in the codebase.

## Responsive Behavior

This is a recommended breakpoint structure, not measured from live site
behavior:

| Breakpoint | Width      | Nav behavior                  | Grid            |
|-----------|------------|--------------------------------|------------------|
| mobile    | <640px     | Collapsed hamburger menu       | 2-col product grid |
| tablet    | 640–1024px | Condensed horizontal nav       | 3-col product grid |
| desktop   | >1024px    | Full mega-menu (age/occasion/collection) | 4-col product grid |

Touch targets for nav links, filter chips, and buttons should maintain a
minimum 44px tap height given the site's child/parent audience and menu
depth ("See more / Close menu" patterns in the page text suggest expandable
mobile sub-menus). Age and occasion filter chips should wrap to multiple
rows on mobile rather than scroll horizontally, given the long taxonomy
lists observed in the navigation text.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction did not include literal `--primary-btn-bg-color`,
  `--primary-btn-text-color`, or `--button-font-stack` values; button colors
  and font-stack are inferred from adjacent evidence (header pink, Montserrat
  usage) rather than directly observed.
- Role assignment for `#d02e2e` (accent/sale) and `#3d7f4e`
  (reassurance/eco) is inferred from typical toy-ecommerce conventions, not
  from selector context in the supplied CSS.
- No `.product-card`, `.footer`, or `.hero` selectors were present in the
  supplied evidence; those component definitions are proposed, category-
  typical patterns, not observed layout.
- Montserrat's licensing/self-hosting status was not verified from the
  supplied evidence; generic sans-serif fallback is included per convention.
- JudgeMeStar, Consolas, and monospace are utility/icon or fallback fonts
  and were excluded from brand typography tokens.
- Mobile menu interaction ("See more / Close menu") is referenced in page
  text but no interaction states, animations, or measured mobile layout were
  observed.
- Spacing and rounding scales are proposed conventions layered onto the
  color/type evidence; no pixel-level spacing values were present in the
  supplied CSS rules.
