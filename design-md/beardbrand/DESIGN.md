---
version: alpha
name: "Beardbrand"
source_url: "https://www.beardbrand.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A rugged yet refined grooming system for the modern bearded man, Beardbrand lives in a tactile, earthy palette anchored by a deep ink (#101010) and a warm off-white canvas (#f9f8f6). The brand's primary voltage is a muted teal (#108474), used sparingly on CTAs and accent elements, while a sharp accent yellow (#fbcd0a) and a softer sage (#c1e6e6) add unexpected moments of brightness. The typographic voice is a mix of the sturdy, geometric Space Grotesk for headlines and the approachable, humanist Nunito Sans for body copy, creating a tension between authority and friendliness. Generous use of soft hairlines (#eeeeee, #dddddd) and muted surfaces (#f9fafb, #f2f2f2) keeps the interface clean and editorial, letting product photography and the brand's signature beard oil bottles take center stage. The overall mood is one of deliberate, unpretentious craftsmanship — a barbershop that happens to be digital, with every corner softened by a consistent `{rounded.sm}` (8px) radius and every interaction feeling solid, not flashy.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#c1e6e6"
  ink: "#101010"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#888888"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#f9f8f6"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fbcd0a"
  accent-lime: "#e5ff52"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  badge-purple: "#a89cc8"
  star-rating: "#fbcd0a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Space Grotesk', 'Arial', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Space Grotesk', 'Arial', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Space Grotesk', 'Arial', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Space Grotesk', 'Arial', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Space Grotesk', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Nunito Sans', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Space Grotesk', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Space Grotesk', 'Arial', sans-serif"
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-best-seller:
    backgroundColor: "{colors.badge-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe", and key conversion points. Rendered in the brand's signature teal (#108474) with white text, it uses an 8px rounded corner and uppercase Space Grotesk for a confident, masculine feel. On hover, it deepens to `{colors.primary-active}` (#0d6b5d), and when disabled, it fades to a soft sage (#c1e6e6) with muted text.

**`button-secondary`** — A ghost-like alternative for less prominent actions, such as "Learn More" or "View Details". It sits on the warm canvas background (#f9f8f6) with ink text and a subtle hairline border. The active state uses a soft surface fill (#eeeeee) to provide tactile feedback without competing with the primary button.

**`button-outline`** — A border-only variant for use on colored backgrounds or when a lighter touch is needed. It has a 1px solid hairline border and transparent background, making it ideal for overlays or cards where the primary button would be too heavy.

**`button-pill-primary`** and **`button-pill-accent`** — Pill-shaped buttons used for filters, tags, and secondary CTAs in the navigation and product grids. The accent variant uses the brand's yellow (#fbcd0a) for "New" or "Featured" tags, adding a playful pop of energy.

### Cards
**`product-card`** — The core product display unit, featuring a white surface, soft 8px corners, and a clean layout for the product image, title, price, and star rating. The image area is also softly rounded to match the card, creating a cohesive, tactile feel. On hover, a subtle shadow or border change (not captured in tokens) signals interactivity.

### Navigation
**`nav-bar`** — A fixed top navigation bar on a warm canvas background, housing the logo, category links, search, and cart. Links are set in uppercase Space Grotesk at 14px with generous letter-spacing, reinforcing the brand's editorial, barbershop aesthetic. On scroll, it collapses to a shorter sticky variant (`nav-bar-sticky`) for space efficiency.

### Forms
**`text-input`** — Standard input fields for search, email signups, and checkout forms. They use the warm canvas background, 8px rounded corners, and Nunito Sans body text for readability. On focus, the border or outline (not fully captured in tokens) would typically switch to the primary teal.

### Footer
**`footer-section`** — A dark, full-width footer anchored by the deep ink (#101010) background, creating a strong visual closure. Links are set in a muted gray (#888888) and switch to white on hover. The footer houses legal links, social icons, and the newsletter signup form.

### Badges
**`badge-new`**, **`badge-sale`**, **`badge-best-seller`** — Small, uppercase, bold badges applied to product cards to denote status. Each uses a distinct color: yellow for new, teal for sale, and purple for best-seller. They are compact (2px 8px padding) with a 4px rounded corner, ensuring they don't overwhelm the product image.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero text reduces to `{typography.display-md}`; search bar moves to a full-width overlay; footer stacks vertically. |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses `{typography.display-xl}`; search bar is a pill in the nav. |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero is full-width with large imagery; search bar is prominent in the nav. |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to four columns; hero uses larger imagery and typography. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44px height.
- Icon buttons and badge elements are at least 32px x 32px.
- Product card tap areas extend to the full card boundary.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu below 744px.
- The secondary navigation (category strip) collapses into a horizontal scrollable row on mobile.
- The footer's multi-column layout collapses to a single stacked column below 744px.
- Product filters collapse into a slide-out drawer on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs and links were not fully extractable from the live site; assumed standard border/outline changes using the primary teal.
- Error and success styling for form validation (e.g., red borders, green checkmarks) was not observed.
- Dark mode or high-contrast mode tokens are not defined; the brand appears to operate in a single light mode.
- Sub-brand or seasonal palette variations (e.g., holiday collections) were not captured.
- Specific shadow values (box-shadow) for cards, modals, and dropdowns were not extractable; a generic 0 2px 8px rgba(0,0,0,0.1) is assumed for elevation.
- Animation and transition durations/easings were not observed; a standard 200ms ease-in-out is assumed for interactions.
- The exact font weight for Nunito Sans (e.g., 400 vs 600) was inferred from common usage; the live site may use additional weights.
- The `HW_Pano_Bold` font family was found in the CSS but not used in any visible UI; it may be a legacy or unused font.
