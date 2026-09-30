---
version: alpha
name: "Lovevery"
source_url: "https://lovevery.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep navy #131c66 anchors Lovevery's entire system — not as a background but as the brand's primary voltage, appearing on buttons, headlines, and the top navigation bar. This is a brand built for parents who research developmental milestones the way others research vacation destinations; the palette is deliberately restrained (navy, white, and warm gray #514f4e) with precise accent injections of lime #bbdc00, coral #ff9955, and teal #60cbc2 that map to play-kit age ranges and developmental categories. The typography runs BrownPro at moderate weights — display sits at 24–32px in weight 500/600 rather than heavy 700+, letting the product photography of wooden toys and baby faces carry emotional weight. Cards use soft 12px radii (`{rounded.md}`), buttons use 8px (`{rounded.sm}`), and the search bar uses 32px (`{rounded.xl}`) — a graduated rounding system that reads as intentional without being saccharine. The brand's signature move is the "stage" badge: a small navy pill with white text and a lime or coral dot that signals which developmental stage a toy serves, turning a logistical detail into a visual system. White space is generous — section padding runs 64px (`{spacing.section}`) — and the footer is a dense, organized grid of links in muted gray #9ca3af on a soft canvas #f5f7fc, reflecting a brand that respects its customer's need for information without visual noise.

colors:
  primary: "#131c66"
  primary-active: "#202ea8"
  primary-disabled: "#e5e7eb"
  ink: "#131c66"
  body: "#514f4e"
  muted: "#9ca3af"
  muted-soft: "#9aa5af"
  hairline: "#dcd7d2"
  hairline-soft: "#e5e7eb"
  canvas: "#ffffff"
  surface-soft: "#f5f7fc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-lime: "#bbdc00"
  accent-coral: "#ff9955"
  accent-teal: "#60cbc2"
  accent-purple: "#b85bbf"
  accent-gold: "#fedb00"
  accent-green: "#1cc286"
  accent-cyan: "#03b2cb"
  badge-bg: "#131c66"
  badge-text: "#ffffff"
  footer-bg: "#f5f7fc"
  footer-text: "#9ca3af"
  stage-dot-lime: "#bbdc00"
  stage-dot-coral: "#ff9955"
  stage-dot-teal: "#60cbc2"
  stage-dot-purple: "#b85bbf"
  stage-dot-gold: "#fedb00"
  stage-dot-green: "#1cc286"
  stage-dot-cyan: "#03b2cb"

typography:
  display-xl:
    fontFamily: "'BrownPro', Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'BrownPro', Georgia, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'BrownPro', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'BrownPro', Georgia, serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'BrownPro', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'BrownPro', Georgia, serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'BrownPro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'BrownPro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'BrownPro', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'BrownPro', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'BrownPro', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'BrownPro', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'BrownPro', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'BrownPro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'BrownPro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'BrownPro', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-accent-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
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
    border: "2px solid {colors.accent-coral}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 12px 20px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base} {spacing.base}"
  stage-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    height: 24px
  stage-badge-dot:
    width: 8px
    height: 8px
    rounded: "{rounded.full}"
    marginRight: 6px
  stage-badge-lime:
    backgroundColor: "{colors.stage-dot-lime}"
  stage-badge-coral:
    backgroundColor: "{colors.stage-dot-coral}"
  stage-badge-teal:
    backgroundColor: "{colors.stage-dot-teal}"
  stage-badge-purple:
    backgroundColor: "{colors.stage-dot-purple}"
  stage-badge-gold:
    backgroundColor: "{colors.stage-dot-gold}"
  stage-badge-green:
    backgroundColor: "{colors.stage-dot-green}"
  stage-badge-cyan:
    backgroundColor: "{colors.stage-dot-cyan}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  testimonial-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  testimonial-author:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  rating-stars:
    color: "{colors.accent-gold}"
    fontSize: 16px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  quantity-selector-button-hover:
    backgroundColor: "{colors.surface-soft}"
  cart-badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Uses deep navy #131c66 background with white text in BrownPro 600 weight. On hover, shifts to a slightly lighter navy #202ea8. Disabled state uses gray #e5e7eb with muted text. Padding is 14px vertical, 24px horizontal for a comfortable tap target. Secondary buttons invert the scheme with a white background, navy text, and a 2px navy border. Tertiary buttons are text-only, used for less prominent actions like "Learn More" links within cards. Accent buttons in lime #bbdc00 and coral #ff9955 are reserved for promotional contexts and age-stage callouts.

