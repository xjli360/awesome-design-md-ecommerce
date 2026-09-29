---
version: alpha
name: "20x200"
source_url: "https://20x200.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every edition in the catalog carries two numbers that encode the brand's founding premise — a fixed run, a fixed price — and the site's visual logic mirrors that arithmetic clarity. The canvas floats on warm off-white (#faf9f5 and #f4f2ee) rather than clinical white, immediately placing the work in a context closer to acid-free mat board than to a sterile tech storefront. Against that warm ground, a single voltage of burnt orange (#ed7c35) pulls every primary CTA, price badge, and hover accent — a hue that reads as neither gallery-stiff nor streetwear-loud, landing precisely in the territory of an independent art publisher's colophon stamp. Merriweather serif carries artwork titles and editorial copy, lending the weight of art criticism to descriptions that start at $35; Libre Franklin handles nav, labels, and UI chrome in a workhorse register that never competes with the image.

  The type scale leans editorial: display headings are set tight with negative tracking, artist names appear in a small Merriweather italic, and edition metadata — print size, paper, run number — renders in a condensed caption stack. A deep wine accent (#7e1412) surfaces on sale banners and error states, giving the system a second voltage with old-broadside energy. The neutral ladder runs from near-black (#111111) through four grays (#585858, #464646, #767676, #b8b8b8) to light hairlines (#dedede), providing enough range to separate artwork metadata hierarchies without introducing decorative color. Rounded corners are minimal — inputs and cards sit at {rounded.xs} or {rounded.sm}, buttons at {rounded.xs} — reinforcing the print-catalog formality that distinguishes this platform from lifestyle DTC peers. Swiper powers the horizontal edition-browse carousels that let collectors scan a run without leaving the page, and the orange hover state on those carousel arrows creates a consistent "next edition" affordance that feels hand-coded for the collecting ritual. The light salmon surface (#feebeb) paired with wine text flags error and sold-out states without reaching for generic red, keeping even exception states inside the brand's editorial palette.

colors:
  primary: "#ed7c35"
  primary-hover: "#ef8b4c"
  primary-active: "#d46b28"
  primary-disabled: "#f4c9a8"
  accent-wine: "#7e1412"
  accent-wine-surface: "#feebeb"
  ink: "#111111"
  ink-strong: "#121212"
  body: "#363636"
  body-secondary: "#464646"
  muted: "#767676"
  muted-light: "#b8b8b8"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#faf9f5"
  surface-soft: "#f4f2ee"
  surface-card: "#ffffff"
  surface-mid: "#585858"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link-system: "#007aff"
  scrim: "#111111"

typography:
  display-xl:
    fontFamily: "'Merriweather', Georgia, 'Times New Roman', serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Merriweather', Georgia, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Merriweather', Georgia, serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Merriweather', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Libre Franklin', 'Franklin Gothic Medium', 'Arial Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  artist-name:
    fontFamily: "'Merriweather', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  caption-strong:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.2px
  edition-meta:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-label:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  nav-label-bold:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  filter-label:
    fontFamily: "'Libre Franklin', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px

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
    padding: 12px 24px
    height: 44px
    transition: background-color 150ms ease
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    width: "100%"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  text-input-error:
    border: "1px solid {colors.accent-wine}"
    backgroundColor: "{colors.accent-wine-surface}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    borderBottom: "1px solid {colors.hairline}"
    height: 60px
    logoColor: "{colors.ink}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-label-bold}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    shadow: "0 4px 16px rgba(17,17,17,0.10)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    artistTypography: "{typography.artist-name}"
    priceTypography: "{typography.price-sm}"
    metaTypography: "{typography.edition-meta}"
    textColor: "{colors.ink}"
    mutedTextColor: "{colors.muted}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  product-card-hover:
    imageScale: 1.03
    transition: transform 200ms ease
  edition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body-secondary}"
    typography: "{typography.edition-meta}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  edition-badge-sold-out:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.edition-meta}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  price-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-banner:
    backgroundColor: "{colors.accent-wine}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-strong}"
    padding: "{spacing.sm} {spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} 0"
  hero-image-card:
    imageBackground: "{colors.surface-soft}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    rounded: "{rounded.none}"
  edition-carousel:
    backgroundColor: "{colors.canvas}"
    arrowColor: "{colors.ink}"
    arrowHoverColor: "{colors.primary}"
    arrowBackground: "{colors.surface-card}"
    arrowBorder: "1px solid {colors.hairline}"
    arrowRounded: "{rounded.full}"
    arrowSize: 40px
  filter-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.filter-label}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.ink}"
    activeUnderline: "2px solid {colors.primary}"
    height: 48px
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body-secondary}"
    typography: "{typography.filter-label}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  artwork-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    artistTypography: "{typography.display-sm}"
    priceTypography: "{typography.price}"
    bodyTypography: "{typography.body-md}"
    metaTypography: "{typography.edition-meta}"
    textColor: "{colors.ink}"
    mutedColor: "{colors.muted}"
    dividerColor: "{colors.hairline}"
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    selectedBorder: "1px solid {colors.ink}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink-strong}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.muted-light}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption-strong}"
    linkHoverColor: "{colors.primary}"
    dividerColor: "#2a2a2a"
    padding: "{spacing.xxl} 0"
  announcement-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-strong}"
    borderBottom: "1px solid {colors.hairline}"
    height: 36px

