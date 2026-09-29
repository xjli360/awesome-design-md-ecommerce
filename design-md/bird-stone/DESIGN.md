---
version: alpha
name: "Bird + Stone"
source_url: "https://www.birdandstone.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every piece at Bird + Stone ships with a cause printed on the tag — a wildlife fund, a girls' education program, a clean-water initiative — converting the act of buying a gold-fill ring into a legible commitment. That friction between lightness (the bird) and permanence (the stone) shapes the visual language: a warm ivory canvas (#fdfaf7) holds near-black ink (#1a1714) in tension with a single warm-gold primary (#c9a87c) that reads less like a brand color and more like the metal itself photographed under soft north light. Display type leans on a high-contrast serif — thin-stroked, slightly condensed — with the cadence of an independent jeweler's letterhead rather than a volume e-commerce template. Body copy and navigation drop to a restrained geometric sans at small weights, with letter-spacing pushed open enough to feel deliberate without tipping into fashion-brand affectation. Buttons stay close to `{rounded.sm}` rather than pushing to pill shapes; only the material-tag chip reaches `{rounded.full}`, marking metal type or stone names as a soft descriptor rather than a CTA. Product cards surface a cause-tag badge in a muted sage (#4a7c59) beneath the price — a small ribbon that reinforces why you're buying rather than just what. Navigation is minimal: four or five links, no mega-menu, a persistent cart drawer sliding from the right without a page reload. Section padding runs wide at `{spacing.section}`, giving each piece the room on a grid that a volume jeweler would fill with another SKU. Hairlines and surfaces lean toward taupe and cream rather than neutral grays, so the warm gold metal sits in a visual environment that flatters rather than competes. The overall register is intimate and purposeful — a brand that treats each purchase as a small act of advocacy, and designs accordingly.

colors:
  primary: "#c9a87c"
  primary-active: "#b5924a"
  primary-disabled: "#e8d9c0"
  gold-light: "#e8d0a0"
  gold-deep: "#8a6a32"
  cause-green: "#4a7c59"
  cause-green-text: "#ffffff"
  ink: "#1a1714"
  body: "#3d3530"
  muted: "#7a6f68"
  hairline: "#e0d8d0"
  hairline-soft: "#ede8e2"
  canvas: "#fdfaf7"
  surface-soft: "#f8f3ee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#c13515"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'Cormorant', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cormorant Garamond', 'Cormorant', Georgia, serif"
    fontSize: 34px
    fontWeight: 300
    lineHeight: 1.22
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Cormorant Garamond', 'Cormorant', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.025em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.46
    letterSpacing: 0.03em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.04em
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.07em
    textTransform: uppercase
  cause-tag:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  announcement:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.06em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    rounded: "{rounded.sm}"
    padding: 13px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    border: "none"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "0 {spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.announcement}"
    height: 36px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageRounded: "{rounded.xs}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    causeTypography: "{typography.cause-tag}"
    gap: "{spacing.sm}"
    padding: "{spacing.sm}"
  cause-badge:
    backgroundColor: "{colors.cause-green}"
    textColor: "{colors.cause-green-text}"
    typography: "{typography.cause-tag}"
    rounded: "{rounded.xs}"
    padding: "3px 7px"
  material-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 540px
    padding: "{spacing.section}"
    imagePosition: right
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    width: 420px
    borderLeft: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    activeBorderBottom: "1px solid {colors.ink}"
    padding: "{spacing.sm} 0"
  pdp-meta-block:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    causeBadgeComponent: "cause-badge"
    divider: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xl}"
  pdp-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderSelected: "1px solid {colors.ink}"
    borderDefault: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.section}"
  section-header:
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    textAlign: center
    maxWidth: 560px
    gap: "{spacing.md}"

## Components