### Cards
**`product-card`** — The primary content container for toy listings. White background with 12px rounded corners (`{rounded.md}`). The image sits flush to the top corners (rounded top, square bottom), followed by the product title in BrownPro 500 weight and price in body weight. Each card carries a `stage-badge` — a navy pill with white uppercase text and a colored dot indicating developmental stage (lime for 0-12 weeks, coral for 3-4 months, teal for 5-6 months, etc.). Badges are 24px tall with 4px horizontal padding and full rounding.

### Navigation
**`nav-bar`** — Fixed 72px top bar with white background and a subtle bottom border (#e5e7eb). Navigation links use BrownPro 500 weight at 15px. Active links get a 2px navy bottom border. The logo sits left-aligned, with primary navigation items centered or right-aligned depending on viewport. On mobile, navigation collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — Standard input fields use 48px height with 12px vertical padding and 16px horizontal. Border is 1px solid #dcd7d2 with 8px rounding. On focus, the border thickens to 2px navy. Error states switch to 2px coral #ff9955. All inputs use BrownPro 400 weight at 16px for readability.

### Search
**`search-bar`** — The search component uses a soft background #f5f7fc with 32px rounding (`{rounded.xl}`), creating a pill-like appearance distinct from the sharper card corners. On focus, it shifts to white with a 2px navy border. Height is 48px with 12px vertical and 20px horizontal padding. The search icon sits inside the left padding.

### Footer
**`footer`** — A dense, organized grid on a soft blue-gray background #f5f7fc. Links are in muted gray #9ca3af at 14px with hover transitions to navy. Section headers use BrownPro 600 weight in navy. The footer includes columns for Shop, Learn, Support, and Company, plus social icons and a newsletter signup. Padding is 64px vertical.

### Accordion
**`accordion`** — Used for FAQ sections and product details. Each item has a white background with a subtle bottom border. The header uses title-sm typography (BrownPro 500, 16px) in navy, with a chevron icon that rotates on expand. Content area uses body-sm (14px) in warm gray #514f4e with 8px vertical padding.

### Testimonials
**`testimonial-card`** — Customer review cards with white background, 12px rounding, and a 1px soft border. Content uses body-md (16px) with the author name in title-sm (16px, 500 weight). Gold stars #fedb00 sit above the quote. Padding is 24px all around for comfortable reading.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; stage badges become full-width; hero text reduces to 24px; search bar becomes full-width with reduced padding |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero section uses 28px display; search bar maintains pill shape but reduces horizontal padding |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses 32px display; search bar centered with max-width 480px |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero section expands with larger imagery; search bar max-width 560px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons are 40x40px with full rounding
- Quantity selector buttons are 40x40px with 8px rounding
- Cart badge is 20px minimum with adequate padding

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Footer grid collapses from 4 columns to 2 columns on tablet, single column on mobile
- Product detail accordions remain collapsed by default on all viewports
- Hero section reduces padding from 64px to 32px on mobile
- Stage badges stack vertically on mobile to accommodate longer age-range labels

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components were inferred from common patterns rather than extracted from the live site
- Error states for forms (validation messages, error icons) were not observed
- Dark mode or high-contrast mode variants are not documented
- The exact font stack for BrownPro could not be confirmed — fallback to Georgia and Times New Roman is assumed for serif contexts, Arial for sans-serif
- Animation timing and easing curves (transitions, hover effects) were not extracted
- The brand's illustration style and icon set are not captured in this document
- Sub-brand or seasonal color palettes (holiday, limited edition) are not documented
- The extracted hex list includes many colors that may be Shopify checkout widgets or social icons — the primary #131c66 and accent #bbdc00, #ff9955, #60cbc2 are confirmed as brand colors based on frequency and distinctiveness
- Accessibility contrast ratios for all color combinations have not been verified
- Print stylesheet behavior is unknown
