---
version: alpha
name: "Kitchen Arts & Letters"
source_url: "https://www.kitchenartsandletters.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A specialty bookstore in New York City since 1983, Kitchen Arts & Letters lives in a deep-navy world anchored by `#00008f` — the theme-color meta tag and the most distinctive extracted hex — a color that reads as learned, serious, and slightly old-world, like the spine of a well-bound cookbook. The brand's second voltage is a warm, urgent red (`#d12328`) used for CTAs, sale badges, and the logo mark, creating a tension between scholarly navy and appetite-driven crimson. The canvas is a soft off-white (`#f0f0f0`) rather than pure white, giving the page a paper-stock feel that matches the bookstore's physical inventory of rare and out-of-print food titles. Typography leans on Archivo for headings — a geometric sans-serif with sharp apertures that feels editorial — and Baskerville for body text, a serif that carries the weight of printed recipe collections and culinary memoirs. The extracted font stack includes Libre Franklin and Times, suggesting a layered approach: Archivo for display, Baskerville for long-form reading, Libre Franklin for navigation and metadata. The site uses `{rounded.none}` throughout — no pill buttons, no rounded cards, no softened corners — a deliberate choice that signals seriousness and trustworthiness over friendliness. Every interaction feels like turning a page in a rare-book room. The red (`{colors.primary}`) appears only in high-signal moments: the add-to-cart button, the sale badge, the newsletter signup. The navy (`{colors.ink}`) dominates headers, footer backgrounds, and the top nav, creating a strong vertical hierarchy. The extracted palette includes a green (`#00964d`) that appears in stock-status badges ("In Stock" / "Available"), and a yellow (`#ffff00`) used sparingly for "New Arrival" flags — both restrained accents that never compete with the primary red. The overall mood is that of a curated library: quiet, authoritative, and deeply knowledgeable about its domain.

colors:
  primary: "#d12328"
  primary-active: "#a31c1c"
  primary-disabled: "#ffebe8"
  ink: "#00008f"
  body: "#212121"
  muted: "#444444"
  muted-soft: "#666666"
  hairline: "#c0c0c0"
  hairline-soft: "#dedede"
  canvas: "#f0f0f0"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  stock-green: "#00964d"
  new-yellow: "#ffff00"
  badge-red: "#c12020"
  footer-bg: "#09093a"
  footer-text: "#e4e4e4"
  link-blue: "#2929ff"
  border-light: "#bdbdbd"

typography:
  display-xl:
    fontFamily: "'Archivo', 'Libre Franklin', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Archivo', 'Libre Franklin', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Archivo', 'Libre Franklin', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Archivo', 'Libre Franklin', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Archivo', 'Libre Franklin', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archivo', 'Libre Franklin', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "Baskerville, 'Times New Roman', Times, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "Baskerville, 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Baskerville, 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.15px
  badge:
    fontFamily: "'Archivo', 'Libre Franklin', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Archivo', 'Libre Franklin', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Archivo', 'Libre Franklin', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Archivo', 'Libre Franklin', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  footer-link:
    fontFamily: "'Libre Franklin', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-add-to-cart-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-outline-dark:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    border: "1px solid {colors.ink}"
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    height: 56px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  top-nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  search-submit:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    rounded: "{rounded.none}"
    height: 40px
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  product-card-stock-badge:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  product-card-new-badge:
    backgroundColor: "{colors.new-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    typography: "{typography.footer-link}"
    textColor: "{colors.footer-text}"
  footer-link-hover:
    textColor: "{colors.primary}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "10px 20px"
    height: 44px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  breadcrumb-link-hover:
    textColor: "{colors.primary}"
  category-link:
    typography: "{typography.nav-link}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} 0"
  category-link-hover:
    textColor: "{colors.primary}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  pagination-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "6px 10px"
  pagination-link-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    rounded: "{rounded.none}"
  pagination-link-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "6px 8px"
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  checkbox:
    accentColor: "{colors.ink}"
  radio:
    accentColor: "{colors.ink}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature red (`{colors.primary}`) with white text and zero border-radius. Used for "Add to Cart", "Checkout", and primary form submissions. On hover, shifts to a deeper crimson (`{colors.primary-active}`). Disabled state uses a pale pink (`{colors.primary-disabled}`) with muted text, signaling unavailability without visual noise.

