---
version: alpha
name: "Holden"
source_url: "https://www.hiholden.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  An olive-gold patina — #868159 — anchors Holden's palette in a tone that reads less like jewelry marketing and more like the warm oxidation of a well-worn keepsake. Against a cream-ivory canvas (#f9f8f1), the effect is intimate rather than aspirational: this is not the cold platinum showroom of legacy bridal, but something closer to a letter-writing room. Louize, a contemporary serif with humanist optical corrections, carries all display weight — headlines feel read rather than advertised. Petit Formal Script appears in editorial moments to sign off with something personal, while TO Record brings structured geometric contrast to UI contexts like navigation and captions. The supporting palette carries a dusty slate-blue (#676986) that keeps the warmth from tipping into sentimentality, and a warm amber (#f4ba7d) that evokes late-afternoon light rather than precious metal. Rounded corners are minimal — sharp-edged interactive elements only, with ring photography given generous, hard-cropped frames. The system trusts negative space and ivory over decoration: no gradients, no sparkle motifs, just restrained surfaces that let close, warm-lit product photography carry the emotional load. CTAs appear in olive-gold primary, inverted in cream ({colors.on-primary}), reinforcing the brand's material world. Navigation is quiet and horizontal, with generous spacing and zero drop-shadows. The lab-grown diamond positioning is handled through confident typography — no asterisks, no hedging — suggesting the brand has already moved past the need to justify the choice. Hairlines in #e5e5e5 divide content at the lightest possible boundary, while muted-warm #b0a38b provides warmth-on-warmth depth for nested surfaces and metadata rows.

colors:
  primary: "#868159"
  primary-hover: "#868155"
  primary-active: "#59552d"
  primary-disabled: "#c8c5b3"
  accent-slate: "#676986"
  accent-amber: "#f4ba7d"
  accent-mint: "#b2f9e9"
  ink: "#121212"
  body: "#272d45"
  muted: "#969696"
  muted-warm: "#b0a38b"
  hairline: "#e5e5e5"
  hairline-cool: "#dbdde4"
  canvas: "#f9f8f1"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  surface-warm: "#c8c5b3"
  on-primary: "#f9f8f1"
  on-dark: "#f9f8f1"
  near-black: "#121212"

