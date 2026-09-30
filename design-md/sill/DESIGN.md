---
version: alpha
name: "The Sill"
source_url: "https://thesill.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep botanical green (#007b5f) anchors every interaction on thesill.com — add-to-cart buttons, sticky nav highlights, and loyalty badges all pulse with the same forest-floor hue, making the chrome feel like a living extension of the product photography. The page opens on a warm cream canvas (#fdf9f3) rather than clinical white, lending an earthy softness that keeps full-bleed plant imagery from feeling sterile. Display type is set in Domaine Display, a high-contrast modern serif whose thin hairlines and generous x-height evoke editorial botanicals more than garden-center signage; it pairs with Gill Sans for navigation and button labels, producing a serif/sans rhythm that separates content from commerce without friction. Card radii stay moderate (`{rounded.md}`) — friendly enough for a lifestyle brand, structured enough for a product grid that regularly holds 12+ SKUs. Near-black ink (#141414) sits atop the cream ground at a contrast ratio well above 7:1, and a second-tier dark (#2a2d2f) handles long-form care guides without the heaviness of pure black. The hairline system splits into two weights: #dedede for card borders and #e2e2e2 for dividers inside modals and drawers, giving layered surfaces subtle depth without extra shadow. A muted blue (#334fb4) appears sparingly — link underlines in care-tip articles and the occasional seasonal collection badge — providing a complementary cool note against the dominant green. Spacing follows a 4px grid with generous `{spacing.section}` gaps (64px) between homepage modules, letting each plant collection breathe as its own vignette. Product cards run full-bleed imagery with a `{spacing.sm}` gutter and overlay a translucent surface-soft (#f6f6f6) strip at the bottom for price and quick-add, ensuring imagery dominates the scroll.

colors:
  primary: "#007b5f"
  primary-active: "#006650"
  primary-disabled: "#99cfc2"
  ink: "#141414"
  ink-secondary: "#1c1c1c"
  body: "#2a2d2f"
  muted: "#545454"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#fdf9f3"
  canvas-cool: "#f9f8f7"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#334fb4"
  dark-ui: "#121212"
  scrim: "rgba(20, 20, 20, 0.45)"

typography:
  display-xl:
    fontFamily: "'Domaine Display', 'PT Serif', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Domaine Display', 'PT Serif', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Domaine Display', 'PT Serif', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Domaine Display', 'PT Serif', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Domine', 'PT Serif', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.4px
  button-lg:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  price:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Gill Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    opacity: 0.8
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 1px 3px rgba(20,20,20,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    overflow: hidden
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "4:5"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(20,20,20,0.08)"
    transform: "translateY(-2px)"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 520px
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.lg}"
    textAlign: center
  badge-bestseller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-easy-care:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"
  quick-add-overlay:
    backgroundColor: "rgba(255,255,255,0.95)"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
    position: "absolute bottom 0"
  plant-care-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  plant-care-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  pot-selector:
    width: 36px
    height: 36px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  pot-selector-active:
    width: 36px
    height: 36px
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  search-modal:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 32px rgba(20,20,20,0.12)"
  footer:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  subscription-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  subscription-card-selected:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "2px solid {colors.primary}"
  toast-notification:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"
---

## Components

### Buttons

