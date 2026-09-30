---
version: alpha
name: "Viori Beauty"
source_url: "https://viori.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A bath-and-shower brand that leads with a hot-pink voltage — #e5067e — a color so saturated it reads as both floral and synthetic, like a peony bred in a lab. This pink (and its deeper sibling #d90073) drives every primary button, badge, and accent, while the brand's canvas stays a warm off-white #f6f4f1 that softens the clinical edge of standard ecommerce whites. The typography stack is deliberately eclectic: Feeling Passionate, a decorative script with dramatic swashes, appears in hero headlines and product titles, while JetBrains Mono — a developer-favorite monospace — shows up in price tags and ingredient callouts, creating a jarring but memorable contrast between romance and precision. Montserrat handles body copy and navigation, grounding the system in a reliable sans-serif. Buttons use full-pill radii ({rounded.full}) for a glossy, almost cosmetic-tube feel, and product cards float on {rounded.md} corners with thin hairlines (#cfcfcf). The brand's secondary palette is equally assertive: a deep green (#1f7a1f) for "natural" badges and sustainability claims, a gold (#f5c518) for star ratings and sale flags, and a crimson (#c5003e) for urgency markers. The overall effect is maximalist but controlled — every surface carries a purpose, every pink clickable element promises a sensory payoff.

colors:
  primary: "#e5067e"
  primary-active: "#c5003e"
  primary-disabled: "#fce5ee"
  ink: "#0a0a0a"
  body: "#111111"
  muted: "#555555"
  muted-soft: "#888888"
  hairline: "#cfcfcf"
  hairline-soft: "#e5e5e5"
  canvas: "#f6f4f1"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#1f7a1f"
  accent-green-soft: "#478947"
  accent-gold: "#f5c518"
  accent-crimson: "#c5003e"
  accent-deep-pink: "#d90073"
  accent-magenta: "#ec008c"
  accent-burgundy: "#73003d"
  accent-error: "#b00020"
  accent-warm-brown: "#8a5a00"
  accent-charcoal: "#5a5a5a"

