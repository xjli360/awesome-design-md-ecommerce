---
version: alpha
name: "Magazine Heaven"
source_url: "https://www.magazineheaven.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-teal spine (#226d7a) runs through Magazine Heaven like a library shelf label — it is the brand's quiet, bookish anchor, appearing on the header, footer, and primary action buttons, while a pale cyan wash (#e4f5fa) backs the page canvas like the endpapers of a vintage hardcover. The extracted palette is narrow but intentional: the teal (#226d7a) and its slightly lighter sibling (#1e6d7a) form the structural color system, while #b0e0e9 and #22b8d1 serve as accent highlights for sale badges, category tags, and link underlines. The site reads as a specialist's shop — a place where magazine back-issues and niche periodicals are cataloged with the seriousness of a university library. Typography runs Arial and Open Sans at moderate sizes, with body text at 15–16px and display headings at 24–28px, never shouting. Corners are softly squared at {rounded.sm} for buttons and {rounded.md} for product cards, avoiding the pill-shaped friendliness of consumer marketplaces in favor of a more editorial, almost academic restraint. The search bar sits prominently in the header, a teal-outlined rectangle with a magnifying-glass icon, signaling that discovery here is query-driven rather than browse-driven. There is no hero carousel, no lifestyle photography — the page is a dense grid of magazine covers, each a small thumbnail with title, issue number, and price, arranged in a 4–6 column layout that prioritizes inventory over atmosphere. The footer is a full-width teal band (#226d7a) with white links, a closing gesture that feels like a bookplate.

