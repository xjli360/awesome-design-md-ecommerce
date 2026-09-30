---
version: alpha
name: "Sugar Paper"
source_url: "https://sugarpaper.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Periwinkle (#899df1) does the unexpected work here — in a stationery category that reaches for blush and cream by reflex, Sugar Paper's brand voltage is a soft blue-violet that reads simultaneously dreamy and precise. The chromatic story assembles in three washes: the periwinkle pairs against a warm blush surface (#feede3) and a cool mint field (#dff1ed), three watercolor registers that float above a near-black ink (#242833) — warmer than pure #000000 — and a hairline gray (#dedede) that borders without announcing itself. Monotype Baskerville carries every headline and editorial moment; this is a deliberate reach for the publishing shelf, not the gift-shop card rack. The serif's old-style structure gives product names and planner categories a typographic authority that Proxima Nova, deployed at the UI layer for prices, navigation, and form labels, deliberately withholds. The split is consistent and readable: Baskerville invites; Proxima Nova transacts. Sweet Sans Pro appears at small scale for badge copy and uppercase category callouts, bridging the two registers without collapsing their tension. Corners are uniformly soft throughout — pill shapes ({rounded.full}) for filter chips and collection tags, {rounded.md} for editorial planner cards, {rounded.sm} for primary buttons — the only hard corners are in the body grid. Product photography follows the palette logic: flat lays on blush and mint paper fields, notebooks photographed open to show interior ruled pages, the physical grain of the goods echoing the warm ink tones in the type. The brand's editorial confidence shows in its willingness to set long Baskerville display strings against low-contrast soft surfaces — legibility yields slightly to mood, which is the right trade for a brand whose products are about slowing down and writing things by hand.

colors:
  primary: "#899df1"
  primary-active: "#6b7fd4"
  primary-disabled: "#c4cefc"
  ink: "#242833"
  body: "#252525"
  muted: "#757575"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-blush: "#feede3"
  surface-mint: "#dff1ed"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  deep: "#121212"

