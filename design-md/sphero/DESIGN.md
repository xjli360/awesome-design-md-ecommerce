---
version: alpha
name: "Sphero"
source_url: "https://sphero.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A bright, primary-blue (#18acf2) brand voltage that signals play-meets-pedagogy across every product tile, CTA, and navigation element — the same electric cyan that powers the Sphero BOLT's LED matrix and the brand's meta-theme bar. Against a near-black ink (#121212) and a warm neutral canvas (#e1e3e4), the system uses a restrained palette of four accent colors — a safety-orange (#f54055), a lime-green (#78d318), a deep purple (#5f249f), and a marigold (#ffb81c) — each mapped to specific product lines or learning stages, creating a color-coded curriculum without needing labels. Typography runs Montserrat at bold weights (700–900) for headlines and Roboto for body, a pairing that reads as authoritative but approachable, like a science textbook that doesn't lecture. Cards and buttons use a consistent {rounded.sm} corner radius, while hero sections and feature modules adopt {rounded.md} to create visual hierarchy through softness. The system avoids hard corners entirely except on data tables and code blocks, where {rounded.none} signals precision. Product cards stack on a white surface (#ffffff) with a subtle {spacing.base} gap, each card carrying a thin {colors.hairline} border that separates without shouting. The overall mood is optimistic and systematic — a classroom that feels like a playground, with every color and curve reinforcing the idea that coding is a creative act.

colors:
  primary: "#18acf2"
  primary-active: "#0a7db3"
  primary-disabled: "#aadddd"
  ink: "#121212"
  body: "#212121"
  muted: "#4a4a4a"
  muted-soft: "#696969"
  hairline: "#d4d6d8"
  hairline-soft: "#e1e3e4"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#f54055"
  accent-red-active: "#ea2239"
  accent-green: "#78d318"
  accent-purple: "#5f249f"
  accent-yellow: "#ffb81c"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-pinterest: "#bd081c"
  social-instagram: "#d83776"

typography:
  display-xl:
    fontFamily: "'Montserrat Black', Montserrat, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary-active}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(24, 172, 242, 0.15)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1:1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-new:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-section-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  social-icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  social-icon-button-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"
    borderBottom: "2px solid {colors.primary}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.none}"
  rating-stars:
    color: "{colors.accent-yellow}"
    size: 16px
    gap: "{spacing.xxs}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's signature blue (#18acf2). On hover, it deepens to `{colors.primary-active}` (#0a7db3); when disabled, it fades to `{colors.primary-disabled}` (#aadddd) with reduced opacity. The button uses Montserrat Bold at 16px with 0.5px letter spacing for a confident, educational tone.

**`button-secondary`** — An outlined variant with a white fill and blue border, used for secondary actions like "Learn More" or "View Details." On hover, the border shifts to `{colors.primary-active}` and the background gains a subtle tint. The 2px stroke maintains visual weight parity with the primary button.

