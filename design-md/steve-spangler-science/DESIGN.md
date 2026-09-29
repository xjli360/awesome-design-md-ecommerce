---
version: alpha
name: "Steve Spangler Science"
source_url: "https://www.stevespanglerscience.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A #ff7700 voltage — the color of a chemical reaction about to happen, of a boiling flask catching the lab light — that powers every primary CTA, add-to-cart button, and category badge across a #f3f2f7 canvas. The brand lives in the gap between classroom demonstration and kitchen-table experiment, and its design language mirrors that: a #282f37 ink that reads as serious enough for a science textbook, but a #4592fe accent that feels like the surprise of a color-change reaction. Product cards sit on a #ffffff surface with soft {rounded.md} corners, each one promising a "wow" moment — the Mentos geyser, the Insta-Snow powder, the Soda Geyser tube. The extracted palette runs wide (over 30 hex values), many of them WordPress default swatches and social-icon blues, but the true brand signature is that #ff7700 orange — neither playful peach nor corporate rust, but the exact shade of a safety cone or a reaction that says "stand back and watch." Type is set in system monospace and serif stacks (Andale Mono, Courier, Baskerville) that evoke lab notebooks and printed instructions, not a sleek brand manual. The site feels like a workshop: dense with product, badges, and "NEW!" flags, held together by a consistent orange thread and generous white space that lets the science — not the chrome — take center stage.

colors:
  primary: "#ff7700"
  primary-active: "#df653e"
  primary-disabled: "#fcb900"
  ink: "#282f37"
  body: "#444444"
  muted: "#555555"
  muted-soft: "#7fa9c5"
  hairline: "#e9e9eb"
  hairline-soft: "#f3f2f7"
  canvas: "#f3f2f7"
  surface-soft: "#e9e9eb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#4592fe"
  accent-green: "#116600"
  accent-dark-blue: "#003388"
  accent-teal: "#7bdcb5"
  accent-yellow: "#fcb900"
  accent-red: "#cf2e2e"
  badge-new: "#ff7700"
  badge-sale: "#cf2e2e"
  badge-sold-out: "#555555"
  link: "#015692"
  link-hover: "#003388"

typography:
  display-xl:
    fontFamily: "'Baskerville', 'Book Antiqua', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Baskerville', 'Book Antiqua', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Courier New', 'Courier', 'Andale Mono', monospace"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Courier New', 'Courier', 'Andale Mono', monospace"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Courier New', 'Courier', 'Andale Mono', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Arial Black', 'Arial Bold', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Arial Black', 'Arial Bold', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Arial Black', 'Arial Bold', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 38px
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 38px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    boxShadow: "0 2px 8px rgba(40, 47, 55, 0.08)"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "3px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 {spacing.base} 0
    boxShadow: "0 1px 3px rgba(40, 47, 55, 0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(40, 47, 55, 0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    fontWeight: 700
    padding: "{spacing.xs} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  category-strip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
  category-tab-active:
    color: "{colors.primary}"
    borderBottom: "3px solid {colors.primary}"
  category-tab-inactive:
    color: "{colors.muted}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"
  rating-stars:
    color: "{colors.primary}"
    fontSize: "16px"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The lab-coat orange CTA that drives every purchase and sign-up. Uses Arial Black in all-caps for a bold, instructional feel — like the warning label on a chemistry set. On hover, shifts to `#df653e` (a deeper, more serious orange). Disabled state uses `#fcb900` (a muted yellow-orange) to signal inactivity without confusion.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details." Uses the same all-caps Arial Black typography but in the dark `#282f37` ink against a white background. On hover, the background fills with ink and text flips to white — a satisfying inversion that mirrors a chemical indicator changing color.

**`button-accent-blue`** and **`button-accent-green`** — Smaller, lower-emphasis buttons for category-specific actions (e.g., "Shop Chemistry" or "Shop Physics"). The blue (`#4592fe`) and green (`#116600`) are pulled from the brand's accent palette and signal different science domains without competing with the primary orange.

