---
version: alpha
name: "Oru Kayak"
source_url: "https://www.orukayak.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A folding kayak brand that uses a deep, confident blue (#1743b8) as its primary voltage — the same blue that anchors the brand's CTAs, header backgrounds, and product highlights, evoking open water and reliable gear. The palette is unexpectedly broad: alongside that core blue sit a warm orange (#f47721) used for sale badges and promotional accents, a coral-pink (#f04860) for limited-edition or special markers, and a muted sage (#7f89b4) that appears in secondary navigation and footer areas. The site runs on a clean white canvas (#f8f8f8) with soft gray surfaces (#ededed, #e3e3e3) for cards and sections, creating a layered, approachable feel that balances adventure-readiness with e-commerce clarity. Typography mixes DM Serif Display for hero headings — a choice that signals craftsmanship and heritage — with Open Sans and Arial for body and UI text, keeping readability high across product detail pages and comparison tables. Buttons use {rounded.sm} corners, product cards use {rounded.md}, and the overall spacing rhythm (base 16px, section 64px) gives each product photo room to breathe. The brand's folding-kayak innovation is communicated through generous whitespace, clear hierarchy, and a color system that never overwhelms the product imagery.

colors:
  primary: "#1743b8"
  primary-active: "#266abe"
  primary-disabled: "#acb5d4"
  ink: "#4f4f4f"
  body: "#6a6c77"
  muted: "#737373"
  muted-soft: "#aaaaaa"
  hairline: "#cfd7e3"
  hairline-soft: "#dfdfdf"
  canvas: "#f8f8f8"
  surface-soft: "#ededed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f47721"
  accent-orange-active: "#e7721b"
  accent-orange-dark: "#cc4e19"
  accent-coral: "#f04860"
  accent-coral-active: "#ea1332"
  accent-gold: "#efae00"
  accent-green: "#1cc286"
  accent-sage: "#7f89b4"
  accent-sage-light: "#acb5d4"
  dark-charcoal: "#575757"
  deep-brown: "#962d16"
  medium-brown: "#a63f14"
  steel-gray: "#676a6c"
  link-blue: "#2f84ed"
  link-blue-active: "#1471e6"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'DM Serif Display', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'DM Serif Display', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Serif Display', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
    padding: 4px 0
  button-text-link-active:
    backgroundColor: transparent
    textColor: "{colors.link-blue-active}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-coral}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
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
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  product-badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-limited:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 480px
  hero-section-overlay:
    backgroundColor: "rgba(23, 67, 184, 0.85)"
    textColor: "{colors.on-primary}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0 {spacing.lg}"
  section-subheading:
    typography: "{typography.title-md}"
    textColor: "{colors.body}"
    padding: "0 0 {spacing.base}"
  feature-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  feature-card-icon:
    color: "{colors.primary}"
    height: 48px
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  footer-link-hover:
    typography: "{typography.body-sm}"
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "0 0 {spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.base}"
  comparison-table-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
  comparison-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  comparison-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Buy Now," and "Shop Collection" actions. Rendered in the brand's deep blue (#1743b8) with white text and 8px rounded corners. On hover, shifts to a lighter blue (#266abe). Disabled state uses a muted periwinkle (#acb5d4) to signal inactivity without visual noise.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "Compare Models." Uses a white background with a 2px solid blue border matching the primary color. Hover state deepens the border to the active blue and adds a light gray background. Maintains the same 48px height and 8px rounding as the primary for visual consistency.

