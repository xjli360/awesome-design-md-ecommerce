---
version: alpha
name: "Adele Dejak"
source_url: "https://adeledejak.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Burnt orange fires without ceremony — #ff6600 appears in a site otherwise built on near-black shadow (#1c1717) and warm cream parchment (#fcfaf7), a palette that performs the same register as hammered brass catching East African afternoon light. The jewelry itself is made by hand in Nairobi, scaled to be seen from across a room: collar pieces that read as architecture, earrings that occupy peripheral vision. The UI inherits this scale instinct — large product photography runs edge-to-edge against the cream canvas, with orange reserved exclusively for primary CTA surfaces and hover states, so it retains maximum charge. A secondary orange, #ff3300, deepens the active state without shifting hue, giving the interaction vocabulary a single-family warmth. The gray palette runs an unusually full eight steps — from #1c1717 through #797979, #aaaaaa, #d6d6d6, to #f2f2f2 — because the products are rich in material texture (bone, brass, resin, ebony), and the UI needs tonal range to describe them without competing. Off-white surfaces (#f8f0e7, #fffcf9) read like aged paper or pale ivory, nodding to the natural materials in the collection. Type is set without a detected custom webfont stack, defaulting to system typefaces, but the spacing and casing choices project conviction: widened letter-spacing on category labels, generous line heights on editorial copy. Buttons sit at sharp rectangular edges (`{rounded.none}`), carrying the same deliberateness as a hand-hammered edge — the brand refuses to soften its decisions or round its corners.

