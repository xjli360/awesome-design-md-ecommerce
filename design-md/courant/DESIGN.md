---
version: alpha
name: "Courant"
source_url: "https://www.staycourant.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep brown #50280f anchors a brand that sells wireless charging as an object of desire — not a utilitarian puck but a leather-and-metal heirloom meant to live on a nightstand or desk. The palette runs from that dark espresso through warm caramel #b15019 and a creamy off-white #f5efe7 that reads as unbleached linen rather than sterile paper. A restrained accent of crimson #d0011b appears only where urgency is needed — sale markers, error states — while the cooler slate #676986 and steel #979797 handle secondary text and borders. The typography relies on Priori Sans, a serif with enough personality to carry headlines without shouting, paired with a clean sans-serif for body copy. Buttons and cards use soft {rounded.sm} corners that suggest leather goods rather than glass screens; the overall effect is a store that feels more like a boutique hotel lobby than a tech accessory shop. The brand trusts material texture — leather grain, brushed metal, woven fabric — over gradients or heavy shadows, and the white space is generous enough that each product photograph breathes like a still life. There is no bright blue or neon accent; the brand's voltage comes from the contrast between warm brown and cream, with the occasional jolt of red.

colors:
  primary: "#50280f"
  primary-active: "#3d1f0b"
  primary-disabled: "#a08070"
  ink: "#1c1a1a"
  body: "#444444"
  muted: "#707070"
  muted-soft: "#979797"
  hairline: "#e5e5e5"
  hairline-soft: "#f4f4f6"
  canvas: "#f5efe7"
  surface-soft: "#f9f8f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#d0011b"
  accent-warm: "#b15019"
  accent-slate: "#676986"
  accent-navy: "#272d45"

typography:
  display-xl:
    fontFamily: "'priori-sans', 'Georgia', 'Times New Roman', serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'priori-sans', 'Georgia', 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'priori-sans', 'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'priori-sans', 'Georgia', 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'priori-sans', 'Georgia', 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'priori-sans', 'Georgia', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'priori-sans', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'priori-sans', 'Georgia', 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'priori-sans', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 600
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
    rounded: "{rounded.sm}"
    padding: 14px 32px
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: 1px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  section-heading:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action uses the signature espresso brown {colors.primary} on a white background, with uppercase Priori Sans at 14px and soft {rounded.sm} corners. On hover, the background deepens to {colors.primary-active} with no border or shadow change — the color shift is subtle, like leather darkening with age. The disabled state drops to a muted brown {colors.primary-disabled} that reads as faded suede.

**`button-secondary`** — An outlined variant with transparent fill and a 1px solid border in {colors.primary}. The text remains uppercase Priori Sans at 14px. On hover, the button fills solid with {colors.primary} and text flips to white — a deliberate inversion that signals commitment without urgency. Useful for "Learn More" or "View Details" actions alongside primary CTAs.

**`button-text`** — A borderless, backgroundless text button using {colors.primary} and uppercase Priori Sans. Reserved for secondary actions within cards or inline contexts where a full button would feel heavy. Hover adds no background, only a subtle opacity shift.

### Cards
**`product-card`** — A white card with {rounded.sm} corners containing a product image, title, and price. The image uses the same corner radius as the card, creating a seamless visual flow. The price is set in {typography.body-md} and colored {colors.primary} to draw the eye. Cards sit on the {colors.canvas} background with generous {spacing.lg} gutters. No shadow — the brand trusts the contrast between white card and warm cream canvas for separation.

**`product-card-image`** — The product photo fills the top of the card with {rounded.sm} corners. Images are high-contrast, well-lit product shots on neutral backgrounds — no lifestyle clutter. The aspect ratio is typically 1:1 for chargers and 3:4 for bundles.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on {colors.canvas} background. Navigation links use uppercase Priori Sans at 14px in {colors.ink}, with the active or hover state switching to {colors.primary}. The logo sits left-aligned, typically in {colors.primary} or {colors.ink}. The cart icon and account link sit right-aligned. On mobile, the nav collapses into a hamburger menu with a slide-out drawer.

**`nav-link-active`** — The active page or section link uses {colors.primary} text color with no underline or background change — the color shift alone signals state.

### Forms
**`text-input`** — A standard input field on {colors.canvas} background with a 1px {colors.hairline} border and {rounded.sm} corners. The placeholder text uses {colors.muted-soft}. On focus, the border switches to {colors.primary} — a warm brown glow rather than a blue ring. The height is 48px with 12px vertical padding for comfortable touch targets.

### Badges
**`badge-sale`** — A small pill-shaped badge in {colors.accent-red} with white uppercase text at 12px. Used sparingly — only for markdowns or limited-time offers. The red is the brand's only high-energy color, so its appearance carries weight.

**`badge-new`** — A warm caramel {colors.accent-warm} badge for new arrivals or restocks. Same shape and typography as the sale badge but in a tone that complements the primary palette rather than competing with it.

### Hero
**`hero-section`** — A full-width section on {colors.canvas} with a large headline in {typography.display-xl} and a single primary CTA. The hero image — typically a product shot on a neutral or textured background — sits beside or behind the text. No carousel, no multiple CTAs — the hero makes one clear offer.

**`hero-cta`** — The hero's primary button, identical to `button-primary` but with additional horizontal padding (32px) for visual weight at scale.

### Footer
**`footer`** — A deep brown {colors.primary} footer with white text. Links use {typography.link} in white with no underline. The footer contains brand navigation, customer service links, and social icons. The background color mirrors the brand's primary, creating a bookend effect with the top nav.

**`footer-link`** — White text links in the footer, using the sans-serif body font for readability at small sizes. No hover underline — the color contrast is sufficient.

### Dividers
**`divider`** — A 1px horizontal line in {colors.hairline} used to separate sections or card elements. In the footer, the divider uses a lighter tone to maintain contrast against the dark background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, hero stacks vertically, buttons full-width, font sizes reduce by 2-4px |
| Tablet | 744–1128px | Two-column product grid, top nav collapses to icon-only, hero text and image side-by-side |
| Desktop | 1128–1440px | Three-column product grid, full top nav with links, hero at full width with generous margins |
| Wide | > 1440px | Max-width container at 1440px, centered content, hero scales with white space |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Product card tap targets include the entire card surface
- Nav links on mobile have 48px tap areas
- Cart and account icons minimum 44x44px

### Collapsing Strategy
- Top navigation links collapse into hamburger menu below 744px
- Product grid collapses from 3 columns to 2 at 1128px, to 1 at 744px
- Hero section stacks vertically on mobile (image above text)
- Footer links collapse into accordion-style sections on mobile
- Search bar collapses to icon-only on mobile, expands on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for buttons and links are inferred from common patterns; exact transitions (duration, easing) not extracted
- Error states for form inputs (red border, error message styling) not observed
- Success/confirmation states (add-to-cart toast, checkout flow) not captured
- Dark mode or high-contrast mode not present on the live site
- Sub-brand or collection-specific color variations (e.g., limited editions) not documented
- Exact font weights for Priori Sans variants (regular, semibold, bold) not confirmed — weights above are best estimates
- Spacing values for specific components (e.g., card padding, section margins) are inferred from common e-commerce patterns
- The extracted hex list includes several grays and blues (#2c3e50, #0e7a82) that may be Shopify checkout defaults or stock image tones — the brand's true palette centers on #50280f, #f5efe7, and #b15019
- Animation durations and easing curves for hover states, page transitions, and loading states not extracted
- Icon set and social media icon colors not documented
