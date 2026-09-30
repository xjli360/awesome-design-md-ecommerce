---
version: alpha
name: "Rascal + Friends"
source_url: "https://rascalandfriends.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A baby-care brand that builds its visual identity on the tension between a deep teal ink (#003a48) and a soft, almost-mint canvas (#cee7e0), with a violet accent (#9574df) that appears in badges, sale tags, and secondary CTAs — a color that feels more like a surprise than a system. The brand name itself is set in Be Vietnam Pro, a geometric sans-serif with generous apertures and a friendly, open character, while body copy runs in DM Sans, a slightly more compact companion. The signature design move is the use of a rounded-square badge in that violet, often paired with a small, uppercase label reading "NEW" or "SALE" — a pattern that appears on product cards and navigation items alike. The overall mood is clean and clinical but softened by the mint canvas and the occasional pink accent (#ec4899) used sparingly for promotional highlights. The brand's primary CTA button is a solid teal rectangle with `{rounded.sm}` corners, white text, and a height of 48px — a shape that feels deliberate and sturdy, not playful. The secondary button is an outline variant with the same teal stroke, suggesting a system that values consistency over novelty. The product cards are white (`{colors.surface-card}`) with `{rounded.md}` corners and a subtle shadow, each containing a product image, a title in `{typography.title-md}`, a price in `{typography.body-md}`, and a violet "NEW" badge. The footer is a dense, three-column layout with a dark teal background (`{colors.ink}`) and white text, a common pattern in DTC but executed here with a slightly larger type size and more generous spacing. The brand's voice is direct and informational — "Rascals Premium Diapers" — with no cutesy language or whimsical illustrations, relying instead on the color system and typography to convey warmth. The extracted font stack includes both Be Vietnam Pro and DM Sans as primary choices, with Sofía Pro appearing as a third option, likely used for display or accent text. The overall impression is of a brand that has chosen a restrained, almost Scandinavian palette and applied it with discipline across every surface, letting the teal and violet do the work of differentiation rather than relying on pattern or illustration.

