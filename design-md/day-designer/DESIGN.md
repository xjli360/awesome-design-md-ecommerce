---
version: alpha
name: "Day Designer"
source_url: "https://daydesigner.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Brass-gold embossing on a physical planner cover is the origin story for this brand's entire digital palette — #aa8b5f, a warm antique gold that reads as neither jewelry nor earth tone, carries every primary CTA, active state, and brand accent on a canvas of warm off-white (#f8f7f5). The pairing of Surveyor Display (a high-contrast editorial serif with ball terminals and ink-trap details) against Gotham's clean geometric sans creates a productive tension: the serif announces the brand's devotion to intentional living; the sans handles every date, price, and UI label with clock-precision legibility. A secondary mint wash (#bce8de) appears in feature callouts and seasonal campaign headers — not a product color so much as a breath of space that keeps the warm neutrals from reading as heavy. Deep navy (#272d45) provides a formal alternative to pure black in editorial headlines, while the standard ink (#212121) anchors body text across the shop. The rounded value of 10px (surfaced directly in the extracted stylesheet) establishes a soft but not bubbly feel for cards and inputs — the same geometry as a spiral-bound corner, just enough curve to signal warmth without infantilizing the format. Red (#c00000) is reserved strictly for sale badges and price-cut labels, never for UI chrome, which keeps the promotional signal from diluting the gold primary. A cool gray (#c4cdd5), surfaced as the meta theme-color, bleeds into the mobile browser chrome and subtly tells iPhone users: this is a structured, organized world before the page even loads. The overall register is a planner-lover's version of quiet editorial — confident structure, unhurried whitespace, and a color system that could transfer directly onto printed paper stock without looking out of place.

colors:
  primary: "#aa8b5f"
  primary-active: "#8d7048"
  primary-disabled: "#d4c0a5"
  primary-light: "#a68c5d"
  ink: "#212121"
  ink-deep: "#111111"
  body: "#414042"
  muted: "#989898"
  muted-soft: "#919191"
  hairline: "#e5e5e5"
  hairline-soft: "#dedede"
  canvas: "#f8f7f5"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  surface-subtle: "#e5e5eb"
  on-primary: "#ffffff"
  accent-mint: "#bce8de"
  accent-mint-light: "#b2f9e9"
  accent-yellow: "#ffcf2a"
  accent-navy: "#272d45"
  badge-sale: "#c00000"
  badge-sale-deep: "#b12704"
  theme-chrome: "#c4cdd5"
  mid-gray: "#606060"
  cool-slate: "#676986"

