---
version: alpha
name: "Frame It All"
source_url: "https://frameitall.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Two lime-greens so close in hue they're nearly twins — #8fc746 and #8dc744 — sit at the top of Frame It All's extracted palette, yet neither is the true brand anchor. That role belongs to #024520, a near-black forest green that covers the header, primary CTAs, and logo lockup. The arrangement reads like a canopy: deep shade at the structure, then a band of bright mid-leaf for interactive states, then warm cedar brown (#4f3b2a) grounding the whole system in the material of the actual product. The palette earns credibility by mirroring what customers are building with.

  Typography pairs Bricolage Grotesque SemiBold — a geometric grotesque with slightly mechanical proportions — for all display and headline work, while Alegreya Sans gives body copy an almanac-like warmth that suits a brand writing long-form guides on soil depth and drainage layers. Poppins handles buttons, labels, and nav items; its uniformly circular letterforms keep UI chrome legible at small sizes without competing with the editorial stack. The 10px border radius extracted from the live site is why {rounded.md} sits at 10px throughout — product cards, inputs, and CTAs all share this number, creating structural consistency across a Shopify catalog that can run dozens of SKUs deep.

  The surprise in the palette is #dd4de6, a vivid purple-magenta that would be garish in most garden brand contexts. Here it functions as a deliberate alarm: promotional banners, sale badges, and newsletter overlays pulse in this color — short-duration, high-contrast events that must be impossible to miss against surrounding greens. It operates exactly the way an unexpected wildflower operates in a raised bed: disruptive by design, then gone.

  A light teal, #aadddd, appears in callout sections and testimonial blocks. It reads like galvanized steel — the material of greenhouse panel frames and corner connectors — making it a material callback rather than a purely decorative surface. The near-black #121212 carries all body copy rather than pure black, and #e7eedd, a barely-green off-white, provides surface-soft backdrops for sidebar filters and informational callouts. At generous column widths and {rounded.md} corners throughout, Frame It All reads as a brand that expects customers to read, measure, and plan before they purchase.

colors:
  primary: "#024520"
  primary-active: "#12703c"
  primary-disabled: "#e7eedd"
  accent-lime: "#8fc746"
  accent-lime-active: "#7ab635"
  accent-promo: "#dd4de6"
  earth: "#4f3b2a"
  dark-forest: "#182400"
  ink: "#121212"
  body: "#121212"
  muted: "#989898"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#e7eedd"
  surface-teal: "#aadddd"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent-lime: "#182400"
  on-promo: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Bricolage Grotesque', 'BricolageGrotesque-SemiBold', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Alegreya Sans', 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Alegreya Sans', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px

rounded:
  none: 0px
  xs: 3px
  sm: 6px
  md: 10px
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
    rounded: "{rounded.md}"
    padding: "12px 24px"
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
  button-accent:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-accent-lime}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "12px 24px"
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-lime-active}"
    textColor: "{colors.on-accent-lime}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "10px 22px"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: "10px 14px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    metaTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "16px"
  hero:
    backgroundColor: "{colors.dark-forest}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 520px
  promo-badge:
    backgroundColor: "{colors.accent-promo}"
    textColor: "{colors.on-promo}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-accent-lime}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "3px 8px"
  bestseller-badge:
    backgroundColor: "{colors.earth}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "3px 8px"
  promo-banner:
    backgroundColor: "{colors.accent-promo}"
    textColor: "{colors.on-promo}"
    typography: "{typography.caption}"
    padding: "10px 24px"
    textAlign: center
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    titleTypography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "20px 16px"
  callout-teal:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.dark-forest}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "24px 32px"
  footer:
    backgroundColor: "{colors.dark-forest}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"

## Components

### Buttons

**`button-primary`** — Forest-green #024520 background at 48px height with Poppins SemiBold at 15px and {rounded.md} corners. Hover transitions to primary-active (#12703c); disabled state drains to the {colors.primary-disabled} near-white with muted gray text. Used for primary navigation CTAs like "Shop Now" and "View All Products."

**`button-accent`** — The "Add to Cart" button and inline product-page CTA. Lime #8fc746 background with dark-forest #182400 text provides strong contrast without repeating the header green. Active state steps down to #7ab635. The lime read on product pages registers as energetic and harvest-adjacent, which suits the brand context.

**`button-secondary`** — White canvas with a 2px primary-green border, matching height and radius as button-primary. Used for "Learn More," "Compare," and secondary navigation CTAs that should not compete with the primary or accent actions.

### Product Card

**`product-card`** — White surface-card with {rounded.md} corners and a 1px hairline border. The product title runs title-md in Bricolage Grotesque SemiBold; price uses price-display at 22px/700 weight in the same family. Supporting copy (dimensions, material notes) uses body-sm in Alegreya Sans. Badge overlays — promo-badge, new-badge, bestseller-badge — anchor to the top-left corner of the image container as absolute-positioned chips. Cards expand to equal height within grid rows.

### Navigation

