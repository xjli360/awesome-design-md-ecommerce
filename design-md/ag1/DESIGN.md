---
version: alpha
name: "AG1"
source_url: "https://ag1.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  One green scoop — that single product gesture anchors every visual decision AG1 makes. The brand's deep forest green, approximating #2A4420, is not borrowed from the wellness-category mint palette; it reads closer to a field-study olive than a pharmacy green, signaling botanical depth over clinical neutrality. Against a cream-tinged canvas (#F8F6F2) rather than a flat white, the effect stays warm and grounded even when the layout is maximally spare. CTA buttons inherit that same forest green as a full-bleed rectangle at `{rounded.sm}` radius — not the pill shape most supplement brands reach for when they want to seem approachable. The restraint signals confidence. A warm gold accent (#C49A3C) threads through award icons, "trusted by 1M+" numerals, and subscription-tier savings badges — carrying premium connotation without pharma-gold heaviness. Typography runs in a clean geometric sans-serif at weights 400 and 600; display headers sit between 48–64px at generous leading, giving science-dense copy room to breathe without academic compression. Subscription pricing cards use a `{colors.surface-card}` lift against the warm canvas with `{rounded.md}` corners, stacking value bullets in `{typography.body-sm}` with forest-green checkmark icons. Section eyebrows — small all-caps labels in `{colors.primary}` — precede every content block, acting as quiet anchors for themes like "THE SCIENCE" and "WHAT'S INSIDE" without resorting to decorative dividers. The overall system is intentionally tight: two hero colors, one accent, a cream canvas, and almost no decorative chrome. Product photography does the atmospheric work that other supplement brands outsource to gradient overlays and illustration.

colors:
  primary: "#2A4420"
  primary-active: "#1D3316"
  primary-disabled: "#A8BFA2"
  accent-gold: "#C49A3C"
  accent-gold-soft: "#EAD9A0"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#6B6B6B"
  hairline: "#E0DDD8"
  hairline-soft: "#ECEAE6"
  canvas: "#F8F6F2"
  canvas-white: "#FFFFFF"
  surface-soft: "#F0EDE7"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  error: "#C0392B"

