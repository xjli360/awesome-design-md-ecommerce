---
version: alpha
name: "Beast Health"
source_url: "https://thebeast.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Beast Health's design system is a study in industrial minimalism, where a raw, almost utilitarian palette of deep charcoals (#333333, #121212, #232323) and warm off-whites (#f8f3ec, #f0eee3, #fffdfc) creates a canvas that feels both premium and approachable. The brand's signature voltage is a singular, unapologetic orange (#ff5601, #ff5500) that ignites every primary CTA, badge, and accent—a deliberate jolt against the muted greys (#666666, #999999, #63615e). This isn't a sterile kitchen-tool brand; it's a tactile, performance-driven one. Typography runs DM Sans and Sofia Pro, with display sizes that feel substantial but never overwrought, and body text that prioritizes clarity over flourish. The system leans on generous `{rounded.full}` pill shapes for buttons and inputs, while cards and containers use a softer `{rounded.md}` radius, creating a friendly, human interface. The palette also introduces unexpected cool tones—a slate blue (#809cb3), a deep teal (#364748), and a muted gold (#ffd45d)—that appear in product details, ingredient callouts, and secondary badges, hinting at a brand that's as much about culinary science as it is about raw power. The overall feel is one of confident restraint: every element has a job, every color a purpose, and the whitespace is a deliberate breath between the heavy machinery of the kitchen.

colors:
  primary: "#ff5601"
  primary-active: "#e04a00"
  primary-disabled: "#ffd1b3"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cfcfcf"
  hairline-soft: "#dedede"
  canvas: "#fffdfc"
  surface-soft: "#f8f3ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#364748"
  accent-teal-soft: "#9ca4a5"
  accent-blue: "#1990c6"
  accent-blue-soft: "#809cb3"
  accent-gold: "#ffd45d"
  accent-warm-grey: "#63615e"
  accent-warm-grey-soft: "#c9c5bf"
  badge-new: "#ff5601"
  badge-sale: "#1990c6"
  badge-eco: "#364748"
  star-rating: "#ffd45d"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-strong:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  link:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'DM Sans', 'Sofia Pro', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 52px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 52px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 44px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 44px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-field-segment:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: 8px 16px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-photo:
    rounded: "{rounded.md}"
    aspectRatio: "1/1"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption-strong}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 16px 40px
    height: 56px
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  feature-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  feature-card-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  checkbox:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.caption-strong}"
    textTransform: uppercase
  newsletter-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
  tab-indicator:
    backgroundColor: "{colors.primary}"
    height: 3px
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  slider:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
    rounded: "{rounded.full}"
  slider-thumb:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 20px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  modal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-eco:
    backgroundColor: "{colors.badge-eco}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    margin-bottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    margin-bottom: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in the signature Beast Orange (#ff5601) with white text. Uses a `{rounded.full}` pill shape and generous padding (14px 32px) to create a substantial, tactile feel. On hover, it shifts to a deeper `{colors.primary-active}` (#e04a00); when disabled, it fades to `{colors.primary-disabled}` (#ffd1b3). The typography is `{typography.button-md}` (16px, weight 600) with slight letter-spacing for readability.

**`button-secondary`** — A clean, minimal alternative for less prominent actions. Uses a white `{colors.canvas}` background with `{colors.ink}` text, maintaining the same `{rounded.full}` pill shape and 52px height as the primary button. An outline variant (`button-secondary-outline`) uses a transparent background with a 1px solid `{colors.hairline}` border for situations requiring a lighter visual footprint.

**`button-tertiary-text`** — A text-only button for the lightest-weight actions. Uses a transparent background and `{colors.primary}` text, with no border or padding. Ideal for "Learn More" or "Skip" links within cards and modals.

**`button-pill-small`** — A compact, high-impact pill for badges, tags, and inline actions. Uses `{colors.primary}` background with white text, `{typography.button-sm}` (14px, weight 600), and tighter padding (8px 20px) for a 36px height.

