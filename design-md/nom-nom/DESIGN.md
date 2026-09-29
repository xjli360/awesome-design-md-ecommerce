---
version: alpha
name: "Nom Nom"
source_url: "https://nomnomnow.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The homepage opens on dog food photographed like restaurant mise en place — raw chicken thighs, bright carrots, leafy greens arranged with the same care a farm-to-table kitchen gives its seasonal board. Against that visual density, the palette extracted from nomnomnow.com collapses into two tones: a deep warm charcoal (#3d3935) and a neutral border gray (#dcdcdc), with everything else yielding to the food. That charcoal anchors the entire system — it is the ink, the primary CTA ground, and the footer fill — reading as "serious nutrition" rather than "playful pet brand," deliberately distancing Nom Nom from the primary-color brights that crowd the pet aisle shelf. The interface architecture is subscription-first in a way that defers commerce: a breed-and-health-goals quiz precedes any pricing, building a nutritional case before the brand makes its financial ask. This sequencing is as much design strategy as UX — product cards arrive after credibility is established, so the card itself can stay visually spare, leaning on ingredient lists and veterinary claims rather than visual noise. Rounded corners land in the moderate register — {rounded.sm} for buttons and inputs, {rounded.md} for cards — avoiding the pill shapes of pure-lifestyle brands and the hard rectangles of clinical nutrition sites, occupying a zone that reads as clean and trustworthy. Spacing is editorial and open; hero sections and ingredient-story rows deploy full {spacing.section} gaps that let photography breathe without the compressed urgency of a conversion-rate-optimized landing page. Typography almost certainly runs a geometric sans at restrained weights — display copy stays confident without going bold-heavy, because the credibility signal here comes from ingredients and third-party nutrition claims, not typographic volume.

