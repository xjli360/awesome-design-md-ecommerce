---
version: alpha
name: "Abby & Finn"
source_url: "https://abbyandfinn.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The diaper print comes before the subscription pitch — Abby & Finn's entire conversion model is organized around illustrated pattern swatches as the first aesthetic commitment a parent makes, not a feature grid or a price comparison. That sequencing shapes everything downstream: the palette is not a single brand voltage but a rotating cast of saturated accent hues (coral, lavender, sunshine yellow, teal) that shift by product line and season, held together by a consistent warm-white canvas and one anchoring teal (#28A99E) that shows up on primary CTAs, nav highlights, and the brand wordmark. Rounded corners are aggressive and consistent — there are no hard edges anywhere a parent might visually "land." Buttons, cards, badges, and input fields all sit at or above `{rounded.md}`, and the subscription pill uses `{rounded.full}` to signal something opt-in and gentle rather than contractual. The type system leans on a friendly, open sans-serif with generous x-height and light-to-medium weights; display headings stay under 700 weight to avoid the commanding tone that would feel out of place in a category about infant comfort. Eco-certification badges travel in a horizontal strip below the fold, rendered as small icon-plus-text lockups rather than the loud green bursts competitors use — the credentials are there, but they don't perform anxiety. Product cards show a full-bleed print swatch on top, price and "ships every X weeks" copy below, and a teal `{rounded.full}` add-to-box button that never says "buy." The overall register is a children's picture book that has been disciplined into an e-commerce funnel: playful illustration vocabulary, warm neutrals, and a palette that changes its outfit by season while keeping the same friendly face.

colors:
  primary: "#28A99E"
  primary-active: "#1E8F85"
  primary-disabled: "#A8DFDC"
  accent-yellow: "#F5C844"
  accent-coral: "#F07A5B"
  accent-lavender: "#B8A8D4"
  accent-sky: "#7EC8E3"
  ink: "#2C2C2C"
  body: "#4A4A4A"
  muted: "#767676"
  hairline: "#E5E5E5"
  hairline-soft: "#F0EEEA"
  canvas: "#FFFFFF"
  surface-soft: "#F9F7F4"
  surface-card: "#FFFFFF"
  surface-warm: "#FDF6EE"
  on-primary: "#FFFFFF"
  eco-green: "#4CAF7D"
  star-gold: "#F5B942"
  error: "#D64545"

typography:
  display-xl:
    fontFamily: "'Nunito', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.46
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  label-uppercase:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 800
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  frequency-select:
    fontFamily: "'Nunito', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        textColor: "{colors.on-primary}"

  button-primary-lg:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 18px 40px
    height: 60px

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 48px
    states:
      hover:
        backgroundColor: "{colors.surface-soft}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px

  button-add-to-box:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 10px 22px
    height: 40px
    label: "Add to Box"

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    states:
      focus:
        border: "1.5px solid {colors.primary}"
        outline: "3px solid {colors.primary-disabled}"
      error:
        border: "1.5px solid {colors.error}"

  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoMaxHeight: 36px
    ctaButton:
      component: button-primary
      label: "Build Your Box"
    states:
      scrolled:
        boxShadow: "0 2px 8px rgba(0,0,0,0.07)"

  mobile-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    backdropColor: "rgba(0,0,0,0.3)"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"

  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    layout: split-50-50
    imageSide: right
    paddingY: "{spacing.section}"
    paddingX: "{spacing.xl}"
    badge:
      backgroundColor: "{colors.accent-yellow}"
      textColor: "{colors.ink}"
      typography: "{typography.badge}"
      rounded: "{rounded.full}"
      padding: "4px 12px"

  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline-soft}"
    overflow: hidden
    swatchImage:
      aspectRatio: "1/1"
      objectFit: cover
      rounded: "{rounded.none}"
    body:
      padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    captionTypography: "{typography.body-sm}"
    captionColor: "{colors.muted}"
    addButton:
      component: button-add-to-box
    states:
      hover:
        boxShadow: "0 6px 20px rgba(0,0,0,0.10)"
        transform: "translateY(-2px)"

  print-swatch-selector:
    layout: "grid"
    columns: 4
    gap: "{spacing.sm}"
    swatchSize: 72px
    rounded: "{rounded.md}"
    border: "2px solid transparent"
    states:
      selected:
        border: "2px solid {colors.primary}"
        boxShadow: "0 0 0 3px {colors.primary-disabled}"
      hover:
        border: "2px solid {colors.hairline}"

  subscription-frequency-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.frequency-select}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    border: "1.5px solid {colors.hairline}"
    states:
      selected:
        backgroundColor: "{colors.primary}"
        textColor: "{colors.on-primary}"
        border: "1.5px solid {colors.primary}"

  eco-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.eco-green}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
    iconSize: 14px
    gap: "{spacing.xs}"

  eco-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    layout: "flex-row"
    gap: "{spacing.xl}"
    paddingY: "{spacing.md}"
    paddingX: "{spacing.lg}"
    borderTop: "1px solid {colors.hairline-soft}"
    borderBottom: "1px solid {colors.hairline-soft}"
    iconColor: "{colors.eco-green}"

  trust-badge-row:
    layout: "flex-row"
    gap: "{spacing.xl}"
    justifyContent: center
    paddingY: "{spacing.xxl}"
    backgroundColor: "{colors.canvas}"
    itemTypography: "{typography.caption-strong}"
    itemColor: "{colors.body}"
    iconSize: 40px
    iconColor: "{colors.primary}"

  review-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.lg}"
    starColor: "{colors.star-gold}"
    starSize: 16px
    authorTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    dateTypography: "{typography.caption}"
    dateColor: "{colors.muted}"

  size-guide-table:
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.label-uppercase}"
    bodyTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rowHoverBackground: "{colors.surface-warm}"
    rounded: "{rounded.md}"
    overflow: hidden

  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    paddingY: "{spacing.sm}"
    textAlign: center

  value-prop-card:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    iconSize: 48px
    iconColor: "{colors.primary}"
    titleTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"

  build-your-box-step:
    stepNumberColor: "{colors.primary}"
    stepNumberTypography: "{typography.display-md}"
    titleTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-md}"
    connectorColor: "{colors.hairline}"
    layout: "horizontal-numbered"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.canvas}"
    paddingY: "{spacing.section}"
    logoMaxHeight: 32px
    socialIconSize: 24px
    borderTop: "none"
    columns: 4

