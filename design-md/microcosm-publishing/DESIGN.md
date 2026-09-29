---
version: alpha
name: "Microcosm Publishing"
source_url: "https://microcosmpublishing.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A riot of hot pink #ed018c against near-black #111111 defines Microcosm Publishing's visual identity — a zine publisher that wears its DIY ethos on its sleeve. The primary pink, a shade that reads as both punk and playful, appears on category headers, sale badges, and primary buttons, while a supporting cast of electric yellow #e8f26e, cyan #8dd9f4, and coral #fd534d creates a palette that feels pulled from a risograph machine rather than a brand guidelines document. The site uses Impact for display headlines — a bold, condensed slab that screams "zine culture" — paired with Lato for body text, creating a deliberate tension between the aggressive and the readable. Navigation is utilitarian: a sticky top bar with dropdown menus, a prominent search field, and category links that use the full spectrum of accent colors. Product cards are simple white rectangles with soft shadows, letting the cover art do the heavy lifting. The footer is dense with links, social icons, and a newsletter signup, all contained within a #111111 band that grounds the page. The overall feel is that of a well-stocked indie bookstore's website — functional, colorful, and unapologetically niche.

colors:
  primary: "#ed018c"
  primary-active: "#c40075"
  primary-disabled: "#ffa2d8"
  ink: "#111111"
  body: "#444444"
  muted: "#777777"
  muted-soft: "#aaaaaa"
  hairline: "#c2cad0"
  hairline-soft: "#e5e7ea"
  canvas: "#ffffff"
  surface-soft: "#f5f9fd"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#e8f26e"
  accent-cyan: "#8dd9f4"
  accent-coral: "#fd534d"
  accent-blue: "#2d62c3"
  accent-teal: "#4ccfd2"
  accent-orange: "#e06901"
  accent-brown: "#846d56"
  accent-maroon: "#770000"
  accent-navy: "#344294"
  accent-lavender: "#ececfc"
  accent-sage: "#5892a8"
  accent-gold: "#edc945"
  accent-cream: "#fbf6d3"
  accent-dark-brown: "#463218"
  accent-tan: "#af9e81"
  accent-dark-teal: "#008888"
  accent-light-blue: "#5ea4d5"
  accent-dark-blue: "#276b9b"
  accent-light-gray: "#eeeeee"
  accent-medium-gray: "#808890"
  accent-dark-gray: "#669999"

typography:
  display-xl:
    fontFamily: "Impact, 'Arial Black', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "Impact, 'Arial Black', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Impact, 'Arial Black', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "Impact, 'Arial Black', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-lg:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0

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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 9px 13px
    height: 44px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-coral}"
    padding: 9px 13px
    height: 44px
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
    height: 44px
  search-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: 9px 19px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: 8px 0
  nav-dropdown-item:
    padding: 8px 16px
    hoverBackgroundColor: "{colors.surface-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: 12px
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: 12px
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1.5"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  category-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-sm}"
    padding: "16px 24px"
    rounded: "{rounded.sm}"
  category-header-alt:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    padding: "16px 24px"
    rounded: "{rounded.sm}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-lg}"
    padding: "48px 24px"
    minHeight: "300px"
  hero-banner-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "48px 24px"
    minHeight: "300px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "48px 24px 24px"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
    hoverColor: "{colors.canvas}"
  footer-heading:
    color: "{colors.canvas}"
    typography: "{typography.caption-bold}"
    textTransform: uppercase
    letterSpacing: "1px"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: "40px"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: "40px"
  social-icon:
    color: "{colors.muted-soft}"
    hoverColor: "{colors.canvas}"
    size: "24px"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    linkColor: "{colors.primary}"
    separatorColor: "{colors.hairline}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    activeColor: "{colors.primary}"
    activeBackgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    border: "1px solid {colors.hairline}"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  rating-stars:
    color: "{colors.accent-gold}"
    size: "16px"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: "1px"
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: "1px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with hot pink #ed018c and white text. Used for "Add to Cart", "Subscribe", and primary checkout actions. On hover, darkens to #c40075. Disabled state uses a lighter pink #ffa2d8. The button has a slight 4px rounded corner and uses Lato Bold at 16px with 0.5px letter spacing for a punchy, readable label.

**`button-secondary`** — An outlined button with a 2px solid black border on a white background. Used for secondary actions like "View Details" or "Learn More". On hover, the background fills with black and text inverts to white. Maintains the same 44px height and 4px rounding as the primary button for visual consistency.

**`button-accent-yellow`** — A high-visibility button using the electric yellow #e8f26e with black text. Used sparingly for "Sale" or "Limited Edition" CTAs where the hot pink would compete with other pink elements on the page. The yellow creates a distinct visual tier of urgency.

