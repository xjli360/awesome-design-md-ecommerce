---
version: alpha
name: "Terrapin Stationers"
source_url: "https://terrapinstationers.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Before a single typeface loads, #121212 on #ffffff states the brand's entire thesis — ink on paper, compressed into the two extracted hex values and nothing else. Terrapin Stationers operates as a division of GHP Media, Inc., a print-heritage company, and that origin shows in every layout decision: this is a digital catalog built by people who arrived from paper, not toward it. The silver-gray #dedede does structural load-bearing throughout as `{colors.hairline}`, edging every input field, product card, and section divider so the `{colors.canvas}` white breathes without a second accent color competing for attention. Corners hold as close to flat as interaction allows — `{rounded.xs}` on buttons and inputs at most, `{rounded.none}` on all cards — echoing the precise cut-edge geometry of a blank correspondence card or a perfectly folded broadside. Display headings earn their authority from a serif face at `{typography.display-md}` scale, borrowing editorial weight from print convention; navigation and secondary labels run in compact sans at `{typography.nav-label}` with tracking opened slightly, evoking the reference-number precision of a print specification sheet. Primary CTAs fill entirely with `{colors.primary}` and reverse to `{colors.on-primary}` white type; secondary actions invert the field to white with an `{colors.ink}` border, maintaining the strict two-tone grammar through every interactive state. A full-width announcement bar in `{colors.primary}` with reversed type is the brand's single moment of chromatic density at the top of each page; below that line, `{spacing.section}` row gaps let product photography carry the argument without copy competition. The footer mirrors that dark inversion to close the layout in the same register it opened — black band top, white body, black band bottom — a compositional format approximately four centuries older than any CSS specification.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#909090"
  ink: "#121212"
  body: "#3d3d3d"
  muted: "#767676"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-label:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  badge:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 46px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 46px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    paddingHorizontal: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.md}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.nav-label}"
    linkTypography: "{typography.body-sm}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 40px
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingBottom: "{spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

## Components

### Buttons

**`button-primary`** — Filled #121212 with uppercase reversed type at 13px/0.08em tracking; the uppercase letter-spacing is the only visual decoration, leaning into the precision of a print-shop imprint rather than a consumer CTA. On `:active` the background deepens to `{colors.primary-active}` true black; on `:disabled` it recedes to `{colors.primary-disabled}` mid-gray while retaining the reversed white type.

**`button-secondary`** — White canvas field with a 1px `{colors.ink}` border and matching uppercase sans type; on hover the background lifts to `{colors.surface-soft}` to signal receptivity without breaking the two-tone grammar. The border weight stays constant across states so the outline never reads as decorative.

**`button-text`** — Inline underlined uppercase link used for tertiary actions such as "View all" within collection rows and "Continue shopping" dismissals. No background, no border; the underline is the only affordance, consistent with editorial typesetting convention.

### Text Input

**`text-input`** — White field with a 1px `{colors.hairline}` border at rest; on focus the border upgrades to 1px `{colors.ink}` without shadow or glow, communicating active state through the same color vocabulary as the rest of the UI. Placeholder text should be `{colors.muted}` at `{typography.body-md}` weight. Error state replaces the border with the same `{colors.ink}` at full opacity and appends a `{typography.caption}` error line below.

### Nav Bar

**`nav-bar`** — 64px white bar with a 1px `{colors.hairline}` bottom border; navigation links in uppercase `{typography.nav-label}` with 0.06em tracking so the category names read as signage headers rather than conversational copy. Logo anchors left; search, account, and cart icons anchor right. On scroll, the bar stays fixed and the bottom border becomes the only separation from page content.

### Product Card

**`product-card`** — Flat rectangular card with no border-radius; a 1px `{colors.hairline}` perimeter border on all four sides distinguishes it from the white canvas without introducing shadow depth. Product name in `{typography.title-sm}` sits below the image at `{spacing.md}` padding; price in `{typography.price-display}` follows immediately beneath. Hover state adds no transform or shadow — the only interactive signal is a cursor change — preserving the static, catalog-page quality. Cards tile in a 4-column grid on desktop, reducing to 2 on mobile.

### Hero

**`hero`** — White canvas section with a `{typography.display-xl}` serif headline, an optional `{typography.body-md}` sub-copy line, and a single `{component.button-primary}` CTA. Minimum height 480px; content centers vertically in the block. A 1px `{colors.hairline}` bottom border separates the hero from the first collection row, maintaining the broadsheet column-rule aesthetic. Product photography is placed as a right-anchored image on desktop and stacks above the text column on mobile.

