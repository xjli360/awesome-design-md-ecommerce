---
version: alpha
name: "AURA Hair Care"
source_url: "https://www.aurahaircare.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every shade in the AURA catalog begins as a quiz answer — a premise the visual system reflects in its warm, consultative palette of ivory canvas (#FAFAF7) and a terracotta-edged primary (#BF7B5E) that reads less like a product shelf and more like an appointment with your colorist. The brand's name, with its suggestion of diffused light and radiant proximity, manifests in a design language that favors airy whitespace, soft warm neutrals, and typography running at light weights — display text settles around weight 300–400, a deliberate softness that signals expertise without clinical detachment. Product photography occupies generous proportions, with color swatches as navigational currency: the quiz selects shades by hue family rather than SKU number, placing visual logic above catalog logic. Rounded corners appear throughout at moderate radii — form cards and input fields carry `{rounded.md}` curves while primary CTAs lean on `{rounded.full}` pills, yielding a friendly, spa-adjacent interface that avoids the hard geometry of mass-market haircare. Surface hierarchy uses warmth rather than depth: a `{colors.surface-soft}` cream separates content zones without elevation shadows, and the `{colors.brand-warm}` tint carries shade-selector backgrounds. The color journey — mixing ratio sliders, developer volume pickers, tone intensity wheels — demands clear, uncluttered input components with strong label contrast against the warm canvas; text inputs therefore run a visible `{colors.hairline}` border that firms up to `{colors.ink}` on focus. Labels throughout use spaced uppercase at 11–12px, a capsule shorthand that signals professionalism while keeping the visual register approachable. Footer and legal areas recede into `{colors.muted}` on cream rather than inverting to dark — the brand stays light-footed all the way to the bottom of the page.

colors:
  primary: "#BF7B5E"
  primary-active: "#A66548"
  primary-disabled: "#E3C2B4"
  ink: "#1A1917"
  body: "#3C3835"
  muted: "#7A736E"
  hairline: "#DDD8D3"
  hairline-soft: "#EDE8E3"
  canvas: "#FAFAF7"
  surface-soft: "#F5F0EA"
  surface-card: "#FFFFFF"
  brand-warm: "#F0E6DC"
  brand-cream: "#FAF6F1"
  on-primary: "#FFFFFF"
  success: "#4A7C59"
  error: "#C0392B"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.02em
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.01em
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-caps:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.04em
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.03em
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.01em

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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.muted}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.body}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  hero-section:
    backgroundColor: "{colors.brand-cream}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    ctaVariant: "button-primary"
  shade-swatch:
    width: 40px
    height: 40px
    rounded: "{rounded.full}"
    borderWidth: 2px
    borderColorSelected: "{colors.ink}"
    borderColorDefault: transparent
  shade-swatch-lg:
    width: 64px
    height: 64px
    rounded: "{rounded.full}"
    borderWidth: 3px
    borderColorSelected: "{colors.ink}"
    borderColorDefault: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.title-sm}"
    imageAspectRatio: "4/5"
    swatchRow:
      gap: "{spacing.xs}"
      overflow: scroll
  quiz-step-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    progressBar:
      backgroundColor: "{colors.hairline}"
      fillColor: "{colors.primary}"
      height: 3px
      rounded: "{rounded.full}"
  quiz-option-chip:
    backgroundColor: "{colors.surface-soft}"
    backgroundColor-selected: "{colors.primary}"
    textColor: "{colors.body}"
    textColor-selected: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    border: "1px solid {colors.hairline}"
    border-selected: "1px solid {colors.primary}"
  badge-recommended:
    backgroundColor: "{colors.brand-warm}"
    textColor: "{colors.primary-active}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-bestseller:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  section-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    marginBottom: "{spacing.lg}"
  accordion-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A pill-shaped CTA (`{rounded.full}`) in warm terracotta `{colors.primary}` with white text at `{typography.button-md}` (14px, weight 500, 0.04em tracking). Height is fixed at 48px with 28px horizontal padding. Active state deepens to `{colors.primary-active}`; disabled state washes out to `{colors.primary-disabled}` without dropping opacity, keeping the affordance visible but clearly inert. Used for all primary quiz progression, checkout, and shop CTAs.

