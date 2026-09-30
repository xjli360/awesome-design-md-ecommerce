---
version: alpha
name: "Medik8"
source_url: "https://www.medik8.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Medik8 is a clinical skincare brand that bridges the gap between professional-grade efficacy and daily ritualistic use. The brand's visual language is anchored on a stark black-and-white canvas — pure white (#ffffff) surfaces against deep charcoal and near-black inks (#191919, #232323, #262626) — creating a laboratory-like precision that signals science-backed formulations. The signature brand voltage comes through two accent colors: a clinical red (#e32c2b) used sparingly for critical CTAs and price highlights, and a deep forest green (#0a3526) that appears in product badges and sustainability messaging, evoking the brand's commitment to vitamin C and eco-conscious practices. Typography runs monospace exclusively (`{typography.display-xl}` through `{typography.caption}`), a deliberate choice that reinforces the scientific, data-driven ethos — every product feels like a prescription. The system relies on generous whitespace and hairline-thin borders (`{colors.hairline}` #dddddd, `{colors.hairline-soft}` #ededed) to create breathing room around product photography and ingredient lists. Rounded corners are minimal — only `{rounded.xs}` (4px) for buttons and `{rounded.sm}` (8px) for cards — maintaining a crisp, clinical edge that never feels soft or casual. The overall mood is one of controlled precision: a white lab coat aesthetic where every element, from the monospace type to the muted greys (#777777, #878787, #9fa0a5), exists to let the science of skincare speak without visual noise.

colors:
  primary: "#e32c2b"
  primary-active: "#c41e1d"
  primary-disabled: "#f5b3b2"
  ink: "#191919"
  body: "#262626"
  muted: "#777777"
  muted-soft: "#9fa0a5"
  hairline: "#dddddd"
  hairline-soft: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#0a3526"
  accent-blue: "#1990c6"
  accent-blue-active: "#136f99"
  badge-green: "#0a3526"
  badge-red: "#e32c2b"
  star-rating: "#232323"
  scrim: "#000000"
  footer-bg: "#121212"
  footer-text: "#cccccc"

typography:
  display-xl:
    fontFamily: "monospace, 'Courier New', Courier, 'Lucida Sans Typewriter', 'Lucida Typewriter', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.25px
  badge:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "monospace, 'Courier New', Courier, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
  product-badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-bestseller:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    height: 480px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
  radio:
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  radio-checked:
    border: "2px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderTop: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  ingredient-list:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    lineHeight: 1.8
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    fontWeight: 600
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.ink}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.ink}"
    height: 4px
    rounded: "{rounded.full}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  modal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  notification-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  notification-banner-error:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  notification-banner-success:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in clinical red (#e32c2b) with white monospace uppercase text. On hover, it shifts to a deeper red (#c41e1d) for tactile feedback. The disabled state fades to a soft pink (#f5b3b2) with reduced opacity, signaling unavailability without visual noise. Padding is generous at 12px vertical and 24px horizontal, with a crisp 4px corner radius that maintains the brand's clinical edge.

