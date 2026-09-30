---
version: alpha
name: "The Farmer__ Dog"
source_url: "https://thefarmersdog.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The double underscore in "The Farmer__ Dog" is the brand's first rhetorical move — two characters functioning as a deliberate gap, separating this product from every conventional pet-food shelf before a single ingredient is described. Forest green (#3d6b52) dominates the entire primary surface system: subscription CTAs, wizard step-progress indicators, trust-badge borders, nav hover states, and active form focus rings. Against it, a warm cream canvas (#fdf8f0) distances the brand from clinical veterinary whites and the saturated blues of big-box pet retail — the background reads like unbleached kraft paper, grounding the product in the farmstead register it claims. Body copy runs at modest weights in a humanist sans-serif with wide line-heights, stepping back so ingredient transparency can take the foreground; typographic quietness here is a trust signal, not a design gap. Photography shoots real dogs mid-meal — fur disheveled, expression unposed, food visibly textured — against warm neutral surfaces so the meal's actual color (orange carrots, ground beef, green peas) provides brand saturation without artificial styling. Product cards adopt an ingredient-first hierarchy: a condensed uppercase meal-plan label in {typography.label-caps} above a macro breakdown in {typography.body-sm}, with no decorative chrome between user and nutritional fact. Subscription checkout runs as a step-by-step wizard with a persistent summary rail, a UX posture that acknowledges the weight of a recurring commitment rather than compressing toward payment. Trust architecture stacks deliberately above the fold — USDA certifications, vet-portrait testimonials, a founding-narrative block — each accented with the forest green against {colors.hairline} dividers. Rounded corners hold a measured register: {rounded.md} on cards and modals, {rounded.sm} on inputs and form fields, with only CTA buttons and pill badges reaching {rounded.full}, signaling warmth without tipping into the bubbly consumer-app register the brand pointedly avoids.

colors:
  primary: "#3d6b52"
  primary-active: "#2d5441"
  primary-disabled: "#9abfad"
  primary-light: "#e8f0ec"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#717171"
  hairline: "#e0dbd3"
  hairline-soft: "#ede9e1"
  canvas: "#fdf8f0"
  surface-soft: "#f5f0e8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#c0392b"
  success: "#3d6b52"
  trust-badge-bg: "#e8f0ec"
  trust-badge-border: "#3d6b52"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: -0.6px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  label-caps:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  step-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    padding: 14px 32px
    height: 52px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 52px
    border: "2px solid {colors.primary}"
    hoverBackgroundColor: "{colors.primary-light}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    activeLinkColor: "{colors.primary}"
    logoColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    mealNameTypography: "{typography.title-sm}"
    macroTypography: "{typography.body-sm}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.primary}"
    hoverBorderColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "80px 0"
    imagePosition: right
    accentColor: "{colors.primary}"
  trust-badge:
    backgroundColor: "{colors.trust-badge-bg}"
    borderColor: "{colors.trust-badge-border}"
    textColor: "{colors.primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    border: "1px solid {colors.trust-badge-border}"
  plan-step:
    stepNumberBg: "{colors.primary-light}"
    stepNumberColor: "{colors.primary}"
    stepNumberActiveBg: "{colors.primary}"
    stepNumberActiveColor: "{colors.on-primary}"
    stepLabelTypography: "{typography.step-label}"
    stepLabelColor: "{colors.muted}"
    stepLabelActiveColor: "{colors.primary}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    connectorColor: "{colors.hairline}"
    connectorActiveColor: "{colors.primary}"
  ingredient-label:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    border: "1px solid {colors.hairline-soft}"
  subscription-rail:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    lineItemTypography: "{typography.body-sm}"
    totalTypography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    dividerColor: "{colors.hairline}"
    accentColor: "{colors.primary}"
  dog-profile-chip:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    iconSize: 20px
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    quoteTypography: "{typography.body-md}"
    attributionTypography: "{typography.caption}"
    attributionColor: "{colors.muted}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    accentColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary-light}"
    linkHoverColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "48px 0 32px"
    dividerColor: "#4a4a4a"

## Components