typography:
  display-xl:
    fontFamily: "'Feeling Passionate', 'Brush Script MT', cursive, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'Feeling Passionate', 'Brush Script MT', cursive, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'JetBrains Mono', 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.5px
  price-sm:
    fontFamily: "'JetBrains Mono', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.3px
  ingredient:
    fontFamily: "'JetBrains Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
  button-pill-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
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
    border: "2px solid {colors.accent-error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(10,10,10,0.08)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "0 {spacing.base} {spacing.sm}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-natural:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  star-rating:
    color: "{colors.accent-gold}"
    size: 16px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
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
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base}"
  ingredient-callout:
    typography: "{typography.ingredient}"
    textColor: "{colors.muted}"
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered as a full-pill in the signature hot pink (#e5067e). Uses uppercase Montserrat 600 at 14px with generous horizontal padding (32px) to create a balanced, weighty button that feels substantial without being heavy. On hover, the background shifts to the deeper crimson (#c5003e) for a clear active state. The disabled state uses a soft pink (#fce5ee) with muted text, signaling unavailability without visual aggression.

**`button-secondary`** — An outlined variant on the warm canvas background (#f6f4f1), with a 2px pink border and pink text. This button appears in less-prominent actions like "Learn More" or "Add to Wishlist" on product cards. Active state deepens the border and text to crimson. The transparent background allows it to sit comfortably on both white cards and the off-white page canvas.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "View All" in category strips. The pink text maintains brand consistency while the transparent background keeps the UI clean. Hover adds a subtle underline or opacity shift.

**`button-pill-green`** and **`button-pill-gold`** — Small, compact pill buttons used for badges and inline actions. The green variant (#1f7a1f) signals "natural" or "vegan" claims, while the gold (#f5c518) marks sales or limited-time offers. Both use 12px uppercase Montserrat 600 and tight padding (8px 20px) to fit within card overlays and category tags.

### Cards
**`product-card`** — The primary product display unit, a white card with a 1px soft hairline border (#e5e5e5) and 12px rounded corners. The card contains a square aspect-ratio image at the top (with rounded top corners only), followed by the product title in 16px Montserrat 500 and the price in 18px JetBrains Mono 500. On hover, the card gains a subtle box shadow and a slightly darker border (#cfcfcf), creating a gentle lift effect. Badges (new, natural, sale) overlay the top-left corner of the image area.

**`hero-section`** — A full-width banner section with a soft gray background (#f5f5f5) and generous vertical padding (64px). The hero headline uses the decorative Feeling Passionate script at 48px, creating an immediate emotional and romantic tone. A single primary CTA button anchors the bottom of the hero, typically leading to a featured collection or new arrival.

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 72px height on the warm canvas background, with a thin bottom border (#e5e5e5). Navigation links use 13px uppercase Montserrat 600 with 0.8px letter spacing for a refined, editorial feel. The active link state shifts text to hot pink with a 2px pink bottom border. The nav typically contains 4-5 links (Shop, Best Sellers, About, Rewards, etc.) plus a search icon and cart icon.

### Forms
**`text-input`** — A standard input field with 48px height, 12px rounded corners, and a 1px hairline border (#cfcfcf) on the warm canvas background. Focus state switches to a 2px pink border (#e5067e) for clear visual feedback. Error state uses a 2px red border (#b00020). Input text uses 16px Montserrat 400 with placeholder text in muted gray (#888888).

### Badges
**`badge-new`** — A small full-pill badge in hot pink with white uppercase text (11px Montserrat 700, 0.5px letter spacing). Used to flag new arrivals and limited drops. Positioned at the top-left of product card images with a slight offset.

**`badge-natural`** — Same shape and typography as the new badge but in deep green (#1f7a1f). Used for "vegan," "natural," or "sulfate-free" claims on product cards and ingredient lists.

**`badge-sale`** — Gold (#f5c518) badge with dark text (#0a0a0a) for sale items and promotional pricing. The high contrast ensures it stands out against both white cards and the warm canvas background.

### Footer
**`footer`** — A dark footer (#0a0a0a) with muted gray text (#888888) and links in the same muted tone. Link hover shifts to hot pink (#e5067e), creating a subtle brand callback in an otherwise neutral space. The footer typically contains 3-4 columns of links (Customer Care, About, Connect, etc.) plus social icons and a newsletter signup.

### Typography Specials
**`ingredient-callout`** — A small monospace block in JetBrains Mono at 12px, set on a soft gray background (#f5f5f5) with 8px rounded corners. Used on product detail pages to list key ingredients in a way that feels technical and trustworthy — a deliberate contrast to the script headlines above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hero headline drops to 32px; product cards stack in 1 column; nav collapses to hamburger; button padding reduces to 24px horizontal; footer stacks to single column |
| Tablet | 744–1128px | Hero headline at 40px; product cards in 2 columns; nav shows 3-4 links; search bar reduces width |
| Desktop | 1128–1440px | Full layout: hero at 48px, product cards in 3-4 columns, full nav visible, search bar at 400px max-width |
| Wide | > 1440px | Content max-width at 1440px centered; hero expands to full width with inner container at 1200px; product cards in 4 columns |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 48px tap targets (padding + height)
- Product card tap targets cover entire card surface
- Badges are minimum 24px height for tap clarity
- Search bar maintains 48px height across all breakpoints

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product grid collapses from 4 columns to 2 at tablet, 1 at mobile
- Footer columns collapse to single column below 744px
- Hero section reduces vertical padding from 64px to 40px on mobile
- Secondary navigation (category strip) collapses to horizontal scroll on mobile
- Multi-row product features collapse to accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list contains 30+ colors, many of which may be Shopify widget defaults (Afterpay green, Klarna pink, etc.) or social icon colors. The primary pink (#e5067e) and its variants (#d90073, #c5003e, #ec008c) are confidently brand-specific, but the green (#1f7a1f) and gold (#f5c518) could be secondary brand colors or checkout defaults — further verification needed.
- Font sizes and line heights are estimated based on typical ecommerce patterns for the detected font families; exact values from the live site's CSS were not extractable.
- Hover, focus, and active states for all components are inferred from common patterns; actual interaction states may differ.
- Error, success, and warning form states are not confirmed from the live site.
- Dark mode is not present on the live site and is not defined.
- Sub-brand or collection-specific color palettes (e.g., limited edition drops) are not captured.
- The Feeling Passionate font may have variable weight or alternate glyphs that affect display sizing.
- Exact spacing values (padding, margin, gap) for component internals are estimated; the live site may use a different scale.
- Animation and transition timings (ease, duration) are not extracted.
- The meta theme-color tag is absent, suggesting no browser chrome theming is implemented.
