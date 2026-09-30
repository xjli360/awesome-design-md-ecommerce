---
version: alpha
name: "Year & Day"
source_url: "https://yearandday.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep navy (#05154b) pressed against warm bone (#fbfaf7) — two colors from opposite ends of temperature — defines the whole visual grammar before a single product appears. Most dinnerware brands lean into terracotta or sage; Year & Day chose the palette of a high-end financial institution and softened it with cream surfaces that read like unglazed clay in digital form. The type system enforces the same productive tension: Quarto-Semibold, a display serif with old-money authority, handles all editorial headings and campaign moments, while Mark-Pro, a precise geometric sans, runs every price, label, button, and navigation item. The combination signals that this is both a premium object and a rational purchase. Buttons are flat-cornered (`{rounded.none}`) throughout — no pill shapes, no softened radii — the geometry as intentional as the plates themselves. The chip guarantee, Year & Day's core brand promise, surfaces as a first-class UI element: a navy badge with letter-spaced uppercase Mark-Pro-Bold type sitting inline with product copy rather than buried in fine print. Product photography fills square cards against `{colors.surface-soft}`, a blush-warm cream (#f9f2ec) that makes white porcelain appear to glow without artificial lightening. The footer and announcement bar mirror `{colors.primary}`, creating a deep-color envelope around the warm interior canvas. The hairline border (#dedede) performs quietly — separating product grids and form fields without adding visual weight. Navigation sits at 64px with widely tracked sans-serif labels, giving the impression that each item has been placed deliberately. The overall effect is a store that behaves like an edited catalog: minimal, decisive, and convinced that the objects speak for themselves.

colors:
  primary: "#05154b"
  primary-active: "#13183b"
  primary-disabled: "#8a91b0"
  ink: "#121212"
  body: "#121212"
  muted: "#6b6b6b"
  hairline: "#dedede"
  canvas: "#fbfaf7"
  surface-soft: "#f9f2ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Quarto-Semibold', Georgia, serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Quarto-Semibold', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Quarto-Semibold', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Mark-Pro-Bold', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Mark-Pro-Bold', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  body-md:
    fontFamily: "'Mark-Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Mark-Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Mark-Pro', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  price:
    fontFamily: "'Mark-Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Mark-Pro-Bold', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Mark-Pro-Bold', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Mark-Pro', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.8px
  label-sm:
    fontFamily: "'Mark-Pro-Bold', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "1/1"
    rounded: "{rounded.none}"
    gap: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  hero-full-bleed:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 600px
    padding: "{spacing.section} {spacing.xl}"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  chip-guarantee-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  swatch-selector:
    borderColor: "{colors.hairline}"
    borderColorSelected: "{colors.primary}"
    borderWidthSelected: 2px
    rounded: "{rounded.full}"
    size: 24px
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 40px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Full-width navy rectangle with uppercase, letter-spaced Mark-Pro-Bold at 14px and 48px height. Active state deepens to `{colors.primary-active}`; disabled state washes to `{colors.primary-disabled}` without altering geometry. No border-radius anywhere in the button family — the hard corner is as deliberate as the plates' own edges.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` border and matching uppercase type, allowing the background surface to show through. Used for secondary CTAs on PDPs and modals where the primary action already commands attention.

**`button-ghost`** — Borderless, zero-padding, ink-colored text styled as a button using `{typography.button-md}`. Reserved for low-hierarchy actions like "See Details" or "Learn More" placed inline in editorial rows; it reads as a link that behaves like a button.

### Text Input
**`text-input`** — Sharp-cornered, 48px tall, `{colors.canvas}` background with a `{colors.hairline}` border that tightens to `{colors.primary}` on focus. Placeholder text renders in `{colors.muted}` at body weight. The form fields share the same zero-radius geometry as the buttons, keeping the entire interactive layer visually consistent.

### Navigation
**`nav-bar`** — 64px tall with `{colors.canvas}` background and a single hairline-weight bottom border. Labels are 13px Mark-Pro with 0.8px tracking, widely spaced for a deliberate, editorial feel. On dark hero sections the `nav-bar-dark` variant swaps the canvas for `{colors.primary}` and all labels to `{colors.on-primary}` without changing height or typographic scale; the wordmark inverts accordingly.

### Product Card
**`product-card`** — Square imagery on `{colors.surface-soft}` with no border-radius and no card border. Product name renders in `{typography.title-sm}`, price in `{typography.price}` directly below with no visual separator. Cards are grid-separated by gap rather than hairlines, letting ceramic shapes read as objects resting in space rather than items in a list.

