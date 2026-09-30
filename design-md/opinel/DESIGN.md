---
version: alpha
name: "Opinel"
source_url: "https://www.opinel-usa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A rugged, heritage-driven French cutlery brand that has been crafting knives since 1890, Opinel’s design system is a study in restrained utility and alpine warmth. The palette is anchored by a deep, confident navy (`#003767`) that appears on primary buttons, the top navigation bar, and the brand’s signature logo lockup — a color that evokes the Savoyard mountains and the brand’s storied past. This is balanced by a warm, golden yellow (`#ffb217`) used for accent badges, sale indicators, and hover states, injecting a sense of craftsmanship and approachability. The canvas is a clean, off-white (`#f5f0ec`), reminiscent of aged beechwood handles, while surfaces and cards use a soft, cool gray (`#dbe4eb` or `#f7f7f7`) to keep the focus on the product photography. Typography is a mix of industrial strength and editorial elegance: the primary display and button text uses ConduitITC in Bold and Medium weights — a condensed, geometric sans-serif that feels like a stamp on a wooden crate — while body copy and captions rely on Poster Bodoni, a high-contrast serif that adds a touch of Parisian atelier. The system avoids hard corners in interactive elements; buttons and search bars use `{rounded.sm}` (8px) radii, while product cards and badges soften to `{rounded.md}` (12px). A muted gray (`#6c757d`) handles secondary text and disabled states, and a vivid red (`#c70000`) is reserved for error states, sale badges, and the brand’s iconic “Opinel” logo dot. The overall mood is one of honest, functional beauty — a design system that doesn’t shout, but lets the steel and wood speak.