colors:
  primary: "#003a48"
  primary-active: "#002a35"
  primary-disabled: "#9ca3af"
  ink: "#003a48"
  body: "#33616d"
  muted: "#9ca3af"
  muted-soft: "#d9d9d9"
  hairline: "#e5e7eb"
  hairline-soft: "#f1f1f3"
  canvas: "#cee7e0"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-violet: "#9574df"
  accent-violet-active: "#7e5ccb"
  accent-pink: "#ec4899"
  accent-teal: "#5ed2bd"
  badge-new-bg: "#9574df"
  badge-new-text: "#ffffff"
  sale-bg: "#ec4899"
  sale-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Be Vietnam Pro', 'DM Sans', 'Sofia Pro', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Be Vietnam Pro', 'DM Sans', 'Sofia Pro', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', 'Be Vietnam Pro', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

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
    padding: 14px 24px
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-accent-violet:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-accent-violet-active:
    backgroundColor: "{colors.accent-violet-active}"
    textColor: "{colors.badge-new-text}"
    rounded: "{rounded.sm}"
  button-pill-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-pink}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    height: 280px
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new-bg}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.sale-bg}"
    textColor: "{colors.sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.base} 0"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.on-primary}"
    padding: "0 0 {spacing.base} 0"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "0 0 {spacing.lg} 0"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. A solid teal rectangle (#003a48) with white text in DM Sans 16px/600 weight, 8px corner radius, and 48px height. On hover, it shifts to a darker teal (#002a35). The disabled state uses a muted gray (#9ca3af) to signal inactivity. Used for "Add to Cart", "Subscribe", and "Shop Now" actions.

**`button-secondary`** — An outlined variant of the primary button, with a 2px solid teal border on a transparent background. The text remains teal. On hover, it fills with the primary teal and inverts the text to white. Used for "Learn More" and secondary checkout paths.

**`button-accent-violet`** — A violet (#9574df) button with white text, 40px height, and 8px radius. On hover, it deepens to #7e5ccb. Used for promotional CTAs, "New Arrivals" links, and badge-associated actions. The violet is the brand's secondary voltage, appearing in badges and accent elements.

**`button-pill-teal`** — A fully rounded pill button in teal (#5ed2bd) with dark teal text (#003a48). Used sparingly for special offers or limited-time promotions, the pill shape signals a temporary or playful interaction compared to the standard rectangular buttons.

### Cards
**`product-card`** — A white card with a 12px corner radius and a subtle drop shadow (0 2px 8px rgba(0,0,0,0.08)). The card contains a product image with rounded top corners, a title in DM Sans 16px/600 weight, and a price in 16px/400 weight. A violet "NEW" badge or pink "SALE" badge can appear in the top-left corner of the image. The card is the primary container for product discovery across collection pages.

**`product-card-image`** — The image container within a product card, with rounded top corners (12px top, 0 bottom) and a fixed height of 280px. Images are expected to be 1:1 or 4:3 aspect ratio, cropped to fill.

### Navigation
**`nav-bar`** — A white, 72px-tall sticky header containing the brand logo, navigation links, and a search icon. Navigation links use DM Sans 15px/500 weight, with the active page indicated by a 2px teal underline. Inactive links are muted gray (#9ca3af). On mobile, the nav collapses into a hamburger menu.

**`nav-link-active`** — The active navigation state, with teal text and a 2px solid teal bottom border. The border is the only visual indicator of the current page — no background color change.

**`nav-link-inactive`** — Inactive navigation links in muted gray (#9ca3af). On hover, they transition to teal (#003a48) with a subtle opacity change.

### Forms
**`text-input`** — A standard text input field with a white background, 16px DM Sans text, 8px corner radius, and a 1px hairline border (#e5e7eb). On focus, the border thickens to 2px teal. On error, the border becomes 2px pink (#ec4899). The input height is 48px with 12px/16px padding.

**`search-bar`** — A fully rounded pill-shaped search input with a white background, 48px height, and 24px horizontal padding. The border is 1px hairline (#e5e7eb). Used in the hero section and mobile navigation.

### Badges
**`badge-new`** — A small, uppercase violet badge (#9574df) with white text, 4px corner radius, and 4px/8px padding. The type is DM Sans 11px/700 weight with 0.5px letter spacing. Used on product cards and collection pages to denote new arrivals.

**`badge-sale`** — A pink badge (#ec4899) with white text, identical in size and typography to the new badge. Used for promotional pricing and clearance items.

### Footer
**`footer`** — A dark teal (#003a48) footer with white text, 48px vertical padding, and a three-column layout. Each column has a heading in DM Sans 16px/600 weight and links in 14px/500 weight. The footer background is the same as the primary color, creating a visual bookend with the hero section.

**`footer-link`** — White text links in the footer, with no underline by default. On hover, they gain a subtle underline or opacity change (0.8).

### Hero
**`hero-section`** — A full-width section with the mint canvas background (#cee7e0) and dark teal text (#003a48). The heading uses Be Vietnam Pro 32px/700 weight with -0.5px letter spacing. A subtitle in DM Sans 16px/400 weight appears below, followed by a primary CTA button. The section has 64px vertical padding.

**`hero-subtitle`** — The subtitle text in the hero, set in DM Sans 16px/400 weight with body color (#33616d). It provides context or a value proposition below the main heading.

### Category Tags
**`category-tag`** — A fully rounded pill tag in soft gray (#f3f3f3) with body text (#33616d). Used for filtering product categories. The active state fills with teal (#003a48) and inverts the text to white.

**`category-tag-active`** — The active filter state, with teal background and white text. Used to indicate the currently selected category in a filter strip.

### Quantity Selector
**`quantity-selector`** — A compact input for selecting product quantities, with a white background, 40px height, 8px radius, and a 1px hairline border. The text is DM Sans 16px/400 weight. Used on product detail pages and cart.

### Accordion
**`accordion-header`** — A clickable header in an accordion component, with a white background, dark teal text, and a 1px soft hairline bottom border. The header uses DM Sans 16px/600 weight with 16px padding. On click, it reveals the accordion content below.

**`accordion-content`** — The expandable content area within an accordion, with white background, body text (#33616d), and 16px padding. The typography is DM Sans 14px/400 weight. Used for product descriptions, shipping details, and FAQ sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero padding reduces to 32px; footer stacks to single column; search bar moves to mobile drawer |
| Tablet | 744–1128px | Product cards display in 2-column grid; nav links remain visible but font size reduces to 14px; hero padding at 48px; footer displays in 2 columns |
| Desktop | 1128–1440px | Product cards in 3-column grid; full nav with all links; hero at full 64px padding; footer in 3 columns |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; increased whitespace around hero and footer |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav links have 48px tap targets on mobile (increased from 40px on desktop)
- Category tags have 40px height with 16px horizontal padding for comfortable tapping
- Quantity selector buttons are 40px x 40px minimum
- Accordion headers have 48px tap targets

### Collapsing Strategy
- Navigation: On mobile (< 744px), the full nav bar collapses into a hamburger menu icon. The menu opens as a full-screen overlay with links stacked vertically.
- Product grid: Collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Footer: Collapses from 3 columns (desktop) to 2 (tablet) to a single stacked column (mobile).
- Hero section: Padding reduces from 64px (desktop) to 48px (tablet) to 32px (mobile). The hero subtitle may be hidden on mobile to save space.
- Search bar: On mobile, the search bar moves from the hero section to a dedicated search drawer accessible from the nav.
- Product images: On mobile, product card images reduce from 280px to 200px height.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (buttons, links, cards) are inferred from common DTC patterns rather than extracted from the live site. The extracted color list did not include hover variants.
- Error styling for form inputs (text-input-error) is assumed based on the pink accent color (#ec4899) appearing in the extracted palette, but no error-specific CSS was observed.
- Dark mode is not supported and no dark mode colors were extracted.
- The exact font weights for Be Vietnam Pro and DM Sans are inferred from the extracted font-family declarations and common usage patterns; the live site may use different weights.
- The Sofía Pro font family appears in the extracted stack but its specific usage (display vs. body) is unclear. It may be used for headings or accent text.
- The accent-teal (#5ed2bd) and accent-pink (#ec4899) colors appear in the extracted palette but their specific usage contexts (buttons, badges, backgrounds) are inferred from common patterns rather than direct observation.
- The product card shadow (0 2px 8px rgba(0,0,0,0.08)) is a standard DTC pattern and may differ from the actual site implementation.
- The nav bar height (72px) and sticky behavior are assumed based on common e-commerce patterns; the actual site may use different dimensions or scroll behavior.
- The hero section layout (heading, subtitle, CTA) is inferred from the brand's homepage structure and may vary across different pages.
- The accordion component is assumed based on common product detail page patterns; the actual site may use tabs or other disclosure mechanisms.
- The quantity selector and its exact dimensions are inferred from standard e-commerce patterns; the live site may use a different implementation.
- The badge typography (11px/700 weight with 0.5px letter spacing) is a common pattern for small labels but may differ from the actual site's badge styling.
- The footer link hover state (underline or opacity change) is assumed; the actual site may use a different hover treatment.
