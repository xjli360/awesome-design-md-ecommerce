---
version: alpha
name: "Massimo De Carlo"
source_url: "https://www.massimodecarlo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  ABCROM runs every line on massimodecarlo.com without variation — one family, near-zero weight deviation below 700, covering everything from 10px location labels to 80px hero exhibition titles. That typographic conservatism is the design signature: the site behaves as if the artwork cannot coexist with a competing type personality, so ABCROM stays almost invisible, a neutral vessel for whatever Cattelan or Stingel or Urs Fischer occupies the frame. The color extraction surfaces a white-cube restraint — #000000 as the carrying theme, #a3a3a3 as the only gray used at scale — but interrupts that austerity with a single operative orange at #ff901b, which appears on interactive highlights and navigation states with an abruptness that reads less like a brand decision and more like a deliberate aesthetic intrusion. Components ship with no radius: zero border-radius everywhere from buttons to cards to form fields, matching the gallery's physical language of planed concrete floors and unadorned walls. Spacing is generous at the section scale (64–96px between content blocks) and tight in inline clusters (4–8px within caption groups), mimicking the compressed hang of a gallery that uses distance between works as editorial argument. Artwork cards suppress pricing entirely in browse mode, surfacing only dimensions and medium — the gallery's way of signaling that inquiring is the transaction, not a checkout flow. The Shopify layer sits almost entirely beneath the surface: the add-to-cart mechanism exists for publications and editions, but it inherits the same zero-radius, ink-on-white austerity as every other surface. Location — Milan, London, Hong Kong, Brussels — toggles in the nav without page reload, each city effectively a filtered view of the same global program. Monospace appears only in timestamp and catalog-number contexts, a rare textural intrusion that marks archival data rather than editorial prose.

colors:
  primary: "#000000"
  primary-active: "#1a1a1a"
  primary-disabled: "#a3a3a3"
  accent: "#ff901b"
  accent-active: "#e07800"
  alert: "#ff1b1b"
  alert-dark: "#cf0000"
  success: "#116600"
  ink: "#000000"
  body: "#1a1a1a"
  muted: "#a3a3a3"
  hairline: "#d4d4d4"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#007aff"

typography:
  display-xl:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 80px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -0.02em
  display-lg:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.01em
  display-md:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.01em
  display-sm:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  caption-sm:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.02em
  catalog-number:
    fontFamily: "monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  nav-label:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  location-tag:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  artist-name-display:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.02em
  button-sm:
    fontFamily: "'ABCROM', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.03em

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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    paddingBlock: 11px
    paddingInline: 0
    border: none
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 0
    border: none
    borderBottom: "1px solid {colors.hairline}"
    focusBorderBottom: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 56px
    padding: 0 32px
    logoTypography: "{typography.title-md}"
    locationTypography: "{typography.location-tag}"
    activeLocationAccent: "{colors.accent}"
    scrollBorder: "1px solid {colors.hairline}"
  location-switcher:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.location-tag}"
    activeAccentBorder: "{colors.accent}"
    gap: "{spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
    height: 40px
  artwork-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "4/5"
    rounded: "{rounded.none}"
    padding: 0
    captionGap: "{spacing.sm}"
    artistTypography: "{typography.body-sm}"
    titleTypography: "{typography.body-sm}"
    titleStyle: italic
    detailTypography: "{typography.caption}"
    detailColor: "{colors.muted}"
    catalogTypography: "{typography.catalog-number}"
    hoverOverlay: none
  exhibition-hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    imageMode: full-bleed
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    dateTypography: "{typography.location-tag}"
    dateColor: "{colors.muted}"
    overlayOpacity: 0
    textPosition: bottom-left
    padding: "{spacing.xxl} {spacing.xl}"
    minHeight: 100vh
  artist-page-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.display-md}"
    bioTypography: "{typography.body-md}"
    bioMaxWidth: 680px
    padding: "{spacing.section} {spacing.xl}"
  press-release:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    maxWidth: 720px
    padding: "{spacing.xxl} {spacing.xl}"
    leadTypography: "{typography.display-sm}"
    dateLabelTypography: "{typography.location-tag}"
    dateLabelColor: "{colors.muted}"
  edition-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "1/1"
    rounded: "{rounded.none}"
    captionGap: "{spacing.sm}"
    artistTypography: "{typography.body-sm}"
    titleTypography: "{typography.body-sm}"
    titleStyle: italic
    priceTypography: "{typography.caption}"
    priceColor: "{colors.ink}"
    ctaTypography: "{typography.button-sm}"
  inquiry-form:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    inputBorderBottom: "1px solid {colors.hairline}"
    inputFocusBorderBottom: "1px solid {colors.ink}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
    privacyTypography: "{typography.caption-sm}"
    privacyColor: "{colors.muted}"
  fair-listing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    fairNameTypography: "{typography.title-sm}"
    dateTypography: "{typography.caption}"
    dateColor: "{colors.muted}"
    locationTypography: "{typography.caption}"
    boothTypography: "{typography.catalog-number}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    linkTypography: "{typography.caption}"
    columnGap: "{spacing.lg}"
    padding: "{spacing.section} {spacing.xl}"
    copyrightTypography: "{typography.caption-sm}"
    copyrightColor: "{colors.muted}"
    inputBorderBottom: "1px solid {colors.on-dark}"