colors:
  primary: "#ff6600"
  primary-active: "#ff3300"
  primary-disabled: "#d6d6d6"
  ink: "#1c1717"
  body: "#404040"
  muted: "#797979"
  muted-soft: "#aaaaaa"
  hairline: "#d6d6d6"
  hairline-soft: "#ececec"
  canvas: "#fcfaf7"
  surface-soft: "#f8f0e7"
  surface-card: "#fffcf9"
  surface-mid: "#f2f2f2"
  on-primary: "#ffffff"
  dark-canvas: "#1c1717"
  on-dark: "#fcfaf7"
  charcoal: "#151515"
  mid-gray: "#969696"
  accent-blue-wash: "#dff3fd"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', 'Palatino Linotype', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.04em
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.08em
    textTransform: uppercase
  price:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  collection-label:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.15em
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoColor: "{colors.ink}"
  nav-bar-dark:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    logoColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageRatio: "4/5"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price}"
    categoryTypography: "{typography.collection-label}"
    categoryColor: "{colors.muted}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
    rounded: "{rounded.none}"
    hoverImageScale: 1.03
  hero-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    layout: fullbleed
    imageMode: "cover, object-position top"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 85vh
    contentPadding: "{spacing.xxl} {spacing.xl}"
    ctaComponent: button-primary
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    layout: "two-column: image left, text right"
    imageRatio: "3/4"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    rounded: "{rounded.none}"
  collection-banner:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-sm}"
    labelTypography: "{typography.collection-label}"
    labelColor: "{colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"
    rounded: "{rounded.none}"
  material-tag:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
    border: none
  craft-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    height: 44px
    iconColor: "{colors.muted}"
  product-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price}"
    bodyTypography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.xl}"
    addToCartComponent: button-primary
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    height: 36px
    padding: "{spacing.xs} {spacing.base}"
  footer:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.muted-soft}"
    borderTop: "1px solid {colors.muted}"
    padding: "{spacing.section} 0 {spacing.xl} 0"
  section-divider:
    color: "{colors.hairline}"
    thickness: 1px
    marginY: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Flat orange block (`{colors.primary}`, `{rounded.none}`) at 48px height with uppercase spaced lettering at 13px/0.12em. Active state deepens to `{colors.primary-active}` (#ff3300) without shifting hue; disabled collapses to `{colors.primary-disabled}` gray. The hard rectangular edge is intentional — it shares the register of a hand-stamped wax seal, uncompromising and final.

**`button-secondary`** — Same sharp rectangle, reversed: transparent fill with a 1px `{colors.ink}` border. On hover, the button floods solid dark (#1c1717), inverting text to `{colors.on-dark}`, echoing the site's own cream/dark zone switching and adding kinetic conviction to the interaction.

**`button-ghost`** — Transparent with a 1px `{colors.on-dark}` border and cream text, used as a secondary CTA wherever `hero-banner` or `collection-banner` dark grounds appear. Never appears on light surfaces.

### Navigation

**`nav-bar`** — 64px bar on warm cream canvas, all-caps links at 13px/0.08em tracking in `{typography.nav-link}`. A hairline bottom border (`{colors.hairline}`) separates it from the page. Switches to `nav-bar-dark` variant when overlaid on dark hero zones — charcoal ground, cream text and logo, no additional artwork swap required.

**`announcement-bar`** — 36px orange stripe pinned above the nav, used for shipping thresholds or limited-run alerts. Text in `{typography.button-sm}` centered. Because the orange is the brand's single hot voltage, this bar is used sparingly and never simultaneously with orange CTAs in the viewport.

### Product Display

**`product-card`** — Portrait 4:5 frame, no border radius, no drop shadow. Category label in `{typography.collection-label}` (11px, 0.15em, uppercase, `{colors.muted}`) prints above the title. Title in `{typography.body-md}`, price below in `{typography.price}` (Georgia serif, 18px). On hover, the image scales to 1.03× with a smooth transition; no overlay or text fade. Separation between cards comes from tonal ground colors, not borders.

**`product-detail-panel`** — Right-column panel on desktop (60/40 image/detail split), full-width below tablet. Title in `{typography.display-sm}` (Georgia 24px), price in `{typography.price}`, then a `{colors.hairline}` divider before material notes and provenance copy in `{typography.caption}` / `{colors.muted}`. Add-to-cart runs `button-primary` full-width. Size selectors use `material-tag` style chips.

**`material-tag`** — Flat `{colors.surface-mid}` chip with no border radius used to surface material type inline: "BRASS", "BONE", "RESIN", "EBONY". Type in `{typography.button-sm}`. Applied in product detail panels and collection filter bars. Minimum eight material values across the range.

**`craft-badge`** — `{colors.primary}` orange sharp badge reserved for handmade provenance callouts ("HANDMADE IN NAIROBI", "LIMITED EDITION"). Used at most once per viewport section to preserve the orange's signal value.

### Hero & Editorial

**`hero-banner`** — Full-bleed cover image at minimum 85vh with dark canvas (#1c1717) underneath. Headline in `{typography.display-xl}` (Georgia 48px), body in `{typography.body-md}`, CTA in `button-primary`. Content sits in the lower third with `{spacing.xxl}` top padding so jewelry photography can breathe above the text block.

**`hero-editorial`** — Two-column split: 3:4 image left, editorial copy right on `{colors.surface-soft}` (#f8f0e7). Headline in `{typography.display-md}` (Georgia 32px), body in `{typography.body-md}`. Used for collection stories, the designer's founding narrative, and craft process features. Stacks image above text below 744px.

**`collection-banner`** — Full-width dark band (`{colors.dark-canvas}`) with a `{typography.collection-label}` category string in `{colors.primary}` orange printing above the collection name in `{typography.display-sm}`. Functions as a section header between product grids, signaling category transitions without needing photography.

### Footer

**`footer`** — Deep charcoal ground (`{colors.charcoal}`, #151515) with `{colors.on-dark}` link text and `{colors.muted-soft}` (#aaaaaa) section labels in `{typography.title-sm}`. Four-column layout on desktop collapses to labeled accordions on mobile. A hairline (`{colors.muted}`) rules the top edge. Brand mark centered at the base in cream.

### Search

**`search-bar`** — Inline expanding field at nav-right on desktop (44px height, `{rounded.none}`, hairline border at rest, ink border on focus). On mobile becomes a full-width takeover. Icon in `{colors.muted}` at rest, `{colors.ink}` on active.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline steps down to `display-md` scale; `hero-editorial` stacks image above text full-width; footer columns become labeled accordions |
| Tablet | 744–1128px | Two-column product grid; `hero-editorial` stays two-column at reduced proportions; nav shows primary collection links, secondary links behind overflow menu |
| Desktop | 1128–1440px | Three- to four-column product grid; `product-detail-panel` runs 60/40 image/detail split; full four-column footer |
| Wide | > 1440px | Grid max-width clamps ~1440px, warm canvas bleeds on sides; hero content column narrows to ~640px to preserve editorial line length |

### Touch Targets

- All buttons minimum 48px height; `button-primary` and `button-secondary` expand to full width on mobile
- `material-tag` and `craft-badge` minimum 36px tap height on mobile via added vertical padding
- Nav hamburger minimum 44×44px tap area
- Product card tap target covers the full card surface including image and text block, not title text alone
- Footer accordion headers minimum 48px height on mobile

### Collapsing Strategy

- Navigation: top-level collection categories collapse into a hamburger drawer below 744px; search moves to drawer header row
- Footer: four-column layout folds to labeled accordions; each section label is a 48px tap target
- `hero-editorial`: image moves above text at < 744px; text block takes full width with `{spacing.xl}` horizontal padding
- Product grid: 4-col → 3-col at 1128px → 2-col at 744px → 1-col at 480px
- `collection-banner` type steps down one level on mobile (display-sm sizing → title-md equivalent) to prevent headline overflow
- `announcement-bar` text truncates to a single short message on mobile if copy exceeds one line

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Custom webfonts not detected**: No font-family declarations were extractable from the live site. Typography stacks default to Georgia (serif display) and system-ui (body/UI). The brand likely uses a licensed or self-hosted typeface; inspect rendered CSS and override all `fontFamily` fields once confirmed.
- **Exact brand typeface unknown**: Adele Dejak's editorial positioning suggests a refined serif or distinctive contemporary sans; confirmed font name, weights, and optical sizes unavailable from static extraction.
- **Icon set not catalogued**: Cart, wishlist, hamburger, and social icons not captured; stroke weight, style (line vs. filled), and size scale unconfirmed.
- **Animation and transition values**: Hover durations, page-load sequences, image fade behavior, and scroll-triggered reveals not captured by static extraction.
- **Accent blues (#dff3fd, #91dbff) origin unclear**: These cool-blue tones appear in the extracted palette but likely belong to a third-party widget overlay (live chat, cookie consent, or a Shopify app) rather than the brand design system. Excluded from primary palette; verify before using anywhere in brand UI.
- **Grid gutter and column margins**: Exact gutter widths inferred from Shopify Dawn theme defaults rather than directly extracted; measure against live product grid before implementing.
- **Dark/light section logic**: Whether the site uses a user-preference toggle or hardcodes cream/dark ground switching per editorial section is unconfirmed from extraction alone.
