---
version: alpha
name: "Big Green Egg"
source_url: "https://www.biggreenegg.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The green arrives first — not a lifestyle-brand sage or a muted olive but a deep, unambiguous porcelain-kiln green (#105742) that matches the ceramic glaze on the Egg itself, sitting on a warm parchment canvas (#f4f0e6) that evokes butcher paper laid across a prep table. Where most outdoor-cooking brands default to charcoal-and-flame palettes, Big Green Egg builds its entire visual identity from the product's physical surface, then wraps it in a typographic system that pairs Fraunces — a variable serif with playful ball terminals and optical-size axis — for display headings with Figtree, a crisp geometric sans-serif, for body and UI text. The result reads as Southern-hospitality premium: warmer than a Traeger, more literary than a Weber, and never clinical. Display type runs large and heavy (Fraunces at 48–56px, weight 800) with tight negative tracking that gives headlines the gravitational pull of a cast-iron skillet, while body copy at Figtree 16px/400 breathes in long recipe descriptions and product specs. A secondary serif, new-spirit, appears in accent contexts — pull quotes, recipe card subtitles, editorial asides — adding a second voice without competing with Fraunces. The accent red (#cf263b) appears on sale badges and urgent CTAs, a deliberate ember-glow against the green; a burnished gold (#a07636) surfaces in premium tier callouts and "Lifetime Warranty" badges, reinforcing the product's heirloom positioning. Cards and product tiles use `{rounded.sm}` to `{rounded.md}` corners with generous `{spacing.lg}` gutters, while primary CTAs are solid green rectangles at `{rounded.sm}` — confident, not cute. The soft teal (#aadddd) functions as an informational highlight for cooking-mode indicators and temperature guides, distinct enough from the primary green to read as data rather than brand. Navigation runs on helvetica-neue-lt-pro in condensed and standard widths, a pragmatic choice that keeps menus compact without sacrificing legibility at small sizes. The overall system trusts negative space, warm photography of charred meats and ceramic curves, and that single inescapable green to carry the brand — ornament is minimal, and every pixel of decoration earns its place.

colors:
  primary: "#105742"
  primary-active: "#0d4535"
  primary-disabled: "#6a7873"
  ink: "#212121"
  deep-ink: "#1a1a1a"
  body: "#646464"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#bebebe"
  hairline-soft: "#cecbc7"
  canvas: "#f4f0e6"
  canvas-white: "#fefefe"
  surface-soft: "#f2f2f2"
  surface-card: "#fefefe"
  surface-warm: "#ece5d4"
  surface-light: "#f7f7f7"
  on-primary: "#fefefe"
  on-dark: "#fefefe"
  accent-red: "#cf263b"
  accent-red-dark: "#a24e4e"
  accent-gold: "#a07636"
  accent-teal: "#aadddd"
  accent-green-mid: "#188263"
  accent-green-bright: "#10f0ae"
  dark-green: "#031811"
  error: "#721c24"
  error-bg: "#f8d7da"
  error-border: "#f5c6cb"
  info-blue: "#4e63df"
  link-blue: "#2f6ed6"
  star-rating: "#a07636"
  scrim: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "'Fraunces', 'new-spirit', Georgia, serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Fraunces', 'new-spirit', Georgia, serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "'Fraunces', 'new-spirit', Georgia, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Fraunces', 'new-spirit', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Fraunces', 'new-spirit', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  accent-serif:
    fontFamily: "'new-spirit', 'Fraunces', Georgia, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'helvetica-neue-lt-pro', 'Figtree', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  uppercase-tag:
    fontFamily: "'helvetica-neue-lt-pro-cond', 'helvetica-neue-lt-pro', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'helvetica-neue-lt-pro', 'Figtree', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link-condensed:
    fontFamily: "'helvetica-neue-lt-pro-cond', 'helvetica-neue-lt-pro', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Figtree', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
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
    textColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-red-active:
    backgroundColor: "{colors.accent-red-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
  button-pill-green:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas-white}"
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
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  mega-menu:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
    borderBottom: "1px solid {colors.hairline-soft}"
    boxShadow: "0 8px 24px rgba(33, 33, 33, 0.1)"
  mega-menu-heading:
    typography: "{typography.nav-link-condensed}"
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focused:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
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
    boxShadow: "0 4px 16px rgba(33, 33, 33, 0.08)"
  product-card-image:
    backgroundColor: "{colors.surface-light}"
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-badge-best-seller:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  size-selector:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
    height: 44px
  size-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "2px solid {colors.primary}"
    height: 44px
  hero-section:
    backgroundColor: "{colors.dark-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 36px
  hero-subheading:
    typography: "{typography.accent-serif}"
    textColor: "{colors.accent-teal}"
  recipe-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  recipe-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  recipe-card-title:
    typography: "{typography.title-lg}"
    textColor: "{colors.ink}"
  recipe-card-meta:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  temperature-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.dark-green}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  cooking-mode-tag:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  warranty-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.accent-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.accent-gold}"
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
  footer-section:
    backgroundColor: "{colors.dark-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    typography: "{typography.uppercase-tag}"
    textColor: "{colors.accent-teal}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-dark}"
  footer-link-hover:
    textColor: "{colors.accent-teal}"
  newsletter-input:
    backgroundColor: "rgba(255, 255, 255, 0.1)"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.accent-green-mid}"
  newsletter-submit:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  social-icon:
    color: "{colors.on-dark}"
    size: 24px
  social-icon-hover:
    color: "{colors.accent-teal}"
  cart-icon:
    color: "{colors.ink}"
    size: 24px
  cart-count-badge:
    backgroundColor: "{colors.accent-red}"
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
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    height: 40px
  feature-icon:
    color: "{colors.primary}"
    size: 36px
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  testimonial-card:
    backgroundColor: "{colors.surface-warm}"
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