**`button-accent-coral`** — A coral #fd534d button with white text, used for "Clearance" or "Final Sale" actions. The coral sits between the primary pink and accent yellow on the urgency spectrum, signaling a serious discount without the aggressive tone of the primary pink.

**`button-text`** — A text-only button styled as a link but with button-like padding. Uses the primary pink for color and Lato Bold for weight. Used for "Read More" links within product descriptions and "View All" links in category sections.

### Navigation
**`nav-bar`** — A 60px white bar with a bottom border in #e5e7ea. Contains the site logo on the left, a full-width search input in the center, and navigation links on the right. Navigation links use Lato Bold at 15px with 0.3px letter spacing. On scroll, the bar gains a subtle box shadow and a stronger bottom border for depth.

**`nav-dropdown`** — A white dropdown panel with 8px rounding and a soft border. Each item has 8px vertical padding and 16px horizontal padding, with a light gray hover state. Used for category sub-menus and account navigation.

### Cards
**`product-card`** — A white card with a 1px soft border and 8px rounding. Contains a product image with a 1:1.5 aspect ratio, the title in Lato Bold at 16px, and the price in Lato Bold at 16px. On hover, the card gains a stronger border and a subtle box shadow. Badges (sale, new, featured) are positioned absolutely in the top-left corner of the image area.

**`product-card-badge`** — A small pill-shaped label in the primary pink with white text, 11px uppercase Lato Bold. Used for "Featured" or "Staff Pick" indicators. Variants include coral for "Sale" items and cyan for "New" arrivals, each with appropriate text contrast.

### Forms
**`text-input`** — A standard input field with a 1px hairline border, 4px rounding, and 10px 14px padding. On focus, the border thickens to 2px and turns primary pink. Error state uses a 2px coral border. All inputs maintain a consistent 44px height for alignment with buttons.

**`search-input`** — A pill-shaped search field with a light gray background (#f5f9fd) and a 1px hairline border. On focus, the background turns white and the border becomes a 2px primary pink ring. Used in the main navigation and on search result pages.

**`newsletter-input`** — A compact input field used in the footer, 40px tall with 8px 12px padding. Paired with a 40px primary pink submit button for a clean, aligned form row.

### Footer
**`footer`** — A dense black (#111111) footer band with white text. Contains multiple columns of links, social media icons, and a newsletter signup form. Links start at #aaaaaa and brighten to white on hover. Section headings use 12px Lato Bold with 1px letter spacing, uppercase, for clear hierarchy in the dark space.

### Badges & Tags
**`filter-tag`** — A pill-shaped filter chip with a light gray background and hairline border. Active state fills with primary pink and white text. Used on category and search result pages for filtering by format, topic, or price range.

**`rating-stars`** — Gold (#edc945) star icons at 16px, used on product cards and review sections. The gold provides a warm accent against the cooler primary palette.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack in 2-column grid; search input moves below logo; footer columns stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; search input remains in nav bar; footer columns arrange in 2x2 grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; search input in center of nav bar; footer columns in 4-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; additional whitespace on sides; larger hero banners |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height
- Navigation links have minimum 44px tap area even if text is smaller
- Filter tags have minimum 32px height with adequate padding
- Product card tap targets (title, image, button) are independently tappable with minimum 44x44px areas

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Product grid columns reduce from 4 to 3 to 2 to 1 as viewport narrows
- Footer columns collapse from 4 to 2 to 1
- Category filter sidebar collapses into a horizontal scrollable strip on mobile
- Hero banner text reduces in size and may stack vertically on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most interactive elements could not be reliably extracted from static CSS; hover colors are inferred from brand logic
- Error message styling (validation text, error icons, inline errors) not observed on the live site
- Loading states (spinners, skeleton screens, progress bars) not present in extracted data
- Dark mode or high-contrast mode variants not implemented
- Focus ring styles for keyboard navigation not observed
- Specific font weights for Lato (400, 700) are assumed; the live site may use additional weights (300, 900)
- The "Jonze" font family found in CSS may be a custom or third-party font; not included in typography due to lack of usage context
- Sub-brand or collection-specific color palettes (e.g., for specific book series) not documented
- Animation durations and easing curves not extracted
- Modal/dialog overlay styling not observed
- Tooltip and popover component styles not present
- The extracted color list includes many potential accent colors; the brand likely uses a smaller subset consistently — the full list is provided for reference but actual usage may vary
- Checkout flow styling (Shopify Pay, cart page) not captured
- Print stylesheet not analyzed