## Components

### Buttons

**`button-primary`** — Full-pill shape (`{rounded.full}`) in brand teal (`{colors.primary}`) with bold white type at 15px/700 weight. The pill form is used even for short labels — "Shop Diapers", "Add to Box", "Get Started" — reinforcing the opt-in softness over transactional bluntness. Hover darkens to `{colors.primary-active}`; disabled washes to `{colors.primary-disabled}` with white text retained for contrast.

**`button-primary-lg`** — Hero-scale variant at 60px height and 18px/700 type, used on landing CTAs ("Build Your Box") where the button must anchor the entire split-panel composition.

**`button-secondary`** — White fill with a 2px teal border and teal text. Appears alongside primary buttons in choice scenarios (e.g., "Learn More" next to "Shop Now"). Hover fills to `{colors.surface-soft}` to signal interactivity without stealing visual weight.

**`button-add-to-box`** — A compact 40px-height pill used inline on product cards. Label always reads "Add to Box" rather than "Buy" or "Add to Cart," reinforcing the subscription-box framing throughout the browse experience.

**`button-ghost`** — Transparent with `{colors.ink}` text, no border. Used for secondary navigation actions and inline text links that benefit from button affordance (e.g., "See All Prints").

### Subscription Frequency Selector

**`subscription-frequency-pill`** — Horizontal row of pill-shaped option chips (e.g., "Every 3 Weeks", "Every 4 Weeks", "Every 5 Weeks"). Unselected state shows a neutral `{colors.hairline}` border on soft background; selected state fills to `{colors.primary}` with white text, making the current cadence immediately legible. This is the most brand-distinctive interactive pattern on the site — it turns a logistical choice into a friendly, tactile selector.

### Navigation

**`nav-bar`** — 68px white header with logo left, text links center (desktop), and a teal pill CTA ("Build Your Box") at far right. A subtle `boxShadow` activates on scroll to separate the nav from content without a heavy border. On mobile, links collapse into an off-canvas drawer (`mobile-menu`) with generous padding and section-level type sizing.

### Product Cards

**`product-card`** — Full-bleed print swatch image occupying the top half of the card, with product name, size range, price, and subscription frequency note below on `{spacing.base}` padding. The teal "Add to Box" pill button sits at the bottom of the card body. On hover, the card lifts 2px with an increased shadow — a motion cue borrowed from lifestyle e-commerce but kept subtle given the parent-focus audience.

**`print-swatch-selector`** — A 4-column grid of 72px square image chips used within the product detail or box-building flow. Selected state gets a 2px teal ring plus a soft teal glow (`{colors.primary-disabled}` outline) to clearly signal which print is chosen without harsh contrast.

### Badges and Labels

**`eco-badge`** — Small pill or tag in `{colors.surface-soft}` with `{colors.eco-green}` text and a matching icon, rendered at `{typography.caption-strong}`. Attached to product cards and product detail pages to flag certifications (chlorine-free, fragrance-free, dermatologist-tested) without interrupting the shopping flow.

**`eco-strip`** — A full-width horizontal band of icon+text lockups (e.g., "Plant-Based", "Free of Chlorine", "No Fragrance") in `{colors.surface-soft}`. Sits between sections as a passive credential read, using `{typography.caption}` to stay informational without being promotional.

**`announcement-bar`** — A 100% width teal bar pinned above the nav. Uses `{colors.primary}` background with white `{typography.caption-strong}` for promotional copy (free shipping thresholds, new print drops, welcome offers). No close button on desktop; dismissible on mobile.

### Hero