typography:
  display-xl:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: -1px
  display-md:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.17
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.21
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-sm:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  label-sm:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  stat-display:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  price-display:
    fontFamily: "'AG1Sans', 'Graphik', 'GT America', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px

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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 52px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 52px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 52px
  text-input:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    padding: 14px 16px
    height: 52px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas-white}"
    boxShadow: "0 1px 8px rgba(0,0,0,0.08)"
  hero-section:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-lg}"
    bodyColor: "{colors.body}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
  subscription-card:
    backgroundColor: "{colors.canvas-white}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    selectedBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.label-sm}"
    badgeRounded: "{rounded.xs}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg} {spacing.xl}"
    iconColor: "{colors.accent-gold}"
    statTypography: "{typography.stat-display}"
    statColor: "{colors.ink}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.body}"
  ingredient-list-item:
    backgroundColor: "transparent"
    textTypography: "{typography.body-md}"
    textColor: "{colors.body}"
    checkColor: "{colors.primary}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"
  expert-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
    nameTypography: "{typography.title-sm}"
    nameColor: "{colors.ink}"
    credentialTypography: "{typography.caption}"
    credentialColor: "{colors.muted}"
    quoteTypography: "{typography.body-sm}"
    quoteColor: "{colors.body}"
  faq-accordion:
    backgroundColor: "transparent"
    borderBottom: "1px solid {colors.hairline}"
    questionTypography: "{typography.title-sm}"
    questionColor: "{colors.ink}"
    answerTypography: "{typography.body-md}"
    answerColor: "{colors.body}"
    iconColor: "{colors.primary}"
    padding: "{spacing.lg} 0"
  benefit-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  section-eyebrow:
    textColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    marginBottom: "{spacing.sm}"
  rating-bar:
    fillColor: "{colors.accent-gold}"
    emptyColor: "{colors.hairline}"
    height: 6px
    rounded: "{rounded.full}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "10px {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The workhorse CTA is a forest-green rectangle (`{colors.primary}`) at `{rounded.sm}`, 52px tall, with `{typography.button-md}` in `{colors.on-primary}`. It leads every subscription entry point and hero section; hover state deepens to `{colors.primary-active}` and disabled state falls back to `{colors.primary-disabled}` while keeping the same geometry. The shape deliberately avoids pill-form — squarer corners signal directness.

**`button-secondary`** — Transparent fill with a 1.5px `{colors.primary}` border, identical dimensions to the primary. Used when two parallel actions need roughly equal prominence — most commonly "Subscribe & Save" paired with "One-time purchase" on the PDP.

**`button-ghost`** — Text-only at `{colors.ink}`, no border or background. Used for nav utility links, inline "learn more" actions, and legal footer links where visual quietness is required.

**`button-gold`** — `{colors.accent-gold}` fill at the same `{rounded.sm}` geometry. Reserved for premium-tier or limited seasonal promotions; appears rarely, which preserves its signal value.

### Navigation

**`nav-bar`** — 72px sticky bar resting on `{colors.canvas}` with a subtle `{colors.hairline}` bottom border. Logo anchors left; primary category links span center; a `button-primary` "Subscribe" CTA pins right. On scroll, background upgrades to `{colors.canvas-white}` and acquires a soft shadow. On mobile (< 744px) all links collapse into a hamburger drawer; only the logo and subscribe button remain visible.

**`promo-banner`** — A full-width `{colors.primary}` strip sitting above the nav bar, approximately 40px tall, carrying short promotional copy in `{colors.on-primary}` at `{typography.body-sm}`. Includes a dismiss ×. Disappears on scroll in some page contexts.

### Product & Purchase

**`product-card`** — White `{colors.surface-card}` card at `{rounded.md}` with `{colors.hairline}` border. Product name in `{typography.title-md}`, price in `{typography.price-display}` colored `{colors.primary}`, short descriptor in `{typography.body-sm}` at `{colors.body}`. A subscription vs. one-time toggle typically lives beneath the price row.

**`subscription-card`** — Selectable pricing tier tile. Default: `{colors.hairline}` border on `{colors.canvas-white}`. Selected: 2px `{colors.primary}` border with `{colors.surface-soft}` fill. A small forest-green savings badge (`{typography.label-sm}`, `{rounded.xs}`) pins to the top-right corner. The entire tile surface is interactive, not just an embedded radio button.

### Trust & Social Proof

**`trust-badge`** — A `{colors.surface-soft}` tile at `{rounded.md}` anchored by a large number in `{typography.stat-display}` (e.g., "1,000,000+") and a short description line in `{typography.body-sm}`. Certification icons (NSF, Informed Sport) render in `{colors.accent-gold}` to distinguish them from body content.

**`expert-card`** — Card at `{rounded.lg}` with `{colors.hairline}` border for scientific advisors. Headshot image leads, name in `{typography.title-sm}`, credentials in `{typography.caption}` at `{colors.muted}`, endorsement quote in `{typography.body-sm}` at `{colors.body}`.

**`rating-bar`** — 6px thin bar for ingredient quality meters. Fill in `{colors.accent-gold}`, empty track in `{colors.hairline}`, both ends at `{rounded.full}`. Often appears inside ingredient detail cards.

### Content

**`hero-section`** — Full-viewport section on `{colors.canvas}`. Headline in `{typography.display-xl}`, intro copy in `{typography.body-lg}`, primary CTA below. Product photography occupies the right half on desktop; stacks below copy on mobile. No decorative backgrounds or gradient overlays — white space and photography carry the weight.

**`section-eyebrow`** — All-caps `{typography.label-sm}` label in `{colors.primary}` placed above every section headline. Examples: "THE SCIENCE", "WHAT'S INSIDE", "DAILY RITUAL". Acts as a structural anchor replacing decorative dividers.

**`ingredient-list-item`** — Flat row separated by `{colors.hairline-soft}` hairlines, `{spacing.md}` vertical padding. Ingredient name in `{typography.body-md}`, green checkmark in `{colors.primary}` at left, brief annotation at right in `{typography.body-sm}` at `{colors.muted}`.

**`benefit-pill`** — Compact `{rounded.full}` chip in `{colors.surface-soft}` with `{colors.primary}` text at `{typography.label-sm}`. Tags nutrient benefits — "Immune", "Energy", "Gut" — in ingredient and comparison tables.

**`faq-accordion`** — Question in `{typography.title-sm}`, answer in `{typography.body-md}` at `{colors.body}`. Expand/collapse toggle is a `{colors.primary}` plus/minus icon at row right. Rows separated by `{colors.hairline}` bottom borders. No surrounding card chrome — sits directly on the page canvas.

**`text-input`** — 52px, `{rounded.sm}`, `{colors.hairline}` border at rest, `{colors.primary}` 2px border on focus. Appears in email capture flows, quiz entry fields, and the checkout address form.

**`footer`** — `{colors.ink}` background, four link columns (Product, Science, About, Help) with `{typography.label-sm}` column headings and `{typography.body-sm}` links in `{colors.on-dark}`. Legal copy and certification badges run in a sub-row at the bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero copy stacks above product image; nav collapses to hamburger drawer; trust-badge grid becomes 2-up; subscription-cards stack vertically; promo-banner wraps to two lines |
| Tablet | 744–1128px | Two-column hero (copy left, image right); trust-badge row 3-up; nav shows primary links, hides secondary; product-cards in 2-column grid |
| Desktop | 1128–1440px | Full nav with all links and subscribe CTA; hero splits ~50/50; trust-badges row 4-up; ingredient list expands to two columns; expert-cards 3-up |
| Wide | > 1440px | Max-width container ~1280px centered; hero image scales proportionally; section vertical padding steps up to `{spacing.section}` × 1.5; no further column changes |

### Touch Targets
- All buttons minimum 52px height, exceeding the 44px WCAG AA minimum
- Nav hamburger icon: 44×44px tap area with generous invisible padding
- FAQ accordion rows: minimum 56px tap height
- Subscription card: entire tile surface is tappable, no inner button required
- Ingredient list rows: 48px minimum height with `{spacing.base}` horizontal side padding
- Benefit pills: minimum 36px height, 44px effective with surrounding whitespace

### Collapsing Strategy
- Nav: full link row → hamburger slide-in drawer with stacked links, green CTA at bottom
- Hero: 50/50 split → stacked (headline + copy + CTA on top, image below)
- Subscription tier cards: horizontal radio row → vertical stacked tiles
- Trust badge row: 4-up inline → 2×2 grid → single-column
- Expert advisor grid: 3-up → 2-up → single-column scrollable
- Footer: 4-column → 2-column → single-column with collapsible accordion sections on mobile
- Promo banner: single line → wraps gracefully; dismiss button remains accessible at 44px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex color values are brand-knowledge estimates** — the live site returned zero extracted colors. AG1's forest-green primary, cream canvas, and gold accent are widely visible in brand photography and materials, but exact values (#2A4420, #C49A3C, #F8F6F2) are approximations and must be confirmed against the live stylesheet or design tokens.
- **Typography family unconfirmed** — no font stacks were extracted. AG1 appears to use a premium geometric sans-serif, possibly a custom face or a licensed Graphik/GT America variant. The stack references 'AG1Sans' as a placeholder; verify family name, weights, and any variable-font axes via browser DevTools.
- **Custom icon set** — AG1 uses bespoke forest-green checkmark icons and category pictograms throughout; no SVG sprite or icon font was captured in extraction.
- **Motion and animation tokens** — the homepage uses scroll-triggered reveals and video-backed hero sections on some page variants; no easing curves, durations, or transition tokens could be extracted.
- **Dark mode** — unclear whether AG1 supports a dark theme; the color system above assumes light-only. No `prefers-color-scheme` handling was observed.
- **Exact border-radius values** — rounded corner values are estimates. AG1 appears to use low-to-moderate radii on cards and zero radius on full-bleed sections, but pixel-exact values need stylesheet confirmation.
- **Subscription flow UI** — the in-cart and checkout experience may introduce additional surface colors, progress indicators, and form patterns not documented here.
