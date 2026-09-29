---
version: alpha
name: "Bluestockings"
source_url: "https://www.bluestockings.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A cooperative bookstore that wears its politics on its sleeve, Bluestockings uses a deep institutional blue #003399 as its primary anchor — the color of a well-worn denim jacket or a vintage union button — against a warm off-white canvas #f4f4f4 that reads more like uncoated book paper than sterile digital white. The brand's typography splits between a proprietary Bluestockings Grotesk for display moments and Poppins across its full weight spectrum (Light through Black Italic) for body and interface text, giving the site a zine-like energy where bold Poppins Black headlines sit alongside light-weight captions without apology. The extracted palette is dominated by utilitarian blues and grays (#0078a8, #3388ff, #777777, #bbbbbb, #c3c3c3) with a single dark ink #222222, suggesting a system built for legibility and low overhead rather than visual flourish — the cooperative ethos made manifest in design. Signature moves include a persistent top nav that likely carries event listings and coalition partners, search treated as a utility rather than a hero feature, and a footer dense with links to mutual aid networks and reading lists. The site trusts its inventory photography and event posters to provide the color, keeping the chrome in a narrow band of blues and neutrals.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99bbee"
  ink: "#222222"
  body: "#333333"
  muted: "#777777"
  muted-soft: "#bbbbbb"
  hairline: "#c3c3c3"
  hairline-soft: "#dddddd"
  canvas: "#f4f4f4"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#0078a8"
  accent-bright: "#3388ff"

typography:
  display-xl:
    fontFamily: "'Bluestockings Grotesk', 'Poppins Black', 'Poppins', sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Bluestockings Grotesk', 'Poppins Bold', 'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Bluestockings Grotesk', 'Poppins Bold', 'Poppins', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins Bold', 'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins Bold', 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  caption-uppercase:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins Bold', 'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Poppins Bold', 'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Poppins Bold', 'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px

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
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 4px 0px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    borderColor: "{colors.accent-bright}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
  badge-event:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  section-heading:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
  event-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in deep blue #003399 with white text and a subtle 4px corner radius. On hover, the background deepens to #002277. Disabled state fades to a pale blue #99bbee. Used for "Add to Cart", "RSVP", and "Donate" actions. The bold Poppins weight and 0.5px letter-spacing give it a printed-poster feel.

**`button-secondary`** — An outlined variant on the warm canvas background, using the primary blue for text and a 1px hairline border (implied by the canvas background). Active state shifts to a soft surface background. Used for "Learn More" and "Browse Events" links where primary would be too heavy.

**`button-link`** — A text-only button with no background or border, styled as an inline link in the primary blue. Used for "Read More" and "View All" actions within content sections.

### Text Inputs
**`text-input`** — A clean white input field on the canvas background, with 12px vertical padding and 16px horizontal. Focus state shows a primary blue border. Error state uses the bright accent blue #3388ff as a border color, signaling a validation issue without the alarm of red. The Poppins body weight keeps form filling comfortable.

### Navigation
**`nav-bar`** — A 64px tall bar on the warm canvas background, carrying links in Poppins semibold at 14px. Active links render in the primary blue; inactive links in muted gray #777777. The nav likely includes "Books", "Events", "About", "Shop", and "Donate" — reflecting the cooperative's dual mission as bookstore and community space.

**`nav-link-active`** — Active state for navigation items, using the primary blue to indicate the current section. No background fill — the color change alone signals location.

**`nav-link-inactive`** — Inactive navigation items in muted gray, reducing visual noise while remaining legible.

### Search
**`search-bar`** — A compact 40px tall search input with an 8px corner radius, rendered on a white card background. The placeholder text sits in muted gray, and the input uses Poppins body-sm for readability. Positioned as a utility in the nav bar rather than a hero element.

### Cards
**`product-card`** — A white card with a subtle 4px corner radius, containing a product image, title in Poppins Bold at 16px, and price in Poppins regular at 16px. The card has no shadow or border — it relies on the contrast between the white surface and the warm canvas background for separation.

