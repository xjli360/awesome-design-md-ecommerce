---
version: alpha
name: "Farer"
source_url: "https://farer.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The dial of a Farer Lander arrives in a color that has no easy name — somewhere between teal and peacock, lacquered and slightly pearlescent — and the website that sells it is nearly its photographic negative: deep midnight navy (#021a30) against pale gray (#f4f4f4) surfaces, every bright note deferred to the product photography. This deliberate restraint is the central design argument: the UI recedes entirely so the watches can perform. FoundersGrotesk carries all text — a geometric grotesque with squared-off terminals that leans on British modernism without borrowing from Swiss tradition — set at modest weights and generous tracking to keep pages airy even when stacked with movement specifications and reference codes. Primary actions are rectangular buttons in #021a30 at zero border radius: a deliberate sharpness that rhymes with the machined edges of the cases themselves. The palette is intentionally narrow; two near-whites (#f4f4f4, #f1f1f1) alternate as canvas and surface-card while a third near-white (#f3f3f3) handles mid-surface states, slate-gray (#374757) covers secondary text and UI chrome, near-black (#121212) anchors headline ink, and hairlines in #dedede quietly rule the grid without announcing themselves. No decorative accent escapes from the product world into the interface: all chromatic energy lives inside the watch photographs, never in the surrounding chrome. Product cards center the dial image against a neutral field with minimal metadata below — reference code, collection name, and price stacked in compressed FoundersGrotesk that trusts the photograph to close the sale. Navigation runs flat and plain-spoken: a horizontal list of collection names in spaced uppercase at 14px, no drop-shadows, no animated reveals. The footer deepens back to #021a30, reversing the canvas-and-navy logic so the page begins and ends in the same midnight ink. The total effect is less a luxury-goods convention than a high-end catalog from a small British workshop: cool, controlled, and confident that the dials themselves are the only color the page needs.

colors:
  primary: "#021a30"
  primary-active: "#011220"
  primary-disabled: "#7a9bb5"
  ink: "#121212"
  body: "#383838"
  muted: "#374757"
  hairline: "#dedede"
  hairline-soft: "#dfdfdf"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#f1f1f1"
  surface-mid: "#f3f3f3"
  on-primary: "#ffffff"
  footer-bg: "#021a30"
  footer-text: "#f4f4f4"

