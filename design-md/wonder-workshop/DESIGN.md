---
version: alpha
name: "Wonder Workshop"
source_url: "https://www.makewonder.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Dash and Dot — the round, expressive robots at the center of this brand — are both the product and the visual grammar. The five colors children use to program their robot's LED lights recur as systematic UI tokens throughout the site: coral `#fa5252` drives every primary action, electric green `#4bce61` signals completion and go-states, warm orange `#f26a21` marks creative prompts, cyan `#00acd7` carries informational surfaces, and purple `#8c5aca` flags advanced curriculum pathways. This five-color vocabulary means the retail experience and the play experience share the same perceptual language — a child who has learned to read green as "go" on the robot encounters the same green on the site's success states. Deep navy `#122246` anchors the palette as ink and hero background, giving weight to what could otherwise read as purely juvenile. Against it, the coral `#fa5252` primary CTA achieves maximum contrast, a deliberate accessibility choice for primary-grade visual acuity ranges.

  Bariol — a rounded humanist sans-serif with circular letter apertures — handles every headline; its geometry mirrors the robots' injection-molded bodies without collapsing into cartoon exaggeration. Museo Sans at weights 300 and 500 takes over for body copy, specifications, and grade-level notation, its geometric precision communicating the engineering credibility that parents purchasing classroom kits require. The contrast between the two families creates a readable hierarchy: Bariol announces, Museo Sans explains.

  The canvas sits at near-white `#f6f7f9` rather than pure white, softening prolonged sessions. Product cards lift to `#fdfdfd` against it, creating depth without drop shadows. Hairlines at `#d5d9e2` provide structure without aggression. Corners scale with hierarchy: cards and inputs use `{rounded.md}` at 12px, hero panels use `{rounded.lg}` at 20px, and command-color badges with pill CTAs use `{rounded.full}` — the rounding progression from data to action to identity reads spatially rather than arbitrarily. Age-range and "New" flags use the same colored-fill badge pattern as the robots' status LEDs, collapsing the gap between physical product feedback and digital retail signal.

colors:
  primary: "#fa5252"
  primary-active: "#e03c3c"
  primary-disabled: "#fcc2c2"
  navy: "#122246"
  navy-mid: "#003388"
  success: "#4bce61"
  success-soft: "#eeffee"
  warning: "#f26a21"
  info: "#00acd7"
  accent-purple: "#8c5aca"
  accent-orange: "#ff8a00"
  ink: "#23282d"
  body: "#444444"
  muted: "#697582"
  muted-light: "#8e98a2"
  hairline: "#d5d9e2"
  hairline-soft: "#e9ebf1"
  canvas: "#f6f7f9"
  surface-soft: "#f6f7f8"
  surface-card: "#fdfdfd"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#970000"
  error-soft: "#fff1f1"

typography:
  display-xl:
    fontFamily: "'Bariol Bold', 'Bariol', 'Museo Sans', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Bariol Bold', 'Bariol', 'Museo Sans', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Bariol Bold', 'Bariol', 'Museo Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Museo Sans 500', 'Museo Sans', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Museo Sans 500', 'Museo Sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Museo Sans 300', 'Museo Sans', sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Museo Sans 300', 'Museo Sans', sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Museo Sans 300', 'Museo Sans', sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "'Museo Sans 500', 'Museo Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Bariol Bold', 'Bariol', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Bariol Bold', 'Bariol', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Museo Sans 500', 'Museo Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Museo Sans 500', 'Museo Sans', sans-serif"
    fontSize: 11px
    fontWeight: 500
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
    rounded: "{rounded.xl}"
    padding: 14px 32px
    height: 52px

  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xl}"

  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xl}"

  button-secondary:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: 14px 32px
    height: 52px

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xl}"
    padding: 12px 30px
    height: 52px

  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"

  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"

  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 36px

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    imageAspectRatio: "1:1"

  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xl}"
    rounded: "{rounded.none}"
    minHeight: 520px

  robot-showcase:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    imageMaxWidth: 420px

  command-badge-action:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.badge}"
    padding: 4px 12px

  command-badge-go:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.badge}"
    padding: 4px 12px

  command-badge-create:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.badge}"
    padding: 4px 12px

  command-badge-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.badge}"
    padding: 4px 12px

  command-badge-advanced:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    typography: "{typography.badge}"
    padding: 4px 12px

  age-badge:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  grade-chip:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: 4px 12px

  curriculum-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    borderLeft: "4px solid {colors.primary}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"

  app-download-strip:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    badgeHeight: 40px

  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-light}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"

## Components

### Buttons

**`button-primary`** — Coral `#fa5252` fill with white Bariol Bold text, 32px border radius, 52px height and 32px horizontal padding. Active state darkens to `#e03c3c`; disabled washes to `#fcc2c2` while retaining white text. The 52px height exceeds the 44px touch minimum, accommodating both young learners on classroom tablets and parents browsing on desktop.

**`button-secondary`** — Navy `#122246` fill with white text, identical geometry to the primary, functionally paired on hero sections and product pages where both purchase and learn-more actions need equal visual weight. No border needed given the dark fill against canvas.

**`button-ghost`** — Coral `#fa5252` border and text on transparent background, 2px stroke weight. Used for secondary actions adjacent to a filled CTA — "Watch Demo" next to "Shop Now." The 2px border reads at small sizes without appearing fragile.

### Navigation

