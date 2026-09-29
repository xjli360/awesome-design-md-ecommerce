---
version: alpha
name: "PetLab Co."
source_url: "https://thepetlabco.com/"
captured_at: "2026-09-29T03:59:18.262366+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from a CSS custom-property system (--oke-* review widget
  tokens and --font-inter design tokens) plus editor-authored heading styles found on the
  PetLabCo. storefront. Two font families are confirmed by rule: Inter drives all body copy,
  buttons, inputs and navigation text, while Copernicus (a serif) is reserved for large
  editorial headings (.text-editor h1, .text-header-text-24), giving the brand a blend of
  clinical, sans-driven UI chrome with a warmer editorial voice for hero and section titles.
  The observed palette is dominated by deep navy blues (#001c72, #33498e, #354d98), which we
  treat as the inferred primary brand color for CTAs and links, paired with a confirmed
  review-widget accent green (#076d08, --oke-highlightColor) used for trust/positive signals
  and an amber (#ff9a0a, --oke-stars-foregroundColor) reserved for star ratings. Neutral grays
  (#1e1f24 ink, #3f424d body, #8d92a3 muted, #d8dadf hairline, #f5f5f1/#f7f8f8 soft surfaces)
  come directly from --oke-text-primaryColor, --oke-border-color and --oke-shadingColor. Card
  radii, spacing and breakpoints are not present in the supplied CSS and are therefore proposed
  defaults suited to a supplement e-commerce layout, clearly marked as inferred below.

colors:
  primary: "#001c72"
  ink: "#1e1f24"
  canvas: "#ffffff"
  body: "#3f424d"
  muted: "#8d92a3"
  hairline: "#d8dadf"
  surface-soft: "#f5f5f1"
  surface-card: "#f7f8f8"
  on-primary: "#ffffff"
  accent-success: "#076d08"
  accent-star: "#ff9a0a"
  accent-warm: "#ff8700"
  alert: "#b91c1c"
  badge-magenta: "#cd0053"
  border-strong: "#b5b9c4"
typography:
  display-xl: {fontFamily: "Copernicus, serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Copernicus, serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Copernicus, serif", fontSize: "24px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0.1px"}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: "16px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    mutedTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** — The main add-to-cart / "Shop Now" call to action. Uses the inferred navy primary against white text with confirmed 16px/600 button typography from --oke-button-fontSize/--oke-button-fontWeight. Hover/active states are not observed and are proposed as a slight darken.

**button-secondary** — An outline variant for lower-emphasis actions (e.g. "View All Products"), sharing button-primary's typography but with primary-colored text on a white surface; border and hover state are proposed.

**text-input** — Email capture and account/login fields (e.g. newsletter signup, quiz start). Border color is the confirmed --oke-border-color hairline; padding and radius are proposed since no explicit input CSS was supplied beyond generic form-element resets.

**nav-bar** — Top utility/nav row (Shop, About, Learn, Health Quiz, Account, Help, cart). Rendered on white canvas with ink text and a bottom hairline; sticky/scroll behavior is not observed and is not asserted.

**product-card** — Repeats for best-seller grid items (title, "FREE gift for subscribers" note, strikethrough/sale price). Uses surface-card background with a hairline border; title uses the serif title-md style to echo hero headings, price and support copy use body styles. Card elevation/shadow is proposed, not observed.

**hero** — Top-of-page banner ("Science-backed pet supplements… Take The Quiz"). Uses the soft neutral surface with the large serif display-xl headline confirmed by the .text-editor h1 (48px/600/Copernicus) rule and body-md supporting copy.

**footer** — Dark ink-colored band containing Company/Information/Learn link columns and legal/FDA disclaimer text, set in small body-sm type on inverted (on-primary) text color; this inversion is inferred from typical footer conventions, not directly measured.

**badge** — Small pill labels such as "New", "Two Pack Sizes", or trust markers (NASC Certified, Free Shipping). Uses the confirmed --oke-highlightColor green as a default state; alternate badge colors (e.g. warm orange for sale, magenta for limited offers) are proposed using other palette entries such as {colors.accent-warm} or {colors.badge-magenta}.

**search** — Implied header search affordance; styled with muted placeholder text and a hairline border on the light card surface. No search-specific selector was present in the supplied CSS, so this pattern is fully proposed.

**subscription-toggle** — Category-appropriate component for the "subscribe & save" purchase option seen throughout PDP-style copy ("FREE gift for subscribers", "Save up to 40%"). Selected state uses the primary navy fill; unselected state sits on the soft surface. No interaction states were observed; this is a proposed pattern based on the subscription messaging present in the page text.

## Responsive Behavior

Recommended breakpoints (proposed, not measured):

| Breakpoint | Width      | Layout notes (proposed) |
|-----------|------------|--------------------------|
| mobile    | 0–639px    | Single-column hero and product grid; nav collapses to hamburger + icon row |
| tablet    | 640–1023px | 2-column product grid; nav shows condensed label set |
| desktop   | 1024–1439px| 3–4 column product grid; full nav with all top-level links visible |
| wide      | 1440px+    | Max-width content container centered on {colors.canvas}; grid gains extra gutter via {spacing.xl} |

Touch targets should be a minimum 44×44px for buttons and nav icons (proposed, not verified against live markup). Primary nav is expected to collapse into a drawer or hamburger menu below the tablet breakpoint; this collapse behavior is a recommendation only and was not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, computed box model, or real breakpoint values were captured, so the responsive table above is a proposed recommendation, not a measurement.
- Color **roles** (primary, alert, badge colors, etc.) are inferred from recurrence and adjacent context (e.g. --oke-highlightColor, --oke-stars-foregroundColor); the presence of a hex in the palette does not itself confirm its UI role site-wide.
- Radius and spacing scales are proposed conventions; no border-radius or margin/padding values were present in the supplied CSS rules.
- Archivo, Neuzeit-Grotesk, and several monospace families appear in the raw font-family list but have no associated selector/rule in the supplied evidence, so they are not assigned a role here.
- No hover, focus, active, disabled, or error states were observed for any interactive component; all such states above are explicitly proposed.
- Mobile/tablet navigation collapse, drawer behavior, and touch interactions were not observed and are stated only as guidance.
- Licensing/availability of Copernicus and Inter for production use was not verified from the supplied evidence; generic serif/sans-serif fallbacks are assumed acceptable.
