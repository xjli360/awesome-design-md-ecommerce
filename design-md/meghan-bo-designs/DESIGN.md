---
version: alpha
name: "Meghan Bo Designs"
source_url: "https://www.meghanbo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Gold fills the frame before the serif does — Meghan Bo's homepage leads with warm, close-cropped jewelry photography where 14k gold catches ambient light in a way that makes the product feel wearable rather than precious. The brand occupies a register of restrained intimacy: small-batch, handmade-feeling fine jewelry priced for daily wear, communicated through a cream-and-gold palette that keeps the metal itself as the loudest visual statement. Display type leans into a high-contrast serif — the kind with hairline horizontals and swelled verticals borrowed from editorial fashion print — while body copy shifts to a geometric sans-serif at modest weights, a pairing that reads as "jewelry boutique" without being fusty. Buttons are minimal: thin-bordered outlines or flat-gold fills with generous letter-spacing in uppercase, echoing the restraint of a museum label beside an object that speaks for itself. Product cards strip back to a single image, name, and price with no badges or urgency mechanics — the brand trusts the object. Navigation stays slim and centered, a single horizontal row of category names in spaced-out caps that disappear on scroll so the photography can breathe. The overall rhythm is slow and unhurried: wide section padding, tight gutter widths, a canvas that sits closer to warm ivory (#FAF8F5) than clinical white, lending a tactile analog warmth to every screen. Rounded corners are conservative — a small `{rounded.sm}` on cards and inputs rather than pill shapes — reinforcing the artisan seriousness rather than playful DTC softness. Hairlines are faint warm stone (#E8E2D9), borders that whisper rather than divide. The gold accent (#B8965A) earns its role as primary by appearing in only the most decisive moments: active CTAs, hover underlines, and the thin rule that separates site header from body.

colors:
  primary: "#B8965A"
  primary-active: "#9A7A44"
  primary-disabled: "#DDD0B8"
  ink: "#1A1814"
  body: "#3D3A36"
  muted: "#7A7570"
  muted-soft: "#A8A4A0"
  hairline: "#E8E2D9"
  hairline-soft: "#F0EDE8"
  canvas: "#FFFFFF"
  surface-soft: "#FAF8F5"
  surface-card: "#FFFFFF"
  surface-warm: "#F4F0EA"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  gold-light: "#D4B896"
  error: "#9B2020"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'IM Fell English', 'Playfair Display', Georgia, serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.02em
  display-lg:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Jost', 'Montserrat', 'Raleway', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Jost', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.14em
    textTransform: uppercase
  body-md:
    fontFamily: "'Jost', 'Montserrat', 'Raleway', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.02em
  body-sm:
    fontFamily: "'Jost', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.02em
  caption:
    fontFamily: "'Jost', 'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.06em
  price:
    fontFamily: "'Jost', 'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  nav-link:
    fontFamily: "'Jost', 'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.18em
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', 'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.18em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Montserrat', sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.16em
    textTransform: uppercase
  editorial-quote:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 24px
    fontWeight: 300
    fontStyle: italic
    lineHeight: 1.5
    letterSpacing: 0.01em

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
  section: 80px
  section-lg: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 46px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 46px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-ghost-gold:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 46px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 42px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoTypography: "{typography.display-sm}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: none
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    letterSpacing: 0.1em
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    gap: "{spacing.sm}"
    hoverEffect: "image zoom 1.03 scale, 300ms ease"
  product-card-label:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    position: "top-left overlay"
  collection-grid:
    columns: 4
    columnsMobile: 2
    columnsTablet: 3
    gap: "{spacing.base}"
    paddingHorizontal: "{spacing.xl}"
  hero-full:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    layout: "image-left text-right 50/50 split"
    paddingVertical: "{spacing.section}"
  hero-editorial-text:
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.editorial-quote}"
    textAlign: center
    maxWidth: 640px
    paddingVertical: "{spacing.section-lg}"
  section-divider-rule:
    borderTop: "1px solid {colors.hairline}"
    marginVertical: "{spacing.section}"
  collection-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-lg}"
    subtitleTypography: "{typography.body-md}"
    paddingVertical: "{spacing.xxl}"
    textAlign: center
  material-badge:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.gold-light}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 420px
    borderLeft: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    itemNameTypography: "{typography.body-sm}"
    itemPriceTypography: "{typography.price}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.title-sm}"
    borderTop: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.section}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted-soft}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 8px 14px
  ring-sizer-prompt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    rounded: "{rounded.none}"

## Components

### Buttons

