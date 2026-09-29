---
version: alpha
name: "Retro-Cade"
source_url: "https://www.retro-cade.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A neon-lit arcade cabinet builder that wears its primary voltage — #ff0000 — like a marquee sign on a 1980s boardwalk, then undercuts that aggression with a secondary pulse of cyan (#34e2e4) and deep indigo (#4721fb) that reads more vaporwave than straight-up retro. The palette is deliberately oversaturated: #d92e3a for error states, #ff6b7a for hover glows, #00d084 for "in stock" badges, and #7a00df for limited-edition finishes. But the real surprise is the canvas: #eeeeee, a warm off-white that softens the high-voltage palette and keeps the cabinet configurator from feeling like a casino floor. Typography runs system-native — -apple-system, Arial, Helvetica Neue, Roboto — no custom arcade font, which is a deliberate choice: the brand lets the cabinet artwork and CRT-style screen mockups carry the period flavor while the UI stays legible. Buttons use {rounded.sm} (8px) — a slight softening of the hard-cornered aesthetic you'd expect from a retro brand — while badge pills go {rounded.full} to contrast against the angular cabinet mockups. The nav bar sits at 72px with a sticky white background and a search bar that uses {rounded.full} with a #ff0000 orb, making the primary action feel like a joystick button. Product cards use {rounded.md} (12px) with a #ffffff surface and a hairline border (#dddddd), but the real signature is the "Build Your Own" CTA that uses a gradient from #ff0000 to #d92e3a, mimicking the gradient stripes on a classic arcade cabinet side panel. The brand trusts high-contrast text (#313131 body, #282828 headings) over the #888888 muted tones, keeping readability high even as the palette screams.

colors:
  primary: "#ff0000"
  primary-active: "#d92e3a"
  primary-disabled: "#faaca8"
  ink: "#282828"
  body: "#313131"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#eeeeee"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#34e2e4"
  accent-indigo: "#4721fb"
  accent-purple: "#7a00df"
  accent-green: "#00d084"
  accent-pink: "#ff6b7a"
  accent-red-deep: "#d92e3a"
  accent-blue-deep: "#003388"
  accent-gold: "#fdd79a"
  accent-sage: "#67a671"
  accent-teal: "#004a59"
  accent-deep-purple: "#330968"
  accent-mint: "#31cdcf"
  accent-navy: "#020381"
  badge-new: "#ff6b7a"
  badge-sale: "#00d084"
  badge-limited: "#7a00df"
  star-rating: "#ff1900"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  micro-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px

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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-accent:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-gradient:
    backgroundImage: "linear-gradient(135deg, {colors.primary}, {colors.primary-active})"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  search-orb:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 44px
    width: 44px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  icon-button-outline:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "2px solid {colors.primary}"
  category-strip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "8px 16px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "2px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4/3"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-card-badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-original-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: "line-through"
  configurator-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  configurator-step:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  configurator-step-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "2px solid {colors.primary}"
  configurator-step-complete:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.hairline}"
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "3px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.surface-card}"
    typography: "{typography.title-sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
  hero-secondary-cta:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "15px 31px"
    height: 56px
    border: "2px solid {colors.hairline}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  testimonial-rating:
    textColor: "{colors.star-rating}"
    fontSize: 16px
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.ink}"
    height: 2px
  badge-new-flag:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale-flag:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited-flag:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "2px solid {colors.accent-red-deep}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  radio-checked:
    border: "2px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-thumb:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 8px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  toast-success:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 20px"
  toast-error:
    backgroundColor: "{colors.accent-red-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 20px"
  toast-info:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 20px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the full-strength #ff0000 background with white text and 8px rounded corners. On hover, shifts to `button-primary-active` (#d92e3a) for a deeper red that signals interactivity. The disabled state uses `button-primary-disabled` (#faaca8), a washed-out pink that maintains readability while clearly indicating non-interactivity.

