---
version: alpha
name: "Mila"
source_url: "https://milacares.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The #1ce4d5 teal names a clean-air default, but Mila's real design invention is using color as product naming: each filter personality — Critter Cuddler, The Overreactor, Basic Breather, and the full roster — receives its own hex, turning the palette into a product catalog where strawberry red (#f42d53), amber gold (#ffc140), and blush pink (#f394b5) are not brand accents but filter identifiers. Every marketing surface therefore doubles as wayfinding within the product line. Graphik carries the full weight range — Regular through Black — and the brand trusts it: display headlines run Graphik-Black at 56px with -1.5px tracking, giving aspirational copy a compressed, engineered quality rather than the airy openness most wellness brands favor. The sole monospace interruption is a stack of Andale Mono / Consolas / Monaco deployed exclusively in spec tables and filter performance data, where it reads as honest measurement. Near-black hero stages (#131314, #19191a) let the teal CTAs glow as if back-lit — a photon-clean visual register borrowed from consumer electronics packaging rather than home goods. The surface vocabulary splits deliberately: dark product stages for aspiration, warm off-white (#f0ece5) for narrative prose, and a near-white (#f9f9f9) for the commerce layer. Corners settle at {rounded.md} across product UI elements and step up to {rounded.lg} on marketing cards; the only {rounded.full} shapes belong to filter-variant color badges, where a pill silhouette signals categorical identity rather than action. On-primary text runs dark (#131314 on #1ce4d5) — possible because teal's luminosity is high enough to pass WCAG AA without inverting to white — a small but conspicuous break from consumer color defaults.

colors:
  primary: "#1ce4d5"
  primary-active: "#16b7ab"
  primary-disabled: "#b0e8e4"
  accent-red: "#f42d53"
  accent-amber: "#ffc140"
  accent-pink: "#f394b5"
  ink: "#131314"
  body: "#262626"
  muted: "#565656"
  muted-soft: "#949494"
  hairline: "#e2e2e2"
  hairline-soft: "#eeeeee"
  canvas: "#f9f9f9"
  surface-soft: "#f0ece5"
  surface-warm: "#c9c3ba"
  surface-card: "#f6f6f6"
  surface-dark: "#131314"
  surface-dark-alt: "#19191a"
  on-primary: "#131314"
  on-dark: "#f9f9f9"

typography:
  display-xl:
    fontFamily: "'Graphik-Black', 'Graphik', sans-serif"
    fontSize: 56px
    fontWeight: 900
    lineHeight: 1.07
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'Graphik-Bold', 'Graphik', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Graphik-Semibold', 'Graphik', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Graphik-Semibold', 'Graphik', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Graphik-Medium', 'Graphik', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'Graphik-Regular', 'Graphik', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Graphik-Regular', 'Graphik', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Graphik-Regular', 'Graphik', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Graphik-Medium', 'Graphik', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Graphik-Medium', 'Graphik', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.15px
  nav-link:
    fontFamily: "'Graphik-Medium', 'Graphik', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Graphik-Bold', 'Graphik', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  mono-spec:
    fontFamily: "'Andale Mono', Consolas, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

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
    rounded: "{rounded.lg}"
    padding: 14px 28px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 12px 26px
    height: 52px
  button-secondary-teal:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 12px 26px
    height: 52px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 14px 28px
    height: 52px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    subtitleColor: "{colors.muted}"
    nameTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    shadow: "0 2px 16px rgba(0,0,0,0.07)"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    headlineColor: "{colors.on-dark}"
    subtitleColor: "{colors.muted-soft}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    paddingY: "{spacing.section}"
  filter-badge-performance:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  filter-badge-sleep:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  filter-badge-sensitive:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  filter-badge-clean:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  air-quality-indicator:
    backgroundColor: "{colors.surface-soft}"
    valueColor: "{colors.primary}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.display-md}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.mono-spec}"
    labelTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
  subscription-card:
    backgroundColor: "{colors.surface-soft}"
    border: "2px solid {colors.primary}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  award-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  footer:
    backgroundColor: "{colors.surface-dark-alt}"
    textColor: "{colors.muted-soft}"
    linkColor: "{colors.on-dark}"
    headingColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.surface-dark}"

## Components

### Buttons

