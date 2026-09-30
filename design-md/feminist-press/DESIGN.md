---
version: alpha
name: "The Feminist Press"
source_url: "https://www.feministpress.org"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A small press publisher whose visual identity is built on a single, unmistakable blue — #0097ff — that appears in the browser chrome as the theme-color, in every primary button, and as the sole saturated accent across an otherwise restrained palette of near-blacks and warm grays. The site reads as a literary institution that trusts its content over decoration: body text sits in Montserrat at modest weights against a #fafafa canvas, with #444444 ink providing comfortable reading contrast. What distinguishes the brand from generic publishing templates is the presence of #fdd7f6 — a blush pink that surfaces in hover states, category badges, and editorial highlights — and the deep crimson #80001e that appears in footer links and sale markers, suggesting a quiet feminist flag planted in the color system. The typography is single-family Montserrat throughout, with display sizes at 28px and 24px in weight 600, body at 16px weight 400, and a tight 1.4 line-height that keeps long reading passages dense but not cramped. Buttons use {rounded.sm} corners rather than pills, and the search bar follows suit — the brand avoids the overly friendly rounded-full aesthetic of consumer platforms in favor of a more scholarly, direct feel. The nav bar is fixed, 72px tall, with the press name in 18px weight 600 on the left and a simple link set on the right. Product cards for books show cover art at a 2:3 aspect ratio with the title and author set in {typography.title-md} and {typography.body-sm} respectively, with a subtle {colors.hairline} border. The overall impression is of a publisher that knows its audience — readers who respond to clarity, signal, and the occasional flash of pink or crimson rather than visual noise.

colors:
  primary: "#0097ff"
  primary-active: "#0088e6"
  primary-disabled: "#b3d9ff"
  ink: "#1c1d1d"
  body: "#444444"
  muted: "#6c6c6c"
  muted-soft: "#929292"
  hairline: "#cdcdcd"
  hairline-soft: "#dedede"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#f2f2f2"
  on-primary: "#ffffff"
  accent-pink: "#fdd7f6"
  accent-crimson: "#80001e"
  accent-crimson-dark: "#6c0a24"
  star-rating: "#1c1d1d"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.2px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
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
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-pink:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  top-nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    aspectRatio: 2/3
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-author:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
    fontWeight: 600
  badge-new:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.accent-crimson}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-crimson-dark}"
    typography: "{typography.link}"
  newsletter-signup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 32px 24px
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon-hover:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Shop Now", "Subscribe", and "Donate" actions. Rendered in the brand blue #0097ff with white text and a 4px corner radius. On hover, shifts to #0088e6. Disabled state uses a pale blue #b3d9ff background with white text. Height is 44px with 12px 24px padding.

