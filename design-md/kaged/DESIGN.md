---
version: alpha
name: "Kaged"
source_url: "https://kaged.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A performance-driven supplement brand that uses a deep teal (#088f87) as its primary voltage — a color that reads as metabolic, clean, and clinical without feeling cold. The brand's canvas is near-black (#121212) rather than white, an unusual choice for a supplement company that signals intensity and focus over the usual bright-and-airy wellness aesthetic. The lightest tone in the palette is a warm gray (#dedede) used for body copy and secondary text, creating a high-contrast, low-glare reading experience against the dark canvas. Typography runs DINPro and Inter — DINPro for display headlines where its geometric, industrial character evokes gym equipment and engineering precision, and Inter for body copy where readability at small sizes matters. Buttons use the teal at full saturation with white text and soft 8px corners (`{rounded.sm}`), while product cards sit on a slightly lighter surface (`{colors.surface-card}`) with 12px rounding (`{rounded.md}`) that softens the otherwise severe dark interface. The brand's "Never Stop Evolving" tagline appears in all-caps DINPro on the homepage hero, set against a full-bleed dark background with the teal used sparingly for CTAs and accent lines. The overall mood is that of a premium performance lab — dark, focused, and unapologetically intense, with the teal acting as a single bright signal that guides the user through an otherwise monochrome interface.

colors:
  primary: "#088f87"
  primary-active: "#06706a"
  primary-disabled: "#064d49"
  ink: "#121212"
  body: "#dedede"
  muted: "#9e9e9e"
  muted-soft: "#757575"
  hairline: "#2a2a2a"
  hairline-soft: "#1e1e1e"
  canvas: "#121212"
  surface-soft: "#1a1a1a"
  surface-card: "#1e1e1e"
  on-primary: "#ffffff"
  on-dark: "#dedede"
  accent-teal-light: "#0ab5ab"
  badge-new: "#088f87"
  badge-sale: "#e53935"
  star-rating: "#ffb300"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'DINPro', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.2px
  display-lg:
    fontFamily: "'DINPro', Inter, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.72px
  display-md:
    fontFamily: "'DINPro', Inter, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.56px
  display-sm:
    fontFamily: "'DINPro', Inter, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.22px
  title-md:
    fontFamily: "'DINPro', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DINPro', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'DINPro', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'DINPro', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'DINPro', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DINPro', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    opacity: 0.5
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-pill-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    minHeight: "600px"
    padding: "{spacing.section} {spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.lg}"
  hero-subheadline:
    typography: "{typography.display-sm}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 40px"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.md}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
    hoverTextColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.md}"
  accordion:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: "40px"
    padding: "0 12px"
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: "52px"
    width: "100%"
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
  add-to-cart-button-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    opacity: 0.5
  newsletter-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: "48px"
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: "48px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in full-saturation teal (#088f87) with white uppercase DINPro text at 16px. On hover, the background shifts to a darker teal (#06706a) for a subtle depth cue. The disabled state drops opacity to 0.5 and uses the disabled teal (#064d49) to maintain brand color while signaling inactivity. All primary buttons use 8px corner rounding (`{rounded.sm}`) and 48px height for consistent tap targets.

**`button-secondary`** — An outlined variant with a transparent background and a 2px teal border, used for secondary actions like "Learn More" or "View Details" alongside primary buttons. On hover, the button fills with teal and switches text to white, creating a satisfying inversion effect. The 48px height matches the primary button for alignment in grouped button layouts.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Skip." The text color matches the body gray (#dedede) and shifts to teal on hover. This button maintains the uppercase DINPro typography of the button system but at a reduced visual weight.

**`button-pill-teal`** — A fully rounded pill variant used for badges, tags, and compact CTAs in tight spaces like product cards or category strips. The smaller 14px button typography and 10px vertical padding allow it to sit comfortably alongside other card content.

