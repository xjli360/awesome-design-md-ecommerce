---
version: alpha
name: "Gotta Groove Records"
source_url: "https://www.gottagrooverecords.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A vinyl pressing plant that communicates its craft through a teal anchor (#52b7bd) — the single brand voltage that appears on every primary CTA, navigation highlight, and product badge — set against a near-white canvas (#fefefe) and deep ink (#0a0a0a) for high-contrast readability. The site uses Lexend and Montserrat for display and body text, with a modest weight range (400–700) that prioritizes legibility over typographic muscle; the brand lets product photography and process descriptions carry the emotional weight. A warm accent palette emerges from the extracted colors: a cautionary orange (#fd7021) for limited-edition or pre-order badges, a deep navy (#0c4d78) for footer backgrounds and secondary surfaces, and a muted gold (#c7b894) for vintage or audiophile-quality callouts. Buttons use soft rounded corners (`{rounded.sm}`) while the search bar and hero CTA adopt pill shapes (`{rounded.full}`), creating a friendly, approachable feel for a technical service. The color list is unusually long — 30+ extracted hexes — suggesting a site that uses many functional UI states (form validation, stock indicators, social icons) rather than a tightly curated brand palette. The most distinctive accent, #52b7bd, is the teal that defines the brand's identity across every page section.

colors:
  primary: "#52b7bd"
  primary-active: "#1583cc"
  primary-disabled: "#cacaca"
  ink: "#0a0a0a"
  body: "#373737"
  muted: "#8a8a8a"
  muted-soft: "#aaaaaa"
  hairline: "#e6e6e6"
  hairline-soft: "#eeeeee"
  canvas: "#fefefe"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#fd7021"
  accent-gold: "#c7b894"
  accent-navy: "#0c4d78"
  accent-red: "#da060b"
  accent-green: "#3adb76"
  accent-yellow: "#ffae00"
  accent-blue: "#2199e8"
  accent-dark-blue: "#003388"
  accent-teal-dark: "#6a878b"
  accent-gray: "#777777"
  accent-gray-dark: "#5f5f5f"
  accent-gray-light: "#a9a9a9"
  accent-white: "#fefefe"
  accent-black: "#313131"
  accent-dark: "#32373c"
  accent-green-dark: "#22bb5b"
  accent-yellow-dark: "#cc8b00"
  accent-orange: "#fd7021"
  accent-navy-light: "#147cc0"
  accent-teal-mid: "#1583cc"
  accent-green-mid: "#00d084"
  accent-blue-mid: "#0693e3"

typography:
  display-xl:
    fontFamily: "'Lexend', 'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lexend', 'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Lexend', 'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Lexend', 'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lexend', 'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Lexend', 'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lexend', 'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    padding: 14px 24px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    border: "1px solid {colors.hairline}"
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
  text-input-error:
    border: "2px solid {colors.accent-red}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    height: 200px
  product-card-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-navy:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
    height: 56px
  hero-cta-hover:
    backgroundColor: "{colors.primary-active}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  badge-warm:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-navy:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  section-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.lg} 0"
    borderBottom: "1px solid {colors.hairline}"
  process-step:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  process-step-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 48px
    width: 48px
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  testimonial-card-accent:
    borderLeft: "4px solid {colors.primary}"
  cta-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.md}"
  cta-banner-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 28px"
    height: 48px
  cta-banner-button-hover:
    backgroundColor: "{colors.surface-soft}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the brand's teal (#52b7bd) on white text. On hover, it shifts to a deeper blue (#1583cc). When disabled, it fades to a light gray (#cacaca) with muted text. The 8px rounded corners (`{rounded.sm}`) keep it friendly without being overly pill-shaped; the pill variant (`button-pill-primary`) uses `{rounded.full}` for hero CTAs and search actions. **`button-secondary`** — A white button with a 2px teal border, used for secondary actions like "Learn More" or "View Details." Active state deepens the border to #1583cc and adds a soft background fill. **`button-tertiary-text`** — A text-only button with teal color, used for inline actions like "Read More" or "Add to Quote." No background or border, just the typography and hover underline.