### Cards
**`product-card`** — The core product display unit, featuring a white `{colors.canvas}` background with `{rounded.md}` (12px) corners. The photo area maintains a 1:1 aspect ratio with matching corner radius. Contains a `{typography.title-sm}` product name, `{typography.price}` for pricing, and optional `{typography.caption-strong}` rating with `{colors.star-rating}` (#ffd45d) stars. Badges use `{rounded.full}` pills with brand-specific colors (`{colors.badge-new}` for new arrivals, `{colors.badge-sale}` for promotions, `{colors.badge-eco}` for sustainable products).

**`feature-card`** — Used in editorial and feature sections, this card uses a `{colors.surface-soft}` (#f8f3ec) warm off-white background with `{rounded.md}` corners and `{spacing.lg}` padding. An optional icon circle uses `{colors.primary}` background with white iconography, maintaining the brand's signature orange voltage.

### Navigation
**`top-nav`** — A fixed-height (72px) navigation bar with a white `{colors.canvas}` background. Navigation links use `{typography.nav-link}` (14px, weight 500, uppercase with 0.5px letter-spacing) for a clean, editorial feel. The bar remains persistent across all viewports, collapsing secondary links into a hamburger menu on mobile.

**`category-strip`** — A horizontal scrollable strip of category tabs, using `{colors.canvas}` background. Active tabs use `{colors.surface-soft}` background with `{rounded.full}` pills, while inactive tabs remain transparent with `{colors.muted}` text. This pattern is used for product categories, recipe filters, and ingredient tags.

### Forms
**`text-input`** — Standard text input with a white `{colors.canvas}` background, `{rounded.sm}` (8px) corners, and 48px height. On focus, the border shifts to `{colors.primary}` (#ff5601). Error states use the same orange border with orange text for error messages, maintaining brand consistency even in validation.

**`select-input`** — Matches the `text-input` dimensions and styling, with a custom dropdown arrow in `{colors.muted}`. The dropdown menu uses `{colors.canvas}` background with `{rounded.sm}` corners and `{colors.hairline}` dividers between options.

**`checkbox`** — A small (16px) square with `{rounded.xs}` (4px) corners. When checked, the background fills with `{colors.primary}` and displays a white checkmark. The label uses `{typography.body-sm}` for a clean, legible pairing.

### Footer
**`footer-section`** — A dark footer using `{colors.ink}` (#121212) background with white text. Links use `{colors.muted-soft}` (#999999) for a subtle, readable contrast. Section headings use `{typography.caption-strong}` with uppercase transformation for visual hierarchy. The newsletter input uses a `{rounded.full}` pill with `{colors.surface-soft}` background, paired with an orange `{colors.primary}` submit button.

### Miscellaneous
**`accordion-header`** — Used in FAQ and product detail sections. The header uses `{typography.title-sm}` with `{colors.ink}` text and no background. Content uses `{typography.body-sm}` with `{colors.body}` text and `{spacing.base}` bottom padding. A `{colors.hairline}` divider separates each accordion item.

**`tab-bar`** — A horizontal tab system for product details, reviews, and specifications. Active tabs use `{colors.ink}` text with a 3px `{colors.primary}` bottom indicator. Inactive tabs use `{colors.muted}` text. The bar itself has a `{colors.canvas}` background and no border.

**`progress-bar`** — Used for product ratings, subscription status, and loading states. The track uses `{colors.hairline-soft}` (#dedede) with `{rounded.full}` corners and 4px height. The fill uses `{colors.primary}` (#ff5601) with matching radius.

**`tooltip`** — A dark tooltip using `{colors.ink}` background with white text. Uses `{typography.caption}` (12px, weight 400) with `{rounded.sm}` (8px) corners and tight padding (6px 12px). Appears on hover with a subtle fade-in animation.

**`modal-overlay`** — A semi-transparent overlay using `{colors.scrim}` (#121212) at 60% opacity. The modal card uses `{colors.canvas}` background with `{rounded.md}` corners and `{spacing.xl}` padding. Close button uses `{colors.muted}` icon with `{colors.ink}` on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack vertically; hero section reduces to 32px font; category strip becomes horizontally scrollable; footer links collapse into accordion; buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links; hero uses 40px display; category strip shows 4-5 visible tabs; footer uses 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; hero uses 48px display; category strip shows all tabs; footer uses 4-column layout |
| Wide | > 1440px | Max-width container (1440px) with centered content; product grid can expand to 4 columns; hero section uses larger imagery; additional whitespace around all sections |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons use 44px circles to meet touch target requirements
- Product card tap targets are the full card area, not just text links
- Category strip items have 48px minimum height for easy scrolling
- Accordion headers have 48px tap targets
- Checkbox and radio inputs have 44px minimum clickable area (including label)

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Product filters collapse into a modal or bottom sheet on mobile
- Multi-column footers collapse to single-column accordions below 744px
- Product image galleries switch from row to swipeable carousel on mobile
- Tab bars collapse to a horizontal scrollable strip on mobile
- Side-by-side feature sections stack vertically below 744px
- Search bar expands to full width on mobile, collapsing the category strip below it

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons (color shifts, shadow effects) could not be reliably extracted
- Error state styling for select inputs, checkboxes, and radio buttons is not fully documented
- Focus ring styles (color, width, offset) for all interactive elements are missing
- Dark mode color overrides and component variants are not available
- Sub-brand or seasonal palette variations (e.g., holiday, limited edition) are not captured
- Animation timing, easing curves, and transition durations are not specified
- Icon library details (stroke width, sizes, color inheritance) are incomplete
- Typography scale for mobile-specific sizes (e.g., smaller display text) is not fully defined
- Dropdown menu and select option hover/active states are not documented
- Loading spinner and skeleton screen specifications are missing
- Video player controls and overlay styling are not available
- Print stylesheet and accessibility-focused high-contrast mode are not defined
- Micro-interaction details (button press, card lift, ripple effects) are not captured
