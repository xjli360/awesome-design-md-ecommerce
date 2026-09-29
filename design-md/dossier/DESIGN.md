---
version: alpha
name: "Dossier"
source_url: "https://dossier.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Dossier is a direct-to-consumer fragrance brand that strips away the traditional luxury markup by offering high-quality, Made-in-France perfumes at fair prices. The brand's visual identity is a study in warm, earthy minimalism, anchored by a signature coral-terracotta primary, `#ef776a`, that appears on every primary button, badge, and accent element. This vibrant hue is set against a canvas of `#faf6f0` — a soft, creamy off-white that feels tactile and inviting, not sterile. The typographic voice is built on the Founders Grotesk family, used across weights from Light to Bold, giving the brand a modern, editorial feel that balances approachability with a touch of sophistication. Supporting neutrals like `#212121` for ink, `#43423c` for body text, and `#727272` for muted elements create a clean hierarchy, while a secondary palette of deeper reds (`#b83520`, `#da2a17`, `#e32c18`) and warm beiges (`#cdb087`, `#dcc8ab`, `#ebdfcf`) echo the natural ingredients and artisanal process behind the scents. The design system relies on generous whitespace, soft `{rounded.sm}` corners on cards and inputs, and `{rounded.full}` pill shapes for CTAs and badges, creating a gentle, human-friendly interface. The overall mood is one of quiet confidence — the brand doesn't shout, it invites discovery, much like the layering of notes in a fine fragrance.

colors:
  primary: "#ef776a"
  primary-active: "#e32c18"
  primary-disabled: "#e07a6a"
  ink: "#212121"
  body: "#43423c"
  muted: "#727272"
  muted-soft: "#9ca3af"
  hairline: "#d1d5db"
  hairline-soft: "#e5e7eb"
  canvas: "#faf6f0"
  surface-soft: "#f7f5f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#da2a17"
  accent-red-soft: "#b83520"
  accent-beige: "#cdb087"
  accent-beige-soft: "#dcc8ab"
  accent-beige-light: "#ebdfcf"
  success: "#24c761"
  error: "#c10000"
  link: "#2563eb"
  star-rating: "#212121"
  scrim: "#111827"

