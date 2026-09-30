---
version: alpha
name: "Glorious"
source_url: "https://www.gloriousgaming.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-voltage gaming peripherals brand that runs on a deep charcoal chassis (#262626) and a cyan spark (#56b7e6) — the same electric blue that fires every primary CTA, navigation highlight, and product-rollover glow. The palette is a gamer’s arsenal: amber (#fdba3b) for ratings and sale badges, red (#fd423b) for limited drops and error states, and a full spectrum of accent colors (lime #c0df16, purple #9530d5, pink #e360d4) that map to specific switch types and product lines. Typography leans on a mix of display faces — athena, bodega-sans, and new-spirit for headlines, with ccmeanwhile and elfreth for editorial moments — creating a layered typographic identity that feels more like a streetwear label than a peripheral company. Buttons are sharp-cornered rectangles (`{rounded.none}`) with 48px height and bold condensed type, while product cards use a soft 8px radius (`{rounded.sm}`) and a white canvas (`{colors.canvas}`) to let the vivid product photography pop. The brand’s visual system is built for contrast: dark nav bars, bright accent strokes, and a generous use of `{spacing.lg}` between product tiles. Every interaction — hover, click, badge — carries a color shift that signals responsiveness without animation. The overall effect is a clean, aggressive, and unmistakably gaming-native aesthetic that prioritizes legibility and shelf impact over atmospheric subtlety.

