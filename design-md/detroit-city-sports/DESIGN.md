---
version: alpha
name: "Detroit City Sports"
source_url: "https://www.detroitcitysports.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A saturated #003399 navy — closer to a championship-ring sapphire than a corporate blue — stakes the entire visual identity against the graduated grays and off-whites that form the rest of the palette. Detroit City Sports deals in authenticated signatures and certified memorabilia, and that cobalt acts as a trust signal: the official color of the city's teams rendered in digital form, standing in for the Red Wings, the Pistons, the Tigers, and the Lions all at once. Against it, #ff0000 red fires as a second accent — used sparingly for sale pricing, alert states, and the occasional clearance badge — keeping the palette within the narrow chromatic range of actual Detroit jersey colors rather than straying into invented territory.

  Type is set in Open Sans and Arial, both system-level stalwarts that prioritize legibility over personality. When selling a framed Wayne Gretzky signature or a Bob Gibson baseball, the photography and the certificate of authenticity do the selling; typography just needs to stay out of the way. Headlines run at weight 700 to add structure, while body copy lives at 400 on mid-gray (#444444) ink to reduce eye strain across long browse sessions.

  The catalog grid organizes into rows and cards against a near-white canvas (#f7f7f7), separated by hairline borders at #dcdbdb. Cards carry small team-color badges that identify sport and franchise at a glance. Search and category filtering sit prominent — this is a catalog-first experience where fans know exactly what they are hunting for. Corners throughout are gently squared ({rounded.xs} to {rounded.sm}), feeling like a well-organized sports shop rather than a lifestyle boutique. The footer drops to a dark #313131 canvas providing a clear visual terminus that reinforces the navy-anchored frame. The muted grays — #606263, #777777, #919394 — form a graduated ink stack that makes metadata and pricing hierarchy read cleanly without additional typographic tricks.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99b3dd"
  accent-red: "#ff0000"
  accent-red-dark: "#cc0000"
  ink: "#313131"
  body: "#444444"
  muted: "#777777"
  muted-mid: "#606263"
  muted-soft: "#919394"
  muted-lighter: "#b8b8b8"
  hairline: "#dcdbdb"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#efefef"
  surface-input: "#f2f4f7"
  surface-mid: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  footer-canvas: "#313131"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
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
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    width: 100%
  text-input:
    backgroundColor: "{colors.surface-input}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: 0 24px
  nav-bar-top-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 32px
    padding: 0 24px
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 12px
    imageAspectRatio: 1/1
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,51,153,0.12)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: 64px 32px
    minHeight: 360px
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-sub:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
    opacity: 0.9
  autograph-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  autograph-badge-certified:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  team-filter-tag:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.body}"
    typography: "{typography.caption-strong}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  team-filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 42px
    padding: 0 16px
  search-bar-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    width: 44px
    height: 42px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-lighter}"
  breadcrumb-active:
    typography: "{typography.caption-strong}"
    textColor: "{colors.ink}"
  price-regular:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  price-sale:
    typography: "{typography.price-display}"
    textColor: "{colors.accent-red}"
  price-original-struck:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  category-sidebar-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: 6px 0
    borderBottom: "1px solid {colors.hairline-soft}"
  category-sidebar-link-active:
    typography: "{typography.body-sm}"
    textColor: "{colors.primary}"
    fontWeight: 700
  footer:
    backgroundColor: "{colors.footer-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.md}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-lighter}"

## Components

### Buttons
**`button-primary`** — Solid #003399 navy fill with white text, uppercase Open Sans at 700 weight with 0.5px letter-spacing, and a tight {rounded.xs} (4px) corner that reads as squared-off without going razor-sharp. Fixed at 44px height with 12px/24px vertical-horizontal padding. Hover deepens to `{colors.primary-active}` (#002277); disabled fades the fill to the desaturated `{colors.primary-disabled}` while keeping white text — no cursor changes needed beyond the standard disabled treatment.

**`button-secondary`** — White canvas fill with a 2px #003399 navy border and matching navy text, same uppercase button-md typography and {rounded.xs} corner. On hover the canvas shifts to `{colors.surface-soft}` and both border and text tighten to the active navy. Communicates a secondary action without the visual weight of the filled primary — used primarily alongside add-to-cart for "View Details" or "Add to Wishlist."

**`button-add-to-cart`** — Full-width variant of button-primary at 48px height and 14px/28px padding, occupying the full horizontal span of the product detail CTA zone. The wider padding and extra height give the primary purchase action additional visual mass without changing the color or typographic language.

