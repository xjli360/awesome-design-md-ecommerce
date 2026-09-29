---
version: alpha
name: "Telescope Casual"
source_url: "https://www.telescopecasual.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  One hundred and twenty-three years of bending aluminum in Granville, New York, and the website still opens with a full-bleed photograph of a powder-coated dining set on a flagstone patio — no headline, no tagline overlay, just the furniture doing the talking the way it has since 1903. The sole extracted brand color is a deep cobalt navy (`#003399`) that appears in the logo mark and principal navigation accents, the kind of blue you see on a beach-club awning before it fades in the salt air. It carries every primary button, every active link, and the thin rule that separates the header from the hero carousel, while the rest of the interface retreats to a white canvas and a disciplined ladder of warm grays — `#333333` for body copy, `#666666` for secondary labels, `#e0e0e0` for hairline dividers. There is no second accent; the palette is a monochrome stage for product photography where sling fabrics and cushion patterns supply all the chromatic energy. Typography could not be extracted from the live site (CSS loads via JavaScript), but the rendered pages read as a neutral, medium-weight sans-serif in the Helvetica/Arial lineage — headings in weight 700 at 28–36px, body at 15–16px in weight 400, all-caps navigation links spaced wide at 12–14px. Corners are overwhelmingly square: buttons, cards, and inputs present hard `{rounded.none}` edges that echo the straight aluminum tube-stock the factory bends into frames and stretchers. The only soft radius lives on the pill-shaped search toggle (`{rounded.full}`) triggered by Cmd+K. Layout follows a dealer-and-retailer model rather than direct e-commerce: product cards link to specification pages and "Find a Retailer" prompts instead of add-to-cart flows, and the navigation tree goes three levels deep — Collection → Material → Individual Piece — reflecting a manufacturer's catalog logic rather than a lifestyle boutique's curated grid. A Room Planner tool, virtual showroom tour, and downloadable PDF catalogs sit prominently in the feature strip below the hero, positioning the site as a configurator for trade buyers as much as an inspiration board for consumers. The footer carries the family-owned, made-in-the-USA provenance line alongside dealer login, social links, and a phone number — old-school trust signals that pair with the no-nonsense navy-and-white interface.

colors:
  primary: "#003399"
  primary-active: "#002477"
  primary-disabled: "#99b3d9"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#e8e8e8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  navy-dark: "#001f5c"
  accent-usa: "#bf0d0d"
  star-rating: "#1a1a1a"
  scrim: "#000000"
  error: "#c0392b"
  success: "#27874a"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  nav-dropdown:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
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
  section: 72px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  search-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  search-pill-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    borderColor: "{colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
    textColor: "{colors.ink}"
  text-input-error:
    borderColor: "{colors.error}"
    textColor: "{colors.ink}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-dropdown-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-dropdown}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.lg}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "4:3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-subtitle:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-collection-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-carousel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 0
    height: 520px
  hero-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.35
  hero-cta:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
  feature-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.xxl} 0"
  feature-strip-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  catalog-download-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 20px
  dealer-login-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    padding: 0
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
  collection-nav-item:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0"
  collection-nav-item-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.title-md}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    cellPadding: "{spacing.sm} {spacing.base}"
  spec-table-stripe:
    backgroundColor: "{colors.surface-soft}"
  room-planner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  find-retailer-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  usa-badge:
    backgroundColor: "{colors.navy-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-heading:
    typography: "{typography.uppercase-tag}"
    textColor: "{colors.on-dark}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  footer-provenance:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted-soft}"
  social-icon:
    textColor: "{colors.muted-soft}"
    size: 20px
  social-icon-hover:
    textColor: "{colors.on-dark}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
  accordion-header:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  load-more-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    borderWidth: 1px
    borderColor: "{colors.primary}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"

## Components