**`button-secondary`** — An outlined variant using the deep navy (`{colors.ink}`) for border and text on the off-white canvas (`{colors.canvas}`). Used for "View Details", "Continue Shopping", and secondary actions. Active state fills with navy and inverts to white text. No rounded corners — maintains the brand's sharp, editorial feel.

**`button-tertiary-text`** — A text-only button in navy (`{colors.ink}`) that transitions to red (`{colors.primary}`) on hover. Used for "Read More", "See All", and inline navigation links within content sections. No border, no background — pure typographic interaction.

**`button-add-to-cart`** — A slightly taller, more prominent version of the primary button (48px height vs 44px) with wider horizontal padding. Used exclusively on product detail pages and in quick-add contexts. The extra height provides a more substantial tap target on mobile while maintaining the same visual language.

**`button-outline-dark`** — A compact outlined button (36px height) used for "Filter", "Sort", and utility actions within product listing pages. Smaller typography (`{typography.button-sm}`) and tighter padding keep it from competing with primary CTAs.

### Navigation
**`top-nav`** — A fixed-height 56px bar in the deep navy (`{colors.ink}`) with white text. Contains the store logo, primary category links, and a search icon. The nav-link typography uses uppercase with 0.5px letter-spacing, giving it a refined, library-catalog quality. Links transition to red on hover.

**`breadcrumb`** — A secondary navigation element using caption-sized type in muted gray. Current page is navy, parent links are muted, and hover reveals the brand red. No separators beyond a simple slash or chevron — keeps the path clean and unobtrusive.

**`category-link`** — Vertical navigation links used in sidebar filters and footer category lists. Uppercase nav-link typography in navy, with red hover. No underline — the color shift alone signals interactivity.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with no border-radius, containing a square aspect-ratio image, title, author name, price, and optional badges. The image area sits on the soft canvas background (`{colors.canvas}`) to handle variable cover art sizes. Badges appear in the top-left corner: red for sale, green for in-stock, yellow for new arrivals. The card has no shadow or border — it relies on the contrast between the white surface and the off-white page background for separation.

**`product-card-badge`** — A small uppercase label in the brand red (`{colors.badge-red}`) with white text. Used for "Sale", "Clearance", and promotional flags. Zero border-radius reinforces the sharp, no-nonsense aesthetic.

**`product-card-stock-badge`** — A green badge (`{colors.stock-green}`) indicating availability. Same uppercase, zero-radius treatment as the sale badge. Used for "In Stock" and "Available" messaging.

**`product-card-new-badge`** — A yellow badge (`{colors.new-yellow}`) with navy text for "New Arrival" flags. The yellow is used sparingly — only for genuinely new inventory — so it retains its signaling power.

### Forms
**`text-input`** — A standard input field with off-white background, navy border on focus, and red border on error. Height is 44px for comfortable typing. No rounded corners. Placeholder text uses body typography in muted gray.

**`select-dropdown`** — A dropdown selector matching the text-input height and border treatment. Used for sorting, filtering, and quantity selection. The dropdown arrow is styled in the brand navy.

**`checkbox`** and **`radio`** — Native form controls with the accent color set to navy (`{colors.ink}`). Used in filter panels and account forms. The navy accent ties them visually to the brand without custom styling that might break accessibility.

**`quantity-selector`** — A compact input (40px height) with increment/decrement buttons. Used on product detail pages and cart line items. The buttons are text-only (minus/plus) in navy, with hover states in red.

### Search
**`search-bar`** — A rectangular input field (40px height) with a 1px hairline border. On focus, the border switches to navy. The search submit button sits adjacent, rendered as a navy square with a white icon or text. No rounded corners — the search bar is a functional tool, not a decorative element.

