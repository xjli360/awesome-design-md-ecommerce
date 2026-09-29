---
version: alpha
name: "Grove Collaborative"
source_url: "https://www.grove.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Grove Collaborative presents itself as a trusted, earth-conscious home essential marketplace where the brand's voice is warm, approachable, and quietly authoritative. The palette is anchored by a deep, almost charcoal ink (`#303030`) that reads as serious and grounded, paired with a soft, natural canvas (`#f7f7f7`) that feels like unbleached linen. The primary action voltage comes from a rich, botanical green (`#1f3521`) — a color that whispers sustainability rather than shouting it, with an active state that deepens to `#121212` for press moments. Supporting accents include a muted terracotta (`#cc6328`), a playful coral (`#bf339d`), and a fresh minty highlight (`#cdec85`) that appears in badges and promotional tags. The system relies heavily on soft, warm neutrals: `#eeeeee`, `#e0e0e0`, `#f3f3f3`, and `#f1f1f1` create layered surfaces that feel tactile and organic, while the hairline (`#dedede`) and muted-soft (`#aaaaaa`) keep the interface airy. Typography uses ValueSans as the workhorse — a clean, humanist sans-serif that appears in Regular, Medium, and Bold weights — with ValueSerif Bold reserved for editorial moments like hero headlines or ingredient storytelling. Buttons and cards carry soft rounded corners (`{rounded.sm}` at 8px for CTAs, `{rounded.md}` at 12px for cards), avoiding the pill-shaped extremes of hospitality brands in favor of a gentle, approachable geometry. The overall mood is one of considered simplicity: plenty of whitespace, restrained use of color, and a trust in product photography and ingredient lists to do the heavy lifting. Signature design moves include a persistent top nav with a bold green logo lockup, category strips with soft dividers, and a footer that feels like a brand manifesto — dense with links, certifications, and sustainability pledges. The system feels like a well-edited pantry: everything has its place, nothing is loud, and the warmth comes from the materials themselves.

colors:
  primary: "#1f3521"
  primary-active: "#121212"
  primary-disabled: "#6b7280"
  ink: "#303030"
  body: "#2b2b2b"
  muted: "#707070"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#f7f7f7"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-terracotta: "#cc6328"
  accent-coral: "#bf339d"
  accent-mint: "#cdec85"
  accent-teal: "#aaf2f3"
  accent-ocean: "#1990c6"
  accent-ocean-deep: "#136f99"
  accent-ocean-dark: "#033b4c"
  error: "#ef4444"
  error-strong: "#d12121"
  error-deep: "#c70000"
  star-rating: "#cc6328"
  badge-new: "#cdec85"
  badge-sale: "#d12121"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'ValueSerif Bold', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ValueSerif Bold', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.15px
  link:
    fontFamily: "'ValueSans Regular', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'ValueSans Medium', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
    padding: 12px 24px
    height: 44px
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
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
  button-accent-terracotta:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 7px 19px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "2px solid {colors.error}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 44px
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    minHeight: 100px
  checkbox:
    backgroundColor: "{colors.surface-card}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    size: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.surface-card}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    size: 20px
  radio-checked:
    border: "6px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    width: 44px
    height: 24px
  toggle-active:
    backgroundColor: "{colors.primary}"
  toggle-knob:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    size: 20px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-logo:
    height: 32px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  nav-icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  nav-icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid transparent"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-card}"
  search-bar-icon:
    textColor: "{colors.muted}"
    size: 20px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: 8px
    left: 8px
  product-card-sale-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: 8px
    left: 8px
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.accent-terracotta}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-add-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    margin: "{spacing.sm} {spacing.base}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.base} 0"
    overflowX: auto
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.full}"
    whiteSpace: nowrap
  category-tab-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.full}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-banner-image:
    rounded: "{rounded.md}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    textDecoration: underline
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.base}"
  footer-divider:
    backgroundColor: "rgba(255,255,255,0.2)"
    height: 1px
    margin: "{spacing.xl} 0"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sustainability:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-ocean:
    backgroundColor: "{colors.accent-ocean}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.lg} 0"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  loading-spinner:
    border: "3px solid {colors.hairline-soft}"
    borderTopColor: "{colors.primary}"
    size: 24px
    rounded: "{rounded.full}"
  skeleton:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    animation: "pulse 1.5s infinite"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for add-to-cart, submit, and key conversion points. Rendered in the brand's deep green (`{colors.primary}`) with white text and a soft 8px corner radius (`{rounded.sm}`). On hover, the background shifts to `{colors.primary-active}` (`#121212`) for a subtle press effect. The disabled state uses `{colors.primary-disabled}` (`#6b7280`) to signal inactivity without visual noise.
**`button-secondary`** — A ghost-style button with a white background, ink text, and a 1px hairline border (`{colors.hairline}`). Used for less prominent actions like "Cancel" or "Learn More". On hover, the border darkens to `{colors.hairline}` and a subtle shadow may appear. The text-only variant (`button-tertiary-text`) drops the border entirely and adds an underline, used for inline links within content blocks.
**`button-accent-terracotta`** — A secondary accent button using the warm terracotta (`{colors.accent-terracotta}`) for promotional or seasonal CTAs. Shares the same sizing and padding as `button-primary` but introduces a warmer, earthier tone that pairs well with the green primary.
**`button-pill-primary`** — A smaller, fully rounded pill button used in category filters, tag chips, and compact action areas. Uses the primary green with a tighter padding (8px 20px) and smaller typography (`button-sm`). The outline variant (`button-pill-outline`) inverts to a transparent background with a hairline border for secondary filter states.

