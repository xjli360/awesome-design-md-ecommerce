---
version: alpha
name: "Valley Rose"
source_url: "https://www.valleyrose.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Cormorant serifs carry the display weight here — set thin at 300–400 rather than bold, stretched across generous 56px headlines — while Work Sans handles body copy with the even-keeled reliability of a workshop label. The contrast defines the house voice: antique romance for product poetry, practical clarity for ring sizes and metal options. Valley Rose builds its visual field from warm earth — the deepest tone (#261818) reads like scorched timber, the signature brown (#5e4636) falls somewhere between walnut and dried terracotta, and the warmest canvas (#fff9f4) is less white than sun-bleached linen. Against this earthy continuum, a single coral-salmon voltage (#fb485e) cuts through for calls to action, darkening toward terracotta (#ae501c) on active states. The canvas hierarchy runs from warm near-white (#fcfbfa) to a peachy surface (#fbebdd) used beneath featured collection modules, lifting sections without leaving the warm register. `{rounded.xs}` governs form fields and product cards; the brand avoids pill shapes entirely — at this price tier, soft-but-precise signals craftsmanship rather than friendliness. A surprise periwinkle (#899df1) appears in accent elements and a bruised plum (#4b3048) surfaces on select editorial callouts, neither color load-bearing but both unmistakably intentional against the earth-tone field. Spacing runs wide: product grid gutters breathe at `{spacing.lg}`, section separators expand to `{spacing.section}`, and the brand never crowds a ring against its neighbor — the eye is expected to linger.

colors:
  primary: "#5e4636"
  primary-active: "#4b3613"
  primary-disabled: "#d1c6c6"
  cta: "#fb485e"
  cta-active: "#ae501c"
  cta-disabled: "#f5c6cc"
  ink: "#191919"
  body: "#555555"
  muted: "#777777"
  muted-soft: "#616161"
  hairline: "#dedede"
  hairline-soft: "#e9e7e7"
  canvas: "#fcfbfa"
  surface-soft: "#fff9f4"
  surface-card: "#f5f4f4"
  surface-warm: "#fbebdd"
  on-primary: "#fcfbfa"
  on-cta: "#ffffff"
  plum: "#4b3048"
  periwinkle: "#899df1"
  earth-mid: "#7c5336"
  earth-light: "#a67350"

typography:
  display-xl:
    fontFamily: "'Cormorant', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant', Georgia, serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Cormorant', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.28
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Work Sans', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.5px
  body-md:
    fontFamily: "'Work Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.42
    letterSpacing: 0.3px
  label-upper:
    fontFamily: "'Work Sans', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Work Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Work Sans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "monospace, 'Courier New', Courier"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  nav-link:
    fontFamily: "'Work Sans', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.8px
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
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.cta-active}"
    textColor: "{colors.on-cta}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.cta-disabled}"
    textColor: "{colors.on-cta}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.cta}"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.primary}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "4/5"
    padding: "{spacing.md}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price-display}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    hoverImageScale: 1.04
    transition: "transform 320ms ease"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    subColor: "{colors.body}"
    ctaComponent: "button-primary"
    minHeight: 580px
    imagePosition: right
    padding: "{spacing.section} {spacing.xl}"
  collection-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary}"
    headlineTypography: "{typography.display-md}"
    descTypography: "{typography.body-md}"
    descColor: "{colors.body}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl} {spacing.section}"
  badge-ethical:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.earth-light}"
    padding: 4px 12px
  badge-new:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  ring-sizer-widget:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-upper}"
    labelColor: "{colors.muted}"
    activeRingColor: "{colors.cta}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  metal-swatch:
    size: 28px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.primary}"
    borderInactive: "2px solid transparent"
    gap: "{spacing.xs}"
  stone-filter:
    backgroundColor: "{colors.surface-card}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 16px
  testimonial-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    quoteTypography: "{typography.display-sm}"
    authorTypography: "{typography.caption}"
    authorColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    headingColor: "{colors.on-primary}"
    dividerColor: "#7e5e49"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Square-cornered (`{rounded.none}`) CTA buttons in coral-salmon (`{colors.cta}`) with uppercase Work Sans tracking at 1px letter-spacing. Active states deepen to terracotta (`{colors.cta-active}`); disabled states fade to a pale coral (`{colors.cta-disabled}`). The 48px height ensures a confident tap target and the uppercase lettering at 14px reads as deliberate, not aggressive.

**`button-secondary`** — Transparent background with a 1px walnut-brown border and matching text in `{colors.primary}`; on hover, inverts to a solid brown fill with on-primary cream text. Same uppercase typographic treatment as primary, same 48px height. Used for secondary product actions — "Save to Wishlist," "Compare Metals," "View in AR."

**`button-text`** — Inline underlined text link in `{colors.ink}` at `{typography.button-sm}` scale. No background, no border. Appears in FAQ accordion bodies, policy footers, and editorial callouts.

### Form Inputs
**`text-input`** — Warm canvas background with a 1px hairline border that sharpens to `{colors.primary}` on focus. `{rounded.xs}` keeps corners barely-soft. Height 44px. Error state swaps the border to `{colors.cta}` — coral red functions as both accent and alert, keeping the error state inside the existing palette.

### Navigation
**`nav-bar`** — 64px tall, warm-canvas background with a subtle hairline bottom border. All links are uppercase Work Sans at 13px and 0.8px tracking (`{typography.nav-link}`), kept intentionally small against the Cormorant display headlines below — the contrast between the two weights and faces is the brand's primary typographic signal. On scroll, a faint box-shadow separates the bar from page content without changing its background. The wordmark renders in `{colors.primary}` brown.

