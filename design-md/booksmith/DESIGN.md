---
version: alpha
name: "The Booksmith"
source_url: "https://www.booksmith.com"
captured_at: "2026-09-29T04:18:48.911892+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The Booksmith's site exposes two CSS custom properties, --color-primary (#df304a, a warm red) and
  --color-secondary (#302a27, a near-black warm brown), which anchor this interpretation as the brand's
  primary and ink colors. The remainder of the observed palette comes largely from a third-party cookie-
  consent widget (Klaro) and Drupal admin theme (Gin), so grays such as #fafafa, #eaeaea, #dddddd, #5c5c5c
  and #a0a0a0 are treated as generic UI neutrals rather than confirmed brand tokens, and are reused here for
  canvas, hairlines, and muted text. A small set of blues (#2581c4, #007fff family) and a green (#1a936f)
  also appear only in third-party widget contexts; they are mapped speculatively to link and accent roles
  since no dedicated brand accent was observed. A CSS variable references --font-poppins, suggesting an
  intended Poppins typeface, but no @font-face rule or rendered font-family list confirms it loads; the
  observed font_families are Arial, Helvetica, and Font Awesome icon fonts, so this spec uses Arial/Helvetica
  as the verified base with Poppins noted only as an inferred aspiration. The interpretation favors a plain,
  content-forward bookstore layout: dense event and new-release listings, a restrained red accent for CTAs
  and price/availability cues, and generous whitespace consistent with a Drupal commerce theme.

colors:
  primary: "#df304a"
  ink: "#302a27"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#fafafa"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  accent-green: "#1a936f"
  link: "#2581c4"
  highlight-bg: "#fffa90"
  highlight-text: "#777620"
  border-strong: "#5c5c5c"
typography:
  display-xl: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.45, letterSpacing: "0px"}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: "18px", letterSpacing: "0.2px"}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
  event-card:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    dateColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.highlight-bg}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.highlight-bg}"
    textColor: "{colors.highlight-text}"
    rounded: "{rounded.xs}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"

## Components
**button-primary** uses the confirmed --color-primary red as fill, proposed for "RSVP," "Add to Cart," and "Buy Tickets" actions seen repeatedly in the event listings; hover/active states were not observed and are proposed as a slightly darkened fill.

**button-secondary** is an outline treatment for lower-emphasis actions (e.g., "See all items," "Browse All"); border and text colors are inferred from the neutral gray set since no secondary-button CSS was captured.

**text-input** covers the site search field and any login/newsletter forms; padding, border, and radius are proposed defaults matching the sm rounded token, which is corroborated by the one observed --border-radius:4px value in the Klaro widget CSS.

**nav-bar** represents the main/utility navigation ("Books / Events / About Us," search, login, wishlist, cart) implied by the page text; a plain white bar with a bottom hairline is proposed, as no header background color was directly observed.

**product-card** models the "New Fiction in Hardcover" grid items (title, author, price, blurb). Price color reuses the primary red for visual consistency with CTAs; card background and border are proposed neutrals.

**event-card** is a category-appropriate component for Booksmith's frequent author events, pairing a red date/time accent with muted caption-style venue/address text, reflecting the dense event listing structure in the page text.

**hero** proposes a dark ink-background banner for the homepage image carousel ("Home Page Image") noted in the content; typography and padding are proposed since no hero-specific CSS was supplied.

**footer** reuses the ink color for a dark footer band, with the observed yellow-tint (#fffa90) proposed as a link/hover accent for contrast against the dark background; this pairing is inferred, not measured.

**badge** is proposed for "New Release" and "Bestseller" labels visible in the New Fiction listings, using the olive-on-yellow pair (#777620 on #fffa90) drawn directly from the observed palette, though its actual UI usage was not confirmed.

**search** models the header search widget ("Search type: Books / Audiobooks / Merchandise / Services"), styled as a bordered input with a muted icon color; exact icon rendering (Font Awesome) is observed in the CSS but its color/state is not.

## Responsive Behavior
This is a proposed breakpoint scheme, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <600px | Single-column stacks for nav, event list, and product grid; nav collapses to a hamburger/off-canvas menu (proposed). |
| tablet | 600–959px | Two-column product/event grids; search and utility menu may condense into icons. |
| desktop | ≥960px | Multi-column product grid (3–4 up), persistent horizontal nav, sidebar or inline event calendar. |

Touch targets should be at least 44×44px for cart/wishlist/search icons and event RSVP buttons. Nav collapse threshold and exact grid column counts are proposed conventions, not extracted from live layout or breakpoint CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from a static CSS/text snapshot and carries several limitations. Most supplied colors originate from third-party widget stylesheets (Klaro cookie consent, Drupal Gin admin theme, Font Awesome) rather than confirmed page-body brand styling; their mapping to roles like accent-green, link, and highlight is inferred, not brand-verified. The --font-family: var(--font-poppins) declaration implies an intended Poppins typeface, but no @font-face rule, font-loading link, or rendered font stack in font_families confirms Poppins actually loads or is licensed for use; Arial/Helvetica are used here as the only directly observed families, with Poppins treated as unverified. All typography sizes, spacing values, rounded values (aside from the single 4px radius found in Klaro CSS), hero/footer treatments, and responsive breakpoints are proposed conventions for an independent-bookstore layout, not measured from live rendering. No hover, focus, active, error, or disabled interaction states were observed. Mobile navigation collapse behavior, grid column counts, and touch-target sizing are design recommendations only. Actual product imagery, cart/checkout UI, and event RSVP flows were not present in the supplied evidence.
