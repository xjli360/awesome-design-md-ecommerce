---
version: alpha
name: "OwlCrate"
source_url: "https://www.owlcrate.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A midnight-blue (#282560) and teal (#86e4e0) subscription world where bookish discovery meets tactile monthly ritual. The brand lives in the tension between deep, almost-navy indigos (#1c1b2e, #141321) and bright, minty aquas (#86e4e0, #19cfd2) — a palette that reads as both cozy and magical, like a reading nook lit by a glowing screen. Every primary CTA and interactive element pulses in that signature teal, while the dark backgrounds create a sense of intimate immersion, as if each page turn happens in a quiet corner of a fantastical library. The typography leans on Asul and Figtree — Asul for display moments that carry a slightly hand-drawn, whimsical weight, and Figtree for body text that stays clean and readable across product descriptions and subscription details. Rounded corners are generous but not pillowy: cards and buttons use `{rounded.md}` (12px) to feel approachable without losing structure, while badges and small tags go tighter at `{rounded.sm}` (8px). The brand's voice is enthusiastic and direct — "Get the Box" buttons in teal against dark backgrounds feel like invitations to join a secret club, not transactional prompts. Product cards feature stacked imagery (the box, its contents, lifestyle shots) with overlays and badges in coral (#c16452), gold (#ffcb67), and deep purple (#4d384b) to denote exclusives, spoilers, and member perks. The footer and secondary navigation retreat into muted lavenders (#cecdeb, #e5e5f5) and soft grays (#f4f4f6), keeping the visual hierarchy clear: dark and teal for action, light and muted for information. OwlCrate feels like a subscription box designed by someone who loves the weight of a hardcover and the surprise of a wrapped package — digital, but reaching toward the physical.

colors:
  primary: "#86e4e0"
  primary-active: "#19cfd2"
  primary-disabled: "#b2f9e9"
  ink: "#141321"
  body: "#1c1b2e"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5f5"
  canvas: "#fcfcff"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#141321"
  accent-coral: "#c16452"
  accent-gold: "#ffcb67"
  accent-purple: "#4d384b"
  accent-green: "#3ea36a"
  accent-red: "#c20000"
  accent-blue: "#126bbf"
  accent-teal-dark: "#00afa6"
  accent-teal-light: "#ebfbfa"
  badge-new: "#c16452"
  badge-exclusive: "#ffcb67"
  badge-spoiler: "#4d384b"
  star-rating: "#ffcb67"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Asul', 'Georgia', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Asul', 'Georgia', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Asul', 'Georgia', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Asul', 'Georgia', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Avenir Next', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px

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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 48px
  button-secondary-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption-sm}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 32px
  section-heading:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
  section-subheading:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-icon:
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 3px 8px
  badge-exclusive:
    backgroundColor: "{colors.badge-exclusive}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 3px 8px
  badge-spoiler:
    backgroundColor: "{colors.badge-spoiler}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 3px 8px
  subscription-tier-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  subscription-tier-card-highlighted:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: 2px solid "{colors.primary}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  testimonial-card-avatar:
    rounded: "{rounded.full}"
    height: 48px
  icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
  icon-circle-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's signature teal (#86e4e0) against the dark ink background or on white canvas. Uses `{typography.button-md}` (16px, weight 600) with `{rounded.md}` (12px) corners for a friendly but grounded feel. On hover, shifts to the deeper `{colors.primary-active}` (#19cfd2); disabled state fades to `{colors.primary-disabled}` (#b2f9e9) with muted text. Padding is generous at 14px 28px to create a substantial tap target.

**`button-secondary`** — An outlined or ghost-style button used for "Learn More" and secondary actions. Rendered on white canvas with ink text and a 1px hairline border. The dark variant (`button-secondary-dark`) inverts for use on light backgrounds within dark sections, using teal text on the ink background. Both maintain the same `{rounded.md}` and `{typography.button-md}` sizing for visual consistency.

**`button-tertiary-text`** — A text-only link styled as a button, used for "View All" or "See Details" links within card grids. Transparent background, teal text, and the same `{typography.button-md}` sizing. No border or rounded corners — relies on hover underline or color shift for interactivity.

