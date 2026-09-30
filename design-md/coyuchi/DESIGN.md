---
version: alpha
name: "Coyuchi"
source_url: "https://www.coyuchi.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A tactile, earth-honoring bath and bedding brand that speaks in the quiet language of organic cotton and slow craft. The palette is anchored by a vivid, oceanic blue — `#00bbff` — that appears as a signature accent across CTAs, badges, and product highlights, evoking clean water and crisp linen air. This primary voltage is supported by a deeper navy `#1990c6` and `#136f99` for active and hover states, creating a tonal gradient that feels both aquatic and grounded. The neutral architecture is built on a warm off-white canvas (`#ffffff`), with body text in `#333333` and softer muted tones of `#999999` and `#cccccc` that whisper rather than shout. Hairlines in `#dedede` keep edges soft, while the ink (`#121212`) anchors headlines and navigation with quiet authority. Typography pairs the clean, humanist sans-serif of TT Norms Pro with the editorial warmth of Tiempos Headline and Tiempos Text, creating a rhythm that feels like a slow Sunday morning — generous in whitespace, deliberate in scale. Rounded corners are gentle (`{rounded.sm}` on buttons, `{rounded.md}` on cards) but never pillowy, preserving a sense of refined simplicity. The design system trusts texture — organic cotton, linen, and terry — over decorative flourish, making every surface feel touchable and true.

colors:
  primary: "#00bbff"
  primary-active: "#1990c6"
  primary-disabled: "#cccccc"
  ink: "#121212"
  body: "#333333"
  muted: "#999999"
  muted-soft: "#cccccc"
  hairline: "#dedede"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-strong: "#e8e8e8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-deep: "#136f99"
  accent-light: "#e0f7ff"
  badge-sale: "#00bbff"
  badge-new: "#136f99"
  star-rating: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Tiempos Headline', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Tiempos Headline', Georgia, serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Tiempos Headline', Georgia, serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Tiempos Text', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Tiempos Text', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.15px
  badge:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'TT Norms Pro', 'Work Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 6px
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
  section: 72px

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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 1px solid "{colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid "{colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 19px
    height: 40px
    border: 1px solid "{colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 44px
    width: 44px
    border: 1px solid "{colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: 1px solid "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.sm} 0"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.xs} {spacing.sm} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: absolute
    top: 8px
    left: 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    borderTop: 1px solid "{colors.hairline}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
    padding: "{spacing.xs} 0"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: 1px solid "{colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} 0"
    borderBottom: 1px solid "{colors.hairline-soft}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: 2px solid "{colors.primary}"
    padding: "{spacing.sm} {spacing.md}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.md}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: 1px solid "{colors.hairline}"
    padding: "{spacing.md} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 44px
    padding: "0 {spacing.sm}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: 1px solid "{colors.hairline}"
  size-selector-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: 1px solid "{colors.ink}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: 1px solid "{colors.hairline}"
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: 2px solid "{colors.ink}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-active:
    typography: "{typography.caption}"
    color: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with Coyuchi's signature blue (`{colors.primary}`) and white text. Used for "Add to Bag", "Shop Now", and primary checkout actions. On hover, it deepens to `{colors.primary-active}` (#1990c6), and in disabled state it fades to `{colors.primary-disabled}` (#cccccc) with muted text. The 6px corner radius (`{rounded.sm}`) keeps it approachable without being overly soft.

**`button-secondary`** — A white button with a subtle hairline border (`{colors.hairline}`) and dark ink text. Used for "Learn More", "View Details", and secondary actions alongside primary buttons. Active state adds a darker border and soft background fill (`{colors.surface-soft}`).

**`button-tertiary-text`** — A text-only button in the primary blue, used for inline links like "See all" or "Read reviews". No background or border — pure typographic action.

**`button-pill-primary`** — A fully rounded pill variant of the primary button, used for filter tags, quick-add actions, and mobile navigation items. Smaller padding and font size (`{typography.button-sm}`) keep it compact.

**`button-pill-outline`** — The outlined counterpart to the pill primary, used for unselected filter options or secondary mobile actions. White background with a hairline border.

### Cards
**`product-card`** — The core product display card, a white container with `{rounded.md}` (12px) corners. The product image sits flush to the top with its own rounded top corners, followed by the title in `{typography.title-sm}` and price in `{typography.body-sm}`. Badges (sale, new, sold out) are positioned absolutely over the top-left of the image with `{rounded.xs}` (2px) corners and uppercase micro typography (`{typography.badge}`).

### Navigation
**`top-nav`** — A fixed 72px white bar with a subtle bottom border (`{colors.hairline-soft}`). Navigation links use `{typography.nav-link}` — 14px uppercase with 0.3px letter spacing. Active links are indicated by a 2px blue underline (`{colors.primary}`). The search icon and cart icon sit to the right, using `{icon-button-outline}` for touch targets.

