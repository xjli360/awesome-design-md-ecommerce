---
version: alpha
name: "Tender Leaf Toys"
source_url: "https://tenderleaftoys.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A wooden-toy brand that paints with a meadow palette — #108474 as the deep forest-green anchor, #b3c636 as the bright leaf-green accent, and #ffd600 as the dandelion-yellow that pops on add-to-cart buttons and sale badges. The site runs on Shopify with a light, airy canvas of #f9fafb and #ffffff, using soft gray borders (#dedede) and muted text (#555555) to keep the focus on product photography. Typography leans on Nunito Sans for headings and body text, with Red Hat Text as a secondary face — both rounded, friendly sans-serifs that match the soft, safe feel of the toys themselves. Product cards use generous whitespace and subtle shadows, with rounded corners at {rounded.md} for the card and {rounded.sm} for the thumbnail, creating a grid that feels like blocks on a nursery floor. The brand avoids hard edges: buttons are pill-shaped at {rounded.full}, category tags are soft rectangles at {rounded.sm}, and the footer stacks information in a warm, uncluttered layout. A secondary palette of pastels (#b5e0fa, #c1e6e6, #a89cc8) appears in seasonal banners and collection highlights, suggesting a brand that rotates its visual energy without losing its earthy core. The overall impression is of a clean, Scandinavian-leaning toy store where the wood grain and the white space do the selling.

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#a3d4c5"
  ink: "#383838"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-leaf: "#b3c636"
  accent-yellow: "#ffd600"
  accent-yellow-dark: "#f5c446"
  accent-sky: "#b5e0fa"
  accent-mint: "#c1e6e6"
  accent-lavender: "#a89cc8"
  star-rating: "#ffd600"
  sale-badge: "#fbcd0a"
  footer-bg: "#edf5f5"
  footer-text: "#6b7e86"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-lg:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Nunito Sans', 'Red Hat Text', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.full}"
    padding: 12px 28px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-accent-leaf:
    backgroundColor: "{colors.accent-leaf}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-add-to-cart:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 56px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
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
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.primary}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginBottom: "{spacing.base}"
  social-icon:
    color: "{colors.footer-text}"
    height: 24px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: "14px 36px"
  collection-grid:
    gap: "{spacing.lg}"
    padding: "{spacing.section} {spacing.xl}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Shop Now", "View Collection", and primary navigation links. Rendered as a pill-shaped button with a deep forest-green background ({colors.primary}) and white text. On hover, shifts to a darker green ({colors.primary-active}) for a subtle depth cue. The disabled state uses a muted green ({colors.primary-disabled}) to indicate inactivity without visual noise.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "Read Reviews". Uses a white background with a 2px solid border in {colors.primary} and green text. Maintains the same pill shape and height as the primary button for consistent rhythm in button groups.

**`button-accent-yellow`** — A high-energy variant reserved for promotional banners, sale sections, and limited-time offers. Uses {colors.accent-yellow} background with dark ink text ({colors.ink}) to create maximum contrast against the white canvas. The bright yellow signals urgency and playfulness without resorting to red.

**`button-accent-leaf`** — A secondary accent button using {colors.accent-leaf} for collection highlights, seasonal categories, or "New Arrivals" badges. The leaf-green pairs naturally with the primary forest-green, creating a cohesive botanical hierarchy.

**`button-add-to-cart`** — The most important conversion element on product pages. Slightly taller (56px) than standard buttons, uses the high-contrast yellow background ({colors.accent-yellow}) with larger bold text ({typography.button-lg}) and softer rounded corners ({rounded.sm}) rather than full pills. This subtle shape difference helps it stand out from other page buttons.

### Cards
**`product-card`** — The primary product display unit in collection grids and search results. A white card with medium rounded corners ({rounded.md}) and 16px padding. The product image sits at the top with smaller rounded corners ({rounded.sm}) and a 1:1 aspect ratio. Below, the title uses {typography.title-sm} with 8px top margin, and the price appears in {typography.price} colored in {colors.primary} to draw the eye. Cards have a subtle box-shadow on hover for lift.