typography:
  display-xl:
    fontFamily: "'Monotype Baskerville W01', 'Monotype Baskerville™ W03', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Monotype Baskerville W01', 'Monotype Baskerville™ W03', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Monotype Baskerville W01', 'Monotype Baskerville™ W03', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Proxima Nova W01', 'Proxima Nova W02', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Proxima Nova W01', 'Proxima Nova W02', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  body-md:
    fontFamily: "'Proxima Nova W01', 'Proxima Nova W02', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Proxima Nova W01', 'Proxima Nova W02', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Proxima Nova W01', 'Proxima Nova W02', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "sweet-sans-pro, 'Proxima Nova W01', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  badge:
    fontFamily: "sweet-sans-pro, 'Proxima Nova W01', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Proxima Nova W01', 'Proxima Nova W02', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Proxima Nova W01', 'Proxima Nova W02', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Proxima Nova W01', 'Proxima Nova W02', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "'Proxima Nova W01', 'Proxima Nova W02', sans-serif"
    fontSize: 15px
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
    height: 44px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageRounded: "{rounded.none}"
    cardRounded: "{rounded.none}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price}"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaComponent: button-primary
  collection-badge:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
    gap: "{spacing.xl}"
  editorial-banner:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: none
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
    placeholderColor: "{colors.muted}"
  swatch-chip:
    size: 24px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "1px solid {colors.hairline}"
  planner-card:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-sm}"
    labelTypography: "{typography.label-upper}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  newsletter-stripe:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    inputComponent: text-input
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.deep}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Periwinkle fill (#899df1) with white uppercase Proxima Nova at 14px and 1px letter-spacing; the spacing gives the label enough air to read as deliberate rather than default-framework. Active state darkens to #6b7fd4; disabled fades to a muted lavender (#c4cefc) that signals unavailability without collapsing into the generic gray most brands use. **`button-secondary`** mirrors the geometry exactly — white fill, 1px ink border — so pairing them in a two-button row maintains formal symmetry while the color difference communicates hierarchy. **`button-ghost`** removes the border entirely and is reserved for tertiary destructive or dismissal actions. **`button-pill`** uses the blush surface and full rounding for filter chips and inline collection tags where a rectangular button would feel over-engineered.

### Navigation
The nav bar holds at 64px with the Baskerville wordmark at display-sm scale — the first typographic signal on every page, serif against uppercase sans, delivered before any product image loads. Navigation links use uppercase Proxima Nova at 13px with 0.8px tracking; the restraint in size (not 16px) keeps the nav from competing with the wordmark. A fine hairline border (#dedede) at the bottom separates the nav from the content without adding visual mass. On mobile the logo centers and a hamburger icon (44px touch target) replaces all navigation links; the full menu opens as a full-screen drawer with the same uppercase Proxima Nova treatment at a larger size.

### Product Card
Cards are flat — no border-radius, no drop shadow — letting photography do all the visual lifting. The product title sits in Proxima Nova body weight (400), not bold, which keeps the grid from feeling like a product catalog scream. Price uses the dedicated price scale (500 weight, 15px) for enough visual separation without requiring color differentiation. A `new-badge` in periwinkle can stack at the top-left corner of the image; it uses `{rounded.xs}` rather than a pill because the stationery product context calls for something more label-like than chip-like. Hover state adds a light shadow lift; the image does not scale or zoom.

### Hero Banner
The hero lives on the blush field (#feede3), the brand's warmest surface, with display-xl Baskerville headline and a `button-primary` CTA. Vertical padding uses the full `{spacing.section}` value top and bottom, creating the generous whitespace the serif headline needs to breathe. On desktop, product photography anchors at right in a 50/50 split; on mobile, the image stacks above the text block and the padding reduces to `{spacing.xl}`.

### Collection Badge & Category Strip
Collection badges use the mint surface (#dff1ed) with uppercase Sweet Sans Pro — filter chips for "Planners," "Memory Books," "Notebooks." The `{rounded.full}` pill gives them a softness that contrasts with the flat product cards below and codes them as interactive without requiring a strong border. The category strip is a horizontally scrollable 48px bar that uses the same `label-upper` typography, with a bottom hairline border to anchor it in the layout.

### Planner Card
A dedicated card variant for the planner collection: blush background, `{rounded.md}` corners, and a large display-sm Baskerville headline naming the planner type. A label-upper callout sits above the headline, typeset in Sweet Sans Pro, identifying the year or edition. This component appears on the planner collection pages and in homepage feature modules; it is the most editorial surface in the product-browsing layer.

### Editorial Banner
Mint-field (#dff1ed) sections appear between product grid rows as content breaks — a Baskerville display-md heading with a Proxima Nova body paragraph. These are full-bleed, no rounded corners, functioning like magazine spreads interpolated into the shopping experience. Used for brand storytelling, gift-guide callouts, and seasonal editorial.

### Search Bar
The search bar breaks from the standard input pattern: `{rounded.full}` pill on a soft gray surface (#f5f5f5), no border at rest. This visually separates search from form inputs throughout the checkout flow. The focus state adds a periwinkle border color matching the primary palette signal.

### Newsletter Stripe
The newsletter section is the site's most saturated surface — full periwinkle (#899df1) background with white Baskerville display-sm heading and Proxima Nova body-sm copy. The email input sits inline on desktop with a white-bordered ghost button; both stack vertically on mobile. This is the only full-brand-color full-bleed section and functions as a visual accent between content and footer.

### Footer
The footer reverses to the deepest black (#121212) — the only fully dark surface in the brand. Heading columns use title-sm Proxima Nova at 600 weight in white; link rows use body-sm. The contrast between the soft pastel palette above and the near-black footer below is the clearest page-end signal the layout provides, requiring no decorative elements.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + full-screen drawer; hero image stacks above text; category strip becomes horizontal scroll; newsletter input and button stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav shows condensed links without secondary categories; hero shifts to 50/50 image-text split |
| Desktop | 1128–1440px | Three to four column product grid; full nav visible; hero at full height with generous vertical padding |
| Wide | > 1440px | Max-width container (1440px) centered; side margins grow proportionally; product grid stays at four columns |

### Touch Targets
- All buttons minimum 44×44px
- Navigation links padded to 44px height on mobile drawer
- Swatch chips expand to 32px diameter on touch viewports
- Filter pill chips have 40px minimum height for reliable tap
- Cart and search icon buttons in nav bar always 44px

### Collapsing Strategy
- Desktop four-column product grid steps to three columns below 1128px
- Three columns step to two below 744px; editorial banners stay full-bleed at all widths
- Hero splits 50/50 on tablet and desktop; single-column stacked on mobile with image above copy
- Category strip scrolls horizontally on all viewports narrower than desktop; no truncation
- Footer column layout: four columns on desktop, two on tablet, one on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact interactive state styles (focus ring color, outline offset, keyboard navigation indicator) not extractable; periwinkle focus ring inferred from brand primary
- Precise letter-spacing values for Proxima Nova in nav and button contexts are estimated from visual inspection conventions, not extracted from CSS
- Sweet Sans Pro exact usage contexts (badge only vs. display applications) are inferred — confirmed as present in font stack but not confirmed per-component
- No dark-mode token set was detectable; Sugar Paper appears to operate in light mode only
- Animation easing curves and transition durations not extractable from static extraction
- Exact mobile breakpoint pixel values and grid gutter widths not confirmed from Shopify theme source
- Logo lockup details (wordmark only vs. wordmark + icon, exact sizing) not confirmed beyond font-stack extraction
- Hover shadow values for product cards estimated; exact box-shadow CSS not captured
