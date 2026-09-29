---
version: alpha
name: "Elgato"
source_url: "https://www.elgato.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, saturated teal (#093836) anchors Elgato's streaming-hardware ecosystem — not as a background, but as the primary brand voltage that fills every key visual, product shot, and hero section. This is a brand that lives in the dark: its canvas is near-black (#111111), its surfaces are layered grays (#323232, #414141, #525252), and its accents are neon-bright — a cyan (#40ddd3) that reads like a live-stream chat glow, a lime (#6ff787) that could be a key-light indicator, and a warning red (#e12a40) for alerts and recording states. The typography stack is a hybrid of display and utility: ABC Ginto Discord Nord (the Discord-derived face) for bold headlines and badges, HelveticaNeueLTPro for body and interface copy, and Bebas Neue Pro for condensed numeric displays. Buttons and interactive elements use sharp, minimal radii — the brand avoids pill shapes in favor of crisp rectangles with {rounded.sm} (8px) corners, reinforcing a pro-audio/studio aesthetic. The color palette is unusually broad for a hardware brand, with 30+ extracted hexes that include a deep blue (#0c2588), a bright blue (#204cfe), a purple (#a638fe), and multiple greens (#55f578, #2eff82, #49f5eb) — suggesting a system where each product line or software feature gets its own accent color. The overall feel is that of a control surface: dark, legible, high-contrast, with color used sparingly but with high saturation to signal state changes, alerts, and brand moments.

colors:
  primary: "#093836"
  primary-active: "#0a4a47"
  primary-disabled: "#1a5a57"
  ink: "#111111"
  body: "#323232"
  muted: "#595959"
  muted-soft: "#858585"
  hairline: "#c8c8c8"
  hairline-soft: "#dbdbdb"
  canvas: "#111111"
  surface-soft: "#323232"
  surface-card: "#414141"
  on-primary: "#ffffff"
  accent-cyan: "#40ddd3"
  accent-lime: "#6ff787"
  accent-green: "#55f578"
  accent-bright-green: "#2eff82"
  accent-blue: "#204cfe"
  accent-deep-blue: "#0c2588"
  accent-purple: "#a638fe"
  accent-red: "#e12a40"
  accent-bright-red: "#ff3c4e"
  accent-soft-red: "#ff7073"
  accent-warm-red: "#e55e5a"
  accent-orange: "#f99000"
  accent-cyan-light: "#49f5eb"
  accent-cyan-bright: "#1cddff"
  surface-light: "#eaeaea"
  surface-mid: "#d8d8d8"
  surface-mid-light: "#f0f0f0"
  surface-blue-tint: "#eaf2ff"
  surface-gray-light: "#f1f3f5"
  gray-100: "#646464"
  gray-200: "#525252"
  gray-300: "#414141"
  gray-400: "#9e9e9e"

typography:
  display-xl:
    fontFamily: "'ABC Ginto Discord Nord', 'HelveticaNeueLTPro-Bd', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'ABC Ginto Discord Nord', 'HelveticaNeueLTPro-Bd', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ABC Ginto Discord Nord', 'HelveticaNeueLTPro-Bd', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'ABC Ginto Discord Nord', 'HelveticaNeueLTPro-Bd', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'HelveticaNeueLTPro-Roman', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'HelveticaNeueLTPro-Roman', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'HelveticaNeueLTPro-Roman', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'HelveticaNeueLTPro-Roman', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'HelveticaNeueLTPro-Roman', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'HelveticaNeueLTPro-Roman', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'ABC Ginto Discord Nord', 'HelveticaNeueLTPro-Bd', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'HelveticaNeueLTPro-Bd', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'HelveticaNeueLTPro-Bd', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'HelveticaNeueLTPro-Roman', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'HelveticaNeueLTPro-Bd', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  display-number:
    fontFamily: "'Bebas Neue Pro SmE Rg', Arial, sans-serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1
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
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.accent-cyan}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 24px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-cyan}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: 80px 24px
  badge-new:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-featured:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-cyan}"
    typography: "{typography.link}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-header:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: 24px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's deep teal (#093836). Used for key actions like "Add to Cart", "Buy Now", and "Learn More". On hover, shifts to a slightly lighter teal (`{colors.primary-active}`). When disabled, the background fades to a muted teal (`{colors.primary-disabled}`) and text drops to `{colors.muted}`. Text is bold HelveticaNeueLTPro-Bd at 14px with 0.5px letter-spacing, giving it a crisp, technical feel.

**`button-secondary`** — A dark surface card (`{colors.surface-card}`) button for secondary actions like "Compare" or "Details". Hover state shifts to `{colors.surface-soft}`. Maintains the same typography and height as primary for visual consistency in forms and product grids.

