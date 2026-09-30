---
version: alpha
name: "Barefoot Books"
source_url: "https://www.barefootbooks.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A children's bookstore that wears its global, story-first soul on its sleeve through a high-voltage primary of #e53624 — a stop-sign red that reads as warmth and urgency, not danger — and a secondary pulse of #003399, a deep trusty blue that grounds every navigation bar and footer. The palette is deliberately un-muted: #98d108 (lime), #33cccc (teal), #f58229 (orange), and #785ba7 (violet) appear as badge fills, age-category tags, and illustrated-element accents, giving the site the feel of a picture-book spread where every page turn reveals a new color. The canvas is #f9f9f9 rather than pure white, softening the reading experience, while #efefef and #dadada provide hairline and surface-soft tones that keep the layout airy. Typography runs Lora for display and body — a serif with calligraphic warmth that signals "read aloud" rather than "scan quickly" — and Roboto for UI labels and buttons, creating a deliberate tension between storybook elegance and functional clarity. Buttons use {rounded.full} pill shapes, softening the intensity of the red primary, while product cards use {rounded.md} to feel approachable without being childish. The search bar, category filters, and age-group badges all sit on {rounded.full} or {rounded.sm} containers, making every interactive element feel tactile and safe for small hands. The overall mood is generous, slightly handmade, and unafraid of color — a digital space that mirrors the physical bookstore's wooden shelves, woven rugs, and open story-time circle.

colors:
  primary: "#e53624"
  primary-active: "#c92e1e"
  primary-disabled: "#f3a39c"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#959595"
  hairline: "#dadada"
  hairline-soft: "#eeeeee"
  canvas: "#f9f9f9"
  surface-soft: "#efefef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-lime: "#98d108"
  accent-teal: "#33cccc"
  accent-orange: "#f58229"
  accent-violet: "#785ba7"
  accent-marigold: "#ffdf66"
  accent-coral: "#f9eae7"
  accent-rose: "#f3d7d2"
  star-rating: "#ff9635"
  badge-new: "#e03626"
  badge-sale: "#ff8400"
  footer-bg: "#003399"
  on-footer: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Lora', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0
  title-md:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0.2px
    textTransform: uppercase
  body-lg:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-md:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.2px
  link:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.30
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 30px
    height: 48px
  button-pill-accent:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 52px
  search-bar-icon:
    color: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    color: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-author:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    padding: "0 {spacing.base}"
  product-card-price:
    typography: "{typography.title-sm}"
    color: "{colors.primary}"
    padding: "{spacing.sm} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    position: "top-left"
  age-badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  age-badge-0-3:
    backgroundColor: "{colors.accent-teal}"
  age-badge-3-7:
    backgroundColor: "{colors.accent-lime}"
  age-badge-7-11:
    backgroundColor: "{colors.accent-orange}"
  age-badge-11-plus:
    backgroundColor: "{colors.accent-violet}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  hero-section:
    backgroundColor: "{colors.accent-coral}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-lg}"
    color: "{colors.body}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-footer}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.on-footer}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-footer}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button in the brand's signature red (#e53624). Used for "Add to Cart," "Shop Now," and primary checkout actions. On hover, it shifts to `{colors.primary-active}` (#c92e1e) for a subtle darkening effect. The disabled state uses `{colors.primary-disabled}` (#f3a39c) with reduced opacity, ensuring users can still perceive the button's presence without interactivity.

**`button-secondary`** — An outlined or filled white button with red text, used for secondary actions like "Learn More" or "View Details." The outline variant (`button-secondary-outline`) uses a 2px solid border in `{colors.primary}` and transparent background, while the filled variant uses `{colors.canvas}` background. Both maintain the full pill shape and 48px height for consistency with the primary button.