## Components

### Buttons

**`button-primary`** — The main call-to-action renders in burnt orange (#ed7c35) on a 44px-tall block with `{rounded.xs}` corners, giving it a publisher's stamp quality rather than a rounded pill softness. On hover the fill shifts to `{colors.primary-hover}` (#ef8b4c), and on press it darkens to `{colors.primary-active}` (#d46b28); the 150ms ease transition is fast enough to feel responsive without calling attention to itself. Disabled state uses a washed peach (#f4c9a8) that visually communicates unavailability without the harshness of gray.

**`button-secondary`** — Outlined variant with a 1.5px ink border and transparent fill, pairing with primary on artwork detail pages where both "Add to Cart" and "Save to List" appear at the same level. Hover fills with `{colors.surface-soft}` to signal interactivity without competing with the primary orange.

**`button-add-to-cart`** — Full-width orange block on product detail, taller at 48px, designed to sit at the foot of the size/edition selector stack. Shares the same orange palette as `button-primary` but with extended side padding to anchor the purchase flow.

### Navigation

**`nav-bar`** — A 60px bar on `{colors.canvas}` with a single hairline bottom border. The 20x200 wordmark is set in the same ink as body text — no separate lockup color — reinforcing that the brand name is typographic rather than logotype-dependent. Active nav links shift to `{colors.primary}` and increase to `{typography.nav-label-bold}` weight. A dropdown panel (`nav-dropdown`) appears for category/browse links, floating with a subtle shadow and hairline border at `{rounded.xs}`.

**`announcement-bar`** — A slim 36px bar above the nav in `{colors.surface-soft}` carries shipping or editorial messages at `{typography.caption-strong}`, keeping the brand voice active without burning orange real estate on marketing prose.

### Product Cards

**`product-card`** — Square artwork image on a soft warm ground (`{colors.surface-soft}`) above a tight text stack: artwork title in `{typography.title-sm}`, artist name in `{typography.artist-name}` (Merriweather italic), price in `{typography.price-sm}`, and edition metadata in `{typography.edition-meta}` uppercase. No card border or shadow — pieces are separated by grid gutter alone. On hover, the image scales to 1.03× with a 200ms ease, creating a light zoom without a drop shadow theatric. Sold-out editions carry the `edition-badge-sold-out` chip in washed gray.

**`edition-badge`** — A small all-caps label (e.g., "EDITION OF 200") in `{typography.edition-meta}` set in `{colors.surface-soft}` at `{rounded.xs}`. Communicates the collectible scarcity without dominating the card layout.

### Artwork Detail

**`artwork-detail-panel`** — The right-column information panel on a PDP. Title in Merriweather `{typography.display-md}`, artist credit in `{typography.display-sm}` weight 400, price in the bold `{typography.price}` scale. Size/paper/edition counts render in `{typography.edition-meta}` uppercase with `{colors.hairline}` dividers between metadata groups. The `size-selector` dropdown sits above the add-to-cart button, using an ink-border active state to confirm selection.

### Filtering and Browse

**`filter-bar`** — A horizontal scrollable bar below the nav on browse pages. Inactive filters use `{typography.filter-label}` in `{colors.body}`; the active filter gains an ink text weight and a 2px orange underline. On mobile this bar scrolls horizontally without showing a scrollbar.

**`filter-pill`** — Used for applied filter chips in the results header. Resting state: `{colors.surface-soft}` fill, `{colors.hairline}` border, `{rounded.full}` shape. Active/selected pills invert to ink fill with white text, signaling a live constraint on the result set.

**`edition-carousel`** — Swiper-powered horizontal scroll for homepage and collection sections. Arrow buttons are 40px circles (`{rounded.full}`) with a card background and hairline border; on hover arrows tint to `{colors.primary}`, creating the consistent orange directional affordance throughout the browse experience.

### Banners and Metadata

**`sale-banner`** — Wine-red (#7e1412) full-width bar for discount announcements. The deep maroon reads as neither error nor celebration, landing as a serious editorial interrupt consistent with the brand's print-catalog register.

**`price-badge`** — Small orange chip overlaid on hero artwork images to communicate the starting price ("from $35"). Uses `{colors.primary}` fill at `{rounded.xs}`, maintaining the orange-as-price-signal convention from cards to hero.

### Footer

**`footer`** — Near-black (#121212) full-bleed with four-column link grid. Section headings in `{typography.caption-strong}` uppercase white; links in `{typography.body-sm}` at `{colors.muted-light}`, shifting to `{colors.primary}` on hover. The dark footer provides the strongest contrast moment on any page, closing the catalog-browse loop with a dense resource index that reflects the breadth of a 15+-year art publishing archive.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark; filter-bar scrolls horizontally; artwork detail panel stacks below image; edition carousel shows 1.2 cards to signal scroll |
| Tablet | 744–1128px | Two-column product grid; nav shows abbreviated link set; artwork detail uses 50/50 image-panel split; filter-bar wraps to two rows if needed |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with dropdown; artwork detail at 55/45 image-panel; edition carousel shows 3–4 cards |
| Wide | > 1440px | Grid max-width constrained to ~1400px, centered on canvas; gutters expand proportionally; hero imagery scales up without reflowing text columns |

### Touch Targets

- All nav links and filter pills maintain a minimum 44px tap height via padding even when type is small
- Carousel arrow buttons are 40px circles but receive a transparent tap extension to 44px on touch devices
- Size selector and edition dropdowns use 42px input height to meet touch minimum
- Product card tap target covers the full card block including the text stack below the image

### Collapsing Strategy

- Navigation: hamburger replaces full link row below 744px; category dropdown becomes a full-screen slide-in drawer
- Filter bar: transitions from horizontal fixed bar to a collapsible "Filters" toggle button that opens a bottom sheet on mobile
- Artwork detail: image moves to full-width top, purchase panel scrolls beneath it; sticky "Add to Cart" bar attaches to viewport bottom on mobile
- Footer: four-column grid collapses to a single accordion-style column with expand/collapse per section heading
- Edition carousel: arrow buttons hidden on touch; swipe gesture with momentum scroll handles navigation

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit brand-defined type scale sizes were extracted — Merriweather and Libre Franklin sizes above are inferred from typical gallery/editorial usage and the hierarchy implied by the page structure
- Hover and focus ring colors were not directly extracted; `{colors.primary}` and ink are used as inference
- Exact button border-radius values were not confirmed from computed styles; `{rounded.xs}` (4px) is a reasonable inference from the catalog-formal aesthetic
- Dark mode variant, if any, was not detected in extraction
- Swiper configuration (slides-per-view, breakpoints, loop settings) is not confirmed — carousel component reflects structural intent only
- Exact footer column count and link taxonomy were not extracted; four-column layout is inferred from standard Shopify gallery theme conventions
- Animation/transition timing values beyond button hover are not confirmed from extraction
- Mobile navigation drawer design (background color, transition direction) was not confirmed
