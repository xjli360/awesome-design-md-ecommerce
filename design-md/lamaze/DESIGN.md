---
version: alpha
name: "Lamaze"
source_url: "https://www.lamazetoys.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every product in the Lamaze lineup doubles as a developmental tool — high-contrast color blocks, bold primary fills, and crinkle textures are engineered to stimulate the infant nervous system, and the brand's digital layer inherits that same chromatic directness. The catalog hero is anchored by a red that sits somewhere between fire-engine and stop-sign — a hue approximating #e31837 that signals safety, warmth, and legibility at low infant focal range. Surrounding primaries — a sunflower yellow, a cobalt blue, a grass green — rotate through product imagery and category badges, creating a palette that reads less like a retail color system and more like a well-stocked art class.

  Navigation is kept minimal and parent-focused: clean horizontal links, a shopping cart icon, and a search field that stays out of the way while the product photography does the work. Cards lean on `{rounded.lg}` corners to echo the soft, safe geometry of plush toy design — no sharp edge appears anywhere in the layout. Product tiles use a white surface (`{colors.surface-card}`) floating against a light gray canvas (`{colors.surface-soft}`), keeping the bright toy imagery as the undisputed focal point.

  CTAs follow a simple hierarchy: a filled primary-red button for add-to-cart and checkout, an outlined secondary for wishlist or learn-more actions. Both adopt a `{rounded.full}` pill shape, borrowing from the rounded-corner language of the toys themselves. Age-range labels appear as small colored badges — yellow for 0–6 months, blue for 6–12 months, green for 12+ months — giving parents an immediate developmental filter without requiring them to read body copy.

  The brand's developmental credibility lives in editorial modules: feature callouts explaining sensory benefits, pediatric expert quotes, and safety-certification icons clustered below product descriptions. These sit in clean white cards with generous internal padding (`{spacing.xl}`) and `{colors.muted}` body text. The overall effect is a site that addresses a shopping parent's need for reassurance and a child's instinct to reach for bright color simultaneously — both met through the same chromatic boldness that defines every Lamaze toy.

colors:
  primary: "#e31837"
  primary-active: "#b5102a"
  primary-disabled: "#f5a0ac"
  accent-yellow: "#f9c31f"
  accent-blue: "#0072bc"
  accent-green: "#00a651"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#717171"
  hairline: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-badge-infant: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "Nunito, 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  age-tag:
    fontFamily: "Nunito, 'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1.5px
    rounded: "{rounded.lg}"
    padding: 12px 16px
    typography: "{typography.body-md}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    imageBorderRadius: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.07)"
  age-badge-infant:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-badge-infant}"
    rounded: "{rounded.full}"
    padding: 4px 10px
    typography: "{typography.age-tag}"
  age-badge-baby:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: 4px 10px
    typography: "{typography.age-tag}"
  age-badge-toddler:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: 4px 10px
    typography: "{typography.age-tag}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
    ctaVariant: "button-primary"
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    borderColor: "{colors.hairline}"
    hoverBorderColor: "{colors.primary}"
  feature-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  expert-quote:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    quoteTypography: "{typography.body-md}"
    attributionTypography: "{typography.caption}"
    attributionColor: "{colors.muted}"
    borderLeft: "4px solid {colors.primary}"
    padding: "{spacing.base} {spacing.lg}"
  safety-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    dividerColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — A fully pill-shaped (`{rounded.full}`) button filled with `{colors.primary}` red, white type at `{typography.button-md}`, 48px tall with 28px horizontal padding. The height and radius make it a generous touch target for parents managing a baby with one arm. The active state deepens to `{colors.primary-active}` and the disabled state washes to `{colors.primary-disabled}`, maintaining the pill silhouette throughout all states. The rounded form is a deliberate echo of Lamaze toy geometry — no hard corner exists anywhere in the layout.

**`button-secondary`** — An outlined counterpart: white fill, 2px `{colors.primary}` border, red label text. Shares the `{rounded.full}` radius and 48px height so the primary/secondary pair reads as a coordinated family. Used for secondary CTAs like "Learn More," "Add to Wishlist," or filtered browsing actions where commitment is lower than a direct purchase.

