---
version: alpha
name: "Panasonic"
source_url: "https://www.panasonic.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep corporate blue — the same saturated #0054a6 that has anchored the Panasonic wordmark since the 1970s — floods every hero banner, primary CTA, and nav accent across panasonic.com, making it one of the most color-stable identities in consumer electronics. The site for home appliances like microwaves and toaster ovens runs a utilitarian grid: tall product hero images shot on neutral backgrounds, specification tables with alternating `{colors.surface-soft}` and `{colors.canvas}` rows, and comparison trays that slide up from the bottom of the viewport. Typography leans on a system-sans stack headed by Arial and Helvetica Neue at conservative weights — display headings sit at 600 weight and 32–40px rather than the bolder treatments fashion or lifestyle brands reach for, reinforcing an engineering-first voice where the product photograph does the selling and the type stays out of the way. Buttons are squared-off at `{rounded.xs}` with generous 48px touch heights, occasionally stepping up to a subtle `{rounded.sm}` on promotional landing pages; there is almost no use of pill shapes or circular elements outside of the search icon. A secondary warm-black `{colors.ink}` (#1a1a1a) carries body copy, while `{colors.muted}` (#717171) handles meta-labels like model numbers, wattage specs, and breadcrumbs. Accent orange (#e87722) appears sparingly — limited to sale badges, promotional banners, and the occasional "New" tag — providing the only warm interruption in an otherwise cool-toned palette. The canvas is bright white (`{colors.canvas}` #ffffff), cards sit on the same white with a 1px `{colors.hairline}` border rather than shadow, and the overall rhythm is dense: `{spacing.lg}` between card rows, `{spacing.base}` gutters, and `{spacing.section}` vertical breathing room between feature blocks. Footer and mega-nav backgrounds drop to a near-black (#1a1a1a) with white type, creating a hard bookend that frames the content cleanly.

colors:
  primary: "#0054a6"
  primary-active: "#003d7a"
  primary-disabled: "#9dbde0"
  accent: "#e87722"
  accent-active: "#cf6510"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#717171"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e8e8e8"
  border-strong: "#b3b3b3"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#eeeeee"
  surface-dark: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent: "#ffffff"
  error: "#d32f2f"
  success: "#2e7d32"
  star-rating: "#f5a623"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  spec-value:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  button-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-mega-heading:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  price-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
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
  section: 64px
  hero: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary-active}
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
    textDecoration: underline on hover
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.error}
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px 12px 44px
    height: 48px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    logoColor: "{colors.primary}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 2px 8px rgba(0,0,0,0.08)
  mega-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.nav-mega-heading}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    borderTop: 1px solid {colors.hairline}
    boxShadow: 0 8px 24px rgba(0,0,0,0.12)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-md}"
    modelTypography: "{typography.caption}"
    hoverBorder: 1px solid {colors.border-strong}
    hoverShadow: 0 4px 16px rgba(0,0,0,0.08)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    aspectRatio: 1 / 1
    objectFit: contain
    padding: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    ctaStyle: button-primary or button-accent
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    aspectRatio: 4 / 3
    hoverTransform: scale(1.02)
    transition: transform 200ms ease
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowBorder: 1px solid {colors.hairline-soft}
    padding: 12px 16px
    alternateRowBg: "{colors.surface-soft}"
  comparison-tray:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    boxShadow: 0 -4px 24px rgba(0,0,0,0.12)
    padding: "{spacing.base}"
    maxProducts: 4
    borderTop: 3px solid {colors.primary}
  badge-new:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
  star-rating:
    filledColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: 2px
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: 3px solid {colors.primary}
  footer-bottom:
    backgroundColor: "#111111"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.base} {spacing.xl}"
  where-to-buy:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
    retailerLogoHeight: 32px
    ctaTypography: "{typography.button-md}"
    ctaColor: "{colors.primary}"
  feature-highlight:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    imagePosition: alternating left-right
    padding: "{spacing.section} 0"
    gap: "{spacing.xl}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    optionTypography: "{typography.body-sm}"
    checkboxColor: "{colors.primary}"
    width: 260px
    padding: "{spacing.lg}"
    borderRight: 1px solid {colors.hairline-soft}
  toast-notification:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
    boxShadow: 0 4px 16px rgba(0,0,0,0.2)

---

## Components

### Buttons

