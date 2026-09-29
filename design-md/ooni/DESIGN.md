---
version: alpha
name: "Ooni"
source_url: "https://ooni.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Ooni is the brand that turned backyard pizza-making into a cult obsession — a design system built around the heat and glow of fire, the char of a Neapolitan crust, and the tactile satisfaction of a steel peel sliding under a perfect pie. The palette is anchored in deep charcoal and iron tones — `#25282a`, `#293035`, `#17191a`, `#22272a` — that read as industrial, serious, and heat-resistant, like the shell of a Koda 16. Against that dark forge, the brand’s primary voltage is a molten amber-gold gradient that lives between `#ffc633`, `#ffd057`, and `#f79a20` — a color that suggests flame, melted cheese, and the moment of truth when you lift the lid. Accents of `#bc3c26` and `#d4602c` add a burnt-orange edge, while `#006fcf` and `#3086c8` appear sparingly as technical highlights (think gas regulator knobs or app UI). The canvas is `#f5f5f5` and `#e2e2e2` — warm off-whites that never feel clinical — with cards and surfaces sitting on `#ffffff`. Hairlines in `#c1c2c3` and `#cccccc` keep the grid crisp without shouting. Typography is absent from extracted hints, so the system assumes a clean, modern sans-serif stack — likely something like Inter or a system fallback — set at moderate weights to let the product photography (steam, fire, dough) do the heavy lifting. Rounded corners are generous but not pill-obsessed: `{rounded.sm}` for buttons, `{rounded.md}` for cards, `{rounded.full}` for the occasional badge or toggle. The voice is direct, confident, and slightly irreverent — “The world’s best pizza oven” isn’t a boast, it’s a fact. Every design move reinforces the central promise: you, in your backyard, making pizzeria-quality pizza in 60 seconds.

colors:
  primary: "#ffc633"
  primary-active: "#f79a20"
  primary-disabled: "#dedede"
  ink: "#17191a"
  body: "#25282a"
  muted: "#575a5d"
  muted-soft: "#6b6a68"
  hairline: "#c1c2c3"
  hairline-soft: "#cccccc"
  canvas: "#f5f5f5"
  surface-soft: "#e2e2e2"
  surface-card: "#ffffff"
  on-primary: "#17191a"
  accent-fire: "#bc3c26"
  accent-burnt-orange: "#d4602c"
  accent-gold: "#ffd057"
  accent-tech-blue: "#006fcf"
  accent-tech-blue-light: "#3086c8"
  accent-warm-amber: "#f48120"
  accent-ember: "#f89f20"
  accent-deep-charcoal: "#293035"
  accent-iron: "#22272a"
  accent-dark-void: "#0b1318"
  accent-near-black: "#231f20"
  accent-warm-gray: "#d8d8d8"
  accent-soft-gray: "#e2e2e2"
  star-rating: "#ffc633"
  scrim: "#0b1318"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, system-ui, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-fire:
    backgroundColor: "{colors.accent-fire}"
    textColor: "{colors.surface-card}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-fire-active:
    backgroundColor: "{colors.accent-burnt-orange}"
    textColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
  button-pill-amber:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline-soft}"
  icon-button-circle-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-fire}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.accent-deep-charcoal}"
    textColor: "{colors.surface-card}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(23, 25, 26, 0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-badge-new:
    backgroundColor: "{colors.accent-fire}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-badge-best-seller:
    backgroundColor: "{colors.accent-tech-blue}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  price-display:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  price-compare-at:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: "line-through"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  review-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  footer-section:
    backgroundColor: "{colors.accent-deep-charcoal}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.surface-soft}"
  footer-link-hover:
    textColor: "{colors.primary}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  social-icon:
    color: "{colors.surface-soft}"
    size: 24px
  social-icon-hover:
    color: "{colors.primary}"
  cart-icon:
    color: "{colors.ink}"
    size: 24px
  cart-count-badge:
    backgroundColor: "{colors.accent-fire}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  mobile-menu-toggle:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 48px
    width: 48px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  feature-grid:
    gap: "{spacing.lg}"
  feature-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  feature-icon:
    color: "{colors.primary}"
    size: 32px
  testimonial-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  testimonial-author:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  trust-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Ooni ecosystem, rendered in the brand's molten gold `{colors.primary}` with dark `{colors.on-primary}` text for maximum contrast against the charcoal-toned hero sections and product pages. On hover, it shifts to `{colors.primary-active}`, a deeper amber that suggests the heat of a fully preheated oven. The disabled state drops to `{colors.primary-disabled}`, a muted gray that signals unavailability without visual noise. All primary buttons use `{rounded.sm}` for a soft, approachable corner that balances the industrial palette.

