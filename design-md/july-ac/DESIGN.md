---
version: alpha
name: "July AC"
source_url: "https://july.ac"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Warm marigold (#dcc532) punctuates an otherwise near-monochrome interface — an unexpected voltage for a window air conditioner brand, arriving where you'd predict the safe appliance-industry blue. That single accent hue marks primary CTAs, the "customize your unit" configurator highlights, and the sticky cart badge, while the rest of the palette stays disciplined in a tight neutral corridor from near-black (#111111) through mid-gray (#777777) to a stack of barely-differentiated light surfaces (#ececec, #f1f1f1, #f3f3f3). The message is clear: the product itself is the color event (buyers pick from curated panel shades that match their wall paint), so the interface stays silent. Typography runs Roboto at restrained weights — display headings land around 32–40px in weight 700 for product names and configurator step titles, while body copy sits at 16px weight 400 with generous 1.6 line-height that gives specification lists room to breathe. Buttons are low-profile rectangles with `{rounded.sm}` corners (8px), tall enough at 48px to feel substantial without the pill-shaped friendliness of lifestyle brands; the gold fill with dark text (`{colors.on-primary}` = #111111) reads as premium hardware, not playful consumer-tech. Cards hold `{rounded.md}` (12px) corners and float on white against a light canvas (#f1f1f1), separated by hairlines (#e0e0e0) rather than shadows — shadow-free design reinforces the flat, architectural quality of the physical product photography. Section spacing runs generous at 64–80px (`{spacing.section}`), ensuring each product hero and comparison module occupies its own visual room. The overall system favors photographic silence: white fields, thin dividers, and that single marigold signal pulling attention to the next action.

colors:
  primary: "#dcc532"
  primary-active: "#c4af1e"
  primary-disabled: "#eee299"
  ink: "#111111"
  body: "#222222"
  muted: "#777777"
  muted-soft: "#444444"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  surface-alt: "#f1f1f1"
  on-primary: "#111111"
  on-dark: "#ffffff"
  accent-green: "#7a9c59"
  accent-red: "#d63638"
  link: "#222222"
  link-hover: "#111111"

typography:
  display-xl:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-md:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  spec-label:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.6px
    textTransform: uppercase
  price:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  configurator-step:
    fontFamily: "Roboto, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px

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
    border: 1px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 16px
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    shadow: 0 1px 4px rgba(0,0,0,0.06)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
  product-card-hover:
    border: 1px solid {colors.hairline}
    shadow: 0 4px 16px rgba(0,0,0,0.06)
  product-image-container:
    backgroundColor: "{colors.surface-alt}"
    rounded: "{rounded.md}"
    aspectRatio: 4 / 3
    padding: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 560px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 36px
    height: 52px
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.configurator-step}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
  configurator-option:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.hairline-soft}
  configurator-option-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 2px solid {colors.primary}
  color-swatch:
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: 2px solid {colors.hairline}
  color-swatch-active:
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: 2px solid {colors.primary}
    shadow: 0 0 0 2px {colors.primary}
  spec-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  spec-row-label:
    textColor: "{colors.muted}"
    typography: "{typography.spec-label}"
  badge-energy:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: 1px solid {colors.hairline}
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
    border: 1px solid {colors.hairline-soft}
    borderFocus: 1px solid {colors.ink}
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  price-compare:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textDecoration: line-through
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
---

## Components

### Buttons