**`search-submit`** — A navy button (40px height) that sits flush against the search input. Zero border-radius maintains the sharp grid. On hover, the background shifts to a slightly lighter navy (`{colors.primary-active}` equivalent).

### Footer
**`footer`** — A deep navy section (`{colors.footer-bg}`) with light gray text (`{colors.footer-text}`). Contains multiple columns: store information, customer service links, category index, and a newsletter signup. Links are in the footer-link typography (Libre Franklin, 13px) and transition to red on hover. The newsletter input and submit button mirror the search bar pattern but at 44px height.

**`newsletter-input`** — A white input field (44px height) with a hairline border. Used within the footer for email collection. The submit button is the brand red, matching the primary button treatment.

### Product Listing
**`filter-dropdown`** — A compact dropdown (40px height) used in product listing sidebars and top filter bars. Matches the select-dropdown styling but with smaller typography for space efficiency.

**`pagination-link`** — Numbered page links in navy with a 6px/10px padding. The active page fills with navy and inverts to white. Hover adds a soft background (`{colors.surface-soft}`). No border-radius — the pagination bar is a straight line of clickable numbers.

### Dividers
**`divider`** — A 1px solid line in medium gray (`{colors.hairline}`). Used between sections, below headers, and in product detail layouts. The soft variant (`{colors.hairline-soft}`) is used in less prominent contexts like card interiors and form groupings.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; filter sidebar becomes a bottom sheet or accordion; search bar moves to full-width below nav; footer columns stack; badge text may truncate to icons |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (Home, Shop, About); search bar remains in nav but collapses to icon; filter sidebar becomes a collapsible panel; footer shows 2-3 columns |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all category links; persistent filter sidebar (240px); search bar expanded with placeholder text; footer shows 4 columns; breadcrumb visible |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; filter sidebar remains 240px; additional whitespace on sides; footer may show 5 columns with extended link lists |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height on mobile
- Product card tap targets (title, image, add-to-cart) are at least 48px tall
- Filter dropdowns and pagination links use 40px minimum height
- Checkbox and radio labels are clickable with 44px minimum touch area
- Top-nav hamburger icon is 48px × 48px

### Collapsing Strategy
- Top-nav category links collapse into a hamburger menu below 744px
- Filter sidebar collapses into a "Filter" button that opens a slide-in panel or bottom sheet on mobile
- Product card badges may collapse to single-character icons (S for sale, N for new) below 480px
- Footer columns collapse from 4 to 2 to 1 as viewport narrows
- Breadcrumb truncates to show only current page and "Home" on mobile
- Search bar collapses to an icon-only button on mobile, expanding to full-width on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons were inferred from brand color logic — actual extracted hover values may differ
- Error styling for form inputs (red border) is assumed based on common e-commerce patterns — no extracted error state colors
- The exact font weights for Archivo, Baskerville, and Libre Franklin were not extractable from the live site CSS — weights shown are best-guess based on typical usage
- Letter-spacing values for display and body typography are estimated — the extracted CSS did not include explicit letter-spacing declarations
- Badge padding values are assumed based on common Shopify badge patterns — actual padding may vary
- The footer background color (`#09093a`) was extracted but may be a dark navy variant — the exact shade could differ in production
- No dark mode or high-contrast mode styles were extractable
- The brand may use additional accent colors for seasonal promotions or special collections that were not present in the extracted palette
- Button border-radius values are assumed to be `0px` based on the absence of any `border-radius` declarations in extracted CSS — the brand may use subtle rounding on some elements
- The `sb-icons` font family in the extracted list suggests a custom icon set — no icon glyphs or sizes were extractable
- The `object-fit: contain` declaration suggests specific image handling for product photos — exact aspect ratios and object-fit behaviors are inferred
- No extracted data for loading states, skeleton screens, or empty-state illustrations
- The brand's physical store address and hours are not represented in the design system tokens — these may appear as text elements without specific styling requirements
