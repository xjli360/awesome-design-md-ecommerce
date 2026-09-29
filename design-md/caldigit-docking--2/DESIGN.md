---
version: alpha
name: "CalDigit"
source_url: "https://www.caldigit.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, saturated #003399 blue anchors CalDigit's digital presence — a color that reads as both technical authority and premium restraint, far from the generic tech blues of the extracted palette. This primary blue, paired with a secondary #003388 that adds depth, creates a system that feels engineered rather than decorated. The brand's tagline — "Considerate. Authentic. Design." — manifests in a design language that prioritizes clarity over flash: white canvas (`{colors.canvas}`), crisp Roboto typography, and generous spacing that lets product photography breathe. The extracted palette reveals a surprising range of accent colors (#ff0000 for alerts, #fcb900 for highlights, #00d084 for success states) that suggests a complex product ecosystem — docking stations, hubs, cables, and accessories — each potentially color-coded for quick identification. The meta theme-color of `#000` signals a dark-mode readiness or a footer/hero treatment that plunges into black, creating dramatic contrast against the blue-and-white primary system. The brand's voice is direct and specification-forward, but the design softens this with rounded corners (`{rounded.sm}` on buttons, `{rounded.md}` on cards) that prevent the interface from feeling cold. The extracted font stack — Roboto, Arial — is utilitarian and highly legible, chosen for readability across technical spec sheets and product comparison tables. The overall impression is of a brand that knows its audience (IT professionals, creative pros) and serves them with minimal friction: every pixel justified, every color intentional, every interaction predictable.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99b3e6"
  ink: "#222222"
  body: "#32373c"
  muted: "#555555"
  muted-soft: "#848484"
  hairline: "#dcdcdc"
  hairline-soft: "#ededed"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ff0000"
  accent-yellow: "#fcb900"
  accent-green: "#00d084"
  accent-orange: "#ff6900"
  accent-pink: "#f78da7"
  accent-purple: "#9b51e0"
  accent-teal: "#00a154"
  accent-cyan: "#8ed1fc"
  accent-blue: "#0693e3"
  accent-dark: "#003388"
  accent-gray: "#abb8c3"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "'Roboto', arial, helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    textColor: "{colors.primary-active}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
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
    border: "2px solid {colors.accent-red}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    textColor: "{colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  logo:
    height: 32px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "16/9"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-spec:
    typography: "{typography.spec-value}"
    color: "{colors.muted}"
    padding: "{spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.title-md}"
    color: "{colors.primary}"
    padding: "{spacing.sm} {spacing.base} {spacing.base}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-alt:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-spec:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
    letterSpacing: "0.5px"
  spec-table:
    borderCollapse: collapse
    width: "100%"
  spec-table-row:
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    color: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table-value:
    typography: "{typography.spec-value}"
    color: "{colors.body}"
    padding: "{spacing.sm} {spacing.base}"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
  tab-active:
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.base} {spacing.lg}"
  tab-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    padding: "{spacing.base} {spacing.lg}"
  tab-hover:
    textColor: "{colors.primary}"
  accordion:
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-sm:
    size: 16px
  loading-spinner-lg:
    size: 40px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with `{colors.primary}` blue and white text. Used for "Buy Now", "Add to Cart", and primary form submissions. On hover and active, shifts to `{colors.primary-active}` (#002277). Disabled state uses `{colors.primary-disabled}` (#99b3e6) with reduced opacity. The `{rounded.sm}` (8px) corners give a professional, approachable feel.

**`button-secondary`** — An outlined variant with a white background and 2px `{colors.primary}` border. Used for secondary actions like "Learn More" or "Compare". Active state darkens the border to `{colors.primary-active}`. The outline maintains the same 48px height as the primary button for alignment in button groups.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` for the text. Used for less prominent actions like "Cancel" or "View Details". The active state shifts to `{colors.primary-active}`. Hover state adds a subtle underline for affordance.

**`button-accent-red`** and **`button-accent-green`** — Color-coded action buttons for specific contexts. The red variant (`{colors.accent-red}`) is reserved for destructive actions like "Remove" or "Delete". The green variant (`{colors.accent-green}`) is used for positive confirmations like "Success" or "Complete". Both maintain the same sizing and corner radius as the primary button for consistency.

### Cards
**`product-card`** — The primary content container for product listings. A white card with a 1px `{colors.hairline-soft}` border and `{rounded.md}` (12px) corners. On hover, the border darkens to `{colors.hairline}` and a subtle box shadow lifts the card. The image occupies the top with a 16:9 aspect ratio and rounded top corners only. Below, the title, spec list, and price are stacked with consistent padding. The price is rendered in `{colors.primary}` blue to draw attention.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 72px height with a white background. Links use `{typography.nav-link}` (16px, weight 500) and sit with 16px horizontal padding. The active page link is highlighted in `{colors.primary}` blue. On scroll, a 1px bottom border appears to separate the nav from content. The logo sits at 32px height, maintaining brand presence without dominating.

**`tab-bar`** — A horizontal tab navigation with an underline indicator. Active tabs show `{colors.primary}` text and a 2px bottom border in the same color. Inactive tabs use `{colors.muted}` gray. Used for product category switching or specification toggles.

### Forms
**`text-input`** — Standard text input fields with a white background, 1px `{colors.hairline}` border, and `{rounded.sm}` corners. On focus, the border thickens to 2px and turns `{colors.primary}` blue. Error states use a 2px `{colors.accent-red}` border. Disabled inputs fade to `{colors.surface-soft}` background with `{colors.muted}` text. The 48px height matches button heights for aligned form layouts.

**`select-input`** — Dropdown select fields matching the text input styling. The same 48px height, 1px border, and focus state apply. A custom dropdown arrow in `{colors.muted}` completes the component.

**`textarea`** — Multi-line text input with the same border and focus styling as text inputs. No fixed height, allowing content to dictate size. Used for contact forms and support requests.

### Badges
**`badge`** — Small, uppercase labels used for status indicators. The default uses `{colors.accent-red}` for alerts or warnings. `badge-new` uses `{colors.accent-green}` for new product introductions. `badge-sale` uses `{colors.accent-orange}` for promotional items. `badge-spec` is a softer, pill-shaped variant with a light gray background for technical specifications like "USB-C" or "Thunderbolt 4".

### Footer
**`footer`** — A dark section with `{colors.scrim}` (#000000) background and white text. Links are rendered in `{colors.muted-soft}` (#848484) and brighten to white on hover. Section headings use uppercase with letter spacing for hierarchy. The footer contains product categories, support links, and legal information in a multi-column layout.

### Spec Table
**`spec-table`** — A two-column table for product specifications. Rows are separated by a soft hairline border. Labels use uppercase `{typography.spec-label}` in `{colors.muted}` gray, while values use `{typography.spec-value}` in `{colors.body}`. This creates a clean, scannable format for technical data like port types, power delivery, and compatibility.

### Accordion
**`accordion`** — Expandable sections for FAQ or detailed product information. Each item has a bottom border for separation. The header uses `{typography.title-md}` in `{colors.ink}` with a clickable area. On expansion, content appears below with `{typography.body-sm}` in `{colors.body}`. A chevron icon rotates on open/close states.

### Tooltip
**`tooltip`** — A small, dark overlay for supplementary information. Uses `{colors.ink}` background with white text and `{rounded.xs}` (4px) corners. Appears on hover of icons or truncated text. Positioned above or below the trigger element with a small arrow.

### Loading States
**`loading-spinner`** — A circular progress indicator in `{colors.primary}` blue. Available in three sizes: small (16px) for inline use, medium (24px) for button loading states, and large (40px) for full-section loading. The spinner animates continuously at a moderate speed.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; spec tables become stacked label-value pairs; footer collapses to single column; hero text reduces to `{typography.display-md}`; buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; spec tables remain two-column; footer uses 2-3 columns; hero uses `{typography.display-lg}` |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; spec tables at full width; footer uses 4 columns; hero at full `{typography.display-xl}` |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to 4 columns; additional whitespace on sides; hero content max-width constrained |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch targets on mobile
- Product card tap targets extend to full card area
- Accordion headers have 48px minimum tap height
- Tab bar items have 48px minimum tap height
- Search bar has 48px tap height with 16px internal padding

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-in drawer for navigation links
- Product filters collapse to a modal or bottom sheet on mobile
- Spec tables collapse to stacked label-value pairs below 744px
- Multi-column footers collapse to single column below 744px
- Accordion sections are used for FAQ and detailed specs on all breakpoints, but become the primary content structure on mobile
- Image galleries collapse to single-image carousel with dot indicators on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color palette includes many framework-default and third-party widget colors (Shopify Pay, Klarna, Afterpay, social icons) that may not represent the brand's true design system. The primary blue (#003399) and secondary blue (#003388) are the most distinctive and likely authentic, but the remaining 20+ colors should be validated against the actual brand style guide.
- Font weights beyond the extracted "Roboto, arial" are inferred from common web usage. The actual weight values (300, 400, 500, 600, 700) should be confirmed.
- Specific hover, active, and focus states for all components are inferred from common patterns. Actual interaction states (box-shadows, transitions, color shifts) need direct extraction.
- Error, success, and warning styling for forms is inferred from the accent color palette. Actual validation patterns (icon placement, message styling, timing) are unknown.
- Dark mode styling is not confirmed. The meta theme-color of #000 suggests dark mode readiness, but no dark mode tokens were extracted.
- Animation durations, easing curves, and transition properties are not extracted. All motion design is inferred from common patterns.
- The brand's iconography style and usage guidelines are unknown. The extracted palette includes many accent colors that may correspond to icon categories or product lines.
- Typography hierarchy beyond the extracted font family is inferred. Actual heading sizes, weights, and line heights should be verified against the brand's design files.
- Component spacing values (padding, margins, gaps) are inferred from common e-commerce patterns. Actual spacing tokens need direct measurement from the live site.
- The brand's logo usage, minimum size, and clear space requirements are unknown.
- Print and accessibility-specific styles (focus outlines, high contrast mode, reduced motion) are not documented.
