---
version: alpha
name: "Hexclad"
source_url: "https://hexclad.com"
captured_at: "2026-09-28T04:10:16.214740+00:00"
evidence_status: "historical_partial_css_evidence"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Hexclad is a cookware brand built on the tension between two worlds — stainless steel performance and non-stick convenience — and its design system mirrors that hybrid philosophy. The palette is anchored in industrial darkness: `#0e0e0e` and `#1a1a1a` form the deep canvas, while `#303030` and `#2b2b2b` provide layered surfaces that feel machined and precise. Against this dark backdrop, a single red voltage — `#d73939` in its primary form, sharpening to `#c70000` on active states and softening to `#ef4444` for hover — acts as the brand's signature accent, appearing on primary CTAs, sale badges, and the iconic hexagonal pattern that gives the brand its name. The system is unapologetically bold: `{rounded.sm}` (8px) corners on buttons and cards keep edges crisp and engineered, while `{rounded.full}` pill shapes on search bars and badges introduce a surprising softness. Typography layers Canela, a refined serif for display moments, alongside din-2014 for technical body copy, creating a dialogue between warmth and precision. The muted palette — `#707070`, `#6b7280`, `#aaaaaa` — handles secondary text and hairlines, while `#dfd5c4` and `#d9d8d6` appear as warm neutral accents on cards and surfaces, preventing the system from feeling cold. The brand's Shopify heritage shows in its component-heavy layout: product cards with `{rounded.md}` (12px) corners, a persistent sticky nav bar at 72px, and a footer that stacks generously at `{spacing.section}` (64px). Hexclad's design language is not about hiding its construction — it's about celebrating the hybrid, the welded, the dual-natured.

colors:
  primary: "#d73939"
  primary-active: "#c70000"
  primary-disabled: "#ef4444"
  primary-hover: "#ef4444"
  ink: "#0e0e0e"
  body: "#303030"
  muted: "#707070"
  muted-soft: "#aaaaaa"
  hairline: "#cccccc"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  surface-mid: "#2b2b2b"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-warm: "#dfd5c4"
  accent-warm-soft: "#d9d8d6"
  badge-sale: "#d73939"
  badge-new: "#805ad5"
  badge-new-bg: "#322659"
  star-rating: "#cc6328"
  hex-pattern: "#303030"
  scrim: "#0a0a0a"
  error: "#d12121"
  success: "#1f3521"
  success-soft: "#11322c"

typography:
  display-xl:
    fontFamily: "'Canela', 'Sawarabi', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Canela', 'Sawarabi', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Canela', 'Sawarabi', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0
  display-sm:
    fontFamily: "'Canela', 'Sawarabi', serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.3px
  caption-sm:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0
  badge:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0
  nav-link:
    fontFamily: "'din-2014', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.8px
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
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    opacity: 0.5
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-outline-light:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 48px
    border: "2px solid {colors.on-primary}"
  button-pill-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-pill-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(14,14,14,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-pill-focus:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(14,14,14,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(14,14,14,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new-bg}"
    textColor: "{colors.badge-new}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.star-rating}"
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 500px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  hero-cta-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
    border: "2px solid {colors.on-primary}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl} 0"
  feature-grid-item:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  feature-grid-item-icon:
    width: 48px
    height: 48px
    rounded: "{rounded.full}"
    backgroundColor: "{colors.primary}"
  testimonial-card:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.base}"
  newsletter-input:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.muted}"
  newsletter-input-focus:
    border: "2px solid {colors.primary}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    width: 44px
    height: 44px
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-total:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.badge-new-bg}"
    textColor: "{colors.badge-new}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-best-seller:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hex-pattern-overlay:
    backgroundColor: "{colors.hex-pattern}"
    opacity: 0.05
    backgroundImage: "url('/hex-pattern.svg')"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.base} 0"
  divider-dark:
    backgroundColor: "{colors.muted}"
    height: 1px
    margin: "{spacing.base} 0"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in `{colors.primary}` (`#d73939`) with white text and `{rounded.sm}` (8px) corners. Uses `{typography.button-md}` — 14px din-2014 in uppercase with 1px letter-spacing — for a technical, precise feel. On hover, shifts to `{colors.primary-hover}` (`#ef4444`); on active, deepens to `{colors.primary-active}` (`#c70000`). Disabled state reduces opacity to 0.5. Height is 48px with 12px/28px padding.

**`button-secondary`** — An outlined variant on a white canvas with `{colors.ink}` text and a 2px solid border. Hover inverts to a solid `{colors.ink}` fill with white text. Shares the same dimensions and typography as `button-primary`. Used for "Learn More" and secondary product actions.

**`button-outline-light`** — Used exclusively on dark backgrounds (hero sections, dark mode). Transparent fill with a 2px white border and white text. Hover state fills solid white with `{colors.ink}` text. Same sizing as primary.

**`button-pill-dark`** — A compact pill-shaped button (`{rounded.full}`) on `{colors.surface-dark}` with white text. Uses `{typography.button-sm}` (12px uppercase). Height is 40px with 10px/24px padding. Used for filter tags, quick-add, and utility actions.

