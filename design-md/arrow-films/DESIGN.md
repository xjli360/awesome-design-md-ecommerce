---
version: alpha
name: "Arrow Films"
source_url: "https://www.arrowfilms.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, obsessive catalog of cult, classic, and horror cinema, Arrow Films wraps its collection in a stark white canvas (#f8f8f8) and a primary blue (#0052b4) that reads more like a scholarly monograph than a streaming service. The brand's visual system is built on high-contrast typography — Aktiv Grotesk and Bigger Display in generous sizes — against near-white surfaces (#eeeeee, #f2f2f2), with red accents (#d80027, #e31f26) reserved for price tags, badges, and limited-edition markers that signal urgency without shouting. The extracted palette reveals a brand that trusts its film stills and poster art to carry emotional weight: the grays (#e5e5e5) and soft whites create a gallery-like grid where product cards sit at {rounded.sm} and the primary CTA button uses a full-height blue rectangle at {rounded.xs}. A secondary teal (#00a2a9) and purple (#ad3381) appear in sub-brand badges and genre tags, suggesting a taxonomy system that categorizes by director, label, and restoration series rather than generic "action" or "drama." The search bar, navigation, and footer all share the same hairline-thin border (#e5e5e5) and 16px base spacing, creating a rhythm that feels editorial — like browsing a film journal that happens to sell Blu-rays.

colors:
  primary: "#0052b4"
  primary-active: "#003d8a"
  primary-disabled: "#b3c9e6"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e5e5e5"
  hairline-soft: "#eeeeee"
  canvas: "#f8f8f8"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#d80027"
  accent-red-active: "#b30020"
  accent-teal: "#00a2a9"
  accent-purple: "#ad3381"
  accent-green: "#0d9c4a"
  accent-yellow: "#d5cd27"

typography:
  display-xl:
    fontFamily: "'Bigger Display', 'Aktiv Grotesk Extended', 'Aktiv Grotesk', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Bigger Display', 'Aktiv Grotesk Extended', 'Aktiv Grotesk', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Aktiv Grotesk Extended', 'Aktiv Grotesk', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Aktiv Grotesk Extended', 'Aktiv Grotesk', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Aktiv Grotesk', sans-serif"
    fontSize: 15px
    fontWeight: 500
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  button-accent-red-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 0
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-info:
    padding: "{spacing.md} {spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-red}"
  badge-limited-edition:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-format:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-label:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.display-sm}"
    textColor: "{colors.muted-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid blue (#0052b4) rectangle with {rounded.xs} corners and white text in Aktiv Grotesk 600. Used for "Add to Basket," "Pre-order," and "Subscribe." On hover, shifts to `primary-active` (#003d8a). Disabled state uses `primary-disabled` (#b3c9e6) with white text at 50% opacity.

**`button-secondary`** — An outlined variant with white background, ink text, and a 1px hairline border. Matches the primary button's height and padding but reads as a lower-priority action — "View Details," "Browse More." Hover adds a subtle shadow; disabled state uses muted text on surface-soft background.

