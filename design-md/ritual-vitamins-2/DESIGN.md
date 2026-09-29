---
version: alpha
name: "Ritual"
source_url: "https://ritual.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy anchor (#142b6f) and a sharp marigold accent (#ffd600) define a brand that treats supplementation as a daily ritual of transparency, not a quick fix. The palette is deliberately restrained — a cool, clinical blue family (#a1aac5, #62719f, #0b38bd) against warm off-whites (#fef6eb, #fcf8ee, #f6ede0) and a near-black ink (#141414) — creating a visual language that feels both scientific and approachable. CircularXX, a geometric sans-serif with a distinctive single-story 'a', runs across the entire experience, lending a modern, almost pharmaceutical precision to headlines and body copy alike. Buttons use a full navy fill with marigold hover states, while product cards float on soft canvases (#eaeef0) with pill-shaped badges and ingredient callouts. The brand's signature move is the "traceable" ingredient reveal — a toggle or accordion that exposes the source, form, and rationale behind each capsule component, often accompanied by a small circular icon or micro-illustration. Generous whitespace, a subdued secondary palette of warm neutrals (#f5f7f8, #e8e6e5, #dedede), and a single high-contrast accent (#c83d1e for error or sale) keep the interface calm and trustworthy. The checkout flow leans on Shopify's native widgets, but the brand's own UI — subscription management, product detail pages, and the "Why Ritual" explainer — feels like a premium health journal: structured, evidence-backed, and never shouty.

colors:
  primary: "#142b6f"
  primary-active: "#0b38bd"
  primary-disabled: "#a1aac5"
  ink: "#141414"
  body: "#2b2727"
  muted: "#717171"
  muted-soft: "#9a9795"
  hairline: "#d1cfce"
  hairline-soft: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f5f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffd600"
  accent-marigold-soft: "#ffef99"
  accent-terracotta: "#c83d1e"
  accent-sage: "#4c840d"
  accent-amber: "#db7f16"
  accent-navy-light: "#62719f"
  accent-cream: "#fef6eb"
  accent-cream-light: "#fcf8ee"
  accent-warm-gray: "#eaeef0"
  accent-warm-gray-dark: "#b3b2b1"
  accent-purple: "#4b3dc4"
  accent-gold: "#e4c25e"
  accent-gold-soft: "#fff7cc"
  accent-brown: "#ab4824"
  accent-brown-light: "#f6ede0"

typography:
  display-xl:
    fontFamily: "'CircularXX', 'Dutch801 Rm BT Headline', 'Inter', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.2px
  display-lg:
    fontFamily: "'CircularXX', 'Dutch801 Rm BT Headline', 'Inter', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.72px
  display-md:
    fontFamily: "'CircularXX', 'Dutch801 Rm BT', 'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.56px
  display-sm:
    fontFamily: "'CircularXX', 'Dutch801 Rm BT', 'Inter', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.22px
  title-lg:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.15px
  link:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  ingredient-label:
    fontFamily: "'CircularXX', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
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
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-marigold-hover:
    backgroundColor: "{colors.accent-marigold-soft}"
    textColor: "{colors.ink}"
  button-pill-navy:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-terracotta}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    size: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    size: 20px
  radio-checked:
    border: "6px solid {colors.primary}"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
  toggle-switch-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    size: 20px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(20, 43, 111, 0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(20, 43, 111, 0.1)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-badge:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  product-card-badge-sage:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  product-card-badge-terracotta:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  ingredient-accordion:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  ingredient-accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  ingredient-accordion-icon:
    size: 24px
    color: "{colors.primary}"
  ingredient-detail-row:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  ingredient-detail-label:
    typography: "{typography.ingredient-label}"
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.accent-cream}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xl}"
  hero-section-navy:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-headline-on-dark:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subheadline:
    typography: "{typography.body-lg}"
    textColor: "{colors.muted}"
  hero-subheadline-on-dark:
    typography: "{typography.body-lg}"
    textColor: "{colors.accent-warm-gray}"
  hero-cta:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.accent-warm-gray}"
  footer-link-hover:
    textColor: "{colors.accent-marigold}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  search-icon:
    color: "{colors.muted}"
    size: 20px
  badge-new:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-vegan:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  subscription-toggle-active:
    backgroundColor: "{colors.accent-cream-light}"
    border: "2px solid {colors.primary}"
  subscription-toggle-label:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  subscription-toggle-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  subscription-toggle-savings:
    typography: "{typography.caption-sm}"
    textColor: "{colors.accent-sage}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 6px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  progress-bar-fill-complete:
    backgroundColor: "{colors.accent-sage}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  tooltip-arrow:
    color: "{colors.ink}"
  modal-overlay:
    backgroundColor: "rgba(20, 43, 111, 0.5)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 32px rgba(20, 43, 111, 0.15)"
  modal-close:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    size: 32px
  modal-close-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  accordion-icon:
    color: "{colors.primary}"
    size: 20px
  rating-stars:
    color: "{colors.accent-marigold}"
    size: 16px
  rating-stars-empty:
    color: "{colors.hairline}"
  rating-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  avatar:
    rounded: "{rounded.full}"
    size: 40px
  avatar-small:
    rounded: "{rounded.full}"
    size: 32px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  spinner:
    color: "{colors.primary}"
    size: 24px
  spinner-on-dark:
    color: "{colors.on-primary}"
    size: 24px
  skeleton:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
  skeleton-text:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
    height: 14px
  skeleton-avatar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    size: 40px

