---
version: alpha
name: "LitJoy Crate"
source_url: "https://litjoycrate.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A bookish world built on parchment warmth — #e2d2b3, the brand's foundational canvas tone, reads like aged paper stock rather than sterile white, immediately signaling this is a subscription service for readers who treat books as objects of beauty. Deep navy ink (#233746) carries body copy and headlines, while a forest-green accent (#2f4d47) appears on badges, borders, and secondary CTAs as a quiet counterpoint to the expected book-club burgundy or gold. The extracted palette is unusually rich — over thirty distinct hex values — suggesting a brand that layers decorative swatches, limited-edition box colors, and seasonal accents rather than enforcing a tight system. Typography splits between Poppins (likely for display and buttons — clean, geometric, slightly playful) and Nunito (rounder, warmer, used for body and captions), with BrandonGro appearing in headlines and JustCosmic reserved for whimsical decorative moments. Buttons carry {rounded.sm} corners and a generous 48px height, while product cards use {rounded.md} and a soft drop shadow that lifts the box art off the page. The overall feel is that of a cozy, curated library — not minimalist, not maximalist, but deliberately layered: gold foil (#c69214) on limited-edition stamps, sage (#7c918d) on subscription tier cards, and a warm off-white (#f3ede1) for secondary surfaces. Every element seems designed to make the subscriber feel they've received something hand-assembled, not mass-produced.

colors:
  primary: "#2f4d47"
  primary-active: "#233746"
  primary-disabled: "#9ca3af"
  ink: "#233746"
  body: "#2f4d47"
  muted: "#7c918d"
  muted-soft: "#9ca3af"
  hairline: "#e1c08d"
  hairline-soft: "#e2d2b3"
  canvas: "#e2d2b3"
  surface-soft: "#f3ede1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#c69214"
  accent-sage: "#7c918d"
  accent-deep-navy: "#101136"
  accent-terracotta: "#9e6947"
  accent-rose: "#b76e79"
  accent-maroon: "#743d2a"
  accent-bright-pink: "#ff9deb"
  accent-purple: "#c078f4"
  accent-yellow: "#ffd606"
  accent-orange: "#d58130"
  accent-red: "#d14d5c"
  accent-teal: "#00694f"
  accent-emerald: "#008464"
  accent-slate: "#7d8b98"
  accent-light-gray: "#e8e8e8"
  accent-mid-gray: "#c0c0c0"
  accent-near-white: "#f9f9f9"
  accent-dark-teal: "#09262d"
  accent-blue: "#76bffd"
  accent-olive: "#747a4d"
  accent-charcoal: "#011247"
  accent-steel: "#848ca3"
  accent-facebook: "#3b5998"

typography:
  display-xl:
    fontFamily: "'Poppins', 'BrandonGro', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'BrandonGro', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'BrandonGro', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', 'BrandonGro', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Nunito', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  decorative:
    fontFamily: "'JustCosmic', cursive"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0

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
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.accent-red}"
    textColor: "{colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
    rounded: "{rounded.xs}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 52px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    borderColor: "{colors.hairline}"
  search-bar-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 3px rgba(47,77,71,0.15)"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.hairline-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-gold}"
  subscription-tier-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.06)"
  subscription-tier-card-featured:
    borderColor: "{colors.accent-gold}"
    borderWidth: "2px"
  subscription-tier-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.hairline-soft}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  rating-stars:
    color: "{colors.accent-gold}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Subscribe Now", "Add to Cart", and "Join the Waitlist". Rendered in forest green (`{colors.primary}`) with white text and {rounded.sm} corners. On hover, shifts to the deeper navy (`{colors.primary-active}`). Disabled state uses a muted gray (`{colors.primary-disabled}`) to clearly indicate non-interactivity. Height is fixed at 48px for consistency with form inputs.

**`button-secondary`** — Outlined-style button for secondary actions like "Learn More" or "View Details". Uses the warm parchment canvas (`{colors.canvas}`) as background with ink-colored text. On hover, the background fills with the softer parchment tone (`{colors.hairline-soft}`). Same 48px height and {rounded.sm} corners as the primary button for visual rhythm.

**`button-accent-gold`** — A special variant reserved for limited-edition drops, pre-order launches, and exclusive items. Gold background (`{colors.accent-gold}`) with dark ink text creates a premium, celebratory feel. Used sparingly to maintain its special status.