**`button-accent-orange`** — Reserved for promotional CTAs, sale banners, and limited-time offers. Uses the warm orange (#f47721) to create urgency and visual contrast against the predominantly blue system. Hover state darkens to (#e7721b). Never used alongside the primary button in the same container to avoid competing attention.

**`button-text-link`** — A text-only button for inline actions like "View Details" or "See Specifications." Uses the link blue (#2f84ed) with no background or border. Hover state darkens to (#1471e6). Underline appears on hover for accessibility.

### Text Inputs & Forms
**`text-input`** — Standard form input for checkout, newsletter signup, and contact forms. White background with a light gray border (#cfd7e3) and 8px rounding. On focus, the border thickens to 2px and turns brand blue. Error state uses a coral border (#f04860) to clearly indicate validation issues. All inputs maintain 48px height for consistent touch targets.

**`select-input`** — Dropdown selectors for product configuration (model, color, accessories). Matches the text-input styling with a custom dropdown arrow. Uses the same 48px height and 8px rounding for form consistency.

### Navigation
**`nav-bar`** — The primary site navigation, 72px tall with a white background and a subtle bottom border. Contains the brand logo, product category links, and utility icons (search, account, cart). On scroll, collapses to 60px with a light drop shadow for depth. Active nav links use the brand blue to indicate current section.

**`nav-link-active`** — Active navigation link state. Text color shifts to the brand blue (#1743b8) while maintaining the same typography and spacing. No underline or background change — the color shift alone signals the active state, keeping the nav clean and minimal.

### Product Cards
**`product-card`** — The primary product display unit across collection pages and search results. A white card with 12px rounding and a subtle shadow. The product image fills the top with matching corner rounding. Title and price sit below with consistent padding. On hover, the shadow deepens to create a subtle lift effect, signaling interactivity without animation.

**`product-badge-sale`** — Orange badges for sale items, using the accent orange (#f47721) with white uppercase text. 4px rounding and tight padding keep them compact. Positioned at the top-left of product images. Also available in green for "New" items and coral for "Limited Edition" markers.

### Hero & Sections
**`hero-section`** — Full-width hero banners on the homepage and campaign pages. Uses the brand blue as background with white text, creating immediate brand recognition. Minimum height of 480px ensures the headline and CTA are visible above the fold. An optional overlay variant adds a semi-transparent blue scrim for readability over background images.

**`section-heading`** — Section titles across the site, using the serif display font at 28px. Dark gray (#4f4f4f) for readability against white or light backgrounds. Paired with generous top padding (64px) to create visual breathing room between content blocks.

**`feature-card`** — Information cards used in "Why Oru" and "How It Works" sections. White background with 12px rounding, 32px padding, and a subtle shadow. Each card contains an icon (48px, brand blue), a title, and descriptive text. Used in 3-column grids on desktop, collapsing to single column on mobile.

### Footer
**`footer-section`** — The site footer, using a light gray background (#ededed) with muted text colors. Contains link columns, social icons, and legal text. Links use the muted gray (#737373) with blue hover states. Section padding of 64px matches the site's vertical rhythm.

**`footer-heading`** — Column headings in the footer, using the sans-serif title style at 18px in dark gray. Separates link groups for products, support, company, and legal sections.

### Search & Utilities
**`search-bar`** — The site search input, styled as a pill shape (9999px rounding) for a friendly, approachable feel. White background with a light gray border. On focus, the border thickens to 2px and turns brand blue. Maintains 48px height for consistent touch targets.

**`quantity-selector`** — Product quantity adjustment control on the cart and product detail pages. A compact 40px height with 8px rounding, matching the form input family. Contains minus, number, and plus controls in a single bordered container.

### Accordion & Tables
**`accordion-trigger`** — Expandable section headers used in product FAQs and specifications. Text-only trigger with a bottom border separator. On click, expands to reveal the accordion content below. Uses the title style at 18px for clear hierarchy.

**`accordion-content`** — The expandable content area beneath accordion triggers. Uses body text styling with bottom padding for spacing. Content can include paragraphs, lists, or specification tables.

**`comparison-table-header`** — Table headers in the product comparison section. Brand blue background with white text, creating a clear visual anchor for the comparison data. Used across model comparison pages to help customers choose between kayak variants.

**`comparison-table-row`** — Standard table rows in comparison tables. Alternating white and light gray backgrounds for readability. Each row contains feature names and checkmarks or values for each product variant.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layouts, nav collapses to hamburger menu, product cards stack vertically, hero sections reduce to 320px min-height, section padding reduces to 32px, font sizes scale down one step |
| Tablet | 744–1128px | 2-column product grids, nav remains visible but condensed, hero sections at 400px min-height, section padding at 48px, font sizes at display-md for headings |
| Desktop | 1128–1440px | 3-4 column product grids, full nav with all links visible, hero sections at 480px min-height, standard section padding of 64px, full typography scale |
| Wide | > 1440px | Max-width containers at 1440px with centered content, additional whitespace on sides, hero sections can extend to 560px for visual impact |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets are the entire card, not just the title or button
- Nav links have 48px minimum touch area even on desktop
- Accordion triggers have 48px touch height for easy expansion on mobile
- Quantity selector controls have 44px minimum tap targets

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer for links
- Product grids reduce columns: 4-column → 2-column → 1-column as viewport narrows
- Hero sections stack content vertically on mobile (headline above image instead of side-by-side)
- Feature cards stack from 3-column to single column below 744px
- Comparison tables convert to stacked card layouts below 744px, with each product becoming a separate card
- Footer link columns collapse from 4-column to 2-column to single column
- Accordion content is always collapsed by default on mobile to reduce vertical scroll

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is unusually large (30+ colors), suggesting the site may pull in colors from Shopify checkout widgets, social media icons, and product imagery. The true brand palette likely centers on the blue (#1743b8), orange (#f47721), and white (#f8f8f8), with the remaining colors being secondary or contextual.
- Font-family declarations included "din-2014" and "yotpo-widget-font" which are likely from third-party integrations (reviews, widgets) rather than core brand typography. The primary brand fonts appear to be DM Serif Display (headings) and Open Sans (body/UI).
- Hover states for buttons and links were inferred from common patterns — actual hover colors may differ on the live site.
- Error states for forms (validation messages, error icons) were not extractable from static HTML/CSS.
- Dark mode styling is not present in the extracted data — the site appears to be light-mode only.
- The meta theme-color tag was not set, which may affect browser chrome styling on mobile.
- Animation durations, easing curves, and transition properties were not extractable from the static analysis.
- Specific spacing values for component padding and margins were estimated based on common e-commerce patterns and the extracted visual hierarchy — actual values may vary on the live site.
- The "accent-sage" (#7f89b4) and "accent-sage-light" (#acb5d4) colors appear in secondary navigation and footer areas but their exact usage context is unclear from extraction alone.
