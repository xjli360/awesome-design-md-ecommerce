---
version: alpha
name: "Messermeister"
source_url: "https://www.messermeister.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Messermeister speaks in the language of professional-grade precision, a brand that equips both serious home cooks and career chefs with tools built to last a lifetime. The palette is anchored by a deep, almost-black ink (`#090a0f`) and a warm off-white canvas (`#f7f6f2`), creating a high-contrast stage for product photography. The signature voltage comes from a crisp, technical blue (`#00a4e4`) that appears in primary actions, hover states, and select accents, supported by a secondary steel-blue (`#338fb1`) and a cooler accent (`#00b3ff`). The system relies on a restrained neutral scale: body text sits at a dark charcoal (`#231f20`), muted elements at a mid-gray (`#4a5764`), and hairlines at a soft silver (`#c1c9d1`). Typography is a blend of the geometric, modern Founders Grotesk for display and headings, paired with the highly legible, humanist Inter for body text and UI — a combination that feels both editorial and utilitarian. The brand's design moves are deliberate and tactile: generous whitespace, sharp but not harsh corners (`{rounded.sm}` for buttons, `{rounded.md}` for cards), and a heavy reliance on high-resolution product imagery over decorative flourishes. The overall mood is one of quiet authority — the interface gets out of the way, letting the forged steel, wood grain, and craftsmanship of the knives speak.

colors:
  primary: "#00a4e4"
  primary-active: "#1990c6"
  primary-disabled: "#a7a9ac"
  ink: "#090a0f"
  body: "#231f20"
  muted: "#4a5764"
  muted-soft: "#777777"
  hairline: "#c1c9d1"
  hairline-soft: "#dedede"
  canvas: "#f7f6f2"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-new: "#00b3ff"
  badge-sale: "#5a5047"
  star-rating: "#090a0f"
  scrim: "#000000"
  footer-bg: "#090a0f"
  footer-text: "#a7a9ac"

typography:
  display-xl:
    fontFamily: "'Founders Grotesk', 'FoundersGrotesk-Medium', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.10
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Founders Grotesk', 'FoundersGrotesk-Medium', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Founders Grotesk', 'FoundersGrotesk-Medium', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Founders Grotesk', 'FoundersGrotesk-Regular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Founders Grotesk', 'FoundersGrotesk-Medium', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0
  body-lg:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Inter', 'Inter var', 'InterVariable', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.20
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
    padding: 14px 32px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
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
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(9,10,15,0.08)"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: "600px"
  hero-banner-overlay:
    backgroundColor: "rgba(9,10,15,0.35)"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 40px"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.nav-link}"
    textColor: "{colors.canvas}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.footer-text}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
  accordion-trigger:
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "0 {spacing.lg} {spacing.lg}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.body}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and key conversion points. Rendered on the signature blue (`{colors.primary}`) with white text and an 8px radius. On hover, it shifts to a deeper steel blue (`{colors.primary-active}`). The disabled state uses a muted gray (`{colors.primary-disabled}`) to signal inactivity. The button includes a subtle uppercase label for a more authoritative feel.

**`button-secondary`** — A high-contrast outlined button for secondary actions like "View Details" or "Learn More". Uses a white fill with a 2px solid ink (`{colors.ink}`) border. On hover, the fill and text invert to the dark ink tone, providing a tactile state change. Padding is adjusted by 1px to account for the border.

**`button-tertiary`** — A text-only button for less prominent actions, such as "Cancel" or "Clear". Uses the primary blue for text color on a transparent background, keeping the interface clean and reducing visual noise.

### Cards
**`product-card`** — The core product display unit, used on collection pages and search results. A white card (`{colors.surface-card}`) with a 12px radius. The image sits flush to the top corners, with the radius applied only to the top edges (`{rounded.md} {rounded.md} 0 0`). The title uses `{typography.title-sm}` and the price uses `{typography.body-md}`. A small badge (`{product-card-badge}`) can overlay the image for "New" or "Sale" indicators.

