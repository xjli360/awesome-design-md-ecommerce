---
version: alpha
name: "Fangamer"
source_url: "https://www.fangamer.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep navy canvas (#052f47) sets the stage for a riot of saturated accent colors — cherry red (#f32b27), electric pink (#d1007a), lime green (#70d800), and cyan (#81cce3) — that signal Fangamer's indie-game-merch identity with the visual energy of a convention hall floor. The site runs Montserrat Variable across all text, a geometric sans-serif that balances readability with a slightly playful, approachable character. Buttons and interactive elements lean into the brand's game-adjacent personality: primary CTAs use the signature red (#f32b27) with white text and {rounded.sm} corners, while secondary actions adopt the deep navy (#052f47) for a more grounded, trustworthy feel. Product cards float on white (#ffffff) canvases with subtle {rounded.md} corners and thin hairline borders (#dedede), letting the vibrant product photography — often featuring plush toys, enamel pins, and retro-style shirts — do the heavy lifting. The top navigation bar sits at 64px tall, using the navy background with white text, and collapses to a hamburger menu on mobile. Search is a full-width bar with {rounded.full} ends and a magnifying-glass icon in the brand red. The footer repeats the navy field with a grid of links in muted gray (#5897bf) and social icons in the brand's accent palette. Badges for "NEW", "SALE", or "EXCLUSIVE" appear as small pills in either red or lime green, using {rounded.full} and uppercase Montserrat at 10px. The overall mood is that of a lovingly curated indie game store — maximalist in color, minimalist in layout, with every accent color feeling earned by the merchandise it frames.

colors:
  primary: "#f32b27"
  primary-active: "#d1007a"
  primary-disabled: "#dedede"
  ink: "#052f47"
  body: "#121212"
  muted: "#5897bf"
  muted-soft: "#81cce3"
  hairline: "#dedede"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#70d800"
  accent-cyan: "#81cce3"
  accent-yellow: "#ffcf40"
  badge-new: "#70d800"
  badge-sale: "#f32b27"
  badge-exclusive: "#d1007a"
  star-rating: "#ffcf40"

