---
version: alpha
name: "Digby & Iona"
source_url: "https://www.digbyandiona.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Mrs. Eaves arrives in five distinct OpenType cuts — roman base, lining figures, small caps, petite caps, and all-petite-caps — a typographic investment more common to a university press than a Shopify storefront, and the single sharpest signal of the brand's ethos: Digby & Iona treats the wedding band not as an accessory purchase but as an heirloom decision, and every layout choice follows from that premise. The champagne field (#eacea7) — warm, slightly sandy, the color of antique gold held in afternoon light — anchors accent surfaces and hero grounds against near-black text (#121212, #191919), a contrast that reads as candlelit intimacy rather than clinical precision; deep navy (#202a36) carries long-form editorial copy while amber (#feb035) and warm orange (#fe9001) surface at CTA moments and price callouts, echoing the oxidized-gold patina of the bands themselves. The Shopify foundation (Wokiee theme, betrayed by the wokiee_icons font) gives a structured grid skeleton that the brand dresses in period detail: small-caps labels sit inside `{rounded.none}` hard-edged cards that feel engraved rather than printed, and inter-section breathing room is generous enough that the page earns its whitespace rather than apologizing for sparse catalog depth. Silver (#c0c0c0) and warm gray (#dedede) frame hairlines and secondary surfaces, keeping visual weight concentrated on the champagne accent and product photography. Ring swatches are the one exception to the no-radius rule — 32px circles (`{rounded.full}`) that reference the literal form of the object being sold. The five-variant type system signals that every word on the page was chosen as deliberately as the metal and stone choices in the catalog.

colors:
  primary: "#eacea7"
  primary-active: "#d4b48a"
  primary-disabled: "#f4e8d6"
  ink: "#121212"
  body: "#191919"
  muted: "#6a6a6a"
  hairline: "#dedede"
  silver: "#c0c0c0"
  canvas: "#ffffff"
  surface-soft: "#f8f4ee"
  surface-card: "#ffffff"
  on-primary: "#121212"
  gold-accent: "#feb035"
  warm-orange: "#fe9001"
  dark-ground: "#202a36"

typography:
  display-xl:
    fontFamily: "'mrs-eaves', 'mrs-eaves-roman-lining', Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'mrs-eaves', 'mrs-eaves-roman-lining', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  display-sm:
    fontFamily: "'mrs-eaves-roman-small-caps', 'mrs-eaves', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.08em
    fontVariant: small-caps
  title-md:
    fontFamily: "'mrs-eaves-roman-small-caps', 'mrs-eaves', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.06em
    fontVariant: small-caps
  title-sm:
    fontFamily: "'mrs-eaves-roman-petite-caps', 'mrs-eaves', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.08em
    fontVariant: small-caps
  body-md:
    fontFamily: "'mrs-eaves', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'mrs-eaves', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  caption:
    fontFamily: "'mrs-eaves-roman-all-petite-c', 'mrs-eaves', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "'mrs-eaves-roman-small-caps', 'mrs-eaves', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.12em
    fontVariant: small-caps
  button-sm:
    fontFamily: "'mrs-eaves-roman-petite-caps', 'mrs-eaves', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.1em
    fontVariant: small-caps
  nav-label:
    fontFamily: "'mrs-eaves-roman-small-caps', 'mrs-eaves', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.1em
    fontVariant: small-caps
  price:
    fontFamily: "'mrs-eaves-roman-lining', 'mrs-eaves', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  engraving-preview:
    fontFamily: "'mrs-eaves', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.15em

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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.dark-ground}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 24px
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
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    hoverColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    padding: "{spacing.md}"
  hero-bridal:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    sublineTypography: "{typography.display-sm}"
    sublineColor: "{colors.muted}"
    minHeight: 80vh
    paddingHorizontal: "{spacing.xxl}"
  editorial-band:
    backgroundColor: "{colors.dark-ground}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  metal-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  metal-badge-silver:
    backgroundColor: "{colors.silver}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  ring-swatch:
    size: 32px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "1px solid {colors.hairline}"
  engraving-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    previewTypography: "{typography.engraving-preview}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  size-selector:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.canvas}"
    unselectedBackground: "{colors.canvas}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 40px
    width: 40px
  price-display:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    saleColor: "{colors.warm-orange}"
  footer:
    backgroundColor: "{colors.dark-ground}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.primary}"
    dividerColor: "{colors.muted}"
    bodyTypography: "{typography.body-sm}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Near-black (#121212) fill with white Mrs. Eaves small-caps at 14px / 0.12em tracking; square corners (`{rounded.none}`) throughout with no border-radius softening. Hover shifts to the deep editorial navy (`{colors.dark-ground}`) — a subtle darkening rather than a hue inversion — and disabled state falls to a flat muted gray that reads as genuinely unavailable rather than faded.

