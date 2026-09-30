---
version: alpha
name: "Because"
source_url: "https://becausemarket.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A muted, earth-toned canvas of #fcfcf4 — the color of unbleached linen or morning light through a muslin curtain — sets the stage for a brand that treats personal care for aging bodies with the same visual dignity as a minimalist home-goods catalog. The extracted palette reads like a desert landscape: sage-adjacent #f2f2ea, warm stone #f5f5dc, and the surprising jolt of #08c5bc, a teal that appears in key interactive moments like a cool spring in dry terrain. Typography splits between DM Sans for clean, legible body copy and Petrona for display — a serif choice that signals warmth and editorial care rather than clinical efficiency. Buttons carry {rounded.full} pill shapes, softening every transaction, while product cards use {rounded.md} to frame incontinence garments and bathing aids as objects of quiet consideration rather than medical supplies. The brand's voice is low-volume: muted grays (#9ca3af, #777777) handle secondary information, hairline borders are soft (#e5e7eb), and the deep ink (#242527) never screams. There is no hard edge, no urgent red, no flash-sale pulse — Because trusts that a 64px section of whitespace and a Petrona display-xl header say "we understand" louder than any discount badge could.

colors:
  primary: "#08c5bc"
  primary-active: "#069e97"
  primary-disabled: "#b3f0ed"
  ink: "#242527"
  body: "#4a4a4a"
  muted: "#777777"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f2f2f2"
  canvas: "#fcfcf4"
  surface-soft: "#f2f2ea"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#8c564b"
  accent-sage: "#f5f5dc"
  accent-stone: "#dedede"
  star-rating: "#242527"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Petrona', 'DM Sans', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Petrona', 'DM Sans', Georgia, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'DM Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  section-heading:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a full pill in teal (#08c5bc) against white text. Hover darkens to #069e97. Disabled state uses a washed-out teal (#b3f0ed) with white text. Used for "Subscribe," "Add to Cart," and "Start Quiz." The pill shape and generous 14px 28px padding make the button feel approachable, not pushy.

**`button-secondary`** — An outlined or ghost pill on the canvas background (#fcfcf4) with ink (#242527) text. Used for "Learn More" and "See Details" actions. Maintains the same 48px height as primary for alignment in forms.

**`button-tertiary-text** — A text-only button with no background, using primary teal for the text. Used for "Skip this step" or "Cancel" in multi-step flows. Hover state adds a subtle underline.

### Cards
**`product-card`** — A white card on the soft canvas background, with 12px rounded corners. Contains a product image (also 12px rounded), product name in body-sm, price in caption, and an optional badge. The card has no shadow — the brand relies on the contrast between the white card and #fcfcf4 canvas for separation. Hover state adds a 1px hairline border (#e5e7eb).

**`product-card-badge`** — A small uppercase pill badge in warm brown (#8c564b) with white text. Used for "Best Seller," "New," or "For Men" labels. The warm accent provides a gentle visual anchor without competing with the primary teal.

### Navigation
**`nav-bar`** — A 72px fixed top bar on the canvas background. Logo sits left, nav links center, cart and account icons right. The nav uses DM Sans at 15px weight 500 — intentionally smaller and lighter than typical e-commerce navs to maintain the brand's low-volume voice. Active link is underlined in primary teal.

### Forms
**`text-input`** — A white input field with 8px rounded corners and 12px 16px padding. Border is hairline (#e5e7eb) by default, switching to primary teal on focus. Placeholder text uses muted (#777777). Used for email signup, shipping address, and quiz responses.

### Search
**`search-bar`** — A full pill search input on white background, with muted placeholder text. The search icon is rendered in primary teal. Used on the shop page and blog. Focus state expands the input width slightly and adds a teal border.

### Footer
**`footer-link`** — A text link in muted gray (#777777) on the canvas background. Used for legal pages, help center, and social links. Hover state transitions to ink (#242527). No underline — the brand trusts color change alone for affordance.

### Hero
**`hero-section`** — A full-width section on the canvas background, with 64px vertical padding. Uses display-xl in Petrona serif for the headline, body-md for subtext, and a single button-primary CTA. The hero may include a product image or lifestyle photography with soft rounded corners.

### Section Headings
**`section-heading`** — A Petrona serif heading at 28px weight 500, used to introduce product categories, testimonials, or educational content. No underline or decorative element — the serif itself provides enough visual weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero padding reduces to 32px; product cards stack vertically; search bar moves below logo; buttons go full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses 48px padding; search bar in top nav |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses 64px padding; search bar in top nav |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to four columns; hero content centered with wider margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain at least 44px height for touch accessibility
- Product card tap targets (image, title, add-to-cart) are at least 48px tall
- Nav hamburger icon is 44x44px with 8px padding
- Search bar is 48px tall on all breakpoints

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; all nav links move into a slide-out drawer
- Product grid collapses from 3 columns to 2 at tablet, to 1 at mobile
- Hero section collapses from side-by-side (image + text) to stacked at tablet
- Footer link columns collapse from 4 to 2 at tablet, to 1 at mobile
- Search bar collapses from inline in nav to a full-width expandable field at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were not reliably extracted from the live site; the active/disabled states above are inferred from the primary color and common accessibility patterns
- Error styling (form validation, input error borders, error messages) was not observed; a red accent (#d62728 appeared in extracted colors but may be a checkout widget color — use with caution)
- Dark mode is not supported and no dark-mode tokens were extracted
- Sub-brand or promotional palettes (holiday, limited edition) were not observed
- The exact font weights for Petrona and DM Sans beyond those listed were not confirmed; the weights above are based on common usage in DTC brands
- Animation and transition durations/easings were not extracted; assume 200ms ease-in-out for hover/focus transitions
- The star-rating component size (16px) is an estimate; actual rendering may vary
- The extracted color list includes many generic web and checkout-widget colors (#1f77b4, #ff7f0e, #2ca02c, etc.) — the brand's true primary is #08c5bc, which appears as the most distinctive accent in the palette