## Components

### Buttons
**`button-primary`** — The primary CTA across the Big Green Egg ecosystem, rendered in the brand's signature porcelain green `{colors.primary}` with `{colors.on-primary}` text. On hover/active, the green deepens to `{colors.primary-active}`, a darker forest shade that reinforces the ceramic-kiln association. Disabled state uses `{colors.primary-disabled}`, a desaturated gray-green that reads as muted without breaking the palette. All primary buttons use `{rounded.sm}` — soft enough to feel approachable, square enough to convey the brand's premium authority.

**`button-secondary`** — A white button outlined in 2px `{colors.primary}` green, used for "Learn More", "Compare Sizes", and secondary actions alongside primary CTAs. On active state the border and text deepen to `{colors.primary-active}`, maintaining green-family consistency. The outlined form ensures it never competes with the solid green primary but remains clearly interactive.

**`button-ghost`** — A borderless, background-free text button for tertiary actions: accordion toggles, "View All" links in grid sections, and in-card navigation. Active state adds a `{colors.surface-soft}` backdrop. Ghost buttons carry the full `{typography.button-md}` weight to maintain visual hierarchy alongside bordered siblings.

**`button-accent-red`** — A high-urgency button in `{colors.accent-red}`, reserved for sale CTAs, clearance actions, and limited-time promotions. The red reads as deliberate heat against the green — an ember in the grill — and on hover deepens to `{colors.accent-red-dark}`. Used sparingly: no more than one per viewport.

**`button-add-to-cart`** — An oversized variant of the primary button at 56px height using `{typography.button-lg}`, dedicated to the product detail page. The extra height and 16px vertical padding give it the gravitational weight that the highest-value CTA on the site demands. Shares the `{colors.primary}` green and `{rounded.sm}` radius of the standard primary.

**`button-pill-green`** — A `{rounded.full}` pill variant of the primary button, used in promotional banners, sticky mobile CTAs, and "Subscribe" actions. The pill shape softens the CTA for contexts where a rectangular button would feel too aggressive.

**`button-pill-outline`** — A pill-shaped outline button with a `{colors.hairline}` border, used for filter chips, category selectors, and "Clear Filters" on collection pages. Transparent background keeps dense filter bars visually light.

