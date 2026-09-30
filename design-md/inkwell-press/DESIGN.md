---
version: alpha
name: "Inkwell Press"
source_url: "https://inkwellpress.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The brand name is typeset with WELL in capitals — inkWELL — embedding a wellness claim directly into the wordmark, and the rest of the visual system honors that signal faithfully. Warm caramel gold (#ce9a60) reads against parchment cream (#f7eedd) the way a leatherbound cover reads against ivory page stock: deliberate, analog-first, and premium without being austere. The pair anchors a disc-planner brand that positions daily scheduling as a self-care practice rather than a productivity system, and the entire color architecture reinforces that positioning — there is no cold blue, no clinical white, no neutral gray promoted to primary.

  Both typefaces — Poppins for display and Cabin for body text — are humanist geometric sans-serifs: geometric in structure but warm in execution. Neither has the corporate regularity of Helvetica or the technical formality of Futura; together they signal contemporary design literacy without alienating the journaling and planner community that gravitates toward softer, more personal aesthetics. Display lockups in Poppins 700 lend structure at large sizes; Cabin at 400 handles editorial copy with legibility and approachability at reading sizes.

  The color extraction surfaces a dual near-black system — #1a1b18 for primary type and #121212 for deep UI surfaces — suggesting the brand uses darkness contextually: rich near-black for inversion modules like email capture, while lighter parchment surfaces carry the main reading experience. The secondary gold #b78c24 functions as a darkened primary for hover and active states, keeping interactions within the warm amber register rather than shifting to a generic blue. The Shopify defaults #d72c0d and #008060 appear in the extracted palette as functional system colors — error red and success green respectively — and are treated strictly as utility tokens, never promoted to brand expression.

  Rounded corners throughout read at {rounded.sm} to {rounded.md}: softened but not pill-shaped. Disc planners photographed flat on linen and wood surfaces inform the prop styling sensibility, and the UI echoes that — no hard 90-degree corners anywhere in interactive components, and every surface carries a slight warmth through either the parchment background or the caramel accent color. The store's visual logic is legible in a single scroll: paper goods, warm light, and the message that writing things down is good for you.

colors:
  primary: "#ce9a60"
  primary-active: "#b78c24"
  primary-disabled: "#e8c8a0"
  ink: "#1a1b18"
  body: "#3d3c39"
  muted: "#7a7972"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f7eedd"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#d72c0d"
  success: "#008060"

typography:
  display-xl:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  label-caps:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  price:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Cabin', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    ctaGap: "{spacing.sm}"
  collection-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  collection-badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  collection-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  price-display:
    currentTypography: "{typography.price}"
    currentColor: "{colors.ink}"
    compareColor: "{colors.muted}"
    compareTextDecoration: line-through
    saleColor: "{colors.error}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  email-capture:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    inputBackgroundColor: "{colors.canvas}"
    inputTextColor: "{colors.ink}"
    inputRounded: "{rounded.sm}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.sm}"
    padding: "{spacing.section} {spacing.xl}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The primary CTA uses the caramel gold (#ce9a60) fill with white text, 8px radius, and Cabin Semi-Bold at 15px with subtle letter-spacing. On hover, the background shifts to the deeper amber `{colors.primary-active}` (#b78c24); on disabled, it fades to the muted `{colors.primary-disabled}` (#e8c8a0). Height is fixed at 48px to ensure comfortable tap targets across all breakpoints. The warm gold CTA reads distinctly on both white canvas and parchment surfaces without requiring a hover underline or shadow.

**`button-secondary`** — An outlined button using the near-black `{colors.ink}` border and text on white canvas. Shares the same 48px height and `{rounded.sm}` radius as `button-primary` for optical consistency when the two appear side by side in hero CTAs or product detail pages. Border weight is 1.5px to hold legibility at small sizes.

**`button-ghost`** — A caramel-outlined variant using `{colors.primary}` for both border and text on a transparent fill. Reserved for secondary actions in warmer surface contexts — product cards on parchment, email section secondary links — where the black outline of `button-secondary` would read too heavy against the soft background.

### Text Input

**`text-input`** — Default state carries a 1px `{colors.hairline}` border on white canvas, keeping forms visually light. Focus ring upgrades to 1.5px `{colors.primary}` — the caramel gold keeps focused states warm rather than defaulting to a browser blue that would break the palette. Cabin Regular at 16px ensures editorial legibility in longer email and address fields. Placeholder text renders in `{colors.muted}` to maintain sufficient contrast without competing with entered values.

### Navigation

**`nav-bar`** — 64px tall, white canvas, hairline bottom border, with Cabin Semi-Bold at 14px / 0.2px tracking for nav links. The compact 64px height suits a focused planner catalog with limited primary categories. An `announcement-bar` in `{colors.ink}` with all-caps Cabin at 11px / 1.2px letter-spacing sits above the nav for shipping thresholds, product launches, and seasonal promotions — the black ground reads as authoritative and distinct from the warm caramel brand accent.

### Product Card

**`product-card`** — Cards rest on white surface with 8px radius on both the card shell and the product image frame. Titles use Poppins Semi-Bold at 16px; price uses the dedicated `{typography.price}` token (Poppins 600 at 18px) to weight the conversion moment distinctly from editorial copy. Badge overlays position top-left on the image using `{typography.label-caps}` — uppercase tracking at 1.2px reads confidently at small sizes without requiring a heavy weight. A subtle gap between image and text area (`{spacing.sm}`) keeps the card from feeling cramped.

