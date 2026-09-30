---
version: alpha
name: "Kosas"
source_url: "https://kosas.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Kosas is a clean color cosmetics brand that lives at the intersection of makeup and skincare, and the palette tells the story. The canvas is a warm off-white, `#f1eee6`, not a clinical bright white — it feels like a linen towel, not a lab coat. Accent colors arrive with intention: a dusty rose `#d33167` for primary CTAs, a deeper berry `#e81f76` for hover states, and a teal `#088f87` that appears in limited-edition packaging and secondary badges. The brand’s typography is anchored on Brown, a rounded, friendly serif that appears in display sizes, paired with Founders Grotesk for body and button text — a mix of warmth and precision. Shadows are soft, cards use `{rounded.lg}` (20px), and buttons are pill-shaped at `{rounded.full}`. The overall mood is elevated but approachable: a makeup brand that trusts its ingredients and its photography, not heavy ornamentation. The muted palette — `#676986`, `#9da1a0`, `#757575` — handles secondary text and hairlines, while `#272d45` serves as the deep ink for headlines. The site uses `#f4f4f6` and `#f8f7f3` as soft surface tones, creating a layered, tactile feel without visual noise.

colors:
  primary: "#d33167"
  primary-active: "#e81f76"
  primary-disabled: "#f4ccd9"
  ink: "#272d45"
  body: "#676986"
  muted: "#9da1a0"
  muted-soft: "#bdbdbd"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#f1eee6"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#088f87"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  badge-hot-pink: "#ff5742"
  star-rating: "#272d45"
  scrim: "#121212"
  canvas-alt: "#eeeec8"
  surface-alt: "#f8f7f3"
  border-strong: "#c8d8e8"

typography:
  display-xl:
    fontFamily: "'Brown', 'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Brown', 'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Brown', 'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Founders Grotesk Mono', 'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Founders Grotesk', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.badge-hot-pink}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas-alt}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
  product-card-image:
    rounded: "{rounded.lg}"
  product-card-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  product-card-badge-hot:
    backgroundColor: "{colors.badge-hot-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  hero-section-alt:
    backgroundColor: "{colors.canvas-alt}"
    textColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  search-bar-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: 16px 20px
  accordion-open:
    backgroundColor: "{colors.surface-soft}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-hot-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-limited:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  color-swatch:
    rounded: "{rounded.full}"
    size: 32px
  color-swatch-selected:
    borderColor: "{colors.ink}"
    borderWidth: 2px
  color-swatch-ring:
    borderColor: "{colors.hairline}"
    borderWidth: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Bag", "Shop Now", and checkout flows. It uses the brand's dusty rose `{colors.primary}` as a solid fill with white text, set in uppercase Founders Grotesk at 15px. The pill shape (`{rounded.full}`) and 48px height give it a friendly, tactile presence. On hover, it shifts to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}`.

**`button-secondary`** — An outlined or ghost variant used for "Learn More" and secondary checkout actions. It inherits the same pill shape and typography but uses a transparent background with `{colors.ink}` text. On hover, a subtle background tint appears. The border is `{colors.hairline}`.

**`button-tertiary-text`** — A text-only button used for "View Details" links and inline actions. It has no background or border, only `{colors.ink}` text in uppercase Founders Grotesk. On hover, the text color shifts to `{colors.primary}`.

**`button-pill-primary`** — A smaller pill button used for filter tags, category links, and quick-add actions. It uses the same primary color but at a smaller 13px uppercase weight and 10px vertical padding.

### Cards
**`product-card`** — The primary product display card, used on collection pages and search results. It has a white background (`{colors.surface-card}`), soft 20px rounded corners (`{rounded.lg}`), and a subtle shadow. The image area uses the same corner radius. Product name, price, and a star rating sit below the image. A badge overlay can appear in the top-left corner.

**`product-card-badge`** — A small pill badge overlaid on product cards, typically used for "New", "Best Seller", or "Clean Beauty" labels. The teal `{colors.accent-teal}` badge signals clean or sustainable attributes, while `{colors.badge-hot-pink}` is reserved for "Sale" or "Limited Edition" urgency.

### Navigation
**`nav-bar`** — The top navigation bar, fixed at 72px height on the warm canvas background. It contains the brand logo, a set of uppercase nav links, a search icon, and a cart icon. On scroll, the background shifts to `{colors.canvas-alt}` for visual separation. The nav links use `{typography.nav-link}` — 14px uppercase Founders Grotesk with 0.3px letter spacing.

### Forms
**`text-input`** — Standard text input used in checkout, account creation, and newsletter signup. It has a warm canvas background, 8px rounded corners (`{rounded.sm}`), and 16px horizontal padding. On focus, a 2px `{colors.primary}` border appears. Error states use `{colors.badge-hot-pink}`.

**`search-bar`** — The site search input, styled as a full pill (`{rounded.full}`) with a white card background. It sits in the nav bar and on the search results page. On focus, a 2px primary border appears. The placeholder text uses `{colors.muted}`.

### Footer
**`footer`** — The site footer, inverted on a deep `{colors.ink}` background with white text. It contains columns of links, social icons, and a newsletter signup. Links use `{colors.muted-soft}` and shift to white on hover. The footer padding matches `{spacing.section}`.

### Badges
**`badge-new`** — A small pill badge in the primary rose color, used to flag new arrivals. **`badge-sale`** uses the hot pink `{colors.badge-hot-pink}` for sale items. **`badge-limited`** uses the teal `{colors.accent-teal}` for limited-edition or clean beauty labels. All badges use 11px uppercase Founders Grotesk Mono.

### Hero
**`hero-section`** — The full-width hero banner on the homepage and landing pages. It uses the warm canvas background with large Brown display type. The `hero-section-alt` variant uses `{colors.canvas-alt}` for visual variety. Hero images are full-bleed with soft overlays.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards stack in 2 columns; hero type reduces to 28px; footer links stack vertically; search bar collapses to icon-only |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 3 columns; hero type at 36px; footer in 2-column grid |
| Desktop | 1128–1440px | Full nav with all links; product cards in 4 columns; hero type at 48px; footer in 4-column grid |
| Wide | > 1440px | Max-width container at 1440px; extra whitespace on sides; product cards may show 5 columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px touch target height.
- Icon buttons (search, cart, hamburger) are at least 44x44px.
- Product card tap targets are the full card area.
- Color swatches are 32px minimum with adequate spacing.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu below 744px.
- The product filter sidebar collapses to a bottom sheet or dropdown on mobile.
- The footer multi-column layout collapses to a single column on mobile.
- Hero content stacks vertically on mobile (image above text).
- Accordion components handle FAQ and product details on all breakpoints.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary button hover states are documented.
- Error styling for forms (validation messages, error icons) was not reliably observed.
- Dark mode is not present on the live site; no dark palette tokens are defined.
- Sub-brand or seasonal color palettes (e.g., holiday collections) are not captured.
- Animation and transition durations (ease-in-out, spring curves) were not extractable.
- Specific shadow values (box-shadow, drop-shadow) were not reliably parsed.
- The "Founders Grotesk Mono" font is referenced in badges but its exact weight and spacing may vary.
- The site uses a Shopify platform; some component structures (cart drawer, checkout) follow Shopify defaults and may differ from the brand's custom design.