### Cards
**`product-card`** — The core content card for vinyl products, with a white background, 12px rounded corners (`{rounded.md}`), and a 1px hairline border. On hover, it gains a subtle box shadow and a teal border to indicate interactivity. The card contains an image area (`product-card-image`) with 8px rounded corners and a fixed 200px height, plus badge overlays for status indicators. **`testimonial-card`** — A testimonial block with a white background, 12px rounded corners, and a 4px teal left accent bar for visual hierarchy. Used on the homepage and process pages to build trust. **`process-step`** — A step card in the "How It Works" section, with a soft gray background (#f7f7f7), 12px rounded corners, and a 48px circular icon in teal. Each step has a 1px hairline border and generous padding.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, white background, with a 1px bottom hairline border. Links use `nav-link` typography (Lexend, 16px, weight 600). The active link has a 3px teal bottom border and teal text; inactive links are muted gray (#8a8a8a). The nav collapses to a hamburger menu on mobile. **`footer`** — A deep navy (#0c4d78) footer with white text, using `body-sm` typography. Links are white and turn teal on hover. The footer spans the full width and uses section-level padding.

### Forms
**`text-input`** — Standard form input with white background, 8px rounded corners, 48px height, and a 1px hairline border. On focus, the border thickens to 2px teal. Error state uses a 2px red (#da060b) border. Disabled inputs use a soft gray background (#f7f7f7) with muted text. **`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a soft gray background (#f7f7f7) and 1px hairline border. On focus, the border becomes 2px teal. Used in the header for product search.

### Badges
**`badge-warm`** — An orange (#fd7021) badge with white text, used for "Limited Edition" or "Pre-Order" labels. **`badge-gold`** — A muted gold (#c7b894) badge with dark text, used for "Audiophile Quality" or "Vintage Pressing" callouts. **`badge-navy`** — A deep navy (#0c4d78) badge with white text, used for "New Arrival" or "Staff Pick" labels. **`badge-green`** — A green (#3adb76) badge for "In Stock" indicators. **`badge-red`** — A red (#da060b) badge for "Sold Out" or "Limited Stock" warnings. **`badge-yellow`** — A yellow (#ffae00) badge for "Back in Stock" or "Sale" labels. All badges use uppercase 11px Montserrat at weight 700 with 0.5px letter spacing and 4px rounded corners.

### Hero & CTAs
**`hero-section`** — The full-width hero area with white background, using `display-xl` typography (36px Lexend, weight 700). The hero CTA (`hero-cta`) is a pill-shaped button (`{rounded.full}`) at 56px height with teal background, white text, and 16px/32px padding. On hover, it shifts to the deeper blue (#1583cc). **`cta-banner`** — A teal background banner with white text, using `display-md` typography (24px Lexend, weight 600). The banner button is a white pill with teal text, which turns to a soft gray on hover. Used for mid-page conversion prompts.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero text reduces to 28px; product cards stack vertically; search bar moves to mobile menu; footer links stack; badges reduce to 10px font |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduce padding; hero uses 32px display text; process steps in 2x2 grid; search bar stays in header |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses 36px display text; process steps in horizontal row; search bar prominent in header |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; hero text scales to 40px; additional whitespace around sections; process steps with more padding |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav links have 48px tap targets even on desktop
- Search bar has 48px height for easy tapping
- Badges are at least 24px tall with 8px padding for touch targets
- Product card images have a minimum 200px height for tap-friendly browsing

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer for links
- Product grid reduces from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Process steps rearrange from horizontal row (desktop) to 2x2 grid (tablet) to vertical stack (mobile)
- Footer links stack vertically on mobile, with section headers as accordion toggles
- Hero section reduces padding on mobile (32px instead of 64px) and centers text
- Search bar moves from header to a full-width overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary button and product card hover states were reliably extracted. Secondary button, link, and badge hover states are inferred from common patterns.
- **Error styling**: Text input error state (red border) is inferred from the presence of #da060b in the palette; no specific error message or validation UI was extracted.
- **Dark mode**: No dark mode tokens were found. The site appears to be light-mode only.
- **Sub-brand palettes**: The extracted color list is unusually long (30+ hexes), suggesting many functional UI states (form validation, stock indicators, social icons) rather than a tightly curated brand palette. The true brand primary (#52b7bd) is distinctive, but many colors (e.g., #2199e8, #3adb76, #ffae00) may be framework defaults or third-party widget colors (Shopify Pay, Klarna, Afterpay).
- **Font weights and sizes**: Font sizes and weights are inferred from common web patterns and the presence of Lexend and Montserrat. No exact CSS declarations were extracted beyond font-family names.
- **Spacing values**: Spacing tokens are based on standard design system conventions (8px grid) rather than extracted values.
- **Rounded corner values**: Rounded corner tokens are inferred from common patterns (4px, 8px, 12px, 20px, 32px, 9999px) rather than extracted CSS.
- **Component padding and heights**: These are inferred from standard UI patterns and may not match the live site exactly.
- **Animation and transition**: No animation durations, easing functions, or transition properties were extracted.
- **Iconography**: No icon set or SVG data was extracted. The site likely uses custom icons for process steps and social media.
- **Photography style**: No image analysis was performed. The brand likely uses product photography of vinyl records and pressing equipment.
