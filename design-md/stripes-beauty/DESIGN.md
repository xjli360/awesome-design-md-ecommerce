---
version: alpha
name: "Stripes Beauty"
source_url: "https://www.stripesbeauty.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The warmest detail on a Stripes Beauty page is the canvas itself — #fffff3, a cream that sits one step shy of warm paper, placing every element in what reads as ambient domestic light rather than a screen's cold glow. Against this ground, the primary blue (#356687) reads not clinical but intentional: a mid-depth teal-leaning pigment borrowed from botanical illustration rather than pharmaceutical packaging, saturated enough to carry every primary CTA without suggesting an infirmary. Secondary warmth arrives in terracotta (#e08a73) and dusty peach (#eaae9d) — skin-tone adjacents that humanize a wellness category that has historically either been so clinical it chills, or so soft it patronizes.

  Rhymes Display handles all headline work: an editorial serif with enough antiquarian confidence to treat menopause as a subject worth publishing about, not just packaging around. It runs unhurried — large, at low weights, with loose-to-neutral tracking — creating a pace that feels more like a magazine feature than an e-commerce conversion funnel. Inter takes over for body copy and navigation at modest weights, keeping long explanatory passages about hormonal health readable without ornament. Franklin Gothic Cond ITC appears in eyebrow labels and ingredient tags, its compressed letterforms adding a decisive functional note beneath Rhymes Display's openness.

  Buttons use `{rounded.sm}` rather than the pill shape common in DTC wellness; the restraint signals product substance over trend-chasing. Cards sit at `{rounded.md}`, soft without being playful. Pale yellow (#ffffb6) appears as a badge and highlight accent — barely visible against the cream canvas but warm enough to register as a signal rather than decoration. The overall shape language avoids both the hard-edged geometry of pharmaceutical packaging and the rounded-corner exuberance of gummy-vitamin brands, landing at a midpoint that trusts the adult intelligence of its audience — women who want science-backed solutions delivered without condescension.

colors:
  primary: "#356687"
  primary-active: "#2a5470"
  primary-disabled: "#9abfd4"
  ink: "#141414"
  body: "#545454"
  muted: "#737373"
  muted-light: "#9b9b9b"
  hairline: "#e2e2e2"
  hairline-soft: "#eeeeee"
  canvas: "#fffff3"
  surface-soft: "#f8f8f8"
  surface-card: "#f7f8fa"
  on-primary: "#fffff3"
  terracotta: "#e08a73"
  peach: "#eaae9d"
  pale-yellow: "#ffffb6"
  light-blue: "#70aac8"
  error: "#700000"
  divider: "#dedede"

typography:
  display-xl:
    fontFamily: "'Rhymes Display', 'Rhymes Display Regular', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Rhymes Display', 'Rhymes Display Regular', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Rhymes Display', 'Rhymes Display Regular', Georgia, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  eyebrow:
    fontFamily: "'Franklin Gothic Cond ITC', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.8px
    textTransform: uppercase
  label-condensed:
    fontFamily: "'Franklin Gothic Cond ITC', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
    errorBorder: "1.5px solid {colors.error}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    iconColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    cartIconColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.eyebrow}"
    height: 36px
    padding: "0 {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
    minHeight: 600px
    padding: "{spacing.xxl} {spacing.xl}"
  section-eyebrow:
    textColor: "{colors.primary}"
    typography: "{typography.eyebrow}"
    marginBottom: "{spacing.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
    captionTypography: "{typography.body-sm}"
    captionColor: "{colors.muted}"
    imageRounded: "{rounded.md}"
    shadow: "0 1px 4px rgba(0,0,0,0.07)"
  benefit-badge:
    backgroundColor: "{colors.pale-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  ingredient-tag:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.label-condensed}"
    border: "1px solid {colors.light-blue}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    accentColor: "{colors.terracotta}"
    quoteMarkColor: "{colors.peach}"
  quiz-cta-block:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl} {spacing.xl}"
  pdp-accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    titleTypography: "{typography.title-md}"
    borderColor: "{colors.hairline}"
    divider: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.surface-soft}"
    headingTypography: "{typography.label-condensed}"
    headingColor: "{colors.hairline-soft}"
    padding: "{spacing.xxl} 0"
    dividerColor: "{colors.body}"

