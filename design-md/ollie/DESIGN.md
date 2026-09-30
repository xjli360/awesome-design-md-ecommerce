---
version: alpha
name: "Ollie"
source_url: "https://ollie.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep aubergine (#4c0f51) split against electric chartreuse (#f5fa67) — that's the first thing that registers on ollie.com, a pairing borrowed more from late-night editorial design than from the earth-toned pet-food aisle. The brand treats its dogs like gourmets and its typography like a magazine: New Spirit Condensed carries the big headlines at compressed, towering proportions while ABC Social handles every workhorse paragraph with clean geometric neutrality. A third typeface, Shadows Into Light, drops in as a handwritten flourish — a lowercase scrawl that signals warmth without leaning on stock illustration. The canvas defaults to warm cream (#feffdf) rather than stark white, which keeps the aubergine from reading as corporate and makes the chartreuse feel edible rather than neon. Soft lavender (#f1ccff) fills panel backgrounds and badge surfaces, pulling the tension out of the primary/accent pairing and giving the page somewhere to breathe. The overall shape language is generously rounded — pill-shaped CTAs at `{rounded.full}`, plan cards at `{rounded.xl}` — a choice that echoes the soft curves of dog ears rather than the hard geometry of a pharma formulary. ABC Social Condensed compresses ingredient labels and plan summaries into dense, scannable blocks; ABC Social Mono handles nutritional data and weight specifications with clinical precision that underscores the brand's human-grade sourcing claims. Color application follows a strict hierarchy: aubergine (#4c0f51) owns every primary CTA and hero background, chartreuse (#f5fa67) fires only on promotional callouts and hover states to preserve its urgency, and lavender (#f1ccff) soaks the secondary surface tier. The near-black ink (#2c2a26) pulls warm-brown rather than cool-gray, staying legible against the cream canvas without the coldness of pure black.

colors:
  primary: "#4c0f51"
  primary-active: "#3d0440"
  primary-disabled: "#c4a3c8"
  accent-volt: "#f5fa67"
  accent-lavender: "#f1ccff"
  ink: "#2c2a26"
  body: "#595954"
  muted: "#72726e"
  hairline: "#e0dbd5"
  canvas: "#feffdf"
  surface-soft: "#f3f4f6"
  surface-card: "#ffffff"
  on-primary: "#feffdf"
  on-volt: "#2c2a26"

typography:
  display-xl:
    fontFamily: "'New Spirit Condensed', serif"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -1px
  display-lg:
    fontFamily: "'New Spirit Condensed', serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'New Spirit Condensed', serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'New Spirit Condensed', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0
  title-md:
    fontFamily: "'ABC Social', 'Adjusted Arial Fallback', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'ABC Social', 'Adjusted Arial Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'ABC Social', 'Adjusted Arial Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'ABC Social', 'Adjusted Arial Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'ABC Social', 'Adjusted Arial Fallback', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-condensed:
    fontFamily: "'ABC Social Condensed', 'Adjusted Arial Narrow Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  mono-data:
    fontFamily: "'ABC Social Mono', 'Adjusted Courier New Fallback', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  script-flourish:
    fontFamily: "'Shadows Into Light', cursive"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'ABC Social', 'Adjusted Arial Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.01em
  button-sm:
    fontFamily: "'ABC Social', 'Adjusted Arial Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.01em
  nav-link:
    fontFamily: "'ABC Social', 'Adjusted Arial Fallback', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1
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
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-volt:
    backgroundColor: "{colors.accent-volt}"
    textColor: "{colors.on-volt}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 52px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 26px
    height: 52px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1.5px
    rounded: "{rounded.md}"
    padding: 12px 16px
    typography: "{typography.body-md}"
    focusBorderColor: "{colors.primary}"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.full}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    badgeBackgroundColor: "{colors.accent-lavender}"
    badgeTextColor: "{colors.primary}"
    badgeTypography: "{typography.label-condensed}"
    badgeRounded: "{rounded.full}"
    shadow: "0 2px 12px rgba(44,42,38,0.08)"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    scriptAccentTypography: "{typography.script-flourish}"
    ctaBackgroundColor: "{colors.accent-volt}"
    ctaTextColor: "{colors.on-volt}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.full}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
  freshness-badge:
    backgroundColor: "{colors.accent-volt}"
    textColor: "{colors.on-volt}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  trust-badge:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.primary}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  plan-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    borderColor: "{colors.hairline}"
    borderWidth: 1.5px
    selectedBorderColor: "{colors.primary}"
    selectedBorderWidth: 2px
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.display-md}"
    detailTypography: "{typography.body-sm}"
    monoDetailTypography: "{typography.mono-data}"
  ingredient-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.base}"
  testimonial-card:
    backgroundColor: "{colors.accent-lavender}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    quoteMarkColor: "{colors.primary}"
    quoteMarkTypography: "{typography.display-md}"
  nutrition-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.label-condensed}"
    cellTypography: "{typography.mono-data}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
  quiz-step:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    scriptAsideTypography: "{typography.script-flourish}"
    optionBackgroundColor: "{colors.accent-lavender}"
    optionTextColor: "{colors.primary}"
    optionTypography: "{typography.title-sm}"
    optionRounded: "{rounded.lg}"
    progressDotColor: "{colors.accent-volt}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-lavender}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"

