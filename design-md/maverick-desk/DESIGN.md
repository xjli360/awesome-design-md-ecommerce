---
version: alpha
name: "Maverick Desk"
source_url: "https://www.maverickdesk.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Where most standing-desk brands default to Scandinavian birch and silver-aluminum composure, Maverick Desk stakes its identity on a darker, more grounded register — a palette built around near-black frames, raw-steel tones, and a single warm copper accent (#C4842D) that names itself in every CTA, badge, and active state. Product photography leans into shadow rather than away from it: lit from above rather than blown out, so grain and weld lines read as features rather than imperfections. Corners are sharper here than in the ergonomic-wellness segment ({rounded.xs} on most interactive elements, {rounded.none} on structural panels), signaling an industrial character that trusts the product's physicality over interface softness. The canvas flips between pure white for product-detail pages — where leg-geometry and surface dimensions need clinical clarity — and a near-black hero ground (#1A1A1A) where lifestyle photography can breathe against a void. Type runs in a geometric sans-serif (stack unconfirmed; font not extracted), set at modest weight on body copy but stepped to 700 on display lines where dimensions, load-ratings, and configurator headings need authority. Spacing is generous in the section rhythm ({spacing.section} at 64px, {spacing.xxl} at 48px between grid rows) and tight at the component level — a contrast that emphasizes the desk as a substantial object in a considered space rather than a consumer gadget surrounded by padding. The configurator, the brand's primary interaction surface, uses compact chip selectors and inline dimension labels rather than dropdown selects, keeping the user in a physical mindset: width × depth × height, not "option A or option B." Availability badges — SHIPS FREE, IN STOCK, SHIPS IN 5 DAYS — appear in small-caps at caption size with copper accent borders, carrying urgency without hysteria.

colors:
  primary: "#C4842D"
  primary-active: "#A36820"
  primary-disabled: "#E3C08A"
  ink: "#111111"
  body: "#3D3D3D"
  muted: "#787878"
  muted-soft: "#A8A8A8"
  hairline: "#D8D8D8"
  hairline-soft: "#EBEBEB"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F4"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A1A"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  steel: "#4A5568"
  steel-light: "#718096"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1px
  display-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  dimension-label:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  spec-value:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  button-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  logo-display:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 0px
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.logo-display}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.logo-display}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageBorderRadius: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    ctaGap: "{spacing.sm}"
  hero-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  configurator-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1.5px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    minWidth: 80px
    selectedBorder: "2px solid {colors.primary}"
    selectedBackgroundColor: "{colors.surface-soft}"
  configurator-dimension-row:
    labelTypography: "{typography.dimension-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.ink}"
    rowPadding: 12px 16px
    rowBorder: "1px solid {colors.hairline-soft}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    checkColor: "{colors.primary}"
  badge-availability:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-promo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    strikePriceTypography: "{typography.body-md}"
    strikePriceColor: "{colors.muted}"
    savingsTypography: "{typography.caption}"
    savingsColor: "{colors.primary}"
  section-header:
    headingTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    mutedColor: "{colors.muted}"
    paddingBottom: "{spacing.xl}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    border: none
  trust-badge:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    iconColor: "{colors.steel}"
    typography: "{typography.caption}"
    iconSize: 24px
    gap: "{spacing.sm}"
    layout: icon-above-label
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    mutedColor: "{colors.muted-soft}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — The copper-amber fill (#C4842D) at {rounded.xs} corners gives the primary CTA a machined-toggle quality rather than a web-app softness. Hover darkens to {colors.primary-active}; disabled washes to {colors.primary-disabled} while preserving the rectangular silhouette. Locked at 48px height for desktop touch targets, full-width at mobile breakpoints.

**`button-secondary`** — Outlined in {colors.ink} at 1.5px, white-filled, geometrically identical to `button-primary`. Used for secondary actions in the configurator ("Compare Models," "Download Spec Sheet") and as the right-side CTA in hero sections. Active state shifts fill to {colors.surface-soft} to signal press without copper drama.

**`button-ghost`** — Transparent background, {colors.primary} text, no border. Reserved for inline text-level actions: "See full specs," "View all finishes," "Learn more." Typeset at {typography.button-sm} to distinguish visually from body-copy links.