**`button-accent-red`** — Reserved for high-urgency actions like "Limited Edition" pre-orders or flash sales. Uses `accent-red` (#d80027) background with white text. Hover darkens to `accent-red-active` (#b30020). Typically paired with the `badge-limited-edition` component.

**`button-text-link`** — A text-only button styled as a link, using `primary` blue and Aktiv Grotesk 400 at 14px. Used for "Sign In," "Create Account," and "View All" links within content sections.

### Navigation
**`top-nav`** — A fixed 64px bar on a white canvas with a single hairline bottom border. Navigation links are uppercase Aktiv Grotesk 500 at 15px with 0.3px letter-spacing. Active page uses a 2px solid blue bottom border; inactive links render in `muted` (#666666). The nav houses the brand logo, main category links (Cult, Classic, Horror, New Releases, Labels, Sales), a search icon, and a basket icon.

**`search-bar`** — A white input field with a 1px hairline border and {rounded.sm} corners, 44px tall. On focus, the border thickens to 2px solid blue. Placeholder text uses `muted-soft` (#999999). The search icon sits at the left edge; a clear button appears on input.

### Cards
**`product-card`** — A white card with {rounded.sm} corners containing a film poster image and an info block. The image area uses `{rounded.sm} {rounded.sm} 0 0` to match the card's top corners. The info block (16px padding) displays the film title in `title-sm` and the price in `accent-red` body-md. A hover state lifts the card 4px with a subtle shadow. Badges overlay the top-left of the image.

**`hero-section`** — A full-width dark section (`ink` background) with white display text. Used for featured collections, new restorations, and seasonal sales. The title uses `display-xl` (48px Bigger Display 700) and the subtitle uses `display-sm` (22px Aktiv Grotesk Extended 600) in `muted-soft`. A `button-primary` sits below the text.

### Badges
**`badge-limited-edition`** — A small red pill with white uppercase text at 11px 700 weight. Uses `accent-red` background and {rounded.xs} corners. Positioned absolutely over the top-left of product card images. Signals numbered editions, slipcases, or exclusive content.

**`badge-format`** — A neutral badge on `surface-soft` background with `muted` text. Indicates the disc format: "Blu-ray," "4K UHD," "DVD," or "Digital." Typically sits below the price or in the product card info block.

**`badge-label`** — A teal badge using `accent-teal` (#00a2a9) for label-specific collections like "Arrow Video," "Arrow Academy," or "Second Run." Helps users identify the restoration series at a glance.

### Filters & Selectors
**`filter-tag`** — A pill-shaped tag on `surface-soft` background with `body` text. Used in the collection sidebar and top filter strip for genres, directors, years, and labels. Active state fills with `primary` blue and white text. Multiple tags can be selected simultaneously.

**`quantity-selector`** — A compact input group with minus/plus buttons flanking a centered number. Uses a 1px hairline border, {rounded.xs} corners, and 44px height. The buttons change the quantity by 1; the input accepts direct typing.

### Footer
**`footer`** — A dark section (`ink` background) with `muted-soft` text at body-sm size. Contains columns for Customer Service, About Arrow, Social Links, and Newsletter Signup. Links use `muted-soft` color and shift to white on hover. The newsletter input matches the `search-bar` style but sits on the dark background with a white border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1–2 cards), hamburger menu replaces top nav, hero text shrinks to display-md, filter tags collapse into a dropdown, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, top nav shows 4–5 links with overflow menu, hero uses display-lg, filter strip remains horizontal but scrollable |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links visible, hero at display-xl, sidebar filters visible, footer in 4 columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero content centered with wider margins, additional whitespace around product cards |

### Touch Targets
- All interactive elements (buttons, links, filter tags, quantity buttons) maintain a minimum 44x44px tap target
- Product card images are fully tappable, linking to the product detail page
- Badges are informational only and not tappable
- Search bar expands to full width on mobile with a larger touch area

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px; the menu slides in from the left with a scrim overlay
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1–2 (mobile)
- Filter sidebar collapses to a horizontal scrollable strip on tablet and a dropdown on mobile
- Footer columns collapse from 4 to 2 on tablet and 1 on mobile
- Hero section reduces font sizes and centers content on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette includes several colors (#00a2a9, #ad3381, #0d9c4a, #d5cd27) that may represent sub-brand badges, genre tags, or third-party payment/social icons rather than core brand colors. Their exact usage context could not be confirmed from extraction alone.
- Hover and active states for secondary buttons, text links, and filter tags are inferred from common patterns; exact values may differ.
- Error states for form inputs (validation, empty fields) were not extractable.
- Dark mode preferences or alternative themes were not detected.
- The extracted font list includes "Open Sans Condensed" and "Bigger Display" — the latter appears to be a display face for hero titles, but its exact weight and spacing variants are estimated.
- Font sizes for display and title levels are estimated based on common editorial e-commerce patterns; exact values from the live site's computed styles were not extractable.
- The `rounded` scale is estimated from typical e-commerce patterns; exact corner radii on cards, buttons, and inputs could not be programmatically extracted.
- Spacing values are based on common 8px/16px grid systems; the live site may use a different base unit.
- Component padding and height values are estimated from typical e-commerce patterns; exact measurements require design file access.
- The brand may use additional component variants (e.g., wishlist button, share button, video player) that were not captured in the extraction.