### Navigation
**`nav-bar`** — The primary site header, fixed at 72px tall on a white canvas. Navigation links use `{typography.nav-link}` in uppercase for a clean, professional look. On scroll, a subtle box shadow (`0 2px 8px rgba(9,10,15,0.08)`) is applied to create depth. The search bar is integrated as a pill-shaped input (`{rounded.full}`) within the nav.

### Forms
**`text-input`** — Standard text input for forms (search, account, checkout). A white background with a 1px hairline border (`{colors.hairline}`) and 8px radius. On focus, the border thickens to 2px and switches to the primary blue (`{colors.primary}`) for clear visual feedback.

**`select-input`** — Dropdown selectors, styled identically to text inputs for consistency. Used for filtering products (e.g., "Sort by", "Size") and in checkout forms.

### Footer
**`footer`** — A full-width, dark section anchored by the deep ink (`{colors.footer-bg}`). Text is set in a muted gray (`{colors.footer-text}`) for readability without strain. Headings use the uppercase nav-link style in white (`{colors.canvas}`). Links have a hover state that transitions to white for clear interactivity. The footer uses generous vertical padding (`{spacing.section}`) to feel substantial.

### Hero
**`hero-banner`** — The full-width hero section on the homepage and key landing pages. Uses a dark ink background (`{colors.ink}`) with white text, allowing product imagery to pop. A semi-transparent overlay (`rgba(9,10,15,0.35)`) ensures text readability over images. The primary CTA (`{hero-cta}`) is a larger, more prominent version of the primary button.

### Accordion
**`accordion`** — Used for FAQ sections and product details. A white card with a soft hairline border (`{colors.hairline-soft}`) and 8px radius. The trigger area is padded for easy tapping, and the content area collapses smoothly. The design is minimal, relying on typography weight changes to indicate open/closed states.

### Badges
**`product-card-badge`** — Small, uppercase labels that overlay product images. The "New" badge uses the bright blue accent (`{colors.badge-new}`), while a "Sale" badge would use the warm brown (`{colors.badge-sale}`). They are compact (4px padding) with a 4px radius, designed to be informative without dominating the image.

### Quantity Selector
**`quantity-selector`** — An inline control for adjusting item quantities on the product page and cart. Styled as a compact input with a 1px hairline border and 8px radius. The design is clean and unobtrusive, with plus/minus buttons flanking the numeric value.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero banner height reduces to 400px; footer links stack; search bar moves to a full-screen overlay. |
| Tablet | 744–1128px | Two-column product grid; nav-bar remains visible but may condense; hero banner at 500px; footer uses a 2-column layout for link groups. |
| Desktop | 1128–1440px | Full three or four-column product grid; full nav-bar with all links; hero banner at 600px; footer uses a 4-column layout. |
| Wide | > 1440px | Max-width container (1440px) centers content; side margins increase; product grid can expand to 5 columns; hero banner remains at 600px. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Product card images are tappable, linking to the product detail page.
- The hamburger menu icon and cart icon in the mobile nav are padded to exceed 44x44px.
- Accordion triggers are padded to ensure easy tapping on mobile.

### Collapsing Strategy
- The primary navigation collapses into a hamburger menu below 744px.
- The footer's multi-column link groups collapse into a single column on mobile.
- Product filters (on collection pages) collapse into a slide-out drawer on mobile and tablet.
- The search bar collapses into a full-screen overlay on mobile, triggered by a search icon.
- Secondary content (e.g., "You Might Also Like" sections) may be hidden behind a "Show More" toggle on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for tertiary buttons and text links were not fully extracted; assumed standard color transitions.
- Error styling for form inputs (e.g., red border, error message typography) was not observed on the live site.
- The specific font weights for Founders Grotesk (e.g., 400, 500, 600) were inferred from common usage; exact weight-to-style mappings may vary.
- Dark mode styling is not present; the system is designed for a light theme only.
- Sub-brand or seasonal color palettes (e.g., for holiday collections) were not captured.
- The exact box-shadow values for cards and modals were not extracted; a generic shadow is assumed for the scrolled nav state.
- Animation durations and easing curves for transitions (e.g., accordion collapse, nav scroll) were not available.
- The `Signifier Light` font family was found in the CSS but its usage context (likely for editorial or decorative headings) could not be reliably determined.