**`button-dark`** — Near-black fill ({colors.surface-dark}), white text, same geometry as `button-primary`. Deployed inside hero sections and dark feature strips where the copper primary would compete with photography; the inverted relationship makes the CTA readable without color conflict.

### Inputs

**`text-input`** — Square-shouldered ({rounded.xs}), 48px tall, 1px {colors.hairline} border at rest, stepping to 1.5px {colors.ink} on focus. Label sits above as a static {typography.caption} line; no floating label. Placeholder clears on type. Used for email capture, contact forms, and the configurator's custom-dimension entry field.

### Navigation

**`nav-bar`** — 64px tall on a white canvas ground, separated from page content by a 1px {colors.hairline} border-bottom. Logo renders as uppercase tracked letterforms at {typography.logo-display} rather than an SVG lockup — the brand trusts its name over a graphic mark. Nav links at {typography.nav-link} weight 500, not bolded. A `nav-bar-dark` variant ({colors.surface-dark} ground, {colors.on-dark} text) covers use above full-bleed dark hero sections; the logo letterforms invert to white.

### Product Cards

**`product-card`** — Image sits flush with no border-radius ({rounded.none}); the card container carries a hairline border and {rounded.xs}. Title at {typography.title-sm}, price at {typography.price-display}. Availability badge positions below price inside the card footprint — a typographic signal rather than a graphic stamp on the image. At desktop, cards arrange in a 3-column grid; at tablet, 2-column; at mobile, single-column full-width.

### Hero

**`hero-dark`** — Full-bleed near-black ground ({colors.surface-dark}) with photography composited behind a subtle dark scrim. Heading at {typography.display-xl} in {colors.on-dark}; subhead at {typography.body-md}. CTA row places `button-primary` left and `button-secondary` (outlined in white rather than ink, adapting the component) right with {spacing.sm} gap. Minimum height 560px; vertical padding at {spacing.section}.

**`hero-light`** — White-ground variant for mid-page feature callouts covering motor specs, cable management, and material callouts. Heading at {typography.display-md}, copy left-aligned, product image right-aligned in a 50/50 grid column. At mobile the image stacks below copy.

### Configurator

**`configurator-chip`** — Square-shouldered ({rounded.xs}) selector chip for finish names, width presets, and height ranges. Unselected: {colors.hairline} border, white fill. Selected: 2px {colors.primary} border, {colors.surface-soft} fill. Minimum width 80px; chips arrange in a flex-wrap row. The sharp geometry maintains industrial character; a fully pill-shaped chip would read too playful for the product category.

**`configurator-dimension-row`** — Two-column compact row showing spec label left ({typography.dimension-label}, {colors.muted}) and live value right ({typography.spec-value}, {colors.ink}). Bottom-bordered in {colors.hairline-soft}. Accumulates below the chip selectors to surface the running configuration summary: "Surface Width: 60 in," "Frame Height Range: 25.5–51 in." This keeps spatial dimensions front-of-mind through the configuration flow.

### Specifications

**`spec-table`** — Two-column table in a {colors.surface-soft} container, {rounded.xs}. Left column: {typography.caption}/{colors.muted} for labels. Right column: {typography.spec-value}/{colors.ink} for values. Rows separated by {colors.hairline-soft} borders. Used below the fold on PDP for full technical specs — weight capacity, motor type, warranty, certification marks.

**`comparison-table`** — Multi-column model-vs-model table. Header row in {colors.surface-soft}, checkmarks in {colors.primary}, container bordered in {colors.hairline} at {rounded.xs}. Column headers at {typography.title-sm}, cells at {typography.body-sm}. On mobile this component is hidden and replaced by a per-model accordion.

### Badges

**`badge-availability`** — Small-caps ({typography.badge}, 0.8px letter-spacing) in {colors.surface-soft} with 1px {colors.primary} border. Reads "IN STOCK," "SHIPS IN 5 DAYS," "MADE TO ORDER." {rounded.xs}, padding 4px 10px. Appears below price in product cards and in the sticky add-to-cart rail on PDP.

**`badge-promo`** — Same typographic treatment as `badge-availability` but copper fill ({colors.primary}) and white text. Carries sale callouts ("SAVE $200," "BUNDLE DEAL"). Positioned top-left on card image at desktop; moves below title on mobile.

### Pricing

