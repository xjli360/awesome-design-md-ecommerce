---
version: alpha
name: "Knaggs Guitars"
source_url: "https://www.knaggsguitars.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Amber lacquer tones — #e09900 and its honeyed companion #edb059 — appear against near-black grounds (#121212, #2a2a2a) with the same material logic a carved guitar top brings to a dark-stained body: warm wood illuminating absorbed depth. The company was founded by Joe Knaggs, longtime master builder at PRS, and that lineage of lutherie precision is legible in the digital structure: Archivo Black carries display headlines at full weight, its dense stroke width echoing the deliberate geometry of a chambered archtop, while regular-weight Archivo handles body copy in a cool light-gray (#d0d0d0) that rests comfortably over dark canvas without strain. The amber primary reads less as a brand-kit choice and more as a material reference — the flash of figured maple under stage lighting, or the specific warm glow of a nitro-lacquer finishing room on a humid afternoon. Dark surface layers stack in controlled increments: base canvas at #121212, soft surface at #2a2a2a, card face at #313131 — small steps that give the product grid visible depth without resorting to heavy dividers or drop shadows. Secondary interactive elements land in two calibrated blues (#1863dc, #0056a7) that keep click targets legible on dark ground without pulling warmth from the amber. A slate-purple (#4e4b66) appears in supporting chrome, a tone that is muted but distinctly not neutral, distinguishing the site from purely monochromatic dark-mode guitar retailers. Border radii stay small throughout: inputs and cards hold `{rounded.xs}` to `{rounded.sm}`, lending the UI a machined, precise quality in keeping with the brand's commitment to dimensional accuracy in lutherie. Typographic hierarchy is blunt — Archivo Black at large sizes and tight line-height for headlines, then a sudden drop to regular-weight Archivo for body copy with no intermediate decorative weights cluttering the stack. Section spacing is wide and unhurried, each instrument given enough breathing room to register as a singular object rather than a catalog entry, in explicit contrast to the dense grids of mass-market guitar sites.

colors:
  primary: "#e09900"
  primary-active: "#c07800"
  primary-disabled: "#664400"
  ink: "#eeeeee"
  body: "#d0d0d0"
  muted: "#abb8c3"
  hairline: "#4e4e4e"
  canvas: "#121212"
  surface-soft: "#2a2a2a"
  surface-card: "#313131"
  on-primary: "#121212"
  accent-blue: "#1863dc"
  accent-blue-hover: "#0056a7"
  amber-warm: "#edb059"
  slate-ui: "#4e4b66"
  dark-slate: "#2d3940"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Archivo Black', 'Arial Black', sans-serif"
    fontSize: 52px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -1px
  display-md:
    fontFamily: "'Archivo Black', 'Arial Black', sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.5px
  title-lg:
    fontFamily: "'Archivo Black', 'Arial Black', sans-serif"
    fontSize: 26px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: 0
  title-md:
    fontFamily: "'Archivo', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Archivo', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Archivo', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Archivo', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Archivo Black', 'Arial Black', sans-serif"
    fontSize: 24px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Archivo Black', 'Arial Black', sans-serif"
    fontSize: 14px
    fontWeight: 900
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Archivo', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Archivo', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  label-tag:
    fontFamily: "'Archivo', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  spec-key:
    fontFamily: "'Archivo', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    border: "1.5px solid {colors.primary}"
    textColor: "{colors.primary}"
  button-ghost-amber:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: "2px solid {colors.amber-warm}"
    outlineOffset: 0px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.on-dark}"
    activeLinkColor: "{colors.primary}"
    activeLinkBorderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "4/3"
    padding: 16px
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.primary}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    minHeight: 600px
    overlayGradient: "linear-gradient(to right, rgba(18,18,18,0.88) 42%, transparent 100%)"
    ctaSpacing: 24px
  series-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    keyTypography: "{typography.spec-key}"
    keyColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline}"
    rowPadding: 10px 16px
    rounded: "{rounded.sm}"
  guitar-gallery:
    backgroundColor: "{colors.surface-card}"
    mainImageRounded: "{rounded.sm}"
    thumbnailBorder: "2px solid transparent"
    thumbnailBorderActive: "2px solid {colors.primary}"
    thumbnailRounded: "{rounded.xs}"
    thumbnailHeight: 80px
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    thumbnailGap: 4px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    padding: 10px 16px
    height: 44px
    focusBorder: "1px solid {colors.primary}"
  finish-swatch:
    size: 40px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.primary}"
    borderGapActive: 2px
    borderInactive: "2px solid transparent"
    swatchGap: 8px
  cta-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: 64px 32px
    accentBorderLeft: "3px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.label-tag}"
    headingColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: 48px 0
    columns: 4

