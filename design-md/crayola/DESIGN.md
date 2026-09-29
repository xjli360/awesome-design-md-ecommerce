---
version: alpha
name: "Crayola"
source_url: "https://www.crayola.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A riot of saturated color anchored on a clean white canvas, where Crayola Green (#00892d) serves as the brand's primary voltage — a deep, grassy green that appears across primary CTAs, navigation accents, and the site's top banner, while Crayola Yellow (#ffcc33) and Crayola Red (#e71a13) provide the secondary jolts of energy that echo the iconic crayon box. The palette is deliberately loud and unapologetic: purple (#792e88), cyan (#0dcaf0), and hot pink (#e00087) appear as accent swatches across product cards and category badges, creating a visual playground that mirrors the physical product experience. Typography runs Omnes — a rounded, friendly sans-serif with multiple weights (Regular, Semibold, Bold) — at generous sizes that feel approachable rather than authoritative; display text sits at 28–32px in Bold weight, while body copy at 16px in Regular keeps instructions and descriptions clear for young readers. Cards and buttons use soft rounding ({rounded.md} ~12px) that avoids the severity of hard corners, while the search bar and hero CTAs adopt pill shapes ({rounded.full}) for maximum approachability. The site's structure is a grid of colorful product categories — each with its own distinct background swatch — that lets the visitor navigate by color association rather than text labels alone. A persistent top nav in white with green accents carries the Crayola wordmark and a search icon, while the footer collapses into a dense grid of links in muted green (#00502e) on a white ground. The overall effect is a digital space that feels like opening a fresh box of crayons: orderly, vibrant, and full of possibility.

