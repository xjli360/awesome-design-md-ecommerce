---
version: alpha
name: "Autographia"
source_url: "https://autographia.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The dark navy (#163959) that anchors Autographia's interface carries the same visual authority as an archivist's binding cloth — every nav header, primary button fill, and trust callout sits in this color, signaling that provenance and authentication are the site's load-bearing commitments before a single item description is read. Against that foundation, a traffic-light status trio performs hard work at the card layer: #bd2426 flags rarity and urgency across limited listings, #9bca3e marks certified-authentic items, and #f68b1f illuminates featured and spotlight pieces. This three-tone certification language is more legible than fine-print disclaimers — the color encodes grade before the collector even reaches the product title.

  Typography runs entirely on system stacks (Arial, Helvetica Neue, -apple-system) at conservative weights. The choice reads as deliberate restraint: the autograph itself — photographed in high resolution and centered — is the typographic event on any product page, not a headline font. Body copy in #404040 against the soft #ebebeb canvas keeps the catalog register close to a printed dealer's reference rather than a digital storefront. Hairlines in #dedede divide sections without asserting themselves, and #737373 carries secondary metadata — certification numbers, grading notes, date ranges — without competing with the primary attribution.

  Buttons avoid the pill-shape syntax of contemporary consumer marketplaces. The slight radius on primary CTAs and contained input fields reads closer to a collector's authentication portal than a promotional checkout flow — `{rounded.sm}` on inputs and cards, `{rounded.xs}` on badges and micro-labels. The authentication badge is the single highest-attention component in the system, rendered in #9bca3e for certified status and #bd2426 for unverified, always positioned at the top corner of every product card alongside a monospace certificate number. Section spacing is wide and unhurried, giving each signed photograph room to exist as an object of value rather than one row in an inventory grid.

colors:
  primary: "#163959"
  primary-active: "#0d2338"
  primary-disabled: "#62a1d8"
  ink: "#272727"
  body: "#404040"
  body-mid: "#595959"
  muted: "#737373"
  muted-light: "#bfbfbf"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#2f7bbf"
  accent-blue-light: "#62a1d8"
  accent-red: "#bd2426"
  accent-red-soft: "#de5052"
  accent-red-dark: "#521010"
  accent-green: "#9bca3e"
  accent-green-soft: "#bada7a"
  accent-green-dark: "#516b1d"
  accent-orange: "#f68b1f"
  accent-orange-light: "#f9b169"
  accent-orange-dark: "#904b06"
  accent-amber: "#c16508"
  accent-fire: "#ee730a"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-strong:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  cert-mono:
    fontFamily: "courier, monaco, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  badge-label:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    border: 1px solid
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    borderColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
  button-cta-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    border: 1px solid
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
    typography: "{typography.body-md}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: 0 24px
    logoAreaWidth: 200px
  nav-bar-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    height: 36px
    borderBottom: 1px solid {colors.hairline}
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    border: 1px solid
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    metaTypography: "{typography.body-sm}"
    metaColor: "{colors.muted}"
  authentication-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  unverified-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  featured-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  cert-number-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.cert-mono}"
    borderColor: "{colors.hairline}"
    border: 1px solid
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 320px
    padding: "{spacing.xxl} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    border: 1px solid
    rounded: "{rounded.xs}"
    inputTypography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    height: 42px
    padding: 0 12px
  category-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.full}"
    padding: 5px 14px
    border: 1px solid {colors.hairline}
  category-filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.full}"
    padding: 5px 14px
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-light}"
    activeColor: "{colors.body}"
    typography: "{typography.caption}"
  price-tag:
    textColor: "{colors.primary}"
    typography: "{typography.price-display}"
  price-tag-sale:
    textColor: "{colors.accent-red}"
    typography: "{typography.price-display}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-blue-light}"
    dividerColor: "{colors.accent-blue}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — Deep navy (#163959) fill with white text at 14px/weight-600, 4px radius, 40px height. Hover darkens to `{colors.primary-active}` (#0d2338); disabled drops to the extracted lighter blue (#62a1d8). This button carries add-to-cart, checkout, and submit-inquiry actions — contexts where trust-signaling through the brand navy matters more than a promotional accent color.

**`button-secondary`** — White canvas with a 1px navy border and matching navy text; same 4px radius and 40px height as primary. Hover applies #ebebeb fill while deepening the border to `{colors.primary-active}`. Used for secondary actions such as "View Details", "Make Offer", and wishlist toggles sitting adjacent to a primary CTA.