### Text Input & Search
**`text-input`** — Light `{colors.surface-input}` (#f2f4f7) background with a 1px `{colors.hairline}` border and {rounded.xs} corners, body-md Open Sans at 15px. On focus the border lifts to 2px `{colors.primary}` navy and the background shifts to white canvas — the navy focus ring unifies form fields visually with the button system.

**`search-bar`** — Inline search field with white canvas background and a hairline-soft border. The submit button is a solid `{colors.primary}` navy square attached flush right ({rounded.none}), making the search action visually inseparable from the input. Placeholder text sits in `{colors.muted}` (#777777). This paired input-plus-submit pattern is the site's primary discovery tool and should remain visible in every header state.

### Navigation
**`nav-bar`** — Full-width #003399 navy bar at 56px height carrying white nav links in 600-weight Open Sans at 14px. A slimmer 32px dark strip (`{colors.ink}` #313131) sits above it for persistent shipping notice or promotional copy. This double-tier header structure keeps trust signals ("Free Shipping Over $X," "COA Included") visible alongside primary navigation without collapsing them into the same visual band.

### Product Cards
**`product-card`** — White canvas cards with a 1px `{colors.hairline}` border, {rounded.sm} (8px) corners, and 12px padding. Product photography fills a square 1:1 aspect ratio image area at the top. Title renders in `{typography.title-md}` (16px/600) in `{colors.ink}`, price in `{typography.price-display}` (18px/700) in navy primary. On hover the border lifts to navy and a faint navy box-shadow (`rgba(0,51,153,0.12)`) adds mild elevation without heavy animation. Badge chips overlay the image top-left corner for autograph or sale status.

### Badges
**`autograph-badge`** — Small rectangular tag in `{colors.primary}` navy with `{typography.badge-label}` (11px/700/uppercase/0.5px tracking) and {rounded.xs} corners, 2px/6px padding. Marks items as hand-signed. The certified variant (`autograph-badge-certified`) swaps the fill to `{colors.accent-red}` (#ff0000) for COA-included or third-party authentication-verified pieces, pulling Detroit sports red onto the product card surface as a premium signal rather than a generic danger color.

**`sale-badge`** — Identical structure to autograph-badge-certified in `{colors.accent-red}`, positioned top-left over the product image. Red is used exclusively for urgency and discount signals across the site, keeping it semantically distinct from the navy primary action language.

### Filters
**`team-filter-tag`** — Pill-shaped ({rounded.full}) filter chips with a `{colors.surface-mid}` (#eeeeee) background and `{colors.hairline}` border, caption-strong type in body gray. The active state fills solid `{colors.primary}` navy with white text — the same visual grammar as the nav bar, unifying the filtering system with the overall brand color logic. Tags scroll horizontally on narrow viewports rather than wrapping to a second row.

### Hero Banner
**`hero-banner`** — Full-bleed #003399 navy section at 360px minimum height, 64px vertical padding. The `hero-headline` runs display-xl (36px/700/white), subtext in body-md at 90% opacity white. The solid navy fill reinforces brand identity at page entry without depending on lifestyle photography, though team imagery can overlay as a right-aligned or bleeding graphic element.

### Pricing
**`price-regular`** — 18px/700 in `{colors.primary}` navy, reading price as a positive brand-colored value. Sale items display `price-sale` in `{colors.accent-red}` alongside the original price in `price-original-struck` (13px/400/`{colors.muted}`/line-through), making discount states immediately legible without additional labels.

### Footer
**`footer`** — Dark #313131 canvas with white body text and `{colors.muted-lighter}` (#b8b8b8) link text at 48px vertical padding. Footer headings render in title-sm (14px/600/white). The shift from navy header to dark gray footer bookends the content area with two authority-coded dark surfaces, creating a clear visual frame around the product canvas.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger menu collapses all nav links behind an overlay; search bar fills full width below the nav; hero drops to 280px height; team filter tags scroll horizontally in a single strip |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline, secondary links in dropdown; sidebar filters collapse into a top horizontal filter row |
| Desktop | 1128–1440px | Three- to four-column product grid; left sidebar for category and team filters exposed; hero at full 360px; full nav link set visible; promotional top strip present |
| Wide | > 1440px | Content maxes at ~1400px centered; side gutters increase proportionally; grid stays at four columns |

### Touch Targets
- All nav links minimum 44×44px tap area via padding compensation
- Filter tag pills minimum 36px height with at least 12px horizontal padding
- Add-to-cart button full-width on mobile at 48px height for thumb reach
- Search submit button 44px wide × 42px tall, flush to input field

### Collapsing Strategy
- Left-rail category/team filter sidebar collapses into a horizontally scrolling pill strip pinned below the nav bar on tablet and below
- The top promotional strip (#313131) collapses to a single-line scrolling marquee on mobile to preserve vertical space
- Product card titles truncate at two lines on mobile; full title visible on hover/focus on desktop
- Hero headline drops from display-xl (36px) to display-sm (20px) on mobile; hero subtext hidden to reduce vertical footprint
- Footer columns stack single-column on mobile with a top border separating each column group

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; site uses web-safe stack (Open Sans, Arial, Helvetica). Custom font loading behind JS rendering cannot be ruled out.
- Meta theme-color not set; #003399 inferred as de-facto brand primary from nav color dominance.
- Exact button and input border-radius values are estimated — no CSS custom properties or design tokens were directly extracted.
- Per-team badge color logic (Red Wings red vs. Pistons blue vs. Tigers navy vs. Lions Honolulu blue) for franchise-specific card variants is not captured; the two-color default (navy + red) covers the general case.
- FontAwesome version and specific icon set in use (icon sizing, weight, usage mapping) not documented.
- Cart, wishlist, and account icon styles within the nav bar not confirmed from extraction.
- Sale badge exact position relative to product image (top-left corner vs. bottom overlay) not confirmed.
- Hover animation timing and easing on product cards not extractable from static color data.