**`button-primary`** — Teal (#1ce4d5) fill with dark ink text (#131314) at 20px rounding; the color inversion (dark-on-light rather than the usual white-on-color) is the single most visually distinctive interactive element on the site, enabled by teal's high luminosity. Active state deepens to #16b7ab; disabled fades to a desaturated teal (#b0e8e4) with muted gray text, dropping affordance without adding red-error connotation.

**`button-secondary`** — 2px dark ink border on a transparent background, height-matched to `button-primary` at 52px. Used alongside primaries on product pages and in the cart flow; shares Graphik-Medium 16px type.

**`button-secondary-teal`** — Teal-border/teal-text variant of the secondary, deployed on dark hero surfaces where a dark-border button would lose contrast against the near-black canvas.

**`button-dark`** — Near-black (#131314) fill with off-white (#f9f9f9) text; used for "Add to Cart" on light product-card surfaces and as a secondary action paired with the teal CTA inside hero banners.

### Text Input

**`text-input`** — 48px input with a 1.5px hairline border (#e2e2e2) that snaps to teal on focus. Graphik-Regular 16px on an #f9f9f9 canvas, 12px corner radius. Placeholder runs in soft gray (#949494). No floating-label animation — the placeholder clears on focus without persisting above the field.

### Navigation

**`nav-bar`** — Near-white (#f9f9f9) canvas with 1px bottom hairline, 72px tall. Graphik-Medium 15px links in near-black. A teal `button-primary` anchors the right side; on scroll a light shadow reinforces separation from page content.

**`nav-bar-dark`** — Near-black (#131314) variant used when the nav floats over full-bleed hero photography. All link text inverts to off-white (#f9f9f9); the teal CTA retains its fill.

### Product Card

**`product-card`** — White card at 20px rounding with a 7% opacity box shadow. A filter-variant badge (one of the four color-coded pills) sits at upper-left, establishing which product personality this card belongs to. Product name in Graphik-Semibold 18px, price in the same weight, description copy in Graphik-Regular 14px muted gray. Hover deepens the shadow without translating the card.

### Hero Banner

**`hero-banner`** — Full-bleed near-black (#131314) stage with Graphik-Black 56px headline at -1.5px tracking; the compression is intentional — it reads as engineered precision, not editorial looseness. Subtitle drops to Graphik-Semibold 24px in muted-soft gray (#949494). CTA is the teal primary button with dark text. Vertical section padding at 64px. Product photography renders at full opacity against the dark field with no overlay scrim.

### Filter Variant Badges

**`filter-badge-performance`** / **`filter-badge-sleep`** / **`filter-badge-sensitive`** / **`filter-badge-clean`** — Pill-shaped ({rounded.full}) labels in Graphik-Bold 11px uppercase with 0.5px tracking. Each maps to a filter personality: strawberry red (#f42d53) for performance/allergen filtration, amber (#ffc140) for sleep-mode units, blush pink (#f394b5) for sensitive or nursery environments, teal (#1ce4d5) for the baseline clean tier. These badges are the primary cross-surface color communication system — the same coding appears on PDPs, collection pages, packaging, and marketing photography.

### Air Quality Indicator

**`air-quality-indicator`** — Warm off-white (#f0ece5) tile displaying a live or simulated air quality value in large Graphik-Bold 36px teal numerals, with a Graphik-Regular 12px gray label below. Used in educational sections and real-time dashboard panels. 12px rounding keeps the tile consistent with the product UI grid.

### Spec Table

**`spec-table`** — Technical specification table using Andale Mono 13px for numeric values and Graphik-Regular 14px for row labels. Light surface (#f6f6f6) with 1px hairline row borders. The monospace departure from Graphik is deliberate: it signals that the numbers present are measurements, not marketing copy. 8px corner radius, full-width on desktop.

### Subscription Card

**`subscription-card`** — Warm off-white (#f0ece5) card with a 2px teal border accent, visually differentiating the filter-replenishment tier from standard product cards. Heading in Graphik-Semibold 18px, body in 14px gray. The teal border echo of the primary CTA color reinforces recurring-purchase framing without resorting to aggressive upsell styling.

### Award Badge

**`award-badge`** — Near-black ({colors.ink}) pill in Graphik-Bold 11px uppercase off-white text. Used sparingly to call out editorial recognition or industry awards. The dark fill distinguishes authority claims from the color-coded filter badges so the two badge types never compete for meaning.

### Footer

**`footer`** — Dark (#19191a) background with muted-soft (#949494) body text and off-white (#f9f9f9) headings and links. Graphik-Medium 16px section headings, Graphik-Regular 14px body links. 1px near-black top border. Four-column grid on desktop collapsing to a single accordion-style column on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger + logo; hero headline drops to ~32px Graphik-Black; filter badges stack below product image; spec table scrolls horizontally in a scroll container |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links only with hamburger for secondary items; hero splits 50/50 text left / product image right |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all links visible; hero at full 56px display headline with 64px vertical padding |
| Wide | > 1440px | Content max-width capped at 1440px with auto margins; product grid stays three-column with widened gutters; hero photography expands to fill the wider viewport |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target
- Filter variant badges expand to full-row tap areas on mobile product cards
- Subscription card CTA stretches to full width below 744px
- Nav hamburger button is at least 44×44px; tap area extends beyond the visible icon

### Collapsing Strategy
- Navigation: logo + hamburger icon only below 744px; full horizontal link row above
- Hero: stacked (text above image) below 744px; side-by-side split above
- Product grid: 1 column (mobile) → 2 columns (744px+) → 3 columns (1128px+)
- Spec table: wrapped in a horizontally scrollable container on mobile; full-width display above 744px
- Footer: single stacked column with section headings as collapsible toggles on mobile; four columns on desktop
- Air quality indicator tiles: full-width single tile on mobile; 2–3 per row on tablet and above

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-disabled` (#b0e8e4) is a derived approximation — no light teal found in extracted palette; actual disabled-state color may differ
- `EasyNotes` font detected in the font-family stack — likely used for handwritten or playful accent copy in hero sections; specific usage context and sizing not confirmed
- Filter personality names (Critter Cuddler, The Overreactor, Basic Breather, etc.) and the exact color-to-filter mapping are inferred from brand knowledge; extracted palette confirms the distinct accent hues but does not label them to specific SKUs
- Pure canvas white (#ffffff) was not present in the extracted colors; #f9f9f9 used as proxy and may not reflect the true page background in all sections
- `#e9eaed` appears in extracted colors but usage context is ambiguous — possibly a Shopify framework default or inactive nav element; not mapped to a token
- Dark hero gradient or image-overlay values (scrim opacity, gradient stops) are not derivable from color extraction
- Hover / active transition timing curves and durations not captured
- Icon set style (line weight, fill vs. stroke, corner radius on glyphs) not confirmed
- Mobile navigation animation (slide-in drawer vs. dropdown overlay) not confirmed
- Exact letter-spacing at display sizes is inferred from Graphik's known design conventions, not extracted from computed styles