**`button-secondary`** — An outlined alternative that inverts the primary: a white canvas background with a 2px solid ink (#191919) border and ink-colored text. Hover state fills the background with ink and flips text to white. Used for "Add to Basket" secondary actions, "Learn More" links, and form cancellations. The 4px radius and uppercase monospace type ensure it sits comfortably alongside the primary button without competing.

**`button-tertiary`** — A text-only button with no background or border, used for subtle actions like "View All" or "Read Ingredients." Hover state adds an underline via border-bottom. The uppercase monospace type at 14px keeps it legible and on-brand while remaining visually quiet.

**`button-pill-primary`** — A smaller, fully rounded variant of the primary button used for badge-style CTAs, newsletter signups, and mobile filter toggles. The 36px height and 20px horizontal padding make it compact enough for tight spaces while the full border-radius (9999px) introduces the only soft corner in the system.

**`button-pill-outline`** — The outlined counterpart to the pill primary, with a 1px hairline border (#dddddd) and ink text. Used for "Filter" and "Sort" controls on collection pages, and for "Subscribe" toggles in the footer. Hover state fills with surface-soft (#f7f7f7).

### Cards
**`product-card`** — The foundational content container for product listings, featuring a white background with 8px rounded corners. The card contains a product image in a surface-soft (#f7f7f7) background with matching rounded top corners, followed by the product title in title-sm (16px, 600 weight), the price in body-md (16px, 600 weight), and optional badge overlays. Cards sit on a white canvas with 16px of spacing between them, creating a clean grid that lets the product photography lead.

**`product-badge-new`** — A compact 10px uppercase monospace badge in deep forest green (#0a3526) with white text, used to flag newly launched products. The 4px corner radius and 2px/8px padding make it read as a clinical tag rather than a promotional sticker.

**`product-badge-sale`** — Identical structure to the new badge but in the primary red (#e32c2b), used for promotional pricing. The red badge against the white card creates immediate visual hierarchy for sale items.

**`product-badge-bestseller`** — A blue variant (#1990c6) for bestseller designations, completing the three-badge system that lets customers quickly identify product status without reading copy.

### Navigation
**`top-nav`** — A fixed 72px white header with a 1px soft hairline (#ededed) bottom border. The brand logo sits left-aligned, with navigation links in 13px uppercase monospace (600 weight) centered or right-aligned. Active nav links receive a 2px ink (#191919) bottom border, while inactive links render in muted (#777777). The search icon, account icon, and basket icon sit in the right rail as 40px circular icon buttons with surface-soft backgrounds.

**`nav-link-active`** — The active state for top-level navigation, distinguished by a 2px solid ink underline. The uppercase monospace type at 13px with 0.5px letter-spacing creates a precise, clinical reading that matches the brand's scientific positioning.

**`nav-link-inactive`** — The default state for navigation links, rendered in muted grey (#777777) to visually recede behind the active section. Hover state transitions to ink (#191919) with a subtle opacity animation.

### Forms
**`text-input`** — Standard text input fields with a white background, 1px hairline (#dddddd) border, and 4px corner radius. The 48px height and 16px horizontal padding provide comfortable touch targets. Active state swaps the border to ink (#191919), while error state uses primary red (#e32c2b). The monospace body-md (16px) type continues the brand's scientific theme even in form fields.

**`select-dropdown`** — Custom-styled select elements matching the text-input dimensions and border system, with a chevron icon in muted (#777777). The dropdown menu itself uses the same white canvas with 4px radius and a subtle box-shadow for elevation.

**`checkbox`** — Square checkboxes with 4px radius and a 2px hairline border. Checked state fills the box with ink (#191919) and displays a white checkmark. The 20px x 20px size ensures adequate touch targets on mobile.

**`radio`** — Circular radio buttons with a 2px hairline border and full border-radius. Checked state shows a 10px ink-filled inner circle within the 20px outer ring.

### Footer
**`footer`** — A dark section with a near-black background (#121212) and light grey text (#cccccc). The footer is organized into columns with white (#ffffff) column headings in title-sm (16px, 600 weight) and body-sm (14px) links in footer-text. The generous section padding (64px top/bottom) and 24px horizontal padding create breathing room against the dark backdrop. Links hover to white (#ffffff) for clear interaction feedback.

### Accordion
**`accordion`** — Collapsible content sections used on product pages for ingredient lists, how-to-use instructions, and full ingredient disclosures. Each accordion item has a 1px soft hairline (#ededed) top border, with the header in title-sm (16px, 600 weight) and a chevron icon that rotates on open. The content area uses body-sm (14px) in body (#262626) with 8px vertical padding.

### Hero
**`hero-banner`** — Full-width promotional banners at 480px height with a surface-soft (#f7f7f7) background. The hero contains a display-lg (28px, 600 weight) headline, body copy, and a primary CTA button. The generous height and muted background let product imagery or lifestyle photography take center stage without competing with the text.

### Search
**`search-bar`** — A 44px tall search input with surface-soft (#f7f7f7) background, 1px hairline border, and 4px radius. The active state switches to a white background with an ink border, providing clear focus indication. The monospace placeholder text at 14px maintains brand consistency even in utility elements.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-up), hamburger menu replaces top-nav links, hero height reduces to 320px, footer stacks vertically, search bar collapses to icon-only, product badges stack vertically, accordion becomes default for all product info |
| Tablet | 744–1128px | Two-column product grid (2-up), top-nav shows limited links with "More" dropdown, hero height at 400px, footer shows 2-column layout, search bar remains full-width but with reduced padding |
| Desktop | 1128–1440px | Three-column product grid (3-up), full top-nav with all links visible, hero at full 480px height, footer shows 4-column layout, search bar with full 16px padding, product cards show hover states for quick-add |
| Wide | > 1440px | Four-column product grid (4-up) with max-width container at 1440px, all elements at maximum spacing, hero may include parallax effects, footer remains 4-column but with increased section padding to 80px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons use 40px diameter circles, exceeding the 44px target for critical actions
- Product card tap targets use the full card area, not just text links
- Accordion headers use 48px minimum touch height
- Checkbox and radio controls are 20px with 44px tap padding via invisible hit areas
- Mobile navigation links use 48px tap targets with 16px spacing between items

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-in drawer for full navigation
- Product filters collapse to a bottom sheet on mobile, with a "Filter" pill button to trigger
- Footer columns collapse to a single vertical stack below 744px, with accordion-style section headers
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile
- Multi-column ingredient lists collapse to single column on mobile
- Hero banners collapse from full-width text overlay to stacked text-below-image layout below 744px
- Search bar collapses to icon-only trigger on mobile, expanding to full-screen overlay on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons, links, and cards are inferred from common patterns but not extracted from live CSS — actual hover transitions (duration, easing) may differ
- Error styling for form validation (error messages, icon placement, color) is assumed based on the primary red but not confirmed from live data
- Dark mode is not implemented on the live site — all tokens assume light mode only
- Sub-brand or collection-specific palettes (e.g., "Clinical" vs "Daily" ranges) may have distinct color accents not captured here
- Typography scale is reconstructed from monospace declarations and common heading sizes — actual font sizes for every breakpoint are not fully extracted
- Animation and transition timing values (durations, easings, delays) are not available from static analysis
- Icon set and SVG styling (stroke width, fill behavior, sizing) is not documented — icons are assumed to use 24px default with currentColor
- Product swatch colors and their associated hex values for shade selection are not extracted
- Newsletter signup form states (success, error, loading) are not confirmed from live data
- Mobile-specific navigation patterns (drawer animation, overlay opacity, close button placement) are inferred from common patterns
- Print stylesheet and accessibility-focused high-contrast modes are not documented
- Third-party widget styling (reviews, loyalty program, live chat) may override system tokens
- Micro-interactions (button press state, card lift on hover, image zoom on product cards) are not captured from live behavior