**`button-pill-sale`** — A smaller, urgent pill button in `{colors.badge-sale}` red. Height is 36px with tighter padding. Used for flash sale CTAs and limited-time offers.

### Cards
**`product-card`** — The core product display unit. White background, `{rounded.md}` (12px) corners, subtle box-shadow. Image area uses `{rounded.md}` on top corners only. Contains a badge overlay (sale or new), product title, rating with `{colors.star-rating}` (`#cc6328`), and pricing. Sale prices render in `{colors.primary}`. Hover state elevates shadow. Badges use `{rounded.xs}` (4px) for a crisp, technical look.

**`testimonial-card`** — A warm accent card using `{colors.accent-warm}` (`#dfd5c4`) as background. `{rounded.md}` corners with generous `{spacing.xl}` padding. Body copy in `{typography.body-md}`. Used for customer reviews and social proof sections.

**`feature-grid-item`** — A soft surface card (`{colors.surface-soft}`) with `{rounded.md}` corners and `{spacing.lg}` padding. Includes a circular icon container (48px, `{rounded.full}`, `{colors.primary}` background). Used in feature grids and benefit sections.

### Navigation
**`nav-bar`** — Fixed at 72px height, white background with a subtle bottom border (`{colors.hairline-soft}`). Sticky variant adds a light box-shadow. Links use `{typography.nav-link}` — 13px din-2014 uppercase with 0.8px tracking. Active state uses `{colors.primary}` text; inactive uses `{colors.muted}`. Mobile collapses to a hamburger menu.

**`nav-link-active`** / **`nav-link-inactive`** — Active links display in `{colors.primary}` red; inactive in `{colors.muted}` gray. Both share the same uppercase typography.

### Forms
**`text-input`** — Standard input field with white background, `{rounded.sm}` corners, 48px height, and a `{colors.hairline}` border. Focus state switches to a 2px `{colors.primary}` border. Error state uses `{colors.error}` (`#d12121`). Typography is `{typography.body-md}` (16px din-2014).

**`select-input`** — Same dimensions and styling as `text-input`, used for dropdowns (size, quantity, sort).

**`newsletter-input`** — Dark variant for footer use. Background is `{colors.surface-mid}` (`#2b2b2b`), text is white, border is `{colors.muted}`. Focus state uses `{colors.primary}` border. Paired with `newsletter-submit` button.

**`quantity-selector`** — A compact 44px height control with a border, `{rounded.sm}` corners, and two side buttons on `{colors.surface-soft}`. Used in cart and product pages.

### Badges
**`badge-sale`** — Red badge (`{colors.badge-sale}`) with white text, `{rounded.xs}` corners, 2px/6px padding. Uses `{typography.badge}` (11px uppercase). Applied to discounted products.

**`badge-new`** — Purple-on-dark-purple badge (`{colors.badge-new}` on `{colors.badge-new-bg}`). Same sizing. Used for new arrivals.

**`badge-best-seller`** — Warm accent badge (`{colors.accent-warm}`) with dark text. Same sizing. Used for top-performing products.

### Footer
**`footer`** — Full-width dark section on `{colors.surface-dark}` with `{spacing.section}` vertical padding. Links use `{colors.muted-soft}` (`#aaaaaa`) with hover to white. Headings use `{typography.title-sm}` (14px uppercase). Contains newsletter signup, navigation columns, and legal text.

### Hero
**`hero-section`** — Full-viewport-height section on `{colors.surface-dark}` with white text. Uses `{typography.display-xl}` (48px Canela). Contains two CTAs: primary (`hero-cta`) and secondary outline (`hero-cta-secondary`). Minimum height 500px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to `{typography.display-md}` (28px); buttons become full-width; footer stacks columns; section padding reduces to `{spacing.xl}` |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero maintains two-column layout; section padding at `{spacing.xxl}` |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full height; standard section padding at `{spacing.section}` |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; extended hero with larger type; generous whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons are 40px × 40px, meeting the 44px touch target with padding
- Product card CTAs are 48px tall
- Quantity selector buttons are 44px × 44px
- Nav links have 44px minimum tap area via padding

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product grid reduces from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer navigation columns stack vertically on mobile
- Hero section reduces to single-column layout on mobile
- Feature grids collapse from 3-column to 2-column to single-column
- Accordion-style sections replace tabbed interfaces on mobile
- Search bar collapses to icon-only trigger on mobile, expanding to full-width on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Hover states for secondary and outline buttons could not be fully verified from static extraction; assumed behavior is standard inversion
- Error state styling for forms (iconography, helper text placement) not extracted
- Dark mode palette not present on live site; all dark surfaces are single-theme
- Sub-brand or collection-specific color variations (e.g., Hexclad Hybrid vs. Hexclad Stainless) not captured
- Animation timing curves and transition durations not extracted
- Focus ring styling (outline, offset, color) not present in extracted CSS
- Modal/overlay component styling not available
- Loading state spinners and skeleton screen patterns not extracted
- Dropdown menu (mega menu) styling for nav not fully captured
- Video player component styling not available
- Star rating component exact sizing and spacing not verified
- Hexagonal pattern SVG or CSS implementation details not extracted
- Print stylesheet not analyzed
- Accessibility contrast ratios not verified against extracted colors
