---
version: alpha
name: "DedCool"
source_url: "https://dedcool.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Burnt orange (#ff6b18) at a fragrance brand is a provocation — the color carries heat, skin, and warmth rather than the icy glass-bottle blues the category defaults to, and DedCool leans into it as its single brand voltage against a near-black canvas of #1a172c. The tagline "Making life smell really good" arrives with deliberate bluntness: no accented letters, no French nomenclature, no botanical Latin. The pillars — GENDERLESS + VEGAN + NON TOXIC — appear in all-caps like a lab certification rather than soft-focus marketing copy, and that document register runs throughout the site. Messina Sans Mono Web, a monospace font, carries UI labels and technical callouts where other fragrance brands reach for editorial serifs; the effect reads closer to ingredient sheet than perfumery counter, entirely on purpose. Universal Sans Display 450 handles headline work — the 450 weight lands precisely between light and regular, giving displays an airy but not wispy quality that reads cleanly over bottle photography without competing. The palette splits into two emotional registers: a warm axis of burnt orange and near-black ink, and a cool axis of graduated sky blues (#cce1f5, #81c1e6, #add9f2, #d0e0f3) that suggest water, air, and ingredient transparency. Neutral surfaces (#f0f0f0, #eeeeee) stay cool-toned so the orange retains full temperature contrast whenever it fires. Corner geometry is minimal — {rounded.sm} on inputs and buttons, {rounded.xs} on classification chips — keeping the visual language flat and functional. The monospace caption system and all-caps badge language produce an identity that could cohabit with a chemistry textbook or a lifestyle editorial with equal ease, which is the exact ambiguity a genderless fragrance brand should occupy.

colors:
  primary: "#ff6b18"
  primary-active: "#d94e00"
  primary-disabled: "#ffb897"
  ink: "#1a172c"
  body: "#121212"
  muted: "#79889f"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#eeeeee"
  surface-mid: "#dcdcdc"
  on-primary: "#ffffff"
  sky-light: "#cce1f5"
  sky-mid: "#81c1e6"
  sky-pale: "#d0e0f3"

typography:
  display-xl:
    fontFamily: "'Universal Sans Display 450', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 450
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Universal Sans Display 450', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 450
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Universal Sans Display 450', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 450
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Universal Sans Display 450', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 450
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Universal Sans Display 450', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 450
    lineHeight: 1
    letterSpacing: 0.04em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Universal Sans Display 450', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 450
    lineHeight: 1
    letterSpacing: 0
  mono-label:
    fontFamily: "'Messina Sans Mono Web', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.06em
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
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "11px 23px"
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    metaTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    imagePaddingTop: "100%"
    hoverBorderColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 80vh
    textAlign: center
  scent-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
  pillar-tag:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  fragrance-note-chip:
    backgroundColor: "{colors.sky-light}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
  bundle-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    labelTypography: "{typography.mono-label}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  newsletter-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    inputBackgroundColor: "{colors.on-primary}"
    inputTextColor: "{colors.ink}"
    inputRounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    labelTypography: "{typography.mono-label}"
    headingTypography: "{typography.caption}"
    dividerColor: "{colors.muted}"

## Components

### Buttons