typography:
  display-xl:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 52px
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  collection-label:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  price:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'FoundersGrotesk', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    paddingX: "{spacing.xl}"
  collection-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} 0"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  product-card-collection:
    typography: "{typography.collection-label}"
    textColor: "{colors.muted}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 600px
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subtext:
    typography: "{typography.body-md}"
    textColor: "{colors.footer-text}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  collection-badge:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.muted}"
    typography: "{typography.collection-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  watch-detail-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  watch-detail-reference:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.footer-text}"
    borderTop: none
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Full-width or fixed-width at 48px tall, zero border radius, midnight navy (#021a30) fill with white uppercase FoundersGrotesk at 13px/1.5px tracking. Hover darkens to #011220; disabled state washes to the slate-blue #7a9bb5. The absence of rounded corners is a brand signature — every button reads as a machined component, not a soft consumer UI element.

**`button-secondary`** — Transparent fill with a 1px #021a30 border and navy uppercase label. Used for secondary actions on light-canvas pages (e.g., "View Collection" alongside a primary "Add to Cart"). Matches primary height and tracking exactly so the two can sit side by side without visual weight imbalance.

**`button-ghost`** — Text-only, no border, no background. Used sparingly for tertiary actions like "Learn More" in editorial sections. Same uppercase button-md type treatment keeps hierarchy readable even without a container.

### Navigation

**`nav-bar`** — White canvas at 64px tall, hairline bottom border. Logo sits left in #021a30; collection links run center or right in 13px spaced uppercase FoundersGrotesk. Cart and account icons anchor far right. On scroll, the bar remains fixed with the same white background — no color transition to dark. No mega-menu panels; collections expand into a simple dropdown list.

**`collection-tab`** — Flat horizontal tabs below the nav for sub-collection filtering (e.g., Lander, Stanhope, Cobb, Aqua). Inactive tabs are muted slate; the active tab carries a 2px #021a30 underline only — no pill, no fill, no rounded treatment.

### Product Cards

**`product-card`** — Square neutral-gray (#f4f4f4) container with zero radius. The watch dial image occupies the full card width at 1:1 aspect ratio, shot against a white or near-white field so the colored dial floats cleanly. Below the image: collection label in 11px spaced caps (muted), model name in title-sm, and price in body-weight 16px. No star ratings, no "new" badge overlays — the card is entirely image-led.

### Hero

**`hero-banner`** — Full-bleed midnight navy (#021a30) panel, minimum 600px tall. Headline in display-xl FoundersGrotesk at white; sub-copy in footer-text (#f4f4f4) at body-md. A single button-primary sits below. Photography is often placed right-aligned or as a full bleed background at reduced opacity. No carousel — Farer heroes are single, still, and editorial.

### Product Detail

**`watch-detail-title`** — Model name in display-md FoundersGrotesk at 36px/500 weight. Reference number sits immediately above in caption type at muted slate, tracked at ~1.5px — the reference number functions as an eyebrow label. The two together form the only "header" for the detail page; there is no decorative divider or badge.

**`spec-table`** — Two-column row list on a #f4f4f4 surface, hairline dividers between rows, zero border radius on the container. Left column in spec-label type at muted color (case material, movement, water resistance, lug width); right column in body-sm at ink. Padding is 8px top/bottom, 16px left/right per row.

### Announcement Bar

**`announcement-bar`** — Slim 36px bar pinned above the nav in #021a30 with white caption text, centered. Typically carries free shipping thresholds or new-collection announcements. No close button visible in the main UI pass — it remains persistent on load.

### Footer

**`footer`** — Full midnight navy (#021a30) reversal of the page canvas. All text in #f4f4f4 at body-sm weight. Links match body-sm color with underline on hover only. Column grid: Brand, Collections, Support, Legal. The footer logo marks the brand's endpoint in white on navy — the same ink tone as the top of the page, forming a deliberate frame.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with slide-out drawer; hero text scales to display-sm; spec table stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links may compress or move to drawer; hero retains two-column text/image split |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all collection links visible; hero at full 600px height |
| Wide | > 1440px | Grid max-width capped (~1400px) with auto side margins; font sizes hold — no further scaling above desktop |

### Touch Targets

- All buttons minimum 48px tall; ghost buttons padded to 44px touch zone
- Navigation items in mobile drawer minimum 48px row height
- Product card tap target is the full card surface including image
- Cart icon and hamburger icon minimum 44×44px tap area

### Collapsing Strategy

- Nav collapses collection tabs into a hamburger drawer on mobile; announcement bar remains visible
- Spec table switches from two-column inline to stacked label-above-value layout below 744px
- Product grid goes 1-up on mobile, 2-up on tablet, 3-up on desktop, optionally 4-up wide
- Hero image drops below text stack on mobile; navy background extends to fill

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No accent or highlight color extracted — Farer's famously colorful watch dials do not appear to produce a recurring UI accent; the site may use dial imagery as the sole chromatic element
- Pure white (#ffffff) likely used as base canvas but was filtered as a framework default; confirmed only indirectly through surface hierarchy
- Hover and focus state transitions (duration, easing) not extractable from static color scan
- Mobile nav drawer background color not confirmed — assumed to match #021a30 primary but not extracted
- No secondary typeface or serif variant detected; FoundersGrotesk appears to carry all type roles without a contrast face
- Icon set style (stroke weight, filled vs. outlined) not determined from extraction
- Cart, wishlist, and account icon designs not captured
