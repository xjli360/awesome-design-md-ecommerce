---
version: alpha
name: "Freestyle"
source_url: "https://freestyle.world"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A baby-care brand that treats chlorine-free diapers as a design problem, not just a sustainability claim. The palette runs on a deep near-black ink (#121212) against a soft off-white canvas (#f1f2f5), with a signature purple (#6638b6) that appears in product badges, accent buttons, and the brand’s “TCF” certification callout — a deliberate departure from the pastel pinks and blues that dominate the category. That purple sits alongside a warm coral (#ee2737) used sparingly for sale tags and urgency markers, and a secondary lavender (#e8c7e8) that softens the brand’s educational content blocks. Typography runs FK Roman Standard for display headlines — a serif with a gentle, almost editorial weight — paired with GroteskNeue for body copy and Gumbo_Regular for accent labels, creating a mix of trustworthy authority and playful clarity. Every product card uses a {rounded.sm} corner radius, while CTAs lean into {rounded.md} to feel approachable without being pill-shaped. The brand’s “Total Chlorine Free” badge appears as a {rounded.xs} tag in {colors.primary} with white text, repeated across the product grid as a consistent visual anchor. The overall mood is clean, clinical in the best sense — like a well-designed pediatrician’s office that happens to sell diapers — with generous whitespace and a restrained use of color that lets the purple do the emotional work.

colors:
  primary: "#6638b6"
  primary-active: "#5d3091"
  primary-disabled: "#c6b9d9"
  ink: "#121212"
  body: "#212121"
  muted: "#909090"
  muted-soft: "#e3e3e3"
  hairline: "#dedede"
  hairline-soft: "#f1f2f5"
  canvas: "#f1f2f5"
  surface-soft: "#f1f2f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-coral: "#ee2737"
  accent-lavender: "#e8c7e8"
  accent-peach: "#f4bc96"
  accent-teal: "#2b657c"
  accent-sky: "#61a2c7"
  accent-plum: "#5f1f5b"
  accent-magenta: "#a85c9d"
  accent-indigo: "#dadaff"
  accent-berry: "#a843a2"
  accent-rust: "#cc4e32"
  accent-dark-teal: "#1b4c62"
  accent-dark-purple: "#020617"

typography:
  display-xl:
    fontFamily: "'FK Roman Standard', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'FK Roman Standard', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'GroteskNeue', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'GroteskNeue', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'GroteskNeue', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'GroteskNeue', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Gumbo_Regular', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.3px
  badge:
    fontFamily: "'GroteskNeue', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'GroteskNeue', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'GroteskNeue', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'GroteskNeue', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'GroteskNeue', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.ink}"
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-badge-tcf:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-educational:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  category-strip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} 0"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe", and "Shop Now" actions. Rendered in the brand’s signature purple (#6638b6) with white text and a 12px corner radius. On hover, it shifts to `{colors.primary-active}` (#5d3091) for a deeper, more grounded feel. The disabled state uses `{colors.primary-disabled}` (#c6b9d9), a muted lavender that signals the action is unavailable without the harshness of a full gray-out.

**`button-secondary`** — A white button with a 1px hairline border, used for "Learn More" and secondary checkout flows. The active state adds a full ink border, creating a clear visual hierarchy without competing with the primary. Padding is intentionally 1px less on each side than the primary to account for the border width, keeping both buttons at 44px height.

**`button-accent-coral`** — A smaller, high-urgency button reserved for sale items and limited-time offers. Uses the coral accent (#ee2737) to create visual tension against the purple system. Typically appears inline within product cards or as a floating badge.

### Cards
**`product-card`** — The core product display unit, a white card with 8px corner radius and 16px internal padding. Each card contains a square aspect-ratio image, product name, price, and one or more badges. The card itself has no border, relying on the soft canvas background (#f1f2f5) to create separation in the grid. On hover, a subtle shadow is applied (not yet tokenized).

**`product-badge-tcf`** — The "Total Chlorine Free" certification badge, rendered as a small purple tag with uppercase white text. This is the brand’s most repeated visual element, appearing on every product that qualifies. The 4px corner radius keeps it sharp and technical, like a certification mark.

**`product-badge-sale`** — A coral variant of the badge system, used to flag discounts and promotions. Same typography and sizing as the TCF badge, but the color shift creates an immediate visual distinction between certification and commercial messaging.

**`product-badge-educational`** — A lavender badge used for informational content blocks, such as "Why TCF Matters" or "Size Guide". The lighter tint (#e8c7e8) keeps educational content from competing with commercial elements.

### Navigation
**`nav-bar`** — A fixed white header at 64px height, containing the brand logo, navigation links in uppercase GroteskNeue, and a cart icon. The nav links use 0.3px letter spacing and 600 weight for clarity at small sizes. On mobile, this collapses to a hamburger menu with a slide-out drawer.

**`category-strip`** — A horizontal scrollable strip below the hero, listing product categories (Diapers, Wipes, Accessories). Active categories are underlined with a 2px purple border, inactive ones remain in muted gray. This strip is sticky on mobile to maintain category navigation as users scroll.

### Forms
**`text-input`** — Standard form input with white background, 8px radius, and a hairline border. On focus, the border doubles to 2px and shifts to the brand purple, providing a clear active state. Used in the subscription builder, checkout, and contact forms.

**`search-bar`** — A dedicated search input with the same dimensions as `text-input` but with placeholder text in muted gray. The search icon sits inside the input on the left, and a clear button appears on the right once text is entered.

### Footer
**`footer-link`** — Standard link styling for the footer section, rendered in muted gray (#909090) to keep the footer visually quiet. Links are 14px with 500 weight, providing enough contrast to be readable without competing with the main content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked hero content, badges become full-width tags |
| Tablet | 744–1128px | Two-column product grid, visible nav links (no hamburger), hero text and image side-by-side |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, expanded hero with larger typography |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, centered content |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Product cards have a minimum tap area of 120px x 120px on mobile
- Category strip items are at least 48px tall for easy horizontal scrolling
- Badges are a minimum of 20px tall, with 8px horizontal padding for tap targets

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer that overlays the content
- Product grid collapses from 4 columns to 1 column on mobile, with images scaling to full width
- Hero section stacks vertically on mobile, with the image appearing below the text and CTA
- Category strip becomes horizontally scrollable on mobile, with snap points at each category
- Accordion sections (FAQ, product details) are collapsed by default on mobile, with the first item open on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, scale) could not be reliably extracted from the live site
- Error styling for form inputs (red border, error message typography) is not present in the extracted data
- Dark mode is not implemented on the current site; all extracted colors assume light mode
- The specific font weights for FK Roman Standard (display) and Gumbo_Regular (caption) are inferred from common web usage; the exact weights used on the live site may vary
- The extracted color list includes many accent colors that may be used in illustrations or photography rather than UI components; the primary palette (ink, body, muted, hairline, canvas, primary) is the most reliable set
- Shopify checkout widget colors (e.g., Klarna pink, Afterpay black) may be present in the extracted hex list but are not part of the Freestyle design system
- The brand’s illustration style and iconography system could not be extracted; all visual elements beyond typography and color are unknown
- Animation durations and easing curves are not available from the static extraction
- The exact spacing between product grid items (gap) could not be determined; the `spacing` block uses standard values inferred from common layout patterns
