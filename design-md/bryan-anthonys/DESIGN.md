---
version: alpha
name: "Bryan Anthonys"
source_url: "https://www.bryananthonys.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The laminated story card folded into every Bryan Anthonys gift box is what separates this brand from the category — before a wearer puts on the piece, she reads a poem. That narrative-first identity saturates every screen: a warm ivory canvas (#fcfbf9) that reads like uncoated paper stock, editorial Baskerville serifs carrying emotional headline copy in gentle italics, and a singular house gold (#ab8c52) that pulls every primary action — add-to-cart fills, price callouts, and hover transitions. This gold is deliberately muted, closer to hammered brass or an oxidised finish than reflective karat shine; its pressed register (#806430) handles active button states, its palest echo (#e8d4ae) washes over disabled elements and background chips, and the mid-tone sibling (#9a7e4a) surfaces in secondary icon highlights. A quiet teal (#108474) functions as the brand's only departure from the warm palette — reserved for trust-building moments like shipping confirmations, in-stock badges, and loyalty callouts — and never overlaid on product photography, where the cream registers (#f5f2ec, #f0ebe2, #f7f4ef) hold uninterrupted. Body text lands at deep charcoal (#212121) rather than pure black, with a softer secondary register at #555555 for supporting copy and hairlines at #dfdcd4 that nearly dissolve into the warm canvas.

  Type stages a studied contrast between a Baskerville serif and a geometric sans. Baskerville at weight 400 — often italicised — carries display headlines and story-card prose in a register lifted from a literary quarterly rather than a product catalog; it is the voice of the narrative layer. Jost handles all UI chrome: navigation labels, button text, overlines, and filter chips sit at wide letter-spacing (0.08–0.15em), lending the sans-serif a composed, editorial quality. Nunito Sans provides the readable body face for product descriptions and cart copy at a comfortable 15px / 1.6 line-height. Button labels are sentence-case and padded generously inside a `{rounded.sm}` container at just 4px — the brand stops well short of pill shapes, which would read as too playful against the romantic, reflective tone. Product cards carry a warm surface wash (#f7f4ef) and `{rounded.md}` at 8px, enough to soften without competing with the imagery. The one exception to the restrained-radius rule is the collection filter chip, which uses `{rounded.full}` to mark interactive filtering as categorically distinct from all editorial content.

colors:
  primary: "#ab8c52"
  primary-active: "#806430"
  primary-disabled: "#e8d4ae"
  primary-muted: "#9a7e4a"
  accent-teal: "#108474"
  accent-teal-soft: "#aecfb8"
  ink: "#212121"
  body: "#2e2e2e"
  muted: "#555555"
  muted-soft: "#636262"
  hairline: "#dfdcd4"
  hairline-soft: "#ece7db"
  canvas: "#fcfbf9"
  surface-soft: "#f5f2ec"
  surface-card: "#f7f4ef"
  surface-warm: "#f0ebe2"
  on-primary: "#ffffff"
  star-gold: "#fbcd0a"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Baskerville Old Face', 'Book Antiqua', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Karla', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.06em
  title-sm:
    fontFamily: "'Jost', 'Karla', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.05em
  body-md:
    fontFamily: "'Nunito Sans', 'Karla', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Karla', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', 'Karla', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  overline:
    fontFamily: "'Jost', 'Karla', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', 'Karla', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.08em
  button-sm:
    fontFamily: "'Jost', 'Karla', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.08em
  nav-link:
    fontFamily: "'Jost', 'Karla', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1em
  story-body:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.7
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: 10px 16px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceColor: "{colors.primary}"
    priceTypography: "{typography.title-sm}"
    nameTypography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    imageRadius: "{rounded.md}"
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  story-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    overlineColor: "{colors.primary}"
    overlineTypography: "{typography.overline}"
    bodyTypography: "{typography.story-body}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  gift-message:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    borderTop: "2px solid {colors.primary}"
    labelTypography: "{typography.overline}"
    bodyTypography: "{typography.story-body}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  collection-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  badge-bestseller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  trust-badge:
    backgroundColor: "{colors.accent-teal-soft}"
    textColor: "{colors.accent-teal}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 12px
  footer:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    headlineTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The primary CTA fills with house gold (#ab8c52) and renders white text in Jost 14px at wide tracking via `{typography.button-md}`, sitting on 4px `{rounded.sm}` corners that read refined rather than playful. On press the fill deepens to the active gold (#806430); the disabled state washes to pale gold (#e8d4ae) with muted body text, maintaining the warm hierarchy even when the action is unavailable. Used universally for add-to-cart, checkout, and newsletter subscribe.

**`button-secondary`** — A canvas-fill, gold-bordered outline button that pairs with `button-primary` in two-CTA moments such as "Add to Cart" alongside "Add to Wishlist." The 1px primary-gold border keeps visual weight minimal against the warm canvas; hover transitions the border to `{colors.primary-active}` without filling the background, preserving the ghost aesthetic.

**`button-ghost`** — A bare text-link styled in `{typography.button-md}` with a simple underline, used for low-commitment navigation actions like "Continue Shopping" or "View All." No background, no border, no height constraint — lets the warm surface show through entirely.

### Inputs

**`text-input`** — A 48px tall field with a hairline (#dfdcd4) border that sharpens to primary gold on focus, confirming the brand touch-point even within a form. Placeholder runs in `{colors.muted-soft}` at `{typography.body-md}`; Nunito Sans keeps reading comfortable at small sizes across newsletter, search, and checkout contexts.

**`search-bar`** — A compact 40px variant tinted with the surface-soft background (#f5f2ec) rather than canvas white, designed to sit inside the nav drawer or collection-page header without creating a contrast break. Shares the same focus-gold border treatment as `text-input`.

### Navigation

**`nav-bar`** — The top bar sits at 64px on canvas white with a feather-light hairline-soft border (#ece7db) along the base. Navigation labels run in Jost 13px / 0.1em tracking — the same wide-tracking register as filter chips — giving the entire UI chrome a unified, composed cadence. A persistent cart icon and the brand wordmark in the primary gold anchor opposite ends of the bar.

### Product

**`product-card`** — Cards sit on the warm surface-card tone (#f7f4ef) with `{rounded.md}` at 8px and a single `{spacing.base}` padding on all sides. Product names render in Nunito Sans `{typography.body-md}`, and the price is highlighted in primary gold via `{typography.title-sm}` — a deliberate cue that links the price disclosure to the primary brand action color. Hover state lifts the card with a soft shadow; no border or background transition occurs, keeping the animation quiet.

**`badge-bestseller`** — A small uppercase overline label in primary gold floated to the top-left corner of the product image. The `{rounded.xs}` (2px) radius prevents it from reading as a chip; it reads more like a press sticker or hallmark stamp, consistent with the brand's editorial positioning.

**`badge-new`** — Same geometry as `badge-bestseller` but with an ink (#212121) fill, visually distinguishing "new arrival" from "popular" at a glance without introducing a third brand color.

**`collection-chip`** — Pill-shaped filter chips (`{rounded.full}`) for browsing by collection, metal, or price range. Default state is canvas-fill with a hairline border; the selected state inverts to a primary gold fill with white text in `{typography.caption}`. The full-radius pill is intentionally the only such shape in the system, marking collection filtering as an interactive affordance categorically distinct from all editorial or commerce elements.

### Brand-Signature Components

**`story-card`** — The brand's most distinctive component, echoing the physical insert card shipped with every order. A surface-soft (#f5f2ec) background with a 1px hairline border contains an uppercase Jost overline in primary gold — the piece title or thematic label — followed by the symbolic narrative in italic Baskerville at `{typography.story-body}` (16px / 1.7 line-height). This component appears in PDP sidebars, editorial landing pages, collection openers, and email headers, and is the primary vehicle through which meaning is communicated alongside product imagery.

**`gift-message`** — Surfaces in cart and checkout as a surface-soft panel with a 2px primary-gold top border acting as an accent rule and a hairline-soft perimeter border. The label runs in `{typography.overline}` and the message body in italic `{typography.story-body}`, reinforcing the handwritten, personal aesthetic of gift-giving. The overriding top border in gold is the one moment in the system where the primary color appears as a line rather than a fill, signalling warmth without weight.

**`trust-badge`** — A soft teal chip ({colors.accent-teal-soft} background, {colors.accent-teal} text) in `{typography.caption}` used for "Free Shipping Over $75," "Authenticity Guaranteed," and "30-Day Returns." The teal is the only cool-hue element in the system, making these reassurance markers immediately distinct from all editorial and commerce elements without breaking the warm canvas.

**`hero-banner`** — A full-width section on the surface-warm cream (#f0ebe2) background, headlined in italic Baskerville `{typography.display-xl}` (48px) with a subhead in Nunito Sans `{typography.body-md}`. The warm background eliminates any need for a dark overlay on lifestyle photography — images sit adjacent to the text column rather than behind it, preserving legibility while holding the uncoated-paper warmth across the entire viewport.

**`footer`** — Rendered on the surface-warm (#f0ebe2) background with a hairline top border, the footer column headers run in Jost `{typography.title-sm}` at wide tracking and body links in Nunito Sans `{typography.body-sm}`. A newsletter input sits inline with a gold `button-primary`. Social icon row uses muted (#555555) monochrome icons at 20px, keeping the footer tonally quiet.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; story-card spans full width with reduced padding; hero uses stacked image-above-text layout |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + cart icon + hamburger; hero can run text/image side-by-side at reduced type scale |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all collection links visible; hero is full-bleed with adjacent image column |
| Wide | > 1440px | Content constrained to 1440px max-width centered; product grid expands to four columns; hero image may bleed edge-to-edge beyond the content column |

### Touch Targets

- All interactive elements maintain a minimum 44×44px tap target on mobile
- Collection chips gain 12px vertical padding on mobile to ensure comfortable single-thumb operation
- Cart icon and hamburger in the mobile nav are padded to 48×48px effective tap zones
- Story-card "Read the Story" CTAs on mobile render as full-width ghost links rather than inline underlines
- Badge overlays on product images do not receive tap targets — they are decorative, not interactive

### Collapsing Strategy

- Primary navigation collapses to a slide-over drawer below 1128px, with top-level collection categories as full-width tappable rows at `{typography.title-md}` scale
- Hero banner switches from side-by-side text/image split to stacked (image above, text below) below 744px; headline reduces from `{typography.display-xl}` to `{typography.display-md}`
- Product grid steps: 4 columns (>1440px) → 3 columns (1128–1440px) → 2 columns (744–1128px) → 2 columns with tighter gutters on mobile
- Story-cards in PDP sidebars move below the product image and add-to-cart block in a single-column stack on mobile
- Gift-message module collapses its checkbox-plus-text-field layout to a full-width accordion row on mobile, expanding inline on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Baskerville weight variants (bold, semi-bold) not confirmed from extraction — all headline weights assumed 400 based on visible brand aesthetic; confirm whether any display copy runs at 700
- Jost and Karla both appear in the extracted font stack; their exact role split is ambiguous — Jost is used here as the primary UI sans with Karla as fallback, but they may serve separate typographic tiers
- Exact letter-spacing values for nav links and button labels estimated from brand conventions; live CSS inspection would confirm precise em values
- No confirmed hover treatment for `button-secondary` border — assumed to transition to `{colors.primary-active}` by analogy with the primary button
- `star-gold` (#fbcd0a) appears in extraction but likely originates from the Judgeme reviews widget rather than the native brand design system; treat as third-party until confirmed
- Dark surfaces (#282c2e, #2e2e2e) appear in extraction but it is unclear whether these are used for a dark announcement-bar variant, a sticky-scroll header, or isolated promotional sections
- Product card hover shadow values (blur, spread, offset) are not derivable from color extraction alone
- Mobile nav drawer visual treatment (scrim opacity, slide animation duration) not confirmed from extraction
