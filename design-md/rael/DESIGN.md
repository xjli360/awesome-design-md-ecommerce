---
version: alpha
name: "Rael"
source_url: "https://getrael.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, botanical green (#2a4239) anchors Rael’s holistic feminine care universe, a color that reads as medicinal yet earthy — closer to crushed sage leaf than synthetic healthcare teal. That green runs through the primary button, the footer, and the brand’s logo lockup, while a warm cream canvas (#fdf7ef) and a lighter sand (#faecd8) soften the clinical edge into something that feels like a spa cabinet rather than a pharmacy aisle. The brand’s secondary palette introduces a dusty rose (#f9dee5) and a muted sage (#789f90), colors that appear in product photography backgrounds, ingredient callout cards, and the occasional decorative accent — never decorative alone, always carrying information about phase-of-cycle or product function. Typography is a deliberate hybrid: display headlines use a serif (Cormorant Garamond Regular, sometimes Big Caslon or Bodoni MT) that brings a literary, almost editorial warmth, while body copy and buttons run in Avenir LT Pro (Heavy for buttons, Roman for body) — a sans-serif with enough geometric precision to feel modern but enough humanist curve to avoid coldness. The result is a brand that treats menstrual health not as a clinical problem but as a holistic practice, signaled through the pairing of a clean, medical-grade sans with a serif that belongs on a book spine. Buttons are softly rectangular (`{rounded.sm}`), never pill-shaped, preserving a gentle seriousness. Product cards use a white surface (`{colors.canvas}`) on the cream background, with thin hairline borders (`{colors.hairline}`) that define space without shouting. The checkout experience, powered by Shopify, introduces a bright accent (#21eac3) in progress indicators and confirmation states — a neon mint that feels like a reward after the deep green of the primary journey. Rael’s design system is a study in contrast: the gravity of #2a4239 balanced by the lightness of #fdf7ef, the authority of Avenir tempered by the warmth of Cormorant Garamond, the clinical category softened by botanical color and editorial typography.

