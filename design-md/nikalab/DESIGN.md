---
version: alpha
name: "Nikalab"
source_url: "https://nikallab.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The name collapses two ideas — a personal first name and a laboratory — and that tension shapes the entire visual proposition: something that feels formulated for you specifically, not mass-produced. Premium supplement brands usually choose between clinical coldness and lifestyle warmth; Nikalab's positioning in the "lab" end of that spectrum suggests a canvas-dominant system where white space does the heavy lifting and a single restrained accent color carries all primary intent. Without live color extraction (the site appears to load tokens client-side or behind bot protection), the palette below is inferred from category-peer analysis of UK-origin premium supplement DTC brands that share the same clinical-meets-personal naming pattern: off-white canvases at #f8f7f5 or colder, ink at near-black rather than pure black to soften the clinical edge, and a muted primary drawn from warm neutrals or desaturated botanicals rather than a vivid hue. Typography in this segment almost universally resolves to a clean geometric sans-serif — Söhne, Inter, or a comparable stack — set at lighter weights for display and medium for body, leaning on tracking adjustments rather than weight contrast to create hierarchy. Buttons tend toward moderate radius (`{rounded.md}` range, approximately 8–12px) rather than the pill shapes of consumer wellness apps, because "lab" implies precision over softness. Product cards likely feature minimal decoration — a clean drop shadow or a hairline border at `{colors.hairline}`, generous internal padding, and the product image as the primary visual anchor. The components spec below constructs a coherent system from these inferences; every value should be validated against the live site before production use, and flagged gaps are enumerated at the end of this document.

colors:
  primary: "#4a6741"
  primary-active: "#3a5232"
  primary-disabled: "#b8cbb5"
  ink: "#1c1c1a"
  body: "#3b3b38"
  muted: "#767672"
  hairline: "#e0ddd8"
  hairline-soft: "#eeece8"
  canvas: "#ffffff"
  surface-soft: "#f8f7f5"
  surface-card: "#ffffff"
  surface-warm: "#f3f0eb"
  on-primary: "#ffffff"
  accent-warm: "#c8a97a"
  accent-warm-soft: "#f0e8da"

typography:
  display-xl:
    fontFamily: "'Söhne', 'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.96px
  display-md:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.48px
  display-sm:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.24px
  title-md:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: -0.18px
  title-sm:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.14px
    textTransform: uppercase
  body-md:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.12px
  caption-label:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0.66px
    textTransform: uppercase
  button-md:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.28px
  button-sm:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.36px
  nav-link:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link-label:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0.55px
    textTransform: uppercase
  ingredient-label:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  stat-display:
    fontFamily: "'Söhne', 'Inter', sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.0
    letterSpacing: -0.8px

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
    letterSpacing: 0.28px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
    textUnderlineOffset: 3px
  button-accent:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.sm}"
    padding: 13px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoTypography: "{typography.title-md}"
  nav-bar-announcement:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    captionTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    maxWidth: 1280px
    layout: split-50-50
  hero-headline-accent:
    textColor: "{colors.primary}"
  ingredient-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"
  stat-block:
    backgroundColor: "{colors.canvas}"
    numberTypography: "{typography.stat-display}"
    numberColor: "{colors.primary}"
    labelTypography: "{typography.caption-label}"
    labelColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  quiz-step:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xxl}"
  quiz-option:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    selectedBg: "{colors.surface-warm}"
    padding: 14px 20px
  accordion-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    triggerTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  benefit-pill:
    backgroundColor: "{colors.accent-warm-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.accent-warm}"
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-label}"
    iconColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    labelTypography: "{typography.nav-link-label}"
    linkColor: "{colors.hairline}"
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Forest-green fill (`{colors.primary}`) on white text, 8px radius (`{rounded.sm}`), 48px tall, letter-spaced label. The hover state darkens to `{colors.primary-active}`; the disabled state fades to `{colors.primary-disabled}` with `not-allowed` cursor. The moderate radius avoids both the hard corporate square and the overly casual pill, appropriate for a brand that wants to feel precise.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, same geometry as primary. Used for secondary CTAs on light surfaces; inverts to white border on dark backgrounds. Letter-spacing matches primary so the two buttons pair cleanly at equal visual weight.

**`button-ghost`** — Transparent background, `{colors.primary}` text, underline with 3px offset. Reserved for inline actions (quiz navigation "back", ingredient detail links) where a full button would be visually excessive.

**`button-accent`** — Uses `{colors.accent-warm}` (a muted sand/caramel tone) as fill, intended for promotional or secondary-page CTAs that need warmth without competing with the primary green. Shares geometry with `button-primary`.

### Inputs

**`text-input`** — White canvas, 1px `{colors.hairline}` border at rest, thickens and shifts to `{colors.ink}` on focus. 48px height aligns with button height so form rows sit flush. Placeholder text uses `{colors.muted}`. No inner shadow or glow — the brand relies on border-weight contrast alone to signal state.

### Navigation

**`nav-bar`** — 64px tall, white, 1px soft hairline bottom border. Logo likely rendered in `{typography.title-md}` weight with tracked-out caps or in SVG wordmark. Nav links use `{typography.nav-link}` at regular weight. Above the nav, `nav-bar-announcement` — a 36px green strip in `{colors.primary}` — carries promotions in all-caps caption type. The announcement strip collapses on mobile when vertical space is at a premium.