## Components

### Buttons
**`button-primary`** — The workhorse CTA, a deep navy fill (#142b6f) with white text and 8px rounding. Hover shifts to a brighter navy (#0b38bd), disabled drops to a muted blue-gray (#a1aac5). Used for "Add to Cart", "Subscribe", and "Get Started" actions. The 48px height and 28px horizontal padding give it a solid, confident presence.

**`button-secondary`** — An outlined variant with a white fill, navy text, and a 2px navy border. Hover lightens the background to the soft surface tint (#f5f7f8) and deepens the border to the active navy. Used for "Learn More" and "Compare" actions where the primary button is already present.

**`button-accent-marigold`** — The high-energy accent button, marigold fill (#ffd600) with dark ink text. Hover softens to the lighter marigold tint (#ffef99). Used sparingly for the most important conversion actions, like "Start Your Ritual" on hero sections, where it creates a bright focal point against the navy-heavy palette.

**`button-pill-navy`** — A fully rounded pill variant of the primary button, used for smaller, inline actions like "View Details" on product cards or "Add to Bundle". The pill shape signals a lighter-weight interaction than the full primary button.

**`button-pill-outline`** — A transparent pill with a 1px navy border and navy text. Used for secondary inline actions like "Compare" or "Learn More" on product cards, where a full button would feel too heavy.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Skip". Hover adds a subtle background tint (not defined here, but typically the surface-soft color).

### Cards
**`product-card`** — The core product display unit, a white card with 12px rounding, a soft hairline border, and 16px padding. Hover elevates with a subtle shadow and a slightly stronger border. Contains the product image (1:1 aspect ratio, 8px rounding), a marigold or sage badge for promotions or attributes, the product title, and the price. The card is designed to work in a 3- or 4-column grid on desktop, collapsing to 2 columns on tablet and a single column on mobile.

**`product-card-badge`** — Small, fully rounded pills that sit on the top-left of the product image. Three variants exist: marigold (#ffd600) for "New" or "Best Seller", sage (#4c840d) for "Vegan" or "Sustainable", and terracotta (#c83d1e) for "Sale" or "Limited Edition". Text is uppercase, 11px, bold.

### Navigation
**`nav-bar`** — A fixed white header, 72px tall, with a soft bottom border. Contains the brand logo on the left, navigation links in the center, and utility icons (search, account, cart) on the right. On scroll, a subtle shadow appears. Active nav links get a 2px navy bottom border and navy text; inactive links are muted gray.

**`nav-link-active`** — The active navigation state, distinguished by navy text and a 2px navy underline. The underline is the primary indicator of the current section.

**`nav-link-inactive`** — Inactive navigation links use the muted gray (#717171) to recede visually, keeping focus on the active section and the brand logo.

### Forms
**`text-input`** — Standard text input with a white fill, 48px height, 8px rounding, and a 1px hairline border. Focus state swaps to a 2px navy border. Error state uses a 2px terracotta border (#c83d1e). Used for email, password, and search fields.

**`select-dropdown`** — Matches the text-input styling but includes a dropdown arrow icon. Used for quantity selectors, subscription frequency, and country selection in the footer.

**`checkbox`** — A 20px square with 4px rounding, white fill, and a 2px hairline border. Checked state fills with navy and uses a white checkmark icon. Used in subscription forms and ingredient preference selectors.

**`toggle-switch`** — A 44x24px pill with a white knob. Active state fills with navy. Used for subscription auto-renewal and notification preferences.

### Ingredient Accordion
**`ingredient-accordion`** — A signature Ritual component, this is a collapsible card on the product detail page that reveals the traceable source of each ingredient. The header shows the ingredient name and a small icon (a leaf, a lab flask, or a location pin). Expanded content includes a source location, the form of the ingredient (e.g., "Vitamin D3 from lichen"), and a brief rationale. The card has a soft background (#f5f7f8), 8px rounding, and a subtle border.

**`ingredient-detail-row`** — A single row within the expanded accordion, showing a label (e.g., "Source", "Form", "Why") in uppercase 12px muted text and the value in 14px body text. Rows are separated by 8px vertical padding.

### Hero Section
**`hero-section`** — The full-width hero banner, typically with a cream background (#fef6eb) and dark text. The navy variant uses the primary navy background with white text. Contains a headline (48px, bold), a subheadline (18px, muted), and a marigold CTA button. The hero is designed to be image-heavy, with product photography or lifestyle imagery taking up roughly 50% of the width on desktop.

**`hero-section-navy`** — The dark variant of the hero, used for product launches or limited-edition drops. The navy background creates a dramatic contrast for the marigold CTA and white text.

### Footer
**`footer`** — A full-width navy footer with white text and warm-gray links. Organized into columns for "Shop", "Learn", "About", and "Support". Social media icons appear in the bottom row. Links hover to marigold. The footer is dense but well-spaced, with 48px vertical padding.

### Badges
**`badge-new`** — A small marigold pill used to flag new products or features. Uppercase 11px bold text on a marigold background. Placed on product cards, navigation items, or hero sections.

**`badge-sale`** — A terracotta pill for sale or limited-time offers. The high-contrast red-orange draws immediate attention.

**`badge-vegan`** — A sage green pill for vegan or plant-based certifications. The green aligns with the brand's sustainability messaging.

### Subscription Toggle
**`subscription-toggle`** — A pair of cards (one for one-time purchase, one for subscription) that let the user choose their purchase model. The active card has a cream background (#fcf8ee) and a 2px navy border. The subscription card shows the per-unit price and a "Save X%" label in sage green. This component is critical to Ritual's business model and is prominently placed on the product detail page.

### Progress Bar
**`progress-bar`** — A thin (6px), fully rounded progress bar used in the subscription onboarding flow and the checkout process. The fill is navy, transitioning to sage green when complete. The background is the soft hairline color.

### Tooltip
**`tooltip`** — A dark, rounded tooltip with white text, used for ingredient explanations and feature descriptions. The small size (12px) and subtle rounding keep it unobtrusive.

### Modal
**`modal-overlay`** — A semi-transparent navy overlay (50% opacity) that darkens the page behind a modal. The modal content is white with 12px rounding, 32px padding, and a soft shadow. The close button is a small, circular icon button with a soft background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero becomes full-width image with text below; ingredient accordions are full-width; subscription toggle stacks vertically; footer collapses to single column with accordion-style sections |
| Tablet | 744–1128px | Two-column product grid; nav shows 3-4 links with "More" dropdown; hero uses 60/40 text-to-image split; ingredient accordions use two-column grid; subscription toggle remains side-by-side |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero uses 50/50 split; ingredient accordions use three-column grid; standard layout as designed |
| Wide | > 1440px | Max-width container (1440px) with centered content; product grid can expand to four columns; hero remains centered with max-width content area; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile and tablet.
- Nav links have 48px touch height on mobile (hamburger menu items).
- Product card CTAs ("Add to Cart", "Subscribe") are 48px tall to meet touch guidelines.
- Toggle switches have 44px touch width.
- Accordion headers have 48px touch height.
- Modal close buttons are 44x44px on mobile.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at < 744px.
- Product grid collapses from 3 columns to 2 at 744px, and to 1 at < 744px.
- Hero section collapses from side-by-side to stacked at < 744px.
- Footer sections collapse to accordion-style expandable panels at < 744px.
- Ingredient accordion grid collapses from 3 columns to 2 at 744px, and to 1 at < 744px.
- Subscription toggle collapses from side-by-side to stacked at < 744px.
- Multi-step checkout collapses to a single-column layout at < 744px.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary and secondary button hover states were extracted. Hover states for nav links, footer links, product cards, and other interactive elements are inferred from common patterns but not confirmed from the live site.
- **Error states**: Only the text-input error state (terracotta border) is confirmed. Form validation error messages, inline error styling, and error summary components are not extracted.
- **Focus states**: Focus ring styles (color, width, offset) for keyboard navigation are not extracted. Assumed to be a 2px navy outline with a 2px offset, but not confirmed.
- **Dark mode**: No dark mode styles were found. The brand appears to be light-mode only at this time.
- **Sub-brand palettes**: Ritual may have sub-brands or limited-edition color palettes (e.g., for pregnancy, teen, or men's lines) that were not captured in the extraction.
- **Animation and transition**: No timing, easing, or animation values were extracted. Assumed to use 200-300ms ease-in-out transitions for hover and focus states.
- **Iconography**: While the brand uses custom icons (ingredient icons, social icons, UI icons), no specific icon set or sizing was extracted. The ingredient-accordion-icon and search-icon sizes are estimated.
- **Typography weights**: The exact font weights for CircularXX are inferred from common usage (400, 500, 600, 700) but not all weights were confirmed from the extracted CSS. The Dutch801 Rm BT font appears to be a secondary or headline font, but its usage context is unclear.
- **Shopify-specific UI**: The checkout flow uses Shopify's native widgets (Shopify Pay, Klarna, Afterpay buttons), which have their own color palettes and styling. These are not part of Ritual's design system and are not documented here.
- **Social media icon colors**: The extracted color list includes several colors that may be from social media icons (e.g., #4b3dc4 for a purple icon). These are not brand colors and have been excluded from the palette.
- **Stock image dominant tones**: Some extracted colors (e.g., #ab4824, #f6ede0) may be dominant tones from product or lifestyle photography rather than intentional brand colors. They are included as accent colors but may not be used consistently across the site.
