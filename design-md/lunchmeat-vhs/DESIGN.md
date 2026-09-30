---
version: alpha
name: "Lunchmeat VHS"
source_url: "https://lunchmeatvhs.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A neon-lit archive of analog horror, built on a black canvas (#000000) that makes every VHS sleeve glow like a cathode-ray tube. The palette is a riot of 90s video-rental fluorescence — #f48120 tangerine, #ffd800 safety yellow, #cc0066 magenta — all competing for attention against a #1d1c1c near-black background that feels like a Blockbuster after closing time. The brand’s primary voltage is #006fcf, a deep electric blue that anchors the chaos across navigation bars and primary CTAs, while #fba900 and #f58720 serve as accent flares for badges and price tags. Typography defaults to system sans-serif stacks (no custom font declarations found), relying on weight contrast and generous letter-spacing to evoke the blocky, hyper-legible text of VHS packaging inserts. Cards use sharp {rounded.sm} corners — nothing pill-soft — and product grids stack with tight {spacing.sm} gutters that mimic the density of a rental shelf. The search bar sits as a full-width banner with {rounded.none}, a deliberate break from the pill-shaped conventions of modern ecommerce. Every button is a slab of color with no gradient, no shadow, no subtlety — the interface is loud, direct, and unapologetically nostalgic.