typography:
  display-xl:
    fontFamily: "'FoundersGroteskBold', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'FoundersGroteskMedium', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'FoundersGroteskMedium', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'FoundersGroteskRegular', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'FoundersGroteskMedium', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'FoundersGroteskMedium', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'FoundersGroteskRegular', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'FoundersGroteskRegular', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'FoundersGroteskRegular', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'FoundersGroteskRegular', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'FoundersGroteskMedium', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'FoundersGroteskMedium', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'FoundersGroteskMedium', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'FoundersGroteskMedium', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'FoundersGroteskRegular', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'FoundersGroteskMedium', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
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
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: 1px solid "{colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    border: 1px solid "{colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: 1px solid "{colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.error}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-photo:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-new:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-sale:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-best-seller:
    backgroundColor: "{colors.accent-beige}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.canvas}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: 1px solid "{colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    paddingTop: "{spacing.sm}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: 2px solid "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Bag", "Shop Now", and checkout flows. It features a solid `{colors.primary}` fill with white text, full pill rounding (`{rounded.full}`), and the `{typography.button-md}` type style. On hover, it shifts to `{colors.primary-active}` for a subtle state change. The disabled state uses `{colors.primary-disabled}` to visually indicate inactivity while maintaining brand consistency.

**`button-secondary`** — An outlined or ghost alternative for secondary actions like "Learn More" or "View Details". It uses a transparent background with `{colors.ink}` text and a full pill shape. On hover, it may adopt a subtle `{colors.surface-soft}` background to provide feedback without competing with the primary button.

**`button-tertiary-text`** — A text-only button for the least prominent actions, such as "Cancel" or "Skip". It has no background or border, relying solely on `{colors.ink}` text and the `{typography.button-md}` style. Hover state adds a subtle underline or color shift to `{colors.primary}`.

**`button-pill-primary`** — A smaller, compact pill button used for inline actions like "Quick Add" or filter tags. It shares the same `{colors.primary}` fill and `{rounded.full}` shape but uses `{typography.button-sm}` for a tighter fit.

**`button-pill-outline`** — The outlined counterpart to the pill button, used for filter toggles or "Sold Out" indicators. It has a transparent background, `{colors.ink}` text, and a `1px` `{colors.hairline}` border, maintaining the pill silhouette.

### Cards
**`product-card`** — The primary product display unit on collection and search pages. It is a white card (`{colors.surface-card}`) with `{rounded.sm}` corners, containing a square photo area, product title, price, and optional badges. The card has no padding at the container level; internal spacing is handled by child elements. On hover, a subtle shadow or border change may occur to indicate interactivity.

**`product-card-photo`** — The image area within a product card, with a `1:1` aspect ratio and `{rounded.sm}` top corners. The background is `{colors.surface-soft}` to provide a neutral placeholder while images load.

**`product-card-title`** — The product name, set in `{typography.title-sm}` with `{colors.ink}` for high readability.

**`product-card-price`** — The product price, set in `{typography.body-md}` with `{colors.body}` to differentiate it from the title.

**`product-card-badge`** — A small, pill-shaped badge overlaid on the product photo, used for "New", "Sale", or "Best Seller" labels. It uses `{colors.primary}` background with white text and `{typography.badge}` for a compact, uppercase label.

### Badges
**`badge-new`** — A red badge (`{colors.accent-red}`) for newly launched products. It follows the same pill shape and `{typography.badge}` style as the standard product badge but uses a distinct color to draw attention.

**`badge-sale`** — A green badge (`{colors.success}`) for discounted items, signaling value and urgency.

**`badge-best-seller`** — A beige badge (`{colors.accent-beige}`) with dark text (`{colors.ink}`) for top-performing products. This softer color integrates with the brand's earthy palette.

### Navigation
**`top-nav`** — The main site navigation bar, fixed at the top of the viewport. It has a `{colors.canvas}` background, `72px` height, and contains the logo, nav links, and utility icons (search, account, cart). Nav links are set in `{typography.nav-link}` with uppercase styling for a clean, editorial look.

**`nav-link-active`** — The active state for a navigation link, using `{colors.primary}` text color to indicate the current page or section.

**`nav-link-inactive`** — The default state for a navigation link, using `{colors.muted}` text color to de-emphasize non-active pages.

### Forms
**`text-input`** — A standard text input for forms like email signup, address entry, or search filters. It has a white background (`{colors.surface-card}`), `{rounded.sm}` corners, a `1px` `{colors.hairline}` border, and `{typography.body-md}` for the input text. On focus, the border changes to `{colors.primary}` for clear visual feedback.

**`text-input-active`** — The focused state of a text input, with a `{colors.primary}` border to guide the user's attention.

**`text-input-error`** — The error state of a text input, using a `{colors.error}` border to clearly indicate a validation issue.

**`search-bar`** — A specialized input for the site-wide search feature. It has a full pill shape (`{rounded.full}`), a white background, and a `1px` `{colors.hairline}` border. On focus, it adopts a `{colors.primary}` border to match the active input pattern.

**`quantity-selector`** — A compact control for adjusting item quantities in the cart or on the product page. It has a `{colors.surface-soft}` background, `{rounded.sm}` corners, and `40px` height. The plus/minus buttons are transparent and sit flush within the container.

### Footer
**`footer`** — The site footer, which uses a dark `{colors.ink}` background with light `{colors.canvas}` text for strong contrast. It contains links, legal information, and social media icons. Links are set in `{typography.link}` with `{colors.muted-soft}` color, transitioning to `{colors.canvas}` on hover.

**`footer-link`** — A standard footer link with `{colors.muted-soft}` text color.

**`footer-link-hover`** — The hover state for a footer link, transitioning to `{colors.canvas}` for readability against the dark background.

### Accordion
**`accordion`** — A collapsible content panel used for FAQs, product details, or shipping information. It has a `{colors.canvas}` background, `{rounded.sm}` corners, and a `1px` `{colors.hairline-soft}` border. The header is set in `{typography.title-sm}` and the content in `{typography.body-sm}`.

**`accordion-header`** — The clickable header of an accordion item, using `{typography.title-sm}` with `{colors.ink}` text.

**`accordion-content`** — The expandable body of an accordion item, using `{typography.body-sm}` with `{colors.body}` text and top padding for spacing.

### Hero
**`hero-section`** — The primary hero banner on the homepage or collection pages. It uses `{colors.canvas}` as the background and `{typography.display-xl}` for the headline. The section has generous padding (`{spacing.section}` top and bottom) to create a spacious, editorial feel.

**`hero-cta`** — The call-to-action button within the hero section, identical in style to `button-primary` but defined separately for contextual clarity.

### Swatches
**`color-swatch`** — A circular color swatch used on product pages to display available color or scent variants. It is `32px` in diameter with `{rounded.full}` rounding.

**`color-swatch-selected`** — The selected state of a color swatch, which adds a `2px` `{colors.primary}` border to indicate the user's choice.

### Rating
**`rating-stars`** — A star rating component, typically displayed as filled and empty star icons. The filled stars use `{colors.star-rating}` (black) for a clean, high-contrast look. Each star is `16px` in size.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero section reduces padding; search bar moves to a toggle icon; accordions are always expanded by default; font sizes scale down by 2px for display styles. |
| Tablet | 744–1128px | Two-column grid for product cards; top-nav remains visible but may condense; hero section uses medium padding; search bar is a full-width element in the nav; accordions are collapsible. |
| Desktop | 1128–1440px | Three-column grid for product cards; full top-nav with all links visible; hero section uses standard padding; search bar is a prominent pill in the nav; sidebars may appear on product pages. |
| Wide | > 1440px | Max-width container (1440px) centered; product cards may expand to four columns; hero section uses larger imagery; whitespace increases to maintain readability. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of `44px` on mobile to meet accessibility guidelines.
- Icon buttons are at least `40px` in diameter.
- Color swatches are `32px` with `44px` touch area via padding.
- Accordion headers have `44px` minimum height for easy tapping.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu on mobile (< 744px), revealing a full-screen overlay with links and utility icons.
- The search bar collapses to a search icon on mobile, expanding to a full-screen overlay when tapped.
- Product filters collapse into a "Filter" button on mobile, opening a bottom sheet or modal.
- The footer collapses to a single-column layout on mobile, with accordion-style sections for link groups.
- Product image galleries collapse from a row of thumbnails to a swipeable carousel on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links are inferred from common patterns but not explicitly extracted from the live site.
- Error and success states for forms (e.g., validation messages, input borders) are based on standard conventions rather than observed data.
- Dark mode is not supported; all colors assume a light theme.
- Sub-brand or seasonal color palettes (e.g., holiday collections) are not captured.
- The exact `fontSize` and `lineHeight` values for typography tokens are estimated based on common design system scales and the brand's editorial feel; they may differ from the actual implementation.
- The `spacing` scale is a standard 4px/8px system; actual spacing values on the site may vary.
- The `rounded` scale uses standard values; the site may use custom radii for specific components.
- Animation and transition durations (e.g., button hover, accordion expand) are not defined.
- The `fontWeight` values for Founders Grotesk are mapped to standard numeric weights (Light: 300, Regular: 400, Medium: 500, Bold: 700) but the actual font files may use different weight values.
- The `textTransform: uppercase` on `nav-link` and `badge` is inferred from the brand's editorial style but not confirmed from the extracted data.
