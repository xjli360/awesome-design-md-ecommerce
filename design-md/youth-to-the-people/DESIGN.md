---
version: alpha
name: "Youth to the People"
source_url: "https://www.youthtothepeople.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A clean, clinical-yet-warm skincare brand that lives in the tension between laboratory precision and botanical vitality. The palette is deliberately restrained — a single dark neutral `#313131` anchors nearly all text and structural elements against a white canvas, creating a crisp, editorial feel that lets product photography and ingredient storytelling take center stage. There is no secondary brand color in the traditional sense; instead, the brand trusts the green of kale, the amber of squalane, and the translucency of their glass bottles to provide the color narrative. Typography runs a system-native stack of `-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, system-ui` — a deliberate choice that reads as modern, accessible, and unpretentious, avoiding the bespoke fashion-font route many competitors take. Buttons and cards use soft rounding (`{rounded.sm}` ~8px for CTAs, `{rounded.md}` ~12px for product cards), never fully pill-shaped, preserving a subtle seriousness. The overall mood is that of a minimalist skincare lab: generous whitespace, thin hairlines (`{colors.hairline}`), muted secondary text (`{colors.muted}`), and a surface-soft background (`{colors.surface-soft}`) that suggests a clean, uncluttered countertop. The brand's voice is direct, ingredient-forward, and slightly aspirational — "superfood skincare" without the hippie aesthetic.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#7a7a7a"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-new: "#313131"
  badge-sale: "#c0392b"
  star-rating: "#313131"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 16px 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.sm} {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  ingredient-highlight:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Bag", "Shop Now", and "Subscribe" actions. Rendered in the brand's dark neutral `{colors.primary}` with white text and a soft 8px radius (`{rounded.sm}`). On hover, it deepens to `{colors.primary-active}` (`#1a1a1a`). The disabled state uses `{colors.primary-disabled}` (`#a0a0a0`) to signal non-interactivity while maintaining readability. Text is set in `{typography.button-md}` — 14px, 600 weight, uppercase with 0.5px letter-spacing for a clean, editorial feel.

**`button-secondary`** — An outlined variant used for less prominent actions like "Learn More" or "View Ingredients". It shares the same dimensions and typography as the primary button but uses a white background with a 1px solid border in `{colors.primary}`. On hover, the background shifts to `{colors.surface-soft}` and the border deepens to `{colors.primary-active}`. This button is the brand's way of offering a secondary action without introducing a second color.

**`button-tertiary-text`** — A text-only button used for inline actions like "Read Reviews" or "See Details". It has no background or border, relying solely on `{colors.primary}` text color and the brand's uppercase button typography. Padding is applied horizontally only to maintain proper touch targets.

### Cards
**`product-card`** — The primary product display unit, used on collection pages and search results. It features a white background with `{rounded.md}` (12px) corners, a product image with rounded top corners, and a structured layout for title, price, and optional badges. The card has no border or shadow — it relies on generous spacing and the contrast between the product image and white background. Titles use `{typography.title-sm}` (16px, 600 weight) and prices use `{typography.body-sm}` (14px, 400 weight) in `{colors.body}`.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a white background and a subtle `1px` bottom border in `{colors.hairline-soft}`. Navigation links use `{typography.nav-link}` (14px, 500 weight, 0.3px letter-spacing). The active link state is indicated by a 2px bottom border in `{colors.primary}`. The nav bar collapses to a hamburger menu on mobile.

### Forms
**`text-input`** — Standard form input used for email signups, search, and account forms. It features a white background, `{rounded.sm}` corners, and a `1px` border in `{colors.hairline}`. On focus, the border transitions to `{colors.primary}`. Error states use `{colors.badge-sale}` (`#c0392b`) for the border. Input text is set in `{typography.body-md}` (16px) for readability.

### Badges
**`badge-new`** and **`badge-sale`** — Small, uppercase labels used to flag product status. The "New" badge uses `{colors.badge-new}` (`#313131`) background with white text, while the "Sale" badge uses `{colors.badge-sale}` (`#c0392b`). Both use `{typography.badge}` (11px, 700 weight, uppercase with 0.5px letter-spacing) and `{rounded.xs}` (4px) for a subtle, non-distracting presence.

### Hero
**`hero-banner`** — The full-width hero section on the homepage and campaign pages. It uses a `{colors.surface-soft}` background with `{colors.ink}` text, set in `{typography.display-xl}` (32px, 700 weight). The hero has a minimum height of 400px and generous padding (`{spacing.section}` vertical, `{spacing.lg}` horizontal). The primary CTA within the hero uses `{typography.button-md}` and `{rounded.sm}`.

### Search
**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a `{colors.surface-soft}` background and `{colors.muted}` placeholder text. It's compact at 40px height, designed to sit in the nav bar or as a standalone element on search-focused pages. Text is set in `{typography.body-sm}` (14px).

### Footer
**`footer-section`** — The site footer uses a `{colors.surface-soft}` background with `{colors.body}` text. Links are set in `{typography.link}` (14px, underlined on hover). The footer is organized into columns with generous padding (`{spacing.section}` vertical) and includes newsletter signup, navigation links, and legal text.

### Accordion
**`accordion`** — Used for FAQ sections and product details. Each accordion item has a white background, a bottom border in `{colors.hairline-soft}`, and a title set in `{typography.title-sm}`. The expanded content area uses `{typography.body-sm}` in `{colors.body}` with `{spacing.sm}` vertical padding. No icon is specified — the brand may use a plus/minus or chevron indicator.

### Ingredient Highlight
**`ingredient-highlight`** — A content block used to feature key ingredients like kale, squalane, or hyaluronic acid. It uses a `{colors.surface-soft}` background with `{rounded.md}` corners and `{spacing.lg}` padding. This component is typically paired with an ingredient image and descriptive text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero banner reduces to 300px min-height; search bar moves to full-width below nav; accordion becomes default for all collapsible sections |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero banner at 350px min-height; search bar remains in nav; footer columns reduce to 2 |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero banner at 400px min-height; search bar in nav; footer columns at 4 |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid may expand to 4 columns; hero banner remains at 400px min-height with larger typography |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px touch target height on mobile and tablet.
- Icon buttons and badge elements have a minimum 32px touch target with adequate padding.
- Product card CTA buttons are at least 48px tall for easy tapping.
- Accordion headers are at least 48px tall to ensure reliable touch interaction.

### Collapsing Strategy
- The primary navigation collapses to a hamburger menu at widths below 744px.
- Product filters collapse into a slide-out drawer on mobile and tablet.
- The hero banner's secondary text and decorative elements are hidden below 744px, retaining only the headline and primary CTA.
- Footer columns collapse from 4 to 2 columns on tablet, and to a single column on mobile.
- Product image galleries switch from horizontal thumbnails to a single swipeable carousel on mobile.
- Multi-step forms (e.g., checkout, subscription) collapse into a single scrollable page on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components beyond primary/secondary buttons could not be reliably extracted — only `button-primary-active` and `button-secondary-active` are documented.
- Error styling for form validation (error messages, iconography, border colors) beyond the `text-input-error` border is not captured.
- The brand's secondary color palette (greens, ambers, botanical tones) is inferred from product photography but not explicitly defined in the codebase — these are used as accent colors in imagery, not as system tokens.
- Dark mode is not supported — the brand uses a white canvas exclusively.
- Sub-brand or campaign-specific palettes (e.g., limited edition drops, holiday collections) are not documented.
- Animation and transition timing values (ease-in-out durations, hover transitions) are not captured.
- Iconography system (cart icon, search icon, menu icon, social media icons) is not defined — the brand appears to use standard SVG icons without a custom icon set.
- Dropdown and select menu styling (custom selects, country selectors) is not documented.
- Modal and overlay styling (lightbox, cart drawer, quick-view) is not captured.
- Loading states (skeleton screens, spinners) and their associated tokens are not defined.
- The brand's approach to accessibility (focus ring colors, ARIA labels, contrast ratios) is not documented.
- Print styles and email-specific styles are not captured.
