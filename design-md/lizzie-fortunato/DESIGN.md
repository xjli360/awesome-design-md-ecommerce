---
version: alpha
name: "Lizzie Fortunato"
source_url: "https://www.lizziefortunato.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Vivid, handmade beadwork and found-vintage hardware are given maximum visual air by a site that refuses to compete with the jewelry itself. The canvas holds at #f5efeb — a warm, undyed-muslin cream that reads closer to natural linen than to paper white — and it is the single most deliberate design decision on the site: every photographed piece, however exuberantly colored, is allowed to float against a ground that implies the studio worktable rather than the sterile gallery wall. Against that warmth, near-black #121212 carries all structural weight — navigation labels, price strings, section titles — with zero accent color interposing between the user and the object. The hairline gray #dedede shows up only as a quiet divider, never loud enough to compete with a column of beaded fringe or a collar made from brass stampings.

  Type is set in Avenir Next Medium for display and label work — a humanist geometric that has editorial confidence without the coldness of pure grotesques. AvenirNextLTPro-Regular handles running body copy and product descriptions, keeping the reading experience consistent with the display weight. Figtree provides a fallback geometric that matches the general proportions. The overall typographic register is restrained: letter-spacing is kept near zero, weights rarely exceed 600, and hierarchy is achieved through size steps rather than dramatic weight jumps.

  The interaction language is stripped to essentials. Buttons are rectangular with minimal rounding — the brand does not lean into pill shapes or soft corners; the jewelry is the expressive object, not the interface chrome. Product cards rely on clean white-space margins and large imagery. Navigation is horizontal and lean, with no mega-menus; the category list is short enough to sit in a single row. The handmade-in-NYC provenance comes through in editorial copy and imagery rather than UI badges, keeping the digital system as a transparent frame for the craft object rather than a marketing layer around it.

  At wide viewports, generous horizontal padding lets imagery breathe. On mobile, the cream canvas compresses gracefully around stacked product imagery. The overall effect is that of a well-lit SoHo showroom — spare enough that a single strand of vintage glass beads reads as the loudest thing in the room.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#9e9e9e"
  ink: "#121212"
  body: "#2e2e2e"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f5efeb"
  surface-soft: "#f5efeb"
  surface-card: "#ffffff"
  surface-neutral: "#f0ebe6"
  on-primary: "#f5efeb"
  on-dark: "#f5efeb"
  error: "#b00020"

typography:
  display-xl:
    fontFamily: "'Avenir Next Medium', 'AvenirNextLTPro-Regular', Figtree, Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Avenir Next Medium', 'AvenirNextLTPro-Regular', Figtree, Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Avenir Next Medium', 'AvenirNextLTPro-Regular', Figtree, Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Avenir Next Medium', 'AvenirNextLTPro-Regular', Figtree, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Avenir Next Medium', 'AvenirNextLTPro-Regular', Figtree, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'AvenirNextLTPro-Regular', 'Avenir Next Medium', Figtree, Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'AvenirNextLTPro-Regular', 'Avenir Next Medium', Figtree, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'AvenirNextLTPro-Regular', Figtree, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  label-uppercase:
    fontFamily: "'Avenir Next Medium', 'AvenirNextLTPro-Regular', Figtree, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Avenir Next Medium', 'AvenirNextLTPro-Regular', Figtree, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
  button-md:
    fontFamily: "'Avenir Next Medium', 'AvenirNextLTPro-Regular', Figtree, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Avenir Next Medium', 'AvenirNextLTPro-Regular', Figtree, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  price:
    fontFamily: "'AvenirNextLTPro-Regular', Figtree, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  announcement:
    fontFamily: "'Avenir Next Medium', 'AvenirNextLTPro-Regular', Figtree, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.05em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 12px
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 46px
    border: none
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 46px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "4/5"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    gap: "{spacing.sm}"
    rounded: "{rounded.none}"
  product-card-hover:
    imageOpacity: 0.92
    cursor: pointer
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-primary
    layout: "full-bleed image with centered or offset text overlay"
    minHeight: 80vh
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    padding: "{spacing.xl} 0"
    borderBottom: "1px solid {colors.hairline}"
  product-grid:
    columns: "4 desktop, 3 tablet, 2 mobile"
    gap: "{spacing.lg}"
    padding: "{spacing.xl} {spacing.xxl}"
    backgroundColor: "{colors.canvas}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "#ffffff"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    gap: "{spacing.xs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    height: 44px
    iconColor: "{colors.ink}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    subtotalTypography: "{typography.title-md}"
    overlayColor: "rgba(18,18,18,0.4)"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    padding: "{spacing.xxl} {spacing.xxl}"
    borderTop: none
  collection-filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    activeUnderline: "2px solid {colors.ink}"
    gap: "{spacing.lg}"