**`button-primary`** — Solid Panasonic blue (#0054a6) rectangle with white text at 600 weight and `{rounded.xs}` corners. On hover, background deepens to `{colors.primary-active}` (#003d7a). Disabled state desaturates to `{colors.primary-disabled}`, a pale sky blue that reads as clearly inactive. Minimum touch-target height of 48px with 14px vertical / 28px horizontal padding.

**`button-secondary`** — White fill with a 2px `{colors.primary}` border and blue text. On hover, the background tints to `{colors.surface-soft}` and the border darkens to `{colors.primary-active}`. Used alongside primary buttons for secondary actions like "Compare" or "View Specs."

**`button-tertiary`** — No background or border; blue text with an underline that appears on hover. Used inline within body copy or spec sections for "Learn more" and "See all features" links.

**`button-accent`** — Solid orange (#e87722) with white text, reserved exclusively for promotional CTAs like "Shop Sale" or limited-time offers. Same dimensions and radius as `button-primary`.

**`button-dark`** — Near-black background (#1a1a1a) with white text. Used within dark hero banners or the footer where a blue button would lack contrast against dark imagery.

### Navigation

**`nav-bar`** — 64px-tall white bar with a 1px `{colors.hairline}` bottom border. The Panasonic wordmark sits left in `{colors.primary}` blue. Navigation links use `{typography.nav-link}` (14px/600) with hover underline. On scroll, the bar gains a subtle box-shadow and the bottom border drops out, creating a floating effect. Right side holds search icon, cart icon, and hamburger on mobile.

**`mega-nav`** — Full-width dropdown that appears below the nav bar with a 1px top border and soft drop shadow. Product categories are organized in columns with bold `{typography.nav-mega-heading}` headers. Each column lists 6–8 subcategory links in `{typography.body-sm}`. A featured product image may appear in the rightmost column as a promotional slot.

### Product Cards

**`product-card`** — Vertical card with a square product image area (1:1 aspect, `contain` fit, `{colors.surface-soft}` background) above a text block. Product name in `{typography.title-sm}`, model number in `{typography.caption}` / `{colors.muted}`, and price in `{typography.price-md}` / `{colors.ink}`. A thin `{colors.hairline-soft}` border wraps the card at `{rounded.xs}`. On hover, the border strengthens and a gentle shadow lifts the card. Star rating appears below the model number when reviews exist.

**`product-card-image`** — The image area uses `{colors.surface-soft}` as a neutral backdrop with generous `{spacing.lg}` padding so that microwave and toaster oven product shots float cleanly without cropping.

### Hero

**`hero-banner`** — Full-bleed dark background (often a lifestyle photograph with a dark overlay) at minimum 480px height. Headline in `{typography.display-xl}` white text, subhead in `{typography.body-lg}`, and a CTA using either `button-primary` or `button-accent`. Text is left-aligned on desktop, occupying roughly 50% of the width.

**`hero-banner-light`** — Same structure on a light `{colors.surface-soft}` background with `{colors.ink}` text. Used for product launch pages where the hero image is a clean product shot on white.

### Specification Table

**`spec-table`** — Two-column table with alternating row backgrounds (`{colors.canvas}` and `{colors.surface-soft}`). Labels in `{typography.spec-label}` (14px/600), values in `{typography.spec-value}` (14px/400). Rows separated by 1px `{colors.hairline-soft}` lines. Section headers span both columns with `{colors.surface-soft}` background and `{typography.title-sm}` bold text. Critical for appliance pages where wattage, dimensions, capacity, and features must be scannable.

### Comparison Tray

**`comparison-tray`** — Sticky bottom tray that slides up when the user adds products to compare. A 3px `{colors.primary}` top border anchors it visually. Up to 4 product thumbnails sit in a row with model names and a "Compare Now" `button-primary`. The tray casts a top shadow to separate it from the page content below.

### Badges

**`badge-new`** — Small orange (#e87722) pill with "NEW" in `{typography.badge}` white uppercase text. Positioned in the top-left corner of product card images with absolute positioning.

**`badge-sale`** — Red (#d32f2f) variant using the same dimensions and typography. Displays percentage or dollar-off messaging.

### Where to Buy

**`where-to-buy`** — Card-style module listing authorized retailers. Each row shows a retailer logo (32px height), availability status, and a "Buy Now" link in `{colors.primary}`. Separated by `{colors.hairline}` dividers. Rounded at `{rounded.sm}` with a single-pixel border.

### Feature Highlight

**`feature-highlight`** — Alternating image-and-text sections that step down the page. Each block pairs a large product detail photograph with a `{typography.display-md}` headline and `{typography.body-md}` paragraph. Images alternate left and right across rows. Vertical spacing of `{spacing.section}` between each block. Used to showcase Inverter Technology, sensor cooking, and other marquee features.

### Filter Sidebar

**`filter-sidebar`** — 260px-wide left rail on category listing pages. Section headings in `{typography.title-sm}`, checkbox options in `{typography.body-sm}`. Checkboxes use `{colors.primary}` fill when selected. A `{colors.hairline-soft}` right border separates the sidebar from the product grid. On mobile, this collapses into a slideover drawer triggered by a "Filter" button.

### Breadcrumb

**`breadcrumb`** — Horizontal text trail in `{typography.caption}` using `{colors.muted}` for ancestor links and `{colors.ink}` for the current page. Chevron separators in `{colors.muted-soft}`. Positioned below the nav bar with `{spacing.base}` top margin.

### Star Rating

**`star-rating`** — 16px filled/empty star icons using `{colors.star-rating}` (gold) and `{colors.hairline}` (empty). Review count follows in `{typography.caption}` / `{colors.muted}` wrapped in parentheses.

### Footer

**`footer`** — Dark background (#1a1a1a) with a 3px `{colors.primary}` blue top border. Content organized in 4–5 columns: Products, Support, About, Connect. Column headings in `{typography.title-sm}` white, links in `{typography.body-sm}` / `{colors.hairline}` that brighten to white on hover. Social media icons sit in the Connect column at 24px size.

**`footer-bottom`** — Even darker strip (#111111) below the main footer carrying copyright, legal links, and region selector in `{typography.caption}` / `{colors.muted-soft}`.

### Toast Notification

**`toast-notification`** — Dark (#1a1a1a) rounded bar that slides in from the bottom-right of the viewport. White text in `{typography.body-sm}` with `{rounded.sm}` corners and a drop shadow. Used for "Added to comparison" and "Item saved" confirmations. Auto-dismisses after 4 seconds.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Nav collapses to hamburger + search icon. Hero text stacks above image. Mega-nav becomes full-screen slideover. Filter sidebar becomes bottom-sheet drawer. Comparison tray shows 2 products max. Spec table scrolls horizontally. |
| Tablet | 744–1128px | Two-column product grid. Nav shows top-level links, mega-nav triggers on tap. Hero text overlays image at 60% width. Filter sidebar remains as collapsible left rail. Feature highlights stack image above text. |
| Desktop | 1128–1440px | Three- to four-column product grid. Full mega-nav on hover. Hero split layout (text left, image right). Sidebar filter always visible. Comparison tray shows up to 4 products. Spec table renders full width. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Side margins grow symmetrically. Product grid stays at four columns. Hero image scales to fill but text container remains fixed-width. |

### Touch Targets
- All interactive elements maintain a minimum 48px tap target on mobile and tablet.
- Nav hamburger icon has a 48×48px hit area even though the visible icon is 24px.
- Checkbox and radio inputs in the filter sidebar use 44×44px tap zones.
- Card tap targets cover the full card surface; tap anywhere navigates to the PDP.

### Collapsing Strategy
- Navigation: horizontal link bar collapses to hamburger at < 744px; mega-nav becomes full-screen overlay.
- Product grid: 4 → 3 → 2 → 1 columns as viewport shrinks across breakpoints.
- Feature highlights: side-by-side image/text becomes stacked (image on top) below 744px.
- Footer columns: 4–5 columns collapse to accordion sections on mobile.
- Comparison tray: max products reduce from 4 → 2; horizontal scroll activates if needed.
- Spec tables: fixed left column with horizontal scroll on remaining columns below 744px.

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted**: The live site returned "Access Denied" (anti-bot / WAF), so zero hex colors were captured from the page. The primary blue (#0054a6) is Panasonic's widely documented corporate blue used across global marketing materials, packaging, and their brand guidelines. All other palette values are inferred from common Panasonic web patterns and should be validated against the live site when accessible.
- **No fonts extracted**: Zero font-family stacks were captured. Panasonic's web properties commonly use system sans-serif stacks (Arial / Helvetica Neue); some regional sites use a proprietary "Panasonic" webfont. The actual font stack should be verified via DevTools on an accessible page load.
- **No meta theme-color**: Could not confirm the mobile browser chrome color. Likely matches `{colors.primary}` (#0054a6) based on convention.
- **Accent orange unconfirmed**: The #e87722 orange used for promotional badges is based on observed patterns across Panasonic's marketing materials but was not extracted from the live DOM.
- **Rounded values estimated**: Without inspecting computed styles, border-radius values are estimated conservatively. Panasonic tends toward minimal rounding; actual values may be 2px or 3px rather than the 4px (`{rounded.xs}`) specified.
- **Component spacing unverified**: All padding, gap, and margin values are approximations based on visual patterns. Actual values from the CSS should be audited.
- **No Shopify platform detected**: The site does not appear to run on Shopify. E-commerce integration patterns (cart, checkout flow) may differ significantly from Shopify-based implementations.