**`hero-banner`** — Split 50/50 layout on `{colors.surface-warm}` with headline in `{typography.display-xl}`, supporting body copy in `{typography.body-md}`, a yellow badge pill for any proof point ("Over 1 Million Boxes Shipped"), and a `button-primary-lg` CTA. Lifestyle photography on the right side with no hard crop — image bleeds to the card edge. The warm-white background rather than pure white gives the hero a nursery-room softness.

### Trust and Social Proof

**`trust-badge-row`** — Three to five icon+label pairs centered on a white background, paddedY at `{spacing.xxl}`. Icons render at 40px in `{colors.primary}` teal; labels use `{typography.caption-strong}`. Common entries: "Dermatologist Tested," "Plant-Based Ingredients," "No Harsh Chemicals," "Ships to Your Door."

**`review-card`** — Bordered card with `{rounded.lg}`, star row in `{colors.star-gold}`, reviewer name in `{typography.title-sm}`, body copy in `{typography.body-sm}` at `{colors.body}`. Date and verified-buyer label in `{typography.caption}` at `{colors.muted}`. Laid out in a 3-column grid on desktop, single-column carousel on mobile.

### Size Guide

**`size-guide-table`** — Rounded table with a `{colors.surface-soft}` header row using `{typography.label-uppercase}`, row body in `{typography.body-sm}`. Row hover highlights in `{colors.surface-warm}` for scannability. Typically appears in a modal or collapsible below the size selector on the PDP.

### How It Works

**`build-your-box-step`** — Numbered horizontal step flow. Step numbers render in `{typography.display-md}` at `{colors.primary}` teal, step titles in `{typography.title-lg}`, and body description in `{typography.body-md}`. Thin `{colors.hairline}` connector lines link steps on desktop; steps stack vertically on mobile.

### Footer

**`footer`** — Dark `{colors.ink}` background with a 4-column link grid on desktop. Section titles in `{typography.title-sm}` white, links in `{typography.body-sm}` at `{colors.hairline}`. Logo reversed to white, social icons at 24px. No top border — the transition from light content to the dark footer relies on abrupt color change for visual punctuation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; nav collapses to hamburger + off-canvas drawer; hero becomes full-width stacked (image above, text below); product grid drops to 1-2 columns; print swatch grid reduces to 3 columns; eco-strip scrolls horizontally; trust-badge-row scrolls as horizontal carousel; footer collapses to 1 column with accordioned link sections |
| Tablet | 744–1128px | 2-column product grid; hero remains split but image crop tightens; nav shows abbreviated links (drops lowest-priority items); print swatch grid at 4 columns; trust-badge-row wraps to 2-row grid; footer at 2 columns |
| Desktop | 1128–1440px | Full 3-column product grid; 4-column footer; full nav with all text links + CTA; hero at full 50/50 split with generous padding; eco-strip displays all items inline without scroll |
| Wide | > 1440px | Content max-width capped at ~1280px, centered; hero image crops to fill remaining right column; extra gutter whitespace added at section edges; product grid stays at 3 columns to maintain card readability |

### Touch Targets

- All interactive elements minimum 44×44px on mobile, per WCAG 2.1 AA
- Subscription frequency pills expand to full row width on mobile for easier tap
- Print swatch grid tiles increase to 80px on mobile to hit touch target minimums
- Nav hamburger button is 48×48px tap zone regardless of icon visual size
- Footer accordion headers are full-width tap targets, minimum 48px height

### Collapsing Strategy

- Navigation: text links → hamburger at 744px breakpoint; "Build Your Box" CTA persists as floating bottom bar on mobile scroll
- Product grid: 3-col → 2-col → 1-col at 1128px and 744px respectively
- Eco strip: flex-row → horizontal scroll container on mobile (no wrapping, -webkit-overflow-scrolling: touch)
- Hero: side-by-side → stacked at 744px, image moves above text on mobile
- Footer: 4-col → 2-col → 1-col with accordion on link groups
- Build-your-box steps: horizontal → vertical stack below 744px, connector lines become vertical

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the live site returned no parseable palette tokens. All colors in this spec are estimated from brand-knowledge observation of Abby & Finn's public materials (packaging, social media, brand guidelines visible in press coverage). None should be considered verified without running a direct extraction against the live DOM.
- **No font families extracted** — Nunito / Nunito Sans is an informed estimate consistent with the brand's friendly, rounded visual register, but the actual typeface (which could be a licensed display font, Poppins, Quicksand, or a custom wordmark face) is unconfirmed.
- **Subscription platform details unknown** — the box-building UX (step count, frequency options, size-change flow) is inferred from DTC subscription conventions and publicly available brand marketing, not from a live session with the actual checkout flow.
- **Dark mode** — no evidence for or against; assumed light-only for this spec.
- **Print/pattern names and seasonal rotation** — swatch naming conventions and the full range of diaper print options are not documented here; the print-swatch-selector component assumes a grid model but exact counts and labels are unknown.
- **Exact border-radius values** — the `{rounded.*}` scale is estimated at friendly/high-radius values consistent with the brand's aesthetic. Actual computed values from the live site should be measured if pixel-fidelity is required.
- **Animation and motion tokens** — no transition durations, easing curves, or micro-interaction specs could be derived without a live session.