**`category-tag`** — Used for filtering and browsing by toy type (e.g., "Puzzles", "Dolls", "Vehicles"). A soft gray pill with muted text, active state flips to {colors.primary} background with white text. These tags appear in horizontal scrollable strips above collection grids.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with white background. Contains the brand logo on the left, main navigation links in the center (using {typography.nav-link}), and utility icons (search, account, cart) on the right. The active link state is indicated by a 2px bottom border in {colors.primary}. On mobile, the nav collapses into a hamburger menu with a full-screen overlay drawer.

### Forms
**`text-input`** — Standard input field for newsletter signups, search, and account forms. White background with a 1px {colors.hairline} border and soft rounded corners ({rounded.sm}). On focus, the border thickens to 2px and turns {colors.primary} for clear active state feedback. Padding is generous at 12px vertical / 16px horizontal for comfortable touch targets.

**`newsletter-input`** — A specialized input for the email signup form in the footer. Uses full pill rounding ({rounded.full}) to match the adjacent submit button, creating a seamless, unified bar. The input and button sit side by side in a flex row, visually appearing as a single rounded element.

### Footer
**`footer-section`** — A warm, mint-tinted footer background ({colors.footer-bg}) with muted teal text ({colors.footer-text}) for a calm, trustworthy closing to the page. Contains columns for customer service, about links, social icons, and the newsletter signup. Headings use {typography.title-sm} in dark ink ({colors.ink}) for clear hierarchy. Social media icons use the footer text color and sit at 24px height.

### Badges
**`sale-badge`** — A small, high-visibility badge for discounted items. Uses a bright yellow-gold background ({colors.sale-badge}) with dark text, uppercase bold typography ({typography.badge}), and soft rounded corners ({rounded.sm}). Positioned in the top-left corner of product card images.

### Hero
**`hero-banner`** — Full-width promotional sections at the top of landing pages and collection pages. Uses the light canvas background ({colors.canvas}) with large display typography ({typography.display-lg}) and a prominent CTA button ({colors.primary}). The hero may feature a full-bleed product photograph with overlaid text, or a split layout with image on one side and text on the other.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes single-column (1 col); hero banner stacks vertically; footer columns stack; search bar becomes icon-only; category tags scroll horizontally with no wrap |
| Tablet | 744–1128px | Nav links remain visible but condensed; product grid shows 2 columns; hero maintains split layout but reduces padding; footer shows 2-column grid; search bar expands on tap |
| Desktop | 1128–1440px | Full nav with all links; product grid shows 3–4 columns; hero uses full split layout with generous padding; footer shows 3–4 columns; search bar always visible |
| Wide | > 1440px | Max-width container (1440px) centered; product grid shows 4 columns; hero padding increases to maintain visual balance; all elements scale proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Product card tap targets (title, image, add-to-cart) are at least 48px tall
- Category tags in horizontal scroll strips are 40px tall with 16px horizontal padding
- Nav bar icons (search, account, cart) are 44x44px tap areas
- Newsletter input and button are both 48px tall for easy one-handed tapping

### Collapsing Strategy
- Main navigation collapses to hamburger menu below 744px, with full-screen overlay drawer
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Footer columns collapse from 4 to 2 to 1, stacking vertically on mobile
- Hero banner switches from side-by-side to stacked layout below 744px
- Category filter strip becomes horizontally scrollable with hidden overflow on mobile
- Search bar collapses to icon-only on mobile, expanding to full input on tap
- Product page layout (image + details side by side) stacks vertically below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components (buttons, cards, links) are inferred from common patterns, not extracted from live CSS
- Error state styling for forms (validation messages, error borders) not observed
- Dark mode or high-contrast mode not present on the live site
- Sub-brand or seasonal palette variations (holiday, birthday, etc.) not documented
- Animation and transition timing values (hover transitions, page loads, drawer animations) not extracted
- Modal/dialog styling (quick-view, cart drawer, age-verification) not observed
- Loading states (skeleton screens, spinners) not documented
- The extracted font list includes JudgemeIcons and JudgemeStar — these are review-widget icon fonts, not brand typography
- Social icon colors (#3b5998 Facebook blue, #1da1f2 Twitter blue) are platform defaults, not brand choices
- The extracted hex list is heavily weighted toward grays and neutrals — the brand's true accent palette (leaf green, yellow, sky blue, mint, lavender) was identified by selecting the most distinctive non-gray colors from the extraction
