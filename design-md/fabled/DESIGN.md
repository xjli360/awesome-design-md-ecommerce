---
version: alpha
name: "The Fabled"
source_url: "https://thefabled.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The Fabled presents itself not as a decor marketplace but as a domain marketplace for premium entertainment and media properties, and its design language reflects that duality — a professional, trustworthy canvas for high-value transactions layered with subtle brand warmth. The palette is anchored by a confident primary green (#0ba348) that appears in the meta theme-color and serves as the brand's signature voltage, appearing alongside a secondary green (#42ad49) that suggests growth and premium positioning. The foundation is deeply neutral — near-black ink (#201d1c), body text (#3c4043), and a muted mid-tone (#a7a9ac) create a serious, legible hierarchy for domain listings and pricing information. The surface layer (#fafafa) and canvas (#f5f5f5) keep the experience airy, while a subtle hairline (#e5e5e5) provides structure without visual noise. What makes The Fabled distinctive is its integration of third-party payment and social brand colors — PayPal blues (#253b80, #179bd7), Facebook (#1877f2), Instagram (#e4405f), Reddit (#ff4500), and various credit card brand colors (#1a1f71, #eb001b, #f79e1b) — suggesting a checkout and sharing ecosystem that must accommodate multiple trusted partners. The typography relies on system-ui and sans-serif stacks with monospace fallbacks (SFMono-Regular, Consolas, Courier New) for technical domain data, while the rounded corners ({rounded.sm} for buttons, {rounded.md} for cards, {rounded.full} for search pills) keep the transactional interface approachable. The overall feel is that of a premium auction house translated to digital — serious enough for six-figure domain deals, warm enough to feel like a partnership.

colors:
  primary: "#0ba348"
  primary-active: "#42ad49"
  primary-disabled: "#a7a9ac"
  ink: "#201d1c"
  body: "#3c4043"
  muted: "#a7a9ac"
  muted-soft: "#e5e5e5"
  hairline: "#e5e5e5"
  hairline-soft: "#f5f5f5"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  domain-highlight: "#01426a"
  paypal-blue: "#253b80"
  paypal-light: "#179bd7"
  facebook: "#1877f2"
  instagram: "#e4405f"
  reddit: "#ff4500"
  visa: "#1a1f71"
  mastercard: "#eb001b"
  amex: "#2478bc"
  google-blue: "#4285f4"
  google-green: "#34a853"
  google-yellow: "#fabb05"
  google-red: "#e94235"
  error: "#e94235"
  success: "#42c31d"
  warning: "#f79e1b"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  domain-mono:
    fontFamily: "SFMono-Regular, Consolas, 'Liberation Mono', Menlo, Monaco, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 56px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(11, 163, 72, 0.15)"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)"
    border: "1px solid {colors.primary}"
  domain-badge:
    backgroundColor: "{colors.domain-highlight}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  price-display:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    fontFamily: "SFMono-Regular, Consolas, 'Liberation Mono', Menlo, Monaco, 'Courier New', monospace"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  social-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  payment-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    height: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the platform, used for key actions like "Buy Domain", "Make Offer", and "Contact Seller". Uses the brand green (#0ba348) on white text with 8px rounded corners ({rounded.sm}). On hover, transitions to the slightly lighter active green (#42ad49). Disabled state uses the muted gray (#a7a9ac) to indicate unavailability. Padding is generous at 12px 24px with a 48px height for comfortable touch targeting.

**`button-secondary`** — An outlined alternative for less prominent actions like "Save Search" or "View Details". Uses a white background with ink text and a subtle hairline border. Maintains the same 48px height and 8px rounded corners for consistency with the primary button.

**`button-tertiary`** — A text-only button for inline actions like "Learn More" or "See All Listings". Uses the primary green for text color with transparent background, making it ideal for placement near content without visual competition.

**`button-pill`** — A fully rounded variant used for filter chips and category tags. Smaller at 40px height with 10px 20px padding, using the primary green background. Active filter pills use this style while inactive ones use a secondary variant with white background and hairline border.