**`nav-bar`** — White `#fdfdfd` surface at 64px height with a 1px `#e9ebf1` bottom rule. Logo sits left at 36px height; Museo Sans 500 nav links center; account and cart icons sit right. The thin rule separates nav from page content without casting shadow weight.

### Inputs

**`text-input`** — White card surface, 1.5px `#d5d9e2` border, 12px radius, 48px height to align with button rows in form layouts. Museo Sans 300 at 16px keeps text legible without matching button-text emphasis. Placeholder renders in `#697582` muted.

**`search-bar`** — Full-pill `{rounded.full}` shape distinguishes it from standard inputs and echoes the Dash robot's circular body vocabulary. Icon anchors inside left padding in muted gray `#697582`; the border lightens to `#d5d9e2` on rest and strengthens slightly on focus.

### Product Card

**`product-card`** — White `#fdfdfd` card on the near-white `#f6f7f9` canvas, 1px `#d5d9e2` border, 12px radius. Product image occupies the top half at 1:1 aspect ratio. Below the image: product name in Museo Sans 500 at 16px, age badge (`age-badge`), and price in Museo Sans 500 at 20px. The Add to Cart CTA (`button-primary`) pins to the card bottom.

### Hero Banner

**`hero-banner`** — Full-bleed navy `#122246` with no border radius, Bariol Bold headline at 56px in white. The coral primary CTA achieves maximum contrast against the dark field. Minimum 520px height accommodates a large right-aligned robot product image on desktop; on mobile the image drops below the text block and the section compresses to content height.

### Robot Showcase

**`robot-showcase`** — Canvas-background feature section (`#f6f7f9`) with 20px radius and 48px padding on all sides. A single robot (Dash or Dot) occupies up to 420px image width on the right; the left half carries a Bariol Bold display-md headline and Museo Sans body copy. Used for product-detail feature callouts between the hero and the product grid.

### Command Badges

**`command-badge-*`** — Five pill variants whose colors directly mirror the robots' LED coding colors: coral for action, green for go, orange for create, cyan for info, purple for advanced. White Museo Sans 500 at 11px maintains legibility across all five fills. These badges appear on activity cards, curriculum level indicators, product capability grids, and the coding app feature list — the visual continuity between physical robot and digital context is the defining brand move.

### Age & Grade Badges

**`age-badge`** — Hairline-soft `#e9ebf1` background with all-caps Museo Sans 500 at 12px in muted gray `#697582`, 4px radius. Communicates "Ages 6–11" at a glance on product cards for parent purchasers. **`grade-chip`** — Navy full-pill with white uppercase label, 12px Museo Sans 500. Used in the curriculum section for "Grades K–5" designations where the navy matches the section's authority register.

### Curriculum Card

**`curriculum-card`** — White card with a 4px coral `#fa5252` left-border accent, 12px radius, 1px overall border. The left accent visually distinguishes curriculum content from product cards sharing the same canvas. Title renders in Museo Sans 500 at 16px; supporting body in Museo Sans 300 at 14px.

### App Download Strip

**`app-download-strip`** — Navy `#122246` section bar at 12px radius with 24px padding. App Store and Google Play badge images render at 40px height with supporting white body text. Appears in the footer approach zone and on robot product pages to drive companion-app adoption.

### Footer

**`footer`** — Navy `#122246` background, multi-column layout on desktop. Section headings in Museo Sans 500 at 16px in white; links in Museo Sans 300 at 14px in `#8e98a2`. Social icons and legal links sit in a bottom strip within the same navy field.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero stacks image below text block; product grid becomes 1-column; command badges wrap; hero min-height reduces to content height |
| Tablet | 744–1128px | 2-column product grid; nav shows primary links with secondary links in overflow drawer; hero splits text left / image right at reduced image size; robot-showcase stacks vertically |
| Desktop | 1128–1440px | 3-column product grid; full nav visible; hero splits 50/50 with Bariol Bold at full 56px; robot-showcase side-by-side with 420px image |
| Wide | > 1440px | Content caps at 1440px max-width; hero horizontal padding expands; product grid may expand to 4 columns; section padding scales from 64px to 80px |

### Touch Targets

- All interactive elements meet 44×44px minimum tap area
- Command badges receive increased padding on mobile (`padding: 8px 16px`) to ensure 44px tap height
- Nav hamburger button is 44×44px hit area regardless of visible icon size
- Product card CTA button occupies full card width on mobile for reliable tap

### Collapsing Strategy

- Primary nav collapses below 744px; first-level category links move to a slide-in drawer
- Footer columns stack vertically on mobile with accordion expand for each link group
- Robot showcase image drops below text block on mobile and tablet
- App download strip badges reflow to a single centered column on mobile
- Curriculum cards remain single-column across all breakpoints (content density is intentional)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Box-shadow values for elevated states (modals, cart drawer, dropdowns) not captured — site likely uses subtle `rgba(0,0,0,0.08)` shadows not recoverable from color extraction
- Hover and focus transition timing curves (duration, easing) not observable from static extraction
- Sale and discount badge color treatment not confirmed — likely `#f26a21` warning orange or `#fa5252` coral, but specific badge component not verified
- Animation values for robot product demo sequences (spin, LED pulse, movement paths) not extractable
- Custom icon set scope unclear — FontAwesome and dashicons present in stack, but a brand-specific robot/coding icon family may exist beyond these
- Exact line-height and letter-spacing values for Bariol at sub-20px sizes not confirmed; values above are derived from Bariol's general optical metrics
- Dark mode support: not determinable from extraction; no `prefers-color-scheme` tokens observed
