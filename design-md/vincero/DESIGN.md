---
version: alpha
name: "Vincero"
source_url: "https://vincerocollective.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep teal (#108474) shows up where most watch brands reach for navy or black — driving every primary CTA, hover state, and filter-active border in a category where chromatic restraint is the unspoken default. Oswald in condensed uppercase compresses editorial headings to an industrial density while EB Garamond handles product copy and brand storytelling in a serif voice borrowed from print; the two faces share no visual DNA, and their friction is the site's sharpest design statement. A warm near-black (#231f20) grounds dark-mode product pages without the cold screen quality of pure #000000, while a barely-differentiated off-white stack — #fdfdfd, #fafafa, #f9f9f9, #f9fafb — builds depth under bright studio photography without competing with it. Gold (#fbcd0a) earns its presence by echoing watch hardware finishes — yellow-case metals, polished gold bracelet links, metallic indices — surfacing as the active tint for star ratings and metallic callouts throughout the buying flow. A saturated hot-pink (#f046a9) arrives only at maximum urgency: flash-sale countdowns, clearance badges, and time-limited offer banners, delivered so far outside the composed palette that it registers as alarm rather than brand color. Buttons favor {rounded.sm} with {colors.primary} as the dominant CTA treatment; on mobile they extend full-width across the viewport. The announcement bar above the nav runs {colors.accent-gold} type on {colors.dark-bg} — the only surface where yellow serves as a text color on a dark field rather than a decorative metallic tint. Hero zones claim {spacing.section} of vertical breathing room; filter and sort rows compress to {spacing.sm}, establishing an unmistakable altitude difference between editorial immersion and transactional efficiency. The mint wash (#edf5f5, #c5f7f0) recurs in trust-bar backgrounds and informational callouts, keeping the teal brand hue active even in low-key utility zones.

colors:
  primary: "#108474"
  primary-active: "#0c6458"
  primary-disabled: "#a8cfc9"
  accent-gold: "#fbcd0a"
  accent-pink: "#f046a9"
  mint-soft: "#edf5f5"
  mint-lighter: "#c5f7f0"
  ink: "#231f20"
  dark-bg: "#121212"
  body: "#3d3d3d"
  muted: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  border-mid: "#cbcbcb"
  canvas: "#fdfdfd"
  surface-soft: "#f9f9f9"
  surface-card: "#fafafa"
  surface-page: "#f9fafb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Oswald', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: 1px
    textTransform: uppercase
  display-md:
    fontFamily: "'Oswald', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Oswald', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Oswald', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  editorial-lg:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  editorial-md:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-caps:
    fontFamily: "'Oswald', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Oswald', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Oswald', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  announcement-bar:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.accent-gold}"
    typography: "{typography.label-caps}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.md}"
  hero-banner:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.editorial-lg}"
    minHeight: 600px
    padding: "{spacing.section} {spacing.xl}"
  badge-sale:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-bestseller:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  collection-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.primary}"
    textColorActive: "{colors.primary}"
    padding: "6px 16px"
  watch-variant-swatch:
    size: 32px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderDefault: "1px solid {colors.border-mid}"
  trust-bar:
    backgroundColor: "{colors.mint-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    padding: "{spacing.lg} {spacing.xl}"
  editorial-band:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.editorial-md}"
    padding: "{spacing.section} {spacing.xl}"
  newsletter-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  star-rating:
    activeColor: "{colors.accent-gold}"
    inactiveColor: "{colors.hairline}"
    typography: "{typography.caption}"
  price-compare:
    originalColor: "{colors.muted}"
    saleColor: "{colors.accent-pink}"
    typography: "{typography.price-display}"
    originalTextDecoration: line-through
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.muted}"
    linkColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} {spacing.xl}"

---

## Components

### Buttons