**`category-strip`** — A horizontal scrollable strip of category tabs (e.g., "Bedding", "Bath", "Sale") below the top nav. Tabs are 14px uppercase with muted text by default; the active tab gains a blue underline and dark ink text.

### Forms
**`search-bar`** — A soft gray (`{colors.surface-soft}`) input field with a hairline border and 6px corners. On focus, the background turns white and the border switches to the primary blue. Height is 44px for comfortable touch interaction.

**`newsletter-input`** — A white input field with hairline border, paired with a dark ink submit button (`{newsletter-submit}`). The submit button uses `{typography.button-sm}` and sits flush to the input for a clean, integrated look.

**`quantity-selector`** — A compact horizontal control with minus/plus buttons and a centered numeric value. Soft gray background (`{colors.surface-soft}`) with 6px corners and 44px height.

**`size-selector`** — A selectable pill for product variants (e.g., "Twin", "Queen", "King"). Default state is white with hairline border; selected state inverts to dark ink background with white text.

### Footer
**`footer`** — A soft gray (`{colors.surface-soft}`) section with a top hairline border. Headings use `{typography.title-sm}` in ink, while links use `{typography.link}` (14px regular weight) in body gray. The newsletter signup sits prominently within the footer, with the input and submit button side by side.

### Badges
**`badge-sale`** — Blue filled badge (`{colors.badge-sale}`) with white uppercase text, used to highlight discounted items. 2px corners and 4px/8px padding keep it compact and legible.

**`badge-new`** — Deep navy badge (`{colors.badge-new}`) for new arrivals, same styling as sale badge but with a different color to differentiate.

**`badge-sold-out`** — Gray badge (`{colors.muted-soft}`) with dark ink text for out-of-stock items. Uses the same compact sizing as other badges.

### Accordion
**`accordion`** — Used for product details, shipping information, and FAQ sections. Each item has a title in `{typography.title-sm}` with a bottom hairline border. Content panels use `{typography.body-sm}` in body gray with comfortable padding.

### Color Swatches
**`color-swatch`** — A 32px circular swatch with a subtle hairline border. Selected state adds a 2px dark ink ring. Used on product detail pages for color variant selection.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single column product grid, hamburger menu replaces top nav links, search becomes icon-only, hero banners stack vertically, footer collapses to single column, category strip becomes horizontally scrollable with no active underline |
| Tablet | 744–1128px | Two column product grid, top nav links collapse to "Shop" dropdown, hero banners maintain full width with reduced padding, footer splits into two columns, category strip shows 4-5 visible tabs |
| Desktop | 1128–1440px | Three column product grid, full top nav with all links visible, hero banners at max width with generous padding, footer in four columns, category strip shows all tabs |
| Wide | > 1440px | Four column product grid for large screens, max-width container (1440px) for content, hero banners use full viewport width with centered content, all layouts scale proportionally |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40px or 44px square to meet touch target guidelines
- Product card images are tappable with a minimum 200px height on mobile
- Color swatches are 32px with adequate spacing (12px gap) to prevent mis-taps
- Accordion headers have 48px minimum touch height

### Collapsing Strategy
- Top navigation collapses to hamburger menu at < 744px, with a slide-out drawer for navigation links
- Product grid reduces from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 (desktop) to 2 (tablet) to 1 (mobile)
- Hero banner text and CTA stack vertically on mobile, with reduced padding
- Category strip becomes horizontally scrollable on mobile, hiding overflow tabs
- Search bar collapses to icon-only on mobile, expanding to full-width overlay on tap
- Product detail page layout shifts from side-by-side (desktop) to stacked (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons beyond active/inactive (e.g., subtle background shifts)
- Error styling for form inputs (border color, error message typography, icon placement)
- Focus ring styles for keyboard navigation (color, width, offset)
- Loading states for buttons (spinner integration, disabled opacity)
- Toast/notification component styling (success, error, informational)
- Modal/dialog overlay styling (scrim opacity, close button placement, animation)
- Tooltip component styling (background, arrow, positioning)
- Dropdown menu styling (shadow, z-index, item hover states)
- Pagination component styling (active page indicator, disabled state)
- Breadcrumb separator styling (icon or character, color, spacing)
- Dark mode color overrides (all tokens would need dark canvas equivalents)
- Sub-brand or collection-specific palettes (e.g., limited edition colorways)
- Animation timing and easing curves for transitions and micro-interactions
- Shadow/elevation tokens for cards, modals, and dropdowns
- Icon library specification (stroke width, size variants, color inheritance)
- Grid system details (column count, gutter width, max-width breakpoints)
- Typography scale for mobile (font sizes may reduce at smaller viewports)
