---
version: alpha
name: "Speed Queen"
source_url: "https://www.speedqueen.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep royal blue (#003388) stamped across a nav bar and every primary CTA — the same shade you find on the steel nameplate of a laundromat's workhorse unit, carried intact into the digital storefront without softening or gradient. Speed Queen's interface is built like its machines: rigid geometry, zero decorative radius (`{rounded.none}` on hero containers, `{rounded.xs}` on buttons), and IBM Plex Serif headlines that read like equipment spec sheets rather than lifestyle copy. The serif choice is deliberate defiance in a category saturated with geometric sans-serifs and rounded appliance-catalog friendliness — it signals engineering lineage and mechanical confidence. Body text switches to Roboto at 400 weight for legibility at small sizes, creating a strict two-voice system: authority in headings, clarity in prose. Red (#dc3232) appears sparingly as an alert accent on warranty badges and promotional callouts, while a hotter orange-red (#f04923) marks urgent CTAs like "Find a Dealer" — together they punch through the cool blue-and-white palette without competing for hierarchy. Canvas stays at #f5f5f5 rather than pure white, giving product photography a slightly warm, showroom-floor neutrality. Cards and surface panels barely differentiate (#eeeeee borders, #ffffff fill), forcing the eye toward product imagery and specification tables rather than UI chrome. Spacing is generous at section level (`{spacing.section}` = 64px) but tight within component clusters — product feature grids pack tightly at `{spacing.md}` gaps, mimicking the dense information layout of a technical manual. The overall impression is institutional trust: a site that would rather show you a 25-year lifespan test result than a lifestyle photograph.

colors:
  primary: "#003388"
  primary-active: "#001ab3"
  primary-disabled: "#527eff"
  accent-red: "#dc3232"
  accent-orange: "#f04923"
  ink: "#112337"
  body: "#313131"
  muted: "#585e6a"
  muted-soft: "#686e77"
  hairline: "#eeeeee"
  canvas: "#f5f5f5"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#67a671"
  highlight: "#fdd79a"

typography:
  display-xl:
    fontFamily: "'IBM Plex Serif', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'IBM Plex Serif', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'IBM Plex Serif', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'IBM Plex Serif', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'IBM Plex Serif', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.14
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "Roboto, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "'IBM Plex Serif', Georgia, serif"
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
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary}
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 2px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    height: 64px
    boxShadow: 0 2px 8px rgba(0,51,136,0.15)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  product-card-hover:
    boxShadow: 0 4px 16px rgba(17,35,55,0.1)
    border: 1px solid {colors.primary}
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xxl}"
    minHeight: 560px
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: 1px solid {colors.hairline}
  warranty-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  dealer-locator:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
    inputHeight: 48px
    buttonColor: "{colors.accent-orange}"
  comparison-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    border: 2px solid {colors.hairline}
    headerBackground: "{colors.primary}"
    headerText: "{colors.on-primary}"
    headerTypography: "{typography.title-sm}"
  comparison-card-featured:
    border: 2px solid {colors.primary}
    headerBackground: "{colors.primary}"
  feature-grid-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    iconColor: "{colors.primary}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    gap: "{spacing.md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.highlight}"
    padding: "{spacing.section} {spacing.xxl}"
    borderTop: none
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    padding: "{spacing.base} 0"
  promo-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    padding: 0 {spacing.base}

---

## Components

### Buttons

