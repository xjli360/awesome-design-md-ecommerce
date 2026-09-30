---
version: alpha
name: "Burn Shop"
source_url: "https://theburnshopwf.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep teal where you expect ember orange — Burn Shop's palette opens on #226d7a, the color of oxidized steel grate left out on a Wichita Falls porch, and it saturates every primary CTA, category header, and icon highlight across the storefront. The choice is deliberate inversion: instead of telegraphing fire and smoke, the brand signals the cool confidence of a pitmaster who has already mastered the flame. Supporting tones cascade from that anchor — a bright cyan (#22b8d1) for hover states and accent links, a soft sky wash (#b0e0e9) for tags and surface highlights, and an almost-white ice (#e4f5fa) for background panels and section dividers. Typography runs a utilitarian Open Sans stack with Roboto and Arial as fallbacks, set at moderate weights that keep the focus on product photography — seared grates, charred brisket, cast-iron grill bodies shot against concrete. Display headings land at 600–700 weight without heavy letter-spacing tricks, and body copy stays at 400/16px for comfortable reading across recipe pages and product specs. Corner radii lean functional: `{rounded.sm}` on buttons and inputs, `{rounded.md}` on cards and modals, `{rounded.full}` reserved for badges and small indicator pills. The grid breathes through a consistent `{spacing.base}` (16px) rhythm, expanding to `{spacing.section}` (64px) between major content blocks. Product cards sit on a white `{colors.surface-card}` canvas with subtle `{colors.hairline}` borders, letting the photography and the teal accents do the selling. The overall system reads as clean, tool-oriented, and unapologetically midwestern — a hardware-store clarity applied to outdoor cooking gear, where the color story says "we care more about your cook than our logo."

colors:
  primary: "#226d7a"
  primary-active: "#1e6d7a"
  primary-dark: "#1a5862"
  primary-disabled: "#a3c9cf"
  accent-cyan: "#22b8d1"
  accent-cyan-active: "#1b9db4"
  accent-sky: "#b0e0e9"
  accent-ice: "#e4f5fa"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d1d5db"
  hairline-soft: "#e5e7eb"
  canvas: "#ffffff"
  surface-soft: "#f5f7f8"
  surface-card: "#ffffff"
  surface-teal: "#e4f5fa"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#c53030"
  error-light: "#fed7d7"
  success: "#276749"
  success-light: "#c6f6d5"
  star-rating: "#f59e0b"
  scrim: "#0a0a0a"

typography:
  display-xl:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Open Sans', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    padding: 14px 28px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  button-ghost-active:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.primary-dark}"
    rounded: "{rounded.sm}"
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-cyan-active:
    backgroundColor: "{colors.accent-cyan-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pill-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.primary}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-circle-active:
    backgroundColor: "{colors.accent-ice}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} 0"
    boxShadow: "0 8px 24px rgba(26, 26, 26, 0.1)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 36px
    height: 52px
  hero-overlay:
    backgroundColor: "rgba(26, 88, 98, 0.55)"
    textColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 16px rgba(34, 109, 122, 0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    backgroundColor: "{colors.surface-soft}"
  product-badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-badge-best-seller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  price-display:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  price-compare-at:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: "line-through"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  review-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-value:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  category-nav-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  category-nav-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
  feature-grid:
    gap: "{spacing.lg}"
  feature-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  feature-icon:
    color: "{colors.primary}"
    size: 32px
  testimonial-card:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  testimonial-author:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  trust-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.accent-sky}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  social-icon:
    color: "{colors.muted-soft}"
    size: 24px
  social-icon-hover:
    color: "{colors.accent-sky}"
  cart-icon:
    color: "{colors.ink}"
    size: 24px
  cart-count-badge:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  mobile-menu-toggle:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 48px
    width: 48px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary CTA rendered in Burn Shop's deep teal `{colors.primary}` (#226d7a) with white text on `{rounded.sm}` corners. On hover/active, the background shifts to `{colors.primary-active}` (#1e6d7a), a fractionally darker teal that creates a subtle pressed-in feel without dramatic color shift. The disabled state moves to `{colors.primary-disabled}`, a washed-out teal-gray that reads as clearly inactive. All primary buttons sit at 48px height with `{typography.button-md}` at 600 weight — assertive but not heavy.

