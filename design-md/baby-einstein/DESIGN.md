---
version: alpha
name: "Baby Einstein"
source_url: "https://www.babyeinstein.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy (#0f193f) canvas sets the stage for a brand that treats early childhood as a serious, joyful design problem — not pastel pablum but saturated primary accents (red #ec2c3e, orange #e87621, yellow #ffdf2d, green #76dca1, teal #4cbea0, blue #00b4e1, purple #aa5ea3) that pop against near-white (#f7f6f0) and light gray (#f2f2f2) backgrounds. The palette reads like a carefully curated set of wooden blocks: each color has weight and purpose, not decorative pastel. Karla and Lato run the typography, with Karla likely handling display and Lato body — a pairing that balances geometric playfulness with readable warmth. Buttons and interactive elements use generous {rounded.full} pill shapes, while product cards and content panels land on softer {rounded.md} corners. The brand's signature move is the "curiosity trigger" — a bright red or orange CTA button against the navy field, creating a visual voltage that says "touch this." Star ratings, age-range badges, and "NEW" tags appear in small, high-contrast capsules. The overall mood is not "baby store" but "children's museum gift shop" — clean, colorful, and designed for small hands and big eyes.

colors:
  primary: "#0f193f"
  primary-active: "#121127"
  primary-disabled: "#607380"
  ink: "#0d0d0d"
  body: "#212121"
  muted: "#607380"
  muted-soft: "#d1d1db"
  hairline: "#d9d9d9"
  hairline-soft: "#f1f1f1"
  canvas: "#f7f6f0"
  surface-soft: "#f2f3ee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ec2c3e"
  accent-orange: "#e87621"
  accent-yellow: "#ffdf2d"
  accent-green: "#76dca1"
  accent-teal: "#4cbea0"
  accent-blue: "#00b4e1"
  accent-purple: "#aa5ea3"
  star-rating: "#ffdf00"
  badge-new: "#ec2c3e"
  badge-sale: "#e87621"
  badge-age: "#4cbea0"

typography:
  display-xl:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Karla', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Karla', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Karla', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Karla', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Lato', 'Karla', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Karla', 'Lato', Arial, sans-serif"
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
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
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.accent-red}"
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
  badge-age:
    backgroundColor: "{colors.badge-age}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "14px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  category-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"

## Components

### Buttons
**`button-primary`** — The workhorse CTA: deep navy (#0f193f) pill with white text, used for primary actions like "Shop Now" and "Add to Cart". On hover, shifts to `primary-active` (#121127). Disabled state uses `primary-disabled` (#607380) for low-contrast but readable indication. **`button-accent-red`** and **`button-accent-orange`** are the high-energy variants — red for urgency (limited-time offers, clearance) and orange for secondary promotions (free shipping, bundle deals). Both maintain the pill shape and bold Karla 700 weight. **`button-secondary`** inverts to a canvas (#f7f6f0) fill with navy text and a 1px navy border, used for "Learn More" or "View Details" alongside primary CTAs. **`button-tertiary-text`** is a plain text link in navy, no background or border, for "See All" or "Read More" in content-rich areas.

### Cards
**`product-card`** — A white card with 12px rounded corners (`{rounded.md}`), containing a product image (top corners rounded, bottom flush), title in Karla 600 at 16px, price in Lato 400 at 16px in accent-red, and optional star rating in yellow (#ffdf00). Hover state adds a subtle shadow (2px offset, 8px blur, 10% opacity black). Cards stack in a responsive grid: 2 columns on mobile, 3 on tablet, 4 on desktop. **`hero-section`** uses the full navy background with white display text and a single red CTA pill — no secondary actions, no clutter.

### Navigation
**`top-nav`** — A 64px fixed bar on canvas (#f7f6f0) with the Baby Einstein wordmark left-aligned, category links in uppercase Karla 600, and a search icon (magnifying glass in a circle) right-aligned. Active nav links get a 2px navy bottom border; inactive links are muted (#607380). On mobile, the nav collapses into a hamburger menu with a full-screen overlay. **`category-strip`** sits below the nav on the homepage, a horizontal scrollable row of pill-shaped category tabs — active tabs fill navy, inactive tabs are soft gray (#f2f3ee) with muted text.

### Badges
**`badge-new`** — A small red (#ec2c3e) pill with white uppercase text, 11px Karla 700, used to flag new arrivals. **`badge-sale`** — Orange (#e87621) pill for sale items. **`badge-age`** — Teal (#4cbea0) pill showing age range (e.g., "0-6 months"). All badges share the same shape and typography, differentiated only by color.

### Forms
**`search-bar-pill`** — A white pill input with 48px height, 12px left padding for the search icon, and placeholder text in Lato 14px. Focus state adds a 2px navy border. **`text-input`** (not explicitly defined in tokens but used in checkout) follows the same pattern: white background, 12px rounded corners, 48px height, navy border on focus.

### Footer
**`footer`** — A full-width navy (#0f193f) section with white body text in Lato 14px. Links are muted-soft (#d1d1db) and underline on hover. Contains three columns: "Shop" (product categories), "Learn" (about, blog, FAQ), and "Connect" (social icons, newsletter signup). Social icons are white circles with 32px diameter.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to 24px; category strip becomes horizontal scroll; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero text at 28px; category strip shows 4-5 pills |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero text at 36px; category strip shows all pills |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero text at 40px |

### Touch Targets
- All buttons and interactive pills: minimum 48px height (exceeds Apple's 44px guideline)
- Search bar: 48px height for easy tap
- Category pills: 36px height with 8px padding
- Icon buttons: 40px diameter circles
- Nav links: 44px minimum tap area (padding extends beyond text)

### Collapsing Strategy
- Top nav: hamburger menu at < 744px, full horizontal links at ≥ 744px
- Product grid: collapses from 4 columns (wide) to 1 column (mobile)
- Footer: three-column layout collapses to single column at < 744px
- Category strip: horizontal scroll on mobile, full row on desktop
- Hero section: image and text stack vertically on mobile, side-by-side on tablet+

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were not extractable from static HTML/CSS — assumed standard opacity/color shifts where not specified
- Error styling for form inputs (red border, error message typography) not observed — placeholder uses navy focus border
- Dark mode not present on the live site — no tokens defined
- Sub-brand or seasonal palette variations (e.g., holiday, collaboration) not captured
- Animation and transition timing values (ease-in-out duration) not extractable
- Specific font weights for Karla and Lato beyond 400, 600, 700 are inferred — the live site may use 500 or 800 weights in some contexts
- Shopify checkout widget colors (e.g., Klarna pink, Afterpay black) were filtered from the extracted palette but may appear in cart/checkout flows
- The extracted color list includes several near-duplicates (#f2f2f2, #f7f7f7, #f9f9f9, #f1f1f1) — the most distinctive canvas tone (#f7f6f0) was chosen as primary background; others may be used in specific contexts
- Star rating color (#ffdf00) is close to accent-yellow (#ffdf2d) — the live site may use either or both depending on context