### Buttons
**`button-primary`** — The primary CTA is a solid navy rectangle (`#003399`) with white text set in Helvetica Neue at 15px weight 600. It stands 48px tall with zero border-radius, consistent with the straight-line geometry of the brand's aluminum tube furniture. On hover it deepens to `#002477`; when disabled it washes to a pale steel blue (`#99b3d9`). Padding is 14px vertical, 28px horizontal, giving the button a wide, grounded proportion. **`button-secondary`** — A white-fill outlined button with a 1px `#e0e0e0` border and ink-colored text. On hover the fill shifts to `#f5f5f5`. Same 48px height and squared corners. Used for secondary actions like "Download Catalog" alongside a primary "Find a Retailer." **`button-tertiary-text`** — A text-only ghost button in the navy primary, used for inline actions like "View All" and "Learn More" where a full button would be visually heavy. **`load-more-button`** — An outlined variant with a navy border and navy text on a transparent background, used at the bottom of product grids to paginate results without a full page reload.

### Cards
**`product-card`** — Product cards are borderless white containers with sharp corners and no drop shadow, letting the product photograph — typically a 4:3 aspect-ratio shot of the piece on a patio or plain background — carry all visual weight. The collection name appears as a small navy badge (`{typography.badge}`, `{rounded.xs}`) in the upper-left of the image. Below the image, the product title sits in `{typography.title-sm}` in ink, with a subtitle line in `{typography.caption}` in muted gray identifying the sub-collection or material type. On hover, the entire card gains a subtle `#f5f5f5` background. There is no price displayed — this is a manufacturer's catalog, not a storefront — so the card instead links to a specification page or a "Find a Retailer" prompt. **`feature-strip-card`** — Square image tiles used in the feature strip below the hero for Room Planner, Catalog Downloads, Virtual Showroom Tour, and About Us. Each card is a white rectangle with `{spacing.base}` padding and a title in `{typography.title-sm}`.

### Navigation
**`nav-bar`** — An 80px-tall white header strip anchored by the Telescope Casual logo on the left and a dealer-login link and phone number on the right. Primary navigation links (Collections, Retailers, Catalog Archive) sit center-left in all-caps `{typography.nav-link}` with 1px letter spacing. The active link turns navy; inactive links remain ink. A thin 1px `#e0e0e0` border separates the nav from the content below. **`nav-dropdown-panel`** — Dropdown menus open as flat, unshadowed white panels (or with a barely-there 4px box shadow) containing two or three columns of links in `{typography.nav-dropdown}`. The Collections dropdown is the deepest, going three levels: material category (Cushion, Sling, Polymer, Aluminum), sub-category (by table-top type or frame finish), and individual collection names. **`search-pill`** — A pill-shaped search trigger (`{rounded.full}`) with a soft gray fill, activated by Cmd+K. On focus, it gains a white background and a navy border. **`breadcrumb`** — A simple text trail in `{typography.caption}` muted gray, with the current page in ink and a hairline-colored separator.

### Hero
**`hero-carousel`** — A full-width image carousel at 520px tall showcasing lifestyle photography of the 2026 collection — patio dining scenes, poolside loungers, fire-table gatherings. Seven slides rotate with simple crossfade transitions. No headline text overlays the images by default; the photography is the message. When a text overlay does appear, it uses `{typography.display-xl}` in white against a dark scrim (35% opacity black). The hero CTA inverts the usual button pattern: white fill with navy text, creating contrast against the photographic backdrop. **`feature-strip`** — A soft-gray band (`#f5f5f5`) immediately below the hero containing four equally-spaced image-and-label tiles linking to the Room Planner, catalog PDF downloads, the factory virtual tour, and the "About Telescope" story. Each tile uses `{typography.title-sm}` below a square thumbnail.

### Specification Tables
**`spec-table`** — Product detail pages display material specs, dimensions, and finish options in a clean two-column table. Headers use `{typography.title-sm}` in ink; body cells use `{typography.body-sm}` in body gray. Alternating rows receive a `#f5f5f5` stripe. Borders are 1px `#e0e0e0`. Cell padding is 8px vertical, 16px horizontal.

### Dealer & Retailer
**`find-retailer-button`** — The primary conversion button on product pages, styled identically to `button-primary` but semantically distinct. It drives users to the dealer-locator flow rather than an add-to-cart action. **`dealer-login-link`** — A small navy text link in `{typography.caption}` positioned in the header utility row, providing trade-buyer access to wholesale ordering and account management. **`usa-badge`** — A compact dark-navy badge (`#001f5c`) with white uppercase text reading "MADE IN USA SINCE 1903," displayed on hero slides and footer. Uses `{typography.badge}` with `{rounded.xs}`.