## Components

### Buttons

**`button-primary`** — The primary CTA runs #356687 fill with #fffff3 text on an 8px rounded rectangle, 48px tall, horizontally padded to 28px. On hover, the fill darkens to the `primary-active` tone (#2a5470); disabled state fades the fill to #9abfd4 while keeping the text legible. The button type (`{typography.button-md}`) is set in Inter at 15px/600 weight with a touch of tracking, lending a composed authority rather than urgency.

**`button-secondary`** — A canvas-background button outlined in 1.5px #356687, matching the primary's height and radius. Used for secondary actions on product pages and in modal flows. Active state shifts the background to `surface-soft` to provide tactile feedback without color shift. Text matches the border at `{colors.primary}`.

**`button-ghost`** — Transparent background, ink-colored text, underlined via CSS. Used inline in editorial copy, footnotes, and "learn more" links within long-form content blocks. No border, no radius — it disappears into prose without asserting a UI frame.

---

### Navigation

**`nav-bar`** — 64px tall, cream (#fffff3) background, separated from page content by a 1px #e2e2e2 hairline. Logo at left in #141414; right-side icons for account and cart. Navigation links in Inter 14px/500 with standard ink color; category items likely use a dropdown or mega-menu for the product taxonomy. The cream background ensures the nav reads as part of the page canvas rather than a detached chrome element.

**`announcement-bar`** — A 36px strip above the nav in #356687 with cream text set in Franklin Gothic Cond ITC eyebrow style. Typically used for free-shipping thresholds, promotions, or brief editorial statements. The condensed uppercase type keeps copy readable at a single glance without competing with the header below.

---

### Product Card

**`product-card`** — Cards sit on #f7f8fa with 12px corner radius and a near-invisible drop shadow (1px, 7% opacity black). Product image fills the top, also rounded at 12px. Title runs `{typography.title-sm}` (Inter 16px/600); price in `{typography.body-md}`; supporting descriptor text (shade name, size, or tagline) in `{typography.body-sm}` at muted gray (#737373). Ingredient or benefit tags may appear beneath the title using `ingredient-tag` or `benefit-badge` components.

---

### Hero Banner

**`hero-banner`** — The canvas (#fffff3) extends wall-to-wall, making hero sections feel like a continuation of the page rather than a distinct module. Eyebrow text in Franklin Gothic Cond ITC (#356687, all-caps, wide-tracked) precedes the headline. Headline runs Rhymes Display at 56px/400 weight — unhurried and editorial. Body copy in Inter 16px/1.65 line-height gives breathing room for the explanatory health language that the brand requires. CTA button drops below at full primary style. Minimum 600px height; image or illustration typically bleeds at right on desktop.

---

### Badges and Tags

**`benefit-badge`** — Pill-shaped (#ffffb6 fill, `{rounded.full}`) label in Franklin Gothic Cond ITC 13px. Used to surface high-level claims like "Clinically Studied" or "Hormone-Free" directly on product cards and hero sections. The pale yellow reads warm against the cream canvas without the alarm-register of bright accent colors.

**`ingredient-tag`** — A rectangular chip (#f7f8fa fill, 1px #70aac8 border, 4px radius) in Franklin Gothic Cond ITC 13px at #356687 text. Used in ingredient lists and PDP detail blocks to call out key actives. The light-blue border echoes the brand's blue family without competing with the primary CTA.

**`section-eyebrow`** — Standalone eyebrow label above section headlines: Franklin Gothic Cond ITC, all-caps, 1.8px letter-spacing, #356687. Always paired with a `{typography.display-md}` Rhymes Display headline below. The contrast between the condensed uppercase label and the open serif headline creates the brand's signature editorial rhythm.

---

### Testimonial Card

**`testimonial-card`** — Light gray (#f8f8f8) card at 12px radius with 24px internal padding. Quote body in Inter 16px/1.65; reviewer name and detail in Inter 12px at #737373. A terracotta (#e08a73) accent — typically a left-border stripe or oversized quotation mark — connects testimonials to the brand's warmer secondary palette. Star ratings, if present, likely render in #141414 rather than gold, consistent with the brand's restrained warmth.

---

### Quiz CTA Block

**`quiz-cta-block`** — A full-bleed or contained block in #356687, 20px radius, generous padding. Headline in Rhymes Display 26px (cream), body in Inter 16px (cream at reduced opacity). This block surfaces the brand's symptom-finder or product-match quiz — a core conversion mechanism for a health brand where the right product depends on individual symptom profile. A single `button-primary` variant in cream fill / primary text inverts inside this block to maintain contrast hierarchy.

---

### PDP Accordion

**`pdp-accordion`** — Cream background, 1px #e2e2e2 dividers between rows. Section titles in Inter 18px/600; expanded body text in Inter 16px/1.65 at `{colors.body}`. Used for Ingredients, How to Use, Clinical Evidence, and FAQ sections on product detail pages. Icon at right (chevron or plus/minus) in #737373. No radius — the accordion runs edge-to-edge within its container, framing clinical detail in a clean, zero-ornamentation shell.

---

### Footer

**`footer`** — Dark canvas (#141414) with #f8f8f8 body text and link color. Column headings in Franklin Gothic Cond ITC 13px at #eeeeee. Body links in Inter 14px, hover underlined. A 1px #545454 divider separates the link columns from the legal/copyright strip below. The dark footer creates a clear terminal boundary for the warm cream pages above — a tonal shift that reads as deliberate punctuation.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; hero headline drops to display-md (36px); nav collapses to hamburger; product grid becomes 1-up or 2-up; quiz-cta-block goes full-width with reduced padding (spacing.lg); announcement-bar text truncates to single key phrase |
| Tablet | 744–1128px | 2-column product grid; hero switches to split layout (copy left, image right); nav shows abbreviated link set; pdp-accordion retains full width; testimonial cards flow 2-up |
| Desktop | 1128–1440px | 3–4 column product grid; hero at full 600px minimum height with wide copy column; nav shows all category links; section eyebrows and Rhymes Display headlines at full scale; footer in 4-column layout |
| Wide | > 1440px | Max content width constrained to ~1400px, centered; hero image area expands; generous horizontal margin prevents line lengths from exceeding ~75ch in body text |

### Touch Targets

- All interactive buttons maintain 48px minimum height on mobile
- Nav icons (cart, account) target 44×44px minimum hit area
- Accordion rows extend to full row tap target, not just the chevron icon
- Ingredient tags and benefit badges scale padding on mobile to ensure ≥ 36px tap height

### Collapsing Strategy

- Navigation: full horizontal links collapse to hamburger drawer at < 744px; drawer inherits canvas (#fffff3) background
- Product grid: 4-up → 3-up → 2-up → 1-up as breakpoints descend
- Hero banner: side-by-side copy/image at desktop → stacked image-above-copy at mobile, image crops to 16:9
- Testimonial section: horizontal scroll carousel at mobile rather than multi-row grid
- Footer: 4-column link grid collapses to 2-column at tablet, single accordion-style at mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius values not confirmed from computed styles — `{rounded.sm}` (8px) is inferred from visual inspection of comparable Shopify wellness brands using this palette
- Franklin Gothic Cond ITC weight variants (regular vs. bold) not differentiated in extracted font stack; assumed bold (700) for eyebrow and label uses based on condensed display convention
- Rhymes Display specific weight/style variants (italic, medium) not enumerated — only "Regular" confirmed; italic may exist for pull-quote or hero subhead use
- Motion/animation tokens (transition duration, easing curves) not extractable from static analysis — brand likely uses subtle ease-in-out at ~200ms for hover states
- Hover states for `product-card` (elevation change, image zoom, add-to-cart reveal) not confirmed
- Dark mode or high-contrast mode support unknown
- Exact spacing rhythm for the PDP layout (sticky add-to-cart bar, image gallery behavior) not confirmed from extraction
- #007aff in the color list is almost certainly a Shopify/iOS system default (Apple blue) and has been excluded from the palette as a framework artifact