### Cards
**`product-card`** — The core product display unit, a white card with a 12px rounded corner (`{rounded.md}`) and a soft hairline border (`{colors.hairline-soft}`). The card contains a square aspect-ratio image with rounded top corners, a title using `title-sm` typography, price in `body-md`, and an optional star rating in terracotta (`{colors.accent-terracotta}`). On hover, the border strengthens to `{colors.hairline}` and a subtle box shadow lifts the card. Badges (new, sale, sustainability) are absolutely positioned at the top-left of the image area. An add-to-cart button sits at the bottom of the card, using the primary green with compact padding.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height with a white background and a soft bottom border (`{colors.hairline-soft}`). The logo sits on the left at 32px height, followed by nav links using `nav-link` typography. Active links gain a 2px green bottom border (`{colors.primary}`) and green text color. Icon buttons (search, cart, account) are 40px circular touch targets that show a soft background fill on hover (`{colors.surface-soft}`). The search bar is a full-height pill with a soft gray background (`{colors.surface-soft}`) that expands on focus with a green border.

### Forms
**`text-input`** — Standard text input with a white background, 1px hairline border, 8px corner radius, and 44px height. On focus, the border becomes a 2px green stroke (`{colors.primary}`) with no outline. Error state uses a 2px red border (`{colors.error}`). Disabled inputs fade to a soft gray background (`{colors.surface-soft}`) with muted text. The select input shares the same sizing but includes a dropdown arrow. Textareas extend the pattern with a 100px minimum height. Checkboxes and radios use a 20px square/circle with a 2px hairline border, switching to a filled green state when checked. Toggles are 44x24 pills with a white circular knob that slides from gray to green.

### Badges
**`badge-new`** — A small, uppercase label in the fresh mint green (`{colors.badge-new}`) with dark text, used to flag new arrivals. The `badge-sale` variant uses the deep red (`{colors.badge-sale}`) with white text for markdowns. The `badge-sustainability` variant uses the accent mint (`{colors.accent-mint}`) for eco-friendly or certified products. The `badge-ocean` variant uses the ocean blue (`{colors.accent-ocean}`) for water-related or ocean-safe products. All badges share the same 11px uppercase typography, 4px corner radius, and compact 2px 8px padding.

### Hero
**`hero-banner`** — A full-width section with a soft gray background (`{colors.surface-soft}`), generous padding (64px top/bottom, 32px sides), and a minimum height of 400px. The headline uses the serif `display-xl` typography for editorial weight, paired with a supporting subheading in `body-md` muted text. A single primary CTA button sits below with extra top margin. The hero image is rendered with a 12px corner radius for a soft, editorial feel.

### Footer
**`footer`** — A full-width, dark green footer (`{colors.primary}`) with white text, serving as the brand's manifesto space. Links are white with no underline by default, gaining an underline on hover. Section headings use `title-sm` typography with bottom margin. A semi-transparent white divider (`rgba(255,255,255,0.2)`) separates content sections. The footer is dense with columns for shop links, about us, sustainability commitments, and social proof elements.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack in 2-column grid; hero banner reduces padding to 32px; footer links stack vertically; search bar hides behind icon; category strip scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows limited links with "More" dropdown; hero banner uses 48px padding; footer uses 2-column layout; search bar shows as icon-only |
| Desktop | 1128–1440px | Full nav with all links visible; product cards in 3- or 4-column grid; hero banner at full padding; footer in 4-column layout; search bar fully expanded |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4- or 5-column grid; hero banner may include full-bleed imagery; additional whitespace around content |

### Touch Targets
- All interactive elements (buttons, links, icons) maintain a minimum 44x44px touch target area
- Product card add-to-cart buttons are at least 36px tall with 16px horizontal padding
- Nav icon buttons are 40x40px circles with generous tap area
- Category strip tabs have 8px vertical padding and 16px horizontal padding for easy tapping
- Form inputs are 44px tall with 12px padding for comfortable interaction

### Collapsing Strategy
- Top nav collapses to a hamburger menu on mobile, with a slide-out drawer for links
- Secondary nav (category strip) becomes a horizontally scrollable strip on mobile
- Product grids collapse from 4 columns on desktop to 2 columns on mobile
- Footer columns collapse from 4 on desktop to a single stacked column on mobile
- Hero banner reduces vertical padding and may hide secondary text on mobile
- Search bar collapses to an icon-only trigger on mobile, expanding to full-width overlay on tap
- Multi-step flows (checkout, onboarding) collapse to single-page vertical layouts on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (secondary buttons, nav links, product cards) are inferred from common patterns but not confirmed from live site inspection
- Error state styling for forms (error messages, validation icons) is partially inferred; exact error text color and iconography not confirmed
- Dark mode palette is not present on the live site; all tokens assume light mode only
- Sub-brand or seasonal palettes (holiday, Earth Day, etc.) may exist but were not extracted
- Animation timing and easing curves (transitions, hover effects, loading states) are not captured
- Specific font weights for ValueSans (Regular, Medium, Bold) are inferred from declarations; exact weight numbers (400, 500, 700) are standard mappings
- Dropdown menu styling (mega menu, flyout menus) not observed in detail
- Modal and dialog component styling (overlay, close button, padding) not captured
- Toast/notification component styling not observed
- Star rating component exact sizing and spacing not confirmed
- Quantity selector (plus/minus buttons) styling not observed
- Accordion and disclosure component styling not captured
- Tab component (non-category) styling not observed
- Pagination component styling not captured
- Breadcrumb component styling not observed
- Loading skeleton animation details (timing, color sequence) are inferred
- Focus ring styling (outline color, offset) not confirmed for accessibility
- Print stylesheet behavior not captured
