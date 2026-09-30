---
version: alpha
name: "Teton Gravity Research"
source_url: "https://www.tetongravity.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A high-altitude media and apparel brand where a neon teal (#2aded0) and a sharp chartreuse (#e1e83a) collide against a near-black canvas (#171717), creating the visual voltage of a summit sunrise hitting ice. The brand lives in extremes — the extracted palette runs from deep forest shadows (#082c2a, #0f504b, #16736c) through electric cyan (#5de6db, #90eee7, #b2f3ee) to acidic yellows (#e8ee69, #eff399, #f4f7b8, #fdfdef), with a full grayscale from charcoal (#2c2b2b, #6d6d6d) to silver (#b0b0b0, #d1d1d1, #e7e7e7) and a crisp off-white canvas (#f5f5f5). Denton, a serif with alpine authority, drives display headlines while Inter handles the body — a pairing that says "we take the mountains seriously but we're not a gear catalog." Buttons wear the teal as primary voltage, with chartreuse as an accent jolt for badges and highlights. Cards and containers use soft radii ({rounded.md}) to keep the interface approachable against the hard edges of the subject matter. The brand's signature move is the high-contrast color block — a teal header bar on a white page, or a black hero section with yellow-accented typography — that mimics the abrupt transitions of mountain terrain: treeline to alpine, shadow to sun, snow to rock.

colors:
  primary: "#2aded0"
  primary-active: "#23baaf"
  primary-disabled: "#b2f3ee"
  ink: "#171717"
  body: "#2c2b2b"
  muted: "#6d6d6d"
  muted-soft: "#b0b0b0"
  hairline: "#d1d1d1"
  hairline-soft: "#e7e7e7"
  canvas: "#f5f5f5"
  surface-soft: "#eefcfb"
  surface-card: "#ffffff"
  on-primary: "#171717"
  accent-chartreuse: "#e1e83a"
  accent-chartreuse-active: "#bdc331"
  accent-teal-dark: "#1d978d"
  accent-teal-deep: "#16736c"
  accent-forest: "#0f504b"
  accent-pine: "#082c2a"
  accent-yellow-light: "#f4f7b8"
  accent-yellow-pale: "#fdfdef"
  accent-lime: "#e8ee69"
  accent-olive: "#75791e"
  accent-moss: "#515415"
  accent-charcoal: "#2c2b2b"
  accent-silver: "#b0b0b0"
  accent-smoke: "#d1d1d1"
  accent-off-white: "#f5f5f5"

typography:
  display-xl:
    fontFamily: "'Denton', 'Merriweather', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Denton', 'Merriweather', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Denton', 'Merriweather', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Denton', 'Merriweather', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  caption-uppercase:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
  section: 80px

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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-chartreuse:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-chartreuse-active:
    backgroundColor: "{colors.accent-chartreuse-active}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    rounded: "{rounded.none}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    rounded: "{rounded.none}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 600px
  hero-section-overlay:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 600px
  hero-section-overlay-gradient:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 600px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  section-divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  badge-default:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-accent:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-tag-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 32px
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 44px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-header-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0
  modal-overlay:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-md}"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
  modal-close:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 32px
  modal-close-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 32px
  dropdown-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  dropdown-item:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 8px 16px
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 8px 16px
  dropdown-item-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: 8px 16px
  tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 12px 16px
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: 12px 16px
  tab-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.nav-link}"
    padding: 12px 16px
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
  pagination-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
  loading-spinner:
    backgroundColor: transparent
    textColor: "{colors.primary}"
  loading-spinner-dark:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's signature teal (#2aded0) against dark text (#171717). Used for add-to-cart, submit, and primary navigation actions. On hover, it shifts to a slightly deeper teal (#23baaf). Disabled state uses a pale teal (#b2f3ee) with muted text to signal inactivity while maintaining brand color coherence.