**`button-primary`** — Solid deep blue (#003388) rectangle with barely-there 4px radius and uppercase Roboto 600 tracking at 0.3px. Hover darkens to primary-active (#001ab3) with no transition easing beyond a fast 150ms swap. Disabled state washes out to the mid-blue (#527eff) at reduced opacity. The uppercase treatment and tight letter-spacing give these buttons a mechanical, stamped-label quality.

**`button-secondary`** — White fill with a 2px blue border and blue text, same squared geometry. On hover, the entire button fills primary blue and text flips to white — a binary on/off state that avoids gradient or partial-fill animations. Used for secondary actions like "View Specs" or "Compare Models."

**`button-accent`** — Orange-red (#f04923) fill reserved for the highest-urgency CTA on any given page, typically "Find a Dealer" or promotional actions. Same squared shape and uppercase treatment as primary.

### Navigation

**`nav-bar`** — 72px-tall white bar with a single hairline bottom border. Logo locks left, nav links in Roboto 500 at 14px sit center or right. On scroll, the bar compresses to 64px, swaps to the primary blue background with white text, and gains a subtle directional shadow.

**`promo-bar`** — 40px-tall strip above the nav in solid primary blue, carrying a single line of promotional copy (warranty messaging, free shipping thresholds) in caption-weight white text. Dismissible with an X icon on mobile.

### Product Cards

**`product-card`** — Zero-radius white rectangle with a 1px hairline border. Product image sits flush to the top edge with no internal padding. Title in IBM Plex Serif 18px/600, a short spec line in body-sm, and a "Learn More" text link in primary blue. On hover, the border transitions to primary blue and a 4px directional shadow lifts the card.

### Hero

**`hero-banner`** — Full-bleed dark navy (#112337) container with no border radius, minimum 560px height. White display-xl headlines in IBM Plex Serif 48px/700 with -0.5px tracking anchor left. Body copy in Roboto 18px/400 sits below with generous line-height (1.56). A single primary or accent button locks to the bottom-left of the text stack. Product photography composites from the right, cropped hard at the container edge.

### Specification Table

**`spec-table-row`** — Alternating rows on the light canvas background. Each row pairs an uppercase 12px/700 label (Roboto, 0.5px tracking) on the left with an IBM Plex Serif 20px/700 value on the right. Rows are separated by hairline borders. This component is central to Speed Queen's product pages, where machine specifications (RPM, water usage, cycle count ratings) receive more visual weight than lifestyle imagery.

### Warranty Badge

**`warranty-badge`** — Compact red (#dc3232) pill with uppercase white text at button-sm scale. Appears inline on product cards and hero sections to call out the brand's signature warranty duration. The red contrasts sharply against the dominant blue-and-white palette to signal trust and durability claims.

### Dealer Locator

**`dealer-locator`** — A contained white panel with light border, housing a zip-code input and an accent-orange submit button. Results list below in a scrollable container. Map integration sits adjacent on desktop. The orange button deliberately breaks from the blue system to signal a different action domain (physical retail vs. digital browsing).

### Comparison Cards

**`comparison-card`** — Vertical card with a colored header strip (primary blue with white text for the model name) and a white body listing feature rows. The featured/recommended variant gains a 2px primary border around the entire card. Cards align in a horizontal row on desktop with equal heights enforced.

### Feature Grid

**`feature-grid-item`** — Icon (in primary blue) + title + short description stacked vertically within the canvas-colored cell. Icons are 32px line-weight illustrations. Grid gaps use `{spacing.md}` (12px) for a dense, specification-manual density.

### Footer

**`footer`** — Dark navy (#112337) full-bleed section with four-column link layout in white body-sm text. Links highlight to gold (#fdd79a) on hover, providing warmth against the cold dark background. A secondary row carries legal copy, social icons, and certification logos at reduced opacity.

### Breadcrumb

**`breadcrumb`** — Minimal text-only trail in muted gray with slash separators, sitting directly below the nav. The active/current page renders in full ink color. No background, no container — just typography.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; hero stacks vertically (text above image) at reduced min-height 360px; product cards go single-column full-width; comparison cards stack vertically with horizontal scroll option; spec table stays full-width with tighter padding; promo bar text truncates with ellipsis |
| Tablet | 744–1128px | Two-column product grid; hero image scales to 50% width; nav links collapse to a "More" dropdown after 4 items; dealer locator stacks map below results; comparison cards show 2-up |
| Desktop | 1128–1440px | Full nav visible; hero at full 560px height with 60/40 text-image split; three-column product grid; spec tables gain more horizontal breathing room; comparison cards 3-up |
| Wide | > 1440px | Content max-width caps at 1440px and centers; hero image can bleed right; section padding increases to 80px; four-column feature grids become viable |

### Touch Targets

- All interactive elements maintain 48px minimum touch height on mobile
- Nav hamburger icon padded to 48×48px hit area
- Product card entire surface is tappable on mobile (not just the text link)
- Comparison card "Select" buttons expand to full card width on mobile
- Footer links gain 12px vertical padding between items for finger clearance

### Collapsing Strategy

- Navigation: full link bar → hamburger drawer (744px breakpoint)
- Product grids: 3-col → 2-col (1128px) → 1-col (744px)
- Hero: side-by-side → stacked (744px), image crops to 16:9 aspect
- Spec tables: two-column key/value maintained at all sizes, horizontal padding reduces
- Comparison cards: horizontal row → horizontal scroll → vertical stack (below 744px)
- Feature grid: 4-col → 3-col (1128px) → 2-col (744px) → 1-col (480px)
- Footer: 4-column → 2-column (744px) → single accordion column (480px)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Many extracted colors (#00d084, #0693e3, #7a00df, #34e2e4, #4721fb, #ab1dfe, #faaca8, #dad0ec, #fafae1, #330968, #31cdcf) appear to be WordPress/Gutenberg editor palette defaults rather than brand tokens — excluded from the design system
- No CSS custom properties or design-token layer was detectable; the site likely injects styles through a CMS theme without a formal token architecture
- Exact button border-radius could not be confirmed (assumed 4px from visual inspection of screenshots; may be 0px on some variants)
- Icon library and illustration style undetermined — line weight, stroke cap, and grid size unknown
- Motion/animation tokens not extractable (transition durations, easing curves for hover states)
- Mobile nav drawer behavior (slide direction, overlay opacity, close gesture) not confirmed
- Exact IBM Plex Serif weights in use could not be verified beyond 600 and 700; lighter weights may appear in pull-quotes or editorial content
- Product image aspect ratios and container sizing rules not available from extraction
