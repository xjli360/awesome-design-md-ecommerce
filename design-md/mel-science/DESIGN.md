---
version: alpha
name: "Mel Science"
source_url: "https://www.melscience.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A bright yellow cardboard box (#ffd040) — the color of a Van de Graaff discharge, of sodium flame tests, of warning tape repurposed as delight — arrives at a child's door and immediately announces that the contents are not homework. MEL Science constructs its entire visual identity around this single voltage: #ffd040 appears on every primary CTA, subscription tier callout, and kit photography corner, functioning as both excitement signal and brand fingerprint rather than a conventional "buy" button color. The canvas defaults to clean white with a near-white surface treatment (#f3f3f3 from meta), giving chemistry photographs and 3D molecular renders the neutral backdrop they need without color cast or visual noise. Display type sits bold and heavy — geometric sans proportions at sizes that lean into the confidence that science is not a difficult subject but an entertaining one. Corners are consistently soft throughout the system: product cards, subscription panels, and experiment badges all favor {rounded.md} to {rounded.lg} radii, deliberately avoiding the hard-edged rectangles of textbook convention. Age-range chip badges (8+, 10+, 14+) use {rounded.full} pill forms in the primary yellow, letting parents scan kit complexity in a single glance. Section pacing is generous — photography and 3D render illustration breathe at {spacing.section} margins, keeping the site reading as a science magazine rather than a standard e-commerce grid. The subscription pitch rides on a CTA architecture that stacks kit discovery above plan selection, with the yellow button functioning as the visual terminus of each content band. On mobile the yellow CTA stretches full-width, maintaining subscription urgency even at the smallest viewport.

colors:
  primary: "#ffd040"
  primary-active: "#d4a800"
  primary-disabled: "#fff4b8"
  ink: "#111111"
  body: "#333333"
  muted: "#777777"
  hairline: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#111111"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 52px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  age-chip:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 800
    lineHeight: 1
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  subscription-price:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 800
    lineHeight: 1
    letterSpacing: -0.5px

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
    rounded: "{rounded.lg}"
    padding: 14px 28px
    height: 52px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.lg}"
  button-primary-full:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    width: 100%
    height: 52px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 13px 27px
    height: 52px
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    border: "1.5px solid {colors.hairline}"
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
    paddingX: "{spacing.xl}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.section}"
    ctaButton: "{components.button-primary}"
    imageRadius: "{rounded.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    imageRadius: "{rounded.md}"
  age-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.age-chip}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  subject-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  subscription-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
    priceTypography: "{typography.subscription-price}"
    border: "2px solid {colors.hairline}"
  subscription-card-featured:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xxl}"
    priceTypography: "{typography.subscription-price}"
    border: none
  experiment-kit-strip:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.caption}"
    imageRadius: "{rounded.md}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid transparent"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  experiment-counter-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    paddingY: "{spacing.section}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    height: 48px
    border: none
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    height: 48px
    padding: "0 24px"

## Components

### Buttons

**`button-primary`** — The primary CTA uses the brand's full-voltage yellow (#ffd040) with dark `{colors.on-primary}` text for accessibility. Corners sit at `{rounded.lg}` (20px), softer than a typical e-commerce button but short of pill, landing in a friendly-but-purposeful range. Hover darkens to `{colors.primary-active}` (#d4a800); the disabled state bleaches to `{colors.primary-disabled}` with muted text. On mobile, a full-width variant (`button-primary-full`) spans the container to maximize the subscription conversion surface.

**`button-secondary`** — White fill with a 2px dark ink border and matching `{rounded.lg}` radius. Used for secondary actions like "Learn more" or "See all kits" alongside a primary yellow CTA. Hover state typically adds a light `{colors.surface-soft}` fill.

**`button-ghost`** — Plain text with an underline, no border or background. Used for low-stakes navigation links inside content blocks, keeping visual weight off informational text areas.

### Navigation

**`nav-bar`** — White canvas bar at 68px height, 1px hairline bottom border. Logo anchors left; nav links in `{typography.nav-link}` weight 600 span the center or right cluster. A yellow `{components.button-primary}` "Start subscription" CTA anchors the far right. On mobile, the nav collapses to a hamburger, with the CTA promoted to a sticky bottom bar.

### Product & Kit Cards

