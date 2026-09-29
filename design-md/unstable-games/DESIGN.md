---
version: alpha
name: "Unstable Games"
source_url: "https://www.unstablegames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Coral-red splashes (#f95346) punch through a near-black stage (#121212) like card art leaping off the table — every CTA and sale badge vibrates at that frequency, daring the visitor to click before the chaos resolves. The color system mirrors a hand of wildly different game decks: teal (#23b192) tags the flagship Unstable Unicorns line, lime (#84bd00) marks family-friendly titles, forest green (#228848) anchors the navigation layer, and a hot orange (#ff8441) fires off limited-edition callouts. Typography stays utilitarian — Source Sans Pro and Open Sans in modest weights keep the eye on illustrated box art rather than competing with it. The layout philosophy is a grid of product cards with generous `{spacing.lg}` gutters, each card floating on `{colors.surface-card}` with a soft `{rounded.md}` radius that rounds just enough to feel toy-like without becoming juvenile. Hero sections run full-bleed on dark canvas (`{colors.ink}`) with oversized game illustrations, animated sparkle particles, and countdown timers for Kickstarter drops — the brand treats every product launch like an event, not a catalog update. Navigation collapses into a mega-menu organized by game franchise rather than generic "shop" categories; each franchise carries its own accent swatch. Buttons favor pill shapes (`{rounded.full}`) at small sizes and squared-off solids (`{rounded.sm}`) for cart actions, splitting playful browsing gestures from transactional commitment. The footer is dense, almost wiki-like, linking rulebooks, FAQ entries, and community Discord — a signal that the post-purchase relationship matters as much as the sale. Shadows are minimal; depth comes from color contrast against the dark canvas rather than elevation, giving the whole experience the flat-but-vivid energy of printed card stock.

colors:
  primary: "#f95346"
  primary-active: "#e03d31"
  primary-disabled: "#f9534680"
  accent-teal: "#23b192"
  accent-lime: "#84bd00"
  accent-green: "#228848"
  accent-orange: "#ff8441"
  ink: "#121212"
  body: "#202020"
  muted: "#6b6b6b"
  hairline: "#d3d3d3"
  hairline-soft: "#dedede"
  border-subtle: "#e0e0e0"
  canvas: "#ffffff"
  canvas-dark: "#121212"
  surface-soft: "#f7f7f7"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-dark-muted: "#d3d3d3"
  sale-badge: "#f95346"
  success: "#228848"

typography:
  display-xl:
    fontFamily: "'Source Sans Pro', 'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.4px
    textTransform: uppercase
  price:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Source Sans Pro', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through

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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.ink}
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.xl}
  nav-bar-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg} {spacing.xl}"
    boxShadow: 0 8px 24px rgba(0,0,0,0.12)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageRatio: 1:1
    hoverTransform: translateY(-4px)
    boxShadow: 0 2px 8px rgba(0,0,0,0.06)
    hoverBoxShadow: 0 8px 24px rgba(0,0,0,0.1)
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-compare-price:
    typography: "{typography.price-compare}"
    textColor: "{colors.muted}"
  hero-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 520px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 16px 36px
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  franchise-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  collection-header:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    padding: 0 {spacing.base}
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark-muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  countdown-timer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: 0 16px 48px rgba(0,0,0,0.2)
---

## Components

### Buttons