### Hero Sections
**`hero-full-bleed`** — Deep navy field with `{colors.on-primary}` text; paired with a Quarto-Semibold display heading at `{typography.display-xl}` and a single `button-primary` inverted against the navy. Minimum 600px tall with `{spacing.section}` vertical padding. Used for campaign launches and seasonal promotions.

**`hero-editorial`** — Warm blush-cream background (`{colors.surface-soft}`) for lifestyle photography rows and brand-story sections. Text runs in `{colors.ink}` with Quarto-Semibold headings at `{typography.display-md}`, giving these sections a warmer and less promotional register than the full-bleed navy hero.

### Chip Guarantee Badge
**`chip-guarantee-badge`** — Navy rectangular tag with 1.2px-tracked uppercase `{typography.label-sm}` type, zero border-radius. Displayed as an inline element on PDPs and collection cards, never as a tooltip or modal trigger. The flat, stamp-like form treats the guarantee as a product attribute rather than a marketing footnote.

### Promotional Banner
**`promo-banner`** — A single-line announcement strip pinned above the nav on every page: `{colors.primary}` background, white `{typography.caption}` centered text. Used for free-shipping thresholds, seasonal discount codes, and the chip guarantee callout. Height is content-driven, typically 36–40px; it compresses gracefully on mobile without wrapping.

### Swatch Selector
**`swatch-selector`** — 24px circular swatches with a 1px `{colors.hairline}` border at rest; selected state gains a 2px `{colors.primary}` ring with no fill change on the outer container. The `{rounded.full}` shape is the only instance of full rounding in the design system, reserved exclusively for color-selection affordances to prevent visual confusion with buttons.

### Footer
**`footer`** — Full-width `{colors.primary}` block mirroring the promo banner and primary button, bookending the warm cream body. Column headers use `{typography.title-sm}`, link text uses `{typography.body-sm}` in white. The `{spacing.section}` vertical padding gives the footer comfortable breathing room and reinforces the catalog-spread feeling of the overall layout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart icon; hero min-height reduces to 360px; section padding drops from `{spacing.section}` to `{spacing.xxl}`; display headings scale from `{typography.display-xl}` to `{typography.display-sm}` |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level items without mega-menu dropdowns; hero switches from full-bleed to 90vw centered block; display headings at `{typography.display-md}` |
| Desktop | 1128–1440px | 3–4 column product grid; full nav with mega-menu flyouts; hero full-bleed at 600px minimum; all display headings at `{typography.display-xl}` |
| Wide | > 1440px | Content max-width ~1440px centered; hero imagery scales to fill viewport width; product grid holds at 4 columns; footer columns spread to maximum readable measure |

### Touch Targets
- All buttons minimum 48px height per component spec
- Swatch selectors expand touch target to 40×40px with invisible padding around the 24px visual element
- Nav icons (cart, account, hamburger) minimum 44×44px tap target
- Quantity stepper buttons are 40px tall with at least 40px wide per increment control
- Promo banner links expand vertical tap area to 44px minimum on mobile

### Collapsing Strategy
- Primary nav collapses into a left-side drawer at <744px; drawer slides over canvas at 80vw width with a `{colors.primary}` overlay scrim
- Product grid: 4-col → 3-col at 1280px → 2-col at 744px → 1-col at 480px
- Hero copy scales: `{typography.display-xl}` (56px) → `{typography.display-md}` (36px) at tablet → `{typography.display-sm}` (28px) at mobile
- Footer columns: 4-col → 2-col at 744px → single-column accordion stack at mobile
- Promo banner: single line at all breakpoints; truncates with ellipsis before wrapping; font-size holds at `{typography.caption}` throughout

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit border-radius values were extractable from the live site; zero-radius (`{rounded.none}`) is assumed from brand aesthetic conventions — verify against Shopify theme CSS on PDPs and collection pages
- `surface-card` set to #ffffff; only two warm-cream variants (#fbfaf7, #f9f2ec) were confirmed from extraction; actual card and modal backgrounds should be cross-checked against theme source files
- `muted` (#6b6b6b) was not present in the extracted palette and was inferred for placeholder and secondary text — extract from computed CSS custom properties to confirm
- `primary-disabled` (#8a91b0) was derived as a desaturated navy tint with no direct site extraction available
- Hover and focus state transitions (timing, easing) are not recoverable from hex/font scanning; assume 150–200ms ease on color transitions unless overridden
- Mega-menu structure, flyout geometry, and dropdown overlay scrim colors are unconfirmed
- Mark-Pro and Quarto-Semibold are commercial fonts; weight variants beyond Mark-Pro (regular/bold) and Quarto (semibold) — e.g., Mark-Pro-Medium or Quarto-Bold — are unconfirmed from extraction
- No confirmed icon set or icon style (stroke weight, fill vs. outline) was identifiable from the extraction hints
