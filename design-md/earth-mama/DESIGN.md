---
version: alpha
name: "Earth Mama"
source_url: "https://earthmamaorganics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The palette tells you what Earth Mama sells before the copy does. Deep forest sage (#40524a) anchors the brand — a green so dark it reads almost mineral rather than leafy — while the action system lives in a bright teal (#009d85) that signals the clean, modern face of the organic category. Below those two keystones, a full nursery of soft hues opens up: peachy sand (#dccec2), newborn blush (#f8d9e0), and meadow haze (#c0d8a5) serve product-line labels and ingredient callouts, with a straw-yellow (#ffec86) reserved for certification stamps and promotional flags. The canvas is a barely-warm off-white (#efecec) rather than pure paper white — it quiets the eye and keeps the page from reading as clinical or pharmaceutical. Shape language is consistently soft: product cards settle at `{rounded.lg}`, buttons and badge chips run to `{rounded.full}` pill forms, and there are no hard-cornered rectangles used for interactive elements. The metaphor is intentional — every corner radius reinforces the brand's "safe, gentle, natural" positioning without stating it explicitly. Spacing is generous; section gaps give ingredient photography and lifestyle imagery room to land rather than stacking products at the tight cadence of a mass-market shelf. Certifications — USDA Organic, EWG Verified, NSF — are first-class visual objects, not fine-print footnotes; they appear as distinct badge tokens in straw-yellow and meadow-green and repeat across the page as trust anchors. The overall system avoids cool neutrals entirely: even mid-tone values — #7f9c90 (muted sage) and #cdd8d3 (soft sage-gray) — tilt green rather than blue or stone, keeping every screen in the same earthy, sun-warmed register that the brand's name promises.

colors:
  primary: "#009d85"
  primary-active: "#4c8477"
  primary-disabled: "#cdd8d3"
  forest: "#40524a"
  forest-muted: "#7f9c90"
  ink: "#121212"
  body: "#3b3d3f"
  muted: "#7f9c90"
  hairline: "#dedede"
  hairline-soft: "#efecec"
  canvas: "#efecec"
  canvas-white: "#ffffff"
  surface-soft: "#e6f9f7"
  surface-card: "#ffffff"
  surface-sage: "#cdd8d3"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  blush: "#f8d9e0"
  sand: "#dccec2"
  meadow: "#c0d8a5"
  yellow-flag: "#ffec86"
  cyan-accent: "#54ebfc"
  steel: "#57728b"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  certification-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
  full: 9999px

spacing:
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.forest}"
    border: "2px solid {colors.forest}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.md}"
    padding: 12px 16px
    typography: "{typography.body-md}"
    focusBorderColor: "{colors.primary}"
    focusOutlineColor: "{colors.surface-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.forest}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.forest}"
  announcement-bar:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
    badgeBackgroundColor: "{colors.meadow}"
    badgeTextColor: "{colors.forest}"
    badgeTypography: "{typography.badge}"
    badgeRounded: "{rounded.full}"
    promoFlagBackgroundColor: "{colors.yellow-flag}"
    promoFlagTextColor: "{colors.forest}"
    promoFlagRounded: "{rounded.xs}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.forest}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    imageFit: cover
    ctaSpacingTop: "{spacing.lg}"
  category-badge:
    backgroundColor: "{colors.meadow}"
    textColor: "{colors.forest}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  certification-badge:
    backgroundColor: "{colors.yellow-flag}"
    textColor: "{colors.forest}"
    typography: "{typography.certification-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  organic-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.forest}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    borderLeft: "4px solid {colors.primary}"
    bodyTypography: "{typography.body-sm}"
  ingredient-tag:
    backgroundColor: "{colors.surface-sage}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  promo-flag:
    backgroundColor: "{colors.yellow-flag}"
    textColor: "{colors.forest}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  swatch-selector:
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: 32px
    selectedOutlineWidth: 2px
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.forest}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    padding: "{spacing.lg} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-sage}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — A fully pill-shaped (`{rounded.full}`) button filled with brand teal (#009d85), carrying white text at `{typography.button-md}` (weight 600, 0.5px letter-spacing). On hover, the fill deepens to forest-muted (#4c8477), reading as a natural shade shift rather than an abrupt corporate darken. The disabled state uses sage-gray (#cdd8d3) fill with white text, maintaining the pill geometry while removing visual urgency; it never goes gray-on-gray. At 48px tall it clears mobile touch targets on the first attempt.

