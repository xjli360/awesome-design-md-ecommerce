---
version: alpha
name: "Magnum Photos Shop"
source_url: "https://shop.magnumphotos.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every print in the Magnum catalog arrives freighted with photographic history, and the shop's visual system respects that weight without announcing it — a pale ash canvas of #f0f0f0 recedes behind photography rather than competing with it, while near-black #1f1f1f grounds typography in a register that reads as archival rather than aggressive. The most distinctive design choice is sage #5a6455 as a brand accent, a green the colour of vintage photographic equipment or aged museum walls, surfacing in category indicators, active states, and the left border of the print-information panel. Against this achromatic field, crimson #b43232 fires exactly once per page as the primary purchase call-to-action — a hot single note that carries the full weight of the interaction without overusing itself. Instrument Sans runs through every text scale at quiet weight settings, trusting long line-lengths and generous leading to produce an editorial reading cadence appropriate to a publication-grade image archive. A muted blue-grey (#bed2dc) marks informational surfaces and selection states, referencing the cool cast of silver-gelatin printing paper. Dark hero sections dissolve from #000044 through #121212, giving the impression that vast documentary photography simply continues off the edge of the viewport. Product cards use {rounded.xs} corners — 4 pixels — to stay crisply rectangular in sympathy with the photographic frame; there are no pill shapes here. The dark navigation bar in #121212 with on-dark type in #f0f0f0 creates a museum-vitrine contrast, positioning each photograph as an object to collect rather than a product to browse. Wide gutters and generous {spacing.section} vertical breaks give the image grid the breathing room it needs to function as a curated exhibition rather than a scroll-optimised catalogue.

colors:
  primary: "#b43232"
  primary-active: "#8f2020"
  primary-disabled: "#e0b4b4"
  sage: "#5a6455"
  sage-muted: "#7a8475"
  slate-blue: "#bed2dc"
  ink: "#1f1f1f"
  body: "#3a3a3a"
  muted: "#6a6a6a"
  hairline: "#dedede"
  hairline-soft: "#e1e1e1"
  canvas: "#f0f0f0"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  hero-overlay: "#000044"
  on-primary: "#ffffff"
  on-dark: "#f0f0f0"

typography:
  display-xl:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -1px
  display-md:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  caption-upper:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  price:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.04em
  button-sm:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.04em
  nav-link:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.02em
  meta-label:
    fontFamily: "'Instrument Sans', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
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
    padding: "12px 24px"
    height: 44px
    letterSpacing: 0.08em
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "11px 23px"
    height: 44px
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid rgba(255,255,255,0.35)"
    padding: "11px 23px"
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: "10px 14px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    imageFit: contain
    shadow: "0 1px 3px rgba(0,0,0,0.07)"
    padding: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    photographerTypography: "{typography.meta-label}"
    photographerColor: "{colors.muted}"
  product-card-hover:
    shadow: "0 6px 20px rgba(0,0,0,0.12)"
    transform: "translateY(-2px)"
    transition: "all 0.2s ease"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    overlayGradient: "linear-gradient(to bottom, {colors.hero-overlay}, {colors.surface-dark})"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.xxl} {spacing.section}"
  category-badge:
    backgroundColor: "{colors.sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  edition-badge:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  print-info-panel:
    backgroundColor: "{colors.surface-card}"
    borderLeft: "3px solid {colors.sage}"
    padding: "{spacing.lg}"
    rounded: "{rounded.none}"
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    labelTypography: "{typography.meta-label}"
    labelColor: "{colors.muted}"
  photographer-header:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption-upper}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"
  image-lightbox:
    backgroundColor: "{colors.surface-dark}"
    imageFit: contain
    padding: "{spacing.xl}"
    closeButtonColor: "{colors.on-dark}"
  filter-pill:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "6px 12px"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
    padding: "6px 12px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 40px
    placeholderColor: "{colors.muted}"
  slate-callout:
    backgroundColor: "{colors.slate-blue}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.canvas}"
    accentColor: "{colors.sage}"
    padding: "{spacing.xxl} 0"
    borderTop: "1px solid rgba(255,255,255,0.08)"

