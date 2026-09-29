---
version: alpha
name: "Foundrae"
source_url: "https://www.foundrae.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Medallions struck with archetypal symbols — Wholeness, Alchemy, Protect — float against a near-void background of #0a0e10, a black so dense it erases any perceived border between canvas and unlit screen. Foundrae builds meaning into material: 18k gold in full relief against this darkness carries visual weight that white-canvas luxury brands achieve only through image staging. The coral accent (#ff7f50) materializes only at the moment of purchase action — the primary CTA and add-to-cart button — appearing nowhere in headers, nowhere in navigation, nowhere decorative, so that when it appears it reads as something urgent against the dominant near-black field. Category labels and structural wayfinding are rendered in muted olive-grey (#757562), occupying deliberate middle territory between the near-black canvas and the light ink (#dedede) of product names and prices. This creates a three-register hierarchy: product identity in light text, category taxonomy in olive, active action in coral — three temperatures, none competing. Navigation runs in tight uppercase letterforms at high tracking, a compressed script that suits the archival gravity of the brand's naming conventions — these are not charm collections but symbolic systems. Border-radius is minimal throughout, {rounded.none} to {rounded.xs}, maintaining the architectural geometry expected of objects meant to last decades rather than UX patterns that date in eighteen months. Card grids sit flush with hairline dividers at #2a2a2a, faintly visible against near-black surfaces, marking structure without introducing noise. Typography loads only as "inherit" in extraction, but the proportional weights and tracking choices visible in computed styles suggest a restrained serif or transitional cut in the 300–400 weight range across display and body — no ultra-thin romantics, no heavy editorial gestures — allowing material photography to carry the sentence. Spacing is generous at section scale ({spacing.section}) but compressed within product cards, where name, metal type, and price run close together like entries in a jeweler's ledger. The symbol catalog scroll — a horizontally scrolling row of named amulet families — is the brand's most distinctive navigation pattern, presenting its entire symbolic vocabulary as primary wayfinding before price or category filters, an unusual inversion of standard e-commerce hierarchy.