**`button-pill-accent`** — A smaller, accent-colored pill button used for promotional banners, newsletter signups, or age-group-specific calls. Uses `{colors.accent-teal}` (#33cccc) as its primary background, creating a friendly, non-red alternative for less urgent actions. Height is 40px with tighter padding.

### Badges & Tags
**`product-card-badge`** — A small, marigold-yellow (#ffdf66) badge positioned at the top-left corner of product cards. Uses uppercase Roboto at 11px with 0.5px letter-spacing. Used to denote "Award Winner," "Staff Pick," or "New Arrival" status. The badge sits on a slightly rounded rectangle (`{rounded.sm}`) with 4px/8px padding.

**`age-badge`** — A pill-shaped badge indicating the recommended age range for a book. The base color is `{colors.accent-lime}` (#98d108) for the 3-7 age group, with distinct colors for other ranges: teal (#33cccc) for 0-3, orange (#f58229) for 7-11, and violet (#785ba7) for 11+. Each badge uses uppercase Roboto at 11px with tight tracking, ensuring readability at small sizes.

**`badge-new`** and **`badge-sale`** — Two additional badge variants for promotional labeling. `badge-new` uses a deep red (#e03626) for "New" indicators, while `badge-sale` uses a bright orange (#ff8400) for discount markers. Both follow the same typography and rounded-rectangle shape as `product-card-badge`.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 72px height on a `{colors.canvas}` (#f9f9f9) background. Contains the brand logo, primary navigation links (Books, Gifts, About, Blog), a search icon, and a cart icon. Links use uppercase Roboto at 15px with 0.3px letter-spacing. On scroll, a subtle box-shadow (`0 2px 8px rgba(0,0,0,0.08)`) appears to separate the nav from content.

**`nav-link`** — Individual navigation links with 8px/16px padding. The active state is indicated by a 2px bottom border in `{colors.primary}` and red text color. Inactive links remain in `{colors.ink}` (#1a1a1a). Hover state adds a light background tint from `{colors.surface-soft}`.

**`category-pill`** — Filter pills used in the category strip below the hero section. Each pill is a fully rounded button in `{colors.surface-soft}` (#efefef) with dark body text. The active state fills with `{colors.primary}` and white text, creating a clear visual distinction. Used for filtering by category (Adventure, Folktales, Nature, etc.) or by age group.

### Cards
**`product-card`** — The primary content card for displaying books. A white (`{colors.surface-card}`) background with `{rounded.md}` (12px) corners. The card image occupies the top portion with rounded top corners only, creating a natural visual hierarchy. Below the image, the title uses `{typography.title-md}` (Lora 18px, semibold), the author uses `{typography.body-sm}` (Roboto 14px, muted gray), and the price uses `{typography.title-sm}` (Roboto 16px, uppercase, in primary red). Padding is 16px on sides, with 8px between elements.

**`hero-section`** — A full-width hero area with a coral/pink background (`{colors.accent-coral}` #f9eae7). Contains a large Lora heading (`{typography.display-xl}` at 36px) and a body-Lora subheading at 18px. Padding is 64px on top/bottom and 32px on sides. The hero may include an illustration or photograph on the right side, with the text block on the left.

### Forms & Inputs
**`text-input`** — Standard text input fields used in search, newsletter signup, and checkout forms. A white background (`{colors.surface-card}`) with `{rounded.sm}` (8px) corners and 12px/16px padding. On focus, the border changes to `{colors.primary}` (#e53624) with a 2px stroke. Height is 48px for consistency with buttons.

**`search-bar`** — A dedicated search input with a pill shape (`{rounded.full}`) and 52px height. Uses a white background with 12px/24px padding. A search icon in `{colors.muted}` (#666666) sits on the left side. On focus, the border transitions to `{colors.primary}`. The search bar may include a subtle placeholder text in `{colors.muted-soft}`.

### Footer
**`footer`** — A deep blue footer section on `{colors.footer-bg}` (#003399) with white text. Contains four columns: About Us, Customer Service, Connect, and a Newsletter signup. Links are in white at 85% opacity with Lora 16px. Column headings use uppercase Roboto at 16px with 700 weight. Padding is 64px on top/bottom and 32px on sides. The footer includes a copyright bar at the bottom with reduced opacity.

### Star Rating
**`star-rating`** — A 5-star rating display using orange (#ff9635) stars at 16px. Used on product cards and review sections. Stars are filled or empty based on the rating value, with half-star support. The component sits between the author and price on product cards.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text centered; category pills wrap to 2 columns; footer stacks to single column |
| Tablet | 744–1128px | 2-column product grid; nav links visible but condensed; hero maintains side-by-side layout; category pills in a horizontal scrollable strip; footer in 2 columns |
| Desktop | 1128–1440px | 3-column product grid; full nav bar with all links; hero with text left, image right; category pills fully visible; footer in 4 columns |
| Wide | > 1440px | 4-column product grid; max-width container (1440px) centered; hero content max-width 1200px; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, pills) have a minimum height of 44px and width of 44px for touch accessibility
- Category pills and age badges are at least 40px tall with 20px horizontal padding
- Search bar is 52px tall for easy thumb access
- Nav links have 48px touch areas (8px padding + 32px text height)
- Product card images are tappable with a minimum 120px height on mobile

### Collapsing Strategy
- On mobile, the top navigation collapses to a hamburger menu with a slide-out drawer; the brand logo remains centered
- The category filter strip becomes horizontally scrollable with snap points on mobile, hiding overflow pills
- Product cards collapse from a 3-column grid to a single column on mobile, with full-width images
- The hero section reduces padding from 64px to 32px on mobile, and the image may stack below the text
- The footer collapses from 4 columns to 1 column on mobile, with accordion-style expandable sections for each category
- Age badges on product cards may be hidden on mobile to save space, with age info shown in the product detail view

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted; the active states provided are inferred from common patterns
- Error styling for form inputs (validation errors, required field indicators) was not visible in the extracted data
- Dark mode is not supported by the current site; no dark-mode tokens are defined
- The exact font weights for Lora (400, 600, 700) and Roboto (400, 600, 700) are inferred from common usage; the site may use additional weights
- Sub-brand or seasonal color palettes (e.g., holiday themes, special collections) were not captured
- The checkout flow colors may include Shopify Pay, Klarna, or Afterpay widget colors that were not filtered from the extracted hex list; the palette focuses on the brand's own UI
- Animation durations, easing curves, and transition properties were not extractable
- The exact spacing values for component padding and margins are estimated based on common patterns; the site may use a different spacing scale
- Accessibility contrast ratios for text on colored backgrounds (e.g., white text on #e53624) should be verified against WCAG standards
- The extracted hex list includes #cfcfcf, #147378, #f98b25, and #ffdf66 which may be used in illustrations or photography rather than UI elements; they are included as accent possibilities but may not be active design tokens