### Cards
**`product-card`** — The primary container for Egg models, EGGcessories, and fuel products. A `{colors.surface-card}` white background with `{colors.hairline-soft}` border and `{rounded.md}` corners. On hover, the border strengthens to `{colors.hairline}` and a subtle 4px box shadow lifts the card. The image area uses `{colors.surface-light}` as a fallback background with top-only radius, letting product photography bleed edge-to-edge horizontally. Title runs in `{typography.title-sm}` and price in `{typography.price}`.

**`recipe-card`** — Used across the recipe library and homepage recipe carousel. Shares the `{colors.surface-card}` background and `{rounded.md}` radius of the product card for visual consistency. The title uses `{typography.title-lg}` (Fraunces serif) to differentiate editorial content from commerce, while cooking metadata — time, temperature, cooking mode — displays in `{typography.caption}` at `{colors.muted}`.

**`feature-card`** — Used in "Why the EGG" and "7 Cooking Styles" grid sections. A `{colors.surface-card}` container with `{colors.hairline-soft}` border and `{rounded.md}` corners. Icons render in `{colors.primary}` green at 36px. Body text in `{typography.body-md}` at `{colors.body}` describes each feature or cooking method.

**`testimonial-card`** — Customer stories displayed on a `{colors.surface-warm}` warm-cream background, creating a distinct visual lane from the white product cards. Author name in `{typography.title-sm}` at `{colors.ink}`, body in `{typography.body-md}` at `{colors.body}`. No border — the warm background provides enough separation from the page canvas.

### Navigation
**`top-nav`** — A 72px white bar with a `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` (helvetica-neue-lt-pro at 14px, 500 weight) to keep the header compact. The logo, primary links (EGGs, EGGcessories, Recipes, Support), search icon, cart, and account sit in a single row. Active links display a 2px `{colors.primary}` underline and green text; inactive links remain in `{colors.body}`.

**`mega-menu`** — A dropdown panel for categories like EGGs (by size) and EGGcessories (by type). White `{colors.canvas-white}` background with generous `{spacing.lg}` padding and a subtle box shadow. Category headings use `{typography.nav-link-condensed}` — helvetica-neue-lt-pro in condensed width, uppercase, at `{colors.primary}` green — creating clear structural divisions within the menu.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a `{colors.surface-soft}` background that reads as a tinted field rather than a bordered box. On focus, the background clears to `{colors.canvas-white}` and a 2px `{colors.primary}` border appears. The pill shape echoes the Egg's ovoid silhouette without being literal.

### Size Selector
**`size-selector`** — A row of clickable size tiles for selecting Egg models (MiniMax, Small, Medium, Large, XLarge, 2XL). Each tile is a `{colors.canvas-white}` box with `{colors.hairline}` border and `{rounded.sm}` corners at 44px height. The active tile flips to `{colors.primary}` background with `{colors.on-primary}` text, creating an unambiguous selection state. This component is central to the shopping experience — every product page for the core Egg lineup uses it.

### Badges
**`product-badge-sale`** — A `{colors.accent-red}` pill with white text and `{typography.badge}` uppercase styling. Positioned absolute in the top-left of product card images. The red stands in deliberate contrast to the green brand environment, ensuring sale items are immediately visible.

**`product-badge-new`** — A `{colors.primary}` green pill for newly launched products and EGGcessories. Using the primary brand color signals "new" as a positive brand moment rather than an urgency trigger.

**`product-badge-best-seller`** — A `{colors.accent-gold}` pill that reinforces the premium heirloom positioning. The warm gold reads as a merit badge, distinct from both the green brand color and the red sale signal.

**`temperature-badge`** — A `{colors.accent-teal}` pill with `{colors.dark-green}` text, used to display cooking temperatures on recipe cards and product pages (e.g., "350°F", "700°F+"). The teal distinguishes data from brand color, reading as informational rather than promotional.

**`cooking-mode-tag`** — A small rectangular tag in `{colors.surface-warm}` with `{colors.primary}` text and `{typography.uppercase-tag}` styling, labeling cooking methods: GRILL, SMOKE, BAKE, ROAST, SEAR. The warm cream background and uppercase condensed type give these tags the feel of stamped labels.