colors:
  primary: "#ff7f50"
  primary-active: "#d96030"
  primary-disabled: "#b08070"
  ink: "#dedede"
  body: "#c0c0c0"
  muted: "#808080"
  hairline: "#2a2a2a"
  canvas: "#0a0e10"
  surface-soft: "#121212"
  surface-card: "#1c1c1c"
  on-primary: "#0a0e10"
  olive-label: "#757562"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.04em
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 30px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.03em
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  body-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.01em
  caption:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
  button-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.14em
    textTransform: uppercase
  nav-link:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  category-label:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.18em
    textTransform: uppercase
  price:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 14px 36px
    height: 48px
  button-primary-hover:
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 35px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 0
    placeholderColor: "{colors.muted}"
  text-input-focus:
    borderBottom: "1px solid {colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-hover:
    textColor: "{colors.olive-label}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspect: "4/5"
    gap: "{spacing.md}"
  product-card-category:
    typography: "{typography.category-label}"
    textColor: "{colors.olive-label}"
    marginBottom: "{spacing.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.muted}"
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 52px
    width: "100%"
  add-to-cart-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
    imageOverlayScrim: "{colors.scrim}"
  hero-eyebrow:
    typography: "{typography.category-label}"
    textColor: "{colors.olive-label}"
    marginBottom: "{spacing.sm}"
  symbol-scroll:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
    overflowX: scroll
    gap: "{spacing.xl}"
  symbol-scroll-item:
    typography: "{typography.nav-link}"
    textColor: "{colors.muted}"
  symbol-scroll-item-active:
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.ink}"
  filter-pill:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.category-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "6px 14px"
  filter-pill-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.lg}"
  badge-new:
    backgroundColor: "transparent"
    textColor: "{colors.olive-label}"
    typography: "{typography.category-label}"
    border: "1px solid {colors.olive-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  search-overlay:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    borderTop: "1px solid {colors.hairline}"
  metal-selector:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.category-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
  metal-selector-active:
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
  product-detail-symbol:
    typography: "{typography.caption}"
    textColor: "{colors.olive-label}"
    marginBottom: "{spacing.md}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} 0"
  footer-heading:
    textColor: "{colors.ink}"
    typography: "{typography.category-label}"
    marginBottom: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — Full-width coral (#ff7f50) rectangle with zero border-radius, uppercase letterforms at 0.14em tracking. Reserved exclusively for purchase-path actions: add-to-cart, proceed to checkout. Hover shifts to `{colors.primary-active}` (#d96030); disabled renders at `{colors.primary-disabled}` with no opacity fade. The flatness and dark text (`{colors.on-primary}`) keep it legible against the near-void canvas.

**`button-secondary`** — Transparent background with a 1px `{colors.ink}` border, same uppercase button type. On hover the fill inverts: the border box floods with `{colors.ink}` and text drops to `{colors.canvas}`. Used for wishlist, notify-me, and secondary navigation CTAs where coral urgency is inappropriate.

### Text Inputs
**`text-input`** — Borderless except for a 1px bottom rule in `{colors.hairline}`, zero radius, transparent background. Placeholder text in `{colors.muted}`. Focus thickens the underline to `{colors.muted}`. This underline-only pattern reads as editorial form rather than functional form, consistent with the brand's archival register.

### Navigation
**`nav-bar`** — 60px tall, `{colors.canvas}` background, `{colors.hairline}` bottom border. Links in uppercase at 0.12em tracking. Hover tints links to `{colors.olive-label}` rather than underlining, preserving the clean horizontal line. Logo sits left, cart and account icons right; search expands an overlay rather than redirecting.

**`symbol-scroll`** — A horizontally scrolling row beneath the primary nav presenting named symbolic families (Wholeness, Full Heart, Alchemy, Protect, etc.) as category wayfinding. Inactive items in `{colors.muted}`; active item in `{colors.ink}` with a 1px underline. This component replaces the conventional mega-menu dropdown as primary product taxonomy navigation.

### Product Card
**`product-card`** — No card border, no shadow, no surface color — images sit directly on `{colors.canvas}` in a 4:5 portrait aspect. Below the image: category label in `{colors.olive-label}` at `{typography.category-label}` weight, then product title in `{typography.title-sm}`, then price in `{colors.muted}`. No hover-overlay CTA; click navigates directly to PDP.

### Hero
**`hero`** — Full-bleed image against `{colors.canvas}`, eyebrow label in `{colors.olive-label}` at `{typography.category-label}` tracking, display title in `{typography.display-xl}`. No gradient overlays on image heroes — the brand trusts material photography at full contrast. Section padding `{spacing.section}` top and bottom maintains breathing room between content modules.

### Filters and Badges
**`filter-pill`** — Zero-radius, 1px `{colors.hairline}` border, muted label text. Active state fills with `{colors.surface-soft}` and promotes label to `{colors.ink}`. The sharply rectangular pill is consistent with the brand's refusal of rounded affordances.

**`badge-new`** — Transparent box with 1px `{colors.olive-label}` border, olive text. Appears on newly introduced symbolic families. Small and unobtrusive — the brand does not use urgency badges (SALE, HOT) anywhere.

### Metal Selector
**`metal-selector`** — Rectangular toggle pills for metal type selection (18k Yellow, 18k White, 18k Rose). Inactive in `{colors.hairline}` border with `{colors.muted}` text; active fills border to `{colors.ink}` with promoted ink text. No swatch dots — metal type is communicated by name only, consistent with the brand's typographic precision.

### Footer
**`footer`** — `{colors.surface-card}` background (#1c1c1c) separates footer from the page canvas by exactly one surface step. Column headings at `{typography.category-label}` in `{colors.ink}`; body links in `{typography.body-sm}` `{colors.muted}`. No social icon grid — newsletter capture dominates the footer action zone, with a single `text-input` and `button-secondary`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; symbol-scroll becomes primary category nav with momentum scrolling; nav collapses to hamburger + logo + cart; hero text stack reduces to `display-md`; add-to-cart button pinned to viewport bottom |
| Tablet | 744–1128px | Two-column product grid; nav bar retains horizontal links but reduces to core categories; hero image shifts to 60/40 text-image split |
| Desktop | 1128–1440px | Three-column product grid; full symbol-scroll bar visible; nav exposes all category links plus search icon; hero runs full bleed with centered text overlay |
| Wide | > 1440px | Grid expands to four columns with max-width container capped at 1440px; side margins grow proportionally; hero copy constrained to 640px max-width to prevent line-length runout |

### Touch Targets
- All nav links and symbol-scroll items maintain minimum 44px hit height via vertical padding even when visible text is smaller
- Metal selector pills padded to 40px height minimum on mobile
- Add-to-cart button at 52px height, pinned sticky at viewport bottom on mobile PDP
- Filter pills padded to 40px on mobile collection pages

### Collapsing Strategy
- Primary nav collapses to hamburger at < 744px; slide-in drawer preserves full symbol taxonomy
- Symbol-scroll persists across all breakpoints as a scrollable row — never collapses into a dropdown
- Product grid never drops below single-column; two-column begins at 744px
- Footer column layout stacks vertically below 744px; newsletter form appears above link columns on mobile
- Search expands as a full-width overlay at all breakpoints — no inline expansion

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font-family extraction returned only "inherit" — no specific typeface names captured; serif fallbacks (Georgia) used throughout but actual brand font is unconfirmed; may be a custom or licensed serif loaded via Shopify CDN not visible in computed style passes
- No explicit heading weight breakpoints extracted; weight 300 assumed for display based on luxury fine jewelry conventions
- Exact nav-bar height unconfirmed from extraction; 60px estimated from common Shopify header patterns
- Hover state colors for coral primary not directly extracted; `primary-active` (#d96030) derived by darkening #ff7f50 ~15%
- No animation or transition timing values captured
- Mobile sticky add-to-cart behavior not confirmed from static extraction
- Icon set (wishlist heart, cart, account, search) style (line vs. fill, stroke weight) not confirmed
