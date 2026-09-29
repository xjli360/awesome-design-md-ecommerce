---
version: alpha
name: "Oakywood"
source_url: "https://www.oakywood.shop"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A restrained, material-first home office brand that uses a single electric violet accent (#4500ff) to punctuate an otherwise monochrome palette of near-blacks (#1a1a1a, #222222, #1d1d1d) and warm off-whites (#fafafa, #f9fafb, #f3f4f6). The violet appears only on primary CTAs, interactive elements, and the brand's signature desk-organizer badge — a deliberate scarcity that makes every click feel like a deliberate action. Surfaces are treated with soft rounding (`{rounded.sm}` ~8px) on cards and `{rounded.md}` ~12px on product images, while buttons use a tighter `{rounded.sm}` that reads as precise rather than playful. The typography stack relies on Muli (a geometric sans-serif with humanist warmth) at moderate weights — body copy at 400, headings at 600–700 — avoiding the extreme thinness or heaviness that would compete with the wood-grain textures that are the brand's true visual hero. A secondary teal (#108474) surfaces in sustainability badges and eco-claims, while a muted marigold (#fbcd0a) provides occasional star-rating or highlight punctuation. The checkout experience pulls in Shopify's default blues (#2463ec, #007aff), which clash slightly with the brand violet — a known tension between platform constraints and brand identity. The overall effect is of a workshop catalog rendered in clean digital: the wood stays warm, the interface stays cool, and the violet is the only voice that asks for your attention.

colors:
  primary: "#4500ff"
  primary-active: "#3a00d9"
  primary-disabled: "#b399ff"
  ink: "#1a1a1a"
  body: "#222222"
  muted: "#6f6f6f"
  muted-soft: "#7b7b7b"
  hairline: "#d9d9d9"
  hairline-soft: "#e5e5e5"
  canvas: "#fafafa"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  accent-marigold: "#fbcd0a"
  badge-eco: "#108474"
  badge-new: "#4500ff"
  star-fill: "#fbcd0a"
  star-empty: "#e5e5e5"

typography:
  display-xl:
    fontFamily: "'Muli', 'Graphie', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-lg:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Muli', 'Graphie', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    height: 40px
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: 2px solid "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: 1
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.md}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-badge-eco:
    backgroundColor: "{colors.badge-eco}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-lg}"
    color: "{colors.muted}"
    maxWidth: 500px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-md}"
    color: "{colors.canvas}"
  badge-sustainability:
    backgroundColor: "{colors.badge-eco}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 6px 12px
  star-rating:
    fillColor: "{colors.star-fill}"
    emptyColor: "{colors.star-empty}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in the signature violet (#4500ff) with white text and `{rounded.sm}` corners. On hover, it deepens to `{colors.primary-active}` (#3a00d9); when disabled, it fades to `{colors.primary-disabled}` (#b399ff). The `{typography.button-lg}` at 16px/600 weight gives it a confident, slightly elevated presence against the mostly neutral page.

**`button-secondary`** — An outlined variant on white canvas with `{colors.ink}` text, used for secondary actions like "Learn More" or "Add to Wishlist." Shares the same `{rounded.sm}` and height as the primary button but uses a 1px `{colors.hairline}` border to maintain visual hierarchy without competing with the violet.

**`button-tertiary`** — A text-only link styled as a button, using `{colors.primary}` for the text and no background. Appears in contexts where the action is supplementary but still brand-significant, such as "View Details" links within product cards.

**`button-pill-primary`** — A compact pill-shaped variant (`{rounded.full}`) at 40px height, used for filter tags, category navigation, and mobile CTAs where space is tight. The `{typography.button-md}` at 14px keeps it readable without overwhelming the surrounding content.

**`button-pill-outline`** — The outlined counterpart to the pill primary, used for inactive filter states and secondary mobile actions. The transparent background and `{colors.ink}` text allow it to sit comfortably on both white and soft gray surfaces.

### Cards
**`product-card`** — The core product display unit, a white card with `{rounded.md}` (12px) corners and a 1:1 aspect ratio product image. The image itself inherits the same rounding, creating a clean, contained visual. Below the image, the title uses `{typography.title-md}` at 18px/600 weight, and the price uses `{typography.price}` at 16px/600 weight. A `{spacing.md}` (12px) gap separates the image from the text block.

**`product-card-badge`** — A small, uppercase badge in `{colors.badge-new}` (violet) that appears on new arrivals or featured products. The `{rounded.xs}` (4px) and tight padding (4px 8px) keep it unobtrusive but legible.