**`button-primary`** — Marigold-gold (#dcc532) fill with dark text (#111111), 8px radius, 48px height. The dark-on-gold combination reads as hardware premium rather than playful — closer to a brushed-brass appliance badge than a candy-colored consumer CTA. On hover/active, the gold deepens to #c4af1e. Disabled state washes out to a pale lemon (#eee299) with muted text, signaling unavailability without introducing a new hue.

**`button-secondary`** — White fill with 1px black border, dark text. On hover the entire button inverts to solid black with white text, providing a decisive binary toggle. Same 48px height and 8px radius as primary. Used for "Learn More," "Compare Units," and secondary actions that shouldn't compete with the gold configurator CTA.

**`button-ghost`** — Transparent background with underlined dark text. No border, no fill. Reserved for tertiary actions like "View all specs" or inline text links that need button-level tap targets without visual weight.

### Navigation

**`nav-bar`** — 72px-tall white bar with a single-pixel bottom border in `{colors.hairline-soft}` (#eeeeee). Logo left-aligned, navigation links ("Products," "How It Works," "Design Yours," "Support") center or right in `{typography.nav-link}` (14px, weight 500). On scroll, the border drops away and a minimal shadow (0 1px 4px rgba(0,0,0,0.06)) appears. Cart icon at right shows a gold dot badge when items are present.

**`search-bar`** — Pill-shaped (`{rounded.full}`) input with light gray fill (#f3f3f3) and near-invisible border. On focus, border darkens to `{colors.ink}`. Placeholder reads "Search products, specs, or support..." in muted gray. Positioned inside nav on desktop, slides down as overlay on mobile.

### Product Display

**`product-card`** — White card with 12px radius and a thin (#eeeeee) border. Product image sits in a 4:3 gray container (#f1f1f1) with internal padding so the unit floats on a neutral field. Below: product name in `{typography.title-sm}`, BTU rating in `{typography.caption}` muted, and price in `{typography.price}` (22px bold). On hover, border strengthens to #e0e0e0 and a subtle lift shadow appears.

**`product-image-container`** — Light gray background (#f1f1f1), 12px radius matching the card. The AC unit is photographed at a three-quarter angle against this neutral field, letting the product's panel color (the customer's custom choice) dominate. Consistent 24px internal padding regardless of unit dimensions.

**`color-swatch`** — 40px circles representing available panel finishes. Larger than typical e-commerce swatches because color selection is the brand's core value proposition. Inactive swatches carry a 2px #e0e0e0 border; active selection receives a 2px gold border plus a 2px gold ring offset (box-shadow). Swatch colors represent physical panel options — matte terracotta, sage, cream, midnight, blush.

### Configurator

**`configurator-panel`** — White panel with 12px radius and hairline border, containing a stepped flow: (1) Choose model/size, (2) Select panel color, (3) Pick side-panel trim, (4) Review. Step titles use `{typography.configurator-step}` (20px, weight 600). The panel is the centerpiece page on the site — all other pages funnel toward it.

**`configurator-option`** — Light gray (#f3f3f3) rounded rectangle representing each selectable option (size, color, trim). On selection, background flips to white with a 2px gold border, creating clear active-state hierarchy. Options contain a small product thumbnail, name, and price delta.

### Pricing

**`price-display`** — Bold 22px in pure dark (#111111). No currency-symbol separation tricks; reads as a single confident number. When a promotional comparison price exists, the original appears in 14px muted with line-through above the current price.

### Specifications

**`spec-row`** — Label/value pairs separated by hairline-soft borders. Labels use uppercase 11px weight-700 in muted gray (BTU RATING, NOISE LEVEL, DIMENSIONS, ENERGY STAR). Values in `{typography.body-sm}` dark. No alternating backgrounds — pure white rows with generous 12px vertical padding for scanability.

### Badges

**`badge-energy`** — Green (#7a9c59) rectangle with 4px radius, white bold caption text. Displays "ENERGY STAR" or efficiency tier. Positioned at top-left of product card overlapping the image container.

**`badge-sale`** — Red (#d63638) rectangle, same geometry. Used for clearance or seasonal promotions. Never paired with badge-energy on the same card — energy efficiency is the persistent story, sale is the interrupt.

### Hero & Marketing

**`hero-banner`** — Full-width section with light gray (#f1f1f1) background rather than a dramatic dark treatment. The product photograph — a window AC unit installed in a styled living space — is the hero. Headline in `{typography.display-xl}` (40px, weight 700) left-aligned. Gold CTA button sits below with extra vertical height (52px) and wider padding for emphasis. Minimum height 560px ensures the lifestyle imagery establishes context.

### Comparison

**`comparison-table`** — White panel with 12px radius and hairline border. Columns for 2–3 product models side by side, with spec rows aligning horizontally. Header row shows product thumbnails and names. Best-value column receives a subtle gold top-border accent (2px). Used on category pages to help buyers choose between BTU tiers.

### Footer

**`footer`** — Dark background (#111111) full-width. Four columns: Products, Design Yours, Support, Company. Headings in `{typography.title-sm}` white, links in `{typography.body-sm}` at 0.7 opacity. Newsletter signup field mirrors `search-bar` styling but with white border on dark. Bottom bar: legal links, copyright, social icons.

### Breadcrumb

**`breadcrumb`** — `{typography.caption}` in muted gray with forward-slash separators. Current page in `{colors.ink}` unlinked. Positioned below nav with `{spacing.sm}` vertical margin.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero reduces to 400px min-height with stacked headline/CTA; configurator steps become vertical accordion; comparison table scrolls horizontally with sticky first column; color swatches shrink to 32px |
| Tablet | 744–1128px | Two-column product grid; nav links visible but abbreviated; hero headline drops to `{typography.display-md}` (32px); configurator panel remains full-width but options reflow to 2-column grid; footer collapses to 2-column |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; configurator shows stepped sidebar + main panel layout; comparison table fits 3 products inline; hero at full 560px height with text overlay on left third |
| Wide | > 1440px | Content max-width 1440px centered; product grid can extend to 4 columns in catalog view; section spacing increases to 80px; hero imagery scales with object-fit cover; configurator gains extra whitespace between options |

### Touch Targets

- All buttons maintain 48px minimum touch target height on mobile
- Color swatches carry transparent padding to ensure 44×44px tap zone even at 32px visual size
- Nav hamburger icon padded to 48×48px
- Product cards are fully tappable on mobile (anchor wraps entire card)
- Configurator options maintain 48px minimum height with 12px gap between options
- Spec rows gain 4px extra vertical padding on touch devices

### Collapsing Strategy

- Desktop horizontal nav → mobile hamburger drawer sliding from left with full-height overlay
- Configurator stepped sidebar → vertical accordion with one step visible at a time
- Comparison table columns → horizontally scrollable with fade-edge indicators on both sides
- Footer 4-column grid → stacked accordion sections with chevron indicators
- Product grid reflows 3→2→1 without internal card layout changes
- Hero text + image side-by-side → stacked with image above, text below on mobile
- Search bar in nav → expandable overlay triggered by search icon tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Page title extracted ("Socolive - Xem tructiepbongda tại Socolive TV hôm nay") indicates the scrape did not reach authentic July AC site content — possible redirect, anti-bot protection, or DNS issue. All color and font data should be treated as low-confidence.
- Many extracted colors (#00d084, #0693e3, #667eea, #764ba2, #007cba, etc.) match WordPress Gutenberg block-editor defaults, suggesting the scrape hit a CMS admin page or unrelated WordPress site rather than the storefront.
- Font families extracted (Dancing Script, Georgia, fl-icons) are unlikely matches for a minimalist appliance brand; Roboto was selected as the most plausible option from the list but may not reflect the actual brand typeface.
- July AC's actual custom webfont (if any) could not be determined — the brand may use a proprietary or licensed face loaded via JavaScript.
- #dcc532 (gold) was chosen as primary because it is the most distinctive non-framework color in the extraction, but it may belong to the wrong site entirely. July AC's actual brand accent is unverified.
- Exact border-radius values, box-shadow definitions, and spacing scale are estimated from the brand's stated minimalist positioning rather than measured CSS.
- Configurator component structure is inferred from product positioning ("Aesthetic-focused customizable AC") rather than observed UI.
- Motion and animation tokens (transitions, loading states, micro-interactions) entirely unknown.
- Icon system and illustration style not captured.
- Actual Shopify theme (Dawn variant, custom, etc.) could not be identified.