## Components

### Buttons

**`button-primary`** — Full black fill (`{colors.primary}`) with white text and zero border radius, matching the gallery's physical language of unadorned surfaces. Padding is 12px vertical and 24px horizontal at 44px height. Active state deepens to `{colors.primary-active}` (#1a1a1a). Disabled uses `{colors.primary-disabled}` (#a3a3a3) without cursor feedback — the gallery prefers to suppress unavailable actions rather than render them visibly disabled.

**`button-secondary`** — White fill with a 1px solid black outline at zero radius, serving as the outline companion for secondary CTAs such as "View Exhibition" and "Download Press Release." No fill shift on hover; only the border weight increases to 2px to signal press.

**`button-ghost`** — Transparent background with a single `borderBottom: 1px solid {colors.ink}` in place of any container. Used for inline text CTAs ("Read More," "Biography," "All Works") where the underline reads as editorial annotation rather than button chrome. No padding block — the underline runs flush to the text baseline.

### Navigation

**`nav-bar`** — 56px tall on a white background, with the wordmark MASSIMODECARLO set in `{typography.title-md}` left-anchored. The right cluster carries location tabs in `{typography.location-tag}` uppercase; the active city gains a bottom-border in `{colors.accent}` (#ff901b), the only orange visible above the fold. On scroll a 1px `{colors.hairline}` border materializes at the bar's bottom edge. Mobile collapses to wordmark plus hamburger icon at the same 56px height without any visible condensation of the wordmark.

**`location-switcher`** — A 40px sub-row beneath the primary bar displaying city names in `{typography.location-tag}`. Inactive cities render in `{colors.muted}` (#a3a3a3), the active city in full `{colors.ink}` with an `{colors.accent}` underline stripe. Clicking a city filters the page's content region in place — no navigation, no page reload. Below 1128px this row is absorbed into the hamburger menu as a nested list.

### Artwork Card

**`artwork-card`** — The primary content unit across exhibitions, artists, and the Shopify catalog. The image occupies a 4:5 ratio with no padding, border, or shadow. The caption block below uses an 8px gap: artist name in `{typography.body-sm}` regular, title in `{typography.body-sm}` italic, then medium, dimensions, and year in `{typography.caption}` muted. Catalog or edition reference numbers appear in `{typography.catalog-number}` monospace when present — the only moment a non-ABCROM face appears in the card. No hover overlay, no price display, and no add-to-cart affordance in browse mode; those surfaces emerge only within the editions and publications sections.

### Exhibition Hero

**`exhibition-hero`** — Full-bleed image at 100vh on desktop, 60vh on mobile, with `{typography.display-xl}` exhibition title positioned bottom-left at 24px above the image edge. No gradient overlay or scrim — the gallery trusts the photograph's compositional weight to hold legible text. Subtitle appears on the line below in `{typography.display-sm}`. Date range and location read as a third row in `{typography.location-tag}` uppercase at `{colors.muted}` where contrast allows. The carousel pagination, if present, uses minimal dot indicators at 6px diameter in white, no numeric labels.

### Artist Page Header

**`artist-page-header`** — Full-width white region with the artist's name at `{typography.display-md}` and a prose biography constrained to 680px max-width in `{typography.body-md}` at 1.6 line-height for extended reading. Generous padding of `{spacing.section}` top and bottom creates the visual breathing room of a gallery wall. No headshot, no pull quote, no decorative rule — just name and text in the same proportional relationship as a wall card beside a major work.

### Press Release

**`press-release`** — A constrained reading column centered on canvas white at max-width 720px. The exhibition title or lead statement renders in `{typography.display-sm}` at 400 weight. Body prose runs in `{typography.body-md}` at 1.6 line-height. Exhibition date and location appear as a `{typography.location-tag}` uppercase annotation above the headline in `{colors.muted}`. No pull quotes, sidebars, or image interruptions — the component is entirely typographic, consistent with the gallery's print press-release convention.

### Inquiry Form

**`inquiry-form`** — A light-surface (`{colors.surface-soft}`) overlay panel, zero border-radius, typically entering from the right side as a sheet over the artwork detail page. Input fields are underline-only: a 1px `{colors.hairline}` bottom border sharpens to `{colors.ink}` on focus, with no bounding box. Field labels in `{typography.caption}` `{colors.muted}` float above on fill. Submit maps to a full-panel-width black button using `{colors.primary}` fill and `{typography.button-md}`. A privacy note in `{typography.caption-sm}` sits below the submit in `{colors.muted}`.

### Fair Listing

**`fair-listing`** — A bare horizontal row separated by `{colors.hairline}` top borders, no card container or shadow. Fair name in `{typography.title-sm}`, dates in `{typography.caption}` muted, booth designation in `{typography.catalog-number}` monospace, and city label in `{typography.caption}` muted. Padding is 24px top and bottom per row. Active or upcoming fairs carry no special color treatment — recency is communicated by position at the top of the list, not accent color.

### Edition Card

**`edition-card`** — A square-format (1:1) variant of the artwork card used for print editions, multiples, and publications available through the Shopify layer. Same caption structure as the artwork card but appends a price line in `{typography.caption}` `{colors.ink}` and a discreet "Add to Cart" text link in `{typography.button-sm}` below. The add-to-cart link is deliberately low-contrast against the catalog metadata — commerce is present but does not compete with the art object.

### Footer

**`footer`** — Full black background (`{colors.primary}`) with white text throughout. A grid of four columns covers gallery contact, location addresses, social links, and a newsletter sign-up. All text runs `{typography.caption}` `{colors.on-dark}`; links underline on hover with no color shift. The newsletter input field inverts the inline form treatment: a white bottom-border on black, with a white "Subscribe" text label — no button container, no rounded affordance. Copyright in `{typography.caption-sm}` renders at reduced opacity in `{colors.muted}` against the black ground.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to wordmark + hamburger; exhibition hero drops to 60vh; artwork cards one-per-row; press release full-width with 16px gutters; location-switcher absorbed into hamburger menu |
| Tablet | 744–1128px | Two-column artwork grid; nav shows location tabs but collapses artist/exhibition dropdowns to accordion; hero at 80vh; inquiry form occupies full-width overlay rather than side panel |
| Desktop | 1128–1440px | Three-to-four column artwork grid; full nav with hover dropdowns; location-switcher sub-nav visible as persistent row; inquiry form opens as right-side panel overlay at ~480px width |
| Wide | > 1440px | Content max-width 1440px centered on body; artwork grid scales to four-to-five columns; hero title scales up via fluid clamp from display-xl through a larger step; section padding increases to 96px |

### Touch Targets

- All nav and location-switcher items padded to a minimum 44px tap height despite their compact visual size at 10–13px type
- Artwork card touch target is the entire card face including image — no separate label tap zone
- Inquiry open trigger on artwork detail pages is a full-width button row at minimum 44px height
- Fair listing rows use a 56px minimum row height on mobile regardless of visual padding to prevent misfire

### Collapsing Strategy

- Primary nav collapses last: wordmark survives at all breakpoints, full desktop nav persists down to 1128px
- Location-switcher sub-row disappears below 1128px, replaced by a nested city list inside the hamburger menu
- Press release column fixed at 720px on desktop, full-bleed with 16px gutters on mobile
- Hero display typography scales via fluid clamp: display-xl (80px) at wide breakpoints reduces to display-md (40px) at mobile — weight stays 400 throughout
- Artwork grid degrades 4→3→2→1 columns across breakpoints without reflow of the caption block structure

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Color extraction surfaced several system-level values (#007aff is Safari/iOS default link blue, likely not a brand token); #ff901b and #a3a3a3 appear most likely to be intentional brand choices, but direct CSS custom-property inspection would confirm
- ABCROM is a proprietary typeface; its full weight and variant inventory — including italic cuts, condensed widths, and variable axes — is not publicly documented; weights above 500 are estimated from visual inspection
- Shopify theme CSS was filtered during extraction; button, cart-drawer, and form-field specifications in the commerce layer may differ from the gallery editorial components above
- Swiper carousel (swiper-icons font stack present) is confirmed but component specifics — navigation arrow style, dot size, autoplay timing, and slide transition easing — were not captured
- Dark-mode behavior is unconfirmed; the #000000 meta theme-color may indicate a dark-header variant rather than a full dark-mode token set; no dark canvas surface tokens are defined here
- Exact column gap values and max-width grid constraints require direct computed-style inspection
- Page transition and hover animation timing (exhibition image fade, artist name reveal, artwork-card enter) not captured from extraction
