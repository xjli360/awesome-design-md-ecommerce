---
version: alpha
name: "Caudabe"
source_url: "https://www.caudabe.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A precision-focused phone-accessory brand that builds its identity on the tension between #866a41, a warm, weathered leather tone, and #108474, a cool, deep teal that reads as industrial rather than aquatic. The palette is overwhelmingly neutral — #f0f0f0, #dcdcdc, #eeeeee, #f9f9f9, #f7f7f7, #fafafa, #f3f3f3, #dadada form a layered gray scale that lets the two accent colors carry all the brand voltage. Typography runs Futura PT across every weight from Book to Black, a geometric sans-serif that brings mid-century modernist rigor to product descriptions and navigation. The brand uses hard corners ({rounded.none}) on product cards and buttons, a deliberate choice that signals durability and precision tooling — there are no pill shapes or soft radii to soften the industrial proposition. The meta theme-color of #000000 sets a black chrome expectation before the page loads, and the extracted palette's density of mid-grays (#777777, #656565, #525252, #515151, #757575, #5e5e5e, #7b7b7b, #848484, #858585, #787878, #969696, #aaaaaa, #afafaf) suggests a system that grades from #1c1c1c near-black through to #f0f0f0 near-white with surgical precision. The distinctive #4d384b (a muted plum) and #126bbf (a technical blue) appear as secondary accents, likely for limited-edition product drops or category badges. This is a brand that trusts material photography and geometric type over decorative flourish — every design decision reads as engineered rather than styled.

colors:
  primary: "#866a41"
  primary-active: "#6b5233"
  primary-disabled: "#c4b49a"
  ink: "#1c1c1c"
  body: "#363636"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#dcdcdc"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#f9f9f9"
  surface-strong: "#f0f0f0"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  accent-plum: "#4d384b"
  accent-blue: "#126bbf"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Futura PT', futura-pt, futura-pt-bold, bebas-neue, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  button-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-swatch:
    rounded: "{rounded.full}"
    height: 16px
    width: 16px
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-material:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    borderColor: "{colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    borderColor: "{colors.accent-plum}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  section-heading:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  color-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    borderColor: "{colors.ink}"
    borderWidth: 2px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
  feature-grid:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  feature-item-icon:
    height: 32px
    width: 32px
  feature-item-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  feature-item-description:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  testimonial-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in {colors.primary} with {colors.on-primary} text and zero border radius. The uppercase Futura PT at 14px with 1px letter-spacing gives it a precision-tooled, industrial feel. On hover, it shifts to {colors.primary-active} for depth without animation flourish. The disabled state uses {colors.primary-disabled}, a desaturated tan that signals unavailability without breaking the neutral palette.

