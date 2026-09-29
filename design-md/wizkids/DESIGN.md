---
version: alpha
name: "WizKids"
source_url: "https://wizkids.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A tabletop RPG brand that wears its gold #986c15 like a guild emblem — it appears on every primary CTA, product-badge border, and category header, anchoring a system that otherwise runs on cool grays (#747474, #3e3e3e, #aaaaaa) and a bone-white canvas (#f8f8f8). The extracted palette reveals a brand that uses color sparingly but with intention: a deep navy #003388 surfaces in footer links and secondary headers, a forest-green #65bc7b marks in-stock indicators, and a warning-red #d04544 flags sold-out or limited-run items. Type is where WizKids distinguishes itself — Captain Nelson, a serif inline printed face, appears on product titles and hero headers, while Klinic Slab Bold and Klinic Slab Book handle subheads and body copy, giving the site a letterpress-meets-gaming-guild feel. Open Sans and PT Sans serve as fallback workhorses for navigation and utility text. Product cards use soft {rounded.sm} corners and a light #ebeaea hairline, with hover states that shift the card background to #f9f9f9. The brand's signature move is the gold-accented badge — a {rounded.xs} pill in #986c15 with white text — that labels "New Release," "Pre-Order," and "Exclusive" across the catalog. Buttons follow a two-tier system: gold-filled for primary actions, gray-outlined (#747474) for secondary, both at 48px height with {rounded.sm} corners. The overall impression is a digital game shop that respects the tactility of physical miniatures and rulebooks — generous whitespace, restrained color, and typography that feels stamped rather than set.

colors:
  primary: "#986c15"
  primary-active: "#7a5510"
  primary-disabled: "#d4b87a"
  ink: "#363839"
  body: "#3e3e3e"
  muted: "#747474"
  muted-soft: "#aaaaaa"
  hairline: "#e0dede"
  hairline-soft: "#ebeaea"
  canvas: "#f8f8f8"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  navy: "#003388"
  green-stock: "#65bc7b"
  red-warning: "#d04544"
  red-sale: "#e0284f"
  badge-gold: "#986c15"
  badge-green: "#a0ce4e"

typography:
  display-xl:
    fontFamily: "'Captain Nelson', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'Klinic Slab Bold', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Klinic Slab Bold', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Klinic Slab Book', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Klinic Slab Book', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'PT Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'PT Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'PT Sans', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', 'PT Sans', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', 'PT Sans', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', 'PT Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'PT Sans', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Open Sans', 'PT Sans', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    padding: 14px 28px
    height: 48px
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
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.muted}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
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
    border: "2px solid {colors.red-warning}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
  product-card-stock:
    typography: "{typography.caption}"
    color: "{colors.green-stock}"
  product-card-sold-out:
    typography: "{typography.caption}"
    color: "{colors.red-warning}"
  badge:
    backgroundColor: "{colors.badge-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-green:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-red:
    backgroundColor: "{colors.red-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-subtitle:
    typography: "{typography.display-lg}"
    color: "{colors.muted}"
  category-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} {spacing.base}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.on-primary}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px

## Components

