---
version: alpha
name: "Joylux"
source_url: "https://joylux.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Coral (#ec523e) pulled against a near-black base (#121212) is Joylux's central design argument: that a medical-grade pelvic floor light therapy device can be sold with the same warmth and directness as premium skincare. The brand runs Work Sans at 600–700 weight for all display copy, giving headlines a confident upward lean that avoids both the sterility of a clinical typeface and the softness of a lifestyle script. Body copy shifts to Assistant — slightly rounder, more conversational — bridging efficacy language and empathetic storytelling. The pairing can hold "FDA-cleared" and "feel like yourself again" in the same scroll without tonal whiplash.

  The color story unfolds across three registers. Warm darks (#121212, #202020) anchor the hero and navigation, establishing a premium tone that prevents the brand from drifting into pastel-bland wellness territory. The coral primary (#ec523e) activates every CTA and product highlight, deepening to rose (#b43145) on hover. A blush surface (#ffefee) appears behind testimonials and feature callouts, diffusing the dark/coral contrast into something closer to a living room than a laboratory. Slate gray (#5f6772) handles secondary labels and descriptive copy — specific enough to feel designed, neutral enough to never fight the coral.

  Corners settle in a moderate range: `{rounded.md}` on product cards and form inputs, `{rounded.sm}` on standard buttons, `{rounded.full}` reserved for trust chips and clinical claim badges. Spacing is generous — section breaks at `{spacing.section}`, content blocks at `{spacing.xxl}` — letting device photography breathe between claims. Trust signals (clinical study markers, FDA clearance chips, before/after data bars) render in `{typography.label-sm}` uppercase at reduced opacity, anchoring credibility without displacing the aspirational primary prose. A secondary palette of deep indigo (#413389) and blue-violet (#4d5bcd) surfaces in data visualization components and the newsletter strip, drawing from medical imaging aesthetics without making the whole site feel pharmaceutical.

colors:
  primary: "#ec523e"
  primary-active: "#b43145"
  primary-disabled: "#ffefee"
  crimson: "#ae2828"
  accent-indigo: "#413389"
  accent-blue: "#4d5bcd"
  ink: "#121212"
  body: "#202020"
  muted: "#5f6772"
  muted-light: "#969696"
  hairline: "#d9d9d9"
  hairline-soft: "#f3f3f3"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  surface-blush: "#ffefee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Work Sans', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.75px
  display-md:
    fontFamily: "'Work Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.4px
  display-sm:
    fontFamily: "'Work Sans', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Work Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.42
    letterSpacing: 0.2px
  label-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.6px
    textTransform: uppercase
  stat-display:
    fontFamily: "'Work Sans', sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
  button-md:
    fontFamily: "'Work Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Work Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Work Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-light}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1px solid rgba(255,255,255,0.4)"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "none"
  nav-bar-scrolled:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    boxShadow: "0 2px 12px rgba(0,0,0,0.3)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    descTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageRounded: "{rounded.md}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaStyle: "button-primary"
    minHeight: 640px
    paddingX: "{spacing.xxl}"
  trust-badge:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.body}"
    iconColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  clinical-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  stat-block:
    backgroundColor: "{colors.surface-blush}"
    headlineColor: "{colors.primary-active}"
    headlineTypography: "{typography.stat-display}"
    labelColor: "{colors.muted}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  testimonial-card:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.body}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    starColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: "none"
  benefit-strip:
    backgroundColor: "{colors.surface-soft}"
    iconColor: "{colors.primary}"
    labelTypography: "{typography.title-sm}"
    descTypography: "{typography.body-sm}"
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.section}"
  before-after-bar:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    height: 8px
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"
  newsletter-strip:
    backgroundColor: "{colors.accent-indigo}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-sm}"
    inputStyle: "text-input"
    ctaStyle: "button-primary"
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-light}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.label-sm}"
    bodyTypography: "{typography.body-sm}"
    paddingY: "{spacing.section}"
    paddingX: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — The coral (#ec523e) primary button is Joylux's workhorse CTA: uppercase Work Sans at 600 weight, 48px tall with 28px horizontal padding, and `{rounded.sm}` corners that feel assertive without being hard-edged. On hover the background deepens to `{colors.primary-active}` (#b43145); the color shift alone signals state — no scale or shadow needed. Disabled state fills with the blush surface (`{colors.primary-disabled}`, #ffefee) and muted gray text, clearly withdrawing interactivity while maintaining the form's footprint in the layout.

**`button-secondary`** — Transparent fill with a 2px coral outline, paired with `button-primary` for secondary actions such as "Learn More" or "Compare" on the product page. The shared coral tone and `{rounded.sm}` radius make the two read as a deliberate family rather than a visual conflict. Same 48px height and uppercase Work Sans type ensure both buttons hold equal visual weight in a side-by-side CTA pair.

**`button-ghost-dark`** — A dark-surface-only variant carrying a 1px semi-transparent white border with white uppercase text. Used exclusively on hero sections and the near-black (#121212) nav — never on light backgrounds. Its purpose is secondary option signaling against the dark canvas without introducing a third color into the frame.

**`button-pill`** — Small coral pill (`{rounded.full}`) at reduced padding (8px 20px), used for quick-add triggers on product cards, quiz prompts, and filter tags. Runs `{typography.button-sm}` — 13px, uppercase, 0.5px tracking — to stay compact without losing legibility.

### Navigation

**`nav-bar`** — Fixed at 64px height on a near-black (#121212) background, the nav renders white Work Sans labels at 14px/500 weight. The dark bar is persistent across all pages and never lifts to transparent or white. The coral logo mark and a single coral `button-primary` ("Shop Now" or "Get vFit") are the only chromatic elements in the bar. On scroll, `nav-bar-scrolled` adds a 0 2px 12px shadow at 30% black opacity without altering the background color, tightening the height by 4px to signal position.

### Product Card

**`product-card`** — White surface with a 1px `{colors.hairline}` border and `{rounded.md}` (12px) corners. Product image fills the top area with object-fit: contain inside a fixed-height container. Title in `{typography.title-md}` (Work Sans 18px/600), price in `{typography.title-sm}`, short descriptor in `{typography.body-sm}` (Assistant 14px). The coral `button-pill` appears as a quick-add trigger at the card bottom, visible on hover on desktop, always visible on mobile. No drop shadow — the hairline border carries all separation work.

### Hero

**`hero-section`** — Full-viewport section (min-height 640px) on a near-black background. Headline uses `{typography.display-xl}` (Work Sans 52px/700) in white; subheadline uses `{typography.body-md}` in white at ~75% opacity. A single `button-primary` sits below the subheadline with 24px top margin. A row of `clinical-chip` elements appears beneath the CTA — "FDA-Cleared · Clinically Studied · 94% Satisfaction" — in `{typography.label-sm}` on translucent dark chips. On desktop the vFit device photograph is positioned offset-right with text left-aligned; on mobile it stacks above the headline.

### Trust & Clinical Signals

**`trust-badge`** — Pill-shaped badge on blush (#ffefee) with a 1px `{colors.hairline}` border, deployed in the nav footer row, product page headers, and PDP trust rails. Icon prefix in coral, label text in `{typography.label-sm}` (uppercase, 0.6px tracking). Common labels: "FDA Cleared", "Clinically Proven", "HSA/FSA Eligible". The blush fill separates these from plain text without introducing a new dominant color.

**`clinical-chip`** — Simpler than `trust-badge`: a `{colors.surface-soft}` chip with muted text, no border, fully rounded. Used inline within body copy or beneath product images to reference specific study citations. Because it carries no border and uses the site's lightest neutral, it recedes to a supporting role rather than competing with the coral trust badges.

**`stat-block`** — Blush-background metric card displaying a large statistic in `{typography.stat-display}` (Work Sans 42px/700) in `{colors.primary-active}` (#b43145). The metric label beneath uses `{typography.caption}` in muted gray. Blocks deploy as a horizontal row of three or four on desktop — "94% reported improvement", "87% saw results in 3 weeks", "Over 100K women treated" — creating a data-forward credibility rail between the hero and the product section.

### Testimonials

**`testimonial-card`** — Blush (#ffefee) card with `{rounded.md}` corners, no border, and `{spacing.xl}` internal padding. Quote text in `{typography.body-md}` at full opacity in `{colors.body}`; author line in `{typography.caption}` at reduced opacity. Star rating dots in coral (#ec523e). On desktop, cards display in a 3-column grid; on mobile they collapse to a single swipeable carousel with dots navigation.

### Data & Progress

**`before-after-bar`** — An 8px progress bar with a `{colors.hairline}` track and coral fill, used in clinical outcome visualizations ("Before: 2/10 · After: 8/10"). The `{rounded.full}` shape keeps it soft and approachable rather than clinical-bar-chart. Labels above each bar use `{typography.caption}` at muted gray. More complex multi-series charts use the deep indigo (#413389) and blue-violet (#4d5bcd) palette, visually separating data-heavy pages from the aspirational marketing sections.

### Email Capture

**`newsletter-strip`** — A full-width band in deep indigo (`{colors.accent-indigo}`, #413389) with a white headline at `{typography.display-sm}` and an inline email `text-input` plus coral `button-primary`. The indigo creates a hard visual stop between page content and the footer, leveraging the accent palette's one meaningful appearance in the UI. No imagery — the color does all the work.

### Footer

**`footer`** — Near-black (#121212) background matching the nav, creating a symmetrical frame around the page. Four-column link grid in `{typography.body-sm}` Assistant, section headings in `{typography.label-sm}` (uppercase, tracked). Link color is `{colors.hairline}` (#d9d9d9) at ~60% opacity, lifting to full white on hover. Social icons, FDA clearance mark, and HSA/FSA eligibility logo appear in the bottom strip alongside the coral wordmark.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero uses display-md headline (36px); nav collapses to hamburger with full-screen dark drawer; product grid 1-up; stat-blocks stack vertically; before-after bars expand to full width; testimonials become swipeable carousel |
| Tablet | 744–1128px | 2-column product grid; hero shifts to 50/50 image-text split; testimonial cards 2-up; stat-blocks 2×2 grid; newsletter strip stacks input above CTA |
| Desktop | 1128–1440px | 3-column product grid; hero uses offset device photography left-text layout; stat-blocks horizontal 4-up row; testimonials 3-column grid; full nav link row visible |
| Wide | > 1440px | Max-width container (~1320px) centered with `{colors.surface-soft}` or ink gutters; hero image scales up, text column stays fixed width; generous whitespace in benefit-strip and footer |

### Touch Targets

- All buttons maintain minimum 48px height on mobile
- Nav hamburger tap target: 44×44px minimum
- Product card tap area covers the entire card surface, not only the pill button
- Filter chips and `trust-badge` pills padded to minimum 40px tap height on mobile
- `clinical-chip` and inline stat labels are non-interactive — no tap target requirement
- Carousel dot controls: minimum 32px tap targets with 8px gap between dots

### Collapsing Strategy

- Navigation: full horizontal link row → hamburger drawer; the coral CTA button remains visible in the top-right corner at every breakpoint
- Hero: offset side-by-side layout → stacked (device image above text block on mobile); headline steps down from display-xl to display-md
- Product grid: 3-up → 2-up (tablet) → 1-up (mobile)
- Stat block row: 4-up → 2×2 grid (tablet) → stacked single column (mobile)
- Testimonials: 3-column grid → 2-up (tablet) → swipeable single-card carousel with dot indicators (mobile)
- Benefit strip: horizontal icon+label row → 2×N grid (tablet) → stacked list with left-aligned icons (mobile)
- Footer: 4-column link grid → 2-column (tablet) → accordion-collapsed sections (mobile)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values extracted from live site; all `rounded` values are estimated from wellness DTC category norms and inferred visual character
- Canvas white (#ffffff) not extracted (universal default); included as necessary baseline
- Exact nav height, scroll behavior, and sticky offset not confirmed from static extraction
- `primary-disabled` mapped to extracted blush (#ffefee) — actual disabled-state token not confirmed
- Font weights not confirmed; Work Sans 600–700 for display and Assistant 400 for body are inferred from common deployment patterns for these Google Fonts
- Animation easing curves, transition durations, and hover delay timings not extractable from static analysis
- Mobile breakpoint values are estimates; Shopify theme may define different breakpoints from the standard 744/1128/1440 grid
- The deep indigo (#413389), blue-violet (#4d5bcd), and several other colors in the extracted list (#1f77b4, #ff7f0e, #2ca02c, #d62728, #a3f234, #8c564b) likely originate from embedded Plotly or matplotlib chart components rather than brand UI — their role as brand accents is inferred, not confirmed
- No extracted letter-spacing or line-height values from live site; all typographic metrics are reasoned defaults for the identified font families
- Icon set (SVG illustrations vs. icon font vs. custom) not identified from extraction
