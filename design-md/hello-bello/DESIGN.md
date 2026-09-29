---
version: alpha
name: "Hello Bello"
source_url: "https://hellobello.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A playful, affordable baby-care brand that wraps its deep purple #300064 around a pastel rainbow of accents — #ff6dff bubblegum pink, #00fc87 mint, #fffe64 marigold — and trusts a clean white canvas to keep it from feeling like a cartoon. The primary purple carries every CTA, badge, and navigation bar, while the secondary #7a60ff provides a lighter hover state that still reads as unmistakably Hello Bello. Product photography and illustration share space generously, with soft pill-shaped buttons ({rounded.full}) and card corners ({rounded.lg}) that mirror the gentle curves of baby products themselves. The brand uses Alexandria as its display and body face, a rounded geometric sans-serif that feels approachable without sacrificing legibility at small sizes. The extracted palette reveals a system built on high-contrast purple-on-white for primary actions, muted grays (#e5e7eb, #9ca3af) for secondary borders and disabled states, and a warm lavender #f2edff for soft surfaces. The checkout flow introduces #0056a1 (a Shopify-standard blue) and various payment-widget colors, but the brand's own identity is unmistakably purple-first, with pink and green as joyful accent voltages. The overall mood is "trustworthy whimsy" — the purple says premium, the pastels say baby, and the white space says we're not trying to sell you anything you don't need.

colors:
  primary: "#300064"
  primary-active: "#7a60ff"
  primary-disabled: "#6f55f5"
  ink: "#1f1f1f"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d1d5db"
  hairline-soft: "#e5e7eb"
  canvas: "#ffffff"
  surface-soft: "#f2edff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-pink: "#ff6dff"
  accent-mint: "#00fc87"
  accent-marigold: "#fffe64"
  accent-coral: "#eb644f"
  badge-purple: "#6f4480"
  badge-lavender: "#f2d8f2"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.15px
  link:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Alexandria', 'Alexandria_Fallback', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    opacity: 0.5
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-accent-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-mint:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
  product-card-image:
    rounded: "{rounded.lg}"
  badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-new:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-bestseller:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px

## Components

### Buttons

**`button-primary`** — The workhorse CTA across the entire site, rendered in deep purple #300064 with white text and full pill rounding ({rounded.full}). On hover, the background shifts to the lighter secondary purple #7a60ff, providing clear feedback without breaking brand identity. The disabled state uses #6f55f5 at 50% opacity, ensuring users can still read the label while understanding the action is unavailable. Padding of 14px 28px and a 48px height give it a substantial, tappable feel on both desktop and mobile.

**`button-secondary`** — An outlined variant with a white background and purple text, used for secondary actions like "Learn More" or "Add to Cart" alongside a primary CTA. The border is 2px solid {colors.primary}, and on hover the background fills with {colors.surface-soft} (#f2edff) while the text remains purple. Same pill rounding and height as the primary button for visual consistency.

**`button-accent-pink`** and **`button-accent-mint`** — Playful accent buttons reserved for promotional banners, limited-time offers, and seasonal campaigns. The pink variant uses #ff6dff with dark text (#1f1f1f), while the mint uses #00fc87. These are the brand's "fun" buttons — same pill shape and size as primary, but the high-saturation pastels signal urgency or delight rather than standard action.

### Cards

**`product-card`** — A white card with soft rounded corners ({rounded.lg}) and a subtle shadow (0 2px 8px rgba(0,0,0,0.08)). The product image sits at the top with matching corner rounding, followed by the product title in {typography.title-md}, a price in {typography.body-md}, and a "Subscribe & Save" badge or standard CTA. On hover, the shadow deepens slightly (0 4px 16px rgba(0,0,0,0.12)) and the card lifts 2px.

**`badge-sale`**, **`badge-new`**, **`badge-bestseller`** — Small pill-shaped badges that overlay product cards or hero imagery. Each uses a distinct accent color from the brand palette: marigold (#fffe64) for sale, mint (#00fc87) for new arrivals, and pink (#ff6dff) for bestsellers. All badges use {typography.badge} (11px uppercase bold) with 4px 10px padding and full rounding.

### Navigation

**`nav-bar`** — A fixed top navigation bar at 72px height, white background with a subtle bottom border ({colors.hairline-soft}). The logo sits on the left (typically the Hello Bello wordmark in purple), with category links (Diapers, Wipes, Bath, etc.) in the center using {typography.nav-link}. The right side contains a search icon, account link, and cart icon. On scroll, the bar gains a slight shadow (0 2px 4px rgba(0,0,0,0.06)).

### Forms

**`text-input`** — Standard form input with a white background, 1px solid {colors.hairline} border, and {rounded.sm} corners. On focus, the border shifts to {colors.primary} with a 2px stroke and a subtle purple box-shadow (0 0 0 3px rgba(48,0,100,0.15)). The placeholder text uses {colors.muted-soft}. Error states use a red border (#eb644f) with an error message in {typography.caption}.

### Footer

**`footer-link`** — Text links in the footer area, rendered in {colors.muted} (#6b7280) with {typography.link}. On hover, the color shifts to {colors.primary} (#300064). The footer itself has a light lavender background ({colors.surface-soft}) with sections for customer service, shop by category, and social links. A copyright line sits at the bottom in {typography.caption} with {colors.muted-soft}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to {typography.display-lg}; buttons go full-width; search bar moves to a slide-out panel |
| Tablet | 744–1128px | Two-column product grid; nav shows category links as text only (no icons); hero uses {typography.display-xl} but with tighter padding; badges remain readable |
| Desktop | 1128–1440px | Full three-column product grid; nav shows all links with optional dropdowns; hero uses full {typography.display-xl} with generous padding; search bar visible in nav |
| Wide | > 1440px | Max-width container at 1440px; content centered; hero may use wider imagery; product grid can expand to four columns for certain categories |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (48px preferred) to meet WCAG touch target guidelines
- Nav links have 48px tap areas even when text is smaller
- Product card CTAs are at least 44px tall
- Badges are 24px+ tall for readability

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu with a slide-out drawer
- Product category filters collapse to a "Filter" button that opens a modal overlay
- Footer columns stack vertically on mobile, with accordion-style expandable sections
- Hero imagery may crop or stack text below image on small screens
- Search bar transitions from inline to a full-screen overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for many components (badges, footer links, product card CTAs) could not be reliably extracted from the static HTML/CSS analysis
- Error state styling for forms (red borders, error message typography) is inferred from common patterns rather than extracted
- The exact font weight for Alexandria at display sizes is uncertain — the extracted CSS showed multiple weights but the specific mapping to each token is inferred
- Dark mode is not present on the live site and no dark-mode palette could be extracted
- The checkout flow uses Shopify's default styling (#0056a1 blue) which may not match the brand's own design system
- Sub-brand or seasonal palettes (e.g., holiday collections, limited-edition diapers) could not be extracted
- Animation and transition timings (hover lift, shadow changes, menu slide) are estimated based on common e-commerce patterns
- The exact spacing scale for section padding and card margins is inferred from layout analysis rather than extracted CSS variables
- Social media icon colors and payment method badge colors were filtered out but may have brand-specific styling not captured
