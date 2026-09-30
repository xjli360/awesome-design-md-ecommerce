---
version: alpha
name: "Topicals"
source_url: "https://www.mytopicals.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Topicals is a skincare brand built for flare-ups — acne, eczema, hyperpigmentation, and the emotional weight that comes with chronic skin conditions. The palette is anchored by a deep, almost-black ink (`#131212`) that reads as serious and grounded, not trendy. Against that sits a warm, off-white canvas (`#f6f6f6`) and a soft card surface (`#ffffff`), creating a clean, clinical-but-comfortable stage for product photography and ingredient storytelling. The brand's primary voltage is a muted, dusty rose (`#973f54`) — not a bright millennial pink, but a sophisticated, almost vintage blush that appears on CTAs, badges, and accent typography. A secondary accent of mustard yellow (`#ffe056`) adds a pop of optimism, while a deep teal (`#00b174`) and burnt sienna (`#ac533e`) round out a palette that feels botanical, not synthetic. Red (`#f61f1f`, `#ff454e`) is reserved for urgency — sale badges, error states, or limited-edition drops. The typography system leans on ITC Garamond Std for display and headline work, lending a literary, editorial feel that separates Topicals from the sans-serif uniformity of most DTC skincare. Body copy runs in a clean monospace or system sans-serif stack, creating a deliberate tension between old-world elegance and modern utility. Rounded corners are generous but not pill-shaped — cards and buttons use `{rounded.sm}` (8px) to `{rounded.md}` (12px), while the primary CTA button uses `{rounded.sm}` with a full-height, bold presence. The brand trusts whitespace, muted hairlines (`#dadada`, `#e6e6e6`), and a restrained use of color to let product photography and ingredient callouts do the heavy lifting. The overall mood is calm, informed, and unapologetically real — no airbrushed models, no pastel gradients, just honest skin science wrapped in warm, tactile design.

colors:
  primary: "#973f54"
  primary-active: "#7a3243"
  primary-disabled: "#cf9ba8"
  ink: "#131212"
  body: "#3b3b3b"
  muted: "#888888"
  muted-soft: "#999999"
  hairline: "#dadada"
  hairline-soft: "#e6e6e6"
  canvas: "#f6f6f6"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffe056"
  accent-teal: "#00b174"
  accent-sienna: "#ac533e"
  accent-red: "#f61f1f"
  accent-red-soft: "#ff454e"
  badge-pink: "#ffc7c9"
  badge-red: "#ff454e"
  star-rating: "#131212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'ITC Garamond Std', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ITC Garamond Std', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ITC Garamond Std', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'ITC Garamond Std', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'ITC Garamond Std', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'ITC Garamond Std', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Consolas, 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Consolas, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Consolas, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'ITC Garamond Std', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'ITC Garamond Std', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "Consolas, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'ITC Garamond Std', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  badge:
    fontFamily: "Consolas, 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 14px 28px
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
    padding: 13px 27px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-sienna}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  ingredient-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and "Subscribe". It uses the brand's dusty rose (`{colors.primary}`) as a solid background with white text (`{colors.on-primary}`) set in ITC Garamond Std at 16px with 0.5px letter spacing. On hover, it shifts to `{colors.primary-active}` (#7a3243). In its disabled state, it fades to `{colors.primary-disabled}` (#cf9ba8) with no shadow or border. The button has 8px rounded corners and a 48px height, giving it a substantial, grounded feel.

**`button-secondary`** — An outlined or ghost variant for secondary actions like "Learn More" or "View Ingredients". It uses the canvas background (`{colors.canvas}`) with ink text (`{colors.ink}`) and a 1px hairline border (`{colors.hairline}`). On hover, the border thickens to 2px and the background shifts to `{colors.surface-soft}`. It shares the same 48px height and 8px rounded corners as the primary button for visual consistency.

**`button-tertiary-text`** — A text-only button for subtle actions like "Cancel" or "Skip". It has no background or border, only ink text (`{colors.ink}`) with an underline on hover. Used sparingly to avoid visual clutter.

**`button-pill-primary`** — A pill-shaped variant (9999px radius) for promotional banners, sticky CTAs, or mobile bottom sheets. It uses the primary rose background with white text and a smaller 14px font. The pill shape signals urgency or a limited-time offer.

### Cards
**`product-card`** — The core product display unit, used on collection pages and the homepage. It has a white background (`{colors.surface-card}`), 12px rounded corners, and a subtle shadow (not defined in tokens but implied by the card surface). The image area has rounded top corners (`{rounded.md} {rounded.md} 0 0`) to create a clean break between photo and text. Product name is set in `{typography.title-sm}`, price in `{typography.body-md}`, and a badge (sale, new, or limited) sits in the top-left corner of the image.