colors:
  primary: "#226d7a"
  primary-active: "#1a555f"
  primary-disabled: "#a3c9d0"
  ink: "#1a1a1a"
  body: "#2d2d2d"
  muted: "#5c5c5c"
  muted-soft: "#8a8a8a"
  hairline: "#c8d8db"
  hairline-soft: "#dce8eb"
  canvas: "#e4f5fa"
  surface-soft: "#f0f8fb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#22b8d1"
  accent-soft: "#b0e0e9"
  sale-badge: "#22b8d1"
  category-tag: "#b0e0e9"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.15px
  badge:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.2px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "2px solid {colors.primary-active}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 14px
    height: 32px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.sm}"
  nav-link-active:
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 44px
    border: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(34, 109, 122, 0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "3/4"
    objectFit: "cover"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  category-tag:
    backgroundColor: "{colors.category-tag}"
    textColor: "{colors.primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
    fontWeight: 600
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    textDecoration: "underline"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  loading-spinner:
    color: "{colors.primary}"
    size: "24px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand teal (#226d7a) and white text. Used for "Add to Cart", "Subscribe", and "Checkout" actions. On hover, darkens to {colors.primary-active}; disabled state uses the muted teal {colors.primary-disabled}. The 4px corner radius ({rounded.sm}) and 40px height give it a compact, no-nonsense profile.

**`button-secondary`** — An outlined variant with a teal border on the pale cyan canvas background. Used for "View Details" and "Preview Issue" actions. On hover, the border deepens to {colors.primary-active} and the background shifts to {colors.surface-soft}. The 2px border is deliberate — it matches the search bar's outline weight, creating visual consistency across interactive elements.

**`button-accent`** — A smaller, brighter button using the cyan accent (#22b8d1) for sale badges, "New Issue" flags, and secondary inline actions. Uses {typography.button-sm} at 13px and a compact 32px height, making it suitable for tight grid spaces within product cards.

### Cards
**`product-card`** — The primary inventory unit: a white card with a magazine cover thumbnail, title, issue number, publication date, and price. The 8px corner radius ({rounded.md}) and thin hairline border keep the card crisp without competing with the cover art. On hover, the border shifts to {colors.primary} and a subtle shadow lifts the card — a quiet signal of interactivity in an otherwise dense grid.

**`product-card-image`** — The magazine cover thumbnail uses a 3:4 aspect ratio (standard magazine proportions) with cover-fit cropping. The image sits in a {rounded.sm} container within the card, creating a nested-corner effect that echoes the card's own rounding.

### Navigation
**`nav-bar`** — A full-width teal bar at 56px height, containing the site logo (left), category links (center), and account/cart icons (right). The teal background is the brand's most assertive color move — it frames every page with the same deep spine color. Navigation links are white with 8px horizontal padding and a subtle white overlay on active state.

**`nav-link`** — White text on teal background with 4px corner rounding on hover/active. The 15px font size at weight 600 balances readability with the bar's compact height.

### Forms
**`text-input`** — A standard input field with a 1px hairline border, white background, and 4px corners. On focus, the border thickens to 2px and adopts the brand teal — a clear, accessible focus indicator that matches the search bar's treatment.

**`search-bar`** — The site's primary discovery tool: a white rectangle with a 2px teal border and a magnifying-glass icon. Unlike consumer sites that use pill shapes, this search bar is squarely rectangular ({rounded.sm}), reinforcing the editorial, library-like tone. The 44px height accommodates both text input and the icon button.

### Badges & Tags
**`sale-badge`** — A bright cyan (#22b8d1) badge with uppercase 11px text, used to flag discounted issues and special offers. The 4px corners and compact padding make it readable at small sizes within the product grid.

**`category-tag`** — A pill-shaped tag ({rounded.full}) using the soft cyan (#b0e0e9) background with teal text. Used for genre labels like "Fashion", "Art", "Music" that appear above search results or within filter strips. The pill shape is the one exception to the site's squared-off aesthetic — a small concession to scannability in filter interfaces.

### Footer
**`footer`** — A full-width teal band matching the header, containing site links, newsletter signup, and social icons. Links are white with underlines, maintaining readability against the dark background. The {spacing.xl} vertical padding gives the footer breathing room without overwhelming the page's dense inventory grid.

### Pagination
**`pagination-button`** — Outlined page-number buttons for navigating multi-page search results and category listings. The active page uses the filled teal treatment, matching the primary button style. Buttons are compact at 32px height with 6px horizontal padding, designed to sit in a tight row below the product grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Product grid collapses to 2 columns; nav-bar reduces to hamburger menu; search bar moves below header; footer stacks vertically; sale badges become full-width strips |
| Tablet | 744–1128px | Product grid shows 3–4 columns; nav-bar shows abbreviated category links (top 4); search bar remains in header but narrows; footer splits into 2 columns |
| Desktop | 1128–1440px | Product grid shows 5–6 columns; full nav-bar with all category links; search bar at full width; footer in 4-column layout |
| Wide | > 1440px | Product grid maxes at 6 columns with centered container; all elements maintain max-width 1440px with generous side margins |

### Touch Targets
- All buttons and links maintain minimum 44px tap target (exceeds 40px button height via padding)
- Product cards are fully tappable with minimum 120px height
- Search bar input field is 44px tall for comfortable touch typing
- Pagination buttons are 32px tall with 12px horizontal padding (effective 44px tap target)
- Category tags are 28px tall with 10px horizontal padding (effective 48px tap target)

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-out drawer showing all category links
- Product grid reduces columns from 6 to 2 on mobile, with images scaling proportionally
- Search bar moves from inline header position to full-width below the logo on mobile
- Footer navigation collapses from 4 columns to stacked single column below 744px
- Category filter strip collapses to a horizontal scrollable row on mobile, with the first tag pinned as "All"

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is narrow (5 hex values) and may not represent the full brand system — missing secondary accents, error states, and hover colors beyond the primary-active derivation
- No meta theme-color was detected, so the browser chrome color is unknown
- Font-family declarations were limited to Arial, Open Sans, Roboto, and sans-serif — the actual brand typeface may include additional weights or a proprietary font not exposed in extracted CSS
- Hover and focus states for text inputs, links, and secondary buttons were inferred from common patterns rather than extracted from live styles
- No extracted data for: error message styling, success states, loading skeletons, empty states, modal/dialog overlays, or tooltip design
- The site returned a 403 Forbidden status at time of extraction, meaning the extracted colors may come from an error page rather than the full production experience — the true brand palette could differ significantly
- No data on dark mode or high-contrast mode adaptations
- Spacing values (section, xxl, etc.) are estimated from common e-commerce patterns rather than extracted from computed styles
- The product card hover shadow value is an estimate — actual shadow depth and color may vary
- No extracted data on iconography style, illustration approach, or photography treatment