**`button-secondary`** — Matching pill geometry (`{rounded.full}`) with a 1px `{colors.hairline}` border on canvas background, carrying the same 48px height. Handles "Learn More," "See All Shades," and secondary navigation actions. Active state lifts the fill to `{colors.surface-soft}` and firms the border to `{colors.muted}`. Pairs cleanly beside `button-primary` in hero and product detail sections.

**`button-text`** — Bare underlined link-style button in `{colors.body}` at `{typography.button-sm}`. No background, no border. Used inside quiz flows for "Skip" and "Back" actions where a full-weight button would compete with the primary progression CTA.

### Inputs

**`text-input`** — 48px tall, `{rounded.md}` corners, 1px `{colors.hairline}` border that snaps to a solid `{colors.ink}` ring on focus — the firmest focus state in the system, ensuring quiz and checkout forms feel precise rather than ambient. Labels render above the field in `{typography.label-caps}` (11px, 0.12em letter-spacing, uppercase), visually locking label and field as a single unit without floating-label animation complexity. Error state adds a 1px `{colors.error}` border with a `{typography.caption}` message below.

**`select-input`** — Identical geometry and border logic to `text-input`. Developer volume, shade intensity, and formula type pickers all share this component so quiz step layouts stay stable across question types. A right-aligned chevron icon indicates selectability.

### Navigation

**`nav-bar`** — 64px tall, canvas white with a soft `{colors.hairline-soft}` bottom rule. Logo sits left; primary links (Quiz, Shop, How It Works, Reviews) run center in `{typography.nav-link}` (14px/500); cart and account icons anchor right. On scroll the bottom border gains a light drop shadow rather than a background color change, preserving the white identity throughout the page.

### Hero

**`hero-section`** — Full-width block on `{colors.brand-cream}`. Headline at `{typography.display-xl}` (48px, weight 300) sits above a 2–3 line subline in `{typography.body-md}`. The CTA is always `button-primary`. Photography fills the right column at desktop in a fixed 4:5 crop; at mobile, image stacks below the text block. No scrim or overlay — copy and image live in separate grid columns so headline legibility never depends on image lightness.

### Product Cards

**`product-card`** — White surface, `{rounded.md}` corners, `{spacing.base}` internal padding. Product image is a 4:5 aspect ratio crop. Title in `{typography.title-sm}`, price in `{typography.title-sm}`, short descriptor in `{typography.body-sm}` at `{colors.muted}`. Below the image, a horizontal-scroll row of `shade-swatch` circles (40px, `{rounded.full}`) lets users preview color variants without expanding the card. Hovering or tapping a swatch updates the product image with a 200ms crossfade. `badge-bestseller` and `badge-recommended` overlay the top-right corner of the image when applicable.

### Shade Swatches

**`shade-swatch`** — 40px circle (`{rounded.full}`). Selected state adds a 2px `{colors.ink}` ring; default has no border, letting color read edge-to-edge. The larger `shade-swatch-lg` (64px, 3px selected border) appears in the quiz shade-selection step and on shade detail pages where color accuracy is the primary decision driver. Both variants carry a `title` attribute with the shade name for accessibility.

### Quiz Components

**`quiz-step-card`** — Full-viewport-width card with `{rounded.lg}` corners and a 1px `{colors.hairline-soft}` border on white surface. Headline at `{typography.display-sm}`, supporting copy at `{typography.body-md}`. A 3px `{rounded.full}` progress bar in `{colors.primary}` runs across the top of the viewport and fills left-to-right over the session. Back and Skip use `button-text`; Next/Continue uses `button-primary` right-aligned at the card bottom.

**`quiz-option-chip`** — Pill-shaped selectable chip, `{rounded.full}`. Default: `{colors.surface-soft}` fill, `{colors.hairline}` border, `{colors.body}` text at `{typography.body-sm}`. Selected: `{colors.primary}` fill, white text, matching border. Used across hair type, texture, porosity, concern, and goal questions. Chips wrap to a 2-column grid on mobile; flow as a wrapping row on desktop. Multi-select questions allow several chips to be active simultaneously.

### Badges

**`badge-recommended`** — Small `{rounded.xs}` pill in `{colors.brand-warm}` with `{colors.primary-active}` text at `{typography.label-caps}`. Appears on quiz-matched shades and featured kit bundles. Warm-on-warm keeps it present without shouting.

**`badge-bestseller`** — Inverted: `{colors.ink}` fill, `{colors.canvas}` text, same `{rounded.xs}` geometry and `{typography.label-caps}` scale as `badge-recommended`. Applied to the image corner of top-selling product cards.