**`button-secondary`** — White fill with a single-pixel ink border and identical small-caps type, matching the primary in height (48px) and corner profile (`{rounded.none}`) for clean side-by-side pairing at checkout or ring-builder CTAs. The outlined form introduces no second hue at the action layer.

**`button-ghost`** — Lighter hairline-bordered ghost in `{typography.button-sm}` petite caps for inline "learn more" and filter actions. Used inside editorial cards and lookbook sections where the full-weight secondary button would crowd reading space.

### Text Input

**`text-input`** — Hairline-bordered, square-cornered input in Mrs. Eaves body text at 16px. Focus lifts the border weight to full ink (`1px solid {colors.ink}`) with no shadow or fill change. The restraint — a single stroke-weight shift — keeps forms typographically consistent with the rest of the editorial system.

### Navigation

**`nav-bar`** — 64px horizontal strip on white canvas with a bottom hairline, links in `{typography.nav-label}` (Mrs. Eaves small caps, 13px, 0.1em tracking). The small-caps format makes navigation read as engraved plate text rather than interactive UI, which is consistent with the brand's ceremonial register. Catalog depth for bridal bands is shallow, so flat navigation without a mega-menu is expected.

### Product Card

**`product-card`** — Square-cropped 1:1 product image with zero corner radius, no card border or shadow. Title renders in `{typography.title-md}` (Mrs. Eaves small caps) and price in `{typography.price}` (Mrs. Eaves lining figures), both in ink. Whitespace and consistent grid sizing do the organizational work without decorative card chrome.

### Hero

**`hero-bridal`** — Warm off-white (`{colors.surface-soft}`) full-viewport hero with the headline in `{typography.display-xl}` (Mrs. Eaves 52px, loose tracking) and a small-caps subline in `{typography.display-sm}`. Photography fills the right half on desktop; on mobile the image stacks above the copy block. The champagne-tinted ground rather than pure white gives the opening moment warmth before product photography loads.

### Editorial Band