typography:
  display-xl:
    fontFamily: "'Montserrat Variable', Montserrat, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Montserrat Variable', Montserrat, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "#042438"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-accent:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-icon:
    color: "{colors.primary}"
    size: 20px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 24px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 8px 12px 0 12px
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: 4px 12px
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-exclusive:
    backgroundColor: "{colors.badge-exclusive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
    hoverColor: "{colors.on-primary}"
  footer-heading:
    color: "{colors.on-primary}"
    typography: "{typography.caption}"
    textTransform: uppercase
    letterSpacing: 1px
  social-icon:
    color: "{colors.muted-soft}"
    size: 24px
    hoverColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: 64px 24px
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.on-primary}"
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
    height: 48px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the signature cherry red (#f32b27) background with white Montserrat 14px/600 text. Corners are softly squared at {rounded.sm} (8px). On hover, the background shifts to the electric pink (#d1007a) for a playful, energetic transition. The disabled state drops to a light gray (#dedede) with muted text, signaling the button is non-interactive without visual noise. Padding is generous at 12px vertical / 24px horizontal, creating a comfortable tap target.

**`button-secondary`** — A darker alternative using the deep navy (#052f47) background, typically employed for "View Details" or "Learn More" actions on light canvases. Hover state darkens slightly to #042438. Same typography and padding as primary, maintaining visual consistency across the button family.

**`button-ghost`** — A text-only variant with no background, using the navy ink color. Used for tertiary actions like "Cancel" or "Clear Filters." Hover adds a subtle background tint (not yet extracted, likely 10% opacity of the primary).

**`button-pill-accent`** — A fully rounded pill button in the lime green (#70d800) accent, used sparingly for celebratory CTAs like "Shop the Drop" or "Limited Edition." Smaller typography (12px/600) and tighter padding (8px/16px) make it feel like a badge-like action.

### Navigation
**`nav-bar`** — A fixed 64px bar in the deep navy (#052f47) with white navigation links. The logo sits left-aligned, typically as a wordmark or icon in white. Links use {typography.nav-link} (14px/600) with 0.5px letter spacing for a slightly spaced, modern feel. The active link is underlined with a 2px red (#f32b27) border. On mobile (< 744px), the nav collapses to a hamburger icon that opens a full-screen overlay menu.

**`nav-link-active`** / **`nav-link-inactive`** — Active links are white with a red bottom border; inactive links use the muted cyan (#81cce3) to reduce visual weight while remaining legible against the dark background.

### Cards
**`product-card`** — A white card with {rounded.md} (12px) corners, no background shadow (the site uses thin borders instead), and a 1:1 aspect ratio product image at the top. The image has rounded top corners only, creating a clean transition to the text below. Title uses {typography.title-sm} (16px/500) and price uses {typography.body-md} (16px/400) in the primary red. Cards are typically displayed in a 2-4 column grid depending on viewport.

### Badges
**`badge`** — Small, fully rounded pills in uppercase 10px/700 Montserrat with 0.8px letter spacing. Three variants exist: green (#70d800) for "NEW", red (#f32b27) for "SALE", and pink (#d1007a) for "EXCLUSIVE." The green badge uses dark text (#052f47) for contrast; red and pink use white. Badges are positioned absolutely over the top-left corner of product card images.

### Forms
**`text-input`** — Standard input fields with white background, 1px solid light gray (#dedede) border, and {rounded.sm} corners. On focus, the border thickens to 2px and switches to the primary red. Height is 44px with 12px/16px padding for comfortable typing.

**`search-bar`** — A full-width, fully rounded pill input with a magnifying glass icon in the primary red. The input itself is white with a light gray border, and the icon sits inside the left padding. On mobile, the search bar expands to fill the available width below the nav.

### Footer
**`footer`** — A deep navy (#052f47) section with a 4-column grid of links. Column headings are uppercase 13px/500 in white with 1px letter spacing. Links are 14px/500 in the muted blue (#5897bf), transitioning to white on hover. Social media icons (24px) use the muted cyan (#81cce3) and turn red on hover. The footer includes a copyright line in the smallest body size.

### Cart
**`add-to-cart-button`** — A prominent 48px-tall button in the primary red, used on product detail pages. Same styling as `button-primary` but with wider horizontal padding (32px) to accommodate longer text like "Add to Cart — $29.99."

**`cart-badge`** — A small 20px circle in the primary red, positioned on the cart icon in the nav bar. Displays the item count in white 10px/700 text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes to 1 column; search bar becomes full-width below nav; hero section reduces padding to 32px; footer stacks to single column |
| Tablet | 744–1128px | Nav links remain visible but condensed; product grid uses 2 columns; hero uses 48px padding; footer uses 2 columns |
| Desktop | 1128–1440px | Full nav with all links; product grid uses 3-4 columns; hero uses 64px padding; footer uses 4 columns |
| Wide | > 1440px | Max-width container at 1440px with horizontal centering; product grid can use 4 columns; hero may include full-bleed background |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets are the entire card, not just text
- Nav links have 48px minimum tap area
- Search bar is 48px tall for easy tapping
- Category tags are 32px+ tall with generous padding

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product grid reduces columns: 4 → 2 → 1 as viewport shrinks
- Footer columns collapse: 4 → 2 → 1
- Hero section stacks vertically on mobile (image above text)
- Search bar moves from nav to below nav on mobile
- Category filter strip becomes horizontally scrollable on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and ghost buttons not fully extracted (assumed darkening/lightening of base color)
- Error states for form inputs (red border, error message styling) not observed
- Success/confirmation toast styling not extracted
- Loading states (skeleton screens, spinners) not documented
- Dropdown menu styling (for account, collections) not captured
- Modal/overlay styling (for cart, quick view) not extracted
- Star rating component exact sizing and spacing not confirmed
- Product variant selector (size/color swatches) styling not observed
- Mobile nav overlay animation and timing not documented
- Dark mode not supported
- Sub-brand or collection-specific palette variations not extracted
- Checkout flow styling (Shopify default vs. custom) not confirmed
- Focus ring styles for keyboard navigation not extracted