**`button-secondary`** — A white button with dark text, used for secondary actions like "Learn More" or "View All". Uses a 1px hairline border (#cdcdcd) by default. On hover, fills with #f5f5f5 background. Same 44px height as primary for alignment in forms.

**`button-tertiary-text`** — A text-only button in the brand blue, used for inline actions like "Read More" or "See Details". No background or border. On hover, shifts to the darker blue #0088e6.

**`button-pink`** — A special accent button using the blush pink #fdd7f6 with dark text. Used sparingly for promotional badges, event RSVPs, or limited-time offers. Smaller at 8px 16px padding with button-sm typography.

### Cards
**`product-card`** — The standard book listing card. White background with a subtle 1px hairline border (#cdcdcd) and 4px corner radius. The book cover image fills the top at a 2:3 aspect ratio with matching 4px top corners. Below, the title uses title-sm (16px, weight 600) and the author uses body-sm (14px, weight 400) in #444444. Price sits at the bottom in body-sm with weight 600. Cards stack in a responsive grid with 24px gap.

**`hero-banner`** — A full-width section used on the homepage and landing pages. Background is #f5f5f5 with 64px vertical padding. The headline uses display-xl (28px, weight 600) and is accompanied by a single primary CTA button. No overlay or gradient — the brand trusts typographic hierarchy over visual effects.

### Navigation
**`top-nav`** — Fixed at 72px tall, white background, with the press name in 18px weight 600 on the left and navigation links on the right. Links use nav-link typography (14px, weight 500, uppercase, 0.5px letter-spacing). On hover, link text shifts to #0097ff. On mobile, the nav collapses into a hamburger menu with a slide-out drawer.

**`top-nav-link`** — Individual navigation items with 8px 16px padding. Uppercase, 14px, weight 500, 0.5px letter-spacing. Hover state transitions to the brand blue.

### Forms
**`text-input`** — Standard input field with white background, 4px corner radius, 12px 16px padding, and 44px height. On focus, a 2px solid border in #0097ff appears. Placeholder text uses muted #6c6c6c.

**`search-bar`** — A compact search input with #f5f5f5 background, 4px corner radius, and 10px 16px padding. Height is 44px. On focus, shifts to white background with the blue focus ring. No search icon by default — uses placeholder text like "Search books, authors, topics..."

**`newsletter-signup`** — A dedicated signup section with #f5f5f5 background and 32px 24px padding. Contains a headline, a text-input for email, and a primary button. The input and button sit side by side on desktop, stacked on mobile.

### Footer
**`footer`** — Full-width dark footer with #1c1d1d background and white text. Contains three columns on desktop: About, Shop, and Connect. Links use the crimson #80001e color, which shifts to #6c0a24 on hover. Social icons are white circles (32px) that fill with crimson on hover. Newsletter signup sits above the footer on some pages.

### Badges
**`badge-new`** — A small pink badge using #fdd7f6 background with dark text. Used for "New Release" or "Just Published" labels on book cards. 2px 8px padding with 2px corner radius.

**`badge-sale`** — A crimson badge using #80001e background with white text. Used for sale items, discounts, or special offers. Same sizing as badge-new.

**`badge-category`** — A pill-shaped badge with #f5f5f5 background and #444444 text. Used for genre or category tags (e.g., "Fiction", "Memoir", "Poetry"). 4px 12px padding with full rounding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack in 1 column; hero padding reduces to 40px 16px; footer stacks vertically; newsletter input and button stack |
| Tablet | 744–1128px | Two-column product grid; top-nav links remain visible but condensed; hero padding at 48px 24px; footer shows 2 columns |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero at full 64px 24px padding; three-column footer |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid can show 4 columns; hero max-width 1200px |

### Touch Targets
- All buttons and links: minimum 44px height (WCAG 2.1 compliant)
- Social icons: 32px circles with 44px touch area via padding
- Mobile nav hamburger: 44x44px tap target
- Product card images: full card width, tap navigates to product page

### Collapsing Strategy
- Top nav: on mobile (< 744px), links collapse into a slide-out drawer from the left; hamburger icon appears on the right
- Product grid: collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer: collapses from 3 columns (desktop) to 2 (tablet) to stacked (mobile)
- Newsletter: input and button side-by-side on desktop/tablet, stacked on mobile
- Hero: reduces padding and font size on mobile (display-xl drops to 24px)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list includes many grays and blues that may include Shopify checkout widget colors (e.g., #33acff, #0088e6) and social icon defaults. The brand's true primary is #0097ff, but the presence of #fdd7f6 (blush pink) and #80001e (crimson) as accent colors is confirmed by their use in hover states and badges on the live site.
- Font stack is inferred as Montserrat with system fallbacks; exact fallback order and any variable font settings are not confirmed.
- Hover and active states for all components are inferred from common patterns; exact transition durations and easing curves are unknown.
- Error states for form inputs (validation, error messages) are not extracted.
- Dark mode is not present on the live site; no dark palette exists.
- Sub-brand or series-specific color palettes (e.g., for specific book collections) are not captured.
- The exact aspect ratio for hero images and the presence of any overlay gradients are not confirmed.
- Loading states, skeleton screens, and empty states are not documented.
- The brand may use additional fonts for editorial content or quotes that were not extracted.
