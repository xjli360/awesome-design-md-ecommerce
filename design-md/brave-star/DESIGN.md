---
version: alpha
name: "Brave Star"
source_url: "https://bravestarselvedge.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Where most denim brands signal authenticity through distressing and marketing language, Brave Star Selvedge earns it through restraint — a dark, near-inkwell primary of deep raw-denim navy (~`#1e2b3e`) sits against natural, unbleached canvas (`#f8f4ee`), the same two-tone contrast built into every pair of jeans before they are ever washed or worn. The palette refuses ornament: a warm amber gold borrowed from brass hardware and leather patches (`#b5813a`) is the only accent that breaks the monochrome, and a selvedge-line rust (`#8b3a2a`) surfaces only on badge and tag elements — the chromatic equivalent of the red ID stripe on the outseam. Display type runs in a condensed heritage serif, uppercase and widely tracked, evoking workwear stencils and 1940s garment labels more than contemporary e-commerce. Body copy drops to a quiet, readable text weight that never competes with the product photography. Buttons carry sharp `{rounded.none}` corners — zero softening anywhere — because the brand sells fabric that is meant to crease, pucker, and age, not smooth over. Product cards are structured like garment spec sheets: fabric weight and selvedge origin stated as plainly as the price. Navigation is sparse, almost austere, with a wordmark in the same condensed serif as the display scale. The spacing system favors breathing room in section breaks but tightens inside component layouts, echoing the density of a folded bolt of 14-oz denim. There is no illustration, no gradient, no hero animation — only precise photography of raw fabric grain and copper rivets against the brand's two anchoring neutrals.

colors:
  primary: "#1e2b3e"
  primary-active: "#111a27"
  primary-disabled: "#7a8fa6"
  accent-amber: "#b5813a"
  accent-amber-active: "#8f6020"
  accent-rust: "#8b3a2a"
  ink: "#141414"
  body: "#2e2e2e"
  muted: "#6b6b6b"
  hairline: "#d4cfc7"
  canvas: "#f8f4ee"
  surface-soft: "#f0ece4"
  surface-card: "#faf8f5"
  on-primary: "#f8f4ee"
  on-amber: "#ffffff"
  badge-bg: "#8b3a2a"
  badge-text: "#f8f4ee"

typography:
  display-xl:
    fontFamily: "'Freight Display Pro', 'Playfair Display', Georgia, serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: 0.06em
    textTransform: uppercase
  display-md:
    fontFamily: "'Freight Display Pro', 'Playfair Display', Georgia, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.04em
    textTransform: uppercase
  display-sm:
    fontFamily: "'Freight Display Pro', 'Playfair Display', Georgia, serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.05em
    textTransform: uppercase
  title-md:
    fontFamily: "'Freight Text Pro', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Freight Text Pro', Georgia, serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.03em
    textTransform: uppercase
  body-md:
    fontFamily: "'Freight Text Pro', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Freight Text Pro', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Freight Text Pro', Georgia, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.04em
  spec-label:
    fontFamily: "'Freight Text Pro', Georgia, serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.10em
    textTransform: uppercase
  button-md:
    fontFamily: "'Freight Display Pro', 'Playfair Display', Georgia, serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Freight Display Pro', 'Playfair Display', Georgia, serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Freight Display Pro', 'Playfair Display', Georgia, serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  price:
    fontFamily: "'Freight Text Pro', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.01em
  price-sm:
    fontFamily: "'Freight Text Pro', Georgia, serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.none}"
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-amber}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
  nav-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBorder: "none"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-sm}"
    specTypography: "{typography.spec-label}"
    specColor: "{colors.muted}"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
  product-spec-sheet:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    padding: "{spacing.lg}"
    divider: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-sm}"
    subheadColor: "{colors.accent-amber}"
    ctaButton: "{components.button-amber}"
    minHeight: 600px
    textAlign: left
    paddingH: "{spacing.xxl}"
  hero-natural:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 520px
    textAlign: center
  selvedge-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  made-in-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  fabric-origin-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    subTextTypography: "{typography.caption}"
    subTextColor: "{colors.primary-disabled}"
    height: 40px
    paddingH: "{spacing.base}"
  section-divider:
    color: "{colors.hairline}"
    style: solid
    weight: 1px
    marginV: "{spacing.section}"
  category-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    captionTypography: "{typography.body-sm}"
    captionColor: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.section}"
    borderBottom: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.nav-link}"
    linkColor: "{colors.on-primary}"
    mutedColor: "{colors.primary-disabled}"
    captionTypography: "{typography.caption}"
    divider: "1px solid rgba(248,244,238,0.15)"
    paddingV: "{spacing.xxl}"
  announcement-bar:
    backgroundColor: "{colors.accent-rust}"
    textColor: "{colors.badge-text}"
    typography: "{typography.spec-label}"
    height: 36px
  swatch-selector:
    borderActive: "2px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    size: 32px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderActive: "2px solid {colors.primary}"
    height: 44px
    width: 56px

## Components

### Buttons

**`button-primary`** — Full-width dark navy (`{colors.primary}`) fill with cream text (`{colors.on-primary}`) and absolutely no radius — `{rounded.none}` across all corners. Uppercase tracked condensed serif at `{typography.button-md}` (12em letter-spacing). Active state deepens to `{colors.primary-active}`; disabled drains to the muted `{colors.primary-disabled}` tint. The sharp geometry signals that this is a working garment brand, not a lifestyle boutique.

**`button-secondary`** — Transparent fill with a 2px `{colors.primary}` border, same uppercase type scale as primary. Used for secondary purchase actions (size guide, notify me) where the CTA hierarchy needs a clear step down without disappearing against the canvas.