### Announcement Bar

**`announcement-bar`** — Full-width 36px strip in `{colors.primary}` reversed to `{colors.on-primary}` white, pinned above the nav bar. `{typography.caption}` centered type carries shipping thresholds, sale notices, or new-arrival announcements. The dark bar functions as the page's top margin line, the visual equivalent of a newspaper's masthead rule. No dismiss control by default; it persists across all pages.

### Footer

**`footer`** — Inverted `{colors.primary}` background with `{colors.on-primary}` reversed type mirrors the announcement bar, closing the broadsheet frame. Column headings in `{typography.nav-label}` uppercase with 0.06em tracking; link lists in `{typography.body-sm}` at reduced opacity (~70%) to distinguish navigational links from the heading level. `{spacing.section}` top and bottom padding. The footer's dark field echoes the announcement bar directly so the page, viewed at any scroll depth, shows the same chromatic signature at both extremes.

### Search Bar

**`search-bar`** — 40px `{colors.surface-soft}` field with a 1px `{colors.hairline}` border; a magnifying-glass icon inset left; `{typography.body-md}` placeholder text in `{colors.muted}`. On focus, the border upgrades to 1px `{colors.ink}`. Typically rendered inline in the nav bar on desktop and expanded to full-width on mobile as a modal overlay. No `{rounded.full}` pill — the corner stays at `{rounded.xs}` to preserve the rectangular language.

### Collection Header

**`collection-header`** — Serif `{typography.display-md}` headline followed by optional `{typography.body-md}` description copy in `{colors.body}`. A 1px `{colors.hairline}` bottom border underlines the block before the product grid begins, functioning as the column rule that separates editorial from catalog in print design. No background tint; section sits on the raw `{colors.canvas}`.

### Product Badge

**`product-badge`** — Small `{colors.primary}` pill at `{rounded.xs}` with `{typography.badge}` uppercase reversed type; used for NEW, SALE, and PERSONALIZE labels overlaid on the product card image at top-left. The rectangular corner keeps badges from reading as playful stickers; they read as stamps. Maximum one badge per card at a time to avoid visual noise.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart; hero image stacks above text; footer columns stack vertically; search expands to full-width overlay |
| Tablet | 744–1128px | Two-column product grid; nav shows condensed inline links or hybrid hamburger; hero uses 60/40 text/image split |
| Desktop | 1128–1440px | Four-column product grid; full nav bar at 64px; hero at full 480px minimum height with right-anchored image |
| Wide | > 1440px | Max content width capped at 1440px with centered layout; side gutters in `{colors.canvas}` white; product grid remains four columns |

### Touch Targets

- All buttons minimum 46px height; icon-only buttons (cart, account, search) minimum 44×44px tap target
- Product cards use full-card tap area, not just title text
- Nav hamburger icon minimum 44×44px with adequate padding
- Footer links minimum 36px line-height for comfortable tap spacing

### Collapsing Strategy

- Primary nav collapses at 744px into a slide-in drawer with the same uppercase `{typography.nav-label}` links stacked vertically
- Announcement bar text truncates with ellipsis below 375px rather than wrapping to two lines
- Collection header description copy hides on mobile; only the `{typography.display-sm}` headline remains to preserve scan speed
- Footer four-column grid collapses to single column with accordion-toggled link sections at mobile widths
- Product card titles truncate to two lines with `line-clamp: 2` at all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No fonts extracted** — the site likely loads its typeface stack via JS or a third-party theme file that was not accessible to the extractor. The serif/sans system-stack fallbacks used here (Georgia, system-ui) are inferred from stationery-catalog convention, not observed values. Actual font families should be confirmed against the live Shopify theme assets.
- **Only two hex values extracted** (#dedede, #121212) — the full palette including any accent colors, sale-price reds, success greens, or hover states could not be confirmed. All intermediate tones (body, muted, surface-soft, etc.) are derived mathematically from the two anchors rather than observed.
- **No meta theme-color** — mobile browser chrome color unknown; defaulting to `{colors.canvas}` white is a safe assumption but unverified.
- **No icon system documented** — nav icons (search, account, cart), social icons in footer, and any product-category glyphs are unextracted. Style (line-weight, filled vs. outline) is inferred as thin-stroke outline consistent with the minimal two-tone palette.
- **Personalization UI unknown** — as a stationery brand, customization flows (monogram input, foil color picker, quantity/paper-stock selectors) are likely present but their component patterns could not be observed.
- **Animation and transition values not extracted** — hover durations, drawer slide timing, and any page-transition conventions are undocumented.