typography:
  display-xl:
    fontFamily: "'Louize', serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Louize', serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Louize', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Louize', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Louize', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Louize', serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Louize', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Louize', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  script-accent:
    fontFamily: "'Petit Formal Script', cursive"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption:
    fontFamily: "'TO Record', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  caption-serif:
    fontFamily: "'Louize', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-micro:
    fontFamily: "'TO Record', sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'TO Record', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'TO Record', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'TO Record', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "'Louize', serif"
    fontSize: 20px
    fontWeight: 400
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
    transition: background-color 200ms ease
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    logoColor: "{colors.ink}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xxl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-micro}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    nameTypography: "{typography.title-sm}"
    nameColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.body}"
    metalLabelTypography: "{typography.caption}"
    metalLabelColor: "{colors.muted}"
    gap: "{spacing.md}"
    hoverEffect: "image-scale 1.03 transition 400ms ease"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    scriptAccentTypography: "{typography.script-accent}"
    scriptAccentColor: "{colors.primary}"
    layout: "full-bleed image left, text right, 50/50 split"
    minHeight: 600px
    padding: "{spacing.xxl} {spacing.section}"
    ctaComponent: "button-primary"
  ring-swatch:
    size: 32px
    rounded: "{rounded.full}"
    borderWidth: 2px
    borderColorSelected: "{colors.primary}"
    borderColorDefault: "{colors.hairline}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    gap: "{spacing.sm}"
  stone-shape-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
    selectedBackgroundColor: "{colors.canvas}"
    selectedBorderColor: "{colors.primary}"
    selectedBorderWidth: 1px
    selectedTextColor: "{colors.ink}"
  lab-grown-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.body}"
    typography: "{typography.label-micro}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  certification-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-warm}"
    typography: "{typography.label-micro}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-cool}"
    padding: "6px 12px"
  pdp-detail-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.body}"
    bodyTypography: "{typography.body-md}"
    sectionDivider: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.primary}"
    height: 48px
    borderBottom: "1px solid {colors.hairline}"
    gap: "{spacing.lg}"
  diamond-comparison-table:
    backgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.caption}"
    headerColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    highlightBackgroundColor: "{colors.canvas}"
    highlightBorderColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  size-guide-tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.canvas}"
    scriptWordmarkTypography: "{typography.script-accent}"
    scriptWordmarkColor: "{colors.muted-warm}"
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons
**`button-primary`** — Flat olive-gold fill (#868159) with zero border radius and TO Record uppercase lettering at 1.5px tracking; the squareness signals precision workmanship over soft consumer retail. On hover the fill shifts to #868155; on active it deepens to #59552d; disabled renders in warm #c8c5b3. All state transitions run at 200ms ease.

**`button-secondary`** — A transparent field bounded by a 1px solid ink border, same TO Record uppercase treatment. Used for secondary CTAs like "Learn More" or "Compare Settings." The ink border is unrelenting — no softening — maintaining the brand's hard-edge composure against the ivory canvas.

**`button-ghost`** — Bare text in olive-gold (#868159) with no bounding box, used for inline "View Details" and editorial navigation moments where a full button would over-weight the context. No underline at rest; underline appears on hover.

### Text Input
**`text-input`** — Clean field on ivory canvas (#f9f8f1) bounded by a single 1px hairline in #e5e5e5; no radius. Focus triggers the hairline to shift to olive-gold (#868159) without any glow or shadow — an almost imperceptible state change that rewards close attention. Placeholder text in #969696 fades on interaction.

### Navigation
**`nav-bar`** — 72px tall, warm ivory (#f9f8f1) background with a soft hairline separator below. The Holden wordmark renders in Louize `{typography.display-sm}`; navigation links in TO Record uppercase at 12px with 1px tracking. Zero elevation — no shadow, no blur — the bar reads as a flat continuation of the page surface. An announcement bar in olive-gold primary sits above it for promotional copy. On mobile the full nav collapses to a centered wordmark with a hamburger icon.

### Product Card
**`product-card`** — Portrait 3:4 ring image bleeds edge-to-edge with no card padding; the ring photograph is the card. Below the image: ring name in Louize `{typography.title-sm}`, price in `{typography.price-display}`, and a metal-and-setting descriptor in TO Record `{typography.caption}` muted gray. No card border, no shadow — cards sit directly on the ivory canvas. Hover triggers a 1.03× image scale over 400ms, deliberate and slow.

### Hero Editorial
**`hero-editorial`** — Full-bleed two-column layout at 50/50 split: a warm, close-crop ring photograph on the left, editorial text on the right. The headline in Louize `{typography.display-xl}` can be interrupted by a Petit Formal Script accent line in olive-gold (#868159), lending the composition handwritten intimacy. Background is the ivory canvas with no overlay or scrim. The primary CTA renders directly below the subhead. On mobile the image stacks above full-width and the text block follows at standard padding.

### Ring Swatch Selector
**`ring-swatch`** — 32px circular swatches filled with metal color (yellow gold, rose gold, platinum, white gold) as inline SVG fills or solid hex approximations. Selected state: 2px olive-gold border. Default state: 1px hairline. Gap between swatches 8px (`{spacing.sm}`). Metal name appears below each swatch in TO Record `{typography.caption}` muted.

### Stone Shape Selector
**`stone-shape-selector`** — Icon-plus-label tiles in a horizontal row, each outlined with a 1px hairline on a soft surface-soft (#f4f4f6) background. Selected tile gains a 1px olive-gold border and white (#ffffff) background. Labels in TO Record uppercase at 12px. Covers Round, Oval, Emerald, Pear, Cushion, Marquise, and Radiant.

### Lab-Grown Badge
**`lab-grown-badge`** — A small mint-green (#b2f9e9) rectangular chip in TO Record `{typography.label-micro}` uppercase. Applied to product cards and the PDP header. The mint reads as a deliberate counterpoint to the warm olive palette — a forward-sourcing signal delivered without moral weight.

### Diamond Comparison Table
**`diamond-comparison-table`** — Full-width table on surface-soft (#f4f4f6). Column headers in TO Record uppercase muted; cells in Louize body-sm. The recommended column is highlighted with a white background and 1px olive-gold border on all four sides, making the brand's preference legible without hard-sell typographic weight.

### PDP Detail Panel
**`pdp-detail-panel`** — Right-hand (or below-image on mobile) panel in ivory canvas. Ring name in Louize `{typography.display-md}`; starting price in `{typography.price-display}`. Sections for metal, stone shape, carat weight, and setting style are divided by 1px hairlines. Each section opens with a TO Record uppercase label in muted, followed by swatches or selectors. The primary CTA button sits fixed at the bottom of the panel on mobile.

### Footer
**`footer`** — Near-black (#121212) base breaks cleanly from the warm ivory site above. Column headings in TO Record `{typography.caption}` muted; links in Louize `{typography.body-sm}` muted gray (#969696), gaining ivory on hover. A Petit Formal Script wordmark variant may appear above the legal baseline for a personal closing — the only ornamental flourish in an otherwise spare footer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + centered wordmark; product grid is 2-column; hero stacks image above text full-width; stone shape selector scrolls horizontally; PDP detail panel moves below image at full width; diamond comparison table becomes swipeable card stack |
| Tablet | 744–1128px | 2–3 column product grid; nav stays horizontal with condensed links; hero maintains two-column at reduced padding; filter bar scrolls horizontally; PDP remains side-by-side but at reduced panel width |
| Desktop | 1128–1440px | 4-column product grid; full nav with all categories visible; hero two-column at generous `{spacing.section}` padding; diamond comparison table at full width; PDP sticky right panel |
| Wide | > 1440px | Max content width capped at 1440px centered; hero image fills remaining edge bleed; grid stays at 4-column with larger card dimensions |

### Touch Targets
- All buttons minimum 48px tall — `button-primary` height as baseline
- Ring swatches are 32px with 8px gap, giving an effective 40px touch zone
- Navigation links in mobile hamburger menu minimum 44px tall
- Stone shape selector tiles minimum 44px tall with lateral padding
- Filter bar items minimum 44px tall with horizontal padding

### Collapsing Strategy
- Navigation: full horizontal desktop/tablet → centered wordmark + hamburger on mobile
- Product grid: 4-col → 3-col (tablet) → 2-col (mobile)
- Hero: two-column editorial → image-over-text stacked on mobile
- Ring customizer sections: side-by-side panels on desktop → accordions on mobile
- Stone shape selector: wrapping tile grid on desktop → horizontal scroll strip on mobile
- Diamond comparison table: full table desktop/tablet → horizontal swipe card stack on mobile
- PDP detail panel: sticky right column on desktop → full-width below image on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius value extracted from the live site; `{rounded.none}` (0px) assumed from fine jewelry brand conventions — actual site may use `{rounded.xs}` on some elements
- Font weights for Louize not confirmed from extraction; weight 400 assumed as primary display weight; semibold or medium variants may exist for certain title contexts
- Miss Confidential found in the font stack but its specific usage context could not be determined — may be an alternate script accent or a deprecated asset from a previous iteration
- Exact TO Record usage scope (UI-only vs. some body copy) inferred rather than confirmed; assigned to caption/button/nav roles
- No confirmed grid column count or gutter width extracted; values derived from visual conventions for the engagement ring category
- No dark mode palette detected; site appears to operate on a single warm-ivory theme
- Animation and transition timing values not confirmed from extraction; 200ms and 400ms are inferred defaults
- Price formatting convention (currency symbol, comma placement, starting-at phrasing) not confirmed
- Exact hero image crop strategy and aspect ratios not confirmed from extraction
- #2c3e50 in the extracted set is a widely used CSS default (Bootstrap's dark text) and may not be a deliberate brand token
