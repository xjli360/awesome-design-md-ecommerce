---
version: alpha
name: "Frank Darling"
source_url: "https://www.frankdarling.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Where engagement ring brands reflexively reach for warm gold and blush rose, Frank Darling built its entire visual identity around deep indigo (#1c1794) — a saturated, almost violet blue that belongs to design studios and editorial magazines rather than jewelry cases. The choice reads as a positioning statement: this is custom work, designed collaboratively, for people who know what they want and want it done differently. The editorial type pairing sharpens that signal. Louize Display trial, a contemporary serif with the warm proportions of a 20th-century book typeface, handles every headline and display moment; AkzidenzGroteskBQ-Reg — the ur-grotesque, unchanged since 1896 — runs all UI chrome: labels, navigation, buttons, captions. Together they read like a well-designed art book rather than an e-commerce template. Light sky blue (#96dbfa) surfaces as a secondary accent used for selection halos and focus rings, carrying a freshness that leavens the indigo's gravity without breaking the cool palette logic. The neutral ground is architectural: charcoal (#373737) for headings, a cool mid-gray (#6b7280) for secondary text, warm silver (#d6d5d0) for hairlines, and a near-white (#f7f7f7) canvas that keeps ring photography as the only warm thing on screen. Corner radii are restrained — `{rounded.none}` on primary buttons, `{rounded.xs}` on cards and inputs — with `{rounded.full}` reserved exclusively for filter pills and quiz option chips where selection-state switching benefits from a clearly pill-shaped affordance. The net effect is a brand that trusts its customer: direct, non-precious in its interface despite selling precious things, and designed to make a custom ring design feel like a conversation with a very smart friend.

colors:
  primary: "#1c1794"
  primary-active: "#15126e"
  primary-disabled: "#9b99d4"
  primary-hover: "#231faa"
  accent-sky: "#96dbfa"
  accent-sky-medium: "#57c5f7"
  ink: "#373737"
  body: "#444444"
  muted: "#6b7280"
  muted-soft: "#9b9b9b"
  hairline: "#d6d5d0"
  hairline-soft: "#e9e9e9"
  hairline-lighter: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-mid: "#eeeeee"
  on-primary: "#ffffff"
  overlay-scrim: "#32373c"

typography:
  display-xl:
    fontFamily: "'Louize Display trial', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Louize Display trial', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Louize Display trial', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.21
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Louize Display trial', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'AkzidenzGroteskBQ-Reg', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'AkzidenzGroteskBQ-Reg', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0.6px
    textTransform: uppercase
  body-md:
    fontFamily: "'AkzidenzGroteskBQ-Reg', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.62
    letterSpacing: 0
  body-sm:
    fontFamily: "'AkzidenzGroteskBQ-Reg', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'AkzidenzGroteskBQ-Reg', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'AkzidenzGroteskBQ-Reg', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'AkzidenzGroteskBQ-Reg', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'AkzidenzGroteskBQ-Reg', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "'AkzidenzGroteskBQ-Reg', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label-sm:
    fontFamily: "'AkzidenzGroteskBQ-Reg', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.36
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 0
    borderBottom: "1px solid {colors.ink}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
    borderWidth: 1px
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    outlineWidth: 2px
    outlineColor: "{colors.accent-sky}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    chevronColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "1/1"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.muted}"
    ctaGap: "{spacing.lg}"
  quiz-option-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    selectedBorderColor: "{colors.primary}"
  ring-builder-step:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline-soft}"
    stepLabelTypography: "{typography.title-sm}"
    stepLabelColor: "{colors.muted}"
    activeStepLabelColor: "{colors.primary}"
    contentTypography: "{typography.body-md}"
  stone-detail-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  consultation-cta-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.section}"
  swatch-selector:
    size: 28px
    rounded: "{rounded.full}"
    borderWidth: 2px
    activeBorderColor: "{colors.primary}"
    inactiveBorderColor: transparent
    gap: "{spacing.sm}"
  price-display:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    mutedTypography: "{typography.body-sm}"
    mutedColor: "{colors.muted}"
  section-label:
    typography: "{typography.title-sm}"
    textColor: "{colors.muted-soft}"
    marginBottom: "{spacing.md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.hairline-soft}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-primary}"
    paddingVertical: "{spacing.section}"