**`button-secondary`** — A white-background outline button with a 2px `{colors.hairline}` border, used for "Compare," "View Details," and secondary actions alongside primary CTAs. On active state the border switches to `{colors.primary}`, pulling the teal accent into the interaction and establishing visual hierarchy. The 2px border weight ensures the button reads as intentional structure, not a browser default.

**`button-ghost`** — A borderless, transparent-background button with `{colors.primary}` text, used in breadcrumbs, accordion triggers, and in-card secondary actions. The active state fills with `{colors.surface-teal}` — the lightest teal wash — and darkens text to `{colors.primary-dark}`, providing a hit target without overwhelming the layout. Ghost buttons carry the full `{typography.button-md}` weight to maintain hierarchy parity with outlined counterparts.

**`button-accent-cyan`** — A high-energy accent button in bright cyan `{colors.accent-cyan}` (#22b8d1), reserved for hero CTAs, promotional banners, and "Shop Now" actions where the primary teal would blend too much into the surrounding palette. The cyan pops against both the dark hero backgrounds and the white product grid, functioning as the brand's "volume knob" when urgency is needed.

**`button-pill-teal`** — A fully rounded pill variant of the primary button using `{rounded.full}`, deployed for filter tags, sticky mobile CTAs, and promotional callouts. The pill shape reads as friendly and tappable, and the teal fill connects it to the primary system even in isolation.

**`button-pill-outline`** — A pill-shaped outline button with a 1px `{colors.primary}` border and teal text on a transparent background, used for filter toggles, "Clear All" actions, and category chips on product listing pages. The outline treatment keeps the teal present without creating visual density in filter bars with many options.

### Cards
**`product-card`** — The primary container for grill listings, accessories, and fuel products. A white `{colors.surface-card}` background with `{colors.hairline-soft}` border and `{rounded.md}` corners creates a clean frame that lets product photography — blackened steel grates, charcoal textures, chrome handles — dominate. On hover, the border strengthens to `{colors.hairline}` and a subtle teal-tinted shadow (`boxShadow` with rgba(34, 109, 122, 0.08)) lifts the card. The image area uses `{rounded.md}` on top corners only, with a `{colors.surface-soft}` background for loading states.

**`feature-item`** — Used in "Why Burn Shop" grids and comparison sections, these cards pair a 32px `{colors.primary}` icon with a heading and description on `{colors.surface-card}` with `{colors.hairline-soft}` borders. The `{rounded.md}` corners and `{spacing.lg}` padding match the product card system, maintaining visual consistency across the page.

**`testimonial-card`** — Customer review cards with a `{colors.surface-teal}` background — the lightest teal wash — that distinguishes them from the white product cards and creates a visual break in the page rhythm. The soft teal fill eliminates the need for a border, while the `{rounded.md}` corners keep them within the card system. Author names use `{typography.title-sm}` in `{colors.ink}` for attribution.

### Navigation
**`top-nav`** — A fixed 72px white bar with a `{colors.hairline-soft}` bottom border housing the logo, category links (Grills, Smokers, Accessories, Fuel, Recipes), search, cart, and account icons. Navigation links use `{typography.nav-link}` at 15px/600 weight — slightly heavier than body text to maintain presence against the product photography below. Active links are marked with a 2px `{colors.primary}` bottom border and teal text; inactive links sit in `{colors.muted}`.

**`nav-dropdown`** — Mega-menu panels on `{colors.canvas}` with `{rounded.sm}` corners and a soft box-shadow. The dropdown provides category-specific navigation (grill types, fuel types, accessories by category) with `{typography.body-md}` links in `{colors.body}`. Padding is set at `{spacing.sm}` vertical, with items spaced by `{spacing.xs}`.

**`category-nav-pill`** — Horizontal scrolling category pills used on collection pages, rendered in `{colors.surface-soft}` with `{typography.button-sm}` and `{rounded.full}`. The active pill fills with `{colors.primary}` and switches to white text, creating a clear selection indicator in the scrollable row.

**`promo-banner`** — A 40px-tall full-width bar in `{colors.primary}` with `{colors.on-primary}` text at `{typography.caption}` size, used for shipping thresholds, seasonal sales, and promotional codes. The banner sits above the top-nav and uses a compact height to avoid dominating the viewport.

### Forms
**`text-input`** — Standard form inputs for checkout, account creation, and contact forms. A white background with a 1px `{colors.hairline}` border and `{rounded.sm}` corners at 48px height. On focus, the border doubles to 2px and switches to `{colors.primary}`, providing a clear teal focus ring. Error states use a 2px `{colors.error}` border.

**`select-dropdown`** — Styled select elements matching the text-input dimensions — same `{colors.canvas}` background, `{colors.hairline}` border, `{rounded.sm}` corners, and 48px height. The consistent sizing ensures form elements read as a cohesive system across checkout and product configuration.

**`search-bar`** — A pill-shaped (`{rounded.full}`) search input on `{colors.surface-soft}` background, differentiating it visually from standard rectangular inputs. On focus, the background clears to `{colors.canvas}` and a 2px `{colors.primary}` border appears. The pill shape signals "search" at a glance without needing a magnifying glass icon as the sole affordance.

**`newsletter-input`** — A footer-context input paired with the `newsletter-submit` button. The input matches standard `{colors.canvas}` and `{colors.hairline}` styling, while the submit button uses `{colors.primary}` to draw the eye. The pair creates a high-contrast capture point against the dark `{colors.ink}` footer background.

### Badges
**`product-badge-new`** — A fully rounded pill in bright `{colors.accent-cyan}` (#22b8d1) with white text, used to flag newly launched grills and accessories. The cyan stands out from the primary teal, creating a visual distinction between "brand color" and "attention signal." The `{typography.badge}` uppercase styling at 11px keeps the badge compact.

**`product-badge-sale`** — A red `{colors.error}` badge for clearance and discount items, deliberately breaking from the teal palette to create urgency. The red is the only warm color in the system, making sale badges impossible to overlook against the cool teal-and-white product grid.

**`product-badge-best-seller`** — A deep teal `{colors.primary}` badge that marks the brand's hero products. Using the primary color for best-seller status reinforces brand affinity — the best-seller badge feels like an endorsement from the house, not a generic sticker.

### Product Details
**`spec-table-label`** — Technical specification labels (BTU, cooking area, fuel type, weight) in `{typography.spec-label}` — 13px uppercase at 700 weight with `{colors.muted}` text. The uppercase treatment distinguishes spec metadata from body prose, creating a scannable reference for buyers comparing grill models.

**`spec-table-value`** — Specification values in `{typography.body-sm}` at `{colors.ink}`, paired with their labels across a `{colors.hairline-soft}` horizontal divider. The darker ink weight against the muted labels creates a clear visual hierarchy within the table.

**`price-display`** — Product prices in `{typography.price}` — 20px at 700 weight in `{colors.ink}`. The heavier weight and larger size separate the price from surrounding body text, making it the second most prominent element on the product card after the image.

**`price-compare-at`** — Struck-through original prices in `{typography.body-sm}` and `{colors.muted}`, positioned next to the current price. The muted color and line-through decoration create an obvious visual comparison without requiring additional "Save $X" labels.

### Footer
**`footer-section`** — A full-width section on `{colors.ink}` (#1a1a1a) — near-black — with text in `{colors.muted-soft}` for readable contrast. The dark footer grounds the page and creates a definitive endpoint. Content includes navigation columns, newsletter signup, social links, and legal text at `{typography.body-sm}`.

**`footer-link`** — Links in `{colors.muted-soft}` with `{typography.link}` styling at 500 weight. The heavier-than-body weight ensures legibility against the dark background without competing with primary navigation.

**`footer-link-hover`** — Footer links transition to `{colors.accent-sky}` (#b0e0e9) on hover, introducing the lightest teal as an interactive moment against the dark backdrop. The sky teal is bright enough to signal interactivity without the full intensity of the primary.

### Cart & Quantity
**`cart-icon`** — A 24px icon in `{colors.ink}`, positioned in the top-nav alongside search and account icons. The dark color keeps the icon calm and navigational.

**`cart-count-badge`** — A small cyan `{colors.accent-cyan}` pill overlaying the cart icon, displaying the current item count at `{typography.caption-sm}` size. The `{rounded.full}` shape and 20px height keep it compact. The bright cyan (rather than primary teal) ensures the badge is visible against the white nav background.

**`quantity-selector`** — A compact input group for adjusting quantities on product pages and in the cart. A `{colors.hairline}` border with `{rounded.sm}` corners contains decrement/increment buttons and a numeric display. Each button is 40px square with transparent background, creating a clean, minimal control.

### Misc
**`accordion-header`** — Used for FAQ sections, product specification expandables, and shipping information. The header sits on `{colors.canvas}` with `{typography.title-sm}` in `{colors.ink}` and a `{colors.hairline-soft}` bottom border. Clicking toggles the content area with a smooth expand.

**`trust-badge`** — Small informational badges (free shipping, warranty, satisfaction guarantee) in `{colors.canvas}` background with `{colors.muted}` text, `{rounded.sm}` corners, and a `{colors.hairline-soft}` border. These badges appear below the Add to Cart button and in the footer to reduce purchase anxiety.

**`divider`** — A 1px line in `{colors.hairline-soft}` used between content sections, within accordions, and as a subtle grid spacer. The soft gray separates without demanding attention.

**`section-heading`** — Section titles in `{typography.display-md}` at 28px/600 weight with `{colors.ink}` and `{spacing.lg}` bottom margin. Used for "Featured Grills," "Customer Reviews," "Recently Viewed," and similar page-level section breaks.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger with slide-out drawer; hero text drops to `{typography.display-md}`; search bar moves to full-width below nav; category pills scroll horizontally; buttons expand to full-width; footer columns stack vertically as accordions; promo banner text truncates with ellipsis |
| Tablet | 744–1128px | Two-column product grid; top-nav shows abbreviated links with "More" overflow; hero uses `{typography.display-lg}`; footer shows 2-column grid; search bar remains in nav but collapses to icon on scroll; spec tables remain side-by-side |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all category links visible; hero uses `{typography.display-xl}` with full-bleed background imagery; footer shows 4-column grid; search bar fully expanded in nav; product detail page shows image gallery + details side-by-side |
| Wide | > 1440px | Max-width container (1440px) centered with side margins; product grid can expand to 4 columns; hero content remains centered with generous `{spacing.section}` padding; additional whitespace frames the content |

### Touch Targets
- All interactive elements maintain a minimum 44px touch target height
- Icon buttons in the top-nav are 48px square
- Quantity selector buttons are 40px — compact for the cart context but supplemented by the input field for direct entry
- Product cards are fully tappable on mobile, with the entire card acting as the link target
- Footer links have 44px minimum tap areas through vertical padding
- Category pills have 40px height with horizontal padding creating adequate targets
- Accordion headers span full width with `{spacing.base}` vertical padding meeting the 48px minimum

### Collapsing Strategy
- Top navigation collapses to a hamburger icon below 744px, opening a full-height slide-out drawer with all category links, account, and search
- Product filters collapse to a sticky "Filter & Sort" button that opens a bottom sheet on mobile
- Footer columns convert to accordion sections on mobile, with each heading as a tap-to-expand trigger
- Feature grids collapse to single-column stacks on mobile, with icons left-aligned alongside text
- Product image galleries switch from a thumbnail grid to a swipeable carousel on mobile
- Search transitions from an expanded pill input to an icon-only toggle on tablet and below
- Spec tables maintain their two-column label/value layout but gain horizontal scroll on very narrow viewports
- Promo banner text collapses to a single line with a "Details" link on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The live site returned a 403 Forbidden page, severely limiting design data extraction; all component specifications below the color palette level are inferred from the extracted teal palette, common e-commerce patterns, and the brand's BBQ/grills category
- Only five hex colors were extracted (#226d7a, #b0e0e9, #1e6d7a, #e4f5fa, #22b8d1), all within the teal/cyan family; no neutral, dark, warm, or error-state colors were observed, so ink, body, muted, hairline, error, and success tokens are standard defaults
- Font stacks (Open Sans, Roboto, Arial) appear generic and may be framework defaults rather than the brand's actual typographic choice; the real site may use a custom or commercial typeface not detectable through static extraction
- No Shopify platform markers were detected; the CMS and template system are unknown, which affects component naming conventions and slot structures
- Hover/active state colors, transition durations, easing curves, and animation specifications could not be extracted
- Dark mode is not documented; all tokens assume light mode
- Modal, overlay, and drawer specifications (backdrop opacity, close button placement, animation timing) are inferred
- Loading states (skeleton screens, spinner colors, shimmer patterns) are undocumented
- Focus-visible ring styles for keyboard navigation are assumed as 2px `{colors.primary}` outline offset
- Checkbox, radio button, and toggle switch styling (custom vs. native) is unknown
- Product configurator UI patterns (grill customization, accessory bundles) were not observed
- Video player and embedded media styling are undocumented
- Error page styling (404, empty cart, out-of-stock) beyond the observed 403 is unknown
- Mobile app or progressive web app specific design tokens are absent
- Logo usage specifications (minimum size, clear space, color variants) were not extractable
---
