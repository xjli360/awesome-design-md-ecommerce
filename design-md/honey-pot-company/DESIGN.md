---
version: alpha
name: "The Honey Pot Company"
source_url: "https://thehoneypot.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A plant-derived feminine care brand that wraps its wellness-first mission in a warm, earthy palette anchored by a deep, almost-black ink (`#252222`) and a soft, creamy canvas (`#fdfbf6`). The brand's signature voltage comes from a vibrant coral-orange (`#da532c`) that appears on primary CTAs, badges, and accent elements, while a secondary teal (`#7bc6b9`) and its lighter wash (`#d7f0e8`) bring a soothing, botanical counterpoint. Pink (`#f7a4d7`) and lavender (`#dccdf1`) accents appear in product-specific contexts, suggesting a playful, inclusive approach to category conventions. Typography leans on a rational display face for headlines and a monospaced Syke Mono for technical or ingredient-focused copy, with a suite of domaine_sans_text weights (italic, light, light italic, regular) providing editorial texture for body and product descriptions. The system uses generous whitespace, soft pill-shaped inputs (`{rounded.full}`), and product cards with gentle rounding (`{rounded.md}` ~12px) to feel approachable and clean — never clinical. The overall mood is confident but gentle, like a trusted friend who happens to be a botanist.

colors:
  primary: "#da532c"
  primary-active: "#c44a26"
  primary-disabled: "#f0b8a0"
  ink: "#252222"
  body: "#231f20"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#d9d9d9"
  canvas: "#fdfbf6"
  surface-soft: "#f7f0e8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#7bc6b9"
  accent-teal-soft: "#d7f0e8"
  accent-pink: "#f7a4d7"
  accent-lavender: "#dccdf1"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  star-rating: "#252222"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Domaine Sans Text', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Domaine Sans Text', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Domaine Sans Text', Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Domaine Sans Text', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Rational Display', 'Domaine Sans Text', Georgia, serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Syke Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  ingredient-label:
    fontFamily: "'Syke Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
  quote:
    fontFamily: "'Domaine Sans Text', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
    fontStyle: italic

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
    padding: 14px 28px
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
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-outline-primary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 26px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
  text-input-focused:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 52px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    border: "2px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-vegan:
    backgroundColor: "{colors.accent-teal-soft}"
    textColor: "{colors.accent-teal}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  ingredient-list:
    typography: "{typography.ingredient-label}"
    color: "{colors.muted}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and key conversion points. Rendered as a full-pill shape in the brand's signature coral-orange (`#da532c`) with white text. On hover, darkens to `#c44a26`; disabled state fades to a soft peach (`#f0b8a0`). The button uses 14px vertical padding and 28px horizontal padding for a comfortable, touch-friendly target.
**`button-secondary`** — An outlined variant with a 2px solid ink border on a cream canvas background. Used for secondary actions like "Learn More" or "View Ingredients". Maintains the same pill shape and typography as primary but with a lighter visual weight.
**`button-tertiary-text`** — A text-only button with no background or border, colored in the brand's primary orange. Used for inline actions like "Read Reviews" or "See Details". Hover state adds an underline.
**`button-outline-primary`** — A bordered variant using the primary orange for both text and a 2px solid stroke. Used for "Shop Now" or promotional CTAs where a secondary button needs more visual presence.

### Cards
**`product-card`** — The standard product display card, used across collection pages and search results. Features a white background with 12px rounded corners (`{rounded.md}`). The product image occupies the top portion with matching top rounding, while title and price sit below with 8px horizontal padding. The card has no border but relies on subtle shadow or spacing for separation. On hover, a slight elevation change or border highlight appears.
**`product-card-title`** — Uses the `title-sm` typography (16px, semibold) in ink. The product name is always a single line, truncated with ellipsis if needed.
**`product-card-price`** — Set in `body-md` (16px, regular) but colored in the primary orange to draw the eye as a key decision point.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on a cream canvas background. Contains the brand logo, primary category links, a search icon, and a cart icon. Links use `nav-link` typography (15px, medium weight, slight letter-spacing). The active link state gains a 2px bottom border in the primary orange.
**`nav-link-active`** — The active navigation state, distinguished by the primary orange text color and a 2px solid underline in the same orange. This creates a clear, warm indicator of the current section.