**`button-accent-red`**, **`button-accent-green`**, **`button-accent-purple`** — Color-coded action buttons mapped to specific product lines or learning stages. Red (#f54055) signals urgency or sale items; green (#78d318) indicates "in stock" or "enroll now"; purple (#5f249f) marks premium or advanced content. Each uses the same `{typography.button-md}` and `{rounded.sm}` as the primary button for consistency.

**`button-pill-primary`** — A compact, fully rounded variant used for filter tags, "Add to Cart" on mobile, or quick-action toggles. Smaller padding and `{rounded.full}` create a pill shape that reads as more casual and interactive than the standard button.

### Cards
**`product-card`** — The standard product display unit, a white card with a thin `{colors.hairline-soft}` border and `{rounded.sm}` corners. On hover, the border shifts to `{colors.primary}` and a subtle blue box shadow appears, creating a lift effect without animation. The card contains an image (1:1 aspect ratio, `{rounded.xs}`), a title in `{typography.title-sm}`, and a muted price line.

**`product-card-image`** — The image container within a product card, using `object-fit: cover` to ensure consistent framing across varying product photography. The `{rounded.xs}` corner radius is slightly tighter than the card itself, creating a nested visual hierarchy.

**`product-badge`**, **`product-badge-new`**, **`product-badge-sale`** — Small, uppercase labels that sit at the top-left corner of product images. Green for standard badges, purple for "New" indicators, red for sale/discount items. The `{typography.badge}` token uses 11px Montserrat Bold with 0.5px letter spacing and uppercase transformation for maximum legibility at small sizes.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on desktop, collapsing to 60px on scroll. The bar is white with a subtle bottom border (`{colors.hairline-soft}`). On scroll, a light box shadow replaces the border for depth. Navigation links use Montserrat Semi-Bold at 14px with uppercase transformation and 0.5px letter spacing.

**`nav-link-active`** — The active navigation state, distinguished by a 2px blue bottom border and blue text color. Inactive links use `{colors.muted}` (#4a4a4a) to de-emphasize without disappearing.

**`category-tab`** / **`category-tab-active`** — Horizontal filter tabs used on collection pages and product category strips. Inactive tabs use muted text; the active tab gains a blue bottom border and blue text, mirroring the nav-link pattern but at a smaller scale.

### Forms
**`text-input`** — Standard text input with a white background, `{rounded.sm}` corners, and a 1px `{colors.hairline}` border. On focus, the border thickens to 2px and shifts to `{colors.primary}`. Error state uses a 2px `{colors.accent-red}` border. All inputs share the same 44px height and 16px horizontal padding for visual alignment.

**`select-input`** — Dropdown select elements matching the text-input styling. The chevron icon uses the brand's primary blue on focus.

**`search-bar`** — A pill-shaped search field (`{rounded.full}`) used in the header and on search results pages. On focus, the border thickens to 2px and turns blue. The 44px height matches button and input heights for horizontal alignment in search forms.

### Footer
**`footer-section`** — A dark footer using `{colors.ink}` (#121212) as background, with white text for headings and `{colors.muted-soft}` (#696969) for body links. Links lighten to white on hover. Social icon buttons are circular (`{rounded.full}`) at 36px, using muted icons that brighten on hover.

### Accordion
**`accordion-header`** — Collapsible section headers used in FAQ and product specification sections. The header uses a soft gray background (`{colors.surface-soft}`) with `{rounded.sm}` top corners, while the expanded content area uses a white background with no rounding, creating a clean separation.

### Ratings
**`rating-stars`** — Star ratings rendered in `{colors.accent-yellow}` (#ffb81c) at 16px with 2px gaps. The yellow provides a warm, positive signal against the predominantly blue and neutral palette.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; buttons become full-width; hero padding reduces to 32px; search bar moves below nav |
| Tablet | 744–1128px | Two-column product grid; nav links truncate to icons; hero uses 48px padding; side-by-side form layouts |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero uses 64px padding; multi-column footer |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero uses 80px padding; expanded footer with 4 columns |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44x44px touch target on mobile
- Navigation hamburger icon is 48x48px
- Product card tap targets (image, title, price, button) are each at least 44px tall
- Search bar tap target is 44px tall, full-width on mobile
- Accordion headers are 48px tall for easy tapping
- Social icon buttons are 44x44px on mobile (expanded from 36x36px)

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Hero section stacks vertically on mobile (image below text)
- Footer collapses from 4 columns to 2 columns on tablet, 1 column on mobile
- Category filter tabs become a horizontal scrollable strip on mobile
- Side-by-side form fields (e.g., "First Name" / "Last Name") stack vertically below 744px
- Accordion content collapses by default on all breakpoints, expanding on click

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only basic hover colors for primary and secondary buttons. Hover states for product badges, accordion headers, and footer links are inferred from common patterns, not verified from live CSS.
- **Error styling**: Only the error border color for text inputs was extracted. Error message typography, icon placement, and animation timing are unknown.
- **Dark mode**: No dark mode implementation was detected on the live site. The palette assumes a light-mode-only system.
- **Sub-brand palettes**: Sphero may use distinct color schemes for sub-brands (e.g., Sphero Edu, littleBits, RVR). Only the main brand palette was extracted.
- **Animation and motion**: No timing values, easing curves, or transition durations were extracted. The system likely uses standard 200-300ms ease-in-out transitions, but this is unconfirmed.
- **Typography scale**: Font sizes for display-xl through caption were inferred from common Montserrat/Roboto pairings and typical e-commerce scales. The exact hierarchy from the live site may differ.
- **Spacing scale**: The spacing tokens follow a standard 4px base system. The live site may use a custom scale (e.g., 8px base) or different section padding values.
- **Icon system**: Material Symbols Outlined was detected in font declarations, but icon sizes, stroke weights, and usage guidelines are unknown.
- **Checkout flow**: Shopify checkout styling (Shopify Pay, Klarna, Afterpay widgets) was excluded from the palette. The checkout experience may use a different design system entirely.
- **Accessibility**: Contrast ratios for text on colored backgrounds (e.g., white text on #18acf2) were not verified. The `{colors.primary-disabled}` (#aadddd) may fail WCAG AA for text contrast.
- **Component states**: Focus-visible outlines, active/pressed states for buttons, and disabled states for inputs beyond color changes are undocumented.
