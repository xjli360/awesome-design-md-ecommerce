---
version: alpha
name: "Kino Lorber"
source_url: "https://kinolorber.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-catalog cinema label that uses electric cyan (#1a9cfc) as its primary voltage — not as a background wash but as sharp accent lines, active-state underlines, and the glow behind "Shop Now" buttons. The site reads like a film-society bulletin board: a dense, text-forward grid on a near-white canvas (#f8f8f8) where every title, director credit, and price tag sits in stacked Lato or Montserrat at modest sizes. A secondary teal (#03dfdc) appears in sale badges and limited-edition callouts, while a deep near-black (#1e1e1e) carries body copy and navigation text. The typographic palette is workhorse — Abril Fatface reserved for hero display headers that anchor seasonal collections, then Lato and Montserrat handling everything from product titles to footer links. Cards use soft rounded corners ({rounded.sm}) and hairline borders (#e5e5e5) that keep the grid airy despite the information density. The brand trusts its catalog photography over decorative imagery; product cards are compact, text-heavy rectangles where the film poster does the emotional work and the typography stays clean and utilitarian. A persistent top nav in near-black (#1e1e1e) with white text and a search bar in the same cyan accent (#1a9cfc) gives the experience a library-meets-marketplace feel — scholarly but transactional, designed for cinephiles who know what they want.

colors:
  primary: "#1a9cfc"
  primary-active: "#1587d8"
  primary-disabled: "#b7ddfc"
  ink: "#1e1e1e"
  body: "#222222"
  muted: "#323232"
  muted-soft: "#b7b7b7"
  hairline: "#e5e5e5"
  hairline-soft: "#ededed"
  canvas: "#f8f8f8"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#03dfdc"
  accent-teal-active: "#03dfdb"
  sale-red: "#e31937"
  gold: "#f1c40f"
  gold-active: "#e2bc0f"
  error: "#bf6b69"
  error-dark: "#5d0e07"

typography:
  display-xl:
    fontFamily: "'Abril Fatface', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Abril Fatface', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Lato', 'Montserrat', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
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
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-accent-teal-active:
    backgroundColor: "{colors.accent-teal-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 14px
    height: 30px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 0 16px
  nav-bar-search:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    height: 400px
  hero-banner-subtitle:
    typography: "{typography.title-lg}"
    textColor: "{colors.muted-soft}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 32px 16px
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-gold-active:
    backgroundColor: "{colors.gold-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in electric cyan (#1a9cfc) with white text. Used for "Add to Cart", "Shop Now", and primary checkout flows. On hover, shifts to `{colors.primary-active}` (#1587d8). Disabled state uses `{colors.primary-disabled}` (#b7ddfc) with reduced opacity feel.

**`button-secondary`** — A white button with dark text for secondary actions like "View Details" or "Learn More". Uses a 1px hairline border (#e5e5e5) on hover to define the edge. No background fill in default state.

**`button-accent-teal`** — Reserved for limited-edition drops, pre-order campaigns, and special collections. Uses the brand's secondary cyan (#03dfdc) with dark text. Active state shifts to #03dfdb.

**`button-sale`** — Compact, urgent button for sale-priced items. Uses a deep red (#e31937) with white text. Smaller padding and font size to fit within product card real estate.

### Cards
**`product-card`** — The core inventory unit: a white rectangle with soft 8px corners, 12px internal padding, and a 1px hairline border (#e5e5e5). Contains a film poster (full-width, top), title in `{typography.title-sm}`, director credit in `{typography.body-sm}`, and price in `{typography.body-md}`. Optional badges overlay the top-left corner.

**`product-card-badge`** — Teal badge for "New Release", "Exclusive", or "Limited Edition". Sits at the top-left of the product card image. Uses uppercase `{typography.badge}` with tight 2px/8px padding.

**`product-card-badge-sale`** — Red badge for discounted items. Same dimensions as the teal badge but uses `{colors.sale-red}` background for urgency.

### Navigation
**`nav-bar`** — A persistent 56px top bar in near-black (#1e1e1e) with white navigation links. Contains the Kino Lorber logo (left), category links (center), and a search bar (right). The search bar uses the primary cyan as its background, creating a distinctive visual anchor.

**`nav-bar-link`** — White text on dark background, 14px weight-600 Lato/Montserrat. Active state uses `{colors.primary}` underline. Hover state adds a subtle opacity shift.

**`nav-bar-search`** — A compact 36px search input with cyan background and white text. Uses `{rounded.sm}` corners. Placeholder text in white at reduced opacity.

### Forms
**`text-input`** — Standard form input for search, account forms, and checkout. White background with 1px hairline border (#e5e5e5). Focus state uses `{colors.primary}` border. Error state uses `{colors.error}` (#bf6b69) border.

### Footer
**`footer`** — Full-width dark section (#1e1e1e) with muted gray text (#b7b7b7). Contains columns for customer service, about links, and social icons. Links use `{typography.link}` and hover to `{colors.primary}`. Padding is generous at 32px vertical.

### Badges
**`badge-gold`** — Used for award-winner indicators, critic's picks, and festival selections. Gold background (#f1c40f) with dark text. Active state shifts to #e2bc0f.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero banner height reduces to 200px; search bar moves to expandable overlay |
| Tablet | 744–1128px | Two-column product grid; nav links visible but truncated; hero at 300px; search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at 400px; search bar always expanded |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero at 450px with wider typography |

### Touch Targets
- All buttons and links maintain minimum 44px tap target height on mobile
- Search bar expands to full-width overlay on mobile for easy one-handed use
- Product card images are tappable with no minimum height below 120px

### Collapsing Strategy
- Navigation links collapse into hamburger menu below 744px
- Category strip collapses into a horizontal scrollable row on mobile
- Footer columns stack vertically below 744px
- Product card badges reduce font size to 10px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for text links and secondary buttons not fully extracted — inferred from common patterns
- Error styling for form validation (red border on text-input inferred from #bf6b69 presence)
- Dark mode not detected on live site — no theme-color meta tag found
- Sub-brand palettes (Kino Lorber Studio Classics, Kino Cult, etc.) not distinguishable from extracted data
- Dropdown menu styling for category navigation not captured
- Modal/overlay styling for quick-view or video player not extracted
- Loading states and skeleton screens not present in extracted data
- The extracted color list is heavily weighted toward blues and grays with a few accent colors — the brand's true palette may include additional accent colors not captured in the top 30 hex values
- Font weight and line-height values are estimated based on common web typography patterns — exact values may vary
- Animation durations and easing curves not extracted from live site
