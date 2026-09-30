---
version: alpha
name: "Act + Acre"
source_url: "https://actandacre.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Act + Acre is a haircare brand that redefines scalp wellness through a sophisticated, nature-rooted aesthetic. The brand’s palette is anchored by a serene primary of `#557b97` — a muted slate-blue that evokes calm and clinical precision — paired with a soft, almost dusty secondary of `#aadddd` and warm neutrals like `#ccc3ba` and `#ebe0d5`. This is not a loud, trend-driven beauty brand; it’s a quiet authority. The ink (`#222222`) and body (`#414041`) typography sits on a canvas of `#f6f6f6` or `#fffefb`, with surfaces softened by `#f5f5f5` and `#f3f0ed`. Accents of `#3a79a9` and `#094a6e` add depth, while `#7a9e55` introduces a subtle botanical note. The typography relies on UntitledSans — a clean, modern sans-serif — in medium and regular weights, with ArialBold as a fallback for emphasis. Rounded corners are generous but not pill-like: `{rounded.sm}` (8px) for buttons, `{rounded.md}` (12px) for cards, and `{rounded.full}` (9999px) for badges and avatars. The overall feel is editorial, spa-like, and intentional — every element breathes, with generous spacing (`{spacing.lg}` 24px, `{spacing.xxl}` 48px) and a restrained use of color that lets product photography and clean typography lead. The brand’s signature move is the use of `{colors.primary}` as a subtle but consistent anchor across CTAs, borders, and hover states, creating a cohesive, trustworthy experience.

colors:
  primary: "#557b97"
  primary-active: "#094a6e"
  primary-disabled: "#99b9c0"
  ink: "#222222"
  body: "#414041"
  muted: "#6b6d76"
  muted-soft: "#777777"
  hairline: "#cccccc"
  hairline-soft: "#d7d7d7"
  canvas: "#f6f6f6"
  surface-soft: "#f5f5f5"
  surface-card: "#fffefb"
  on-primary: "#ffffff"
  accent-teal: "#aadddd"
  accent-warm: "#ccc3ba"
  accent-rose: "#ebe0d5"
  accent-forest: "#7a9e55"
  accent-deep-blue: "#094a6e"
  accent-bright-blue: "#3a79a9"
  accent-error: "#ff003b"
  accent-warm-dark: "#3a1d00"
  accent-stone: "#d2b69b"
  accent-charcoal: "#647565"