### Navigation
**`top-nav`** — A fixed 72px dark bar using the canvas color (#121212) with a subtle hairline bottom border (#2a2a2a). Navigation links use uppercase DINPro at 14px with 0.5px letter spacing, creating a clean, industrial feel. The active link state adds a 2px teal bottom border for clear wayfinding.

**`nav-link-active`** — Active navigation links use teal text (#088f87) with a 2px teal bottom border, creating a clear visual anchor for the current page. The uppercase DINPro typography remains consistent with the inactive state.

**`nav-link-inactive`** — Inactive navigation links use the muted gray (#9e9e9e) to reduce visual noise while remaining readable against the dark canvas. On hover, the text shifts to body gray (#dedede) for a subtle brightening effect.

### Cards
**`product-card`** — A dark surface card (#1e1e1e) with 12px corner rounding (`{rounded.md}`) and 16px padding. The card uses a subtle elevation from the canvas (#121212) to create depth without relying on shadows. On hover, a 1px teal border appears, signaling interactivity without overwhelming the product image.

**`product-card-image`** — Square aspect ratio images with 12px corner rounding, maintaining the card's soft geometry. Images are full-bleed within the card's padding, creating a clean edge-to-edge visual.

**`product-card-badge`** — A compact teal badge (#088f87) with white uppercase text at 11px, used for "New" or "Best Seller" labels. The 4px corner rounding (`{rounded.xs}`) and tight 4px/8px padding keep the badge from competing with the product image.

**`product-card-badge-sale`** — A red badge (#e53935) for sale or discount indicators, using the same typography and sizing as the standard badge. The red provides a clear visual contrast against the teal brand color and dark card background.

### Forms
**`search-bar`** — A dark input field (#1a1a1a) with a 1px hairline border (#2a2a2a) and 8px corner rounding. The input uses Inter body text at 16px for readability. On focus, the border thickens to 2px and switches to teal (#088f87), providing a clear focus indicator against the dark background.

**`newsletter-input`** — Matches the search bar styling for visual consistency across form elements. The input sits within the footer, collecting email addresses for the brand's newsletter. The dark surface (#1a1a1a) and hairline border maintain the brand's dark aesthetic even in conversion-focused areas.

**`quantity-selector`** — A compact 40px input for product page quantity selection, using the same dark surface and hairline border as other form elements. The 8px corner rounding and centered text create a clean, minimal control that doesn't distract from the product.

### Hero
**`hero-section`** — A full-width dark section (#121212) with a minimum height of 600px, using generous vertical padding (64px top/bottom) and horizontal padding (32px sides). The hero typically features a full-bleed background image or video with a dark overlay, with the headline and CTA centered or left-aligned.

**`hero-headline`** — The brand's largest typography at 48px DINPro bold with -1.2px letter spacing, creating a commanding presence against the dark background. The headline uses the body gray (#dedede) for maximum contrast without the harshness of pure white.

**`hero-subheadline`** — A 22px DINPro semi-bold line in muted gray (#9e9e9e), providing secondary context without competing with the headline. The reduced weight and color keep the subheadline visually subordinate.

**`hero-cta`** — A larger primary button variant at 52px height with 40px horizontal padding, used as the hero's primary action. The teal background and white uppercase text create a clear visual anchor against the dark hero background.

### Footer
**`footer`** — A dark footer matching the canvas color (#121212) with a hairline top border (#2a2a2a) for separation. The footer uses 64px vertical padding and 32px horizontal padding, with muted gray (#9e9e9e) text for secondary information like legal links and copyright.

**`footer-link`** — Footer links use Inter at 14px in muted gray, shifting to teal on hover. The reduced visual weight keeps the footer from competing with the main content while maintaining accessibility.

**`footer-heading`** — Footer section headings use 16px DINPro semi-bold in body gray (#dedede), providing clear hierarchy for link groups like "Shop," "Support," and "Company."

### Accordion
**`accordion`** — A collapsible content panel using the dark surface (#1a1a1a) with a 1px hairline border and 8px corner rounding. The accordion is used on product pages for ingredient details, usage instructions, and FAQs, keeping the page clean while providing expandable depth.

**`accordion-header`** — The clickable header uses 16px DINPro semi-bold in body gray, with a chevron icon that rotates on expansion. The 16px vertical padding provides a comfortable tap target.

**`accordion-content`** — Expanded content uses Inter at 14px in muted gray (#9e9e9e), creating a clear visual hierarchy between the header and the body text. The 8px top padding provides breathing room from the header.

### Ratings
**`rating-stars`** — A 5-star rating system using amber (#ffb300) for filled stars and muted gray (#757575) for empty stars. The 16px star size keeps the rating compact within product cards while remaining clearly visible against the dark card background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero headline reduces to 32px; hero section min-height reduces to 400px; footer links stack; accordion becomes full-width |
| Tablet | 744–1128px | 2-column product grid; top-nav shows limited links with "More" dropdown; hero maintains 48px headline but reduces padding; footer uses 2-column link layout |
| Desktop | 1128–1440px | 3-column product grid; full top-nav with all links visible; hero at full 600px min-height; footer uses 4-column link layout |
| Wide | > 1440px | 4-column product grid; max-width container at 1440px with centered content; hero scales proportionally; increased horizontal padding for breathing room |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets include the entire card surface, not just the title or price
- Accordion headers provide 48px minimum tap height
- Navigation links in mobile menu provide 48px tap targets with 16px padding
- Quantity selector buttons (plus/minus) are 40px × 40px minimum

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer containing all links
- Product filters collapse to a "Filter" button that opens a modal on mobile
- Footer link groups collapse to accordion-style sections on mobile, with the first group expanded by default
- Product descriptions and ingredient lists use accordion components that are collapsed by default on all breakpoints
- Hero background images switch to a mobile-optimized crop below 744px to maintain visual impact

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is limited to three hex values (#dedede, #088f87, #121212), which may not represent the full brand palette. Additional accent colors (like the amber rating stars and red sale badge) were inferred from common e-commerce patterns rather than extracted from the live site.
- Hover and focus states for form elements (inputs, textareas, selects) could not be reliably extracted — the focus ring color and style are assumed to match the primary teal.
- Error states for form validation (red borders, error messages) were not observed and are not included in the design system.
- The font stack uses DINPro and Inter based on CSS declarations found, but exact font weights and sizes for all typography tokens were inferred from common patterns rather than extracted from specific elements.
- Dark mode is not applicable as the brand already uses a dark canvas by default.
- Sub-brand or collection-specific color palettes (e.g., for Kaged Elite or Kaged Muscle) could not be extracted.
- The Shopify platform may introduce checkout-specific colors (Shopify Pay buttons, Klarna badges) that are not part of the Kaged brand system.
- Animation and transition durations (hover effects, page transitions, loading states) were not extracted and use standard 200-300ms ease-in-out defaults.
- Iconography style (line weight, corner rounding, stroke width) could not be determined from the extracted data.
