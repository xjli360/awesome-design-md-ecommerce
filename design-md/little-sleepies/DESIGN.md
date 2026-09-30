---
version: alpha
name: "Little Sleepies"
source_url: "https://littlesleepies.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A pastel-soft universe built around a single distinctive sage-teal #a9cdd3 that appears nowhere in the generic web palette — this is the brand's true primary, a muted celadon that wraps every product card, badge, and accent element in a calm, bedtime-ready warmth. The canvas is pure white (#ffffff) and the ink is near-black #141414, but the visual center of gravity is the interplay between that sage and a warm butter-yellow #fad588 that surfaces in sale badges, star ratings, and playful accents. A secondary blush-sky #cce8f2 extends the pastel range without competing with the primary. The typography stacks three distinct voices: Inter for body and UI clarity, a rounded custom display face called alana for product titles and headlines (giving a soft, handwritten warmth), and beverly-drive-right for decorative or script moments — likely in logos or limited-edition banners. Corners are universally soft: buttons use {rounded.full} pill shapes, product cards use {rounded.lg} (20px), and the search bar is a pill. The brand avoids hard geometry entirely — even the footer links sit on a {surface-soft} #f6f6f6 background with generous {spacing.section} padding. The overall effect is a digital nursery: safe, tactile in feeling though not in texture, with a color story that reads as "clean bedtime" rather than "clinical baby." The red #d95c5c is the only high-saturation note — used sparingly for error states, sale urgency, or small accent dots — and it lands with deliberate contrast against the pastel field.

colors:
  primary: "#a9cdd3"
  primary-active: "#8bb8c0"
  primary-disabled: "#d4e6ea"
  ink: "#141414"
  body: "#3d3c3d"
  muted: "#545454"
  muted-soft: "#7a7a7a"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#141414"
  accent-warm: "#fad588"
  accent-sky: "#cce8f2"
  accent-red: "#d95c5c"
  accent-purple: "#403940"

typography:
  display-xl:
    fontFamily: "'alana', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-lg:
    fontFamily: "'alana', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'alana', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
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
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  decorative:
    fontFamily: "'beverly-drive-right', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-accent-warm:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-accent-sky:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
  product-card-image:
    rounded: "{rounded.lg}"
  product-card-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 10px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  hero-banner:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.xl}"
  star-rating:
    color: "{colors.accent-warm}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill in the brand's signature sage-teal {colors.primary}. Uses {typography.button-md} in near-black for strong contrast. On hover, shifts to {colors.primary-active} (#8bb8c0). In disabled state, fades to {colors.primary-disabled} with muted text. Used for "Add to Cart," "Shop Now," and checkout entry points.

