---
version: alpha
name: "Books Are Magic"
source_url: "https://www.booksaremagic.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Brooklyn independent bookstore that uses a restrained palette of #0078a8 as its sole accent voltage — a deep, confident teal that appears on the primary navigation bar, the shopping-cart icon, and the footer background, while everything else stays in a grayscale of #222222, #777777, and #f4f4f4. The site runs Radikal, a Swiss-style sans-serif with seven weights from Light to Black Italic, giving the typography a sharp editorial clarity that feels more like a literary magazine than a retail storefront. Headlines sit in Radikal Black at generous sizes with tight tracking, while body copy uses Radikal Light for a surprising airiness — the brand trusts its book covers and event photography to carry emotional weight rather than relying on decorative type or illustration. The navigation is a single horizontal bar with dropdown menus for events and books, using {rounded.none} corners throughout except for the search bar which takes {rounded.full} pill shape and a subtle {colors.hairline} border. Product cards for books show cover art, title, author, and price in a clean three-column grid with {rounded.sm} corners on images and no box shadows — the covers themselves provide all the visual texture. The footer uses the teal #0078a8 as a full background with white text, creating a clear terminal signal that the page has ended. There are no badges, no sale flags, no star ratings — the design assumes visitors already know what they want or are willing to browse without persuasion.

colors:
  primary: "#0078a8"
  primary-active: "#005f8a"
  primary-disabled: "#b3d4e3"
  ink: "#222222"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#999999"
  hairline: "#c3c3c3"
  hairline-soft: "#d9d9d9"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  footer-bg: "#0078a8"
  footer-text: "#ffffff"
  link: "#0078a8"
  link-hover: "#005f8a"
  event-badge: "#3388ff"

typography:
  display-xl:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 900
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  author:
    fontFamily: "'Radikal', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 300
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
    rounded: "{rounded.none}"
    padding: 12px 28px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 27px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    height: 56px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-hover:
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-active:
    borderColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.author}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.hairline}"
  event-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  event-card-date:
    typography: "{typography.caption}"
    textColor: "{colors.primary}"
    fontWeight: 700
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.base}"
  page-section:
    padding: "{spacing.section} {spacing.lg}"
  section-heading:
    typography: "{typography.display-md}"
    marginBottom: "{spacing.lg}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  cart-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
  cart-icon-count:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px

## Components

### Buttons
**`button-primary`** — Solid teal (#0078a8) rectangle with uppercase Radikal Bold text in white. No border radius — the sharp corners reinforce the editorial Swiss aesthetic. On hover, darkens to #005f8a. Disabled state uses a desaturated light teal (#b3d4e3) with white text. Used for primary actions: "Add to Cart," "RSVP," "Subscribe."

**`button-secondary`** — White background with #222222 text and a 1px #c3c3c3 border. Same uppercase Radikal Bold treatment as primary. Hover fills the background with #f4f4f4. Used for secondary actions like "View Details" or "Learn More."

### Navigation
**`nav-bar`** — Full-width white bar at 64px height containing the store logo on the left and navigation links on the right. Links use Radikal Bold uppercase at 15px with 0.3px letter-spacing. On scroll, the bar shrinks to 56px and the background switches to teal (#0078a8) with white text — a dramatic transition that signals the user has entered the browsing experience. The logo remains in its original weight regardless of scroll state.

**`nav-link`** — Inline uppercase links with 8px horizontal padding. Hover state changes text color to teal (#0078a8). Active page uses teal text and a 2px bottom border in teal. No dropdown chevrons — the site uses simple expandable menus triggered on click.

### Search
**`search-bar`** — Pill-shaped input field with white background, 1px #c3c3c3 border, and Radikal Light 16px placeholder text. The pill shape is the only rounded element in the entire system, creating a deliberate visual contrast against the otherwise rectilinear design. Focus state swaps the border to teal (#0078a8). Includes a magnifying glass icon in #777777 on the left.

### Product Cards
**`product-card`** — Minimal book display with no card background or border — just the book cover image, title, author, and price stacked vertically. The cover image has 8px rounded corners ({rounded.sm}) while the text sits flush left. Title uses Radikal Bold 18px, author in Radikal Light 13px #777777, price in Radikal Regular 14px #222222. No hover effects, no add-to-cart button visible until the user clicks into the product detail page. The grid uses 3 columns on desktop, 2 on tablet, 1 on mobile.

### Footer
**`footer`** — Full teal (#0078a8) background section with white text, 48px vertical padding. Contains three columns: store information, quick links, and newsletter signup. Links use Radikal Regular 15px with hover state lightening to #c3c3c3. The newsletter input matches the search bar pill shape but with a white border and teal background — the only place where the color scheme inverts.

### Event Cards
**`event-card`** — Light gray (#f4f4f4) background rectangle with no border radius. Contains the event date in teal Radikal Bold 13px, event title in Radikal Bold 18px, and a short description in Radikal Light 14px #444444. A "RSVP" button sits at the bottom right. Events are listed in a single column with generous 24px spacing between cards.

### Hero Section
**`hero-section`** — Light gray (#f4f4f4) background section with 64px vertical padding. Contains a large headline (Radikal Black 40px), a subheading in Radikal Light 16px #777777, and optional CTA button. No background image — the hero relies on typographic weight and whitespace. Used on the homepage and category landing pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero font drops to 28px; footer stacks to single column; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but with reduced padding; hero font at 32px; footer shows two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 40px; footer three columns |
| Wide | > 1440px | Max-width container at 1280px centered; product grid remains three columns but with wider gutters |

### Touch Targets
- All buttons and links maintain minimum 44px tap target height
- Navigation links have 48px minimum tap area on mobile
- Search bar height stays at 44px across all breakpoints
- Cart icon button is 36px with 44px touch padding on mobile

### Collapsing Strategy
- Navigation collapses to hamburger icon below 744px
- Product grid reduces columns as viewport shrinks (3 → 2 → 1)
- Footer columns stack vertically below 744px
- Hero section reduces padding from 64px to 32px on mobile
- Search bar moves from inline nav position to full-width below nav on mobile
- Event cards remain single column at all breakpoints but reduce padding on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs could not be reliably extracted — assumed teal border on focus based on brand color usage
- Error states for forms (validation, required fields) not observed on live site
- Dropdown menu styling for navigation sub-items not captured — likely uses simple white overlay with text links
- Mobile hamburger menu animation and overlay behavior not documented
- Product detail page layout (single book view with description, reviews, etc.) not fully extracted
- Checkout flow styling not available — site uses external payment processing
- Dark mode not supported by the brand
- Sub-brand or seasonal color variations not observed
- Loading states and skeleton screens not present on current site
- Print stylesheet behavior unknown
- Accessibility focus indicators not verified — assumed default browser outlines
- Newsletter confirmation/error states not captured