## Components

### Buttons
**`button-primary`** — The primary CTA fills with deep indigo (#1c1794), white text set in AkzidenzGroteskBQ-Reg at 14px with 1.2px letter-spacing and uppercase transform, zero border-radius — a deliberate right angle against the over-softened edges of competing wedding-market brands. Hover shifts fill to `{colors.primary-hover}` (#231faa); active presses to `{colors.primary-active}` (#15126e); disabled fades to a muted lavender `{colors.primary-disabled}`.

**`button-secondary`** — White background with a 1px indigo border and indigo text. The same uppercase grotesque type and zero radius keeps the pair visually paired on white canvas sections. Used for "See all settings" and "Compare stones" type secondary actions.

**`button-ghost`** — Text-only with a 1px bottom underline in ink, no background or border box. Carries no button silhouette, reads as a deliberate typographic link — used for editorial flows like "Learn about our process" where soft persuasion is preferred over a hard CTA.

**`filter-pill`** / **`filter-pill-active`** — The only components using `{rounded.full}`. At rest: hairline-outlined chips with `{typography.label-sm}` uppercase text in muted gray. Selected: background fills to primary indigo, text turns white. The sharp-to-pill contrast means ring style and metal filters register as a clearly interactive layer even against a near-white page.

### Inputs
**`text-input`** — Canvas background, 1px hairline border, 4px radius (`{rounded.xs}`), 48px height. On focus the border promotes to indigo `{colors.primary}` and a 2px outline in sky blue `{colors.accent-sky}` appears — the only place the sky blue accent is load-bearing in the UI, making focus states unmistakable without using a heavy color.

**`select-input`** — Identical dimensions and treatment to `text-input`; native or custom chevron inherits `{colors.muted}`.

### Navigation
**`nav-bar`** — 72px tall, white background, 1px bottom border in `{colors.hairline-soft}`. All links use `{typography.nav-link}` (13px uppercase, 0.8px tracking) in ink; active or hovered links shift to indigo. No underline or background fill on hover — the color shift alone is the affordance. Logo sits left; main nav items center or right depending on viewport; account and cart icons anchor the far right.

### Product Cards
**`product-card`** — Sits on `{colors.surface-soft}` (#f7f7f7), 4px radius, 1:1 image aspect ratio. Title in `{typography.body-sm}`, price in `{typography.price}` (18px), a metal or category label in `{typography.caption}` muted gray below. No drop shadow — light-gray card on near-white page separation is sufficient and keeps scan clean. Hover may lift image slightly via CSS transform, no card outline change.

### Ring Builder & Design Quiz
**`quiz-option-chip`** — Full pill (`{rounded.full}`) with a 1px hairline border at rest; selection fills with primary indigo and turns text white. These chips handle style choices (solitaire, halo, vintage), metal choices (platinum, 14k gold, rose gold), and stone shapes across the custom design consultation flow. Their pill shape visually distinguishes them from rectangular card selectors.

**`ring-builder-step`** — Each configuration step is a white panel divided by a top `{colors.hairline-soft}` border. The step label uses `{typography.title-sm}` in `{colors.muted}` at rest and promotes to `{colors.primary}` indigo when active. Content inside each step uses `{typography.body-md}`. No accordion chrome or animated collapse — the stepped pattern scrolls naturally on desktop, accordion-collapses on mobile.

### Badges & Labels
**`stone-detail-badge`** — Small rectangular chip in `{colors.surface-soft}`, `{typography.label-sm}`, 4px radius. Surfaces concise stone metadata (cut grade, carat, clarity, origin) inside ring detail views without crowding the layout. Multiple badges run in a horizontal flex row.

**`section-label`** — Reusable typographic motif: `{typography.title-sm}` uppercase in `{colors.muted-soft}`, with `{spacing.md}` bottom margin. Runs as a running header across product grid sections, comparison tables, and editorial content blocks — the single most repeated typographic pattern on the site.

### Editorial & Marketing
**`hero-section`** — White canvas, large Louize Display headline at `{typography.display-xl}` (56px, weight 400), subtitle in `{typography.body-md}`, CTA button(s) below with `{spacing.lg}` gap. Photography-led hero variants layer the headline over a dark-treated ring image; the serif at light weight reads clearly over dark photography without requiring a text scrim.

**`consultation-cta-banner`** — Full-bleed indigo panel (`{colors.primary}`), white text. Headline in `{typography.display-md}` (Louize Display at 28px), body copy in `{typography.body-md}`. Used for "Book a consultation" and "Start designing" conversion moments at section breaks — the only section of the page where indigo is the background rather than an accent.

**`swatch-selector`** — 28px circles with a 2px active border in `{colors.primary}`. No text label unless hovered; an adjacent or tooltip label carries the metal name. Gap between swatches is `{spacing.sm}`. Platinum and white gold swatches use the hairline gray tones; yellow and rose gold will introduce the only warm tones on the page.

### Footer
**`footer`** — Dark charcoal (#373737) background in a 4-column grid. Section headings in `{typography.title-sm}` white (`{colors.on-primary}`), links in `{typography.body-sm}` hairline-soft gray. Newsletter signup uses an inverted text-input variant (dark background). No rounded corners anywhere in the footer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces inline links, drawer slides from left over `{colors.overlay-scrim}` scrim; hero headline drops to `{typography.display-md}`; ring builder steps stack full-width; filter pills scroll horizontally in a single row |
| Tablet | 744–1128px | Two-column product grid; nav retains inline links at reduced spacing; hero can run side-by-side text + image split; consultation banner reduces padding to `{spacing.xl}` vertical |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all dropdowns visible; hero headline at full `{typography.display-xl}`; ring builder may run two-column (options panel left, ring preview right) |
| Wide | > 1440px | Grid max-width caps at ~1400px with auto side margins; hero photography can bleed full viewport width behind a contained text column |

### Touch Targets
- Minimum 44×44px for all interactive elements on mobile
- Filter pills scale to 40px height on mobile from 36px desktop
- Swatch circles scale to 36px on touch to meet minimum tap target
- Navigation drawer links: 52px minimum row height
- Stone detail badges are display-only and do not need tap target sizing

### Collapsing Strategy
- Primary nav collapses to hamburger at < 744px; drawer slides from left, `{colors.overlay-scrim}` scrim dims content behind it
- Product filter panel collapses from a persistent sidebar on desktop to a bottom sheet or modal on mobile
- Ring builder step flow reflows to a full-width accordion with expand/collapse per step on mobile
- Footer collapses to single-column stacked sections with chevron-toggle accordion on mobile
- Consultation CTA banner reduces to single-column centered text and stacked CTA on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one weight of Akzidenz Grotesk was detected (`AkzidenzGroteskBQ-Reg`); the brand likely also loads Bold and/or Light variants for typographic hierarchy — confirm weight range from loaded font files or brand style guide
- Louize Display trial is a trial-license font; production usage may differ (licensed full version or a substitute) — verify the production font name
- No explicit hover or animation duration values were extracted; transition timing (likely 150–200ms ease) should be confirmed from source
- Several extracted colors (#cf2e2e, #fcb900, #00d084, #9b51e0, #ff6900, #0693e3, #fcb900) are WordPress/Gutenberg block editor palette defaults injected by the Shopify/WP stack — excluded as non-brand tokens
- Specific box-shadow values for product cards, modals, and dropdown menus could not be extracted
- Ring detail photography color treatment (warm-toned vs. neutral/cool) not determinable from palette extraction alone; photography art direction may introduce warmth the UI palette deliberately withholds
- Custom SVG icon set for ring style, cut shape, and metal type selectors not captured — likely exists as a bespoke library
- Exact grid gutter widths and max-width container breakpoints were not confirmed from extraction