### Cards
**`product-card`** — The core listing card for domain properties. Features a white background with 12px rounded corners ({rounded.md}), 16px padding, and a subtle hairline border. On hover, gains a subtle box shadow and a green border highlight to indicate interactivity. Contains the domain name in monospace font, price in the display typography, and metadata badges.

**`domain-badge`** — A small uppercase badge used to indicate domain attributes like "Premium", "Auction", or "Make Offer". Uses the deep blue (#01426a) background with white text, 4px rounded corners ({rounded.xs}), and tight 2px 8px padding.

### Navigation
**`nav-bar`** — The top navigation bar fixed at 72px height with a white background and bottom hairline border. Contains the brand logo, navigation links using nav-link typography, and a search trigger. Active nav links display a 2px green bottom border and green text color.

### Forms
**`text-input`** — Standard text input for search queries, contact forms, and offer submissions. Features a white background, 48px height, 12px 16px padding, and 8px rounded corners with a hairline border. On focus, the border thickens to 2px and turns green with no outline shift to maintain layout stability.

**`search-bar`** — The prominent search component for domain lookup. Uses fully rounded corners ({rounded.full}) at 56px height with 12px 24px padding. On focus, gains a green border and a subtle green-tinted box shadow to draw attention to the primary action.

### Social & Payment
**`social-button`** — Used for sharing listings or logging in via social platforms. A compact 40px button with white background, hairline border, and 8px rounded corners. Each social platform (Facebook, Instagram, Reddit) uses its respective brand color for the icon while maintaining the neutral button shell.

**`payment-badge`** — Small badges displaying accepted payment methods (Visa, Mastercard, Amex, PayPal). Uses a white background with 4px rounded corners and 4px 8px padding at 32px height. These badges appear in the checkout flow and footer to build trust.

### Hero
**`hero-section`** — The full-width hero area on landing pages and category pages. Uses a soft surface background (#f5f5f5) with generous section-level padding (64px top/bottom, 24px sides). Contains the page title in display-xl, a subtitle in body-md, and the search bar component.

### Footer
**`footer`** — The site footer uses the deep ink color (#201d1c) as background with white text. Contains navigation columns, social links, payment badges, and legal text. Uses body-sm typography with xxl padding (48px) for comfortable spacing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single column layout, hamburger navigation, search bar collapses to icon, product cards stack vertically, hero padding reduces to 32px, footer columns stack |
| Tablet | 744–1128px | Two column product grid, persistent search bar with reduced width, nav links collapse to icons, hero maintains section padding |
| Desktop | 1128–1440px | Three column product grid, full navigation visible, search bar at full width, hero at section padding |
| Wide | > 1440px | Max-width container at 1440px, four column product grid for premium listings, additional whitespace in hero |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch accessibility
- Button components at 48px height exceed minimum touch target requirements
- Search bar at 56px height provides comfortable tap area
- Social buttons at 40px height meet minimum but are paired with visible labels
- Domain badges at 20px height are non-interactive; associated actions use full card tap targets

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Search bar transitions from full input to icon-only trigger on mobile
- Footer navigation columns stack vertically on mobile
- Hero section reduces vertical padding by 50% on mobile
- Category filter strip becomes horizontally scrollable on tablet and mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for social buttons and payment badges could not be reliably extracted
- Error state styling for text inputs (border color, helper text typography) is inferred from the error color token
- Dark mode palette is not present in the extracted data; all tokens assume light mode
- Sub-brand or category-specific color variations (e.g., "Entertainment" vs "Media" domain categories) are not captured
- Loading states and skeleton screen patterns are not documented
- Dropdown and select component styling is absent from extracted data
- Modal/overlay component specifications including scrim opacity and animation timing are missing
- Focus ring styles (outline color, width, offset) are not explicitly defined
- Animation and transition timing tokens (ease-in-out durations) are not available
- The exact font stack for headings versus body could not be distinguished; system-ui is used uniformly with monospace for domain data