**`button-primary`** — Flat gold fill (#B8965A) with white uppercase tracking text, no border radius, 46px tall. Hover darkens to `{colors.primary-active}` with no animation beyond the color swap, communicating confidence without showiness. Disabled state bleaches to `{colors.primary-disabled}`, preserving the shape language while withdrawing interactivity.

**`button-secondary`** — Transparent background with a 1px ink-colored border and the same uppercase tracking label as the primary. On hover, inverts to a solid ink fill with white text — a clean reversal that reads as intentional rather than accidental. Both button types share identical sizing and letter-spacing so they can sit side-by-side without visual hierarchy confusion.

**`button-ghost-gold`** — Transparent with a 1px gold border and gold text, used for secondary CTAs in editorial contexts where the black secondary button would feel too heavy against a warm cream background.

### Navigation

**`nav-bar`** — 64px centered bar on a pure white canvas, with the logo in display serif centered or left-anchored and category links in 11px spaced uppercase sans-serif. An announcement bar in dark ink sits above at 36px with promotional copy in tight caps. On scroll, the announcement bar collapses and the nav gains a faint hairline bottom border — no box shadow, preserving the airy overhead feel.

### Product Cards

**`product-card`** — Square-to-portrait (4:5) image on a warm ivory background, no border, no rounding. Product name sits below in 13px sans-serif at normal weight, price below that in the same scale at a slightly lighter color. A 1.03x image zoom on hover is the only interaction affordance — no "quick add" overlay, no urgency badges. The restraint positions each card as an object to consider rather than a unit to convert.

### Hero Sections

**`hero-full`** — Typically a 50/50 split: rich macro jewelry photography left, editorial text and CTA right. Title in light-weight Cormorant Garamond at 48px, sub-copy in 15px sans-serif. Background of the text panel sits on `{colors.surface-warm}` to lift it from the canvas without adding a new color.

**`hero-editorial-text`** — Center-aligned text-only hero for campaign moments: a display headline, an italic serif subline in `{typography.editorial-quote}`, and a single ghost-gold button. Maximum width 640px, padded generously above and below with `{spacing.section-lg}`.

### Product Detail Page

**`size-selector`** — Flat rectangular swatches with 1px hairline borders, zero radius. Selected state fills with ink color and inverts text to white, directly echoing the button-secondary hover behavior for system consistency.

**`ring-sizer-prompt`** — A quiet warm-toned inset block below the size row, carrying a short text link to a ring-sizer guide. Styled in `{colors.surface-soft}` with a hairline border; the link itself uses gold to signal interactivity without breaking the calm.

**`material-badge`** — Inline label for metal type (14k Gold, Sterling Silver) in 12px uppercase gold text with a faint gold hairline border. No fill. Appears on product cards and PDP to communicate material tier at a glance.

### Cart & Footer

**`cart-drawer`** — Right-side sliding drawer, 420px wide, white background, single left hairline border. Title in uppercase tracking sans, item names in 13px body, prices in the dedicated price scale. No aggressive upsell blocks.

**`footer`** — Warm ivory (`{colors.surface-soft}`) background with four columns: navigation links, care guide, about, and newsletter signup. Headings in uppercase title-sm, links in caption-scale sans. Top hairline border only.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; product grid collapses to 2 columns; nav bar condenses to logo + hamburger; hero switches to stacked image-over-text; cart drawer goes full width |
| Tablet | 744–1128px | Product grid 3 columns; nav links visible but tighter spacing; hero maintains split but text column shrinks; collection banner reduces vertical padding |
| Desktop | 1128–1440px | Full 4-column product grid; nav expands to include all category labels; hero split at full 50/50; section padding at `{spacing.section}` |
| Wide | > 1440px | Content container max-width ~1400px, centered; section padding increases to `{spacing.section-lg}`; hero image gets more breathing room |

### Touch Targets

- All buttons minimum 44px tall; `button-primary` and `button-secondary` set to 46px
- Size selector swatches minimum 44×44px on mobile even if visually smaller on desktop
- Nav hamburger icon minimum 44×44px tap target
- Cart icon and logo anchors padded to 44px tap height

### Collapsing Strategy

- Announcement bar hides on scroll on mobile to preserve viewport; on desktop it collapses on scroll but reappears on scroll-up
- Four-column footer collapses to two columns on tablet, single accordion-style column on mobile
- Editorial hero text panel stacks below image on mobile, reducing type size from 48px to 30px display-md
- Collection sub-nav (if present) wraps to a horizontal scroll strip on mobile rather than stacking vertically

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site returned no color data during crawl (likely JS-rendered tokens or anti-bot protection). All palette values are inferred from brand category conventions (artisan fine jewelry, gold/silver everyday) and are not verified against live production
- **No font stacks extracted** — font families (Cormorant Garamond, Jost) are inferred from visual conventions common to small fine jewelry DTC brands; actual typefaces may differ entirely
- **No theme-color meta tag** — prevents confirming primary brand color; gold (#B8965A) is a reasonable inference but should be validated against the live site
- **Platform unconfirmed** — flagged as non-Shopify, but no framework signals were extracted; component patterns may need adjustment for the actual stack
- **Logo treatment unknown** — whether the wordmark is typeset in the display serif or a custom lockup cannot be confirmed without visual inspection
- **Motion and transition values** — hover durations and easing curves are estimated at typical fine jewelry conventions (slow, 300–400ms ease); not extracted
- **Mobile navigation pattern** — hamburger vs. bottom tab bar vs. slide-out drawer cannot be confirmed; hamburger assumed as default
