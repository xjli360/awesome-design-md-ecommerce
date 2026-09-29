---
version: alpha
name: "Tripped Travel Gear"
source_url: "https://trippedtravelgear.com"
captured_at: "2026-09-28T04:35:47.354560+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The evidence shows a bright, white-canvas storefront (#ffffff) with near-black
  body copy (#000000, #333333) and a warm orange accent (#f1a34d) repeated across
  primary buttons, badges, price emphasis, and stat callouts — this is treated as
  the brand's primary action color. A deep navy (#304362) appears consistently in
  the Judge.me review-widget variables (primary color, write-review button,
  reviewer name) and is adopted here as a secondary/trust color. A dark teal
  (#1e3d48) used as a full-width section background is mapped to an accent/hero
  tone, and gold (#efbf04 / #ffc617) is preserved for star ratings. Neutral grays
  (#dddddd, #e6e6e6, #f7f7f7, #777777) support hairlines, search fields, and soft
  surfaces.

  Font evidence lists Montserrat (explicitly forced on a homepage CTA button),
  Nunito Sans, Maven Pro, and Playfair Display alongside system fallbacks
  (Arial/Helvetica/Times). No heading selectors were supplied, so the pairing of
  Playfair Display for display type against Nunito Sans/Montserrat for UI and
  body text is an inferred typographic hierarchy, not a captured observation.

  The resulting interpretation favors a clean, adventure-retail feel: bright
  neutral surfaces, an orange call-to-action that carries through commerce
  moments (buttons, badges, pricing), and navy/teal used sparingly for
  trust-building elements like reviews and feature banners.

colors:
  primary: "#f1a34d"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary: "#304362"
  accent-deep-teal: "#1e3d48"
  star-gold: "#efbf04"
  review-track: "#dfe3e2"
  search-bg: "#e6e6e6"
  neutral-dark: "#424242"
typography:
  display-xl: {fontFamily: "'Playfair Display', serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Playfair Display', serif", fontSize: "36px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "'Maven Pro', sans-serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Nunito Sans', sans-serif", fontSize: "18px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Nunito Sans', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "Arial, sans-serif", fontSize: "12px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "1px"}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: "16px", fontWeight: 700, lineHeight: 1, letterSpacing: "0.3px"}
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
    textColor: "{colors.secondary}"
    borderColor: "{colors.secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.accent-deep-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  search:
    backgroundColor: "{colors.search-bg}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  review-rating:
    backgroundColor: "{colors.review-track}"
    accentColor: "{colors.star-gold}"
    textColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** renders the orange (`#f1a34d`) call-to-action seen across product highlight buttons, gift-card pricing, and the homepage `.needsclick` CTA, paired with white text and Montserrat per the forced `font-family:Montserrat!important` rule. Hover/focus states are proposed, not observed.

**button-secondary** is a proposed outline variant using the navy secondary color for text/border on a transparent background, intended for lower-emphasis actions (e.g., "Learn more") alongside the filled primary button.

**text-input** proposes a light-gray field (`#f7f7f7`) with a hairline border, matching the general neutral-gray hairline family (`#dddddd`, `#e6e6e6`) present throughout the palette; no explicit input selector was supplied, so padding and radius are proposed.

**nav-bar** reflects the `.header` CSS custom properties directly: white background, near-black text, and a gray accent (`rgb(119 119 119)` ≈ `#777777`) for secondary nav elements. Sticky/scroll behavior is not observed.

**product-card** is a proposed pattern for the travel-gear catalog grid, using a white surface, hairline border, and title-md typography; card shadow/elevation was not present in supplied evidence and is intentionally omitted.

**hero** maps to the dark teal full-bleed background (`#1e3d48`) found in one banner rule, paired with white display type — consistent with the `.product-highlight__title` white-on-dark styling supplied. Overlay treatments are proposed.

**footer** is inferred (no footer-specific selectors were supplied) and reuses the navy secondary color for a grounded, trustworthy close to the page, with light body text.

**badge** directly reflects `.product-highlight__badge`: pill-shaped, orange background, dark-gray text, uppercase caption typography with letter-spacing — used for merchandising callouts like "Bestseller" or feature flags.

**search** uses the `--search-bg-color: #e6e6e6` variable from the header block for a light input affordance distinct from the pure-white canvas.

**review-rating** is the category-appropriate component: it packages the Judge.me review-widget tokens (navy primary, light track `#dfe3e2`, gold stars `#efbf04`/`#ffc617`) into a rating/testimonial block appropriate for a gear brand that leans on customer trust signals.

## Responsive Behavior

This is a recommended layout strategy, not measured site behavior — no responsive breakpoints or mobile DOM were present in the supplied evidence.

| Breakpoint | Range | Layout guidance |
|---|---|---|
| Mobile | < 768px | Single-column stacking; nav collapses to a hamburger/off-canvas menu; hero and product-highlight sections stack text above/below media |
| Tablet | 768px–1024px | 2-column product grid; nav remains condensed with wrap-friendly search |
| Desktop | > 1024px | 3–4 column product grid; full horizontal nav; hero content in a two-column split |

Touch targets should be at least 44×44px for buttons and nav items. Search and filter controls should collapse into an icon-triggered overlay below tablet width. All figures above are proposed defaults for a Shopify-style storefront, not extracted measurements.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- All CSS was gathered via static extraction; no rendered DOM, computed styles, or live viewport screenshots were available, so no layout, spacing, or interaction claims are verified observations.
- Semantic color roles (e.g., treating `#1e3d48` as a hero background, `#304362` as a "secondary/footer" color) are inferred from limited selector context and may not reflect actual site-wide usage.
- Several palette entries (e.g., `#12a713`, `#a89cc8`, `#c1e6e6`, `#f9a825`, `#1773b0`) had no accompanying selector context and were intentionally excluded from the token set to avoid unfounded role assignment.
- Typography pairing (Playfair Display for display type, Nunito Sans/Maven Pro for body/UI) is inferred from the available font-family list; no heading selectors confirmed which family is actually applied to `h1`–`h3` elements.
- Font sizes marked "proposed" (display-xl, title-md, button-md size, caption context beyond the badge) were not present in the supplied CSS and are design defaults only.
- The `rounded` and most `spacing` scales are proposed conventions; only the button's 6px radius and badge's 20px radius were directly observed and approximated into the nearest scale steps.
- Mobile navigation, menu collapse behavior, and touch interactions were not observed and are described only as recommendations.
- Availability, hosting, and licensing of Montserrat, Nunito Sans, Maven Pro, and Playfair Display on this specific storefront were not verified beyond their appearance in the supplied font-family list.