colors:
  primary: "#2a4239"
  primary-active: "#155d4f"
  primary-disabled: "#7e8a82"
  ink: "#0b1511"
  body: "#212121"
  muted: "#697870"
  muted-soft: "#7e8a82"
  hairline: "#dedede"
  hairline-soft: "#f2f2f2"
  canvas: "#fdf7ef"
  surface-soft: "#faecd8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rose: "#f9dee5"
  accent-sage: "#789f90"
  accent-mint: "#21eac3"
  error: "#d20000"
  error-bg: "#f8d7da"
  error-border: "#f5c6cb"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond Regular', 'Big Caslon', 'Bodoni MT', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant Garamond Regular', 'Big Caslon', 'Bodoni MT', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant Garamond Regular', 'Big Caslon', 'Bodoni MT', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Avenir LT Pro Heavy', 'Avenir Heavy Oblique', 'Jost', 'Oswald', sans-serif"
    fontSize: 18px
    fontWeight: 800
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Avenir LT Pro Heavy', 'Avenir Heavy Oblique', 'Jost', 'Oswald', sans-serif"
    fontSize: 14px
    fontWeight: 800
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Avenir LT Pro Roman', 'Figtree', 'Myriad', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir LT Pro Roman', 'Figtree', 'Myriad', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir LT Pro Roman', 'Figtree', 'Myriad', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Avenir LT Pro Heavy', 'Avenir Heavy Oblique', 'Jost', 'Oswald', sans-serif"
    fontSize: 14px
    fontWeight: 800
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Avenir LT Pro Heavy', 'Avenir Heavy Oblique', 'Jost', 'Oswald', sans-serif"
    fontSize: 12px
    fontWeight: 800
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  link:
    fontFamily: "'Avenir LT Pro Roman', 'Figtree', 'Myriad', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Avenir LT Pro Roman', 'Figtree', 'Myriad', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
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
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(11, 21, 17, 0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "0 {spacing.base} {spacing.base}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginTop: "{spacing.md}"
  badge-phase:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-ingredient:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.accent-mint}"
    rounded: "{rounded.full}"
    height: 4px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, rendered in deep botanical green (#2a4239) with white uppercase text set in Avenir LT Pro Heavy at 14px with 1px letter-spacing. On hover, the background shifts to a darker forest tone (#155d4f). The disabled state uses a muted sage (#7e8a82) that maintains readability without misleading the user. The button has a soft 8px corner radius (`{rounded.sm}`) and a compact 48px height, designed to feel substantial without dominating the layout.

**`button-secondary`** — An outlined variant on the cream canvas (#fdf7ef) with a 2px green border and green text. On hover, the button fills with the primary green and inverts to white text. This variant is used for “Learn More” and “Add to Cart” actions on product detail pages where a secondary action sits alongside the primary CTA.

**`button-tertiary-text`** — A text-only link styled as a button, used for “Skip” or “Cancel” actions in multi-step flows. No background, no border — just the primary green text in the brand’s heavy uppercase typeface. The hover state adds a subtle underline.

### Cards
**`product-card`** — A white card on the cream canvas, with a 1:1 product image at the top (soft top corners only, `{rounded.sm}`), followed by the product name in heavy uppercase 14px and the price in body 16px green. The card has no border but relies on the contrast between the white surface and the cream background for separation. On hover, the card lifts with a subtle shadow.

**`hero-section`** — A full-width section using the soft sand background (#faecd8) with the display serif headline (Cormorant Garamond, 48px) and a body-weight subheadline in muted sage (#697870). Used on the homepage and category landing pages to introduce a collection or a brand philosophy.

### Badges
**`badge-phase`** — A pill-shaped badge in dusty rose (#f9dee5) with dark ink text, used to indicate which phase of the menstrual cycle a product supports (e.g., “Menstrual,” “Follicular,” “Luteal”). The soft pink reads as warm and informative, not clinical.

**`badge-ingredient`** — A sage green (#789f90) pill badge with white text, used to call out key ingredients (e.g., “Aloe Vera,” “Tea Tree,” “Vitamin C”). The green ties back to the brand’s botanical identity.

**`badge-sale`** — A red (#d20000) pill badge with white text, used sparingly for clearance or promotional pricing. The red is the only high-saturation alert color in the system.

### Navigation
**`nav-bar`** — A 72px sticky bar on the cream canvas, housing the brand logo (green wordmark), a centered set of nav links in Avenir LT Pro Roman 14px, and a right-aligned search icon and cart icon. On scroll, a thin shadow appears beneath the bar. The nav links use the brand’s muted green (#697870) with a heavier weight on the active page.

**`footer`** — A deep green (#2a4239) full-width footer with white text at 80% opacity for links. The footer contains three columns: “Shop” (product categories), “Learn” (education articles, cycle guide), and “Support” (FAQ, shipping, returns). A newsletter signup form sits in the center column with a white input and a green submit button.

### Forms
**`text-input`** — A white input field with a 1px light gray border (#dedede) and 8px corner radius. On focus, the border thickens to 2px and turns green. The error state uses a red border (#d20000) with a pink background (#f8d7da) and red error message below. Inputs are 48px tall with 16px horizontal padding.

**`search-bar`** — A pill-shaped search field (9999px radius) with a white background and light gray border, used in the nav bar and on the search results page. The input includes a magnifying glass icon on the left and a clear button on the right when text is present.

### Progress & Feedback
**`progress-bar`** — A thin 4px bar with a light gray track and a neon mint (#21eac3) fill, used in multi-step checkout, quiz flows, and onboarding. The mint accent is the only place this bright color appears, making it a reward signal for progress.

**`accordion`** — A white collapsible panel with a light gray border and 8px radius, used on product detail pages for “How to Use,” “Ingredients,” and “Shipping & Returns” sections. The header uses the heavy uppercase 14px type with a plus/minus icon toggle.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero headline reduces to 32px; footer stacks to single column; accordions become full-width without side padding |
| Tablet | 744–1128px | Nav links remain visible but compact; product cards display in 2-column grid; hero uses 36px headline; footer uses 2 columns |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3- or 4-column grid; hero uses 48px headline; footer uses 3 columns |
| Wide | > 1440px | Max-width container at 1440px with centered content; product cards may expand to 4 columns; hero section uses larger padding |

### Touch Targets
- All buttons and tappable elements are minimum 44px height (primary buttons are 48px)
- Nav bar hamburger icon is 44x44px
- Product card tap targets (title, price, image) are the full card width
- Accordion headers are 48px tall for easy tapping
- Search bar input is 44px tall

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger menu with a slide-in drawer
- Product filters collapse to a “Filter” button that opens a bottom sheet
- Footer columns collapse to a single column with accordion-style section headers
- Hero sections reduce padding and font size proportionally
- Multi-column grids collapse to single column below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components (text-input, nav-links, badges) could not be reliably extracted from the live site — the extracted CSS may not include all interactive pseudo-classes
- Error styling for forms (error messages, icon placement, animation) is inferred from common Shopify patterns rather than extracted from the site
- Dark mode is not present on the live site and has not been designed
- The neon mint accent (#21eac3) appears in checkout progress indicators but its exact usage rules (when to use vs. primary green) are not fully documented
- Sub-brand or collection-specific color variations (e.g., “Rael for Teens” or “Rael Menopause”) may exist but were not extracted
- The typography system’s exact scale (font sizes, line heights, letter spacing) is inferred from extracted font-family declarations and common editorial patterns — the live site may use slightly different values
- Animation and transition durations (button hover, card lift, nav shadow) are not specified
- The brand’s icon system (search, cart, hamburger, plus/minus, social icons) was not extracted — icons may be custom SVG or a third-party set
- Accessibility ratios (contrast for text on colored backgrounds) have not been verified against WCAG standards