**`button-secondary`** — Same pill geometry as primary but white fill with a 2px forest-green (#40524a) border. Used for "Learn More," secondary PDP actions, and modal cancel paths where the primary CTA is already present. The forest border keeps the button firmly in the earthy palette rather than floating as a neutral outline.

**`button-ghost`** — Transparent background with primary teal (#009d85) text, no border. Used for inline text-level actions like "See all ingredients," "Read more," and navigation-drawer close. Sits flush with surrounding copy without drawing a box-shaped frame around the action.

### Text Input

**`text-input`** — White fill with a 1px #dedede border at `{rounded.md}` (12px) — just soft enough to feel approachable without the full pill. Focus state swaps the border to primary teal (#009d85) and adds a soft mint halo from `{colors.surface-soft}`. Placeholder text in `{colors.muted}` (#7f9c90); filled body copy in `{colors.ink}` (#121212). The moderate corner radius deliberately stops short of pill so the input reads as a data field rather than a button.

### Navigation

**`nav-bar`** — White bar at 72px tall with a hairline (#dedede) bottom border. Logo and nav links render in forest green (#40524a) rather than black, pulling every element into the same natural-goods family. Sub-navigation opens as a mega-menu panel with category badges (`{colors.meadow}` chips) grouping items by life stage: Pregnancy, Baby, Birth. A separate `announcement-bar` component sits above the nav in solid forest (#40524a) with white caption-scale text for shipping thresholds and seasonal promotions; it disappears on scroll past a set threshold.

### Product Card

**`product-card`** — White surface at `{rounded.lg}` (20px) with a `{rounded.md}` (12px) cropped product image. Title in `{typography.title-sm}` weight 600; price in `{typography.body-md}` in `{colors.ink}`. Organic category badges run as pill chips in meadow green (#c0d8a5) with forest text. Straw-yellow (#ffec86) promo flags sit at the card's top-left corner as a `{rounded.xs}` stamp. Add-to-cart access appears on hover at desktop via a teal ghost layer; on mobile a persistent cart icon occupies the card bottom-right.

### Hero

**`hero`** — The warm off-white canvas (#efecec) grounds the hero with forest-green (#40524a) headline text at `{typography.display-xl}`. At desktop the layout is a 50/50 split: text block left, full-bleed lifestyle photography right. The primary CTA button sits one `{spacing.lg}` below the subhead with no competing secondary action in the hero zone itself. On mobile the image collapses above the text as a full-width aspect-ratio-fixed block before giving way to the headline, body, and button stacked vertically.

### Category Badge & Certification Badge

**`category-badge`** — Meadow-green (#c0d8a5) pill with forest text in `{typography.badge}` uppercase. Marks product-line affiliation (Pregnancy, Baby, Birth) and appears on cards, category headers, and filter chips. **`certification-badge`** — Straw-yellow (#ffec86) pill with forest text in `{typography.certification-label}`; carries USDA Organic, EWG Verified, and NSF marks. The two badge types never share the same row without visual separation, preserving their distinct functional registers.

### Organic Callout

**`organic-callout`** — A mint-surface (#e6f9f7) block at `{rounded.lg}` with a 4px left-rule in primary teal (#009d85). Used for key ingredient callouts, "free from" claim lists, and substantiation blocks adjacent to product descriptions. Body copy in `{typography.body-sm}` in `{colors.forest}`. The left-rule treatment signals editorial authority without invoking an alert or error visual language.

### Ingredient Tag

**`ingredient-tag`** — A sage-gray (#cdd8d3) pill in `{typography.caption}` with body-charcoal text. Appears in ingredient panels and "made with" modules to enumerate individual botanicals at low visual weight. Multiple tags flow horizontally and wrap; they carry no interactive state, functioning purely as taxonomic labels.

### Promo Flag

**`promo-flag`** — A small `{rounded.xs}` stamp in straw-yellow (#ffec86) with forest text at badge scale. Applied to sale percentage labels and "NEW" product callouts within product cards and category grids. Kept small and text-only — no icon — so it reads as a factual stamp rather than a marketing shout.

### Trust Strip

**`trust-strip`** — A mint-surface (#e6f9f7) band pinned below the hero with caption-scale copy and teal (#009d85) icon marks. Lists organic certifications, carbon-offset claims, free-of lists, and safety standards in a horizontal row at desktop; collapses to a 2-column grid at tablet and a single stacked column at mobile. The top hairline border (#dedede) cleanly separates the trust strip from the hero without a hard color shift.

### Footer

**`footer`** — Deep forest (#40524a) fill with white body copy and sage-gray (#cdd8d3) link text. Column headings in `{typography.title-sm}` weight 600 in white. Four columns at desktop: Shop, Learn, Company, and a newsletter signup with a `{rounded.full}` email input and primary teal submit button. The footer functions as a second-opinion trust layer — certification logos, "B Corp" mark, and recycling information run in a sub-footer band at smaller type.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero image full-bleed above stacked text; nav collapses to hamburger + centered logo; announcement bar truncates to essential message; footer accordion-collapsed by section |
| Tablet | 744–1128px | 2-column product grid; hero splits to 50/50 text + image; nav shows top-level categories, sub-nav in slide-out drawer; trust strip wraps to 2-row grid |
| Desktop | 1128–1440px | 3–4 column product grid; full nav with mega-menu dropdowns; hero at constrained content width with generous side padding; footer 4-column grid |
| Wide | > 1440px | Content max-width locked at ~1280px with auto side margins; layout unchanged, whitespace grows symmetrically |

### Touch Targets
- All primary and secondary buttons minimum 48px tall; pill geometry ensures comfortable lateral tap width at any label length
- Navigation links minimum 44px touch zone via vertical padding extension beyond visible text bounds
- Product card entire surface is tappable to the PDP; add-to-cart and wishlist targets are separated by at minimum `{spacing.base}` to prevent fat-finger misfires
- Swatch selectors 32px visible diameter with 8px invisible padding ring to reach a 48px tap target
- Badge chips are display-only and not tappable; filter chips that are interactive receive the same 44px minimum height rule

### Collapsing Strategy
- Navigation: mega-menu panel → hamburger drawer with accordion sub-categories per life-stage group
- Product grid: 4-col → 3-col → 2-col → 1-col at breakpoints 1440 / 1128 / 744 / 0
- Footer: 4-col grid → 2-col grid → single-column accordion with expand/collapse per section heading
- Hero: side-by-side (50/50) → stacked (image, then headline, body, CTA)
- Certification badge strip in trust section: horizontal scroll row → 2×2 grid → 4-row stack

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stacks were extractable from the live site; the crawler returned only the CSS property string `object-fit: contain` rather than any `font-family` declarations. Actual brand typefaces are unknown — system-ui fallback stacks are used throughout all typography tokens.
- Meta theme-color was not set; mobile chrome bar tint and PWA splash-screen color cannot be confirmed from extraction.
- Precise button and card corner radii could not be pixel-measured; `{rounded.full}` (pill) for interactive elements and `{rounded.lg}` (20px) for cards are inferred from the brand's visual aesthetic, not extracted values.
- The cyan accent (#54ebfc) and steel blue (#57728b) appear in the extracted palette but their exact usage context — whether illustrations, icon fills, a specific product line, or seasonal campaign elements — could not be confirmed.
- Dark-mode behavior is unknown; no `prefers-color-scheme` alternate stylesheet or meta was detected.
- Font weights, sizes, and line-heights for display and body typography are estimated; pixel-accurate values require a design-token export or manual DevTools inspection session.
- Exact navigation bar height (reported as 72px here) and announcement bar height are estimated; live measurement may differ.