**`button-amber`** — Reserved for hero-level CTAs overlaid on the dark primary hero surface; `{colors.accent-amber}` fill reads as warm brass hardware against the dark navy, drawing the eye without the clinical brightness of a Rausch-style red. Sharp `{rounded.none}` corners match the rest of the system.

### Text Input

**`text-input`** — Square-cornered `{rounded.none}`, 1px `{colors.hairline}` border at rest that snaps to `{colors.primary}` on focus. Placeholder text in `{colors.muted}`. No fill change on focus — the border shift alone carries the state signal, consistent with the brand's preference for minimal visual noise.

### Navigation

**`nav-bar`** — 64px tall, natural canvas `{colors.canvas}` background with a bottom hairline `{colors.hairline}`. Wordmark in `{typography.display-sm}` condensed serif uppercase; nav links in `{typography.nav-link}` with 0.12em tracking. A `nav-bar-dark` variant (`{colors.primary}` fill, cream text) applies on category pages and the PDP where the hero image bleeds to the viewport edge.

### Product Card

**`product-card`** — No rounded corners, no drop shadow. Image occupies the full card width; below it, fabric origin and weight appear in `{typography.spec-label}` muted text before the product name and price, inverting the usual e-commerce hierarchy to lead with material credentials. A `{components.selvedge-badge}` or `{components.made-in-badge}` overlays the image corner when applicable.

### Product Spec Sheet

**`product-spec-sheet`** — A warm `{colors.surface-soft}` panel on the PDP listing fabric weight (oz), selvedge origin, construction details, and fit specs as labeled rows. Labels in `{typography.spec-label}` muted; values in `{typography.body-sm}` body. Horizontal dividers in `{colors.hairline}`. Reads as a garment hang-tag transcribed to screen.

### Hero

**`hero`** (dark) — Primary navy `{colors.primary}` background, headline in `{typography.display-xl}` uppercase condensed serif in `{colors.on-primary}`, subhead accent line in `{colors.accent-amber}` at `{typography.title-sm}`. CTA uses `{components.button-amber}` to maintain contrast hierarchy on the dark field. Left-aligned text block, photography occupying the right half on desktop. Minimum 600px height.

**`hero-natural`** — Canvas `{colors.canvas}` version for secondary landing sections; centered text, headline in `{typography.display-xl}` ink, no amber accent. Used on brand story and fabric education pages.

### Badges

**`selvedge-badge`** — Rust-red `{colors.badge-bg}` fill, cream text, `{typography.spec-label}` uppercase, zero radius. Signals that the garment uses a true selvedge edge; appears on product cards and the PDP image gallery as a flag overlay.

**`made-in-badge`** — Same geometry in `{colors.primary}` navy. Used for domestic manufacture callouts. The two badge colors together (rust and navy) echo the selvedge ID stripe running down the outseam of the jeans themselves.

### Fabric Origin Bar

**`fabric-origin-bar`** — A 40px-tall full-width dark navy strip between the hero and the product grid, carrying concise origin copy ("Cone Mills White Oak Selvedge — Greensboro, NC") in `{typography.spec-label}`. Functions as a provenance certificate more than a marketing banner.

### Announcement Bar

**`announcement-bar`** — 36px rust-red `{colors.accent-rust}` strip at the very top of the viewport. Uppercase spec-label type, cream text. Reserved for shipping thresholds, restock alerts, and limited-run notifications — used sparingly so it retains signal value.

### Footer

**`footer`** — Full `{colors.primary}` navy field. Nav links in `{typography.nav-link}` cream uppercase; section headings in the same scale. Legal copy and copyright in `{typography.caption}` at `{colors.primary-disabled}`. Horizontal rule between columns at 15% white opacity rather than a solid line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero becomes full-width stacked (image above, text below); spec sheet rows stack label over value; announcement bar truncates to one line |
| Tablet | 744–1128px | Two-column product grid; hero splits 50/50 image/text; nav links condense to 4 top-level items; fabric origin bar wraps to two lines if needed |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero image occupies 55% viewport width; spec sheet displays in two-column label/value layout |
| Wide | > 1440px | Four-column product grid; hero max-width constrained to 1440px; section padding scales to `{spacing.section}` lateral gutters; product card images scale up to maintain visual weight |

### Touch Targets

- All buttons minimum 48px height, matching `{spacing.xxl}` tap area on mobile
- Size selector tiles 44px height, 56px width with generous tap margin
- Swatch selectors minimum 32px × 32px, spaced at `{spacing.sm}` gap
- Nav hamburger icon 44 × 44px hit area

### Collapsing Strategy

- Product grid: 4 → 3 → 2 → 1 column across breakpoints
- Navigation: full horizontal links → 4 condensed labels → hamburger drawer
- Hero: side-by-side split → stacked (image first, text below) on mobile
- Fabric origin bar: hidden on mobile below 375px width; single-line truncation with ellipsis on 375–744px
- Spec sheet: two-column label/value → single-column stacked at mobile
- Footer column grid: 4 → 2 → 1 column

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — all palette values above are estimated from documented brand photography, product imagery, and common selvedge denim aesthetic conventions; must be verified against the live site or brand style guide
- No font families were extracted — typography system uses Freight Display Pro / Freight Text Pro as informed estimates from the brand's editorial voice; actual typefaces should be confirmed by inspecting loaded font files or CSS `@font-face` declarations
- Exact button radii unconfirmed — `{rounded.none}` assumed from the brand's sharp-edged, workwear aesthetic; verify against live component inspection
- No spacing scale or grid column count was extractable; values follow standard 8px base grid inference
- Dark/light nav variant logic (scroll-triggered vs. page-type-triggered) unconfirmed
- Animation and transition timing values completely absent — no motion data available
- The site does not appear to be on Shopify, so component structure may differ substantially from platform defaults; cart drawer and checkout flow tokens are unspecified
