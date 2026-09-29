---
version: alpha
name: "Selmer Paris"
source_url: "https://www.selmer.fr"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, resonant navy (#0e2431) anchors Henri SELMER Paris — not as a background afterthought but as the brand's primary voltage, pulled from the dark felt lining of a clarinet case and the shadow between keys. This is a brand that trusts restraint: the palette runs from that near-black ink through warm brass (#debc82), a sage whisper (#aaccaa), and a clean off-white canvas (#f8f8f8). The brass isn't decorative — it's the material truth of a saxophone bell catching stage light, used sparingly for hover states, accent borders, and the occasional badge. Montserrat runs the typography system at modest weights (400–600), never shouting, while Syncopate appears in select display contexts as a nod to the brand's mid-century Parisian heritage. Every corner is sharp (`{rounded.none}`) or softly squared (`{rounded.xs}`) — there are no pill-shaped buttons or bubbly cards. The product grid treats each instrument as a sculpture: generous padding (`{spacing.xxl}`), minimal text, and photography that lets the lacquer and engraving speak. The nav bar lives in the deep navy, white text floating above it like a museum label. This is not a lifestyle brand; it's a workshop that happens to sell to the world's best clarinetists and saxophonists.

colors:
  primary: "#0e2431"
  primary-active: "#121212"
  primary-disabled: "#3a3a3a"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#dedede"
  muted-soft: "#f8f8f8"
  hairline: "#dedede"
  hairline-soft: "#f8f8f8"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  brass: "#debc82"
  brass-hover: "#c9a86e"
  sage: "#aaccaa"
  sage-soft: "#d4e8d4"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  syncopate-display:
    fontFamily: "'Syncopate', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase

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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-brass:
    backgroundColor: "{colors.brass}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-brass-hover:
    backgroundColor: "{colors.brass-hover}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"
    padding: 4px 0
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.brass}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.brass}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    boxShadow: "0 4px 12px rgba(14, 36, 49, 0.08)"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.md}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.brass}"
    marginTop: "{spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.brass}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    marginTop: "{spacing.xl}"
  section-heading:
    typography: "{typography.title-lg}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.xl}"
  badge-new:
    backgroundColor: "{colors.sage}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.body}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.brass}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-uppercase}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.none}"
  text-input-error:
    border: "2px solid #c13515"
    rounded: "{rounded.none}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.brass}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.md}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.xl} 0"
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.lg} 0"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0"
    borderTop: "1px solid {colors.hairline}"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0 {spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in deep navy (#0e2431) with white uppercase Montserrat. No rounding — the sharp corner signals precision craftsmanship. On hover, shifts to near-black (#121212). Disabled state uses muted gray (#3a3a3a) with lighter text. Used for "Add to Cart", "View Product", and primary form submissions.

**`button-secondary`** — An outlined variant with a 2px navy border on a white background. The text sits in the primary navy. On hover, the button fills with navy and the text inverts to white. Used for "Learn More", "Explore Range", and secondary actions in hero sections.

**`button-brass`** — The accent button, filled with warm brass (#debc82) and dark ink text. On hover, deepens to #c9a86e. Reserved for high-visibility actions in the hero, limited-edition launches, and the primary CTA on product detail pages where the brand wants to echo the instrument's lacquer.

**`button-text-link`** — A text-only button with no background or border. Uses the link typography token. Used for "Read the Story", "View Specifications", and inline navigation within content sections.

### Navigation
**`nav-bar`** — A fixed 72px bar in the primary navy with white uppercase navigation links. The brand logo sits left, navigation items center or right. The bar carries the brand's full weight — it's the first thing visitors see and it never wavers.

**`nav-link-active`** — The active or hovered navigation item. The text shifts to brass (#debc82) and a 2px brass underline appears below. This is the only place brass appears as a text color, creating a subtle but unmistakable signal.

**`nav-link-inactive`** — Default navigation link in white. No underline, no decoration. The brand trusts the contrast of white on navy to communicate hierarchy.

### Cards
**`product-card`** — A minimal card with no rounding, white background, and generous padding. The image sits in a 4:3 aspect ratio on a soft gray background. Below: an uppercase title in 14px/600 and the price in body-md. On hover, the card gets a soft shadow and the background shifts to #f8f8f8. No border, no badge by default — the instrument photography is the decoration.

**`product-card-hover`** — The hover state adds a subtle box shadow (0 4px 12px rgba(14, 36, 49, 0.08)) and a light background shift. The typography remains unchanged — the brand doesn't need to shout to indicate interactivity.

### Badges
**`badge-new`** — A small sage (#aaccaa) badge with dark text, 2px rounding, and uppercase 11px type. Used to flag newly released instruments or models. The sage is the brand's only "fresh" color — it appears nowhere else in the system.

**`badge-sold-out`** — A muted gray badge for out-of-stock items. Uses the same shape and typography as `badge-new` but in a neutral tone that doesn't compete with available products.

**`badge-limited`** — A brass badge for limited editions or anniversary models. The warm metallic tone signals exclusivity without resorting to red or orange.

### Forms
**`text-input`** — A sharp-cornered input field with a 1px hairline border. On focus, the border thickens to 2px and shifts to the primary navy. Error state uses a red border (#c13515). The input height (48px) matches the primary button for visual alignment in forms.

**`select-dropdown`** — Matches the text-input in height, padding, and border treatment. The dropdown arrow is rendered in the primary navy.

### Footer
**`footer-section`** — A full-width navy footer with white body text. Links are muted gray by default and shift to brass on hover. Section headings use the uppercase title-sm token. The footer is dense with information — product categories, support links, and legal text — but the consistent navy background keeps it from feeling cluttered.

**`footer-link`** — Muted gray (#dedede) links that shift to brass on hover. No underline decoration — the color change is the only signal.

### Dividers
**`divider`** — A 1px hairline (#dedede) used between major sections. **`divider-soft`** uses #f8f8f8 for subtler separation within cards or content blocks.

### Accordion
**`accordion-trigger`** — A full-width clickable row with an uppercase title and a hairline top border. The trigger has no background — it relies on the border and typography to signal interactivity. **`accordion-content`** uses body-md with generous bottom padding for readability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger; product cards stack single-column; hero padding reduces to 32px; typography scales down one step (display-xl becomes 32px); footer links stack vertically |
| Tablet | 744–1128px | Nav bar shows all links but reduced padding; product cards in 2-column grid; hero maintains 48px padding; section padding reduces to 48px |
| Desktop | 1128–1440px | Full nav bar with 32px padding; product cards in 3-column grid; hero at 80px section padding; all typography at default sizes |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with max-width 800px; additional whitespace in margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Nav bar links have 48px tap targets even when text is smaller
- Product cards are fully tappable (the entire card is a link, not just the title)
- Accordion triggers have 48px minimum tap height
- Form inputs and buttons maintain 48px height across all breakpoints

### Collapsing Strategy
- Primary nav collapses to a hamburger menu below 744px, with a slide-in drawer from the left
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer link columns collapse from 4 to 2 at tablet, then stack vertically at mobile
- Hero content stacks vertically at mobile (title above subtitle above CTA)
- Accordion content collapses by default on all breakpoints, toggling open on click
- Secondary navigation (breadcrumbs, sub-category filters) collapses into a select dropdown below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for `button-secondary` and `button-brass` are inferred from brand logic, not extracted from the live site
- Error styling for forms (red border hex #c13515) is a standard convention, not extracted from Selmer Paris
- The `syncopate-display` typography token is based on extracted font-family declarations but its exact usage context (headings, logos, or decorative elements) is unknown
- Dark mode is not present on the live site and no dark mode palette has been defined
- Sub-brand or collection-specific palettes (e.g., "Supreme" vs. "Reference" saxophone lines) could not be extracted
- The `badge-new`, `badge-sold-out`, and `badge-limited` tokens are inferred from common e-commerce patterns, not extracted from the live site
- Accordion behavior (trigger, content) is a reasonable assumption for a product specification page but was not confirmed from the live site
- The `product-card-hover` box-shadow value is a design-system convention, not extracted
- No extracted data for loading states, skeleton screens, or empty states
- The extracted hex list includes #aaccaa (sage) and #debc82 (brass) which are distinctive enough to be intentional brand colors, but their exact usage (backgrounds, accents, badges) is inferred from context
- Shopify checkout widget colors (if any) were filtered from the extracted palette, but some residual checkout colors may remain in the muted grays