colors:
  primary: "#00892d"
  primary-active: "#006301"
  primary-disabled: "#75b798"
  ink: "#2d2e2f"
  body: "#373b3e"
  muted: "#6a6a6a"
  muted-soft: "#c6c7c8"
  hairline: "#dce7e2"
  hairline-soft: "#e1f3e7"
  canvas: "#ffffff"
  surface-soft: "#fefad5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffcc33"
  accent-yellow-soft: "#fce828"
  accent-red: "#e71a13"
  accent-purple: "#792e88"
  accent-cyan: "#0dcaf0"
  accent-pink: "#e00087"
  accent-blue: "#003c8c"
  accent-blue-light: "#0078c2"
  accent-green-dark: "#00502e"
  accent-green-deep: "#003a17"
  badge-new: "#e00087"
  badge-sale: "#e71a13"
  star-rating: "#feae00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Omnes-Bold', 'Omnes-Semibold', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Omnes-Bold', 'Omnes-Semibold', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Omnes-Semibold', 'Omnes-Bold', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Omnes-Semibold', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.40
    letterSpacing: 0
  title-md:
    fontFamily: "'Omnes-Semibold', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Omnes-Semibold', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'OpenSans-Regular', 'Omnes-Regular', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0
  body-sm:
    fontFamily: "'OpenSans-Regular', 'Omnes-Regular', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'OpenSans-Semibold', 'Omnes-Semibold', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'OpenSans-Regular', 'Omnes-Regular', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Omnes-Bold', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Omnes-Semibold', 'Omnes-Bold', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Omnes-Semibold', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'OpenSans-Regular', 'Omnes-Regular', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Omnes-Semibold', Arial, sans-serif"
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
    rounded: "{rounded.md}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 24px
    height: 48px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 24px
    height: 48px
  button-pill-green:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-pill-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  category-card-featured:
    backgroundColor: "{colors.accent-yellow-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-category:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-banner-alt:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-green-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.canvas}"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    color: "{colors.accent-yellow}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    accentColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  radio:
    accentColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in Crayola Green (#00892d) with white text and 12px rounding. On hover, it shifts to the deeper green (#006301). The disabled state uses a muted sage (#75b798) to signal inactivity without visual noise.

**`button-secondary`** — An outlined variant with a white fill, green text, and a 2px green border. Used for secondary actions like "Learn More" or "View All" alongside primary buttons. Maintains the same 48px height and 12px rounding as the primary.

**`button-accent-yellow`** — A high-energy variant using Crayola Yellow (#ffcc33) with dark ink text. Appears in promotional banners and hero sections where the brand wants to signal fun and creativity rather than transactional intent.

**`button-accent-red`** — An urgent-action variant using Crayola Red (#e71a13) with white text. Reserved for sale badges, clearance sections, and limited-time offers where urgency is appropriate.

**`button-pill-green`** / **`button-pill-yellow`** — Fully rounded pill buttons used for the search bar CTA and hero-section prompts. The pill shape ({rounded.full}) reads as friendly and exploratory, inviting clicks rather than commanding them.

### Navigation
**`top-nav`** — A fixed white bar at 72px height with a 1px green-tinted hairline bottom border. Contains the Crayola wordmark, navigation links in Omnes Semibold, and a search icon. The active link state gains a 3px green bottom border and green text.

**`nav-link`** — Standard navigation links in dark ink (#2d2e2f) with 8px vertical and 16px horizontal padding. The active state switches to green and adds a thick underline, creating a clear wayfinding signal.

### Cards
**`category-card`** — A white card with 20px rounding and a soft green-tinted border. Used to display product categories (e.g., "Coloring Books", "Crayons", "Markers") with an icon or image and a title. The featured variant uses a yellow-tinted background (#fefad5) to highlight promoted categories.

**`product-card`** — A compact white card with 12px rounding and a soft border, used in grid layouts for individual products. Contains a rounded image, product title in Omnes Semibold, and a muted price. The card has 16px internal padding.

### Badges
**`badge-new`** — A hot pink (#e00087) pill badge with uppercase white text, signaling newly added products. Uses 4px vertical and 10px horizontal padding with full rounding.

**`badge-sale`** — A red (#e71a13) pill badge for sale items, following the same shape and sizing as the new badge. The red creates urgency while the pill shape keeps it friendly.

**`badge-category`** — A cyan (#0dcaf0) pill badge used for category labels within product listings. The bright cyan provides a neutral but playful accent that doesn't compete with the primary green.

### Forms
**`text-input`** — Standard text input with white background, 12px rounding, and a green-tinted hairline border. On focus, the border thickens to 2px and turns Crayola Green. Height is 48px with 12px vertical and 16px horizontal padding.

**`select-dropdown`** — Matches the text-input styling for visual consistency, with a custom dropdown arrow in the brand's green.

**`checkbox`** / **`radio`** — Standard form controls with the accent color set to Crayola Green (#00892d). Checkboxes use 4px rounding; radio buttons remain circular.

### Hero
**`hero-banner`** — A full-width banner in Crayola Green with white text, used for the primary hero on the homepage. Contains a headline in display-lg (28px Bold) and a subheadline in body-md, with generous padding (64px vertical, 32px horizontal). An alternate yellow variant exists for secondary hero sections.

### Footer
**`footer`** — A dark green (#00502e) footer with white links and body text. Links are underlined on hover and shift to Crayola Yellow (#ffcc33) for a playful contrast against the dark ground. Padding is generous at 64px vertical and 32px horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to hamburger; hero text reduces to display-md; product cards stack vertically; category cards become full-width; search bar moves to top of page |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains display-lg; category cards in 3-column grid; search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full display-xl; category cards in 4-column grid; search bar in nav with expanded width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with max-width; category cards in 5-column grid; search bar at max 400px width |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav links have 16px horizontal padding to ensure adequate tap area
- Product cards have 16px internal padding to prevent accidental taps on adjacent elements
- Search bar has 48px height for comfortable thumb targeting
- Category cards have 24px padding to create clear tap zones

### Collapsing Strategy
- Top nav collapses to a hamburger menu at < 744px, with the Crayola wordmark and search icon remaining visible
- Product grid collapses from 4 columns to 2 columns at tablet, then to single column at mobile
- Category cards collapse from 5 columns to 3 columns at tablet, then to 2 columns at mobile
- Hero banner text reduces in size at mobile, with the CTA button moving below the headline
- Footer link columns collapse to a single column at mobile, with links stacked vertically

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons (beyond primary-active) could not be reliably extracted; secondary and accent button hover states are inferred from the primary pattern
- Error states for form inputs (red borders, error messages) were not present in the extracted data
- Dark mode is not supported; all extracted colors assume a light theme on white canvas
- Sub-brand palettes (e.g., Crayola Silly Scents, Crayola My First) could not be extracted; only the main brand palette is represented
- The exact font sizes for display-xl and display-lg are inferred from the extracted font declarations and typical brand usage; actual values may vary
- The `swiper-icons` font family suggests a carousel component exists, but its specific styling (arrows, dots, transitions) could not be extracted
- The extracted color list includes many greens (#00892d, #00502e, #003a17, #006301) — the hierarchy among them (primary vs. secondary vs. decorative) is an editorial interpretation based on frequency and context
- The extracted color list also includes blues (#0d6efd, #003c8c, #0078c2, #0a58ca, #86b7fe) that may be framework defaults or checkout-widget colors; they are included as accent-blue variants but may not be brand-intentional
- The extracted color #0dcaf0 (cyan) and #e00087 (pink) are distinctive enough to be intentional brand accents, but their exact usage context (badges, backgrounds, icons) is inferred
- The extracted color #feae00 (star-rating) is assumed to be the rating star color based on typical e-commerce patterns
- The extracted color #fce828 is a slightly different yellow than #ffcc33; both are included as accent-yellow and accent-yellow-soft, but their specific roles are inferred
- The extracted font "Omnes" appears in multiple weights (Regular, Semibold, Bold) and italic variants; the exact weight-to-role mapping (e.g., which weight for body vs. display) is inferred from typical brand usage
- The extracted font "OpenSans" appears in Regular, Semibold, and Italic variants; its role as a secondary body font is inferred from its presence alongside Omnes
- The extracted font "Arial" and "sans-serif" are fallbacks; the primary brand font is assumed to be Omnes based on its prominence in the extracted declarations
