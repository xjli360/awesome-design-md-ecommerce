---
version: alpha
name: "Flamingo"
source_url: "https://www.shopflamingo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric violet (#6600ff) carries every primary action on the site — not as an accent or seasonal pop, but as the brand's permanent structural color, pressed against near-white lavender-tinted surfaces (#f7f7f8, #f4f4f6) for a high-contrast charge that women's body care rarely attempts at this saturation. The hue family stretches from a deep cosmic purple (#2b1453) in dark heroes and overlays, through the main CTA voltage at #6600ff, to a pressed-state at #5a00e0 and a soft lavender (#c299ff) for disabled states and decorative fills — a monochromatic spectrum that reads anything but single-note because each stop has a distinct functional role. Inter handles all typographic work: a neutral grotesque that does not compete with color, letting the violet and form language carry the character. Buttons reach for {rounded.full}, giving CTAs and pill-tag filters a smooth oval silhouette; product cards and inputs land at {rounded.sm} to stay grounded without going boxy. The supporting palette is deliberately cool — muted blue-grays (#676986, #9a9db1) carry secondary body copy, and near-white hairlines (#dbdde4, #e5e5eb) draw borders and dividers without introducing warmth that would flatten the violet's impact. Dark navy (#272d45) anchors footer hierarchies, giving the page definitive closure on long scroll. The meta theme-color (#c4cdd5), a fog-blue, surfaces only in browser chrome — it is not a brand application color. Flamingo's system makes one bet and follows it completely: violet is primary, and every surface decision exists to make that primary pop.

colors:
  primary: "#6600ff"
  primary-active: "#5a00e0"
  primary-disabled: "#c299ff"
  brand-deep: "#2b1453"
  brand-lavender: "#c299ff"
  ink: "#141414"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#f7f7f8"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  surface-strong: "#d3d4dd"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#141414"

typography:
  display-xl:
    fontFamily: "'Inter', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.96px
  display-lg:
    fontFamily: "'Inter', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.54px
  display-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.28px
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.12px
  label-uppercase:
    fontFamily: "'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.55px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.22px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1.5px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageBorderRadius: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    padding: "{spacing.base}"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
    activeBorder: none
  badge-promo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  hero-section:
    backgroundColor: "{colors.brand-deep}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaVariant: button-primary
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xl}"
  review-widget:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    ratingColor: "{colors.primary}"
    reviewerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  section-label:
    textColor: "{colors.primary}"
    typography: "{typography.label-uppercase}"
    marginBottom: "{spacing.sm}"

## Components

### Buttons

