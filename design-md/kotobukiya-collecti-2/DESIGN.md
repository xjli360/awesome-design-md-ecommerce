---
version: alpha
name: "Kotobukiya"
source_url: "https://www.kotobukiya.co.jp"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A portal for plastic-model and figure enthusiasts, Kotobukiya’s digital presence is anchored on a vivid primary green (#009944) that reads as both a brand signature and a nod to the company’s name (Kotobukiya meaning “longevity” or “congratulations,” often associated with celebration and nature). The green appears on every primary CTA, navigation bar, and category accent, set against a predominantly white canvas (#ffffff) with a soft secondary surface (#f7f7f7) for card backgrounds and content sections. The extracted color palette reveals a surprising breadth — alongside the core green, there are accent tones for product categories: a warm orange (#f77a00), a cool blue (#0577c8), a soft pink (#f26faa), a deep red (#e92121), and a marigold (#eac33d). These are not decorative; they map to specific product lines (M.S.G weapon sets, Frame Arms, Megami Device, etc.), creating a color-coded taxonomy that helps collectors navigate a vast catalog. Typography relies on a stack of Japanese system fonts — FOT-筑紫A丸ゴシック (a rounded gothic) in multiple weights (Std D, M, B, E) alongside Hiragino Kaku Gothic Pro and Meiryo — giving the interface a friendly, approachable feel that contrasts with the precision-engineered subject matter. The rounded gothic’s soft terminals mirror the gentle corner radii used throughout: cards at `{rounded.sm}` (8px), buttons at `{rounded.sm}`, and the search bar at `{rounded.full}`. Borders are thin and light (`{colors.hairline}` #d0d0d0, `{colors.hairline-soft}` #e6e6e6), keeping the layout clean and uncluttered despite the density of product information. The overall effect is a structured, information-rich portal that uses color as a wayfinding system and typographic softness to make a complex hobby feel accessible.

colors:
  primary: "#009944"
  primary-active: "#007032"
  primary-disabled: "#b6d9c0"
  ink: "#222222"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#8d8d8d"
  hairline: "#d0d0d0"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f77a00"
  accent-blue: "#0577c8"
  accent-pink: "#f26faa"
  accent-red: "#e92121"
  accent-marigold: "#eac33d"
  accent-purple: "#9875cf"
  accent-teal: "#00997e"
  accent-sky: "#50c9df"
  accent-burgundy: "#8a1a1f"
  accent-brown: "#6e4941"
  badge-new: "#e92121"
  badge-sale: "#f77a00"
  star-rating: "#eac33d"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'FOT-筑紫A丸ゴシック Std E', 'FOT-筑紫A丸ゴシック std E', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'FOT-筑紫A丸ゴシック Std D', 'FOT-筑紫A丸ゴシック std D', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.3px
  display-md:
    fontFamily: "'FOT-筑紫A丸ゴシック Std D', 'FOT-筑紫A丸ゴシック std D', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  title-lg:
    fontFamily: "'FOT-筑紫A丸ゴシック Std M', 'FOT-筑紫A丸ゴシック std M', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'FOT-筑紫A丸ゴシック Std M', 'FOT-筑紫A丸ゴシック std M', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'FOT-筑紫A丸ゴシック Std M', 'FOT-筑紫A丸ゴシック std M', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.1px
  body-sm:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  caption:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'FOT-筑紫A丸ゴシック Std B', 'FOT-筑紫A丸ゴシック std B', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'FOT-筑紫A丸ゴシック Std D', 'FOT-筑紫A丸ゴシック std D', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'FOT-筑紫A丸ゴシック Std D', 'FOT-筑紫A丸ゴシック std D', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Hiragino Kaku Gothic ProN', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'FOT-筑紫A丸ゴシック Std M', 'FOT-筑紫A丸ゴシック std M', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  price:
    fontFamily: "'FOT-筑紫A丸ゴシック Std D', 'FOT-筑紫A丸ゴシック std D', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  price-lg:
    fontFamily: "'FOT-筑紫A丸ゴシック Std D', 'FOT-筑紫A丸ゴシック std D', 'Hiragino Kaku Gothic Pro', 'Meiryo', -apple-system, 'Arial', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.1px

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "8px"
    left: "8px"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.body}"
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
  price-display:
    typography: "{typography.price-lg}"
    textColor: "{colors.body}"
  price-display-sale:
    typography: "{typography.price-lg}"
    textColor: "{colors.accent-red}"
  price-display-original:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    textDecoration: "line-through"
  stock-indicator:
    typography: "{typography.caption-sm}"
    textColor: "{colors.primary}"
  stock-indicator-low:
    textColor: "{colors.accent-orange}"
  stock-indicator-out:
    textColor: "{colors.accent-red}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: "1px"
    margin: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with `{colors.primary}` green and white text. Used for add-to-cart, checkout, and primary navigation actions. On hover, shifts to `{colors.primary-active}` (#007032). Disabled state uses a muted green (`{colors.primary-disabled}`). Height is 44px with `{rounded.sm}` corners.

**`button-secondary`** — An outlined variant with a white fill and `{colors.primary}` green border and text. Used for secondary actions like "View Details" or "Cancel." Maintains the same 44px height and `{rounded.sm}` as the primary button for visual consistency.

**`button-accent-orange` / `button-accent-blue` / `button-accent-pink`** — Category-specific CTAs that map to product line colors. Orange (`{colors.accent-orange}`) for M.S.G weapon sets, blue (`{colors.accent-blue}`) for Frame Arms, pink (`{colors.accent-pink}`) for Megami Device. These appear on product detail pages and category landing pages to reinforce the color-coded taxonomy.

**`button-ghost`** — A minimal text-only button with no background or border. Used for "Read More" links, filter resets, and dismissible actions. Hover state adds a subtle background tint (not yet extracted).

### Cards
**`product-card`** — The core content unit for the product grid. A white card with a 1px soft border (`{colors.hairline-soft}`) and `{rounded.sm}` corners. Contains a square aspect-ratio image at the top (with `{rounded.sm}` top corners), followed by the product title in `{typography.title-sm}` and price in `{typography.price}`. On hover, the border darkens to `{colors.hairline}` and a subtle box-shadow appears. Badges (new, sale, pre-order) are positioned absolutely at the top-left of the image.

**`category-tag`** — Small pill-shaped tags used for filtering and category navigation. Default state is a light gray fill (`{colors.surface-soft}`) with muted text. Active state fills with `{colors.primary}` green and white text. Uses `{rounded.full}` for a friendly, approachable shape.

### Navigation
**`nav-bar`** — The top navigation bar, 60px tall with a white background and a single `{colors.hairline}` bottom border. Links use `{typography.nav-link}` (14px, medium weight). Active links are indicated by a 2px `{colors.primary}` bottom border. A secondary variant (`nav-bar-primary`) inverts to a green background with white text for category landing pages.

**`breadcrumb`** — Simple text-based breadcrumbs in `{typography.caption}` (12px). Default links are `{colors.muted}`, active (current page) is `{colors.body}`. Separators are not yet extracted but likely use a simple ">" or "/" in `{colors.hairline}`.

### Forms
**`text-input`** — Standard text input with a white background, 1px `{colors.hairline}` border, and `{rounded.sm}` corners. On focus, the border thickens to 2px and changes to `{colors.primary}` green. Height is 44px to match button heights for form alignment.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a light gray background (`{colors.surface-soft}`) and `{colors.hairline}` border. On focus, the background turns white and the border becomes 2px `{colors.primary}` green. Height is 44px.

### Footer
**`footer`** — A dark footer with `{colors.ink}` (#222222) background and light gray text (`{colors.muted-soft}` #8d8d8d). Links are the same muted color and lighten to white on hover. Padding is generous at `{spacing.xxl}` (48px) on top/bottom and `{spacing.xl}` (32px) on sides.

### Badges & Indicators
**`product-card-badge`** — Small rectangular badges (4px radius) positioned at the top-left of product images. Uses `{colors.badge-new}` (#e92121) for "New" items, `{colors.badge-sale}` (#f77a00) for sale items. Text is white, uppercase, 11px bold.

**`stock-indicator`** — Text-based stock status. Green (`{colors.primary}`) for "In Stock," orange (`{colors.accent-orange}`) for "Low Stock," red (`{colors.accent-red}`) for "Out of Stock." Uses `{typography.caption-sm}`.

### Dividers
**`divider`** — A simple 1px horizontal line in `{colors.hairline}` (#d0d0d0) with 16px vertical margin. Used to separate sections within product detail pages and content blocks.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns). Nav-bar collapses to hamburger menu. Search bar becomes full-width. Product card images stack vertically. Footer links stack. Category tags wrap. |
| Tablet | 744–1128px | Two-column product grid. Nav-bar shows limited links with "More" dropdown. Search bar is 50% width. Sidebar filters appear as a slide-out panel. |
| Desktop | 1128–1440px | Three-column product grid. Full nav-bar with all links visible. Search bar is fixed width (400px). Sidebar filters are persistent. Hero banners use full-width layout. |
| Wide | > 1440px | Four-column product grid. Max-width container (1440px) centered. Additional whitespace on sides. Hero banners may include parallax or full-bleed imagery. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons and category tags have a minimum 44x44px tap area, even if the visual element is smaller.
- Product card tap targets extend to the full card area (not just the title/price).
- Search bar and text inputs are 44px tall to meet WCAG touch target recommendations.

### Collapsing Strategy
- **Navigation**: On mobile, the full nav-bar collapses into a hamburger menu. Category sub-navigation becomes an accordion or slide-out panel.
- **Sidebar Filters**: On tablet and mobile, the filter sidebar collapses into a "Filter" button that opens a modal or slide-out panel.
- **Product Grid**: Columns reduce from 4 (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile). On mobile, product cards may use a list layout instead of grid.
- **Footer**: On mobile, footer link columns stack vertically. The multi-column layout collapses to a single column with accordion-style section headers.
- **Hero Banners**: On mobile, hero banners reduce padding and may crop images to focus on the central subject. Text overlays become bottom-aligned instead of centered.
- **Breadcrumbs**: On mobile, breadcrumbs may truncate to show only the current page and one parent level, with a "Back" button as the primary navigation.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only extracted for product cards (box-shadow) and nav links (border). Button hover states (opacity, shadow, scale) are inferred but not confirmed from the live site extraction.
- **Focus states**: No focus ring styles were extracted. Likely uses a 2px `{colors.primary}` outline or box-shadow, but this is unconfirmed.
- **Error states**: No form error styling (border colors, error messages) was extracted. Likely uses `{colors.accent-red}` (#e92121) for error borders and text.
- **Dark mode**: No dark mode tokens were found. The site appears to be light-mode only.
- **Sub-brand palettes**: The accent colors (orange, blue, pink, etc.) are inferred from the extracted color list and product line associations. Exact mapping to specific product lines (M.S.G, Frame Arms, Megami Device, Hexa Gear, etc.) is based on industry knowledge, not extracted data.
- **Animation/transition**: No transition durations or easing functions were extracted. Likely uses 200-300ms ease-in-out for hover/focus states.
- **Typography scale**: Font sizes and weights are estimated based on common Japanese e-commerce patterns and the extracted font stack. Exact sizes may vary. The rounded gothic fonts (FOT-筑紫A丸ゴシック) are confirmed in the stack but their specific weight usage (Std D vs M vs B vs E) is inferred.
- **Spacing scale**: The spacing tokens are based on common 8px/4px grid systems. Exact values from the live site were not extracted.
- **Rounded corners**: The `{rounded.sm}` (8px) for cards and buttons is confirmed from the extracted CSS. Other values (xs, md, lg, xl, full) are estimated based on common patterns.
- **Iconography**: No icon system was extracted. The site likely uses custom SVG icons or a font icon set for cart, search, menu, and social links.
- **Color usage**: The extracted color list includes 30+ colors, many of which may be from third-party widgets (social icons, payment badges) rather than the brand's design system. The primary green (#009944) is confirmed as the meta theme-color and most distinctive brand color.