### Buttons
**`button-primary`** — A warm-gold fill (#c9a87c) at 44px height, uppercase tracking-wide label in 12px sans-serif. On hover, background deepens to `{colors.primary-active}` (#b5924a) with no transform or shadow; the restraint keeps it feeling like a jeweler's counter rather than a checkout funnel. Disabled state uses `{colors.primary-disabled}` with muted text.

**`button-secondary`** — Transparent fill, 1px border in `{colors.ink}`, same uppercase type. Sits beside `button-primary` on PDPs for add-to-wishlist or "learn about this cause" flows. On hover the border lightens to `{colors.muted}`.

**`button-ghost`** — No border, no background; muted text in `{typography.button-sm}`. Used for inline navigation actions ("clear filters", "show more") where visual weight would distract from product photography.

### Text Input
**`text-input`** — Warm-canvas background, thin hairline border that transitions to `{colors.primary}` gold on focus. Corner radius is minimal at `{rounded.xs}` (2px) to keep the form aesthetic grounded. Used for email capture, search, and checkout fields.

### Navigation
**`nav-bar`** — 60px tall, warm ivory background, uppercase 12px sans links with 0.07em tracking. A subtle hairline-soft bottom border separates it from the page without the hard line many jewelry brands use. Logo sits centered or left; a cart icon and account icon occupy the right end. No mega-menu — category links expand into simple dropdowns on hover.

**`announcement-bar`** — Slim 36px stripe in `{colors.surface-soft}` above the nav, rotating cause-of-the-month copy in `{typography.announcement}`. Keeps the mission visible without interrupting the shopping flow.

### Product Card
**`product-card`** — Clean white card with minimal 2px corner radius on the image frame. Title in `{typography.title-sm}`, price in `{typography.price-display}` on the same line or stacked. A `cause-badge` in sage green sits below the price, naming the cause this piece supports. On hover, image scales to ~1.03× with a 300ms ease; no overlay text appears.

### Cause Badge
**`cause-badge`** — Sage green (#4a7c59) chip in uppercase 10px, 2px radius. The single moment of color outside the gold primary, chosen to signal ecology and ethics rather than urgency. Appears on product cards, PDP meta blocks, and the cart line item.

### Hero
**`hero`** — Warm surface-soft background, minimum 540px height, `{typography.display-xl}` serif headline at weight 300 (the thin stroke against cream reads as refinement without austerity). Right-side or full-bleed editorial photography. One `button-primary` CTA, sometimes accompanied by a `button-ghost` "shop by cause" link.

### Cart Drawer
**`cart-drawer`** — 420px right-side panel over a scrim, canvas background, left border in `{colors.hairline}`. Each line item shows thumbnail, title in `{typography.title-md}`, price in `{typography.price-display}`, and the cause badge. No upsell grid — the drawer stays purposeful.

### PDP Meta Block
**`pdp-meta-block`** — Product title in `{typography.display-sm}` serif, price in `{typography.price-display}`, cause badge immediately below. Material swatches use `pdp-swatch` with 20px circles and a hairline border that thickens to ink on selection. Dividers in `{colors.hairline-soft}` separate each section (metal, size, care, cause detail).

### Material Tag
**`material-tag`** — Pill-shaped chip at `{rounded.full}` in `{colors.surface-soft}`, 1px hairline border, caption-scale text. Used to label "14k Gold Fill", "Sterling Silver", "Vermeil" beneath product titles and in filter rows.

### Footer
**`footer`** — Surface-soft background, generous `{spacing.xxl}` vertical padding. Four columns: Shop, Give Back, About, Care Instructions. Links in `{colors.ink}`, body copy in `{colors.body}`. The "Give Back" column names active cause partners with short descriptions — the mission presence carried to the bottom of every page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; announcement bar text truncates to one cause name; hero image stacks below headline; cart drawer goes full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero image at 45% right column; section padding reduces to `{spacing.xl}` |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero at split 50/50 layout; cause badge visible on card hover as well as default state |
| Wide | > 1440px | Grid max-width caps at 1320px centered; hero image expands but headline container stays fixed; section padding increases to `{spacing.section}` |

### Touch Targets
- All buttons minimum 44px height, matching `button-primary` and `button-secondary` specs
- Swatch circles 20px display, tap target padded to 36×36px minimum
- Cart and account icons in nav-bar padded to 44×44px touch area
- Cause-badge chips are display-only, not interactive; no tap-target requirement

### Collapsing Strategy
- Navigation collapses to hamburger below 744px; drawer slides from left
- Filter row on collection pages collapses to a "Filter & Sort" bottom sheet on mobile
- PDP image gallery switches from side-scroll thumbnails to swipe-enabled full-width carousel on mobile
- Announcement bar hides on screens narrower than 375px if text overflows one line
- Cart drawer becomes a full-screen overlay below 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Extraction returned unrelated site data**: the live-site crawler returned content and colors from "Xoilac TV" (a Vietnamese football streaming service), not birdandstone.com. All hex colors and font stacks in this file are derived from brand knowledge and fine-jewelry category conventions, not confirmed extraction.
- **Exact brand fonts unconfirmed**: the use of Cormorant Garamond for display type is inferred from brand aesthetic; the actual font may be Freight Display, Canela, or a licensed serif not publicly identified.
- **Primary gold hex unverified**: #c9a87c is a reasonable approximation for warm gold-fill imagery; the true brand primary may differ.
- **Cause-badge green unverified**: #4a7c59 is inferred; the actual environmental/cause accent color is not confirmed from extraction.
- **Specific component spacing**: padding values, grid gutter widths, and animation durations are estimates consistent with Shopify-based fine jewelry stores.
- **Dark mode**: no evidence of a dark mode variant; assumed single light theme throughout.