**`button-secondary`** — An outlined pill on a white canvas with {colors.ink} text. Functions as the secondary action — "Learn More," "View Details," or "Continue Shopping." The border is {colors.hairline} (#dedede). Hover state adds a subtle {colors.surface-soft} background.

**`button-accent-warm`** — A warm butter-yellow pill ({colors.accent-warm}) used for limited-time offers, loyalty perks, or "Treat Yourself" moments. Same pill shape as primary but slightly shorter (40px) with {typography.button-sm}. Reserved for promotional urgency without the red of a sale badge.

**`button-accent-sky`** — A lighter sky-blue pill ({colors.accent-sky}) used for secondary promotional actions like "Subscribe & Save" or "Join the Club." Matches the accent-sky used in hero banners and category pills.

### Cards
**`product-card`** — A white card with {rounded.lg} corners containing a product image, title, price, and optional badge. The image itself inherits the same corner radius. Cards sit on the white canvas with no shadow — the separation comes from the image content and the {spacing.base} gap in grid layouts. On hover, a subtle scale transform (1.02) and a {colors.surface-soft} background on the text area signal interactivity.

**`product-card-badge`** — A small warm-yellow pill overlaid on the product image, typically top-left. Uses {typography.badge} and {rounded.full}. Content is short: "NEW," "BESTSELLER," or "LIMITED." The warm tone reads as friendly and celebratory rather than urgent.

### Navigation
**`nav-bar`** — A fixed 72px white bar with {colors.ink} text using {typography.nav-link}. Left side holds the logo (likely in the decorative beverly-drive-right script). Right side holds icon buttons for search, account, and cart. The cart icon shows a badge count in {colors.accent-red}. On mobile, the nav collapses to a hamburger with a slide-out drawer.

**`category-pill`** and **`category-pill-active`** — Horizontal scrolling strip of pill-shaped category filters below the hero. Inactive pills are {colors.surface-soft} with {colors.body} text. Active pill uses {colors.primary} with {colors.on-primary} text. Used for "Pajamas," "Daywear," "Accessories," "Sale," etc.

### Forms
**`text-input`** — A white input field with {rounded.md} corners and {typography.body-md}. Used in search, newsletter signup, and checkout forms. Focus state shows a {colors.primary} border. Placeholder text is {colors.muted}. Error state uses {colors.accent-red} border and helper text.

**`search-bar-pill`** — A pill-shaped search field on a {colors.surface-soft} background. Used in the nav bar and on the search results page. The pill shape matches the brand's button language. Focus expands the input and shows recent searches.

### Badges & Indicators
**`sale-badge`** — A small red pill ({colors.accent-red}) with white text. Used sparingly for markdowns, clearance, or flash sales. The red (#d95c5c) is the brand's only high-saturation color, so it carries real urgency weight.

**`star-rating`** — Rendered as filled stars in {colors.accent-warm} (#fad588). The warm yellow against the sage-teal primary creates a distinctive brand color pair. Empty stars are {colors.hairline}. Size is 16px for product cards, 14px for review snippets.

### Hero
**`hero-banner`** — A full-width section on a {colors.accent-sky} background with {typography.display-lg} in the alana font. Typically contains a headline, subtext in {typography.body-md}, and a {button-primary} CTA. The sky-blue background (#cce8f2) provides a soft, airy entry point that doesn't compete with the sage-teal primary used in buttons.

### Footer
**`footer-section`** — A full-width block on {colors.surface-soft} (#f6f6f6) with {spacing.section} vertical padding. Links use {typography.link} in {colors.body}. Columns for "Shop," "Help," "About," and "Connect." Social icons are rendered as {icon-button} circles. The footer also contains a newsletter signup with a {text-input} and {button-primary}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, hero text at {typography.display-md} |
| Tablet | 744–1128px | Two-column product grid, expanded nav links, hero at {typography.display-lg} |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero at {typography.display-xl} |
| Wide | > 1440px | Max-width container (1440px) centered, four-column product grid, extended whitespace |

### Touch Targets
- All buttons and interactive pills are minimum 44px height (exceeds WCAG 2.1 minimum).
- Icon buttons in nav are 40px circles with 24px icons.
- Category pills in scroll strip are 36px height — acceptable for touch but borderline; consider 40px on mobile.
- Product card tap targets (title, price, image) are full-card width.

### Collapsing Strategy
- Top nav collapses to hamburger at < 744px. The logo remains centered, cart and account icons stay visible.
- Category pill strip becomes horizontally scrollable with hidden overflow on mobile.
- Footer columns stack vertically on mobile, with accordion-style expandable sections for "Shop," "Help," etc.
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Hero banner reduces font size and padding on mobile; CTA button remains full-width.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font sizes for alana and beverly-drive-right are inferred from typical usage patterns; the extracted CSS only showed font-family declarations without size/weight values for these custom faces. The sizes above are best estimates for a baby-clothing brand.
- Hover and focus states for text inputs, links, and secondary buttons are inferred from common patterns — extracted CSS did not include :hover/:focus pseudo-classes.
- Error state styling (border colors, helper text, iconography) is not present in the extracted data. The red #d95c5c is assumed for error indicators based on its role as the only high-saturation color.
- Dark mode is not supported — the brand uses a white canvas exclusively.
- The accent-purple (#403940) appears in the extracted colors but its specific usage is unclear — possibly for footer text, secondary badges, or decorative elements. It is not used in any defined component above.
- Checkout-specific components (Shopify Pay button, Klarna/Afterpay badges) are not included — their colors may bleed from the extracted palette but are not brand-controlled.
- Star rating exact rendering (filled vs. half-star, SVG vs. unicode) is not confirmed from extraction.
- The decorative font (beverly-drive-right) may only appear in the logo or seasonal banners — its usage in components above is speculative.
- Spacing values for product card internal padding, grid gaps, and hero inner margins are inferred from common e-commerce patterns rather than extracted CSS.