**`price-block`** — Three-line stacked arrangement on PDP: current price at {typography.price-display}/{colors.ink} on top, strikethrough original at {typography.body-md}/{colors.muted} below, savings line at {typography.caption}/{colors.primary} at the base. Condenses to a single line in the product-card grid view.

### Social Proof

**`testimonial-card`** — {colors.surface-soft} fill, no visible border, {rounded.sm}. Body at {typography.body-md}, attribution at {typography.caption}/{colors.muted}. No quotation-mark graphic; copy runs unadorned. Three-column uniform-height row at desktop; single-column at mobile. Suitable for pairing with a workspace photography thumbnail to the left at tablet width.

### Trust Signals

**`trust-badge`** — 24px icon in {colors.steel} stacked above a short label at {typography.caption}. Topics: "10-Year Warranty," "Free Shipping," "Made in USA," "30-Day Trial." Four-column row across the PDP above the fold; collapses to 2×2 grid at mobile.

### Footer

**`footer`** — Full-width {colors.surface-dark} ground, {colors.on-dark} text, {spacing.section} padding. Four-column link layout with {typography.title-sm} column headings. Logo mark top-left as white reversed letterforms. Newsletter capture row at the base: `text-input` inline with a white-outlined secondary button (border: 1.5px solid {colors.on-dark}). Collapses to single-column accordion at mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero heading drops to {typography.display-md}; configurator chips wrap to 2-column grid; nav collapses to hamburger drawer; spec-table scrolls horizontally; comparison-table hidden and replaced by per-model accordion; trust badges in 2×2 grid; hero CTAs stack vertically, full-width |
| Tablet | 744–1128px | 2-column product grid; configurator chips in 3-column wrap; nav shows primary links, overflow in hamburger; hero heading at {typography.display-lg}; trust badges maintain 4-column row; comparison-table visible |
| Desktop | 1128–1440px | 3-column product grid; full horizontal nav; configurator panel fixed as right-rail on PDP; hero at full {typography.display-xl}; comparison-table fully expanded |
| Wide | > 1440px | Content max-width 1440px with auto side-margins; hero photography extends full bleed beyond content boundary; no layout structure changes |

### Touch Targets

- All buttons minimum 48px height
- Configurator chips minimum 44px height on mobile
- Nav hamburger icon 44×44px touch area
- Footer accordion section headers 48px tall
- Badge components are display-only; adjacent CTAs carry the tap target
- Product card entire surface is tappable, not just the title link

### Collapsing Strategy

- Navigation collapses from full horizontal to hamburger icon at < 1024px; drawer slides in from the right over a dark scrim, {colors.canvas} background, full-height
- Configurator options panel transitions from sticky right-rail to a bottom-sheet drawer at < 744px; drawer persists above the viewport fold with a drag handle
- Spec table uses horizontal scroll within a constrained container at mobile rather than reflowing to a stacked card layout — preserving column alignment for scan-reading
- Footer link columns collapse to individual accordion sections at < 744px; the newsletter row pins to the bottom of the accordion stack
- Comparison table replaces with a per-model detail accordion at < 744px, each row expandable to its full spec list

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (JS-loaded design tokens or anti-bot protection blocked scraping); all color values are inferred from brand-name character and desk-market positioning — treat as alpha estimates requiring visual QA against the real site
- No font families were detected; typography stack defaults to DM Sans / Inter / system-ui as a geometric sans-serif approximation; verify actual typeface via browser DevTools on the live site
- No theme-color meta tag was found; primary brand color (#C4842D) is a reasoned inference from the "Maverick" name and industrial-workspace positioning, not a confirmed brand asset
- Exact corner-radius treatment not confirmed; {rounded.xs} (4px) chosen for industrial character — may be {rounded.none} (0px) throughout if the brand uses fully sharp geometry
- Configurator interaction pattern (chip selector vs. dropdown vs. swatch grid, live-preview vs. submit-to-update) not confirmed from extraction; inferred from premium desk category convention
- Logo format (wordmark, SVG glyph, or type-only lockup) not confirmed; specified as uppercase tracked type as a plausible default
- Mobile navigation pattern (hamburger drawer vs. bottom tab bar) not confirmed; hamburger assumed based on category norms for a content-heavy desk brand
- Whether a sticky add-to-cart rail exists on PDP, and its exact contents, could not be verified without live site access