**`button-primary`** — Full green (#007b5f) fill with white text, 8px radius, and 48px height. On hover, darkens to `primary-active` (#006650) with a subtle 120ms ease transition. Disabled state fades to a muted sage (#99cfc2) with reduced opacity. Used exclusively for add-to-cart, checkout progression, and subscription CTAs.

**`button-secondary`** — White fill with a 1px hairline border and dark ink text. On hover the border strengthens to ink-color and the background tints to surface-soft. Employed for "View all" links, filter toggles, and secondary actions alongside a primary CTA.

**`button-tertiary`** — Text-only with primary-green color and an underline. No background or border. Used for inline links within editorial content and "Learn more" affordances beneath product descriptions.

### Navigation

**`nav-bar`** — 64px-tall white bar with a subtle bottom hairline. Logo sits left; main links (Plants, Pots & Planters, Care, Gifts, Subscriptions) are centered in `nav-link` weight-500 Gill Sans. Cart icon and account avatar anchor right. On scroll past 80px, the bar gains a soft drop shadow and sticks to viewport top. Mobile collapses to a hamburger with a slide-in drawer from the left.

**`announcement-bar`** — 40px full-width strip above the nav in solid primary green with white centered caption text. Cycles through promotional messages (free shipping threshold, seasonal sales) with a crossfade every 5 seconds.

### Product Cards

**`product-card`** — 12px rounded container with a 4:5 aspect-ratio plant image filling the top. Below the image: plant name in `title-sm`, pot/size variant in `caption`, and price in `price` typography. Hover lifts the card 2px with a soft shadow and reveals a quick-add overlay at the image base. Badges (bestseller, new, easy-care) position absolute at the image's top-left corner with an 8px offset.

**`quick-add-overlay`** — Translucent white strip that slides up from the bottom of the product-card image on hover. Contains a single "Quick Add" button in `button-md` typography. On mobile, this overlay is replaced by a persistent "+" icon button in the card's bottom-right.

### Plant Care Chips

**`plant-care-chip`** — Pill-shaped filter tokens for light level (Low, Medium, Bright), pet-friendliness, and size. Cream background with a hairline border in resting state; active state fills with primary green and switches text to white. Used on collection pages and the plant quiz flow.

### Pot Selector

**`pot-selector`** — 36px circular swatches on the PDP showing available planter colors. Each swatch is filled with the pot's color and outlined with a 2px hairline border. Active selection switches the border to primary green. Swatches sit in a horizontal row with `spacing.sm` gaps.

### Subscription Card

**`subscription-card`** — Rounded card offering one-time vs. subscription purchase on the PDP. Unselected cards show a hairline border; the selected option gains a 2px primary-green border and a small green checkmark icon in the top-right corner. Interior shows frequency dropdown (Monthly, Bi-monthly) and savings percentage in green caption text.

### Hero Banner

**`hero-banner`** — Full-width section on the homepage with a large lifestyle photograph (plant in context) on one side and display-xl serif headline on the other. Minimum height of 520px. CTA button sits below the subtitle with `spacing.lg` top margin. On mobile the layout stacks image-above-text.

### Search Modal

**`search-modal`** — Centered overlay triggered by the nav search icon. 12px rounded white card with a prominent text input at top, recent searches below, and trending product thumbnails in a 2×2 grid. Background scrim at 45% opacity. Escape or clicking the scrim dismisses.

### Footer

**`footer`** — Dark (#121212) full-bleed section with four columns: Shop, Learn, Company, Support. Headings in `title-sm` white text, links in `body-sm` with muted opacity that brightens on hover. Bottom row contains social icons, copyright, and payment-method badges. Newsletter signup input with a green submit button sits in the rightmost column.

### Toast Notification

**`toast-notification`** — Dark rounded pill that slides up from the bottom-center after add-to-cart. Shows a checkmark icon, product name, and "View Cart" text link. Auto-dismisses after 4 seconds with a fade-out; can also be swiped away on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-up). Nav collapses to hamburger + cart icon. Hero stacks vertically. Footer accordion for link columns. Announcement bar text truncates to one line. |
| Tablet | 744–1128px | Product grid shifts to 3-up. Nav shows top-level links but mega-menu panels require tap. Hero uses 50/50 split. Pot selector scrolls horizontally if > 6 options. |
| Desktop | 1128–1440px | Full 4-up product grid. Mega-menu dropdowns on hover. Hero at natural 520px height. Sticky nav with shadow on scroll. Footer renders all four columns inline. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Product grid can stretch to 5-up on collection pages. Hero image scales proportionally, text size remains fixed. Side padding increases to 64px. |

### Touch Targets
- All tappable elements maintain a minimum 44×44px hit area on mobile, even if the visual element is smaller (e.g., pot-selector swatches use invisible padding).
- Care-chip filters stack into a horizontally-scrollable row with 8px gaps and 16px side padding on small screens.
- Quick-add on mobile uses a 40px circular "+" button rather than the full-width hover overlay.

### Collapsing Strategy
- Navigation mega-menu becomes a full-screen slide-in drawer on mobile with accordion sub-sections.
- Footer columns collapse into expandable accordions, each closed by default.
- PDP secondary info (shipping, returns, care guide) collapses into accordion panels below the main content on all breakpoints below desktop.
- Homepage collection carousels switch from a static grid to a swipeable horizontal scroll with peek (next card partially visible).

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font-weight values for Domaine Display could not be confirmed from extraction alone; 600/700 are inferred from visual hierarchy.
- Gill Sans may be served as a web-font variant (e.g., Gill Sans Nova) with different metrics; the fallback to Inter covers rendering consistency.
- Hover transition durations and easing curves (assumed 120–200ms ease) were not extractable from static analysis.
- The warm cream canvas (#fdf9f3) may be conditional — some interior pages could use pure white (#ffffff) as canvas; extraction only confirms homepage usage.
- Mega-menu panel structure, including column counts and featured-image placement, was not fully captured.
- Loyalty/rewards program badge colors and tier system were not visible in the extracted palette.
- The blue accent (#334fb4) usage context is limited — it may be reserved for specific seasonal or editorial contexts rather than a permanent system token.