typography:
  display-xl:
    fontFamily: "'UntitledSans-Medium', 'ArialBold', helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'UntitledSans-Medium', 'ArialBold', helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'UntitledSans-Medium', 'ArialBold', helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'UntitledSans-Medium', 'ArialBold', helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'UntitledSans-Regular', helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'UntitledSans-Regular', helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'UntitledSans-Regular', helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'UntitledSans-Regular', helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'UntitledSans-Medium', 'ArialBold', helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'UntitledSans-Medium', 'ArialBold', helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'UntitledSans-Regular', helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'UntitledSans-Medium', 'ArialBold', helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  badge:
    fontFamily: "'UntitledSans-Medium', 'ArialBold', helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    padding: 12px 24px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 80px 24px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    borderColor: "{colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 24px
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 16px 24px
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  rating-stars:
    color: "{colors.accent-warm-dark}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand’s signature slate-blue (`{colors.primary}`) on a white label. On hover, it deepens to `{colors.primary-active}` (`#094a6e`). The disabled state uses `{colors.primary-disabled}` (`#99b9c0`). All states share `{rounded.sm}` (8px) and `{typography.button-md}` for a clean, professional look.

**`button-secondary`** — An outlined or ghost-style button on a white canvas (`{colors.canvas}`) with ink text. Ideal for secondary actions like “Learn More” or “Add to Wishlist.” Hover state may use a subtle background tint of `{colors.surface-soft}`.

**`button-tertiary-text`** — A text-only button with no background, using `{colors.primary}` for the label. Used for inline actions like “View Details” or “Cancel.” Hover state may underline the text.

**`button-pill`** — A compact, fully rounded (`{rounded.full}`) button for badges, tags, or small CTAs. Uses `{typography.button-sm}` and tight padding for use in product cards or category strips.

### Cards
**`product-card`** — The primary container for product listings. Uses a white surface (`{colors.surface-card}`) with `{rounded.md}` (12px) and 16px padding. The product image sits inside with `{rounded.sm}` (8px). Text uses `{typography.body-sm}` for descriptions and `{typography.title-sm}` for product names. A subtle shadow or border may be applied on hover.

**`product-badge`** — A small, pill-shaped badge using `{colors.accent-teal}` (`#aadddd`) background and ink text. Used for labels like “New,” “Best Seller,” or “Limited Edition.” Uses `{typography.badge}` and `{rounded.full}`.

### Navigation
**`nav-bar`** — The top-level site navigation, 72px tall, with a light canvas background (`{colors.canvas}`). Links use `{typography.nav-link}` (14px, medium weight, 0.5px letter-spacing). Active links switch to `{colors.primary}`. The bar may include a logo, menu items, and a search icon.

**`nav-link-active`** — The active state for navigation links, using `{colors.primary}` for text color. No background change, maintaining a clean, minimal look.

### Forms
**`text-input`** — Standard text input fields for forms (e.g., email signup, search). Uses a white surface (`{colors.surface-card}`), `{rounded.sm}`, and a `{colors.hairline}` border. On focus, the border switches to `{colors.primary}`. Height is 48px with 12px/16px padding. Typography is `{typography.body-md}`.

### Hero
**`hero-section`** — The primary hero banner, often used on landing pages. Background is `{colors.surface-soft}` (`#f5f5f5`) with generous padding (80px top/bottom, 24px sides). Headline uses `{typography.display-xl}` (36px, medium weight). May include a subheadline using `{typography.body-md}` and a `{button-primary}` CTA.

### Footer
**`footer-section`** — The site footer, using a dark ink background (`{colors.ink}`) with white text. Links use `{colors.muted-soft}` (`#777777`) and `{typography.link}`. Padding is 48px top/bottom. May include columns for navigation, social links, and a newsletter signup.

### Accordion
**`accordion-header`** — Used for FAQ or product details. Background is `{colors.surface-soft}` with `{rounded.sm}` and `{typography.title-sm}`. Padding is 16px/24px. On click, it expands to reveal `{accordion-content}`.

**`accordion-content`** — The expanded content area, using `{colors.surface-card}` and `{typography.body-sm}`. Padding matches the header.

### Tabs
**`tab-active`** — The active tab in a tabbed interface (e.g., product categories). Uses `{colors.primary}` background with white text, `{rounded.sm}`, and `{typography.button-sm}`.

**`tab-inactive`** — Inactive tabs use `{colors.surface-soft}` background with `{colors.muted}` text. Same typography and rounding as active tabs.

### Miscellaneous
**`icon-button`** — A circular icon button (e.g., for search, cart, or social icons). Uses `{colors.surface-soft}` background, `{rounded.full}`, and 40px height/width.

**`divider`** — A thin horizontal line using `{colors.hairline-soft}` (`#d7d7d7`), 1px height. Used to separate sections or list items.

**`rating-stars`** — Star rating indicators, using `{colors.accent-warm-dark}` (`#3a1d00`) for filled stars. Typically 5 stars, with half-star support.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; hero padding reduces to 48px 16px; product cards stack vertically; accordions become full-width; buttons become full-width; typography scales down (display-xl to 28px, display-lg to 24px). |
| Tablet | 744–1128px | Two-column grid for product cards; nav-bar remains visible but may shrink to 64px; hero padding at 64px 24px; search bar remains visible; footer columns reduce to 2. |
| Desktop | 1128–1440px | Three-column grid for product cards; full nav-bar with all links; hero at full padding; standard spacing and typography. |
| Wide | > 1440px | Max-width container (1440px) centered; increased whitespace; hero may have larger imagery; product cards may have 4-column grid. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Icon buttons are 40x40px, with 2px padding for visual clarity.
- Accordion headers are 48px tall for easy tapping.
- Tab items have 8px padding on each side, with a minimum width of 80px.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu, with a slide-out drawer for links.
- The product category strip collapses into a horizontal scrollable row with snap points.
- Footer columns collapse from 4 to 2 on tablet, and to a single column on mobile.
- Hero sections may collapse to a single image with text overlay on mobile.
- Search bars may collapse to an icon-only button on mobile, expanding on tap.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links beyond primary/active/disabled are not fully extracted (e.g., subtle background tint for secondary buttons, underline for tertiary links).
- Error styling for form inputs (e.g., red border, error message typography) is not captured.
- Sub-brand or seasonal color palettes (e.g., holiday, limited edition) are not defined.
- Dark mode or high-contrast mode tokens are absent.
- Specific font weights for UntitledSans (e.g., 300, 700) are not confirmed; only medium (500) and regular (400) are present.
- Drop shadow values (e.g., for cards, modals) are not extracted.
- Animation and transition timing (e.g., hover fade, accordion slide) are not specified.
- Accessibility tokens (e.g., focus ring color, outline width) are missing.
- Iconography style (e.g., stroke width, fill vs. outline) is not defined.
- Specific spacing for grid layouts (e.g., column gap, row gap) is not extracted.
- Modal, tooltip, and popover component tokens are absent.
- Loading state (e.g., spinner, skeleton) tokens are not captured.