### Footer
**`footer`** — A full-width section with a near-black background (`#1a1a1a`) and four content columns: Our Company, Dealers, Media, and Recent News. Column headings use `{typography.uppercase-tag}` in white. Links are set in `{typography.link}` at muted gray (`#999999`) and brighten to white on hover. The provenance tagline ("Producing Quality Furniture in the USA Since 1903") sits in `{typography.caption-sm}` in muted-soft gray. Social icons (Facebook, Twitter, YouTube) are 20px muted-gray glyphs that turn white on hover. The footer uses 48px vertical padding.

### Accordion
**`accordion`** — Used on product detail pages for collapsible sections (Description, Dimensions, Materials, Care Instructions). The header uses `{typography.title-md}` in ink with 16px vertical padding. Content uses `{typography.body-md}` in body gray. No borders or background — hierarchy comes from typography weight alone. On mobile, tabbed content collapses into this accordion pattern.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; hero carousel drops to 320px tall; product cards stack vertically; feature-strip tiles stack 2×2; footer columns collapse to accordion; search pill becomes full-width bar; three-level nav dropdown becomes slide-in drawer |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses `{typography.display-lg}` at 420px tall; feature-strip shows 2×2 grid; footer uses two-column layout; dropdown menus remain flyout panels |
| Desktop | 1128–1440px | Three-column product grid; full 80px nav bar with all links and dealer-login; hero at 520px with `{typography.display-xl}`; feature-strip in a single row of four tiles; footer in four columns; hover states active on product cards |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to four columns; hero section gains additional lateral padding; whitespace scales proportionally; spec tables widen to fill available space |

### Touch Targets
- All interactive elements (buttons, links, inputs) meet a 44×44px minimum touch target on mobile.
- Product card taps navigate to specification pages; no hover states on touch devices.
- Accordion headers have a 48px minimum tap height.
- Nav hamburger icon is 44×44px with 16px inset padding.
- Footer links have 44px row height for comfortable thumb tapping.

### Collapsing Strategy
- Top nav collapses to a hamburger menu at < 744px; the three-level Collections tree becomes a slide-in drawer with expandable sections.
- Feature-strip tiles reflow from a single row to a 2×2 grid on tablet and a stacked list on small mobile.
- Footer columns collapse to accordion sections with tappable headers on mobile.
- Spec tables become vertically stacked label–value pairs on mobile (no horizontal scroll).
- Search pill collapses to a search icon in the nav bar; tapping expands a full-width input.
- Breadcrumb truncates to the parent level and a back-arrow on mobile.
- Hero carousel controls shift from side arrows to swipe gestures with dot indicators below the image.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only a single hex color (`#003399`) was extractable from the live site; all other palette tokens (grays, active/disabled states, accent-usa red) are inferred from visual inspection and common conventions. The site likely loads its full stylesheet via JavaScript, blocking static extraction.
- No font-family stacks were extractable. Typography is specified as Helvetica Neue / system sans-serif based on visual similarity; the actual typeface may be a licensed web font loaded asynchronously.
- No border-radius values were directly extracted; the squared-corner default is based on visual observation of rendered buttons and cards.
- Button dimensions, padding, and hover colors are inferred from the site's visual rendering, not from inspected CSS values.
- The `accent-usa` red (`#bf0d0d`) is not extracted but inferred from the patriotic "Made in USA" motif common to the brand's marketing; it may not appear in the digital interface.
- The hero carousel height (520px), transition style, and slide count (7) are approximations from the homepage; exact values may vary by viewport or CMS configuration.
- Product card aspect ratios and image sizing are estimated from rendered thumbnails; the CMS may serve different crops.
- The Room Planner tool is an embedded third-party application; its internal UI tokens are not covered by this design system.
- Dark mode is not implemented on the live site; no dark-mode tokens are defined.
- The dealer-login and wholesale portal likely use a separate interface with its own design tokens not captured here.
- The site is not on Shopify and appears to be a custom CMS; platform-specific component conventions do not apply.
- Error states for forms, empty states for search results, and loading skeleton patterns were not visible on the live site and are best-guess implementations.
- The three-level navigation depth (Collection → Material → Piece) may use additional typographic or color differentiation at the third level that was not extractable.