**`button-secondary`** — A white-background button with a 2px hairline border (#dddddd) and dark ink text, used for secondary actions like "Learn More" or "View Details." Matches the height and padding of the primary button for visual alignment in button groups.

**`button-tertiary-text`** — A text-only button using the primary red for text color, no background or border. Used for less prominent actions like "Cancel" or "Skip" within forms and configurator flows.

**`button-pill-primary`** — A fully pill-shaped variant of the primary button, used for compact actions like "Add to Cart" or "Quick Build." Smaller padding and font size than the standard primary button.

**`button-pill-accent`** — A pill-shaped button using the cyan accent (#34e2e4) as background with dark ink text, used for secondary promotional actions or "Shop Now" CTAs on featured products.

**`button-gradient`** — A signature Retro-Cade button that uses a diagonal gradient from #ff0000 to #d92e3a, mimicking the gradient stripes on classic arcade cabinet side panels. Used exclusively for the "Build Your Own Cabinet" CTA on the hero and product pages.

### Navigation
**`top-nav`** — A 72px sticky navigation bar with white background, 1px hairline bottom border, and dark ink text. Contains the brand logo, nav links, search orb, and cart icon. Nav links use `nav-link-active` with a 3px primary-red bottom border for the active page, and `nav-link-inactive` with muted text for non-active pages.

**`search-orb`** — A 44px circular button with #ff0000 background and white icon, positioned in the top nav. Functions as a search toggle that expands into the full `search-bar-pill` on click. The orb shape references the start button on a classic arcade cabinet.

**`search-bar-pill`** — A fully pill-shaped search input with soft gray background (#f5f5f5) and 1px hairline border. On focus, transitions to `search-bar-focused` with a 2px primary-red border and white background.

**`category-strip`** — A horizontal scrollable strip of category tabs below the hero, using white background and muted text. Active categories use `category-tab-active` with a soft gray background and full pill shape, while inactive tabs use `category-tab-inactive` with transparent background.

### Cards
**`product-card`** — A white card with 12px rounded corners, 1px hairline border, and 16px padding. Contains an image area with 8px rounded corners and 4:3 aspect ratio, product title, price (primary red), original price (muted with line-through), and badge flags. On hover, transitions to `product-card-hover` with a 2px primary-red border and subtle box shadow.

**`product-card-badge`** — A fully pill-shaped badge positioned at the top-left of the product card image. Three variants: `product-card-badge` (#ff6b7a for "New"), `product-card-badge-sale` (#00d084 for "Sale"), and `product-card-badge-limited` (#7a00df for "Limited Edition"). All use uppercase 11px bold text.

**`testimonial-card`** — A white card with 12px rounded corners, 1px hairline border, and 24px padding. Contains customer quote text, star rating in #ff1900, and customer name. Used on the homepage and product detail pages.

### Forms
**`text-input`** — A standard text input with white background, 8px rounded corners, 1px hairline border, and 48px height. On focus, transitions to `text-input-focused` with a 2px primary-red border. Error state uses `text-input-error` with a 2px deep-red border (#d92e3a).

**`select-input`** — A dropdown select matching the text input styling, used for cabinet model selection, finish options, and quantity.

**`checkbox`** and **`radio`** — Standard form controls with 2px hairline borders. Checked states use primary-red background for checkboxes and primary-red border for radio buttons.

**`toggle`** — A 44x24px pill-shaped toggle with hairline background. Active state uses primary-red background. The thumb is a 20px white circle.

### Configurator
**`configurator-panel`** — The main cabinet builder interface, a white card with 12px rounded corners, 24px padding, and 1px hairline border. Contains multiple `configurator-step` panels.

**`configurator-step`** — Individual step panels within the configurator, using soft gray background and 8px rounded corners. Active steps use `configurator-step-active` with a 2px primary-red border. Completed steps use `configurator-step-complete` with green background (#00d084) and white text.

**`color-swatch`** — A 32px circular color swatch with 2px hairline border. Selected state uses `color-swatch-selected` with a 3px primary-red border. Used for cabinet finish selection.

### Footer
**`footer`** — A dark footer section with #282828 background and white text. Uses 64px vertical padding and 24px horizontal padding. Footer links use `footer-link` with muted-soft color (#aaaaaa) and 14px body font. Footer headings use `title-sm` typography with white color.

### Feedback
**`toast-success`** — A green (#00d084) notification toast with white text, 8px rounded corners, and 12x20px padding. Used for successful actions like "Added to cart."

**`toast-error`** — A deep-red (#d92e3a) notification toast with white text, used for error states like "Out of stock."

**`toast-info`** — A cyan (#34e2e4) notification toast with dark ink text, used for informational messages like "Free shipping on orders over $100."

**`tooltip`** — A dark (#282828) tooltip with white text, 8px rounded corners, and 6x12px padding. Used for hover explanations on configurator options.

**`modal-overlay`** and **`modal-card`** — A semi-transparent black overlay with a white modal card using 12px rounded corners and 32px padding. Used for the "Quick Build" preview and "Add to Cart" confirmation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger, configurator becomes vertical stepper, product cards stack full-width, hero CTA buttons stack vertically, search bar hides behind orb icon |
| Tablet | 744–1128px | Two-column product grid, configurator uses side-by-side steps, nav shows 4-5 links, hero uses side-by-side CTA buttons, search bar shows as icon-only |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, configurator shows 3-column step layout, hero uses full-width layout with large CTA, search bar shows full pill |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, configurator uses 4-column layout, hero uses centered layout with max-width 1200px, search bar shows full pill with expanded width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target
- Product card CTAs use 56px height on mobile for easier tapping
- Color swatches expand to 44px on mobile with increased tap padding
- Category strip uses horizontal scroll with snap points on mobile
- Configurator steps use 56px minimum height on mobile for tap targets

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px, with slide-out drawer
- Product grid collapses from 4 columns to 1 column on mobile
- Configurator steps collapse from side-by-side to vertical stepper on mobile
- Hero section collapses from side-by-side layout to stacked on mobile
- Footer columns collapse from 4 columns to 2 columns on tablet, 1 column on mobile
- Category strip shows first 3 categories as pills on mobile, rest in "More" dropdown
- Search bar collapses to icon-only orb on mobile, expands on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (buttons, cards, inputs) are inferred from the primary color and common patterns — actual site hover colors could not be extracted
- Error state styling (form validation messages, error icons, error border colors) is inferred from the deep red (#d92e3a) — actual error patterns may differ
- Dark mode is not present on the live site — no dark theme tokens could be extracted
- Animation and transition durations, easing functions, and micro-interactions could not be extracted
- Font weights beyond 400, 500, 600, 700, and 800 are inferred — the live site uses system fonts with variable weights
- The extracted color list includes 30+ colors, many of which may be from third-party widgets (payment buttons, social icons) rather than brand colors — the primary (#ff0000), cyan (#34e2e4), indigo (#4721fb), and deep red (#d92e3a) are the most likely brand colors
- No custom font family was found — the site relies entirely on system fonts, which is unusual for a brand with a strong visual identity
- The extracted colors include several that appear to be from WordPress block editor defaults (#0693e3, #007cba, #006ba1, #005a87) — these have been excluded from the brand palette
- No loading states, skeleton screens, or spinner styles could be extracted
- No print styles or reduced-motion preferences could be extracted
- The meta theme-color tag is absent, suggesting no browser chrome theming is implemented
- No sub-brand or collection-specific palette variations could be extracted