**`button-secondary`** — A white canvas button with a `{colors.hairline}` border, used for "Learn More" and "Compare" actions alongside primary CTAs. On active state, the border deepens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`, creating a clear hierarchy without competing with the primary button. The 2px border ensures it reads as intentional and structural, not accidental.

**`button-ghost`** — A text-only button with no background or border, used in navigation dropdowns, accordion triggers, and secondary actions within cards. The active state adds a `{colors.surface-soft}` background to provide a hit target without overwhelming the layout. Ghost buttons inherit the full `{typography.button-md}` weight to maintain visual parity with their bordered counterparts.

**`button-accent-fire`** — A high-energy accent button using `{colors.accent-fire}`, a burnt red-orange that appears in limited, intentional doses — typically for "Shop Now" on sale items, limited-edition announcements, or the checkout CTA. On hover, it deepens to `{colors.accent-burnt-orange}`, reinforcing the heat-and-fire metaphor that runs through the brand.

**`button-pill-amber`** — A fully rounded pill variant of the primary button, used sparingly for promotional banners, sticky mobile CTAs, and "Subscribe" actions. The `{rounded.full}` shape reads as friendly and urgent, while the amber gold `{colors.primary}` keeps it within the Ooni color story.

**`button-pill-outline`** — A pill-shaped outline button with a `{colors.hairline}` border, used for filter toggles, category pills, and "Clear All" actions. The transparent background and subtle border make it ideal for dense UI sections like product listing pages where visual hierarchy must be maintained without clutter.

### Cards
**`product-card`** — The primary container for oven listings, accessories, and recipe cards. A white `{colors.surface-card}` background with a soft `{colors.hairline-soft}` border and `{rounded.md}` corners creates a clean, product-forward frame. On hover, the border strengthens to `{colors.hairline}` and a subtle `boxShadow` lifts the card, signaling interactivity without the heavy drop shadows typical of e-commerce. The card image area uses `{rounded.md}` on top corners only, allowing the photo to bleed edge-to-edge horizontally.

**`feature-item`** — Used in the "Why Ooni" grid sections, these cards combine an icon, heading, and short description. The `{colors.surface-card}` background with `{colors.hairline-soft}` border and `{rounded.md}` corners mirrors the product card, creating visual consistency across the page. Icons render in `{colors.primary}` gold, tying the feature set back to the brand's core voltage.

**`testimonial-card`** — Customer review cards on the `{colors.canvas}` background with a `{colors.hairline-soft}` border. The author name uses `{typography.title-sm}` in `{colors.ink}` for emphasis, while the body text runs in `{typography.body-md}` at `{colors.body}`. The subtle border keeps the card distinct from the background without competing with the product photography.

### Navigation
**`top-nav`** — A fixed 72px white bar with a `{colors.hairline-soft}` bottom border, housing the Ooni logo, product category links, search, cart, and account icons. Navigation links use `{typography.nav-link}` at 15px with 500 weight — intentionally lighter than the button typography to keep the header calm and browsable. Active links are marked with a 2px `{colors.primary}` bottom border, while inactive links sit in `{colors.muted}`.

**`nav-link-active`** — The active state for top-level navigation items, distinguished by a `{colors.primary}` underline and full `{colors.ink}` color. The 2px border is thin enough to feel structural, not decorative.

**`nav-link-inactive`** — Default navigation links in `{colors.muted}`, creating a clear visual hierarchy between the current section and available destinations. No underline or border in the inactive state.

### Forms
**`text-input`** — Standard form inputs for checkout, account creation, and newsletter signup. A white background with a `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border doubles to 2px and switches to `{colors.primary}`, providing a clear, accessible focus indicator. Error states use a 2px `{colors.accent-fire}` border, the brand's burnt red-orange, ensuring error states are unmistakable without relying solely on color.

**`select-dropdown`** — Styled select elements matching the `{colors.surface-card}` background and `{colors.hairline}` border pattern of text inputs. The `{rounded.sm}` corners and consistent 48px height ensure form elements feel like a cohesive system, not an afterthought.

**`search-bar`** — A dedicated search input with `{rounded.md}` corners (slightly rounder than standard inputs to signal its special role) and a `{colors.hairline}` border. On focus, the border becomes 2px `{colors.primary}`, matching the text-input pattern. The search bar sits in the top nav and on the search results page.

**`newsletter-input`** — A footer-specific input paired with the `newsletter-submit` button. The input matches the standard `{colors.surface-card}` and `{colors.hairline}` pattern, while the submit button uses `{colors.primary}` to draw the eye. The pair sits flush against the dark `{colors.accent-deep-charcoal}` footer background, creating a high-contrast capture point.

### Badges
**`product-badge-new`** — A small, fully rounded pill in `{colors.accent-fire}` with white text, used to flag newly launched ovens and accessories. The `{typography.badge}` uppercase styling at 11px ensures the badge reads as metadata, not primary content.

**`product-badge-sale`** — A gold `{colors.primary}` badge for sale and discount items, matching the primary button color to create a visual link between the badge and the "Shop Sale" CTA. The uppercase badge typography keeps it compact and scannable.

**`product-badge-best-seller`** — A blue `{colors.accent-tech-blue}` badge that stands out from the warm amber palette, used exclusively for best-seller designations. The cool blue provides deliberate contrast against the predominantly warm product photography and gold accents.