### Forms
**`text-input`** — Standard text input fields used in checkout, account creation, and newsletter signup. Features a cream background, 8px rounded corners, and a 1px hairline border (`#dedede`). On focus, the border thickens to 2px and switches to the primary orange, providing a clear, accessible focus indicator. Placeholder text uses the muted gray (`#6a6a6a`).
**`search-bar-pill`** — The site-wide search input, styled as a full-pill shape with a 1px hairline border on a cream background. At 52px height, it's slightly shorter than primary buttons but still touch-friendly. On focus, the border becomes 2px solid primary orange. The search icon sits inside the left padding.

### Badges
**`badge-new`** — A small, pill-shaped badge in the brand's teal (`#7bc6b9`) with white text, using the monospaced Syke Mono font in uppercase. Used to flag new product arrivals or limited editions.
**`badge-sale`** — A promotional badge in the primary orange with white text, using the same monospaced uppercase style. Used for discounts, bundles, or sale items.
**`badge-vegan`** — An informational badge in the soft teal wash (`#d7f0e8`) with teal text. Used to highlight plant-based or vegan certifications on product cards and detail pages.

### Footer
**`footer`** — The site footer, inverted on a deep ink (`#252222`) background with cream text. Contains link columns, social icons, and legal text. Links use the `link` typography in white for maximum contrast. The footer padding is generous at 48px vertical and 24px horizontal, creating a grounded, substantial closing section.

### Miscellaneous
**`ingredient-list`** — A technical list of ingredients displayed in the monospaced Syke Mono font at 12px in muted gray. Used on product detail pages to present the full ingredient deck in a clean, readable, and scientifically-toned format.
**`quantity-selector`** — A compact input for adjusting product quantities on the cart or product page. Features a cream background, 8px rounded corners, and a 1px hairline border. Contains minus, number, and plus controls in a horizontal layout.
**`accordion-header`** — Used for collapsible sections on product pages (e.g., "How to Use", "Ingredients", "Shipping"). A simple text header with a bottom hairline separator, using the `title-sm` typography. On click, it expands to reveal the accordion content below.
**`accordion-content`** — The expanded content area below an accordion header, using `body-sm` typography in the body color. Padded with 8px top and 16px bottom for comfortable reading.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to display-md; search bar becomes full-width; footer links stack |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses display-lg; search bar is 60% width; footer uses two-column layout |
| Desktop | 1128–1440px | Full three or four-column product grid; expanded nav with all links; hero uses display-xl; search bar is 40% width; footer uses four-column layout |
| Wide | > 1440px | Max-width container (1440px) centered; extra whitespace on sides; product grid can expand to five columns; hero section uses larger padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Product card tap targets are the entire card surface, not just text links.
- Quantity selector buttons are at least 40px × 40px.
- Accordion headers are at least 48px tall for easy tapping.

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px.
- Product filters collapse to a "Filter" button that opens a slide-out panel on mobile.
- Footer link columns collapse to accordion-style sections below 744px.
- Hero section reduces headline size and stacks CTA buttons vertically on mobile.
- Product image galleries switch from horizontal thumbnails to a single swipeable carousel on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and active states for secondary, tertiary, and outline buttons (color shifts, shadows).
- Error styling for form inputs (border color, error message typography and placement).
- Focus ring styles (color, width, offset) for keyboard accessibility.
- Sub-brand or collection-specific color palettes (e.g., limited editions, seasonal drops).
- Dark mode color overrides for any component.
- Exact shadow values (box-shadow) for cards, modals, and elevated elements.
- Transition durations and easing curves for interactive states.
- Modal, drawer, and overlay component specifications.
- Toast/notification component design (success, error, info variants).
- Loading spinner and skeleton screen specifications.
- Typography scale for mobile (font sizes may reduce below 744px).
- Exact spacing values for product grid gaps and margins.
- Icon library details (custom vs. system, stroke weights, sizes).