**`product-card`** — A white card with `{rounded.lg}` corners, subtle hairline border, and `{spacing.base}` internal padding. Kit photography fills the top in a `{rounded.md}` container; `{components.age-badge}` and `{components.subject-badge}` chips sit below the image. Title uses `{typography.title-md}` weight 700; description uses `{typography.body-sm}`. A yellow CTA button anchors the card bottom.

**`age-badge`** — Pill-shaped (#ffd040 background, `{rounded.full}`) chip showing the recommended age range (e.g. "8+"). Text is heavy `{typography.age-chip}` weight 800, dark ink, visible against the yellow. These appear consistently on product cards and in hero contexts to help parents self-select kit complexity.

**`subject-badge`** — Soft gray (`{colors.surface-soft}`) pill in `{typography.badge}` uppercase, labeling the science discipline (Chemistry, Physics, Biology). Pairs with age-badge on every kit card.

### Subscription & Pricing

**`subscription-card`** — Gray-tinted surface card with generous `{rounded.xl}` corners and `{spacing.xxl}` padding. Price rendered in `{typography.subscription-price}` (32px, weight 800). The featured tier flips to a full yellow (`{colors.primary}`) fill, the only component in the system that uses the brand color as a background at card scale. Both variants sit in a horizontal row on desktop, stacking vertically on mobile.

### Hero

**`hero`** — Full-width band on white canvas, `{spacing.section}` vertical padding. Heading uses `{typography.display-xl}` (52px, weight 800) for maximum legibility at a science-toy gift consideration moment. Body copy sits at `{typography.body-md}`. The CTA button is always the full-size `{components.button-primary}`. Photography or animated kit imagery appears right-aligned on desktop in a `{rounded.xl}` container; it drops below the text stack on mobile.

### Experiment Strip

**`experiment-kit-strip`** — A horizontal scrollable band of thumbnail experiment cards on a `{colors.surface-soft}` background, labeled in `{typography.caption}` uppercase. Used on category pages to surface individual experiments within a kit subscription. Each thumbnail is `{rounded.md}`; the strip itself is `{rounded.lg}`.

### Footer

**`footer`** — Dark ink (`{colors.ink}`) full-width band with white `{colors.on-dark}` text. Link clusters in `{typography.body-sm}`, column headings in `{typography.title-sm}` weight 600. Yellow is absent from the footer — the brand reserves it strictly for action surfaces, letting the dark footer read as a visual reset after content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; product cards stack full-width; hero image drops below text; nav collapses to hamburger; primary CTA becomes sticky bottom bar; subscription cards stack vertically |
| Tablet | 744–1128px | Two-column product grid; hero switches to side-by-side text+image; nav links may abbreviate; subscription cards shift to 2-up layout |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with CTA; hero at full `{spacing.section}` padding; subscription cards in 3-up row |
| Wide | > 1440px | Max-width container (~1440px) centered; section padding increases to `{spacing.section}` × 1.5; hero image scales up within fixed container |

### Touch Targets

- All buttons minimum 48px height on mobile
- Age and subject badge chips minimum 36px tap height despite visual compactness
- Nav hamburger menu touch target minimum 44×44px
- Subscription tier cards fully tappable, not just the inner CTA button

### Collapsing Strategy

- Nav: links hidden behind hamburger below 744px; yellow CTA demoted to sticky bottom strip
- Hero: image drops below text on mobile (text-first priority for SEO and scan)
- Experiment-kit-strip: converts from fixed grid to horizontal scroll on mobile with snap points
- Subscription cards: horizontal 3-up collapses to full-width vertical stack with the featured card first

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only 2 hex values were extracted from the live site (#f3f3f3, #ffd040); all other color tokens (ink, body, muted, hairline, on-dark) are inferred from standard accessibility patterns and cannot be confirmed without full site extraction
- No font-family stacks were recovered — the site likely loads typography via JS bundle or a custom font CDN that was filtered as a framework default; all `fontFamily` values above are system-stack placeholders and should be replaced once the brand's actual typeface is identified
- Specific hover, focus, and error state colors for inputs and secondary buttons are inferred, not extracted
- Icon system (experiment category glyphs, navigation icons) not documented — MEL Science likely uses a custom icon set that could not be extracted
- Animation and motion tokens (kit reveal animations, subscription tier transitions) are not documented; the brand likely uses physics-based spring animations on kit imagery
- Exact box-shadow values for elevated cards are not confirmed
- Dark mode support, if any, could not be determined from extraction