**`warranty-badge`** — A `{colors.surface-warm}` rectangle with a `{colors.accent-gold}` border and gold text, used for "Lifetime Warranty" and "Best-in-Class" callouts. The gold border elevates this above standard badges, signaling a premium guarantee.

### Forms
**`text-input`** — Standard form inputs for checkout, account, and dealer-locator flows. White background, `{colors.hairline}` border, `{rounded.sm}` corners, 48px height. On focus, the border becomes 2px `{colors.primary}` green — a clear, accessible indicator. Error state swaps to `{colors.error-bg}` background with a `{colors.error}` border, leveraging the extracted error palette rather than relying on the accent red alone.

**`select-dropdown`** — Styled select elements matching the text-input pattern: `{colors.canvas-white}` background, `{colors.hairline}` border, `{rounded.sm}`, 48px height. Used for country selectors, Egg model pickers in the support flow, and accessory filtering.

### Promotional
**`promo-banner`** — A slim 40px bar at the very top of the page in solid `{colors.primary}` green with `{colors.on-primary}` text. Displays shipping promotions, event announcements, or dealer-locator CTAs. Text uses `{typography.caption}` for compact, scannable messaging. This banner sits above the main nav and is the first brand touchpoint.

**`hero-section`** — A full-bleed section with `{colors.dark-green}` background (the near-black extracted green #031811) and `{colors.on-dark}` text. Display headlines use `{typography.display-xl}` (Fraunces at 56px, weight 800) for maximum impact. The hero CTA inverts the primary pattern: white `{colors.on-primary}` background with `{colors.primary}` green text, creating a bright focal point against the dark canvas. Subheadings use `{typography.accent-serif}` in `{colors.accent-teal}`, adding a color layer that guides the eye from headline to CTA.

### Footer
**`footer-section`** — A full-width section in `{colors.dark-green}`, the same near-black green as the hero, creating bookend symmetry. Text in `{colors.on-dark}` white. Section headings use `{typography.uppercase-tag}` in `{colors.accent-teal}`, providing structural contrast against the dark canvas. Contains the newsletter signup, navigation columns, social icons, dealer-locator link, and legal text.

**`footer-link`** — Links in `{colors.on-dark}` with `{typography.link}` styling, transitioning to `{colors.accent-teal}` on hover. The teal hover state provides a warm, interactive moment distinct from the primary green, avoiding the awkwardness of green-on-dark-green.

**`newsletter-input`** — A semi-transparent input with a `{colors.accent-green-mid}` border, sitting against the dark footer. The translucent background lets the dark green show through while maintaining legibility. Paired with a white `newsletter-submit` button that inverts the primary palette.

### Cart & Quantity
**`cart-icon`** — A 24px icon in `{colors.ink}`, positioned in the top nav alongside search and account icons. The cart count badge overlays it in `{colors.accent-red}` with a `{rounded.full}` pill shape and `{typography.caption-sm}` text.

**`quantity-selector`** — A compact input group at 44px height with `{colors.hairline}` border and `{rounded.sm}` corners. Decrement and increment buttons are 44px square with transparent backgrounds, meeting touch-target minimums. Used on product pages and in the cart drawer.

### Dividers & Headings
**`divider`** — A 1px line in `{colors.hairline-soft}`, used between sections, within accordions, and in product detail tabs. The warm-tinted gray keeps separators soft against the cream canvas.

**`section-heading`** — Page and section titles in `{typography.display-md}` (Fraunces at 32px, weight 700) with `{colors.ink}` color and `{spacing.lg}` bottom margin. The serif display font at this scale provides the editorial gravitas that distinguishes Big Green Egg from utilitarian grill brands.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layouts; top-nav collapses to hamburger + logo + cart icon; product cards stack vertically; hero text drops to `{typography.display-md}`; size-selector wraps to two rows; mega-menu becomes a full-screen slide-out drawer; search becomes full-width overlay; footer columns stack with accordion expand/collapse; buttons go full-width; recipe cards become a horizontal swipeable carousel |
| Tablet | 744–1128px | Two-column product grids; top-nav shows logo and condensed links with overflow in "More" dropdown; hero uses `{typography.display-lg}`; size-selector fits in a single row; footer shows 2-column grid; mega-menu still uses slide-out pattern; search collapses to icon toggle |
| Desktop | 1128–1440px | Full top-nav with all links, search bar, and icons visible; three-column product grids; hero uses `{typography.display-xl}` with full-width photography; mega-menu renders as hover-triggered dropdown panel; footer shows 4-column grid; size-selector displays all sizes inline with labels |
| Wide | > 1440px | Max-width container (1440px) centered with `{colors.canvas}` cream bleed on sides; product grids can expand to 4 columns; hero imagery extends full-bleed while text content remains within container; additional whitespace in `{spacing.section}` between major sections |

### Touch Targets
- All interactive elements maintain a minimum 44px height for touch accessibility
- Top-nav icons are 48px square tap targets (cart, search, account, hamburger)
- Size-selector tiles are 44px tall with adequate horizontal padding for thumb tapping
- Product card tap targets span the full card width on mobile
- Quantity selector buttons are 44px square, meeting accessibility minimums
- Footer links get increased vertical padding (44px tap areas) on mobile
- Accordion headers are 48px+ tall with full-width tap targets
- Pill-shaped filter chips maintain 44px height with generous horizontal padding

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px; the full category tree appears in a slide-out drawer with accordion-style sub-navigation for EGGs, EGGcessories, Recipes, and Support
- Mega-menu content (size guides, category thumbnails) reorganizes into a vertical scrollable list on mobile
- Product filters collapse to a sticky "Filter & Sort" bar that opens a bottom-sheet modal on mobile
- Size-selector wraps gracefully from a single row to a 3×2 grid on narrow viewports, maintaining touch-target sizing
- Multi-column feature grids collapse to single-column stacks with images above text blocks
- Product image galleries become a swipeable carousel with dot indicators replacing the desktop thumbnail strip
- Recipe card grids become horizontal scroll carousels on mobile with peek of next card visible
- Footer columns stack vertically with each heading becoming an accordion toggle
- Promo banner text truncates with ellipsis on very narrow viewports; a "Details" link replaces the full message

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font-weight axes for Fraunces (a variable font with weight, optical-size, and WONK axes) were not extractable from the Shopify theme CSS; weights used here (600–800) are inferred from visual hierarchy
- The relationship between new-spirit and Fraunces — whether new-spirit is used as a fallback, an editorial accent, or a deprecated legacy choice — could not be determined from the extracted font stacks alone
- helvetica-neue-lt-pro and helvetica-neue-lt-pro-cond usage boundaries are assumed to be navigation and badge contexts based on the condensed width's suitability for menus; actual usage rules may differ
- Hover and active state transition durations, easing curves, and animation specifications were not extractable
- Dark mode specifications are not present on the live site; all tokens assume light mode only
- Sub-brand or product-line-specific palettes (e.g., different styling for the Modular Outdoor Kitchen line vs. core Eggs) may exist but were not observable from global CSS extraction
- Modal and overlay specifications (backdrop opacity, drawer animation, close button placement) were not observed
- Loading state designs (skeleton screens, spinner colors, shimmer animations) are not documented
- Focus-visible ring styles for keyboard navigation were not observed; the system assumes a 2px `{colors.primary}` outline offset as a reasonable default
- Checkbox, radio, and toggle-switch custom styling is not documented; the site likely uses Shopify theme defaults
- The `{colors.accent-green-bright}` (#10f0ae) and `{colors.info-blue}` (#4e63df) tokens appeared in extraction but their specific UI roles could not be confirmed; they may be interactive state highlights or third-party widget artifacts
- Multi-step form patterns (checkout flow, dealer-locator wizard) were not observed; progress indicator and step-navigation styling are unknown
- Video player controls and embedded media styling are not documented
- Cookie consent banner and GDPR-related UI patterns were not extracted
- Print stylesheet specifications are absent