### Accordion

**`accordion-item`** — No card wrapper; FAQ, ingredient, and how-to entries sit directly on canvas, separated by 1px `{colors.hairline}` rules. Headers in `{typography.title-sm}`; expanded body text in `{typography.body-sm}` at `{colors.body}`. A right-aligned chevron rotates 180° on expand with a 150ms ease transition. Used in FAQ, ingredient glossary, and application instruction sections.

### Section Labels

**`section-label`** — Uppercase `{typography.label-caps}` in `{colors.muted}` placed directly above section headlines as a category identifier ("YOUR FORMULA", "HOW IT WORKS", "SHADE FINDER"). Provides scanning rhythm without adding visual weight or requiring a rule or divider.

### Footer

**`footer`** — `{colors.surface-soft}` background; stays in the warm neutral range rather than inverting to dark. Column headers in `{typography.label-caps}`; links in `{typography.body-sm}` at `{colors.body}`. Copyright and legal text step down to `{typography.caption}` at `{colors.muted}`. No dark band at page end — the brand's airy warmth persists through the final scroll position.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks text above image; quiz chips wrap to 2-column grid; nav collapses to hamburger + logo + cart icon; product card swatch row stays horizontal-scroll; section vertical padding reduces to `{spacing.xl}` |
| Tablet | 744–1128px | 2-column product grid; hero shifts to 50/50 text-image split; nav shows up to 5 links before overflow; quiz card max-width 600px centered with auto side margins |
| Desktop | 1128–1440px | 3-column product grid; hero expands to 60/40 text-image; quiz card max-width 720px; full nav link bar; section padding expands to `{spacing.section}` |
| Wide | > 1440px | Layout constrained to 1440px max-width with auto margins; display-xl may scale up 4–8px via clamp(); 4-column product grid optional on wide editorial pages |

### Touch Targets

- All interactive controls (buttons, chips, swatches, accordion headers, nav links) minimum 44×44px
- `shade-swatch` at 40px diameter gains a transparent 4px padding wrapper on mobile to meet the 44px minimum without altering visual size
- Nav hamburger: 44×44px tap target centered around a 24px icon glyph
- Quiz option chips: minimum 44px height enforced on mobile regardless of label length via min-height override
- Footer links: minimum 36px row height with additional `padding-top` and `padding-bottom` applied on mobile

### Collapsing Strategy

- Navigation: full link bar → 5-item bar with overflow "More" dropdown → hamburger drawer at < 744px
- Product grid: 4-column (wide) → 3-column (desktop) → 2-column (tablet) → 1-column (mobile)
- Hero: 60/40 side-by-side → 50/50 → full-width stacked text-above-image on mobile
- Quiz layout: centered card with 80px side gutters → full-bleed card with `{spacing.base}` internal side padding on mobile
- Footer: 4-column link grid → 2-column → single-column accordion-style expandable sections on mobile with `{colors.hairline}` separators

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted**: The site returned zero hex values from automated extraction — likely JS-rendered design tokens or anti-bot protection on aurahaircare.com. All palette values in this file are inferred from brand-category conventions for premium hair color DTC brands and have not been verified against the live site. Manually sample hex values via browser DevTools color picker before using in production.
- **No fonts extracted**: Zero font-family stacks were returned. The system falls back to `'Helvetica Neue', Helvetica, Arial, sans-serif`. The brand may use a licensed typeface common in this category (GT America, Neue Haas Grotesk, Freight Display, or similar). Verify via DevTools → Network → Fonts tab on the live site.
- **Primary color confidence is low**: `#BF7B5E` is a plausible warm terracotta for the brand category but is not confirmed from any authoritative source. AURA is not widely enough documented for a "Tiffany blue"-style color citation.
- **Quiz UX structure unverified**: Step count, question branching, slider components, and mixing-ratio input types are inferred from category conventions and may differ substantially from the live quiz implementation.
- **Shade naming and taxonomy**: Color family groupings, shade name conventions, and swatch ordering logic on the live site are unknown and may not match the conventions used in this spec.
- **Commerce platform unknown**: The site is confirmed not on Shopify. The actual platform (custom headless, Recharge, Bold, etc.) may affect how design tokens are implemented in practice.
- **Meta theme-color absent**: Could not confirm the brand's primary color via `<meta name="theme-color">`, which is normally the single most reliable hex signal.