---

## Components

### Buttons

**`button-primary`** — Solid amber (#e09900) block with near-black Archivo Black uppercase lettering, the brand's single high-energy CTA surface. Hover state deepens to #c07800, maintaining the warm amber register without jarring shift; disabled state mutes to #664400 with gray text, signaling unavailability without opacity reduction. Sharp `{rounded.xs}` corners make the button read as a stamped, machined element — not a soft consumer pill.

**`button-secondary`** — Transparent with a 1.5px #eeeeee border and white uppercase Archivo Black text, pairing cleanly beside `button-primary` as a clear second choice on dark surfaces. Hover transitions the border and text to #e09900 amber, echoing the primary without filling it. Used for "Learn More," "View Gallery," and secondary navigation CTAs.

**`button-ghost-amber`** — Minimal outline button in amber (#e09900) border and text, reserved for tertiary actions such as "View Specs" or "Download Brochure" where full amber fill would dominate. Sits at 40px height versus 48px for primaries — a deliberate subordination signal.

### Forms

**`text-input`** — Dark charcoal (#2a2a2a) fill with a 1px #4e4e4e border produces a sunken-surface feeling appropriate for contact and order forms on the dark canvas. Focus state rings the field in a 2px amber (#edb059) outline, making active fields immediately identifiable at a glance. Placeholder text in #abb8c3 provides contrast cues without competing with entered #eeeeee text.

### Navigation

**`nav-bar`** — Fixed dark bar at 72px, background matching the #121212 canvas so the nav reads as an extension of the page rather than an overlay panel. Navigation links in 13px uppercase Archivo at 0.8px letter-spacing; active link receives an amber (#e09900) underline and text color. Logo anchors left in white; mobile menu trigger anchors right. The nav is spare — model families, About, and a Search icon, nothing more.

### Products

**`product-card`** — Dark card (#313131) with a 1px #4e4e4e border and `{rounded.sm}` radius sits against the base canvas with visible but subtle lift. Product photography fills a 4:3 image area at top; model name in 18px bold Archivo below; price in 24px Archivo Black in amber (#e09900). A brief series descriptor in #d0d0d0 body text completes the reading hierarchy. Hover state: card border transitions to #e09900 amber, providing recognition feedback without animation overload.

**`guitar-gallery`** — Main image fills a `{rounded.sm}` container; a horizontal thumbnail strip runs below at 80px tall with 4px gaps. Active thumbnail receives a 2px amber border; inactive thumbnails have transparent borders, keeping the focus on the selected image. Swipe-enabled on mobile; keyboard arrow navigation on desktop. Caption typography in 13px Archivo muted-gray appears below the main frame for finish or series notes.

**`finish-swatch`** — 40px circular swatches displaying guitar finish options on product configuration pages. Selected state: 2px amber (#e09900) border with a 2px gap between swatch surface and ring, creating a clear selection halo. Used for finishes such as Natural, Three-Tone Sunburst, and custom color options. The amber selection ring ties finish choice back to the brand primary.

### Hero

**`hero`** — Full-bleed guitar photography with a left-side gradient overlay (rgba(18,18,18,0.88) to transparent at 42%), keeping the headline legible while the right half of the frame shows the instrument in full color. Headline in 52px Archivo Black; subhead in 16px Archivo at #d0d0d0. Primary CTA button sits 24px below subhead. The combination positions each hero as a poster rather than a marketing banner.

### Series & Badges

**`series-badge`** — Small amber (#e09900) chip with near-black Archivo uppercase text at 1.5px letter-spacing, affixed to product imagery or card headers to call out series names: Kenai, Tula, Choptank, Pegasus. Sharp `{rounded.xs}` corners match the broader UI vocabulary and avoid softening the brand tone.

### Specs

**`spec-table`** — Two-column table on a #2a2a2a surface. Left column: specification name in 12px uppercase Archivo at #abb8c3 muted-gray. Right column: specification value in 14px Archivo at #eeeeee. Rows separated by 1px #4e4e4e hairlines. Used on product detail pages for body wood, neck profile, scale length, fret count, nut width, and hardware spec details. The uppercase muted-gray keys evoke a luthier's blueprint spec sheet.

### Discovery

**`search-bar`** — Dark #2a2a2a input with a magnifying-glass icon in #abb8c3, at 44px height with `{rounded.xs}`. On focus the border transitions to amber (#e09900). On mobile, activating search opens a full-overlay panel; on desktop, a dropdown of results appears inline with product images, model names, and series badges.

### Editorial

**`cta-strip`** — Full-width band in #2a2a2a with a 3px left-border accent in amber (#e09900). Headline in 26px Archivo Black; body copy in 16px Archivo at #d0d0d0. One primary button and an optional ghost-amber secondary link. Appears between page sections as an editorial break and conversion nudge — typically linking to the custom shop inquiry form or dealer locator.

### Footer

**`footer`** — Four-column grid on #121212 canvas, separated from the body by a 1px #4e4e4e top border. Column headings in 11px uppercase Archivo at #eeeeee; links in 14px Archivo at #d0d0d0 with hover transitioning to #e09900 amber. Social icons row anchors to the bottom-right. The amber hover echo on footer links closes the amber reading loop that begins in the hero CTA.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to 32px display-md; nav collapses to hamburger; guitar-gallery thumbnails scroll horizontally; spec-table stacks key above value; footer collapses to single column |
| Tablet | 744–1128px | Two-column product grid; hero headline at 42px; nav shows top-level labels, sub-items in dropdown; spec-table returns to two-column; footer in two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all series labels visible; hero headline at 52px; cta-strip goes two-column (text left, CTA right) |
| Wide | > 1440px | Four-column product grid; hero image fills viewport with broader gradient spread; max content-width capped ~1400px with auto side margins; footer four-column |

### Touch Targets

- All interactive buttons minimum 48px tall
- Finish swatches 40px diameter with 8px gaps, meeting minimum tap spacing
- Nav hamburger trigger 44×44px minimum
- Guitar gallery thumbnail strip scrollable with momentum on iOS; thumbnails 80px tall × auto width with minimum 64px wide
- Footer links line-height expanded to 44px effective tap height on mobile

### Collapsing Strategy

- Primary nav collapses first: model families move to hamburger drawer, direct-buy CTA persists in top-right at all breakpoints
- Product grid degrades from four to three to two to one column as width decreases; card images maintain 4:3 ratio throughout
- Hero: text overlay maintains 88% opacity gradient at all sizes; body copy line hidden on mobile below 480px to keep headline/CTA above fold
- Spec table converts from two-column inline layout to stacked key-then-value on mobile, maintaining the full specification set without truncation
- Footer collapses from four to two to one column; social icons move below nav links rather than anchoring right

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color detected; dark canvas assumption (#121212) inferred from extracted near-black values and instrument photography conventions, not confirmed
- Many colors in the extracted list (#00d084, #0693e3, #f78da7, #cf2e2e, #ff6900, #fcb900, #7bdcb5, #8ed1fc, #9b51e0) appear to be WordPress Gutenberg block-editor palette entries, not brand tokens — excluded from the system
- Font weights for Archivo Black could not be confirmed as CSS-loaded versus system-substituted; weight 900 assumed from the Black variant name
- Exact button radius in the live UI not measurable; `{rounded.xs}` (4px) is a best-inference from the precision-instrument aesthetic
- Price display formatting (with or without "Contact for Pricing" flows for custom instruments) not determinable from extraction
- Mobile nav drawer behavior (slide-in vs. full-overlay) not confirmed
- Custom-shop and dealer-locator form field styling not extractable; `text-input` spec is inferred from site color palette