**`button-primary`** — Teal (#108474) fill, white type, 8px radius, 48px tall, Oswald condensed uppercase at 15px with 1px letter-spacing. Darkens to #0c6458 on active/hover; mutes to a desaturated teal (#a8cfc9) fill when disabled. On mobile, stretches full viewport width to maximize tap area.

**`button-secondary`** — Transparent fill with a 1.5px ink (#231f20) border, same Oswald type and 8px radius as `button-primary`. Sits beside the primary in product detail pages; border lightens to {colors.hairline} on hover to signal interaction without competing with the primary.

**`button-dark`** — Near-black (#121212) fill with white type; used in hero overlays and editorial-band CTAs where teal would vanish against dark photography. Identical geometry to `button-primary`.

**`button-gold`** — Gold (#fbcd0a) fill with ink (#231f20) type; reserved for highest-value promotional moments like limited-edition launch CTAs. Only appears when the context justifies drawing from the accent palette.

### Announcement Bar

**`announcement-bar`** — A 36px-tall strip pinned above the nav, #121212 background with #fbcd0a Oswald label-caps type, center-aligned. The sole context on the site where gold operates as foreground text on a dark field. Carries sale codes, free-shipping thresholds, and countdown language. Dismissible on mobile to preserve vertical space.

### Navigation

**`nav-bar`** — 64px tall on desktop, #fdfdfd background with a 1px #eeeeee bottom border. Logo left, Oswald uppercase nav-links center or right, cart and search icons right. Becomes sticky on scroll. Collapses to hamburger + logo + cart icon below the tablet breakpoint; a full-height slide-in drawer reveals category links.

### Product Card

**`product-card`** — Square-crop image at 1:1 ratio, {rounded.md} corners, 1px #eeeeee border, #fafafa fill. Title renders in Oswald uppercase (title-md), price in Lato bold (price-display), sale price in accent-pink (#f046a9) with the original struck through in muted (#7b7b7b). Badge overlays (sale, new, bestseller) anchor to the top-left of the image. Hover lifts the card with a subtle box-shadow; on mobile, cards run two-up in a grid.

### Badges

**`badge-sale`** — Hot-pink (#f046a9) pill with white Oswald label-caps; 3px top/bottom padding, 8px sides, {rounded.xs}. Used on clearance and time-limited promotions.

**`badge-new`** — Same geometry in teal (#108474) fill; signals new collection arrivals.

**`badge-bestseller`** — Gold (#fbcd0a) fill with ink (#231f20) type; reserved for social-proof callouts on top-performing SKUs.

### Hero Banner

**`hero-banner`** — Full-width dark (#121212) background with full-bleed watch photography layered behind an editorial text block. Title in Oswald display-xl (uppercase, 56px, 700 weight); subtitle in EB Garamond editorial-lg for contrast. CTA pair: `button-primary` and `button-dark`. Minimum height 600px; vertical padding {spacing.section} top and bottom to give product photography room to breathe.

### Collection Filter

**`collection-filter`** — Pill-shaped chips ({rounded.full}) in surface-soft (#f9f9f9) with a 1px #dedede border. Typography: Lato body-sm. Active chip gets a 1px teal (#108474) border and teal text. Filter row scrolls horizontally on mobile without wrapping. Chips represent material, case size, strap type, and price range.

### Watch Variant Swatch

**`watch-variant-swatch`** — 32px circle swatches for case-color and strap selection. Default state: 1px #cbcbcb border. Selected state: 2px #108474 border with a small offset gap for visual clarity. Renders in a horizontal row beneath the product title on PDP.

### Trust Bar

**`trust-bar`** — A full-width stripe in mint (#edf5f5) with teal (#108474) icon glyphs and Lato body-sm labels. Four trust nodes: free shipping threshold, returns window, warranty, and authenticity. Padding {spacing.lg} vertical, {spacing.xl} horizontal. Sits between the hero and product grid on collection pages, and just above the footer on PDP.

### Editorial Band

**`editorial-band`** — Full-bleed dark (#121212) section with Oswald display-md heading and EB Garamond editorial-md body copy; used for brand-story moments ("Built for the driven"), collection launches, and ambassador features. Paired with a `button-dark` or `button-gold` CTA. {spacing.section} vertical padding.

### Newsletter CTA

**`newsletter-cta`** — Full-width teal (#108474) band with white Oswald display-sm heading and Lato body-md subtext. Email input in a borderless white field inline with a `button-dark` submit button. {spacing.xxl} vertical padding. Appears above the footer on most marketing and collection pages.

### Star Rating

**`star-rating`** — Gold (#fbcd0a) fill for active stars, hairline (#dedede) for inactive. Rating count in Lato caption below or beside the stars. Used on product cards and top of PDP.

### Price Compare

**`price-compare`** — Original price in muted (#7b7b7b) with `line-through`, sale price in accent-pink (#f046a9), both at price-display size. Renders inline, sale price leading when both are present.

### Footer

**`footer`** — Deep near-black (#121212) background, muted (#7b7b7b) body text, #eeeeee link tint, Oswald label-caps for column headings. Four-column layout on desktop (Shop, Company, Support, Social); single-column accordion on mobile. {spacing.xxl} vertical padding, {spacing.xl} horizontal.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid switches to 2-up; nav collapses to hamburger + logo + cart; buttons run full-width; hero text scales to display-md (Oswald 36px); announcement bar dismissible; filter chips scroll horizontally |
| Tablet | 744–1128px | 2–3 column product grid; nav shows abbreviated links with hamburger overflow; hero height increases to 500px; trust bar wraps to 2×2 grid |
| Desktop | 1128–1440px | 4-column product grid; full nav link row visible; hero banner reaches 600px minimum height; filter sidebar option available |
| Wide | > 1440px | Max content width 1440px, centered with auto margins; hero background extends edge-to-edge behind a contained text column; footer columns gain additional whitespace |

### Touch Targets

- All buttons minimum 48px tall; on mobile, primary CTA extends to full viewport width
- Nav hamburger icon: 44×44px tap area
- Watch variant swatches: 32px diameter with 8px gap — tight but acceptable for precision selection; consider 40px on mobile
- Filter chips: 36px minimum height for horizontal scroll row

### Collapsing Strategy

- Nav: full link row → hamburger drawer; category mega-menu collapses into accordion inside the drawer
- Footer: 4-column grid → single-column with collapsible accordion sections
- PDP image gallery: desktop side-by-side (image left, details right) → stacked single-column on mobile with swipe-enabled image carousel
- Trust bar: 4-node horizontal row → 2×2 grid on tablet → 2×2 stacked on mobile
- Filter panel: sidebar on wide desktop → horizontal pill-scroll row on tablet and mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Oswald and Lato weight usage per context not confirmed from extraction; assigned weights are inferred from watch-brand conventions and Oswald's typical condensed-heading application
- EB Garamond usage scope unclear — may be limited to editorial landing pages or brand-story modules rather than general body copy
- No confirmed modal or drawer overlay color; dark-bg (#121212) assumed but could use a scrim with opacity
- Exact border-radius on product images in gallery/PDP not extracted; {rounded.md} (12px) assumed from card context
- Hover and focus animation timing/duration not captured (transitions, easing curves)
- Mobile nav drawer background color not confirmed; canvas (#fdfdfd) assumed
- FontAwesome and JudgemeStar are utility icon fonts, not brand typography — no design data needed, but icon style and size guidelines are absent
- Sticky-nav behavior on scroll (height compression, shadow appearance) not confirmed
- Exact announcement-bar dismissal behavior and reappearance logic not extracted