colors:
  primary: "#56b7e6"
  primary-active: "#3a9fd4"
  primary-disabled: "#b4ddf2"
  ink: "#262626"
  body: "#3a3a3a"
  muted: "#808080"
  muted-soft: "#b4b4b4"
  hairline: "#d9d9d9"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#fdba3b"
  accent-amber-active: "#e6a832"
  accent-red: "#fd423b"
  accent-red-active: "#dc3513"
  accent-lime: "#c0df16"
  accent-purple: "#9530d5"
  accent-pink: "#e360d4"
  accent-blue-deep: "#0857c3"
  accent-green: "#3b8638"
  star-rating: "#fdba3b"
  sale-badge: "#fd423b"
  limited-badge: "#9530d5"
  switch-blue: "#56b7e6"
  switch-brown: "#d3b25b"
  switch-red: "#fd423b"
  switch-silver: "#d3d3d3"
  switch-black: "#262626"
  switch-green: "#2bac26"
  switch-yellow: "#ffff03"
  switch-white: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'bodega-sans', 'athena', Impact, 'Arial Black', sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'bodega-sans', 'athena', Impact, 'Arial Black', sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'new-spirit', 'athena', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'new-spirit', 'athena', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'ccmeanwhile', 'elfreth', 'Arial', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  title-md:
    fontFamily: "'ccmeanwhile', 'elfreth', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
  title-sm:
    fontFamily: "'ccmeanwhile', 'elfreth', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'subway-berlin-sc', 'Arial', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'subway-berlin-sc', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'subway-berlin-sc', 'Arial', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'athena-inline', 'bodega-sans', 'Arial Black', sans-serif"
    fontSize: 14px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'athena-inline', 'bodega-sans', 'Arial Black', sans-serif"
    fontSize: 12px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'subway-berlin-sc', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'athena-inline', 'bodega-sans', 'Arial Black', sans-serif"
    fontSize: 13px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'athena-inline', 'bodega-sans', 'Arial Black', sans-serif"
    fontSize: 10px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  product-name:
    fontFamily: "'new-spirit', 'athena', Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'subway-berlin-sc', 'Arial', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-secondary-active:
    backgroundColor: "#1a1a1a"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-accent-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-accent-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 36px
  button-sm-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    height: 56px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.product-name}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-card-badge-limited:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.accent-amber}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-banner-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    height: 360px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.primary}"
  section-heading:
    typography: "{typography.title-lg}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
  switch-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  switch-selector-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in cyan (#56b7e6) with white uppercase condensed type. Sharp corners (`{rounded.none}`) reinforce the brand's aggressive gaming aesthetic. On hover, shifts to `button-primary-active` (#3a9fd4). Disabled state uses a washed-out cyan (`button-primary-disabled`). Used for "Add to Cart", "Pre-Order", and primary checkout flows.

**`button-secondary`** — Dark ink (#262626) background with white type, used for secondary actions like "View Details" or "Learn More". Hover state darkens to near-black (#1a1a1a). Same sharp-cornered, uppercase condensed typography as primary.

**`button-ghost`** — Transparent background with ink text, used for tertiary actions like "Cancel" or "Clear Filters". Hover reveals a soft surface background. Maintains the same typographic weight and uppercase treatment.

**`button-accent-amber`** — Amber (#fdba3b) background with dark ink text, used for sale-related CTAs and promotional actions. Hover darkens the amber. Same structural properties as primary.

**`button-accent-red`** — Red (#fd423b) background with white text, reserved for limited drops, clearance, or destructive actions. Hover shifts to a deeper red (#dc3513).

**`button-accent-lime`** — Lime (#c0df16) background with dark ink text, used for switch-specific promotions or brand collaborations. Maintains the brand's sharp-cornered, uppercase condensed identity.

**`button-sm`** — A compact version of the primary button at 36px height, used for inline actions like "Quick Add" or filter applications. Same visual language, smaller footprint.

### Cards
**`product-card`** — White canvas card with soft 8px radius (`{rounded.sm}`), 12px padding, and product name in serif new-spirit. On hover, a subtle box shadow lifts the card. The product image sits at a 1:1 aspect ratio with matching radius. Badges overlay the top-left corner in red (sale), purple (limited), or amber (promotion).

**`product-card-badge`** — Sharp-cornered label in uppercase condensed 10px type. Red background for standard badges, purple for limited editions, amber for sale items. Padding is tight (4px 8px) to keep the badge compact against the product image.

**`product-card-price`** — Set in subway-berlin-sc at 16px bold, body color (#3a3a3a). Sits below the product name with standard spacing.

**`product-card-rating`** — Caption-sized text in amber (#fdba3b), reflecting the star-rating color. Positioned below the price.

### Navigation
**`nav-bar`** — Full-width dark ink (#262626) bar at 64px height, housing navigation links in uppercase condensed type. On scroll, compresses to 56px. The brand logo sits left-aligned, with nav links centered or right-aligned depending on viewport.

**`nav-link`** — White text on dark background, 13px uppercase condensed with 0.5px letter spacing. Active and hover states shift to cyan (#56b7e6). Padding is 8px 16px for comfortable tap targets.

**`nav-bar-scrolled`** — Reduced height variant (56px) with the same background and link styling. Triggers after 80px of scroll.

### Forms
**`text-input`** — White canvas with 1px hairline border, 48px height, and sharp corners. Focus state gains a 2px cyan border. Error state switches to a 2px red border. Placeholder text in muted gray (#808080).

**`select-input`** — Same structural properties as text-input, used for dropdowns like switch type filters or sort options. Includes a custom dropdown arrow (not specified in tokens but assumed from brand patterns).

**`search-bar`** — White canvas with hairline border, 48px height, sharp corners. Focus state uses cyan border. Used for site-wide product search.

### Footer
**`footer`** — Dark ink (#262626) background with muted-soft (#b4b4b4) text in body-sm. Section-level padding (64px top/bottom, 24px sides). Links are in link typography with hover state shifting to cyan.

### Hero
**`hero-banner`** — Full-width dark ink banner at 480px height, featuring display-xl typography in white. Used for major product launches or brand campaigns. An accent variant uses cyan background at 360px height for secondary promotions.

### Switch Selector
**`switch-selector`** — White canvas with hairline border, used for the brand's signature switch-type filter (Blue, Brown, Red, Silver, Black, Green, Yellow, White). Active state fills with cyan and inverts text to white. Each switch type maps to its corresponding color in the palette.

### Quantity Selector
**`quantity-selector`** — White canvas with hairline border, 48px height, used on product detail pages. Contains minus/plus buttons flanking a numeric input. Sharp corners maintain brand consistency.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row); nav collapses to hamburger menu; hero height reduces to 320px; buttons become full-width; switch selector becomes a horizontal scroll strip; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero at 400px; buttons remain inline but shrink padding; switch selector wraps to two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 480px; standard button sizing; switch selector displays as a single row |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero at 520px; additional whitespace around sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Nav links have 48px tap targets (8px padding + 32px text height)
- Product card badges are at least 20px tall for legibility
- Quantity selector buttons are 44px x 44px minimum
- Switch selector items are 44px tall with adequate horizontal padding

### Collapsing Strategy
- Primary nav collapses to hamburger menu at < 744px viewport width
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Footer link columns collapse to a single stacked column at < 744px
- Hero banner text reduces in size and centers vertically on mobile
- Switch selector becomes a horizontally scrollable strip on mobile rather than wrapping
- Search bar moves from inline to full-width below the nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card badges (red, purple, amber) were not reliably extracted from the live site; assumed to darken by 10-15% based on brand patterns
- Error state styling for forms (text-input, select-input) beyond border color is inferred; actual error message typography and iconography not captured
- Sub-brand palettes (Glorious PC Gaming Race vs. Glorious Core software) may have distinct color variations not reflected in the extracted hex list
- Dark mode styling was not detected on the live site; all tokens assume light mode
- Animation and transition durations (hover fades, card lift, nav scroll) were not extracted; assumed 150-200ms ease-in-out based on common gaming peripheral patterns
- The extracted hex list includes many colors likely from Shopify checkout widgets (Afterpay, Klarna, PayPal) and social media icons; the brand's true primary is #56b7e6 (cyan), which appears consistently across navigation, CTAs, and product highlights
- Switch type colors (brown, silver, green, yellow, white) are inferred from mechanical keyboard industry standards and the extracted hex list; actual brand-specific switch colors may vary
- Font weights for athena, athena-inline, bodega-sans, ccmeanwhile, elfreth, new-spirit, and subway-berlin-sc are estimated based on common variable font weights; actual font files may support different weight ranges
- Letter spacing values for uppercase condensed typography are estimated at 0.5-1px based on brand patterns; actual values may differ
- Product card shadow values are estimated; actual box-shadow properties not extracted
- Hero banner height values are estimated from common e-commerce patterns; actual heights may vary by page
- Footer link hover color is assumed to match primary cyan; actual hover color not extracted