## Components

### Buttons

**`button-primary`** — Full-width or auto-width rectangle with zero border-radius, near-black #121212 fill, and warm-cream #f5efeb text set in uppercase Avenir Next Medium at 13px with 0.08em tracking. Height locks at 46px. Hover darkens to absolute black #000000; disabled state drops to #9e9e9e fill. The sharp corners align with the brand's preference for editorial restraint over friendly pill shapes — the interface steps back so the jewelry reads as the expressive object.

**`button-secondary`** — Transparent fill with a 1px #121212 border and matching ink text. On hover it inverts: fills to #121212 with cream text. Used for secondary CTAs like "Continue Shopping" or "View All" within collection pages. Shares the same 46px height and uppercase tracking as `button-primary` to keep the two visually weighted on the same baseline.

### Navigation

**`nav-bar`** — 56px tall, canvas-colored (#f5efeb) with a 1px #dedede bottom border. The brand wordmark sits center or left in `{typography.display-sm}` Avenir Next. Category links are sparse — Jewelry, Collections, About — at 13px/500-weight with 0.04em tracking. Cart icon and search icon sit at right; no mega-menus. The `announcement-bar` above it is a full-width black stripe (36px) for promotions in cream uppercase type.

### Product Card

**`product-card`** — No border-radius, white surface card with a 4:5 portrait image aspect ratio. Product name uses `{typography.body-md}` in ink; price runs in `{typography.price}` at muted body weight below. Hover reduces image opacity to 0.92 to signal interactivity without motion complexity. `badge-new` and `badge-sale` chips overlay the top-left corner in sharp rectangles.

### Hero

**`hero-editorial`** — Full-bleed image at 80vh minimum with the wordmark and a short headline in `{typography.display-xl}` (40px/500 weight). Text may sit centered over the image or offset-left on a cream half-panel. CTA is `button-primary`. The canvas-colored areas surrounding cropped editorial shots reinforce the studio-light aesthetic.

### Collection Grid

**`product-grid`** — Four columns desktop, three tablet, two mobile with `{spacing.lg}` gutters. Background is the warm canvas #f5efeb rather than white, so the entire browse experience feels continuous with the editorial canvas. No card borders or shadows — products sit directly on the ground.

### Cart Drawer

**`cart-drawer`** — 400px right-side drawer over a 40%-opacity near-black scrim. Canvas background, ink text, hairline-bordered line items. "Checkout" button is `button-primary` at full drawer width. The drawer pattern keeps the user on the PDP rather than navigating to a separate cart page.

### Footer

**`footer`** — Near-black #121212 fill with warm-cream text and links — an inversion of the page canvas, marking a clear visual close. Section headings use `{typography.label-uppercase}` (11px/600/0.1em tracking); link columns use `{typography.body-sm}`. Newsletter input is inline with a `button-secondary` in inverted colors.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column nav collapses to hamburger; product grid drops to 2 columns; hero text stacks below image; cart drawer goes full-width |
| Tablet | 744–1128px | 3-column product grid; nav shows abbreviated link row; hero returns to side-by-side layout |
| Desktop | 1128–1440px | 4-column product grid; full horizontal nav with all category links visible; hero at 80vh with text overlay |
| Wide | > 1440px | Max content width caps around 1400–1600px with symmetric horizontal padding; hero imagery scales but text container stays centered |

### Touch Targets

- All buttons minimum 44px height on mobile
- Nav icons (cart, search, hamburger) minimum 44×44px tap area
- Product card tap target covers the full image+title+price block
- Filter chips minimum 36px height with generous horizontal padding

### Collapsing Strategy

- Primary nav → hamburger drawer at < 744px; drawer slides in from left over canvas overlay
- Footer columns → stacked accordion on mobile with `{typography.label-uppercase}` toggle headers
- Product filters → bottom sheet on mobile rather than inline filter bar
- Announcement bar stays pinned and full-width at all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only three hex values were extracted (#f5efeb, #dedede, #121212); hover states, sale-red, and any accent colors used in editorial imagery are inferred from brand conventions, not observed
- Exact border-radius values on interactive elements could not be confirmed — zero radius is assumed based on the brand's editorial positioning, but some components may use 2–4px
- Font sizing for display headlines was not directly measured; the scale above is inferred from the Avenir Next stack and standard Shopify theme proportions
- Figtree appears in the font stack but its exact role (body fallback vs. primary) is ambiguous without JS execution
- Animation/transition timing on hover states and drawer open/close could not be extracted
- Grid gutter and section padding exact pixel values are estimated; live measurement via DevTools would confirm
- Whether the nav is sticky or static on scroll was not confirmed from the extracted data