**`product-card-badge-eco`** — A sustainability badge in `{colors.badge-eco}` (teal #108474), used to flag products made from certified materials or with eco-friendly manufacturing. Same dimensions as the new-arrival badge but distinct in color to signal a different kind of value.

### Navigation
**`nav-bar`** — A fixed-height (72px) white navigation bar with `{colors.ink}` text links set in `{typography.nav-link}` (15px/600 weight). The active link state uses a 2px solid underline in `{colors.primary}`, providing a clear but restrained indicator of the current section. The bar remains white across all pages, relying on the violet accent only for the active state.

**`nav-link-active`** — The active navigation state, distinguished by the violet underline rather than a background fill or bold weight change. This keeps the nav bar visually calm while still providing clear wayfinding.

### Forms
**`text-input`** — A standard text input on white canvas with `{rounded.sm}` (8px) corners and `{typography.body-md}` at 16px. On focus, it gains a 2px `{colors.primary}` border, replacing the default `{colors.hairline}`. The 48px height matches the primary button, ensuring form fields and CTAs align vertically in checkout flows.

**`select-input`** — A dropdown variant of the text input, sharing the same dimensions, rounding, and focus behavior. Used for quantity selectors, sort options, and filter dropdowns on collection pages.

### Hero & Search
**`hero-section`** — The primary brand storytelling area, using the white canvas as a backdrop for large product photography or lifestyle imagery. The heading uses `{typography.display-xl}` at 32px/700 weight with a `maxWidth` of 600px to prevent line-length issues on wide screens. The subheading sits below in `{typography.body-lg}` at 17px/400 weight in `{colors.muted}` (#6f6f6f), with a 500px max width.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) at 48px height, used on collection pages and the mobile navigation drawer. The `{typography.body-md}` placeholder text reads as approachable, and the full rounding differentiates it from the more angular form inputs.

### Footer
**`footer`** — A dark footer on `{colors.ink}` (#1a1a1a) with white text, providing a clear visual boundary at the bottom of every page. Links use `{colors.muted-soft}` (#7b7b7b) to reduce visual weight, while section headings use `{typography.title-md}` in white for hierarchy. The `{spacing.section}` (64px) vertical padding gives the footer generous breathing room.

### Badges
**`badge-sustainability`** — A pill-shaped badge in teal (#108474) with white uppercase text, used to flag eco-certified products and sustainability claims. The `{rounded.full}` shape and 6px 12px padding make it feel like a tag rather than a button, reinforcing its informational role.

**`star-rating`** — A 5-star rating display using `{colors.star-fill}` (marigold #fbcd0a) for filled stars and `{colors.star-empty}` (#e5e5e5) for empty ones. Each star is 16px, and the component is used on product cards and review summaries.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards go to single column; hero section reduces heading to 24px; search bar moves to sticky bottom; footer stacks vertically. |
| Tablet | 744–1128px | Nav bar shows 4–5 links; product cards in 2-column grid; hero heading at 28px; search bar in nav bar. |
| Desktop | 1128–1440px | Full nav bar with all links; product cards in 3-column grid; hero heading at 32px; search bar in nav bar. |
| Wide | > 1440px | Max content width of 1440px with centered layout; product cards in 4-column grid; hero section has larger photography. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons are 40x40px, exceeding the 44px target in one dimension.
- Product card tap targets (title, price, image) are grouped into a single touch zone to prevent mis-taps.
- Filter pills are 40px tall with 24px horizontal padding, providing ample tap area.

### Collapsing Strategy
- On mobile, the nav bar collapses to a hamburger icon that opens a full-screen overlay drawer with all links and the search bar.
- The product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- The footer collapses from a multi-column layout to a single vertical stack on mobile, with accordion-style expandable sections for link groups.
- The hero section collapses its side-by-side image/text layout to a stacked layout on tablet and mobile, with the image above the text.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font list includes "JudgemeStar" (a review-widget icon font), "graphie" (likely a misspelling or internal name), and "swiper-icons" (a carousel library) — the primary brand font is inferred as Muli based on frequency and context, but the exact font stack (including fallbacks) is an educated reconstruction.
- Hover and focus states for secondary buttons, text inputs, and links are inferred from common patterns rather than extracted from the live site.
- The exact border radius for product cards (12px) is estimated from the extracted color frequencies and typical Shopify theme patterns; the actual value may vary by 2–4px.
- Error styling for form inputs (red borders, error message typography) is not present in the extracted data.
- Dark mode is not supported by the brand's current site; all extracted colors assume a light theme.
- The teal (#108474) and marigold (#fbcd0a) accent colors are present in the extracted list but their exact usage contexts (badges, ratings, eco-labels) are inferred from common e-commerce patterns rather than confirmed.
- The Shopify checkout overlay colors (#2463ec, #007aff) are platform defaults and may not reflect intentional brand choices — they are excluded from the core palette but noted here as a known tension.
- The brand's wood-grain and material textures are not captured in the extracted data; these are visual elements that would need to be sourced separately.