**`button-pill-accent`** — A fully rounded pill button reserved for promotional badges and limited-time offers. Uses the coral accent (#c16452) for urgency, white text, and `{typography.button-sm}` (14px, weight 600). Typically appears on hero sections or featured product cards.

### Cards
**`product-card`** — The core content container for monthly boxes and individual products. White background with `{rounded.md}` (12px) corners, body-sm typography for descriptions, and title-sm for pricing. The image area uses the same corner radius for visual continuity. Badges overlay the top-left corner of the image area using `product-card-badge` styling — coral background, uppercase 11px weight-700 type, with `{rounded.sm}` (8px) corners and 4px 10px padding.

**`subscription-tier-card`** — A larger, more detailed card used on the subscription comparison page. Standard variant has a white surface with `{rounded.md}` and 32px padding. The highlighted variant uses the ink background with a 2px teal border and white text, making the recommended tier visually distinct. Both use `{typography.body-md}` for descriptions and `{typography.title-md}` for tier names.

**`testimonial-card`** — A soft gray (`{colors.surface-soft}`) card for customer quotes and reviews. Uses `{rounded.md}` and 24px padding. The avatar circle uses `{rounded.full}` at 48px. Star ratings render in the gold accent (#ffcb67) using `{typography.caption-sm}`.

### Navigation
**`nav-bar`** — The primary site header, 72px tall on desktop, using white canvas with ink text. Navigation links use `{typography.nav-link}` (15px, weight 600, 0.3px letter spacing). Active links shift to teal. On scroll, the bar transitions to an ink background with white text and shrinks to 64px — a dark, immersive header that signals depth. The mobile menu icon uses the `icon-circle` pattern (40px, soft gray background, teal icon).

**`nav-link-active` / `nav-link-inactive`** — Active nav links render in teal (`{colors.primary}`) with no background; inactive links use muted gray (`{colors.muted}`). Both maintain the same `{typography.nav-link}` sizing for consistent spacing.

### Forms
**`text-input`** — Standard text input fields for search, email signup, and account forms. White background, `{rounded.sm}` (8px) corners, 12px 16px padding, 48px height, and a 1px hairline border. On focus, the border thickens to 2px and switches to teal. Error state uses a 1px red border (`{colors.accent-red}`). Typography is `{typography.body-md}` (16px) for readability.

**`search-bar`** — A pill-shaped search field (`{rounded.full}`) used in the header and on collection pages. Soft gray background (`{colors.surface-soft}`), 12px 20px padding, 48px height. The search icon renders in muted gray. Typography matches `{typography.body-md}`.

### Footer
**`footer`** — A dark, full-width footer on the ink background. Links use `{typography.link}` (14px, weight 500) in muted-soft gray (#9a9db1), shifting to teal on hover. Section headings use `{typography.title-sm}` in white. Dividers between sections use `{colors.hairline}` (#dbdde4) at 1px. Social icons use the `icon-circle-dark` pattern (ink background, teal icon, 40px).

### Badges
**`badge-new`** — Coral background (#c16452), white text, uppercase 11px weight-700, `{rounded.sm}` (8px), 3px 8px padding. Used for "New" indicators on products and collections.

**`badge-exclusive`** — Gold background (#ffcb67), ink text, same typography and sizing. Used for member-exclusive items and early-access badges.

**`badge-spoiler`** — Purple background (#4d384b), white text, same typography and sizing. Used for spoiler-tagged content and unboxing previews.

### Miscellaneous
**`icon-circle`** — A 40px circle with soft gray background and teal icon, used for social media links, utility icons, and decorative elements. The dark variant (`icon-circle-dark`) inverts for use on light backgrounds.

**`divider`** — A 1px horizontal rule in hairline gray (#dbdde4). The soft variant (`divider-soft`) uses #e5e5f5 for lighter separation within cards and sections.

**`loading-spinner`** — A teal (#86e4e0) spinning indicator used during async operations like subscription loading and cart updates.

**`tooltip`** — A small, dark tooltip with ink background, white text, `{rounded.sm}` (8px), and 6px 12px padding. Uses `{typography.caption-sm}` (12px, weight 400).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layouts; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces to 28px display type; search bar moves into collapsible drawer; subscription tier cards stack; footer links collapse into accordion |
| Tablet | 744–1128px | Two-column product grids; nav-bar shows 4-5 primary links; hero maintains 32px display type; search bar remains visible but compact; subscription tier cards display in 2-column grid |
| Desktop | 1128–1440px | Three-column product grids; full nav-bar with all links; hero uses 36px display-xl; search bar full-width in header; subscription tier cards in 3-column grid; footer columns display inline |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grids can expand to 4 columns; hero section uses larger imagery; additional whitespace around cards and sections |

### Touch Targets
- All buttons and interactive elements maintain minimum 48px height for touch accessibility
- Icon circles and avatar elements are 40px minimum
- Nav links have 44px minimum tap area (padding + height)
- Search bar and text inputs are 48px tall
- Product card CTAs maintain 48px height with 14px vertical padding
- Badges and tags are minimum 24px height with adequate padding

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-in drawer from the left
- Product grids collapse from 3 columns to 2 at tablet, to 1 at mobile
- Subscription tier comparison collapses from 3 columns to stacked cards
- Footer link columns collapse to accordion-style expandable sections below 744px
- Hero section reduces font size and stacks CTA buttons vertically on mobile
- Search bar collapses to an icon-triggered overlay on mobile
- Product card badges shift from corner overlay to inline placement on mobile
- Testimonial carousel collapses to single-card display on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons and text inputs could not be reliably extracted from the live site — assumed standard opacity shifts (90% for hover, 60% for disabled) pending design review
- Error styling for forms (validation messages, error icons) was not observed — placeholder assumes red border and caption-style error text
- Dark mode is not implemented on the live site; all dark sections use the ink palette directly
- Sub-brand palettes (OwlCrate Jr., OwlCrate Adult, special editions) may exist but were not distinguishable from the extracted color data
- Animation and transition timing values (hover transitions, page load animations, card entrance effects) were not extractable
- Dropdown menu styling (mega menus, account dropdowns) was not observed in the extracted data
- Modal and overlay styling (lightbox, cart drawer, quick-view) was not captured
- Checkout flow styling (Shopify checkout, payment form elements) uses default Shopify theme styles and was excluded from the design system
- Stock image dominant tones may have influenced some extracted hex values — the palette has been curated to brand-consistent colors
- Font weights beyond the extracted declarations (Asul appears only in 700, Figtree in 400/500/600) are assumed based on common web usage
- Letter-spacing values for display typography are estimated from visual inspection and may require adjustment
- The extracted color list contained several Shopify-default blues and grays that were filtered; the remaining palette is believed to be brand-accurate