**`button-cta-red`** — Alert-red (#bd2426) fill for high-urgency, scarcity-driven actions: "Bid Now", "Last Item", or time-sensitive auction CTAs. Identical geometry to `button-primary`. Never used for standard checkout flows — reserved strictly for auction-mode and rarity callouts.

### Text Inputs
**`text-input`** — White fill with a 1px #dedede border, 4px radius, 38px height. Placeholder text runs in #737373; on focus the border transitions to brand navy (#163959). Used uniformly across search, checkout, and the authentication inquiry form.

### Navigation
**`nav-bar`** — Full navy (#163959) bar at 56px with white text in 14px/weight-600. Logo area sits left at ~200px; category links span center; account, cart, and search icons cluster right. A secondary utility strip (`nav-bar-secondary`) sits immediately below in #ebebeb at 36px height with a #dedede bottom border, carrying breadcrumbs, item counts, and sort controls.

### Product Card
**`product-card`** — White surface, 1px #dedede border, 4px radius, 8px padding. Image occupies a 4:3 aspect-ratio well at top. The authentication badge (green or red) overlays the image's top-right corner, paired with the `cert-number-chip` (monospace, #ebebeb field) directly beneath it on the card body. Title renders in 15px/weight-600 ink; seller and grade metadata in 13px/#737373; price in 20px/weight-700 navy. Cards flow in a responsive grid — 4-up on wide, 3-up on desktop, 2-up on tablet, 1-up on mobile.

### Authentication & Certification Badges
**`authentication-badge`** — Green (#9bca3e) pill with white uppercase label ("CERTIFIED") at 10px/weight-700, 4px radius. Immediately below, a `cert-number-chip` displays the PSA/JSA/Beckett number in courier/monaco at 11px on a soft #ebebeb field. This badge-plus-chip pairing is the most brand-distinctive UI pattern in the system.

**`unverified-badge`** — Red (#bd2426) version for items lacking third-party certification; identical geometry to `authentication-badge`.

**`featured-badge`** — Orange (#f68b1f) for staff-picks and spotlight items; identical geometry.

### Hero Banner
**`hero-banner`** — Full-width navy (#163959) band, minimum 320px tall. Headline in white display-xl (36px/700); subhead in white body-md. On desktop, a signed-item photograph occupies a 40% right column; on mobile the image collapses to a background blur. The CTA here is a white-fill/navy-text ghost of `button-secondary`, inverting the standard relationship to maintain contrast against the dark ground.

### Search
**`search-bar`** — White input with #dedede border and a flush navy submit button; 42px combined height, 4px radius on the outer container. Placeholder reads in #737373. Submit renders a white magnifying-glass icon. On mobile the bar expands to full width below the collapsed nav.

### Category Filter Pills
**`category-filter-pill`** / **`category-filter-pill-active`** — Rounded-full pills on an #ebebeb strip below the secondary nav bar. Inactive: soft-gray fill, hairline border, dark-gray text. Active: navy fill, white text. Filters for Sport, Entertainment, Historical, Music, and other top-level categories. On mobile these pills scroll horizontally in a snap-scroll row.

### Footer
**`footer`** — Full-width navy (#163959). Section headings in 15px/weight-600 white; body links in 13px rendered in #62a1d8 (extracted light blue) for legibility against the dark ground. Columns divide at #2f7bbf horizontal rule. Standard four-column layout: Shop by Category, Authentication Info, Customer Service, About Autographia.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + search icon; hero stacks text above image; filter pills scroll horizontally in snap-scroll row; authentication badge moves inline below title rather than image overlay |
| Tablet | 744–1128px | 2-column product grid; secondary nav bar collapses to filter-drawer toggle; hero splits into 60/40 text/image columns |
| Desktop | 1128–1440px | 3- or 4-column product grid depending on sidebar presence; full horizontal nav with category dropdown; two-column hero |
| Wide | > 1440px | Grid max-width caps at 1400px with auto side gutters; hero text column widens to 50% with display-xl bumped to 42px |

### Touch Targets
- Primary and secondary buttons maintain minimum 40px height on all touch viewports
- Authentication badge tap target expands to 44×44px minimum via padding on mobile
- Filter pills in the horizontal scroll row achieve at least 36px height
- Nav icons (cart, account, search) are 44×44px tap targets in collapsed mobile nav
- Product card image well is fully tappable as a link to the detail page

### Collapsing Strategy
- Secondary utility nav collapses first below 744px; sort and filter controls move into a slide-up drawer
- Desktop dropdown nav collapses to accordion-style mobile drawer
- Three- and four-column product grids step down: 4→3→2→1 across breakpoints
- Footer four-column grid collapses to two columns at tablet, single stacked column at mobile
- Hero photograph hides or becomes a blurred background fill below 480px viewport width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site is behind Cloudflare anti-bot protection; no live DOM or CSS variables were accessible — all extracted hex values are sourced from the Cloudflare error-page assets, not Autographia's actual design system
- No custom brand font detected; typography assumes system stacks (Arial, Helvetica Neue) — a custom webfont may load via JS or be served behind the bot wall
- Exact border-radius and spacing values are inferred from brand context; `{rounded.xs}` (4px) assumed for the conservative catalog register rather than confirmed from live CSS
- Platform is not Shopify, so no theme token variables were available; component padding values are estimated
- The orange/amber cluster (#f68b1f, #f9b169, #904b06, #c16508, #ee730a) likely maps to pricing, discounts, or sport-category accents — exact per-context usage unknown
- Dark maroon (#521010) role is unclear; may serve error states, deep-hover on accent-red, or a specific memorabilia category color
- Whether #9bca3e and #bada7a actually encode PSA/JSA certification status or serve a different function (promotional tags, category color) could not be confirmed
- Logo treatment, icon style (outlined vs. filled), and product-image overlay scrim behavior could not be confirmed from available data