**`button-secondary`** — An outlined-style button on the white canvas (#f5f5f5) with dark ink (#171717) text. Used for secondary actions like "View Details" or "Learn More." Active state fills with the soft hairline (#e7e7e7) to provide a subtle press effect without competing with the primary button.

**`button-accent-chartreuse`** — The brand's secondary voltage, filled with chartreuse (#e1e83a) against dark text. Used for limited-time offers, sale items, or high-energy CTAs where the teal is already present elsewhere on the page. Active state deepens to (#bdc331).

**`button-ghost`** — A transparent button with teal text, used in dense layouts or on colored backgrounds where a filled button would overwhelm. Active state adds a soft teal-tinted background (#eefcfb) for hover feedback.

### Cards
**`product-card`** — A white card with a softly rounded corner ({rounded.md}) containing a product image, title, price, and optional badges. The image area uses the same corner radius to maintain visual continuity. On hover, the card lifts with a subtle shadow (not captured in extracted colors but inferred from standard ecommerce patterns).

**`product-card-badge`** — Small uppercase labels in chartreuse (#e1e83a) for "New" or "Featured" tags. Sale badges use the primary teal (#2aded0), while "Exclusive" or "Limited" badges use the dark ink (#171717) for maximum contrast. All badges use tight tracking (0.8px) and 11px type to stay compact.

### Navigation
**`nav-bar`** — A 64px white bar with uppercase, tightly tracked nav links. The brand uses the full width for desktop, collapsing to a hamburger menu on mobile. On scroll, the bar reduces to 56px to reclaim vertical space while maintaining brand presence.

**`nav-link`** — Uppercase 14px Inter at weight 600 with 0.5px letter-spacing. Active and hover states transition to the primary teal, providing a clear wayfinding signal without underlines or heavy borders.

### Forms
**`text-input`** — Standard 48px input fields with a subtle border (defaulting to hairline #d1d1d1) and 16px horizontal padding. Focus state uses the primary teal as a border color. Error state (not fully extracted) would likely use a red derived from the brand's accent palette.

**`search-bar`** — A pill-shaped ({rounded.full}) search input with 20px horizontal padding, used in the header for site search. The full-radius shape contrasts with the more angular card components, creating a friendly entry point for discovery.

### Footer
**`footer`** — A dark (#171717) footer with light text (#f5f5f5) and muted links (#b0b0b0). Link hover states brighten to white (#f5f5f5). The footer uses the brand's body-sm typography (14px Inter) for a clean, readable hierarchy.

### Badges & Tags
**`badge-default`** — Soft background (#eefcfb) with body text for informational tags. **`badge-primary`** uses the teal fill for emphasis. **`badge-accent`** uses chartreuse for promotional content. **`badge-dark`** uses the ink color for maximum contrast on light backgrounds.

**`category-tag`** — Pill-shaped tags with uppercase 11px type and 1px tracking. Used for filtering products by category (e.g., "Skiing," "Snowboarding," "Climbing"). Active state fills with teal; hover state uses a soft gray (#e7e7e7).

### Interactive Elements
**`icon-button`** — Circular 40px buttons for social sharing, wishlist, and cart actions. Hover adds a soft background (#eefcfb). Primary variant uses the teal fill for high-visibility actions like "Add to Cart."

**`accordion-header`** — Used for FAQ sections and product descriptions. Active state switches text to teal, providing a clear visual cue for expanded content.

**`modal-overlay`** — A dark (#171717) scrim with white modal content. The close button is a circular 32px icon with a soft background, hovering to a slightly darker gray (#e7e7e7).

**`dropdown-menu`** — White dropdowns with 8px vertical padding per item. Hover items get the soft teal background (#eefcfb), while active selections show teal text.

**`tab`** — Uppercase nav tabs for content sections (e.g., "Videos," "Articles," "Shop"). Active and hover states use the primary teal, matching the nav-link pattern.

**`pagination-button`** — Small 36px buttons for page navigation. Active page uses the teal fill; hover adds the soft background.

**`progress-bar`** — A 4px rounded bar using the hairline-soft (#e7e7e7) for the track and teal for the fill. Used for loading states and progress indicators.

**`tooltip`** — Dark (#171717) tooltips with white text, using the caption typography (12px, 0.3px tracking).

**`loading-spinner`** — A teal spinner on light backgrounds, white spinner on dark backgrounds.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger nav, stacked product cards, full-width hero (300px height), stacked footer columns, search bar moves to drawer |
| Tablet | 744–1128px | Two-column product grid, sticky nav with condensed links, hero at 450px height, footer in 2-column grid, search bar in nav |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links visible, hero at 600px height, footer in 4-column grid, search bar prominent in header |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero at 700px height with parallax effect, expanded footer with newsletter signup |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain minimum 44px touch target per WCAG guidelines
- Icon buttons are 40px with 32px icon inset, providing adequate tap area
- Product card CTAs are 44px tall for comfortable tapping
- Category tags are 36px tall with 16px horizontal padding
- Accordion headers have 44px minimum tap height (16px padding top and bottom)
- Dropdown items have 40px minimum tap height (8px padding top and bottom)

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer collapses from 4-column to single-column stacked layout
- Hero text overlay reduces font size from 48px to 28px on mobile
- Search bar collapses to icon-only trigger on mobile, expanding to full-width overlay
- Category filter strip collapses to horizontal scroll on mobile
- Secondary navigation (sub-links) collapses to accordion on mobile
- Product image galleries switch from grid to single-image carousel on mobile
- Accordion content is collapsed by default on all breakpoints
- Modal content uses full-screen on mobile, centered dialog on tablet and above

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for many components are inferred from standard patterns rather than extracted from the live site
- Error state colors (form validation, error messages) were not extracted — likely a red variant not present in the palette
- Dark mode colors were not extracted — the brand may not support dark mode, or it was not detected
- Shadow values (box-shadow, drop-shadow) were not extracted — product card hover states likely use subtle shadows
- Gradient definitions for hero overlays were not extracted — inferred as dark gradient from ink color
- Transition durations and easing curves were not extracted
- Focus ring styles (outline, offset) were not extracted
- Specific font weights for Denton and Inter beyond what was declared in font-family strings were not extracted — weights are inferred from standard brand usage
- Line heights and letter spacing values are inferred from standard typographic practice and may differ from the live site
- The extracted palette includes many teal and chartreuse variants — the exact usage hierarchy (which shade for which purpose) is inferred
- Shopify-specific components (cart drawer, checkout button, product variant selector) were not extracted
- Video player styles (play button, controls, progress bar) were not extracted
- Loading states (skeleton screens, shimmer animations) were not extracted
- The `normalidad-wide` and `proxima-nova` font families were found in extracted declarations but not consistently used — likely legacy or fallback fonts
- The `__Merriweather_577ed0` font family appears as a fallback for Denton — exact usage ratio between Denton and Merriweather is unclear
- Accessibility contrast ratios for all color combinations were not verified against WCAG standards