**`button-secondary`** — A white button with {colors.ink} text, used for secondary actions like "View Details" on product cards. The 1px border is implied by the 13px vertical padding (1px less than primary's 14px) to maintain equal 48px height. Active state uses {colors.surface-strong} background.

**`button-outline`** — Transparent background with {colors.ink} text and a 1px solid {colors.hairline} border. Used for "Add to Cart" on product detail pages and filter toggles. The hard corner reinforces the brand's precision engineering language.

**`button-text`** — A text-only button with no background or border, used for "Learn More" links in feature grids and "Read Reviews" on product cards. The uppercase styling and letter-spacing maintain brand consistency even without a container.

### Navigation
**`top-nav`** — A 72px fixed header with {colors.canvas} background and {colors.ink} navigation links. The brand logo sits left-aligned, with product category links (Cases, Screen Protectors, Accessories) centered and utility icons (Search, Account, Cart) right-aligned. Active nav links use {colors.ink} while inactive use {colors.muted}. The nav collapses to a hamburger menu below 744px.

**`nav-link`** — Uppercase Futura PT at 14px with 0.5px letter-spacing, matching the button typography's precision. The active state has no underline or indicator — the brand trusts the user's spatial memory of the layout.

### Cards
**`product-card`** — A zero-radius card with {colors.canvas} background and {colors.ink} product title. The product image fills a 1:1 aspect ratio with no rounding. On hover, the card background shifts to {colors.surface-soft} and a subtle shadow appears. The price sits in {colors.body} below the title, with color swatches ({rounded.full}, 16px) for material variants.

**`product-card-hover`** — The hover state uses {colors.surface-soft} background with a 1px {colors.hairline} border and a subtle box-shadow (0 2px 8px rgba(0,0,0,0.08)). No scale or translate transforms — the brand avoids motion that could suggest fragility.

### Badges
**`badge-new`** — A teal ({colors.accent-teal}) badge with white uppercase text, used for newly released products. The zero-radius rectangle sits in the top-left corner of product images. The 11px Futura PT Bold with 0.5px letter-spacing is the smallest uppercase treatment in the system.

**`badge-sale`** — A black ({colors.ink}) badge with white text, used for clearance items. The high contrast against product photography ensures visibility without competing with the product itself.

**`badge-material`** — A light gray ({colors.surface-strong}) badge with {colors.body} text, used for material labels like "Leather" or "Silicone". The 12px regular weight sits below the product title on detail pages.

### Forms
**`text-input`** — A zero-radius input field with {colors.canvas} background and 12px/16px padding. On focus, the border shifts to {colors.ink} for clear state indication. Error states use {colors.accent-plum} border — the muted plum signals an issue without the alarm of red. Used for email signup, search, and checkout forms.

**`search-bar`** — A {colors.surface-soft} background input with {colors.muted} placeholder text, used in the mobile navigation and search overlay. The zero-radius rectangle matches all other input fields in the system.

### Footer
**`footer-link`** — Standard link styling in {colors.muted} at 14px regular weight. The footer uses a three-column layout with {colors.ink} headings in {typography.title-sm} and links stacked vertically. A {colors.hairline} divider separates the footer from the main content area.

### Hero
**`hero-section`** — A full-width section with {colors.canvas} background and {colors.ink} display typography. The hero uses large product photography (often a single case on a clean surface) with the product name in {typography.display-xl} and a {colors.primary} CTA button. The section padding uses {spacing.section} (80px) top and bottom for generous breathing room.

### Feature Grid
**`feature-grid`** — A {colors.surface-soft} background section with 32px icons and {colors.ink} titles. Each feature item uses a three-column layout on desktop, collapsing to single column on mobile. The {colors.body} description text sits below the title with no rounding or card containers — just typography and whitespace.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, hero text reduced to {typography.display-md} |
| Tablet | 744–1128px | Two-column product grid, expanded nav with dropdowns, two-column footer |
| Desktop | 1128–1440px | Three-column product grid, full nav, three-column footer, hero at full {typography.display-xl} |
| Wide | > 1440px | Max-width container at 1440px centered, product grid expands to four columns |

### Touch Targets
- All buttons and interactive elements maintain minimum 48px height for touch accessibility
- Color swatches are 24px with 2px selected border for clear tap targets
- Nav links have 44px minimum tap area even when text is smaller
- Search bar and text inputs maintain 48px height for comfortable mobile interaction

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with slide-out drawer for links
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer collapses from 3 columns to 2 columns at tablet, to stacked single column at mobile
- Hero section reduces heading size and stacks CTA below copy at mobile
- Feature grid collapses from 3 columns to single column at mobile, with icons remaining left-aligned

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components are inferred from brand patterns rather than extracted from live CSS — actual transitions, shadows, and border colors may vary
- Error, success, and warning states for form validation were not observed — the {colors.accent-plum} error border is an assumption based on the extracted palette
- Dark mode styling is not present on the live site — no dark theme tokens exist in the extracted data
- The extracted color list is dominated by grays and neutrals — the true brand primary (#866a41) and secondary (#108474) are distinctive but appear infrequently in the extracted frequencies, suggesting they're used sparingly as accent colors rather than background fills
- Font weights for Futura PT variants (Book, Medium, Demi, Bold, Black) are mapped to numeric values based on standard font-weight conventions, not extracted CSS — actual weight values may differ
- Shopify checkout widget colors (Klarna, Afterpay, PayPal buttons) may be present in the extracted palette but could not be isolated — some gray values may belong to third-party payment elements rather than the brand system
- Animation durations, easing curves, and transition properties were not extracted — the brand appears to use minimal motion
- Product card shadow values are estimated — actual box-shadow properties were not captured in extraction
- The meta theme-color of #000000 suggests a black browser chrome expectation, but the site canvas is white — this may indicate a dark mode preference or a brand update in progress