**`button-small`** — A 36px pill (`{rounded.full}`) used for in-card actions such as quick-add. Uses `{typography.button-sm}` to keep it compact without losing legibility inside product tile grids.

### Text Input & Search
**`text-input`** — White fill, 1.5px `{colors.hairline}` border, softly rounded at `{rounded.lg}`. Focus state switches the border to `{colors.primary}` red, giving clear affordance without motion. Used in checkout forms, newsletter capture, and account flows.

**`search-bar`** — A pill-shaped (`{rounded.full}`) field over `{colors.surface-soft}` gray. A magnifier icon in `{colors.muted}` precedes the placeholder. The soft-gray background keeps it visually distinct from the white nav bar without requiring an outline. On mobile this expands to a full-screen sheet.

### Navigation
**`nav-bar`** — 64px tall white bar with a bottom hairline divider. Carries the Lamaze wordmark on the left, horizontal category links in `{typography.nav-link}` at center on desktop, and cart plus search icons on the right. The lean height and minimal element count reflect the utilitarian clarity parents need when browsing one-handed.

### Product Cards
**`product-card`** — White surface card with `{rounded.lg}` corners and a 7%-opacity drop shadow that lifts the card off the `{colors.surface-soft}` background. The product image fills the card top with `{rounded.md}` clip radius. Below the image: an age badge, product name in `{typography.title-sm}`, a short descriptor in `{typography.body-sm}`, price in `{typography.title-md}`, and a `button-small` add-to-cart. Internal gap is `{spacing.sm}`, padding `{spacing.base}`.

### Age Badges
**`age-badge-infant`** / **`age-badge-baby`** / **`age-badge-toddler`** — Three pill badges mapping developmental stage to a distinct color: sunflower yellow (`{colors.accent-yellow}`) with dark ink text for 0–6 months, cobalt blue (`{colors.accent-blue}`) with white text for 6–12 months, and grass green (`{colors.accent-green}`) with white text for 12+ months. Type is `{typography.age-tag}` in uppercase with generous tracking. Positioned at the top-left of every product card, they create an instant visual filter system readable before the product name registers — designed for the speed of a distracted parent's scan.

### Hero Banner
**`hero-banner`** — Full-width `{colors.surface-soft}` panel with headline in `{typography.display-xl}`, subhead in `{typography.body-md}`, and a `button-primary` CTA. On desktop the layout is 60/40 text-left / imagery-right; on tablet and mobile it stacks vertically with image above text. Section-level padding (`{spacing.section}` top and bottom) gives the product photography room to dominate.

### Category Cards
**`category-card`** — White card at `{rounded.lg}` with a `{colors.hairline}` border that transitions to `{colors.primary}` on hover. Title in `{typography.title-md}` with a category illustration or cropped product shot in the upper area. Used in the homepage grid to navigate between toy types — rattles, teethers, soft books, activity centers. The red hover border reinforces the primary brand color as an active-state signal.

### Feature Callouts
**`feature-callout`** — A `{colors.surface-soft}` module used to explain developmental benefits: "Encourages Reaching," "Supports Sensory Exploration," "Builds Hand-Eye Coordination." Headline in `{typography.display-sm}`, body in `{typography.body-md}`, each paired with a small brand illustration or icon. `{rounded.md}` corners and `{spacing.xl}` padding give it contained, card-like presence without a shadow. Groups of two or four appear between the product grid and the editorial footer on category pages.

### Expert Quote
**`expert-quote`** — White card with a 4px `{colors.primary}` left border — a quiet typographic device that signals pediatric authority. Quote text in `{typography.body-md}` `{colors.body}`, attribution in `{typography.caption}` `{colors.muted}`. Appears on the About page and on PDPs beneath safety badges to surface endorsements from child development specialists.