## Components

### Buttons

**`button-primary`** — Pill-shaped (`{rounded.full}`) with aubergine (#4c0f51) fill and warm cream (#feffdf) text, 52px tall with 28px horizontal padding. Active state deepens to #3d0440; disabled washes to a muted lavender-gray (#c4a3c8). This is the subscription and checkout CTA used throughout the purchase funnel.

**`button-volt`** — Identical pill geometry to `button-primary` but filled with chartreuse (#f5fa67) and paired with dark ink (#2c2a26) text for legibility. Reserved for hero-level urgency — "Get Started," limited-time promotions, and inline hero CTAs — where the electric yellow-green against the aubergine background creates maximum contrast. Use sparingly; its power depends on scarcity.

**`button-secondary`** — Transparent background with a 2px aubergine border and aubergine text, pill-shaped at the same 52px height. Appears alongside `button-primary` for secondary actions like "Learn More" or "See Our Recipes," maintaining the pill geometry system without competing for visual priority.

**`button-ghost`** — No border, no background, underlined ink (#2c2a26) text in button-sm scale. Used for tertiary navigation, account flows, legal links, and drawer close actions.

### Navigation

**`nav-bar`** — 64px-tall cream (#feffdf) bar with the Ollie wordmark in aubergine at left, primary navigation links centered in ABC Social nav-link weight, and a pill-shaped "Get Started" CTA at right with aubergine fill. A 1px warm hairline (#e0dbd5) separates the bar from page content. On scroll, the bar acquires a soft drop shadow rather than a color change, preserving the cream identity.

### Product & Plan Cards

**`product-card`** — White surface (`{rounded.lg}`, 20px radius) with 24px padding and a soft warm shadow. Recipe or meal name in title-md ABC Social Semibold; supporting descriptors in body-sm. A lavender (#f1ccff) pill badge in the upper corner ("Vet Approved," "Fan Favorite") uses label-condensed all-caps with aubergine text. No hard border in default state.

**`plan-card`** — Cream canvas background at `{rounded.xl}` (32px radius), 1.5px hairline border at rest that upgrades to 2px aubergine on selection. Price rendered in New Spirit Condensed at display-md scale; per-serving nutritional breakdowns in ABC Social Mono for columnar legibility. A selected card gains a thin aubergine left-edge accent. Plan cards stack two-per-row on tablet and three-per-row on desktop.

### Hero

**`hero`** — Full-bleed aubergine (#4c0f51) background with New Spirit Condensed display-xl headline in cream (#feffdf). Chartreuse (#f5fa67) handles highlight words or the primary CTA button to create maximum voltage against the purple field. A Shadows Into Light script gloss can annotate a headline word as a warm handwritten aside. Minimum 560px tall; text left-aligned with product photography bleeding from the right half.

### Badges

**`freshness-badge`** — Chartreuse (#f5fa67) pill with dark ink text in label-condensed uppercase. Applied to new recipes, seasonal drops, and limited-availability SKUs to borrow the accent's urgency signal.

**`trust-badge`** — Lavender (#f1ccff) pill with aubergine text in label-condensed uppercase. Used for credentialing claims — "Human-Grade," "USDA Inspected," "Vet Recommended" — where authority must register without triggering primary-CTA associations.

### Quiz / Onboarding

**`quiz-step`** — Full-viewport aubergine panels that guide users through the dog profile builder. Headline in New Spirit Condensed display-md in cream; a Shadows Into Light script aside sits beneath the headline as a warm parenthetical ("because every pup is different"). Selection options appear as lavender (#f1ccff) rounded tiles (`{rounded.lg}`) with aubergine text in title-sm. Chartreuse progress dots track step position along the bottom.

### Testimonials

**`testimonial-card`** — Lavender (#f1ccff) surface at `{rounded.lg}` with 32px padding. Quote body in body-md ink text; author attribution in caption-scale muted gray (#72726e). An oversized aubergine quotation mark in New Spirit Condensed display-md anchors the top-left corner as a structural glyph rather than decoration.

### Nutrition Table

**`nutrition-table`** — White card container at `{rounded.md}`. Aubergine header row with cream label-condensed column titles; cell content in ABC Social Mono mono-data for column-aligned decimal legibility. Row hairlines at 1px warm gray (#e0dbd5). Scrolls horizontally on mobile rather than collapsing columns.

### Ingredient Tags

**`ingredient-tag`** — Light gray (#f3f4f6) soft-square chips at `{rounded.sm}` with body-colored label-condensed uppercase text. Used in recipe detail views to enumerate protein sources, vegetables, and supplements in compact scannable clusters.

### Footer

**`footer`** — Full-width deep aubergine (#4c0f51) block. Section headings in ABC Social title-sm in cream; navigation and legal links in lavender (#f1ccff) with underline on hover. No top border — the aubergine creates its own hard edge against the preceding cream or soft-gray content section. Social icons render in cream at 20px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger with full-screen aubergine drawer; hero headline drops to display-md scale; plan cards and product cards stack vertically; quiz steps go full-viewport; primary buttons expand to 100% container width; nutrition tables scroll horizontally |
| Tablet | 744–1128px | Two-column product grid and plan card grid; nav shows condensed links without the CTA pill (pill moves into hamburger); hero uses split layout at display-lg headline scale; testimonials display 2-up |
| Desktop | 1128–1440px | Three-column product grid; full nav with CTA pill; hero at display-xl with full image bleed; quiz uses centered split-panel at 50/50; footer in 4-column grid |
| Wide | > 1440px | Content max-width ~1280px centered with increased lateral padding; hero padding scales up; New Spirit Condensed display can push to 80–96px; section spacing increases by ~25% |

### Touch Targets

- All pill buttons maintain minimum 52px height on all breakpoints
- Quiz selection tiles minimum 56px tall on mobile to prevent mis-taps
- Nav hamburger icon minimum 44×44px tap zone
- Product card and plan card tap targets cover the full card surface
- Form inputs minimum 48px height on mobile

### Collapsing Strategy

- Nutrition tables scroll horizontally on mobile rather than reflowing columns
- Ingredient tag clusters truncate at 3 rows with a "+N more" disclosure pill in `{colors.accent-lavender}`
- Testimonial grid collapses from 3-column → 1-column swipeable carousel with chartreuse dot pagination on mobile
- Footer navigation sections collapse into accordions on mobile (aubergine headers, lavender chevron toggle)
- Primary nav links hidden behind hamburger below 744px; cart and account icons remain visible in the top-right at all widths

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hairline color (#e0dbd5) not present in extracted palette — derived as a warm-beige complement to the cream canvas (#feffdf); verify against actual CSS border tokens
- Primary-disabled color (#c4a3c8) not extracted — interpolated between primary (#4c0f51) and white; actual disabled state may use opacity instead
- Font weights for New Spirit Condensed not confirmed from extraction; 700/600 assumed from visual headline weight
- Exact nav bar height not extracted; 64px is inferred from standard Shopify theme patterns
- Card shadow values (0 2px 12px rgba(44,42,38,0.08)) estimated — actual elevation tokens not accessible from static extraction
- Hover/focus animation timing (button scale, card lift) not extractable from static snapshot
- Dark mode or high-contrast theme variants not observed; unknown whether the brand supports them
- Exact letter-spacing and line-height values for New Spirit Condensed display sizes require live CSS inspection to confirm