**`button-primary`** — Full-pill shape ({rounded.full}, 48px tall) in electric violet (#6600ff) with white Inter 600 text. On press, the fill shifts immediately to #5a00e0 with no delay — the feedback is instant and decisive. Disabled state uses soft lavender (#c299ff), keeping the violet hue family intact rather than falling back to generic gray. On desktop hover, brightness drops ~8% without introducing border or shadow changes.

**`button-secondary`** — White canvas background ({colors.surface-card}) with a 1.5px #6600ff border and matching violet text. Shares the {rounded.full} radius with button-primary so the two pair cleanly side-by-side in a CTA row. On hover, background tints to {colors.surface-soft}; the border remains violet. Used for secondary actions like "Compare" or "Learn more."

**`button-ghost`** — Transparent background, 1.5px {colors.hairline} border, {colors.ink} text. Used for neutral or reversible actions (dismiss, skip, cancel). Maintains the {rounded.full} pill family for visual consistency; no fill on hover — only a hairline darkening.

### Text Input

**`text-input`** — White background, 1px {colors.hairline} border, {rounded.sm} corners, 48px height aligned to button touch targets. Focus state upgrades border to 1.5px #6600ff, mirroring the primary CTA color as a clear active signal. Placeholder uses {colors.muted} (#676986). Error states should use a red border (not currently extracted) and keep the {rounded.sm} shape.

### Navigation

**`nav-bar`** — White ({colors.surface-card}), 64px tall, with a 1px {colors.hairline} bottom border for definition against the canvas. The Flamingo wordmark sits at the leading edge in {colors.ink}. Product category links use {typography.nav-link} (Inter 500, 14px). On scroll, the bar adds a soft drop shadow rather than changing color. Above it, the **announcement-bar** pins a 40px strip in #6600ff with white {typography.body-sm} center-aligned text — typically one line covering free shipping thresholds or promo codes. The bar is dismissible; closing it collapses to show the nav at full height.

### Product Card

**`product-card`** — White ({colors.surface-card}) background with {rounded.sm} radius on card and image clip. Image fills the top at a square or 4:5 ratio. Title uses {typography.title-sm} in {colors.ink}; price uses {typography.price} below. A **badge-promo** may overlay the image corner: full-pill, #6600ff fill, white uppercase Inter 700 at 11px. On desktop hover, the card lifts with a soft box-shadow and the image scales to 1.03×. No decorative dividers between cards — whitespace and shadow provide separation.

### Hero Section

**`hero-section`** — Full-bleed panels in {colors.brand-deep} (#2b1453) anchor launch campaigns and seasonal moments. Headline runs {typography.display-xl} in white; body copy uses {typography.body-md} in {colors.on-dark} at ~70% opacity for a secondary register. A single button-primary CTA sits below copy. Photography or flat-color illustration bleeds to the container edge with no inner padding; text lives in the left ~50% column at desktop, stacked below image at mobile.

### Filter Pills

**`filter-pill`** — Pill-shaped toggles ({rounded.full}, 36px tall) for shade, category, and skin-type filters. Resting state: {colors.surface-soft} fill, {colors.muted} text, 1px {colors.hairline} border. Active state: #6600ff fill, white text, border removed. The visual flip is high-contrast with no intermediate glow or transition — selection is clear at a glance. At mobile, the filter row becomes a horizontally scrollable no-wrap strip.

### Badges

**`badge-promo`** — Tight pill in #6600ff (4px 10px padding) with white Inter 700 uppercase text at 11px. Applied to product image overlays for "NEW", "SALE", and "BESTSELLER" labels. The badge reads as a tag, not a button — its small scale makes the violet pop without competing with the CTA.

**`badge-category`** — Same pill geometry with {colors.surface-soft} fill and {colors.muted} text. Used on editorial pages and blog content for taxonomy tagging (e.g., "Shaving", "Skincare", "Tips").

### Section Label

**`section-label`** — A short uppercase line in {colors.primary} (#6600ff) using {typography.label-uppercase} (Inter 700, 11px, 0.55px tracking), placed above a section headline to signal context ("OUR PICKS", "HOW IT WORKS"). The violet color makes these eyebrow labels feel like a live element rather than decorative chrome.

### Review Widget

**`review-widget`** — Powered by Okendo (`oke-widget-icons` icon font for star glyphs). Card surface is {colors.surface-card} with a 1px {colors.hairline-soft} border, {rounded.sm} corners. Star glyphs render in {colors.primary} (#6600ff) — an unusual choice that replaces conventional gold/amber with violet, keeping the entire product detail page inside the brand's hue family. Reviewer name uses {typography.caption}; review body uses {typography.body-sm}.

### Category Card

**`category-card`** — Used on collection landing pages to organize SKU families (razor, wax, body lotion, etc.). {colors.surface-soft} fill, {rounded.md} corners. A product illustration or still-life photo occupies the top half; {typography.title-md} label and a {typography.body-sm} descriptor sit below. CTA link uses {colors.primary} underline text rather than a full button, keeping the card light.

### Footer

**`footer`** — {colors.ink} (#141414) background with four link columns at desktop. Column headings use {typography.title-sm} in {colors.on-dark}; links use {typography.body-sm} in {colors.muted-soft} (#9a9db1). Social icons render inline at 20px in {colors.muted-soft}. Newsletter input at the footer base is a {rounded.sm} field with an inline {rounded.full} pill CTA at desktop widths. Legal copy drops to {typography.caption} in {colors.muted-soft}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart; hero stacks image above text; filter pills scroll horizontally no-wrap; primary buttons go full-width in add-to-cart contexts |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category links inline, secondary links in hamburger drawer; hero uses 60/40 text-image split |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav links visible; hero text in 50% left column with image bleeding right; filter pills wrap naturally |
| Wide | > 1440px | Content max-width ~1280px centered with expanding side gutters; hero image area breathes wider; column count stays at four |

### Touch Targets

- All buttons minimum 48px tall, matching iOS HIG and Material touch guidelines
- Filter pills are 36px tall — below guideline but acceptable in a dedicated horizontally scrolling filter row with ample side padding
- Nav icons (cart, hamburger) have minimum 44×44px tap zones, independent of visible icon size
- Product cards are fully tappable across title and price rows — no dead zones

### Collapsing Strategy

- Nav: all category links collapse into a slide-in left drawer at mobile, using {colors.surface-card} background and {typography.title-sm} per row; the drawer closes on backdrop tap or ✕ button
- Filter row: converts from a flex-wrap grid to a horizontally scrollable no-wrap strip; no "Show more" toggle or modal fallback
- Hero section: image moves above text at mobile; the CTA button shifts below body copy and expands to full column width
- Footer: four columns collapse to two at tablet, then to a single-column accordion at mobile; each heading row acts as a disclosure toggle with a +/− indicator

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand display typeface detected; Inter is the sole extracted font family. A web font loaded via JS after interaction (or served through an A/B test) may exist but was not captured.
- Pure white (#ffffff) did not appear in the extracted top-color list; {colors.surface-card} is inferred as white for component backgrounds — verify against live rendered surfaces.
- Exact button and card border-radius values could not be confirmed from static extraction; {rounded.full} for CTAs and {rounded.sm} for inputs and cards are inferred from visual inspection conventions for the brand's pill-forward aesthetic.
- The `oke-widget-icons` and `oke-widget-icons!important` font stacks are Okendo review-widget icon fonts, not brand typefaces.
- Animation easing curves, transition durations, and motion tokens were not captured.
- Dark mode support (if any) is unconfirmed; {colors.ink} (#141414) appears in footer contexts but may not be part of a full dark-mode theme toggle.
- The meta theme-color (#c4cdd5) represents the mobile browser chrome tint only; it is not a confirmed in-product UI color.
- Exact grid gutter widths, hero aspect ratios, and product image aspect ratios were not extracted; values above use sensible defaults derived from the spacing token set.