### Safety Badges
**`safety-badge`** — Small `{colors.surface-soft}` chips in `{typography.caption}` displaying certification text ("BPA-Free," "EN71 Certified," "ASTM F963 Compliant"). `{rounded.sm}` corners, `{spacing.xs}` vertical and `{spacing.sm}` horizontal padding. Clusters of three to five appear directly below the product description on PDPs, providing the reassurance signals parents actively scan for before purchase.

### Footer
**`footer`** — Dark `{colors.ink}` footer with white (`{colors.canvas}`) body text and `{colors.hairline}` links at `{typography.body-sm}`. Four columns on desktop: Shop, About, Support, Social. The Lamaze wordmark renders white-on-dark at the top of the left column. Collapses to stacked accordion sections on mobile with `{colors.muted}` `{spacing.xxl}` vertical padding.

### Breadcrumb
**`breadcrumb`** — Inline path (Home / Shop / Rattles / Product Name) in `{typography.caption}` `{colors.muted}`, with the current segment in `{colors.ink}`. The "/" separator matches `{colors.muted}`. Sits directly below `nav-bar` on category and product pages to orient parents who arrive via search or direct link.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer + cart icon; hero stacks vertically (image above text); age badges row-scrollable; footer collapses to accordions with hairline dividers |
| Tablet | 744–1128px | Two-column product grid; nav may retain top-level links or collapse to icon strip; hero shifts to side-by-side 50/50; feature callout grid 2-up |
| Desktop | 1128–1440px | Three-to-four-column product grid; full horizontal nav with all category links visible; hero at 60/40 text-left/image-right; category card grid 4-up |
| Wide | > 1440px | Max-width container (~1440px) centered with `{spacing.section}` side margins; product grid expands to 4–5 columns; hero imagery scales while text column stays fixed-width |

### Touch Targets
- All primary and secondary buttons minimum 48px height, 44px minimum width
- `button-small` at 36px height — supplement with 44px invisible tap zone on mobile
- Age badges padded to minimum 32px height for reliable tap
- Nav icons (cart, search, hamburger) minimum 44×44px hit area
- Full product card surface is tappable on mobile, not just the button

### Collapsing Strategy
- Desktop horizontal nav → slide-in hamburger drawer on mobile with full category tree and search at top
- 4-column product grid → 2-column on tablet → 1-column on mobile
- Side-by-side hero (60/40) → stacked hero on tablet/mobile with image above text
- 4-up feature callout row → 2-up on tablet → 1-up on mobile
- Footer 4-column layout → stacked accordion sections on mobile with `{colors.hairline}` dividers between each

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex colors are inferred from brand knowledge** — the live site returned zero extractable color tokens (likely JS-rendered or behind anti-bot protection). The primary red (#e31837) approximates the Lamaze logo red but must be verified against official brand assets or CSS inspection.
- **No typeface data was extractable.** "Nunito" and "Poppins" are reasonable guesses for a baby brand at this register, but the actual font(s) used on lamazetoys.com are unknown. Verify by inspecting computed `font-family` on the live site.
- **Accent palette (yellow #f9c31f, blue #0072bc, green #00a651)** is inferred from Lamaze toy photography norms, not extracted from site CSS. Exact hex values for age-badge colors require live inspection or brand style guide access.
- **No `<meta name="theme-color">` tag** was detected, removing one reliable primary-color signal that would otherwise anchor the palette.
- **Component measurements** (nav height, card shadow values, grid column counts, hero split ratio) are estimated from DTC baby brand conventions and require verification via browser DevTools or design file access.
- **Typography scale sizing** is estimated; actual font sizes, weights, and line heights on lamazetoys.com are unknown without CSS extraction.
- **Dark mode** — no data on whether the site implements an alternate dark theme.
- **Custom iconography** — Lamaze uses branded character illustrations in toy packaging; whether a matching custom icon set appears in the UI cannot be confirmed without site access.
- **Platform** — the site is not confirmed Shopify; the underlying platform and its default component patterns are unknown, which may affect form styling, cart behavior, and checkout flow conventions.