**`nav-bar`** — Forest-green #024520 header at 64px height. Links render in Poppins 500 at 14px in on-primary white. The logo sits left-aligned; a cart icon and search trigger sit right. On mobile, a hamburger opens a full-screen drawer with back-navigation per category level.

### Badges

**`promo-badge`** — Purple #dd4de6 background with white all-caps Poppins 700 at 11px, applied exclusively to sale events and limited-time SKUs. Its hue is violent against every green surface on the page, which is the point: it must interrupt browsing attention.

**`new-badge`** — Lime #8fc746 background with dark-forest text. Signals recently added SKUs or seasonal catalog additions. Shares shape with promo-badge but reads as positive rather than urgent.

**`bestseller-badge`** — Cedar brown #4f3b2a background with white text, communicating social proof through a material-referencing color rather than an arbitrary accent.

### Hero

**`hero`** — Dark forest #182400 background at a minimum 520px height. The headline runs display-xl in Bricolage Grotesque 700 in on-primary white. Body copy uses body-md in Alegreya Sans. The CTA defaults to button-accent (lime) for maximum contrast on the dark ground. On desktop the image sits right of the text column; on mobile it stacks below with reduced height.

### Promotional Banner

**`promo-banner`** — A full-width purple strip using accent-promo (#dd4de6) above the nav-bar. Short Poppins caption text is centered in on-promo white. Reserved for sitewide sale events, free-shipping thresholds, and seasonal promotions; should not persist as a permanent fixture.

### Category Tiles

**`category-tile`** — Light green-cream surface-soft background with primary-green title text in title-sm Bricolage Grotesque. Used in homepage grid navigation for Raised Beds, Greenhouses, Accessories, and Bundle categories. {rounded.md} corners and a hairline border. Icon or thumbnail sits above the label.

### Callout Sections

**`callout-teal`** — The teal-gray #aadddd surface with {rounded.md} corners reads like galvanized steel in the context of greenhouse panels and metal corner connectors. Used for material guarantee blocks, warranty callouts, and testimonial highlights. Text runs in dark-forest (#182400) for strong contrast on the pale ground.

### Footer

**`footer`** — Dark forest #182400 background mirrors the hero, creating visual bookends on long pages. Section headings use title-sm in Bricolage Grotesque; link items use body-sm in Alegreya Sans at on-primary white. A four-column layout on desktop collapses to a single accordion-style list on mobile.

### Breadcrumb

**`breadcrumb`** — Muted gray (#989898) for ancestor segments, ink (#121212) for the active page segment, separated by a forward slash in caption Poppins 500. Appears below the nav-bar on category and product detail pages. No background — sits directly on the canvas.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav drawer, full-width hero image stacked below headline, stacked CTA buttons |
| Tablet | 744–1128px | Two-column product grid, compact horizontal nav with dropdown menus, hero retains side-by-side layout |
| Desktop | 1128–1440px | Three-column product grid, full horizontal nav with mega-menu flyouts, hero at full 520px+ height |
| Wide | > 1440px | Container max-width ~1440px centered, optional four-column grid for accessories and add-on SKUs |

### Touch Targets
- All buttons minimum 44×44px tap area including icon-only variants
- Nav links minimum 44px tap height inside the mobile drawer
- Product cards fully tappable from image to price row
- Badge chips link to filtered category views; minimum 32px height
- Breadcrumb segments minimum 36px tap height on mobile

### Collapsing Strategy
- Mega-menu collapses to full-screen side drawer with hierarchical back-navigation on mobile
- Hero image moves below headline text on mobile; min-height reduces to 320px
- Category tile grid goes 2-up on mobile, 3-up on tablet, 4-up on wide desktop
- Promo-banner text truncates at narrower widths rather than wrapping to two lines; no marquee scroll
- Footer four-column layout collapses to stacked accordion sections with expand/collapse per group

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No logo file or SVG extracted; exact wordmark weight, spacing, and any icon lockup variant are unconfirmed
- Button hover transition duration and easing curve not extractable; 150–200ms ease-in-out is a safe default
- Exact nav-bar height not measured from live DOM; 64px inferred from typical Shopify Dawn header patterns
- Bricolage Grotesque variable font axis range not confirmed; weight 600/700 assumed from the BricolageGrotesque-SemiBold font-family string in extraction
- No shadow or elevation tokens extracted; product card drop-shadow depth and modal overlay blur are unconfirmed
- Mobile breakpoints not directly observed; 744px and 1128px follow Shopify Dawn defaults and may differ
- #dd4de6 usage context unconfirmed; it may originate from a third-party loyalty or pop-up widget (e.g., Klaviyo, Smile.io) rather than core brand UI — verify before applying to owned components
- No icon set identified; outline vs. filled style and icon grid size (20px vs. 24px) unknown
- Alegreya Sans weight variants beyond 400 and 700 not confirmed as loaded; italic variant availability unknown
- No animation or micro-interaction specs extractable from static analysis
