---
version: alpha
name: "BlushingDrops"
source_url: "https://blushingdrops.com"
captured_at: "2026-09-28T09:59:23.807026+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Blushing Drops' storefront presents as a custom photo-backdrop and event-decor
  brand rather than a nursery-specific shop; observed navigation and product
  copy span Wedding, Bridal Shower, Bachelorette, Engagement, Birthday,
  Graduation, Baby Shower, Baptism, and Holiday categories, so baby/nursery
  content is one vertical among several rather than the brand's sole focus.
  This interpretation is grounded in that broader "custom celebration decor"
  positioning.

  The supplied CSS exposes a blush-forward palette: soft pink surfaces
  (header background #f9e5e4, button fill #f5d1d1, rating-icon accent
  #f6c6c6) paired with near-black and warm-gray type (#1a1a1a, #393939cf,
  #333333) on a white canvas. Hairlines and quiet fills use light neutrals
  (#dedede, #e6e6e6, #fdfbf8). A wider swatch set (navy, teal, orange,
  greens) also appears in the evidence but reads as Shopify color-picker /
  variant-swatch options rather than confirmed brand colors, so it is
  excluded from primary roles here.

  Typography combines DM Sans (sans, inferred body/paragraph and UI role)
  with Crimson Pro (serif, inferred heading role from the theme's h1–h6
  variable structure) and Pinyon Script as a decorative accent consistent
  with the site's "Whimsical," "Coquette," and "Quotes" style categories.
  Role assignments for fonts and colors are inferred from CSS variable
  naming and selector context, not confirmed visual audit.

colors:
  primary: "#f5d1d1"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dedede"
  surface-soft: "#f9e5e4"
  surface-card: "#fdfbf8"
  on-primary: "#393939cf"
  accent-blush: "#f6c6c6"
  border: "#e6e6e6"
typography:
  display-xl: {fontFamily: "'Crimson Pro', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Crimson Pro', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  display-script: {fontFamily: "'Pinyon Script', cursive", fontSize: 36px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'DM Sans', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'DM Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'DM Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'DM Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'DM Sans', sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.2px}
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    accentTypography: "{typography.display-script}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  occasion-nav:
    backgroundColor: "{colors.surface-soft}"
    itemTypography: "{typography.body-sm}"
    activeTextColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the observed blush fill (#f5d1d1) with the dark warm-gray text color (#393939cf) taken directly from the email-signup button rule; hover state (lighter fill, #fdfbf8, per the observed `:hover` rule) is proposed as the default interactive pattern site-wide, not confirmed on all buttons.

**button-secondary** is an inferred outline variant for lower-emphasis actions (e.g., "View all," "Order Now" links) using the ink color on a transparent background with a hairline border; no direct CSS evidence of a secondary button style was supplied.

**text-input** is proposed for search and account fields; only the theme's default border/background tokens were observed, so exact input styling (focus ring, error state) is unmeasured.

**nav-bar** reflects the observed header background (#f9e5e4) from the `#shopify-section...header` rule, extended into a full navigation bar treatment covering the mega-menu categories (Wedding, Baby Shower, Graduation, etc.).

**product-card** is inferred from the repeated "Add / Choose / price" product-grid text pattern in the page excerpt (e.g., "$68.00 USD"); card surface, radius, and padding are proposed defaults, not measured from layout CSS.

**hero** combines the display-xl heading role with the Pinyon Script accent, matching the site's tagline ("Your Story, Beautifully Designed") and blush header background; exact hero sizing/imagery is not confirmed.

**footer** is proposed as a dark-ink surface for contrast, referencing observed footer links (About Us, F.A.Q, Shipping & Return, Blog, email signup) but the actual footer background color was not directly evidenced.

**badge** is proposed for promotional flags ("Free Shipping," "Graduation Season") using the accent-blush swatch (#f6c6c6) sourced from the rating-icon CSS variable, repurposed here as a small-label accent.

**occasion-nav** is a category-appropriate component addressing the site's occasion-driven shopping model (Wedding, Bridal Shower, Baby Shower, Graduation, etc.), styled on the same soft-pink surface as the header.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <480px | Single-column stacking, nav collapses to a hamburger/menu drawer; touch targets ≥44px. |
| Tablet | 480–959px | 2-column product grid; nav condenses secondary categories under "More." |
| Desktop | ≥960px | Full mega-menu nav, 3–4 column product grid, hero at full width. |

This table is a recommendation based on common Shopify-theme conventions and the presence of a "More" menu grouping in the observed text; it is not measured site behavior. No JavaScript-driven interaction, animation timing beyond the documented `--hover-transition-duration: .25s` variable, or actual mobile screenshots were available.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered screenshots, computed layout, or DOM measurements were available.
- Font-to-role mapping (Crimson Pro = heading, DM Sans = body, Pinyon Script = accent) is inferred from CSS variable naming conventions and thematic category names ("Whimsical," "Coquette"), not a confirmed style-guide.
- The extended color swatch set (e.g., #8b0000, #006400, #1d3686, #1990c6, #ea6952) likely represents Shopify variant/color-picker options rather than brand UI colors; excluded from primary role assignment.
- Category mismatch: the requested brief labels this brand "Nursery Decor," but observed evidence shows a general celebration/event-backdrop store where baby shower is one of many categories; this document reflects the evidenced scope.
- All pixel sizes in typography beyond the button's explicit `12px 24px` padding and `14px`/`500` font values are proposed, not measured.
- No confirmed hover/focus/error states beyond the single documented button `:hover` rule; other interaction states are proposed placeholders.
- Custom font licensing/availability (Crimson Pro, DM Sans, Pinyon Script) was not verified for production use.