colors:
  primary: "#3d3935"
  primary-active: "#2a2724"
  primary-disabled: "#a09e9b"
  ink: "#3d3935"
  body: "#5a5754"
  muted: "#8c8a87"
  hairline: "#dcdcdc"
  canvas: "#ffffff"
  surface-soft: "#f9f7f5"
  surface-card: "#ffffff"
  surface-strong: "#f0eeed"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.4px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  label-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 52px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 52px
    border: "1.5px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1.5px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    imageAspectRatio: "4/3"
    imageRounded: "{rounded.sm}"
  quiz-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    borderSelected: "2px solid {colors.primary}"
    backgroundSelected: "{colors.canvas}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-sm}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    ctaSpacing: "{spacing.lg}"
  ingredient-badge:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.body}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  nutrition-stat:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.label-sm}"
    valueTypography: "{typography.display-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  plan-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    borderSelected: "2px solid {colors.primary}"
    backgroundSelected: "{colors.surface-soft}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.display-md}"
  trust-badge:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    iconColor: "{colors.body}"
    gap: "{spacing.sm}"
  progress-bar:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-sm}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Full charcoal (#3d3935) fill with white text at 52px height; this is the dominant conversion button appearing at the quiz CTA, the hero "Get started" call, and checkout submission. Hover darkens to `{colors.primary-active}` (#2a2724); disabled renders at `{colors.primary-disabled}` with no label opacity change, keeping the muted state legible. `{rounded.sm}` (8px) keeps the shape assertive without being boxy — the button reads as serious rather than friendly.

**`button-secondary`** — Outline variant on `{colors.canvas}` with a 1.5px `{colors.ink}` border, matching primary at 52px height and `{typography.button-md}` weight so the two sit visually at parity in side-by-side plan-comparison layouts. Used for secondary paths like "Learn more," "Compare recipes," or modal dismissals.

**`button-ghost`** — Transparent background, charcoal label, no border; reserved for inline text-adjacent actions such as "See all ingredients" within product detail sections or "Skip" within the quiz. Inherits `{rounded.sm}` to stay consistent with the broader button family.

### Text Input

**`text-input`** — Clean white field, 1px `{colors.hairline}` border at rest sharpening to 1.5px `{colors.ink}` on focus. No floating label — placeholder text clears on type. 48px height, `{rounded.sm}`, `{typography.body-md}` inside. Used primarily in the quiz flow for dog name, weight, and zip code fields, and in the newsletter capture in the footer.

### Nav Bar

**`nav-bar`** — White bar at 72px with a 1px `{colors.hairline}` bottom rule that holds the boundary on scroll. Logo sits left; primary navigation links at `{typography.nav-link}` (15px/500) run center-right; a filled `button-primary` "Get started" sits at the far right. On mobile, secondary links collapse to a hamburger with a full-viewport slide-in overlay on `{colors.canvas}`.

### Product Card

**`product-card`** — Sits on `{colors.surface-card}` with a 1px `{colors.hairline}` border and `{rounded.md}` (12px) corners. The top image zone occupies a 4:3 aspect ratio with `{rounded.sm}` applied to the image block independently. Below the break: protein source in `{typography.title-md}`, a brief descriptor at `{typography.body-sm}`, then an ingredient-badge row. Cards within plan-selector pages include a sub-row for calories per day and protein percentage.

### Quiz Card

**`quiz-card`** — Multi-choice answer tile in the dog-profile onboarding flow. Rests at `{colors.surface-soft}` background with a `{colors.hairline}` border; on selection the border swaps to 2px `{colors.primary}` and the background lifts to `{colors.canvas}`. `{rounded.md}` throughout, `{spacing.xl}` internal padding. Title set in `{typography.title-sm}`. Options may carry a small illustration or breed silhouette in the upper corner.

### Hero Section

**`hero-section`** — Full-width section on `{colors.surface-soft}` with `{spacing.section}` vertical padding on both sides. Headline in `{typography.display-xl}` (52px/700) sits above a supporting body paragraph in `{typography.body-md}`. The primary CTA button follows with `{spacing.lg}` gap below the body copy. On desktop, food photography occupies the right 50% of the split; on mobile, the image stacks beneath the text block at full width.

### Ingredient Badge

**`ingredient-badge`** — Small chip in `{colors.surface-strong}` with `{rounded.xs}` (4px) corners and `{typography.label-sm}` (11px/700/uppercase). Appears in horizontal wrapping rows below product card titles and within nutrition detail sections. Labels name single ingredients: "CHICKEN," "SPINACH," "SWEET POTATO." Label only, no icon. Not interactive — informational display component.

### Nutrition Stat

**`nutrition-stat`** — A card-within-card block surfacing a single macro metric: label in `{typography.label-sm}` (uppercase), value large in `{typography.display-md}` (28px/600). White background, 1px `{colors.hairline}` border, `{rounded.sm}`. Used in a 3- or 4-column grid within product detail to display protein percentage, fat percentage, moisture content, and calorie density per cup.

### Plan Selector

**`plan-selector`** — Subscription tier picker rendered as a card row. Each option sits on `{colors.canvas}` with `{colors.hairline}` border at rest; the selected tier applies a 2px `{colors.primary}` border and `{colors.surface-soft}` background tint. `{rounded.md}` corners, `{spacing.xl}` internal padding. Plan name in `{typography.title-md}`, price in `{typography.display-md}`. A sub-line at `{typography.body-sm}` shows delivery cadence (e.g., "Ships every 2 weeks").

### Trust Badges

**`trust-badge`** — Horizontal icon-and-label pairs in `{colors.muted}` text at `{typography.caption}` (12px/500). Icons drawn in `{colors.body}`. Appears as a horizontal row directly beneath the hero CTA to surface claims like "Vet-designed recipes," "No artificial preservatives," and "Free shipping on every order." Icon-to-label gap at `{spacing.sm}`.

### Progress Bar

**`progress-bar`** — 4px track in `{colors.hairline}`, fill in `{colors.primary}`, `{rounded.full}` caps on both track and fill. Spans the full viewport width as a step-progress indicator pinned to the top of the quiz flow. Fill percentage advances with each completed question; transitions are CSS-animated at ~300ms ease-out.

### Footer

**`footer`** — Full-width dark footer filling with `{colors.primary}` (#3d3935), white text and links at `{colors.on-dark}`. `{spacing.section}` top and bottom padding. Section header labels in `{typography.label-sm}` (uppercase); link text and body copy in `{typography.body-sm}`. Four-column layout on desktop (Shop, Learn, Company, Connect) collapses to tap-to-expand accordion on mobile. Includes white social icons, a newsletter email input, and the Nom Nom wordmark repeated at reduced scale.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; nav collapses to hamburger overlay; hero image stacks below copy; product cards in 1-up vertical scroll; quiz cards stack full-width; nutrition stats in 2×2 grid |
| Tablet | 744–1128px | 2-column product grid; hero retains side-by-side split at reduced padding; plan selector in 2-column row; nav shows logo and CTA only, hides secondary links |
| Desktop | 1128–1440px | 3-column product grid; hero at full 50/50 split; 4-column nutrition stat grid; plan selector 3-up; footer 4-column |
| Wide | > 1440px | Content max-width 1280px centered; hero photography scales within fixed column; no additional layout changes |

### Touch Targets

- Primary and secondary buttons minimum 52px height; full-width on mobile viewports
- Quiz card tap targets span the full card face — not just the label text — minimum 56px height per option
- Nav overlay links minimum 48px tap height
- Ingredient badges are informational only and not interactive; trust-badge icon pairs minimum 24px if linked

### Collapsing Strategy

- Nav secondary links collapse at 1128px; hamburger overlay activates at 744px using `{colors.canvas}` background
- Product card grid steps: 3-col at 1128px+ → 2-col at 744–1128px → 1-col below 744px
- Footer columns collapse to accordion below 744px; section headers become tap-to-expand triggers
- Quiz option grid: 2-column at 480–744px, single column below 480px
- Nutrition stat grid: 4-col → 2-col at 744px; hero section padding scales from `{spacing.section}` to `{spacing.xl}` on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only 2 hex values extracted (#3d3935, #dcdcdc); the full color system almost certainly loads via JavaScript or Shopify's CDN asset pipeline — accent colors for success states, error validation, promotional highlights, and hover treatments were not captured and are inferred from brand positioning
- No font families detected; all typography tokens fall back to a system sans-serif stack — actual brand typefaces (likely a licensed geometric sans) must be verified against the live site's network panel or brand asset kit
- Primary CTA color uncertainty: #3d3935 is assigned as primary based on extraction ranking, but Nom Nom may use a warmer accent (amber, orange, or green) for CTA buttons that was not captured — confirm by inspecting the live "Get started" or "Build your plan" button element
- Illustration and iconography style not captured — Nom Nom uses custom breed illustrations and iconography in the quiz flow; line weight, color palette, and fill vs. outline style are unknown
- Dark mode support and `prefers-color-scheme` variants not confirmed from extraction
- Promotional banner and announcement bar styling (background color, typography, dismissal behavior) not extracted
- Mobile navigation overlay animation timing and easing not confirmed