colors:
  primary: "#003767"
  primary-active: "#002a4f"
  primary-disabled: "#a0b8cc"
  ink: "#1a1a1a"
  body: "#303030"
  muted: "#6c757d"
  muted-soft: "#888888"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#f5f0ec"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#ffb217"
  accent-gold-hover: "#e09e14"
  badge-red: "#c70000"
  badge-red-hover: "#a30000"
  error: "#c70000"
  link-blue: "#2932fc"
  star-rating: "#ffb217"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'ConduitITC Bold', 'ConduitITC Medium', 'Barlow', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'ConduitITC Bold', 'ConduitITC Medium', 'Barlow', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ConduitITC Medium', 'ConduitITC Bold', 'Barlow', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'ConduitITC Medium', 'Barlow', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'ConduitITC Medium', 'Barlow', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Poster Bodoni', 'Arimo', 'Barlow', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poster Bodoni', 'Arimo', 'Barlow', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'ConduitITC Light', 'Barlow', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'ConduitITC Bold', 'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'ConduitITC Bold', 'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Poster Bodoni', 'Arimo', 'Barlow', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'ConduitITC Medium', 'Barlow', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'ConduitITC Bold', 'Barlow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-accent-gold-hover:
    backgroundColor: "{colors.accent-gold-hover}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 2px solid "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 80px
  nav-bar-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-bar-link-hover:
    textColor: "{colors.accent-gold}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 2px solid "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 80px 24px
  hero-section-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-gold}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  category-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for “Add to Cart”, “Shop Now”, and checkout flows. It uses a deep navy (`{colors.primary}`) background with white text set in ConduitITC Bold, all-caps for a sturdy, industrial feel. On hover, it shifts to `{colors.primary-active}` (#002a4f), and when disabled, it fades to `{colors.primary-disabled}` (#a0b8cc). The button has an 8px rounded corner (`{rounded.sm}`) and 14px vertical / 32px horizontal padding, standing 48px tall.

**`button-secondary`** — An outlined or ghost variant used for “Learn More” or “View Details” links, especially on product cards. It uses the off-white canvas (`{colors.canvas}`) background with dark ink text. On hover, the background becomes `{colors.hairline-soft}` (#e0e0e0). It shares the same typography and dimensions as `button-primary` but with 1px less vertical padding to account for the lack of a border.

**`button-accent-gold`** — A special accent button reserved for promotional actions, such as “Get Yours” on sale items or limited-edition drops. It uses the warm gold (`{colors.accent-gold}`) background with dark ink text, and on hover darkens to `{colors.accent-gold-hover}` (#e09e14). This button is designed to stand out against the navy primary.

### Cards
**`product-card`** — The standard product display card, used on collection pages and search results. It has a white background (`{colors.surface-card}`), 12px rounded corners (`{rounded.md}`), and 16px padding. The product image sits at the top with a softer 8px radius (`{rounded.sm}`). Below, the title uses `title-sm` typography (18px ConduitITC Medium) and the price uses `body-md` (16px Poster Bodoni). A subtle shadow or border is implied by the card structure.

### Navigation
**`nav-bar`** — The top-level site navigation, fixed at 80px height with a solid `{colors.primary}` background. Links are set in ConduitITC Medium, all-caps, 15px, with white text. On hover, links turn gold (`{colors.accent-gold}`). The nav bar may include a logo lockup on the left and a search icon on the right.

**`category-tab-active`** — Used in the category strip on collection pages to indicate the currently selected filter (e.g., “Pocket Knives”, “Chef’s Knives”). It is a pill-shaped button (`{rounded.full}`) with a navy background and white text. The inactive state uses a soft gray background (`{colors.surface-soft}`) with body-colored text.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and checkout forms. It has an off-white canvas background, 8px rounded corners, and a 1px solid hairline border. On focus, the border thickens to 2px and turns navy (`{colors.primary}`). On error, it switches to red (`{colors.error}`). Height is 48px with 12px vertical / 16px horizontal padding.

**`search-bar`** — A full-rounded pill (`{rounded.full}`) used in the site’s main search field, often placed in the nav bar or hero section. It has a white or canvas background, a 1px hairline border, and 12px vertical / 24px horizontal padding. On focus, the border becomes 2px navy.

### Badges
**`badge-sale`** — A small, all-caps badge indicating a discount or sale. It uses a vivid red background (`{colors.badge-red}`) with white text, 8px rounded corners, and 4px vertical / 8px horizontal padding. The typography is ConduitITC Bold at 11px.

**`badge-new`** — Similar in shape to the sale badge but using the gold accent (`{colors.accent-gold}`) with dark ink text. Used for “New Arrivals” or limited-edition markers.

### Footer
**`footer`** — The site footer, spanning the full width with a navy background (`{colors.primary}`) and white text. It uses `body-sm` typography (14px Poster Bodoni) for links and legal text. Links turn gold on hover. Padding is 48px vertical and 24px horizontal.

### Hero
**`hero-section`** — A full-width hero banner, typically used on the homepage or landing pages. It has a navy background with white text, using `display-xl` typography (48px ConduitITC Bold). A semi-transparent black overlay (`{colors.scrim}` at 30% opacity) may be applied over background images. Padding is 80px vertical and 24px horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in a single column; hero text reduces to `display-lg` (36px); buttons become full-width; footer links stack vertically. |
| Tablet | 744–1128px | Nav bar remains expanded but with reduced link padding; product cards display in a 2-column grid; hero text uses `display-lg`; search bar remains pill-shaped but shrinks to 40px height. |
| Desktop | 1128–1440px | Full nav bar with all links visible; product cards in a 3- or 4-column grid; hero text uses `display-xl`; all buttons at standard 48px height. |
| Wide | > 1440px | Max-width container (1440px) centered; product cards may expand to 4- or 5-column grid; hero section may include a parallax effect. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 48px on mobile to meet accessibility guidelines.
- Icon-only buttons (e.g., search, cart) have a 44x44px touch target.
- Category tabs and badges have a minimum height of 32px.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger menu; the logo remains centered.
- The category strip collapses into a horizontal scrollable row on mobile.
- Footer columns stack vertically on mobile, with each link group expanding/collapsing via accordion.
- Product card grids reduce from 4 columns to 2 columns on tablet, and 1 column on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for `button-secondary` and `button-accent-gold` are inferred from common patterns; exact color values may vary.
- Error styling for form inputs (e.g., error messages, iconography) is not fully extracted; only the border color change is documented.
- Dark mode is not supported; all tokens assume a light theme.
- Sub-brand palettes (e.g., Opinel Outdoor, Opinel Kitchen) may have distinct accent colors not captured here.
- Typography weights for ConduitITC Light, Medium, and Bold are assumed; exact font files may have different weight mappings.
- The `star-rating` component’s size and spacing are estimated; the exact implementation may use SVG or custom icons.
- The `scrim` overlay opacity is a best-guess; the actual value may be 0.2 or 0.4 depending on context.
- The `link-blue` token (#2932fc) is extracted but its usage context (e.g., legal links, text links) is not confirmed.
- The `#3b5998` hex is likely a Facebook brand color used for social sharing buttons; not included in core tokens.
