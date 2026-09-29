---
version: alpha
name: "Yamazaki Home"
source_url: "https://theyamazakihome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A Japanese-inspired home organization brand that speaks in quiet, considered tones — its palette is anchored by a range of sophisticated neutrals that never shout. The primary action color is a restrained steel blue (#1990c6), a hue that feels more like a thoughtful accent than a demand for attention, with an active state that deepens to (#136f99). Against a canvas of warm white (#f5f5f5) and soft surfaces (#e0e0e0, #dedede), the brand builds hierarchy through subtle shifts in value rather than aggressive contrast. Ink (#2b2b2b) and body (#4d4e55) text sit comfortably on cards and containers, while muted tones (#999999, #9e9e9e, #767676) handle secondary information with the same quiet confidence. The brand introduces two signature accent colors: a fresh mint (#16c793) for positive indicators and eco-friendly badges, paired with a soft green surface (#dff3e7), and a restrained red (#c33b31) for sale markers or limited-time badges. Hairlines use (#dedede) and (#e5e5e5) — soft, forgiving lines that organize without creating visual noise. Typography leans on Bio Sans and Brutal, two geometric sans-serifs with humanist warmth, set at moderate weights (400–600) and generous line heights that echo the brand's philosophy of breathing room. Corners are softly rounded (`{rounded.sm}` 8px for buttons, `{rounded.md}` 12px for cards), never pill-shaped — a deliberate restraint that keeps the system feeling architectural rather than playful. The overall effect is one of calm curation: a design system that trusts its products' clean lines and the user's need for order, and never feels the need to raise its voice.

colors:
  primary: "#1990c6"
  primary-active: "#136f99"
  primary-disabled: "#9ecfe5"
  ink: "#2b2b2b"
  body: "#4d4e55"
  muted: "#75767e"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#f5f5f5"
  surface-soft: "#e0e0e0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-mint: "#16c793"
  accent-mint-soft: "#dff3e7"
  accent-red: "#c33b31"
  dark-ink: "#121212"
  dark-surface: "#202020"
  border-strong: "#cccccc"
  border-medium: "#aaaaaa"
  text-secondary: "#707070"
  text-tertiary: "#767676"
  text-light: "#9e9e9e"
  badge-sale: "#c33b31"
  badge-eco: "#16c793"
  badge-new: "#1990c6"