**`editorial-band`** — Full-width dark-navy (#202a36) section block with reversed white type and champagne (`{colors.primary}`) accent highlights for pull quotes and callout labels. Used for brand story, process, and testimonial sections. The navy-against-champagne pairing is the brand's most distinctive visual signature — the combination reads as jeweler's velvet under warm spot light.

### Metal Badges

**`metal-badge`** and **`metal-badge-silver`** — Compact all-caps labels for metal-variant tagging (Yellow Gold, Rose Gold, White Gold, Sterling Silver). The gold variant uses the warm champagne fill (`{colors.primary}`) with dark ink text; the silver variant uses #c0c0c0 with ink text. Both are square-cornered (`{rounded.none}`), in `{typography.caption}` uppercase, with minimal padding. Rose gold would likely share the champagne fill; white gold the silver fill.

### Ring Swatch

**`ring-swatch`** — 32px circular swatches (`{rounded.full}`) for metal-color selection on the PDP. Active state gains a 2px ink border ring; inactive rests behind a hairline. The circle is the only pill or full-radius shape in the entire system — its roundness is justified by literal reference to the ring form being sold.

### Engraving Callout

**`engraving-callout`** — Soft-cream block (`{colors.surface-soft}`) with a live preview of personalization text in `{typography.engraving-preview}` (Mrs. Eaves 18px, 0.15em tracking, mimicking an engraver's hand). Section label in `{typography.caption}` all-petite-caps above the preview field. This is likely the signature interactive moment on the PDP, where the brand's emphasis on custom engraving becomes tangible for the customer.

### Size Selector

**`size-selector`** — 40×40px square cells (`{rounded.none}`) for ring size selection. Selected cell fills with ink background and white text; unselected cells are white with hairline borders. The grid of identical square cells reads as a compact typeset table — consistent with the editorial character of the wider system.

### Footer

**`footer`** — Dark navy (#202a36) footer with white body copy and champagne (`{colors.primary}`) link color, repeating the warm-against-dark signature of the editorial band. Section headers in `{typography.caption}` uppercase, links in `{typography.body-sm}`. Generous top padding (`{spacing.section}`) maintains the brand's unhurried pacing all the way to the page end.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero image stacks above headline copy; nav collapses to hamburger with full-screen overlay in Mrs. Eaves small caps on dark-ground; engraving preview full-width below ring swatch row; size selector scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; hero switches to 50/50 image-text split; nav links visible horizontally; editorial band reduces padding to `{spacing.xl}`; engraving callout and size selector remain stacked |
| Desktop | 1128–1440px | Three-column product grid; hero reaches full 80vh with right-rail image fill; nav bar at full 64px height; engraving callout and size selector side-by-side on PDP |
| Wide | > 1440px | Grid max-width capped ~1320px centered; hero typography at display-xl ceiling; editorial band full-bleed with interior content max-width constrained; footer columns gain breathing room |

### Touch Targets

- Ring swatches maintain minimum 44×44px tap target (32px visual, 44px hit area via padding)
- Size selector cells minimum 44×44px on mobile despite 40px visual size
- Nav items minimum 44px height in mobile overlay
- All buttons maintain 48px height across all breakpoints
- Metal badges not interactive; no tap-target requirement

### Collapsing Strategy

- Product grid: 3-col → 2-col → 1-col at tablet and mobile breakpoints
- Hero: side-by-side (desktop) → stacked image-above-text (mobile)
- Navigation: full horizontal strip → hamburger; overlay uses full-screen `{colors.dark-ground}` with centered links in Mrs. Eaves small caps at display-sm scale
- Footer: 4-col → 2-col → 1-col, section labels collapse above their link lists
- PDP layout: two-column image+details → single column stacked at tablet; engraving callout moves below size selector on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Several extracted hex values (#ff0000, #ffff00, #0000ff, #00ff00, #800080, #ee82ee, #ffc0cb, #add8e6, #23cddc) appear to originate from a color-picker swatch component rather than brand UI and have been excluded from the palette
- `primary-active` (#d4b48a) and `primary-disabled` (#f4e8d6) are derived by darkening and lightening #eacea7 respectively; not directly extracted from the live site
- `surface-soft` (#f8f4ee) is a warm-tinted off-white derived for tonal consistency; the exact canvas tint value was not observed in extraction
- Whether the primary CTA button uses dark-ink fill or champagne fill is inferred from luxury-brand convention, not confirmed from extraction
- No hover transition timing or easing values extracted (duration, cubic-bezier)
- Exact Shopify/Wokiee breakpoint values not confirmed from source; standard theme defaults assumed
- Icon set details beyond the presence of the wokiee_icons font not extracted
- Engraving personalization font treatment (whether Mrs. Eaves or a script face) not confirmed from extraction
- Mobile navigation pattern (slide-in drawer vs. full-screen overlay) not confirmed
- No confirmed pricing for metal variants; amber/warm-orange assignment to sale price is inferred