**`product-card-image`** — The product image within a card, sharing the same 4px corner radius as the card itself. No rounded corners on the bottom — the image sits flush with the card's top edge.

**`product-card-title`** — The book title in Poppins Bold at 16px, using the dark ink #222222 for maximum legibility.

**`product-card-price`** — The price in Poppins regular at 16px, using the body color #333333.

### Badges
**`badge-event`** — A small, tight badge in the accent blue #0078a8 with white text, using 2px vertical padding and 8px horizontal. The 2px corner radius and 11px bold Poppins make it read as a printed sticker. Used for "In-Store", "Virtual", or "Workshop" labels on event cards.

**`badge-sale`** — A primary blue badge with white text, using the same dimensions as the event badge. Used for "Sale", "New Arrival", or "Staff Pick" labels on product cards.

### Footer
**`footer-section`** — A dark footer in the deep ink #222222 with white text, carrying links in the soft muted gray #bbbbbb. The footer likely includes sections for "Hours & Location", "Newsletter Signup", "Mutual Aid Partners", and "Social Media". The dark background creates a visual bookend to the warm canvas of the main content.

**`footer-link`** — Footer links in Poppins regular at 14px, rendered in the soft muted gray to reduce contrast against the dark background. Hover state would shift to white (not extracted but assumed).

### Hero
**`hero-section`** — A full-width hero on the warm canvas background, using the display-xl typography (36px Bluestockings Grotesk or Poppins Black) for the main headline. No background color other than the canvas — the hero relies on typography and event photography for visual impact.

### Section Headings
**`section-heading`** — A 28px heading in Bluestockings Grotesk or Poppins Bold, using the dark ink color. Used for "Featured Books", "Upcoming Events", and "Our Mission" section titles. The slightly negative letter-spacing gives it a compressed, poster-like quality.

### Event Cards
**`event-card`** — A white card with a 4px corner radius, containing an event image, date, title, and description. Uses Poppins body-sm for the description and title-sm for the event name. The card stacks vertically on mobile and grids on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; event cards full-width; search bar hidden behind icon; footer links stack |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; event cards in 2-column grid; search bar visible as compact input; footer in 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; event cards in 3-column grid; search bar full width in nav; footer in 3-column layout with newsletter signup |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid expands to 4 columns; event cards in 4-column grid; additional whitespace on sides |

### Touch Targets
- All buttons and links maintain a minimum 44px height for touch accessibility
- Nav bar links have 48px tap targets (64px bar height provides ample padding)
- Search bar has 40px height — slightly below the 44px recommendation but acceptable for a utility element
- Product card images are tappable with full card width as the hit area
- Footer links have 44px minimum tap targets with adequate spacing between rows

### Collapsing Strategy
- Top nav collapses to a hamburger menu on mobile (below 744px)
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Event card grid follows the same collapse pattern as product cards
- Search bar collapses to an icon-only trigger on mobile, expanding to a full-width overlay when activated
- Footer sections collapse from 3 columns to 2 (tablet) to a single stack (mobile)
- Category or filter strips (if present) collapse to a horizontal scroll on mobile rather than a dropdown

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for footer links (assumed white on dark background but not extracted)
- Error message styling for forms (only border color extracted, not the message typography or background)
- Active/visited states for text links (not present in extracted data)
- Dropdown menu styling for nav (if the site uses mega-menus or simple dropdowns)
- Modal or overlay styling for search expansion on mobile
- Pagination styling for product lists
- Star rating or review component styling (not present on the site)
- Dark mode or high-contrast mode variants
- Print stylesheet behavior
- The extracted color palette is heavily weighted toward blues and grays — the brand's true primary (#003399) is distinctive but the supporting palette is generic. The accent blue #0078a8 and bright blue #3388ff may be widget colors rather than intentional brand tokens. The warm canvas #f4f4f4 is the most characterful non-primary color in the set.
- Font stack order is inferred — "Bluestockings Grotesk" appears as a .woff2 file, and Poppins variants appear with `!important` flags in the CSS, suggesting a system where Poppins is the reliable fallback and the Grotesk is the display preference.