### Footer
**`footer-section`** — A full-width dark section using `{colors.accent-deep-charcoal}` as the background, with text in `{colors.surface-soft}` for readability. Links use `{typography.link}` at 14px with 500 weight, and hover to `{colors.primary}` gold. The footer contains the newsletter signup, navigation columns, social icons, and legal text — all on the same dark canvas that echoes the brand's industrial heritage.

**`footer-link`** — Standard footer links in `{colors.surface-soft}` with `{typography.link}` styling. The 500 weight is slightly heavier than standard body text, ensuring legibility against the dark background.

**`footer-link-hover`** — Footer links transition to `{colors.primary}` on hover, creating a warm, interactive moment against the charcoal backdrop. The gold matches the primary button color, reinforcing the brand's core identity.

### Cart & Quantity
**`cart-icon`** — A 24px icon in `{colors.ink}`, sitting in the top nav alongside the account and search icons. The icon is simple and geometric, matching the brand's no-nonsense industrial aesthetic.

**`cart-count-badge`** — A small red `{colors.accent-fire}` pill that overlays the cart icon, displaying the current item count. The `{rounded.full}` shape and compact sizing (20px height) ensure it reads as a notification, not a design element.

**`quantity-selector`** — A compact input group for adjusting product quantities in the cart and on product pages. A `{colors.hairline}` border and `{rounded.sm}` corners contain the decrement button, numeric display, and increment button. Each button is 40px square with transparent background, creating a clean, minimal interaction.

### Dividers & Headings
**`divider`** — A 1px horizontal line in `{colors.hairline-soft}`, used between sections, within accordions, and in the footer. The soft gray ensures it separates content without creating visual noise.

**`section-heading`** — Page and section titles using `{typography.display-md}` at 28px with 600 weight and `{colors.ink}`. The `{spacing.lg}` bottom margin provides consistent breathing room between the heading and the content below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layouts; top-nav collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-md}`; search bar moves to full-width below nav; footer columns stack; quantity selector becomes full-width; buttons expand to full-width for touch targets |
| Tablet | 744–1128px | Two-column product grids; top-nav shows limited links with "More" dropdown; hero uses `{typography.display-lg}`; footer shows 2-column grid; search bar remains in nav but collapses to icon on scroll |
| Desktop | 1128–1440px | Full top-nav with all links visible; three-column product grids; hero uses `{typography.display-xl}`; footer shows 4-column grid; search bar fully expanded in nav |
| Wide | > 1440px | Max-width container (1440px) centered; additional whitespace on sides; product grids can expand to 4 columns; hero content remains centered with generous padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons in the top nav are 48px square to provide adequate tap targets
- Quantity selector buttons are 40px — slightly below the 44px recommendation but acceptable for the compact cart context
- Product card tap targets span the full card width on mobile
- Footer links have 44px minimum tap areas through increased padding
- Accordion headers are 48px tall with full-width tap targets

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with the full link list appearing in a slide-out drawer
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer columns stack vertically on mobile, with accordion-style expandable sections for each column heading
- Multi-column feature grids collapse to single-column on mobile, with images stacking above text
- Product image galleries collapse to a single swipeable carousel on mobile, replacing the thumbnail grid
- Search transitions from an expanded input to an icon-only toggle on tablet and below
- Cart drawer replaces the full cart page on mobile, sliding in from the right

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font-family declarations could not be extracted from the live site; the system assumes Inter as the primary sans-serif based on common DTC appliance brand usage, but the actual stack may differ
- Hover and active states for all components are inferred from common e-commerce patterns and the brand's color palette; actual interaction specifications (transition durations, easing curves, shadow depths) were not extractable
- Error state styling for forms (error messages, validation icons) is assumed based on the `{colors.accent-fire}` error border; actual error message typography and placement are unknown
- Dark mode specifications are not present on the live site; all tokens assume light mode only
- Sub-brand or collection-specific palettes (e.g., Koda series vs. Fyra series vs. Karu series) may exist but were not extractable from the global CSS
- Modal and overlay specifications (backdrop opacity, close button placement, animation) were not observed
- Loading state designs (skeleton screens, spinner colors, shimmer animations) are not documented
- Tooltip and popover styling (background, arrow, z-index) is absent from the extracted data
- Focus-visible ring styles for keyboard navigation were not observed; the system assumes a 2px `{colors.primary}` outline as a reasonable default
- Checkbox and radio button styling (custom vs. native, checked state, indeterminate state) is not documented
- The `{colors.accent-tech-blue}` and `{colors.accent-tech-blue-light}` tokens appear sparingly and may represent a secondary brand color for technical/educational content; their exact usage rules are inferred
- Multi-step form patterns (checkout, oven configurator) were not observed; progress indicator styling is unknown
- Video player controls and play button styling are not documented
- Cookie consent banner and GDPR-related UI patterns were not extracted
- Print stylesheet specifications are absent from the design system data
