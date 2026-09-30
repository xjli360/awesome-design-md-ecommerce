---
version: alpha
name: "Pela"
source_url: "https://www.pelacase.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A muted sage-and-slate palette — #617c55, #405960, #a9c1c7 — wraps Pela's compostable phone cases in the visual language of soil, stone, and recycled fiber. The brand's primary green (#617c55) reads less like a logo color and more like a natural pigment, appearing on CTAs, badges, and the "100% Compostable" stamp that anchors the hero. Secondary teal (#577c85) and a warm clay accent (#bc5548) add just enough tension to keep the palette from drifting into monotone. Typography splits between Poppins (headings, buttons) and Lora (body), a pairing that signals both modern clarity and editorial warmth — Poppins Medium at 16px for nav links, Lora at 15px for product descriptions. Cards and buttons use soft rounding ({rounded.sm} at 8px, {rounded.md} at 12px), never pill shapes, preserving a grounded, un-gimmicky feel. The canvas is a cool off-white (#ecf2f3) rather than pure white, a subtle choice that echoes the brand's environmental ethos — nothing feels bleached or synthetic. Product imagery sits on {surface-card} (#ffffff) with a thin {hairline} (#c5c7c8) border, letting the cases' flax-straw texture and muted colorways (Sage, Terracotta, Ocean) carry the visual story. The footer collapses into a dense, link-heavy block on mobile, while the nav bar compresses to a hamburger with a persistent cart icon — standard Shopify DTC, but executed with restraint.

colors:
  primary: "#617c55"
  primary-active: "#4d6343"
  primary-disabled: "#afc3a7"
  ink: "#272d45"
  body: "#405960"
  muted: "#676986"
  muted-soft: "#929692"
  hairline: "#c5c7c8"
  hairline-soft: "#dbdde4"
  canvas: "#ecf2f3"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#aabfa1"
  accent-teal: "#577c85"
  accent-clay: "#bc5548"
  accent-ocean: "#0e7a82"
  star-rating: "#899df1"
  badge-green: "#617c55"
  badge-sale: "#bc5548"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Poppins Bold', 'Gotham Medium', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', 'Poppins Medium', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Poppins Medium', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Poppins Medium', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Lora', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lora', Georgia, 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins', 'Poppins Medium', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Poppins Medium', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Poppins', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Poppins Medium', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Poppins Bold', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  badge-compostable:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: 64px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with {colors.primary} (#617c55) and set in Poppins Medium 16px. Hover transitions to {colors.primary-active} (#4d6343) with a subtle 0.2s ease-in-out. Disabled state uses {colors.primary-disabled} (#afc3a7) and cursor: not-allowed. Used for "Add to Cart", "Shop Now", and checkout entry points.

**`button-secondary`** — Outlined variant on {colors.canvas} (#ecf2f3) background with {colors.ink} (#272d45) text. Hover adds a 1px solid {colors.primary} border. Used for "Learn More" and secondary product actions.

**`button-tertiary-text`** — Ghost button with no background, {colors.primary} text, and underline on hover. Used for "View Details" links within product cards.

**`button-pill`** — Full-pill variant used sparingly for promotional badges and "Subscribe & Save" CTAs. Same color logic as button-primary but with {rounded.full} and tighter padding.

### Cards
**`product-card`** — White surface ({colors.surface-card}, #ffffff) with {rounded.md} (12px) corners and a 1px {colors.hairline} (#c5c7c8) border. Image area uses {rounded.md} as well. Title in {typography.title-sm}, price in {typography.body-sm} with {colors.muted} (#676986). Hover lifts the card 2px with a soft box-shadow.

**`badge-compostable`** — Small uppercase label in {colors.badge-green} (#617c55) with white text. Used to flag compostable materials on product cards and category pages. {rounded.xs} (4px) keeps it crisp.

**`badge-sale`** — Same shape as compostable badge but in {colors.accent-clay} (#bc5548). Used for clearance or limited-edition drops.

### Navigation
**`nav-bar`** — Fixed top bar at 64px height on {colors.canvas} (#ecf2f3). Logo left-aligned, nav links (Shop, Materials, About, Impact) in {typography.nav-link} (Poppins Medium 16px, {colors.ink}). Cart icon and search icon right-aligned. On mobile (< 744px), nav links collapse into a hamburger menu; cart icon persists.

**`search-bar`** — Pill-shaped input with {rounded.full}, white background, and placeholder text in {colors.muted-soft} (#929692). Expands on focus with a 2px {colors.primary} border.

### Forms
**`text-input`** — Standard input field with {rounded.sm} (8px), 48px height, and 12px 16px padding. Border is {colors.hairline} (#c5c7c8) by default, shifts to {colors.primary} on focus. Error state uses {colors.accent-clay} (#bc5548) border and text.

### Footer
Footer uses a dense column layout on desktop (4 columns: Shop, Learn, Support, Connect) with links in {typography.link} ({colors.muted}). Background is {colors.surface-soft} (#f4f4f6). Social icons (Instagram, TikTok, Facebook) appear in {colors.muted} with hover to {colors.primary}. Bottom bar includes copyright, privacy, and terms in {typography.caption} ({colors.muted-soft}).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero padding reduces to 32px 16px; footer columns stack to single column; search bar moves to full-width below nav |
| Tablet | 744–1128px | Nav links visible (Shop, Materials, About, Impact); product cards in 2-column grid; footer in 2-column layout; hero padding at 48px 24px |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; footer in 4-column layout; hero padding at 64px 24px |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero content centered with larger typography |

### Touch Targets
- All buttons and links: minimum 44px height for tap targets
- Nav icons (cart, search, hamburger): 44x44px tap area
- Product card CTAs: 48px height minimum
- Footer links: 44px line height for tap spacing

### Collapsing Strategy
- Nav links collapse to hamburger at < 744px
- Footer columns collapse from 4 → 2 → 1 as viewport shrinks
- Product grid collapses from 4 → 3 → 2 → 1 columns
- Hero image and text stack vertically on mobile
- Search bar moves from inline to full-width below nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components not fully extracted — only primary button hover is confirmed
- Error states for text-input (border color, helper text styling) inferred from brand palette, not extracted
- Dark mode not present on live site — no dark palette tokens available
- Sub-brand palettes (e.g., Pela 360, Pela Earth) not extracted — only main brand colors captured
- Font weights for Lora (body) not confirmed — 400 used as default, but 400 italic may exist for emphasis
- Star rating color (#899df1) appears in extracted list but may be a Shopify widget default — used as accent but not confirmed as brand choice
- Button hover transitions (duration, easing) not extracted — 0.2s ease-in-out assumed from common DTC patterns
- Product card shadow values not extracted — lift effect inferred from common ecommerce patterns
- Footer social icon colors not confirmed — muted with primary hover assumed
- Checkout flow colors (Shopify Pay, Afterpay badges) present in extracted list but excluded as platform defaults