## Components

### Buttons

**`button-primary`** — The primary purchase button renders in crimson `#b43232` with white type at `{typography.button-md}`, 44px tall with `{rounded.xs}` corners that echo the photographic rectangle. A slightly widened letter-spacing (0.08em) gives the label the deliberate weight of a catalogue label rather than a retail shout. On press it deepens to `#8f2020`; disabled state washes to a pale blush `#e0b4b4` that reads as unavailable without using grey, preserving the page's warm tone.

**`button-secondary`** — Transparent fill, `{colors.ink}` type, a `{colors.hairline}` outline at the same 44px height as the primary. Used for secondary page actions (enquire, add to wishlist, share) where the crimson primary should not compete. On hover the border intensifies to `{colors.ink}`.

**`button-ghost-dark`** — Reversed-out for dark hero sections: transparent background, `{colors.on-dark}` type, white border at 35% opacity. Used for "View Collection" or "Explore Archive" CTAs that appear directly over full-bleed photography where a solid fill would mask the image beneath.

### Navigation

**`nav-bar`** — Full-width 64px bar in `{colors.surface-dark}` (`#121212`), forming the dark frame that brackets the light editorial body. Link type renders in `{colors.on-dark}` at `{typography.nav-link}`. The absence of a bottom border keeps the nav as one solid plane; the jump in luminosity to the `#f0f0f0` canvas below is the only separator needed. Cart icon and logo sit at opposing ends of the bar with no background treatment.

### Product Card

**`product-card`** — Cards surface on white `{colors.surface-card}` mounts with `{rounded.xs}` (4px) corners, a deliberate reference to the physical mounting board of fine-art prints. The photograph occupies the upper 70–75% of the card with `object-fit: contain` so full image framing is never cropped. Below the image: photographer name in `{typography.meta-label}` / `{colors.muted}`, print title in `{typography.body-sm}` / `{colors.ink}`, price in `{typography.price}`. The card lifts 2px with a softened shadow on hover, marking interactivity without adding colour noise.

### Hero Banner

**`hero-banner`** — Full-bleed photography sections backed by a gradient overlay running from `{colors.hero-overlay}` (`#000044`) at the top to `{colors.surface-dark}` at the base. This dissolve technique allows legible `{typography.display-xl}` white type even against complex photographic subjects and sky tones. Minimum 560px tall to give documentary images the scale their subject matter demands. CTAs use `button-ghost-dark` rather than the crimson primary, preserving the photograph's primacy.

### Badges

**`category-badge`** — Sage `{colors.sage}` filled, no border radius, all-caps `{typography.caption-upper}` in white. Appears on collection landing pages and search result cards to classify subject matter (War, Portrait, Street, Sport, etc.) without overriding the photograph. The sage reads as curatorial rather than promotional.

**`edition-badge`** — Dark `{colors.surface-dark}` filled, same geometry, used for edition-type labels (Limited Edition, Open Edition, Archival Pigment) positioned in the corner of the product card. The dark badge on the white card mount behaves like a museum accession tag.

### Print Info Panel

**`print-info-panel`** — A white card on the product detail page with a 3px sage left border marking the print-specification section: edition number, paper stock, print process, image dimensions, and provenance. The sage border connects the informational zone to the brand identity without introducing colour near the photograph itself. Labels use `{typography.meta-label}` in `{colors.muted}`; values use `{typography.body-sm}` in `{colors.body}`.

### Photographer Header

**`photographer-header`** — An all-caps `{typography.caption-upper}` byline in `{colors.muted}`, separated from the content below by a full-width `{colors.hairline}` rule. Appears at the top of photographer collection pages and above the print title on product pages. Functions as a section divider that positions authorship before subject.

### Filters

