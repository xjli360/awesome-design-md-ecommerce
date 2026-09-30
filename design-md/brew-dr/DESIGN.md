---
version: alpha
name: "Brew Dr"
source_url: "https://brewdrkombucha.com"
captured_at: "2026-09-29T04:16:02.347482+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Brew Dr. Kombucha's supplied CSS centers on a deep teal identity, with `#006072` (documented as a `--dark-slate-grey` / `--_brew-dr-library---deep-teal` custom property) recurring across buttons and headline treatments, alongside closely related teal variants (`#05414c`, `#013741`, `#036072`, `#016172`, `#006172`). A pale `#fafaf4` "floral white" token and a bright `#1ecad3` "clear-mind" teal round out the brand-specific evidence. Neutral grays (`#333`, `#777`, `#ddd`, `#f5f5f5`) come from generic body-copy and Webflow default styling. Typography is mixed: `Arial, sans-serif` is the base body stack, `gopher` and `Bricolage Grotesque` drive large jumbo headlines (110px observed), and `din-2014` / `din-2014-narrow` power uppercase button and CTA labels. A large set of Bootstrap-pattern alert/button colors (blues, greens, ambers, reds) also appears in the CSS but reads as inherited component-library scaffolding rather than deliberate brand color, so it is excluded from the interpreted palette below.

  This interpretation proposes a calm, organic-beverage system: deep teal as the primary brand color and CTA fill, floral-white and light-teal tints as soft section backgrounds, dark charcoal-teal for headline ink, and the bright clear-mind teal reserved for small accents (badges, tags, underlines). Rounded-full buttons echo the observed `100px`/pill radii; sharp `0px` radii are kept for legacy `.w-button` states. All sizing not explicitly present in the CSS (spacing scale, most typographic steps, shadows) is proposed and labeled inferred throughout.

colors:
  primary: "#006072"
  ink: "#013741"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#fafaf4"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent: "#1ecad3"
  accent-tint: "#d7f2f3"
  surface-deep: "#05414c"
typography:
  display-xl: {fontFamily: "Bricolage Grotesque, sans-serif", fontSize: 110px, fontWeight: 700, lineHeight: 1, letterSpacing: -1px}
  display-md: {fontFamily: "gopher, sans-serif", fontSize: 56px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "din-2014-narrow, sans-serif", fontSize: 24px, fontWeight: 800, lineHeight: 1, letterSpacing: 0.5px}
  body-md: {fontFamily: "Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 20px, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 18px, letterSpacing: 0px}
  caption: {fontFamily: "Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 16px, letterSpacing: 0.3px}
  button-md: {fontFamily: "din-2014-narrow, sans-serif", fontSize: 22px, fontWeight: 800, lineHeight: 1.2, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    shadow: "0 1px 3px rgba(0,0,0,0.08)"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  flavor-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.accent}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"

## Components
**button-primary** renders the deep-teal fill with white label text, matching the observed `.submit-button` background using `var(--dark-slate-grey)` and pill-shaped radii seen on `.button`/`.button-text`. Proposed hover/active darkening states are inferred, not observed.

**button-secondary** is an outline variant for lower-emphasis actions (e.g. "Find Us", secondary nav CTAs). Its pill radius and teal border are proposed extensions of the primary button's shape language; no outline-button class was present in the supplied CSS.

**text-input** covers newsletter/email capture fields (the page text references an email signup). Border, radius, and padding are proposed since no dedicated `.w-input` styling was included in the evidence.

**nav-bar** reflects the site's flat top navigation (About, Products, Impact, Find Us, Blog, Merch links per the page text) plus the confirmed `.w-nav-button` mobile toggle class, indicating a collapsing hamburger pattern. Exact bar height/background were not measured.

**product-card** is proposed for the bottles/cans/iced-tea flavor grid implied by the "Explore our flavors" and "Kombucha in bottles / kombucha in Cans / Sparkling Iced Tea" navigation items. Card shadow and radius are inferred defaults, not extracted from CSS.

**hero** models the homepage banner ("Elevate your tea… Discover our smooth, refreshing, organic tea beverages") using the jumbo display typography and floral-white background token, both grounded in the `.h1-jumbo` and `--floral-white` evidence.

**footer** uses the darkest teal token as a full-bleed footer background with white text, covering the observed footer link list (Flavors, Kombucha, Iced Tea, Find In Store, Shop, About, FAQ, Wholesale, Careers, Blog, Brand Assets, Contact Us). Actual footer background color was not directly confirmed in the CSS rules supplied.

**badge** supports short trust callouts like "ORGANIC · PROBIOTIC · NO FAKE STUFF" seen in the page copy, using the light teal tint and primary-teal text as a proposed pairing.

**search** is a proposed component; no search UI was evidenced in the supplied CSS/text, included here for structural completeness of an e-commerce-adjacent site.

**flavor-tag** is a category-appropriate proposed component for labeling product attributes such as "Gut-friendly," "Perfectly Sweet," or "Sparkling," echoing the short benefit callouts in the page text, styled as a small teal-bordered pill distinct from the primary badge.

## Responsive Behavior
This is a recommendation, not measured site behavior:

| Breakpoint | Width      | Nav pattern                  | Grid columns |
|-----------|------------|-------------------------------|--------------|
| sm        | <480px     | Hamburger (`.w-nav-button`)   | 1            |
| md        | 480–767px  | Hamburger                     | 1–2          |
| lg        | 768–991px  | Inline nav or hamburger       | 2–3          |
| xl        | ≥992px     | Full inline nav               | 3–4          |

Touch targets should be at least 44×44px for nav toggles and buttons. The nav should collapse into the `.w-nav-button` pattern already present in the CSS at narrower widths, though the exact collapse breakpoint was not present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, hover/focus states, or actual responsive breakpoints were observed. Semantic role assignments (e.g., which teal serves as "primary" vs. "surface-deep") are inferred from selector names and usage context, not confirmed via live inspection. Spacing scale, shadow values, most typographic sizes below `display-xl`, and letter-spacing values are proposed defaults, not measured. A large set of Bootstrap-style alert/button colors present in the raw palette (blues, greens, ambers, reds) was intentionally excluded as generic framework scaffolding rather than brand color. Custom font availability, licensing, and self-hosting/Typekit status for `gopher`, `din-2014`, `din-2014-narrow`, `Bricolage Grotesque`, and `Handelson One` were not verified. Interaction patterns and mobile layout behavior are not observed and are marked proposed throughout.