**`button-ghost`** — Text-only button with no background or border, used for "Cancel", "Skip This Month", or "View All". On hover, a subtle background tint may be applied, but the primary affordance comes from the text color and cursor change.

### Cards
**`product-card`** — The core content container for book boxes, individual titles, and merchandise. A white surface (`{colors.surface-card}`) with {rounded.md} corners and a soft drop shadow. The card image area maintains a 1:1 aspect ratio with matching corner radius. A gold badge (`{product-card-badge}`) overlays the top-left corner for "Signed Edition", "Exclusive", or "Best Seller" labels. Price is displayed in the brand's forest green (`{product-card-price}`) for quick scanning.

**`subscription-tier-card`** — Larger, more detailed card used on the subscription comparison page. Features {rounded.lg} corners and generous padding. The featured tier (e.g., "The Collector's Edition") gets a 2px gold border. A sage-green pill badge (`{subscription-tier-badge}`) labels the tier name. These cards stack vertically on mobile and form a three-column grid on desktop.

### Navigation
**`nav-bar`** — Fixed-height (72px) top navigation bar rendered on the warm parchment canvas. Logo sits left-aligned, with nav links (`{nav-link}`) spaced evenly. The active page link is underlined with a 2px forest-green border (`{nav-link-active}`). On scroll, the nav bar gains a white background and subtle shadow (`{nav-bar-sticky}`) for improved readability over page content.

**`nav-link`** — Individual navigation items with {rounded.xs} hover state. Uses Poppins at 14px with 0.3px letter-spacing for a clean, slightly elevated feel. Active state is indicated by the green underline rather than a background fill.

### Forms
**`text-input`** — Standard text input for search, email signup, and address forms. White background with a warm hairline border (`{colors.hairline}`). On focus, the border switches to forest green and a subtle ring appears (`{text-input-focus}`). Error state uses the red accent (`{text-input-error}`) for both border and text. Height matches buttons at 48px for aligned form rows.

**`search-bar`** — A pill-shaped search field (`{rounded.full}`) used in the header and on search results pages. White background with warm border. On focus, gains a green border and a soft green glow ring. The pill shape differentiates it from standard form inputs and signals its primary role as a discovery tool.

### Footer
**`footer-section`** — Full-width footer with a deep navy background (`{colors.ink}`) and light text. Links are rendered in the soft parchment tone (`{colors.hairline-soft}`) and shift to gold on hover. The footer contains navigation columns, social links, and legal text. Padding is generous at 48px top and bottom.

### Dividers & Decorations
**`divider`** — A 1px horizontal rule in the warm hairline color, used between sections and card elements. A softer variant (`{divider-soft}`) is used within cards and tight spaces where a lighter touch is needed.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to {typography.display-md}; subscription tiers stack; search bar moves to expandable overlay |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero maintains two-column split; subscription tiers show 2-across; search bar remains in header |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses full display-xl; subscription tiers show 3-across; search bar is always visible |
| Wide | > 1440px | Max-width container (1440px) centered; extra whitespace on sides; product grid can show 4-across for certain categories; hero may include decorative side elements |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40px × 40px minimum
- Nav links have 8px vertical padding plus the 72px nav bar height for comfortable tapping
- Product card CTAs are full-width on mobile for easy thumb reach

### Collapsing Strategy
- Primary nav links collapse into a hamburger menu below 744px
- Secondary footer links collapse into accordion sections on mobile
- Product filters collapse into a slide-out drawer on mobile
- Multi-column subscription tier comparison collapses to a single-column vertical list
- Hero section reduces from two-column (text + image) to stacked single-column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components could not be reliably extracted from the live site; the tokens above represent best guesses based on common patterns
- Error states for forms (validation messages, error icons) were not observed on the homepage
- Dark mode or high-contrast mode styles are not present in the extracted data
- Sub-brand or seasonal color palettes (e.g., holiday editions, author collaborations) may exist but were not captured
- The exact font stack ordering and fallback chain for BrandonGro, JustCosmic, and FiraSans could not be confirmed from the extracted declarations
- Animation durations, easing curves, and transition properties were not extracted
- Drop shadow values for cards and modals are estimated based on common e-commerce patterns
- The decorative "JustCosmic" font usage context (headlines vs. accent text vs. logos) is inferred from its whimsical name
- Social media icon colors (Facebook blue `#3b5998`) are present in the palette but their exact usage context is unknown
- The extracted palette includes many colors that may be from stock imagery, limited-edition boxes, or third-party widgets rather than core brand tokens