**`button-primary`** — Solid coral-red (#f95346) fill with white text, used for all primary conversion actions: "Add to Cart," "Shop Now," and newsletter signup. On hover, darkens to `primary-active` (#e03d31) with a subtle 150ms ease transition. Disabled state drops to 50% opacity. Height sits at 48px with `{rounded.sm}` corners for a clean, decisive shape.

**`button-secondary`** — Transparent background with a 2px solid ink border, used for secondary actions like "View Rules" or "Learn More." On hover, fills with `{colors.ink}` and text flips to white. Maintains the same 48px height as primary to sit inline without visual jitter.

**`button-pill`** — Compact coral pill (`{rounded.full}`) for inline CTAs within hero banners and promotional carousels. Smaller padding and `{typography.button-sm}` keep it subordinate to the main cart button.

**`button-add-to-cart`** — Oversized variant of primary at 52px height with extra horizontal padding, used exclusively on product detail pages. The additional mass signals finality and draws the thumb on mobile.

### Navigation

**`nav-bar`** — Full-width dark bar (`{colors.canvas-dark}`) at 64px height. Logo sits left, franchise mega-menu links center, cart icon with quantity badge right. Text uses `{typography.nav-link}` in white. On scroll, a subtle bottom border in `{colors.muted}` fades in to separate nav from content.

**`nav-bar-mega-menu`** — Drops below nav on hover/click, white background with game franchise columns. Each franchise shows its accent color as a left-border indicator (teal for Unicorns, lime for family games, orange for limited editions). Dismisses on outside click or Escape key.

### Product Cards

**`product-card`** — Square image ratio (1:1) showing box art on `{colors.surface-card}` background with `{rounded.md}` corners. On hover, card lifts 4px with expanded shadow, inviting interaction. Title below in `{typography.title-sm}`, price in `{typography.price}`. Compare-at prices show struck-through in muted gray beside the active price.

**`sale-badge`** — Small uppercase label in coral-red, positioned absolute top-left of the product card image area. Indicates percentage-off or "NEW" status. Uses `{typography.badge-label}` at 11px bold with tight letter-spacing for legibility at small sizes.

**`franchise-badge`** — Identical structure to sale-badge but in `{colors.accent-teal}` or the relevant franchise color. Communicates which game family a product belongs to at a glance.

### Hero Sections

**`hero-dark`** — Full-bleed dark canvas section with minimum 520px height. Large illustrated game art bleeds edge-to-edge as a background image, with a gradient overlay from left ensuring text readability. Display text in `{typography.display-xl}` left-aligned, with a `hero-cta` pill button below. Used for featured launches and seasonal campaigns.

**`countdown-timer`** — Inline block within hero sections showing days/hours/minutes/seconds in `{typography.display-sm}` on dark rounded containers. Each time unit sits in its own `{rounded.sm}` box separated by `{spacing.sm}` gaps. Used for Kickstarter launches and limited-edition drops.

### Collection & Content

**`collection-header`** — Dark banner at the top of collection pages with the collection title in `{typography.display-md}` centered. Optional subtitle in `{typography.body-md}` with `{colors.on-dark-muted}` sits below.

**`announcement-bar`** — Slim 36px bar pinned above the nav in `{colors.accent-green}` with white caption text. Communicates shipping thresholds, active promotions, or event countdowns. Auto-rotates multiple messages with a fade transition.

### Search

**`search-overlay`** — Modal overlay triggered by the nav search icon. White card with `{rounded.md}` corners, large shadow, and an autofocused text input. Results populate below the input as product rows with thumbnail, title, and price. Closes on overlay-click or Escape.

### Footer

**`footer`** — Dense dark section with four columns: Shop (game links), Support (FAQ, rules, returns), Community (Discord, social links), and Newsletter signup. Headings use `{typography.title-sm}` in white; body links in `{colors.on-dark-muted}` that brighten to white on hover. A bottom row carries copyright and payment icons.

### Form Inputs

**`text-input`** — 48px height input with 1px `{colors.hairline}` border, transitioning to `{colors.ink}` on focus. Placeholder text in `{colors.muted}`. Used in search, newsletter signup, and checkout flows. Error state swaps border to `{colors.primary}` with a caption-sized message below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-up cards). Nav collapses to hamburger + slide-out drawer. Hero text shrinks to `{typography.display-md}`. Mega-menu becomes accordion. Announcement bar text truncates with ellipsis. |
| Tablet | 744–1128px | 3-column product grid. Nav shows logo + hamburger; cart remains visible. Hero maintains full-bleed but reduces min-height to 400px. Footer stacks to 2×2 column layout. |
| Desktop | 1128–1440px | 4-column product grid. Full nav with mega-menu on hover. Hero at full 520px height. All components at designed scale. Countdown timer displays inline within hero. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Product grid may expand to 5 columns. Additional whitespace buffers on hero edges. Footer columns spread with extra gutter. |

### Touch Targets

- All interactive elements maintain minimum 44×44px touch area on mobile
- Product cards expand tap target to full card surface (not just title or image)
- Nav hamburger icon padded to 48×48px hit zone
- Close buttons on modals/drawers sized at 44×44px minimum
- Announcement bar dismiss (×) enlarged to 36×36px on mobile

### Collapsing Strategy

- Mega-menu franchise columns collapse to vertical accordion on mobile, each franchise as an expandable section
- Product grid transitions: 5-col → 4-col → 3-col → 2-col at breakpoints
- Hero CTA stack changes from horizontal (desktop) to vertical (mobile) when multiple buttons present
- Footer columns collapse to single accordion stack on mobile with expandable headings
- Collection filters move from sidebar (desktop) to bottom-sheet drawer (mobile)
- Countdown timer digits shrink from `{typography.display-sm}` to `{typography.title-md}` on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No CSS custom properties or design tokens file was detected; colors and fonts were inferred from rendered page extraction only
- Exact border-radius values on product cards and buttons could not be measured precisely — `{rounded.sm}` and `{rounded.md}` are approximations from visual inspection
- Animation/transition timing values (hover effects, mega-menu open, carousel autoplay interval) are estimated defaults
- The site likely loads additional web fonts or icon fonts via JavaScript that did not appear in static extraction
- Exact spacing scale could not be confirmed from CSS — values follow common Shopify theme patterns
- Dark mode or alternate theme states were not detected but may exist for seasonal campaigns
- Specific box-shadow values on hover states are approximations; actual implementation may use Shopify theme settings
- Game franchise accent color assignments (which color maps to which game line) are inferred from page context, not from a documented token system