### Product Cards
**`product-card`** — Portrait-ratio (4:5) imagery on `{colors.surface-card}` with `{rounded.xs}` corners. Product titles are set in Cormorant `{typography.display-sm}` — the brand's most distinctive card-level choice, lending ring names the gravity of a proper noun. Prices display in monospace `{typography.price-display}` for optically aligned numerals across a multi-column grid. On hover, the image scales to 1.04× over 320ms ease.

### Hero
**`hero`** — Full-width section on warm linen canvas (`{colors.surface-soft}`) with the headline in Cormorant display-xl at 56px, weight 300 — the lightest display weight in the system. The image aligns right; the CTA calls `button-primary`. Minimum 580px height ensures ring photography reads at appropriate scale before the fold.

### Collection Banner
**`collection-banner`** — A full-bleed peach-warm section (`{colors.surface-warm}`) used to introduce curated edits like "Sapphire Season" or "The Lab Diamond Edit." Headline in Cormorant 32px; body in Work Sans below. No rounded corners — the warmth of the background color does all the lifting.

### Badges
**`badge-ethical`** — Pill-shaped (`{rounded.full}`) on warm-white with an earth-light border and dark brown text in uppercase 11px Work Sans at 1.5px tracking. Used for "Lab Grown," "Ethical," "Conflict Free" callouts. **`badge-new`** — Same pill geometry in coral-salmon for product "New" labels, inheriting `{typography.label-upper}`.

### Ring Sizer Widget
**`ring-sizer-widget`** — A brand-signature conversion component for interactive ring sizing, rendered as a bordered canvas card at `{rounded.xs}`. Labels use `{typography.label-upper}` in muted gray; active size selections highlight in `{colors.cta}`. This widget is central to the purchase flow and should appear on every PDP above the add-to-cart button.

### Metal Swatches
**`metal-swatch`** — 28px circular swatches (`{rounded.full}`) representing metal options (yellow gold, rose gold, white gold, platinum). Active state gets a 2px `{colors.primary}` ring; inactive carries a transparent 2px border to prevent layout shift on selection. Swatches gap at `{spacing.xs}`.

### Stone Filter
**`stone-filter`** — Pill-shaped filter chips (`{rounded.full}`) for stone type: sapphire, white diamond, rose-cut, opal, salt-and-pepper. Inactive state is `{colors.surface-card}` with a hairline border; active fills to `{colors.primary}` walnut brown with reversed on-primary text. Used in collection sidebars and top filter bars.

### Testimonials
**`testimonial-card`** — Canvas card with hairline border and `{rounded.sm}` corners. Customer quote text uses Cormorant `{typography.display-sm}` — treating customer words with the same typographic weight as product names is deliberate brand positioning. Reviewer name follows in `{typography.caption}` muted gray.

### Footer
**`footer`** — Deep walnut-brown background (`{colors.primary}`) inverts the color logic: the only section where the brand brown becomes the field rather than the mark. On-primary cream text for all copy and links; section headings in `{typography.label-upper}`; links in `{typography.body-sm}`. A warmer mid-earth tone (#7e5e49) serves as column dividers.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks text above image; nav collapses to hamburger and centered wordmark; ring-sizer-widget expands to full viewport width; stone-filter scrolls horizontally; footer stacks to single column |
| Tablet | 744–1128px | 2-column product grid; hero maintains split layout at reduced image size; nav shows primary links, hides secondary; collection-banner padding reduces to `{spacing.xl}` |
| Desktop | 1128–1440px | 3–4 column product grid; hero at full 580px height with full display-xl headline; ring-sizer-widget inline with product options panel; all nav links visible |
| Wide | > 1440px | Grid maxes at 4 columns; outer gutters expand to center content at ~1440px max-width; no new layout changes beyond horizontal centering |

### Touch Targets
- button-primary and button-secondary: 48px height meets minimum target
- text-input: 44px height meets minimum target
- Metal swatches at 28px visual size require 44px tap-target padding applied via wrapper
- Stone-filter pills: minimum 36px height on mobile to prevent mis-taps
- Nav hamburger icon: minimum 44×44px touch area
- Product card tappable area covers the full card surface, not just the title row

### Collapsing Strategy
- Primary nav: full link row → hamburger at < 744px; wordmark stays centered on mobile
- Product grid: 4-col → 3-col at 1128px → 2-col at 744px → 1-col at < 480px
- Hero: side-by-side → stacked (text above, image below) at < 744px; display-xl drops to display-lg at < 480px
- Footer columns: 4-col → 2-col at 744px → 1-col at < 480px
- Stone-filter bar: horizontal scroll on mobile rather than wrapping, preserving card real estate
- Ring-sizer-widget: modal overlay triggered by tap on mobile vs. inline panel on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button corner radius not confirmed — `{rounded.none}` (0px) assumed from the sharp-edged visual aesthetic; the live site may use a minimal 2–4px radius that didn't surface in extraction
- Hover fill color for `button-secondary` inferred from palette; no direct computed-style evidence
- Monospace font usage context is confirmed in the font-family stack but specific placement (price only, or also ring size and carat callouts) requires deeper site inspection
- The periwinkle (#899df1) and plum (#4b3048) appear in extracted colors but their exact UI role — accent text, illustration tint, sale badge, or promotional banner — could not be determined; both assigned conservatively as named tokens without component assignments
- Animation durations (hover scale on product cards set to 320ms) are estimated; actual values require computed style inspection
- Mobile nav behavior — slide-in drawer vs. full-screen overlay vs. accordion — not confirmed
- Ring-sizer widget interaction model (dial, dropdown, printable guide, or AR measurement) requires direct inspection for full component fidelity
- Footer link hover color not extracted