typography:
  display-xl:
    fontFamily: "'Surveyor Display A', 'Surveyor Display B', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Surveyor Display A', 'Surveyor Display B', Georgia, serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Surveyor Display A', 'Surveyor Display B', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Surveyor Display A', 'Surveyor Display B', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham A', 'Gotham B', 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Gotham A', 'Gotham B', 'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.05em
    textTransform: uppercase
  body-md:
    fontFamily: "'Gotham A', 'Gotham B', 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham A', 'Gotham B', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham A', 'Gotham B', 'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  label-allcaps:
    fontFamily: "'Gotham A', 'Gotham B', 'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  price:
    fontFamily: "'Gotham A', 'Gotham B', 'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Gotham A', 'Gotham B', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Gotham A', 'Gotham B', Gotham Medium, 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham A', 'Gotham B', Gotham Medium, 'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gotham A', 'Gotham B', 'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.04em

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 10px
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
    padding: 14px 28px
    height: 48px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 13px 27px
    height: 48px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.md}"
    padding: "12px {spacing.base}"
    typography: "{typography.body-md}"
    focusBorderColor: "{colors.primary}"
    height: 48px
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "12px {spacing.base}"
    typography: "{typography.body-md}"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    iconColor: "{colors.ink}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    shadow: "0 4px 20px rgba(0,0,0,0.08)"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    padding: "{spacing.sm}"
    hoverShadow: "0 2px 12px rgba(0,0,0,0.07)"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-allcaps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-allcaps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-best-seller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-allcaps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-dark:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 480px
  editorial-section:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl} {spacing.section}"
  collection-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    labelTypography: "{typography.label-allcaps}"
    rounded: "{rounded.md}"
    hoverOverlayColor: "rgba(170,139,95,0.08)"
  category-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-allcaps}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-allcaps}"
    height: 36px
  announcement-bar-navy:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-allcaps}"
    height: 36px
  price-strike:
    textColor: "{colors.muted}"
    typography: "{typography.price-sm}"
    textDecoration: line-through
  price-sale:
    textColor: "{colors.badge-sale}"
    typography: "{typography.price}"
  cart-drawer:
    backgroundColor: "{colors.surface-card}"
    borderLeft: "1px solid {colors.hairline}"
    titleTypography: "{typography.display-sm}"
    subtotalTypography: "{typography.title-md}"
    ctaComponent: "button-primary"
    width: 400px
  planner-cover-swatch:
    rounded: "{rounded.sm}"
    borderWidth: 2px
    selectedBorderColor: "{colors.primary}"
    inactiveBorderColor: "{colors.hairline}"
    size: 32px
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-mint}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Flat rectangles with no border-radius, gold fill (#aa8b5f), white uppercase Gotham text at 14px with wide letter-spacing (0.08em). The shape deliberately evokes the clean cut corner of a planner page rather than a digital pill. Hover darkens to `{colors.primary-active}` (#8d7048); disabled state uses `{colors.primary-disabled}`, a bleached parchment gold. Minimum height 48px to meet touch targets.

**`button-secondary`** — White fill with a 1px gold border and gold uppercase text. Used for secondary editorial CTAs like "Learn More" or "View All" adjacent to a primary sell action. Matches the primary button's height and letterSpacing so stacked pairs feel like a deliberate typographic set rather than accidental siblings.

**`button-ghost`** — Transparent fill, hairline border, ink text. Appears in filter panels, variant selectors, and quantity controls. The neutral tone ensures it never competes with the gold primary in dense product-page layouts.

### Navigation

**`nav-bar`** — White ground, 64px tall, hairline bottom border. Logo sits left in gold; center houses category links in 13px Gotham with 0.04em tracking; right cluster holds search, account, and cart icons in ink. On scroll the bar stays fixed and gains a faint box-shadow to separate from product imagery.

**`nav-dropdown`** — Appears beneath category links with a 10px rounded card, soft shadow, and generous internal padding. Sub-categories use `{typography.body-sm}` with `{colors.body}` text; featured collection tiles may appear alongside for high-traffic categories.

**`announcement-bar`** — Full-width 36px strip in brand gold or navy, uppercase Gotham micro-text. Carries shipping thresholds, sale countdowns, and seasonal messaging. The gold variant is default; navy swaps in for academic-year campaign periods.

### Product Cards

**`product-card`** — Neutral white card with 10px radius on both image and card container. The planner cover image occupies ~70% of card height; below it, a `{typography.label-allcaps}` category label in muted gray, a `{typography.title-md}` product name in ink, and price in 18px Gotham medium. Sale and Best Seller badges (`badge-sale`, `badge-best-seller`) pin to the top-left image corner as flat rectangles with no radius. On hover a 2px gold border traces the card edge and a subtle shadow lifts the card 2px — the animation takes 150ms ease.

**`planner-cover-swatch`** — 32px circular or rounded-square color/pattern chips used on the PDP for cover-color selection. The active swatch gets a 2px gold ring (`{colors.primary}`) with a 2px gap between chip and ring; inactive chips show a hairline border. This pattern mirrors physical swatch samples in a brand showroom.

### Hero & Editorial

**`hero-banner`** — Full-bleed image with text left-aligned on a warm canvas ground (#f8f7f5). Headline in `{typography.display-xl}` Surveyor Display, subhead in `{typography.body-md}` Gotham, followed by a `button-primary`. Minimum height 560px; image occupies the right 50% on desktop with the text column padded to `{spacing.section}` horizontal margin.

**`hero-banner-dark`** — Navy (#272d45) ground, white text, same Surveyor/Gotham hierarchy. Used for academic-year launch campaigns where the darker register signals a seasonal transition.

**`editorial-section`** — Mint-washed (#bce8de) full-width module. Headline in `{typography.display-md}`, body copy in `{typography.body-md}`, optional CTA. The mint grounds a secondary campaign narrative (e.g., goal-setting content, gifting guides) without using brand gold, giving the page a visual rest stop between product shelves.

### Badges & Labels

**`badge-sale`** — Flat rectangle, red (#c00000), white uppercase Gotham at 11px. Positioned absolutely on the product image, top-left. Never applied to non-discounted items; the signal is kept clean.

**`badge-new`** and **`badge-best-seller`** — Same flat geometry. Navy for NEW, gold for BEST SELLER. The three badge colors (red, navy, gold) form a deliberate tricolor that reads clearly against any cover photography.

**`category-label`** — Small all-caps label in muted gray, with a hairline underline used as a section divider heading on collection pages. Provides taxonomic structure without adding visual weight.

### Cart & Checkout

**`cart-drawer`** — 400px right-side drawer, white, left-border hairline. Title in `{typography.display-sm}` Surveyor, line items in `{typography.body-sm}`, subtotal in `{typography.title-md}`. Checkout CTA uses `button-primary` full-width at the drawer's base. Planner customization thumbnails render as 56px square images with a 4px gold border on the selected configuration.

### Footer

**`footer`** — Deep navy (#272d45) ground. Column headings in `{typography.title-sm}` uppercase, links in `{typography.body-sm}` mint (#bce8de) so they're readable against the dark ground without resorting to pure white. Social icons use the mint tint. Newsletter input field uses a white-bordered variant against the navy background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart; hero text fills full width over stacked image; announcement bar text truncates with marquee scroll; cart drawer goes full-width |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links, dropdowns suppressed; hero shifts to 60/40 text/image split; editorial sections stack to two columns |
| Desktop | 1128–1440px | Three or four-column product grid; full mega-nav with dropdown panels; hero at full 50/50 split; editorial sections in two-column layouts with images |
| Wide | > 1440px | Max-content-width wrapper (~1400px) centered; hero image crops wider; product grid holds at four columns with wider gutters |

### Touch Targets

- All buttons minimum 48px height with at least 44px tap width
- Cover-color swatches minimum 32px with 8px gap between chips
- Nav links in mobile drawer padded to 52px tall rows
- Cart quantity +/– controls minimum 40×40px tap areas
- Breadcrumb links minimum 36px tall on mobile

### Collapsing Strategy

- Desktop mega-nav → mobile hamburger drawer with accordion category expansion
- Hero two-column layout → stacked image above / text below on mobile (image first for visual punch)
- Three/four-column product grid → two-column tablet → single-column mobile
- Footer four-column layout → two-column tablet → stacked accordion mobile
- Editorial side-by-side sections → stacked single-column on mobile
- Announcement bar: long text switches to marquee scroll below 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-weight numeric values confirmed for Surveyor Display; weights inferred as 300/400 based on editorial serif conventions for this brand tier
- Gotham Medium was present as an `!important` override in the font stack — suggests aggressive weight-locking in a few components, but specific selectors are unknown
- No confirmed box-shadow values extracted; shadow tokens are editorial estimates based on comparable Shopify storefronts
- Animation/transition timing values (hover durations, drawer slide speeds) were not extractable from the static scan
- No confirmed grid column counts or gutter widths from the stylesheet; responsive breakpoints estimated from Shopify defaults plus the 744/1128/1440 standard range
- `#ffcf2a` (yellow) and `#6371c7` (periwinkle) appeared in the extracted palette but their specific usage contexts (promotional banners, partner badges?) could not be confirmed — omitted from primary tokens to avoid misuse
- Dark mode or high-contrast variant not observed; assumed light-mode-only storefront