### Product Cards

**`product-card`** — White surface, 1px soft border, 8px radius. Image sits on a `{colors.surface-soft}` swatch background. Title uses `{typography.title-md}`, price uses `{typography.body-md}`, supporting copy in `{typography.body-sm}`. Spacing is generous — 16px internal padding — to prevent the information density from feeling clinical rather than curated.

### Hero

**`hero`** — Split 50/50 layout on desktop: editorial copy left, product image right. Background tints to `{colors.surface-soft}` rather than full white to signal a section boundary without a hard rule. Headline at `{typography.display-xl}` (300 weight, -0.96px tracking) with the occasional `{typography.display-md}` subhead. The accent-colored word or phrase within the headline uses `hero-headline-accent` to pull the primary green into the editorial space without a background block.

### Quiz / Personalization

**`quiz-step`** — Large padded card (`{spacing.xxl}` padding, `{rounded.md}` radius) that centers the formulation question with `{typography.display-sm}` headline and `{typography.body-md}` body. **`quiz-option`** — Selectable answer tiles: soft fill at rest, 2px primary border + `{colors.surface-warm}` background when chosen. No checkbox icons — the border weight alone indicates selection state.

### Supporting

**`ingredient-badge`** — Small warm-surface chips with `{colors.hairline}` border listing key compounds (Vitamin D3, Omega-3, etc.). All-caps caption-label type at 11px. These appear in a horizontal scroll row on mobile below the product title.

**`stat-block`** — Large numeral in `{typography.stat-display}` (40px, 300 weight) colored `{colors.primary}`, with an uppercase label beneath in `{colors.muted}`. Used in social-proof sections ("10,000+ customers", "92% saw results in 8 weeks").

**`benefit-pill`** — Rounded-full chips in the warm accent soft color (`{colors.accent-warm-soft}`) with a subtle accent border. Used as feature-flag decorations near section headers rather than as interactive elements.

**`accordion-item`** — Borderless top, 1px bottom hairline. Trigger in `{typography.title-md}`; expanded body in `{typography.body-sm}`. Used for ingredient deep-dives, FAQ, and dosage instructions. No background fill — the accordion lives directly on whatever page surface is behind it.

**`trust-bar`** — A full-width stripe in `{colors.surface-soft}` carrying 3–5 icon+label trust signals (e.g. "Third-party tested", "Free UK delivery", "Certified GMP facility") in `{typography.caption-label}` with `{colors.primary}` icons. Appears both below the hero and above the footer.

**`footer`** — Dark ink fill (`{colors.ink}`) reverses text to white. Column headings in `{typography.nav-link-label}` (uppercase, tracked), links in `{typography.body-sm}` at `{colors.hairline}` opacity. Generous vertical padding (`{spacing.xxl}`).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks image below copy; product grid collapses to 1 column; nav-bar hides text links behind a hamburger icon; ingredient-badge row becomes horizontal scroll; quiz options stack vertically full-width; announcement bar truncates to single key message |
| Tablet | 744–1128px | 2-column product grid; hero remains stacked but image scales up; nav shows primary links with overflow menu for secondary; stat-blocks appear in a 2×2 grid |
| Desktop | 1128–1440px | Hero splits 50/50; 3-column product grid; full nav link row; trust-bar expands to 5 icons inline; quiz options display as 2-column grid |
| Wide | > 1440px | Max-width container locks at 1280px and centers; hero image may extend to bleed edge; additional whitespace added via increased section padding |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Quiz option tiles expand to full-width for easy tap
- Nav links in mobile menu set to at least 48px row height
- `ingredient-badge` chips are non-interactive (display only); no minimum enforced

### Collapsing Strategy
- Navigation: hamburger at < 744px; full link row from 1128px; at tablet, primary links visible and secondary in overflow
- Hero: split layout at ≥ 1128px only; stacked below that
- Product grid: 1 col → 2 col → 3 col at 744px / 1128px breakpoints
- Accordion: always single-column; no lateral expansion
- Footer columns: 2-column stack on mobile, 4-column grid on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex colors are inferred** — the live site (nikallab.com) returned no extractable color tokens; the palette above is constructed from category-peer analysis and should be verified against the live stylesheet or Figma source before use
- **Font stack is unknown** — no `font-family` declarations were extracted; Söhne/Inter is a plausible inference for a premium UK supplement brand but may be incorrect
- **Primary brand color is unconfirmed** — the olive-green `#4a6741` is a hypothesis; it is possible the brand uses a cooler tone, a warm neutral, or a completely different hue
- **Accent color origin unverified** — `{colors.accent-warm}` (#c8a97a) is inferred from packaging aesthetic conventions in the category, not extracted from the site
- **Rounded values are inferred** — no border-radius tokens were captured; values approximate what the "lab" positioning suggests
- **No theme-color meta tag** — the site did not expose a `meta[name=theme-color]`, removing a common shortcut to the primary brand color
- **Shopify vs. custom platform unknown** — `platform-shopify: False` but no alternative platform detected; component structure may differ from standard Shopify component patterns
- **Logo treatment unknown** — wordmark, lettermark, or icon-plus-wordmark composition could not be confirmed
- **Quiz/personalization flow** — inferred from category norm; actual quiz architecture (steps, logic branching, result page) may differ significantly