**`button-primary`** — Solid burnt-orange ({colors.primary}, #ff6b18) fill with reversed white text in all-caps Universal Sans Display 450 at 14px with 0.04em tracking. {rounded.sm} corners read as flat and functional rather than friendly or pill-soft. Active state darkens to {colors.primary-active} (#d94e00); disabled washes to {colors.primary-disabled} (#ffb897). Height locks at 44px to maintain comfortable touch targets across devices.

**`button-secondary`** — Transparent fill with a 1px {colors.ink} outline and matching ink text. Shares the all-caps {typography.button-md} and {rounded.sm} corner radius of the primary button, forming a matched pair at the same physical footprint. Used for secondary actions — variant selection, learn-more, back-navigation — that should not compete with the conversion CTA.

### Inputs

**`text-input`** — White canvas fill, {colors.hairline} (#dedede) border at rest that snaps to full {colors.ink} on focus. {typography.body-md} in Arial at 16px. {rounded.sm} corners stay consistent with the button language throughout the page. Placeholder runs {colors.muted} (#79889f) for gentle differentiation without disappearing.

**`search-bar`** — Recessed {colors.surface-soft} (#f0f0f0) fill with no visible border at rest — sits pressed into the canvas surface. Same 44px height and {rounded.sm} corners as the text-input. Placeholder and leading icon in {colors.muted}.

### Navigation

**`nav-bar`** — White canvas bar, 56px tall, separated from content by a 1px {colors.hairline} bottom border. Links in {typography.nav-link} (Universal Sans Display 450, 13px). The wordmark may render in {colors.primary} orange or as a mono-weight lockup; no observed mega-menu or flyout panels — flat horizontal links with hover underline only. Cart and account icons anchor the right side.

### Product Cards

**`product-card`** — {colors.surface-card} (#eeeeee) tile with {rounded.sm} corners and a square image region (padding-top: 100%) that keeps bottle photography proportional across grid widths. Title in {typography.title-md}, price in {typography.body-sm}, category or size annotation in {typography.caption}. On hover, a {colors.primary} border signal appears at the card edge rather than a fill change — the grid stays visually cool by default, with orange marking the active or hovered state only.

### Hero

**`hero`** — Deep {colors.ink} (#1a172c) base grounds the primary brand entry point. Headline in {typography.display-xl} (48px, weight 450, −0.5px tracking), sub-copy in {typography.display-sm} (22px). Min-height 80vh. The orange primary appears as a CTA button or a single typographic accent word inside the hero field, not as a background fill — the dark field carries the brand's temperature, the orange marks the action.

### Brand-Signature Components

**`scent-badge`** — Small rectangular chip in {colors.surface-soft} with a 1px {colors.hairline} border and {rounded.xs} (4px) corners. Text runs in {typography.mono-label}: Messina Sans Mono Web, 11px, all-caps, 0.06em tracking. Used to classify fragrance family (WOODY / FLORAL / CITRUS), intensity level, and ingredient callouts. The monospace font makes each label read as a classification code rather than a decorative tag, consistent with the brand's lab-register voice.

**`pillar-tag`** — Zero-fill outlined tag with a 1px {colors.ink} border and sharp {rounded.none} corners. Renders GENDERLESS / VEGAN / NON TOXIC in {typography.mono-label}. These function as brand certifications, not promotional badges — displayed on PDPs and hero sections. No fill ensures they never compete with product imagery or the orange primary.

**`fragrance-note-chip`** — Pill-shaped ({rounded.full}) chip in {colors.sky-light} (#cce1f5) for top-note, heart, and base-note callouts on PDPs. {typography.caption} (Arial, 12px). The sky-blue ground invokes air, water, and ingredient transparency — the cool axis of the palette working in counterpoint to the warm orange primary.

**`bundle-card`** — White {colors.canvas} card with a 1px {colors.hairline} border and {rounded.sm} corners. Title in {typography.title-md}; bundle count or promotional label in {typography.mono-label} to maintain the lab-register voice even in e-commerce contexts. Orange {colors.primary} appears as a savings callout or price accent, not a structural fill.

**`newsletter-strip`** — Full-bleed horizontal band in {colors.primary} (#ff6b18) — the one moment in the page layout where brand voltage fills an entire section. Headline in {typography.display-md} reversed to {colors.on-primary} white. Email input sits inline with a {colors.on-primary} white fill, {colors.ink} text, and {rounded.sm} corners, embedded directly in the orange field without a separate container.

**`footer`** — {colors.ink} (#1a172c) base with {colors.canvas} body text. Section headings in {typography.mono-label} (Messina Sans Mono Web, all-caps) maintain the laboratory voice at the bottom of every page. Navigation and policy links in {typography.body-sm}. Horizontal dividers between sections in {colors.muted} (#79889f).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with cart icon visible; hero headline scales from display-xl to display-md (32px); pillar-tags wrap to new rows; newsletter strip stacks headline above input |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links, overflow into hamburger; hero maintains display-xl but horizontal padding tightens to 24px |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav bar; hero runs edge-to-edge with centered text block and single-column copy |
| Wide | > 1440px | Content max-width ~1400px centered; hero imagery may bleed edge-to-edge while text block stays within the max-width container |

### Touch Targets

- All tappable elements (buttons, chips, nav links, card overlays) minimum 44×44px
- Fragrance note chips in PDP context pad to at least 36px height on mobile for reliable tap
- Pillar-tags gain {spacing.sm} (8px) margin between siblings to prevent mis-taps on small screens
- Cart and account icons in collapsed nav maintain 44px hit area regardless of visual icon size

### Collapsing Strategy

- Nav: full horizontal links collapse to hamburger below 744px; cart and account icons remain visible in the collapsed bar
- Product grid: 4-col → 3-col → 2-col → 1-col descending through breakpoints
- Hero: display-xl (48px) → display-md (32px) on mobile; min-height 80vh → 60vh
- Bundle cards: horizontal split (image left, text right) on desktop → fully stacked vertical on mobile
- Pillar-tags (GENDERLESS / VEGAN / NON TOXIC): inline flex row on desktop, wrapping flex on mobile with {spacing.xs} gap
- Footer columns: 4-col → 2-col → 1-col on mobile with accordion expansion per section

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No border-radius values extracted from the live site — {rounded.sm} (8px) for buttons and inputs is inferred from the flat-functional brand register
- Canvas base (#ffffff) not present in the extracted hex list — likely rendered via CSS default rather than a declared variable; assumed safe as a universal default
- Font weight fallbacks for Universal Sans Display 450 are unconfirmed — "450" is a variable-font axis value; no secondary bold/display weight (600+) was observed in extraction
- Sky-blue sub-palette (#cce1f5, #81c1e6, #add9f2, #d0e0f3) usage context is inferred from extraction frequency; specific assignment to note chips, section backgrounds, or image-tint overlays is not confirmed from live inspection
- Hover and focus animation durations not extractable — 150ms ease-in-out assumed as category norm
- No dark-mode or alternate-theme token variants observed in the extraction
- Icon set style (line vs. filled, stroke weight) not determinable from color or font scan
- No confirmed grid gutter widths, column counts, or max-width breakpoint values extracted