**`filter-pill`** and **`filter-pill-active`** — Outlined and filled pill pairs for faceted browse across photographer, decade, subject, format, and price. The active state inverts to `{colors.ink}` fill with `{colors.canvas}` type, a clear binary signal that uses no additional colour. Pills are `{rounded.xs}` to stay consistent with the card geometry.

### Search

**`search-bar`** — A quiet 40px input on `{colors.surface-soft}`, 1px `{colors.hairline}` border, `{rounded.xs}`, with placeholder text in `{colors.muted}`. No decorative icon frame — the input field matches the editorial restraint of the surrounding page and does not draw attention away from the product grid.

### Image Lightbox

**`image-lightbox`** — Full-screen `{colors.surface-dark}` overlay with the print centred at `object-fit: contain`, generous `{spacing.xl}` padding on all sides. The dark field isolates the photograph from any ambient page chrome, replicating a darkroom or projection context. Close and navigation controls render in `{colors.on-dark}`.

### Slate Callout

**`slate-callout`** — Informational banners in muted blue-grey `{colors.slate-blue}` for shipping notice, certificate of authenticity detail, or print-quality guarantee copy. The slate reads as cool and factual against the warmer ash canvas, distinct from the sage brand accent and the crimson CTA.

### Footer

**`footer`** — Dark `{colors.surface-dark}` full-width band mirroring the navigation, with `{colors.on-dark}` body text and sage `{colors.sage}` tinting column headings or divider lines. A barely-visible 1px top border in white/8% marks the transition from content body. Link hover brightens to `{colors.canvas}`.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to logo + hamburger icon on `{colors.surface-dark}`; hero min-height drops to 320px; print-info-panel becomes full-width stacked below image; filter pills scroll horizontally in a snap-scroll row; buttons expand to full width |
| Tablet | 744–1128px | 2-column product grid; nav shows logo + cart icon only with secondary links in slide-out drawer; hero 440px min-height; category-badge appears above product title in card |
| Desktop | 1128–1440px | 3-column product grid; full horizontal nav with all collection links visible; hero 560px; print-info-panel sits as a sticky right-rail panel at 340px width alongside the main image |
| Wide | > 1440px | 4-column product grid; max content width 1440px centred on canvas; visible left/right `{colors.canvas}` margins; hero image scales to fill full viewport width |

### Touch Targets
- All interactive controls minimum 44px tall — `button-primary`, `button-secondary`, `text-input` all spec'd at 44px
- Filter pills expanded to 40px tall on mobile for tap accuracy
- Product cards: full card surface is the tap target, no small link-only zones
- Nav hamburger icon: minimum 44×44px hit area with transparent padding
- Lightbox close and navigation arrows: 44×44px minimum

### Collapsing Strategy
- Product grid collapses 4→3→2→1 column at Wide→Desktop→Tablet→Mobile breakpoints
- Navigation collapses to icon-only bar on tablet, full hamburger drawer on mobile
- Print-info-panel moves from sticky right rail to below-image stacked block on tablet and mobile
- Hero CTA buttons stack vertically and expand full width on mobile
- Filter pills shift from wrapping grid to horizontal scroll strip on mobile; active pills scroll into view on selection
- Photographer header rule spans full width at all breakpoints; only font-size steps down on mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; dark nav background assumed from `#121212` (darkest non-overlay extracted value)
- Exact button border-radius not confirmed from live CSS; `{rounded.xs}` (4px) inferred from editorial/architectural aesthetic
- Typography weights (300 for display) not confirmed from font inspection; inferred from fine-art print archive conventions
- Hover animation duration and easing curve not extracted from live site
- Footer column structure and number of link groups not observed
- Mobile navigation pattern (hamburger vs persistent icon row) not confirmed
- Price formatting conventions (currency symbol position, sale/original price treatment) not extracted
- Print size selector and variant-picker component styling not observed
- Cart interaction model (slide-out drawer vs full-page cart) not confirmed
- Lazy-load skeleton and image placeholder colours not extracted
- Exact sage usage frequency and placement rules not confirmed beyond inference from extracted palette