### Buttons
**`button-primary`** — Forest green (#3d6b52) fill with white text on a fully-rounded pill ({rounded.full}), 52px tall. The pill shape is the brand's warmth gesture: it appears on all primary subscription and meal-plan CTAs, "Get Started" flows, and checkout confirmations. Hover darkens to `primary-active` (#2d5441); disabled state uses the washed-out `primary-disabled` (#9abfad), preserving the pill shape so layout does not shift.

**`button-secondary`** — Transparent fill with a 2px forest green border and green text, matching the pill geometry of the primary. Used for secondary paths such as "Learn More" on feature sections and "Change Plan" in account management. On hover the fill adopts `primary-light` (#e8f0ec) for a soft green wash.

**`button-ghost`** — Text-only with underline, ink-colored, no border or fill. Appears as in-flow inline actions: "Skip this step," "Remove," or "Edit" within the subscription wizard. Does not carry the pill rounding.

### Text Input
**`text-input`** — White surface on a `hairline`-bordered rectangle at {rounded.sm}, 48px tall. Focus ring switches border to `primary` green without expanding the element footprint. Placeholder text in `muted` (#717171). Used for email capture, zip-code entry in the meal-plan quiz, and account fields.

### Navigation
**`nav-bar`** — Cream canvas (#fdf8f0) background, 72px tall, with a `hairline` bottom border. Logo renders in `ink` (#313131). Nav links use {typography.nav-link} at 15px/500 weight; active or hovered links shift to `primary` green without an underline, relying on color alone to signal state. A primary CTA button ("Get Started") sits in the right rail with the standard pill geometry.

### Product Card
**`product-card`** — White surface, 1px `hairline` border, {rounded.md} corners. The meal-plan name renders in {typography.title-sm} bold, preceded by a {typography.label-caps} category label (e.g., "BEEF RECIPE") in `primary` green. Macro breakdown (protein, fat, calories) runs in {typography.body-sm} with a subtle `hairline-soft` separator. Hover state upgrades the border to `primary` green to signal selectability without shadow or lift.

### Hero Banner
**`hero-banner`** — Cream canvas background with headline in {typography.display-xl} at 52px/600 weight. Body copy in {typography.body-md} at 1.65 line-height for maximum readability. Photography panels the right half on desktop; on mobile the image stacks above the copy block. The CTA button sits directly below the body copy with 24px of breathing room.

### Trust Badge
**`trust-badge`** — Small forest green-bordered chip at {rounded.xs} with `primary-light` fill and {typography.label-caps} text in `primary`. Used inline for "Vet-Developed," "USDA Certified," and "Human-Grade" marks. Clusters of badges appear below hero CTAs and in product card footers.

### Plan Step Indicator
**`plan-step`** — Numbered step circles track through the meal-plan quiz wizard. Inactive steps show the step number in `primary` on a `primary-light` fill circle; the active step inverts to white-on-`primary`. A `hairline`-colored connector line between circles turns `primary` as steps complete. Step label copy uses {typography.step-label} uppercase at 13px; active label color is `primary`, inactive is `muted`.

### Ingredient Label
**`ingredient-label`** — A `surface-soft` inset block at {rounded.sm} used inside product detail drawers to display ingredient lists and nutritional guarantees. The category header uses {typography.label-caps} in `muted`; ingredient text runs in {typography.body-sm} in `body` color. A 1px `hairline-soft` border separates label from surrounding content.

### Subscription Summary Rail
**`subscription-rail`** — Sticky sidebar card on checkout and plan-configuration screens. `surface-soft` background, 1px `hairline` border, {rounded.md}. Title in {typography.title-md}; line items (meal, quantity, frequency) in {typography.body-sm}; a `hairline` rule above the total row, which renders in {typography.title-sm} bold. Edit actions appear as ghost-style inline links in `primary` green.

### Dog Profile Chip
**`dog-profile-chip`** — A small `primary-light` pill ({rounded.full}) with {typography.label-caps} text in `primary`. Displays the dog's name and a 20px avatar icon in the account header and plan summary. Multiple dogs render as a scrollable chip row.

### Testimonial Card
**`testimonial-card`** — White surface, 1px `hairline` border, {rounded.md}, {spacing.lg} padding. Quote text in {typography.body-md} italic; vet or customer attribution in {typography.caption} `muted`. A `primary`-colored quotation mark glyph or 3px left accent border anchors the card visually.

### Footer
**`footer`** — Dark `ink` (#313131) fill for a strong content-end marker. All body text in `on-dark` white at {typography.body-sm}; links render in `primary-light` (#e8f0ec) — the same mint that appears as badge fills — so they remain legible against dark without switching to a foreign accent. Legal/copyright copy uses {typography.caption} at `muted` gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero image stacks above headline; product cards scroll horizontally in a snap carousel; subscription rail collapses into a bottom-anchored sticky drawer; nav condenses to logo + hamburger + CTA pill |
| Tablet | 744–1128px | Two-column grid for product cards; hero shifts to 50/50 image-copy split; subscription rail pins as a sidebar at 320px width; nav expands to show top-level links with hamburger for secondary |
| Desktop | 1128–1440px | Three-column product card grid; hero headline scales to display-xl 52px; trust badges render inline horizontal row below CTA; full nav with all links and CTA button visible |
| Wide | > 1440px | Max content width capped at 1280px with auto horizontal margins; hero padding increases to 96px vertical; section spacing expands to 80px |

### Touch Targets
- All CTA buttons maintain 52px height, meeting the 44px minimum on mobile without modification
- Nav hamburger button targets 44×44px minimum tap area with invisible padding
- Plan step circles scale to 40px diameter on mobile (from 32px desktop) to ensure tappability
- Dog profile chips maintain 36px height minimum on mobile

### Collapsing Strategy
- The sticky subscription rail becomes a bottom sheet on mobile, toggled by a "View Plan Summary" bar pinned to the viewport bottom
- Horizontal ingredient label blocks stack vertically below 744px
- Testimonial card carousels reduce from 3-up to 1-up with swipe support on mobile
- The top nav hides secondary links (Blog, Careers) behind the hamburger on tablet and below; "Get Started" remains always visible
- Footer link columns collapse from 4-column grid to 2-column at tablet, single accordion at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color extracted (#313131, the near-black ink tone) — the site likely loads brand tokens via JavaScript or was behind anti-bot protection at extraction time; all other palette values (primary green, cream canvas, surface tints) are inferred from widely observable brand visual identity and should be verified against the live site or brand assets
- No custom font family detected; all stacks are system UI defaults (-apple-system, Helvetica Neue, Arial); The Farmer's Dog may use a licensed humanist sans-serif (possibly GT America or similar) loaded via JS or a font CDN not captured in static extraction
- Exact button corner radius unconfirmed — pill-style ({rounded.full}) is derived from brand screenshot observation, not extracted CSS
- Specific motion/animation values (wizard step transitions, hero image parallax timing) could not be extracted
- Dark mode behavior unknown; brand appears to be light-only based on the cream-canvas visual identity
- Exact spacing scale for the meal-plan quiz wizard steps not confirmed from source