**`hero-section`** — The full-width hero banner on the homepage. It uses the canvas background (`{colors.canvas}`) with a large display headline (`{typography.display-xl}`) set in ITC Garamond Std at 48px. The hero CTA button is larger than standard (16px padding vertical, 32px horizontal) to anchor the visual hierarchy. The hero may include a background image or pattern, but the text and button remain centered with generous whitespace.

### Navigation
**`nav-bar`** — A fixed top navigation bar with a white background, 72px height, and ink text. Links are set in ITC Garamond Std at 16px with 0.3px letter spacing. The active link uses the primary rose color with a 2px bottom border. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — Standard text input for email signups, search, and checkout forms. It has a white background, 8px rounded corners, a 1px hairline border (`{colors.hairline}`), and 16px monospace body text. On focus, the border becomes 2px solid primary rose (`{colors.primary}`). The height is 48px to match button heights for form alignment.

**`search-bar`** — A pill-shaped search input (9999px radius) used in the nav or on the search page. It has a white background, 1px hairline border, and 48px height. The placeholder text is set in `{typography.body-md}` with muted color (`{colors.muted}`).

### Badges
**`badge-sale`** — A small, uppercase badge with red background (`{colors.accent-red}`) and white text. Used on product cards to indicate discounts or promotions. It has 4px rounded corners and tight padding (4px 8px).

**`badge-new`** — A teal badge (`{colors.accent-teal}`) for new product launches. Same shape and size as the sale badge but with a different accent color to differentiate the message.

**`badge-limited`** — A burnt sienna badge (`{colors.accent-sienna}`) for limited-edition drops. Creates a sense of scarcity and aligns with the brand's botanical, earthy palette.

### Footer
**`footer-section`** — A dark footer with ink background (`{colors.ink}`) and white text. Links are set in monospace at 14px with muted-soft color (`{colors.muted-soft}`). The footer includes columns for "Shop", "Learn", "Community", and "Support", plus social media icons and an email signup form. Padding is generous (48px vertical, 16px horizontal) to create breathing room.

### Accordion
**`accordion`** — Used for FAQ sections and ingredient details. Each accordion item has a white background, 8px rounded corners, and a 1px soft hairline border (`{colors.hairline-soft}`). The header is set in `{typography.title-sm}` with ink text, and the body content uses `{typography.body-sm}`. On open, the header text color shifts to primary rose (`{colors.primary}`).

### Ingredient Callout
**`ingredient-callout`** — A soft, muted card used to highlight key ingredients (e.g., "Niacinamide", "Retinol", "Azelaic Acid"). It has a soft surface background (`{colors.surface-soft}`), 8px rounded corners, and body-sm monospace text. The ingredient name is bolded and set in title-sm. These callouts are used in product descriptions and educational content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text scales down to 28px; buttons become full-width; search bar moves to sticky bottom; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero text at 36px; side-by-side ingredient callouts; footer in two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 48px; multi-column footer; accordions in two-column layout |
| Wide | > 1440px | Max-width container at 1440px; centered content; larger hero padding; product grid can expand to four columns; increased whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and width of 44px to meet WCAG touch target guidelines.
- Nav bar hamburger icon is 48x48px.
- Product card CTAs are at least 48px tall.
- Accordion headers have a 48px tap area.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger menu with a full-screen overlay. The search bar moves to a sticky bottom bar.
- Product cards stack into a single column on mobile, two columns on tablet, and three on desktop.
- Footer columns collapse into a single column on mobile, with accordion-style expandable sections for each column.
- The hero section reduces font size and padding on mobile to avoid overflow.
- Accordions remain single-column on mobile and tablet, expanding to two columns on desktop.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components beyond primary/secondary buttons are not reliably extracted (e.g., product card hover shadow, nav link underline animation, accordion hover background).
- Error and validation styling for forms (red border, error message typography, success state) is not fully documented.
- Dark mode or high-contrast mode tokens are not available.
- Sub-brand or collection-specific palettes (e.g., "Faded" vs. "Like Butter" product lines) may have unique accent colors not captured here.
- Animation and transition timing (ease-in-out durations, spring curves) are not defined.
- Shadow tokens (box-shadow for cards, modals, dropdowns) are missing.
- Modal, drawer, and overlay component specs are not extracted.
- Loading states (skeleton screens, spinners) are not documented.
- Typography scale for mobile (font-size reductions) is inferred but not confirmed from source.
- Specific icon set and icon sizing guidelines are not available.
- Print stylesheet behavior is unknown.