colors:
  primary: "#006fcf"
  primary-active: "#005ab9"
  primary-disabled: "#3086c8"
  ink: "#1d1c1c"
  body: "#232323"
  muted: "#444444"
  muted-soft: "#5f6368"
  hairline: "#dedede"
  hairline-soft: "#444444"
  canvas: "#000000"
  surface-soft: "#1d1c1c"
  surface-card: "#231f20"
  on-primary: "#ffffff"
  accent-tangerine: "#f48120"
  accent-yellow: "#ffd800"
  accent-magenta: "#cc0066"
  accent-orange: "#fba900"
  accent-fire: "#f58720"
  accent-deep-blue: "#1e3764"
  badge-sale: "#f48120"
  badge-new: "#ffd800"
  badge-exclusive: "#cc0066"
  star-rating: "#fba900"
  error: "#eb001b"
  success: "#34a853"
  warning: "#fbbc04"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.15px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.accent-tangerine}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-tangerine:
    backgroundColor: "{colors.accent-tangerine}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.accent-tangerine}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-tangerine}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-full:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-tangerine}"
    fontWeight: 700
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-exclusive:
    backgroundColor: "{colors.badge-exclusive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  star-rating:
    textColor: "{colors.star-rating}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  section-heading:
    typography: "{typography.display-lg}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.lg} 0"
  filter-tag:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 12px
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 12px
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in electric blue (#006fcf) with white text. Used for "Add to Cart", "Checkout", and "Browse" actions. On hover, shifts to `{colors.primary-active}` (#005ab9). Disabled state uses `{colors.primary-disabled}` (#3086c8) with reduced opacity. Sharp 4px corners (`{rounded.sm}`) reinforce the no-nonsense, retro-video-store feel.

**`button-secondary`** — An outlined-style button using the dark card surface (`{colors.surface-card}`) with tangerine (#f48120) text. Used for secondary actions like "View Details" or "Save for Later". Maintains the same 44px height and 4px corner radius as the primary button for visual consistency.

**`button-accent-tangerine`** — A high-impact button using the brand's signature tangerine (#f48120) with dark ink (#1d1c1c) text. Reserved for promotional CTAs, limited-time offers, and sale announcements. The bright orange against black creates the highest contrast in the system.

**`button-accent-yellow`** — A safety-yellow (#ffd800) button with dark ink text, used sparingly for "New Arrivals" or "Pre-Order" actions. The yellow evokes the classic Blockbuster and Suncoast video-store signage.

**`button-ghost`** — A transparent-background button with tangerine text, used for tertiary actions like "Cancel" or "Learn More". No border, no background — just the accent color on the dark canvas.

### Navigation
**`top-nav`** — A 60px fixed-height bar on pure black (#000000) with uppercase, letter-spaced nav links. The brand logo sits left-aligned, with category links (VHS, Blu-ray, Merch, etc.) center or right. Active links glow in tangerine (#f48120), inactive links sit in muted gray (#444444). No dropdown menus — the nav is flat and direct.

**`nav-link-active`** — Uppercase, 14px, weight 600, letter-spaced 0.5px, rendered in tangerine. The active state is the only color deviation from the otherwise monochrome nav.

**`nav-link-inactive`** — Same typography as active, but in `{colors.muted}` (#444444). Hover state transitions to `{colors.accent-tangerine}`.

### Search
**`search-bar-full`** — A full-width, sharp-cornered search bar that spans the content area. Background is the dark card surface (#231f20) with muted placeholder text (#444444). No rounded corners — this is a deliberate departure from the pill-shaped search conventions of modern ecommerce. The search icon sits left-aligned in tangerine.

### Product Cards
**`product-card`** — A compact card on the dark surface (#231f20) with 4px rounded corners. Contains a product image (typically a VHS sleeve or Blu-ray cover), the title in `{typography.title-sm}`, and the price in tangerine (#f48120) at weight 700. Cards stack in a responsive grid with `{spacing.sm}` gutters, mimicking the density of a rental shelf.

**`product-card-title`** — 16px, weight 600, white text. Truncates to one line with ellipsis on overflow.

**`product-card-price`** — 16px, weight 700, tangerine text. Sale prices appear in the same tangerine, while regular prices may appear in muted gray.

### Badges
**`badge-sale`** — A small tangerine (#f48120) badge with dark ink text, 10px uppercase, letter-spaced 0.5px. Used to flag discounted items. 2px corner radius (`{rounded.xs}`).

**`badge-new`** — A safety-yellow (#ffd800) badge with dark ink text. Used for new arrivals or recently added inventory.

**`badge-exclusive`** — A magenta (#cc0066) badge with white text. Reserved for limited-edition releases, signed copies, or store exclusives.

### Filters & Pagination
**`filter-tag`** — A pill-shaped tag on the dark card surface with muted text. Used for category filters (Horror, Sci-Fi, Action, etc.). Active state fills with the primary blue (#006fcf) and white text.

**`filter-tag-active`** — The active filter state, rendered in primary blue with white text. The pill shape (`{rounded.full}`) is the only rounded-full element in the system, creating a subtle distinction for active selections.

**`pagination-button`** — Square 4px-cornered buttons for page navigation. Inactive buttons use the dark card surface with muted text. Active buttons use primary blue with white text.

### Footer
**`footer`** — A pure black background section with muted gray (#444444) links and body text. Contains links to About, Contact, Shipping, Returns, and social media icons. Links hover to tangerine. The footer is the quietest part of the interface — no accent colors beyond hover states.

### Hero
**`hero-banner`** — A full-width section on pure black with large display text (36px, weight 800). Typically features a single VHS sleeve or promotional image as the background, with the brand's value proposition overlaid in white. The hero uses `{spacing.section}` (64px) for top and bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero text reduces to 24px; search bar moves below hero; filter tags stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but reduced to 5 items; hero maintains 28px text; search bar remains full-width |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 36px; filter tags in horizontal strip |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero text scales to 40px; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Filter tags are 32px minimum height with 12px horizontal padding
- Nav links have 48px tap targets (padding extends beyond text)
- Pagination buttons are 36px × 36px minimum

### Collapsing Strategy
- Navigation collapses to a hamburger icon below 744px; the menu slides in from the left on activation
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport narrows
- Filter tags collapse from a horizontal scrollable strip to a vertical accordion below 744px
- Hero banner reduces padding from 64px to 32px on mobile
- Search bar moves from inline to below the hero on mobile
- Footer links collapse from a multi-column layout to a single column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font-family declarations were found on the live site; the system relies on the default system sans-serif stack. A custom VHS-inspired typeface may exist but was not detected.
- Hover and focus states for most components (beyond buttons) could not be reliably extracted from the live site. The system assumes a simple color shift to `{colors.primary-active}` for interactive elements.
- Error, success, and warning form states are inferred from common Shopify patterns (#eb001b for error, #34a853 for success, #fbbc04 for warning) but were not confirmed on the live site.
- Dark mode is not applicable — the brand already uses a black canvas as its default.
- The extracted color list includes several checkout-widget colors (Shopify Pay, Klarna, Afterpay) and social-icon colors that are not part of the brand's design system. The true brand palette was distilled to the most distinctive and frequently occurring colors: #006fcf (primary blue), #f48120 (tangerine), #ffd800 (yellow), #cc0066 (magenta), and the various dark neutrals.
- No animation or transition timing values were extracted. The system assumes 200ms ease-in-out for hover transitions.
- Dropdown menus, mega-menus, and mobile navigation patterns were not observed on the live site and are not documented.
- The star-rating component color (#fba900) is inferred from the extracted palette but its exact usage context was not confirmed.