### Hero Section

**`hero-section`** — The hero sits on the warm parchment surface (`{colors.surface-soft}`, #f7eedd), immediately separating the site from white-canvas Shopify defaults. Headline copy uses Poppins 700 at 52px / -0.5px tracking for tight editorial control at large sizes. The parchment ground evokes the core product — actual paper — without reaching for illustration or metaphor. CTA buttons sit in a small horizontal cluster with `{spacing.sm}` gap: typically a `button-primary` ("Shop Planners") beside a `button-secondary` ("Take the Quiz").

### Collection Badges

**`collection-badge`** — The default badge (Bestseller, Featured) fills with the primary caramel gold and white all-caps Cabin, sitting at 4px radius to feel like a stamp rather than a pill. `collection-badge-new` flips to `{colors.ink}` fill for a high-contrast announcement effect. `collection-badge-sale` uses the functional error red `{colors.error}` (#d72c0d) — strictly reserved for discount events and kept off standard marketing surfaces to preserve the warm amber brand register.

### Price Display

**`price-display`** — Current price in Poppins 600 at 18px in `{colors.ink}`. When a sale is active, the compare-at price renders in `{colors.muted}` with `text-decoration: line-through`; the sale price switches to `{colors.error}` to signal urgency without disrupting the overall warm palette. The two sit on the same baseline, compare-at text slightly smaller via `{typography.body-sm}`.

### Testimonial Card

**`testimonial-card`** — Customer reviews sit on the warm parchment surface inside a card with a 1px hairline border and 12px radius. Quote text uses Cabin Regular at 16px with a relaxed line-height of 1.6 for comfortable reading of multi-sentence reviews. Author attribution uses `{typography.caption}` in `{colors.muted}`. Cards appear in a 3-column grid on desktop, collapsing to a single-column carousel on mobile with pagination dots.

### Email Capture

**`email-capture`** — The email signup module inverts against `{colors.surface-dark}` (#121212) to create a decisive tonal break in the otherwise warm, light-surfaced page. Headline in Poppins Semi-Bold at 24px in `{colors.on-dark}`; supporting copy in Cabin Regular at 14px at slightly reduced opacity. The caramel gold CTA reads warmly against the near-black ground, reinforcing brand presence even in a functional conversion block. Input and button maintain `{rounded.sm}` for consistency with the rest of the form system.

### Footer

**`footer`** — Footer sits on `{colors.surface-soft}` parchment, matching the hero to create a bookend framing the full page scroll. Column headings use Poppins Semi-Bold at 16px; body links use Cabin Regular at 14px in `{colors.body}`. A 1px hairline top border separates footer from content. Bottom row carries legal copy and payment icons in `{typography.caption}` / `{colors.muted}`.

### Breadcrumb

**`breadcrumb`** — Breadcrumbs appear on product and collection pages in `{typography.caption}` / `{colors.muted}`, with a hairline separator between segments. Gap between items is `{spacing.xs}`. The muted treatment keeps breadcrumbs navigable without competing with product headlines on the same view.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks image above headline; nav collapses to hamburger drawer from left; announcement bar truncates to one line; email capture input and CTA stack vertically |
| Tablet | 744–1128px | Two-column product grid; hero uses side-by-side layout with headline at ~38px; nav shows primary links with overflow in dropdown; testimonial cards in 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all category links; hero at full 52px type scale; email capture in two-column split (copy left, form right) |
| Wide | > 1440px | Content max-width ~1400px centered; hero padding expands to maintain proportion; four-column product grid on collection pages; footer in 5-column layout |

### Touch Targets

- All buttons fixed at 48px height minimum
- Nav links maintain 44px touch target height on mobile regardless of visual size
- Product card images have full-bleed tap area; text area below is a separate tap zone
- Icon buttons (wishlist, cart, hamburger) maintain 44×44px minimum tap area
- Badge overlays do not intercept taps on the product card image

### Collapsing Strategy

- Navigation collapses to hamburger at < 744px; drawer slides from left with `{colors.canvas}` background and `{colors.ink}` close icon
- Product card price and badge information remains visible at all breakpoints — never hidden behind hover state on mobile
- Testimonial cards collapse from 3-column grid to single-column swipeable carousel with dot pagination
- Email capture stacks input and CTA button vertically on mobile; input becomes full-width
- Footer 4-column link grid collapses to single-column accordion on mobile with Poppins heading as toggle trigger
- Hero CTA button pair stacks vertically on mobile at full width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit border-radius values extracted from computed CSS; `{rounded.sm}` (8px) and `{rounded.md}` (12px) are inferred from the humanist sans-serif aesthetic and planner category conventions
- Font size values for display-xl and display-md are estimated from category norms — no computed CSS font-size values were available in extracted hints
- #008060 and #d72c0d are Shopify system defaults (success green / error red) rather than inkWELL Press brand colors; treated as functional-only tokens
- No dark mode palette detected — `{colors.surface-dark}` (#121212) appears as a single email-capture inversion surface, not a full dark scheme
- Letter-spacing and line-height values for Poppins display scales are estimated; live rendering may differ
- No icon system, illustration style, custom graphic elements, or planner-cover photography art direction could be extracted from the available hints
- Disc planner customizer UI (cover color picker, disc size selector, layout options) likely exists on product detail pages but could not be characterized without visual extraction
- The relationship between Cabin and Poppins across specific page regions (which headings use which family) is inferred from typical two-family DTC patterns, not confirmed from computed styles