### Cards
**`product-card`** — The primary product display unit, a white card with soft `{rounded.md}` corners and a subtle shadow that lifts it off the `#f3f2f7` canvas. The image fills the top with a 1:1 aspect ratio and rounded top corners only, creating a natural reading flow from visual to title to price. On hover, the shadow deepens to signal interactivity. The price is always in `#ff7700` — the brand's signature voltage — making it the most scannable element on the card.

**`badge-new`**, **`badge-sale`**, **`badge-sold-out`** — Small, uppercase badges that sit in the top-left corner of product images. The "NEW" badge uses the primary orange to match the brand's excitement tone; "SALE" uses red for urgency; "SOLD OUT" uses gray for finality. All use Arial Black at 11px for maximum readability at small sizes.

### Navigation
**`nav-bar`** — A clean white header with `#282f37` text and a subtle bottom border. At 64px tall, it's compact enough for a content-heavy site but tall enough for comfortable touch targets. The active nav link gets an orange underline — a small but consistent brand signal that persists across all pages.

**`nav-bar-sticky`** — On scroll, the nav gains a soft shadow that creates depth without obscuring content. The shadow uses the ink color at 8% opacity for a natural, non-distracting elevation.

### Forms
**`text-input`** — Standard form inputs with a white background, `{rounded.sm}` corners, and a light gray border. On focus, the border doubles in thickness and turns orange — a clear, accessible state change that doesn't rely on color alone (the thickness change provides redundancy). Error states use a red border for validation feedback.

**`search-bar`** — A pill-shaped search field (`{rounded.full}`) that sits prominently in the nav or hero area. The full-roundness contrasts with the more angular product cards, signaling that search is a friendly, open-ended action. On focus, the border turns orange to match the brand's primary interaction color.

### Footer
**`footer-section`** — A dark `#282f37` footer with light gray text, creating a clear visual boundary between content and site information. Links are muted by default and brighten to white on hover — a subtle but effective way to guide secondary navigation without competing with the main content area.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to 24px; search bar moves to full-width below nav; badges stack vertically on product cards |
| Tablet | 744–1128px | Two-column product grid; nav links show as text (no hamburger); hero maintains 28px display; search bar sits inline in nav; badges remain horizontal |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero uses 36px display; search bar is prominent in nav center; category strip shows all tabs |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centers content; hero uses larger padding; category strip scrolls horizontally if needed |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are at least 48px tall
- Nav links on mobile have 48px minimum tap area
- Search bar is 48px tall on all breakpoints
- Badges are at least 20px tall with 8px padding for finger-friendly tapping

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Category strip becomes horizontally scrollable on mobile (no wrapping)
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Hero section reduces vertical padding by 50% on mobile
- Footer links stack vertically on mobile (single column)
- Search bar moves from inline nav to full-width below nav on mobile
- Accordion-style content sections replace side-by-side layouts below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex list is dominated by WordPress default swatches (the `#abb8c3`, `#f78da7`, `#cf2e2e`, `#ff6900`, `#fcb900`, `#7bdcb5`, `#00d084`, `#8ed1fc`, `#0693e3`, `#9b51e0`, `#b02b2c`, `#edae44`, `#eeee22`, `#83a846`, `#7bb0e7` are all WordPress 5.8+ core palette colors) — the true brand palette is likely smaller, with `#ff7700` as the primary anchor
- No meta theme-color was extracted — the brand may not have set one, or it may be set dynamically
- Font-family declarations are system-level and don't reveal a custom brand typeface — the site likely uses system fonts with no web font loading
- Hover states for links and secondary buttons are inferred from common patterns, not extracted
- Error styling for forms (validation messages, error icons) was not observed
- Dark mode support is unknown — the extracted palette is entirely light-mode
- Sub-brand or seasonal color variations (holiday kits, limited editions) were not captured
- Loading states, skeleton screens, and empty states were not observed
- Animation timing and easing curves were not extracted
- The extracted palette includes social-icon blues (`#4592fe`, `#0693e3`) that may not be brand colors — they appear frequently in checkout widgets and social share buttons