typography:
  display-xl:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', 'InterDisplay', sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  link:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Bio Sans', 'Brutal', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.border-strong}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-mint:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px 12px 44px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 8px 16px 4px 16px
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 500
    padding: 0 16px
  product-card-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 400px
  hero-banner-overlay:
    backgroundColor: "rgba(18, 18, 18, 0.3)"
    textColor: "{colors.on-primary}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  category-tile-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.surface-card}"
  badge-eco:
    backgroundColor: "{colors.accent-mint-soft}"
    textColor: "{colors.accent-mint}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
    border-bottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature steel blue (#1990c6) with white text. On hover, it deepens to (#136f99). The disabled state uses a pale blue (#9ecfe5) to maintain visual hierarchy without misleading users. All primary buttons use 8px corner rounding (`{rounded.sm}`) and 44px height for comfortable touch targets.
**`button-secondary`** — A ghost-style button with a white fill and a soft hairline border (#dedede). On hover, the background shifts to (#e0e0e0) and the border strengthens to (#cccccc). Used for "Add to Wishlist," "Compare," and other secondary actions that should not compete with the primary CTA.
**`button-tertiary`** — A text-only button with no background or border, using the body text color (#4d4e55). Reserved for "Cancel," "Clear Filters," and other low-emphasis actions. Hover state adds a subtle underline.
**`button-mint`** — A compact, positive-action button using the brand's mint accent (#16c793) with dark ink text. Used for eco-friendly badges, sustainability filters, and "In Stock" confirmations. Smaller at 36px height with tighter padding.
**`button-red`** — A sale or urgency button using (#c33b31) with white text. Used for "Sale," "Clearance," and limited-time offers. Same compact 36px height as the mint variant.

### Cards
**`product-card`** — The primary product display unit, a white card with 12px corner rounding (`{rounded.md}`). The image area uses rounded top corners matching the card, while the content area below uses 16px horizontal padding. The title uses `{typography.title-sm}` (16px, weight 500), and the price uses `{typography.body-md}` with weight 500 for emphasis. Badges overlay the top-left of the image area with 4px corner rounding (`{rounded.xs}`).
**`category-tile`** — A navigational card for department browsing, using a white background with 12px rounding and 16px padding. The active state gains a 2px solid border in the primary blue (#1990c6) and a soft background shift to (#e0e0e0).

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, white background, with a single hairline bottom border (#dedede). Navigation links use uppercase letter-spacing (0.3px) at 15px weight 500. Active links shift to the primary blue (#1990c6), while inactive links remain in the muted gray (#75767e).
**`nav-link-active`** — Active navigation state using the brand's primary blue for the text color, maintaining the same typography as the default nav link.
**`nav-link-inactive`** — Inactive navigation state using the muted gray (#75767e) for reduced visual weight.

### Forms
**`text-input`** — Standard text input with a white background, 8px corner rounding, 48px height, and a soft hairline border (#dedede). On focus, the border transitions to the primary blue (#1990c6). Error state uses the red accent (#c33b31) for the border.
**`select-input`** — Dropdown selector matching the text input's dimensions and styling, with a custom chevron icon in the muted gray.
**`search-input`** — A dedicated search field with 12px corner rounding (`{rounded.md}`) and 44px left padding to accommodate a search icon. Maintains the same 48px height and hairline border as standard inputs.

### Badges
**`badge-eco`** — A soft green badge using (#dff3e7) background with (#16c793) text, 4px rounding, and uppercase 11px weight 600 typography. Used for "Sustainable," "Eco-Friendly," and "Recycled Materials" labels.
**`badge-new`** — A blue badge using (#1990c6) background with white text, signaling new arrivals or recently added products.
**`badge-sale`** — A red badge using (#c33b31) background with white text, reserved for sale items, clearance, and limited-time offers.

### Footer
**`footer-section`** — A dark footer area using (#202020) background with white text. Links use the muted-soft gray (#999999) and shift to white on hover. The section uses generous vertical padding (48px top/bottom, 24px sides) to create breathing room.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item), hamburger navigation replaces top nav, search collapses to icon-only, footer stacks vertically, hero banner reduces to 280px height, category tiles become a horizontal scroll strip |
| Tablet | 744–1128px | Two-column product grid (2 items), top nav shows 4 primary links with "More" dropdown, search bar remains full but reduces padding, footer uses 2-column layout, hero banner at 340px height |
| Desktop | 1128–1440px | Three-column product grid (3 items), full top navigation visible, search bar at full width, footer uses 4-column layout, hero banner at 400px height, category tiles display in a 4-column grid |
| Wide | > 1440px | Four-column product grid (4 items), max-width container at 1440px centered, all elements at their largest comfortable sizing, hero banner at 480px height with wider typography |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain a minimum 44px height for comfortable touch interaction on mobile devices.
- Icon buttons use 40px × 40px touch targets, exceeding the 44px recommendation for critical actions but acceptable for secondary controls.
- Product card tap targets (title, price, image) are at minimum 48px tall to prevent accidental navigation.
- Category tiles in mobile horizontal scroll strips use 120px width × 48px height minimum.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at viewport widths below 744px, with the search icon moving into the header bar.
- Product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile).
- Footer sections collapse from 4 columns (desktop) → 2 columns (tablet) → stacked single column (mobile).
- Hero banner text overlay reduces font size and padding on mobile, with the CTA button moving below the headline.
- Category tiles transition from a grid layout (desktop) to a horizontal scrollable strip (mobile) with snap-scroll behavior.
- Accordion-style sections (product details, shipping info) remain collapsed by default on all breakpoints, expanding on user interaction.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for tertiary buttons and text links were not reliably extracted — assumed underline or opacity shift based on common patterns.
- Error state styling for form inputs (iconography, helper text color, animation) was inferred from the red accent color but not confirmed from live site inspection.
- Dark mode palette was not present on the live site; the dark surface (#202020) and dark ink (#121212) values were inferred from footer and overlay usage.
- Focus ring styling (outline color, width, offset) was not extractable — recommended using a 2px solid primary blue (#1990c6) with 2px offset for accessibility compliance.
- Loading states (skeleton screens, spinner colors, animation timing) were not observed on the live site.
- Sub-brand or collection-specific color variations (e.g., "Tosca" collection, "Wood" series) were not captured — the system assumes a unified palette.
- Typography scale for mobile-specific sizes (smaller display text, tighter line heights) was not confirmed — the current scale uses desktop values across all breakpoints.
- Modal and dialog component styling (overlay opacity, close button placement, animation) was not extractable from the static site analysis.
- Tooltip and popover styling (background, arrow positioning, z-index) was not present in the extracted styles.
- Rating and review component styling (star icons, distribution bars, sorting controls) was not observed on the product pages analyzed.
- Quantity selector increment/decrement button styling (hover, active, disabled states) was inferred from the icon-button pattern but not confirmed.
