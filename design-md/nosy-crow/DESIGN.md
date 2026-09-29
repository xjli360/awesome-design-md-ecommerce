---
version: alpha
name: "Nosy Crow"
source_url: "https://nosycrow.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A children's book publisher whose visual identity is built on a deep, confident blue — #003388 — that appears across the site as the primary brand color, used for the logo, navigation, and key interactive elements. This blue is paired with a clean white canvas (#ffffff) and a secondary accent of #ff9900, a warm orange that appears in badges, promotional elements, and hover states, creating a friendly, energetic contrast. The typography relies on Arial and Helvetica, a pragmatic choice that ensures readability across devices, with a restrained approach to weight variation — most body text sits at 400 weight, while headings and buttons use 600-700 for clear hierarchy. The design language is straightforward and accessible, with rounded corners on buttons and cards using {rounded.sm} (8px) and {rounded.md} (12px), avoiding the harshness of sharp edges while maintaining a clean, uncluttered layout. The overall feel is that of a well-organized library — calm, inviting, and focused on content discovery rather than visual spectacle. The extracted color palette includes a wide range of blues (#003399, #0693e3, #0a7aff) and grays (#eeeeee, #cdcdcd, #949494), but the distinctive #003388 stands out as the brand's true primary, while #ff9900 provides the necessary warmth for calls-to-action and children-oriented elements. The site uses generous whitespace and a grid-based layout that prioritizes book covers and illustrations, with the brand blue serving as a consistent anchor throughout the browsing experience.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#95bedd"
  ink: "#1e1f26"
  body: "#444444"
  muted: "#949494"
  muted-soft: "#cdcdcd"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#ff9900"
  accent-orange-hover: "#e68a00"
  accent-pink: "#e94c89"
  accent-green: "#00d084"
  badge-new: "#ff9900"
  badge-sale: "#e94c89"
  link-blue: "#0757fe"
  star-rating: "#ff9900"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
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
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
    padding: 4px 0
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-logo:
    height: 40px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.sm}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-age-range:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    textColor: "{colors.accent-orange}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.section}"
    minHeight: 300px
  hero-banner-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 40px
  filter-dropdown-focused:
    border: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action button, filled with {colors.primary} (#003388) and white text. Used for key actions like "Add to Cart", "Subscribe", and "Shop Now". On hover, it shifts to {colors.primary-active} (#002266). The disabled state uses {colors.primary-disabled} (#95bedd) to indicate inactivity while maintaining brand consistency.

**`button-secondary`** — An outlined variant with a white background and 2px solid border in {colors.primary}. Used for secondary actions like "Learn More" or "View Details". The hover state fills the background with {colors.primary} and switches text to white.

**`button-accent-orange`** — A warm accent button using {colors.accent-orange} (#ff9900) with dark text. Reserved for promotional actions, "New Releases" sections, and children-oriented CTAs where the brand blue feels too formal. Hover darkens to {colors.accent-orange-hover} (#e68a00).

**`button-accent-pink`** — A playful accent button using {colors.accent-pink} (#e94c89) with white text. Used sparingly for special promotions, seasonal campaigns, or "Sale" sections. Provides a distinct visual break from the blue-orange palette.

**`button-text-link`** — A minimal text-only button styled as an inline link with {colors.link-blue} (#0757fe). Used for "Read More", "See All", and secondary navigation within content blocks. Underlines on hover for clarity.

### Navigation
**`top-nav`** — The primary navigation bar, 72px tall with a white background and a subtle bottom border in {colors.hairline} (#e5e5e5). Contains the brand logo (40px height), navigation links, and a search bar. Sticky on desktop, collapsing to a hamburger menu on mobile.

**`nav-link-active`** — Active navigation link with {colors.primary} text and a 3px bottom border in the same blue. Indicates the current section or page.

**`nav-link-inactive`** — Inactive navigation link in {colors.body} (#444444). Hover transitions to {colors.primary} text color.

**`search-bar`** — A pill-shaped search input with a light gray background ({colors.surface-soft} #eeeeee) and subtle border. On focus, the background turns white and the border becomes 2px solid {colors.primary}. The rounded-full shape gives it a friendly, approachable feel.

### Cards
**`product-card`** — A book display card with a white background, 12px rounded corners, and a soft box shadow. The card contains a 3:4 aspect ratio image at the top (with rounded top corners), followed by the book title and price. On hover, the shadow deepens to indicate interactivity.

**`badge-new`** — A small, uppercase badge with an orange background ({colors.badge-new} #ff9900) and dark text. Used to flag newly released books. Positioned at the top-left corner of product cards.

**`badge-sale`** — A pink badge ({colors.badge-sale} #e94c89) with white text for sale or discount indicators. Uses the same uppercase, bold typography as the new badge.

**`badge-age-range`** — A pill-shaped badge with a light gray background and muted text, displaying the recommended age range (e.g., "3-5 years"). Appears on product cards and search results.

### Footer
**`footer`** — A full-width footer with a deep blue background ({colors.primary}) and white text. Contains navigation links, newsletter signup, and social media icons. Links turn orange on hover ({colors.accent-orange}) for visual contrast against the blue background.

**`newsletter-input`** — A white text input with a 1px border for email collection. Paired with an orange submit button ({colors.accent-orange}) that creates a clear call-to-action against the footer's blue background.

### Hero
**`hero-banner`** — A full-width hero section with a {colors.primary} background and white text. Used for featured collections, seasonal promotions, and brand messaging. An accent variant uses {colors.accent-orange} for high-energy campaigns. Minimum height of 300px with generous padding.

### Filters & Navigation
**`category-tag`** — A pill-shaped filter tag with a light gray background. Active state fills with {colors.primary} and white text. Used in category navigation and search filters.

**`filter-dropdown`** — A standard dropdown with a white background, 1px border, and 8px rounded corners. On focus, the border thickens to 2px solid {colors.primary}.

**`breadcrumb`** — Small caption text in {colors.muted} (#949494) for secondary navigation. The active/last item uses {colors.ink} (#1e1f26) to indicate the current page.

**`pagination-button`** — A bordered button with {colors.primary} text. The active page uses a filled {colors.primary} background with white text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack vertically; hero banner reduces to 200px min-height; search bar moves to expandable overlay; footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links with "More" dropdown; hero banner at 250px; search bar remains visible but compact; footer links in two columns |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; hero banner at 300px; search bar full width; footer links in four columns |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero banner expands to 350px with larger typography |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px on mobile
- Product cards have a minimum tap area of 120x180px
- Category tags and badges are at least 32px tall with 44px tap padding
- Navigation hamburger icon is 44x44px
- Pagination buttons are 40x40px minimum

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer for navigation links
- Product grid collapses from 4 columns to 1 column on mobile
- Footer link columns collapse from 4 to 1 on mobile
- Hero banner text reduces in size and padding on mobile
- Search bar collapses from full-width to an icon that expands on tap
- Category filter strip becomes horizontally scrollable on mobile
- Breadcrumbs truncate to show only the last two levels on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted font declarations were limited to Arial, Helvetica, and serif — the brand may use a custom web font (e.g., for headings) that wasn't captured in the extraction
- The extracted color palette is unusually large (30+ colors), suggesting many are from third-party widgets (social icons, payment buttons, stock images) rather than the brand's true design system
- Hover and active states for most components are inferred from common patterns rather than extracted from the live site
- Error states for form inputs (validation, error messages) were not captured
- Dark mode or high-contrast mode variants are not documented
- The brand's illustration style and iconography system are not captured
- Animation durations and easing curves are not documented
- Focus ring styles for accessibility were not extracted
- The specific shade of blue used for the logo may differ slightly from the extracted #003388
- Typography scale is inferred from common children's book publisher patterns rather than extracted measurements
- Spacing scale is estimated based on common web patterns rather than extracted from the live site
- The brand may use a secondary typeface for display headings that wasn't captured in the extraction