### Buttons
**`button-primary`** — Gold-filled (#986c15) workhorse for all primary actions: "Add to Cart," "Pre-Order Now," "Subscribe." On hover, darkens to #7a5510. Disabled state uses a muted gold #d4b87a with reduced opacity. Text is white Open Sans 600 at 15px, with 8px rounded corners and 48px height for comfortable tap targets.

**`button-secondary`** — Outlined variant for secondary actions like "View Details" or "Compare." Uses a 1px #747474 border on white canvas, with text in the same muted gray. Active state shifts border and text to ink (#363839) with a #f6f6f6 background. Same 48px height and 8px radius as primary for visual consistency.

**`button-tertiary-text`** — Text-only link styled as a button, used for "Learn More" or "See All" in content sections. Gold #986c15 text with no background or border. Hover darkens to primary-active.

### Cards
**`product-card`** — The core catalog unit: a white card with a 1px #ebeaea border and 8px rounded corners. Contains a product image (full-width, no border-radius on top), a Klinic Slab Book title at 18px, a gold price in Open Sans 16px, and a stock indicator in green (#65bc7b) or red (#d04544). On hover, background shifts to #f6f6f6, border to #e0dede, and a subtle box-shadow appears. Badges (New, Pre-Order, Exclusive) overlay the top-left corner of the image area.

### Navigation
**`nav-bar`** — Fixed 72px white header with a 1px #ebeaea bottom border. Logo sits left (typically the WizKids wordmark or shield icon), with nav links in Open Sans 600 at 15px. Active page gets a 2px gold bottom border. Hover state tints links gold. Secondary nav items (Cart, Account, Search) sit right-aligned as icon buttons.

**`search-bar`** — Pill-shaped input with full border-radius, 44px height, and a 1px #e0dede border. On focus, border thickens to 2px gold. Placeholder text in #aaaaaa. Often paired with a search icon button.

### Forms
**`text-input`** — Standard form field for checkout, account creation, and filters. White background, 48px height, 8px radius, 1px #e0dede border. Focus state uses a 2px gold border. Error state switches to 2px #d04544. Padding is 12px vertical, 16px horizontal.

**`quantity-selector`** — Compact numeric input for cart line items. 40px height, 8px radius, 1px #e0dede border. Typically rendered as a row with minus/plus buttons flanking the number.

### Badges
**`badge`** — Small uppercase label in 11px Open Sans 700, 0.5px letter-spacing, with 4px rounded corners and 4px/10px padding. Three variants: gold (#986c15) for "New Release" and "Exclusive," green (#a0ce4e) for "In Stock" and "Sale," red (#e0284f) for "Limited" and "Clearance." Always white text.

### Footer
**`footer`** — Deep navy (#003388) full-width section with white text. Links render in #aaaaaa and lighten to white on hover. Typography is Open Sans 14px. Contains columns for Support, Community, Shop, and Legal. Social icons appear in a row at the bottom.

### Hero
**`hero-section`** — Full-width promotional area using Captain Nelson 48px for the headline and Klinic Slab Bold 36px for the subtitle. Background is white (#f8f8f8) with generous 64px vertical padding. Often features a large product image or lifestyle shot behind the text.

### Pagination
**`pagination`** — Numbered page controls at the bottom of catalog listings. Inactive numbers are gray (#747474) on white with 8px radius. Active page uses gold fill with white text. Previous/Next arrows use the same styling as inactive.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero font drops to 32px; search bar moves to sticky top; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only; hero at 40px; filter bar collapses to dropdown |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at 48px; persistent sidebar filters on category pages |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero scales to 56px |

### Touch Targets
- All buttons and interactive elements minimum 44px height (buttons at 48px, inputs at 48px, quantity selector at 40px)
- Nav links have 48px tap area even if text is smaller
- Product card tap target is the entire card surface
- Badges are minimum 24px height for touch

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; secondary icons (cart, account, search) remain visible
- Product filters collapse to a single "Filter" button on mobile, opening a slide-out panel
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Hero image stacks below text on mobile (text first)
- Product grid collapses from 4 columns to 1 on mobile, 2 on tablet

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components were inferred from common patterns; actual extracted hover colors were not available
- Error state styling for forms (red borders confirmed, but error message typography and iconography not extracted)
- Dark mode is not present on the live site; no dark palette tokens exist
- Sub-brand or franchise-specific palettes (Dungeons & Dragons, Magic: The Gathering, Pathfinder) may exist but were not extracted
- Animation and transition durations (hover fades, card lift, nav dropdown) not captured
- Loading states (skeleton screens, spinners) not observed
- Modal and overlay styling (cart drawer, quick-view, age-gate) not extracted
- The extracted font list includes "STIU Jason" and "awb-icons" which appear to be icon-font or system fonts; they are not used in the typography system
- Checkout flow (Shopify default) may override brand tokens for payment widgets (Afterpay, Klarna colors not included)
- Print stylesheet and accessibility focus outlines not verified