**`button-accent-cyan`** — A high-energy accent button using the brand's signature cyan (#40ddd3). Used for "Stream Now", "Get Started", or other action-oriented CTAs. Text is dark (`{colors.ink}`) for contrast. This button signals a moment of activation or live status.

**`button-accent-lime`** — A lime-green (#6ff787) accent button, used for "Download", "Free Trial", or "New Feature" CTAs. Like the cyan variant, text is dark for maximum contrast against the bright background.

**`button-ghost`** — A transparent-background button with white text, used in hero sections and on dark image backgrounds. Hover state adds a subtle white border or background tint (exact hover treatment not confirmed from extraction).

### Cards
**`product-card`** — A dark card (`{colors.surface-card}`) with 8px rounded corners and 16px padding. Contains product image, title, price, and action buttons. On hover, the card background shifts to `{colors.surface-soft}` for a subtle lift effect. Text is body-sm (14px) for descriptions, with product names using title-sm (16px, 600 weight).

**`hero-section`** — Full-width dark canvas section with 80px vertical padding. Uses display-xl (48px) for the main headline, with body-md for supporting text. The hero often features product imagery with the brand's teal or cyan as an accent overlay or gradient.

### Navigation
**`nav-bar`** — A fixed 64px dark navigation bar with white text. Links use nav-link typography (14px, 700 weight, 0.5px letter-spacing). Active links and hover states shift to the accent cyan (`{colors.accent-cyan}`). Inactive links are muted (`{colors.muted}`). The bar includes the Elgato logo on the left and navigation links on the right.

### Forms
**`text-input`** — Dark input fields with a surface-card background, 1px hairline border, and 8px rounded corners. On focus, the border switches to a 2px accent-cyan stroke. Height is 44px with 12px/16px padding for comfortable typing. Placeholder text uses `{colors.muted}`.

### Badges
**`badge-new`** — A small lime-green badge for "NEW" labels on products and features. Uses uppercase bold typography at 11px with 0.5px letter-spacing. 4px rounded corners and 2px/8px padding keep it compact.

**`badge-sale`** — A red badge for sale or discount indicators. Same dimensions and typography as badge-new, but with the brand's alert red (`{colors.accent-red}`) background.

**`badge-featured`** — A cyan badge for "Featured" or "Recommended" labels. Same structure, using the accent cyan for visibility.

### Footer
**`footer-section`** — A dark footer with 48px vertical padding. Links use muted gray text that shifts to accent cyan on hover. Dividers between sections use the hairline color. Typography is body-sm (14px) for link text and caption (12px) for copyright and legal text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layouts, stacked product cards, hamburger navigation, reduced hero padding (40px), smaller display typography (display-xl drops to 32px) |
| Tablet | 744–1128px | Two-column product grids, expanded navigation, hero padding at 60px, display-xl at 40px |
| Desktop | 1128–1440px | Three-column product grids, full navigation visible, hero at full 80px padding, display-xl at 48px |
| Wide | > 1440px | Max-width container (1440px) centered, additional whitespace on sides, product grids may expand to 4 columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon-only buttons (search, cart, menu) are 44x44px minimum
- Product card tap targets are the full card surface
- Navigation links have 48px minimum tap height on mobile

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px
- Product grids collapse from 3 columns to 2 at tablet, to 1 at mobile
- Hero sections stack vertically on mobile (image above text)
- Footer link columns collapse to single column below 744px
- Search bar collapses to icon-only on mobile, expanding on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is unusually large (30+ hexes), suggesting a complex system with product-line-specific accents, software UI states, and marketing gradients. The true primary brand color (#093836) was identified by frequency and distinctiveness, but the brand may use multiple primaries across different contexts (hardware vs. software vs. marketing).
- Font weights and exact sizing for the extracted font families (ABC Ginto Discord Nord, HelveticaNeueLTPro, Bebas Neue Pro) are inferred from common web usage patterns, not extracted from CSS. The actual weight values may differ.
- Hover, active, and focus states for most components are estimated based on common dark-theme patterns. Exact transition durations, box-shadows, and border treatments are not confirmed.
- Error states, validation styling, and form feedback patterns are not present in the extraction.
- Dark mode is the default (and only observed) theme. A light mode variant may exist but was not detected.
- The brand's use of gradients, overlays, and image treatments (e.g., product shots on dark backgrounds with cyan edge lighting) is described from visual observation but not tokenized.
- Sub-brand or product-line-specific color tokens (e.g., for Stream Deck, Facecam, Key Light) may exist but are not separable from the general palette.
- The extracted font list includes "Apple Color Emoji" and monospace fonts (Consolas, Courier New, Liberation Mono, Menlo, Monaco) which are likely for code blocks or system UI, not brand typography.
