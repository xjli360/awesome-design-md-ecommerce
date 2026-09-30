---
version: alpha
name: "Keeps"
source_url: "https://keeps.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clinical-grade men's health brand that uses a near-black ink (#231e20) and a warm off-white canvas (#fafaf5) as its primary tension — the palette feels like a doctor's office that someone remembered to paint. The brand's voltage comes from a single red (#e22631) that appears on primary CTAs, price badges, and the "K" in the logotype; it's a stop-sign red, not a romantic crimson, and it signals urgency without panic. Typography runs a mix of Apercu (a clean geometric sans with a slight humanist warmth) for body and headlines, with TiemposHeadline reserved for editorial moments and Knockout used sparingly for condensed display weight. The system uses soft squared corners ({rounded.sm} ~8px) on cards and inputs rather than pills — the brand wants competence, not friendliness. Buttons are full-width, 48px tall, with 16px horizontal padding and that red fill; secondary buttons invert to a white fill with a 2px red stroke. The site's structure is a single-column narrative scroll with sticky top-nav (80px, white background, logo left, CTA right), product cards in a 2-column grid on desktop, and a persistent "consultation" entry point that mimics a telehealth flow. The overall feel is direct, medical-but-not-sterile, with generous whitespace and a muted gray (#5c5c5c) for secondary text that keeps the reading experience calm despite the red urgency.

colors:
  primary: "#e22631"
  primary-active: "#ba3838"
  primary-disabled: "#fdecf0"
  ink: "#231e20"
  body: "#3c3839"
  muted: "#5c5c5c"
  muted-soft: "#808080"
  hairline: "#e7e7e7"
  hairline-soft: "#dcd7ce"
  canvas: "#fafaf5"
  surface-soft: "#f5f3ed"
  surface-card: "#fbfbfb"
  on-primary: "#ffffff"
  success: "#38a169"
  error: "#ff4646"
  badge-red: "#e22631"
  badge-green: "#38a169"
  star-rating: "#f1c40f"

typography:
  display-xl:
    fontFamily: "'TiemposHeadline', 'Georgia', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Apercu', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  display-condensed:
    fontFamily: "'Knockout', 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
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
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 12px 22px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
    padding: 11px 15px
  text-input-error:
    border: "1px solid {colors.error}"
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.muted-soft}"
    rounded: "{rounded.xs}"
    size: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.muted-soft}"
    size: 20px
  radio-checked:
    border: "6px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 80px
    borderBottom: "1px solid {colors.hairline}"
  nav-logo:
    height: 28px
  nav-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 20px
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
  product-card-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  star-icon:
    color: "{colors.star-rating}"
    size: 14px
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 600px
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.md}"
  hero-cta:
    marginTop: "{spacing.lg}"
  consultation-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  consultation-step:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  consultation-step-number:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    width: 24px
    height: 24px
    display: flex
    alignItems: center
    justifyContent: center
  badge-green:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-red:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.lg}"
  testimonial-quote:
    typography: "{typography.body-md}"
    fontStyle: italic
  testimonial-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.sm}"
  faq-accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  faq-question:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  faq-answer:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.sm}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Full-width on mobile, auto-width on desktop. Uses the brand red (#e22631) background with white text in Apercu 16px/600. Hover state darkens to `{colors.primary-active}` (#ba3838). Disabled state uses a soft pink tint `{colors.primary-disabled}` with muted gray text. Rounded corners at `{rounded.sm}` (8px). Padding is 14px vertical, 24px horizontal, height locked at 48px for consistent tap target.

**`button-secondary`** — Inverted variant for less prominent actions. White background with a 2px red stroke and red text. Hover shifts background to `{colors.surface-soft}` and darkens the stroke. Same 48px height and 8px radius as primary. Used for "Learn More" links, secondary form actions, and ghost CTAs in hero sections.

**`button-tertiary-text`** — Text-only button with no background or border. Red text in Apercu 16px/600. Used for inline links styled as buttons, "Skip" actions, and cancel buttons in multi-step flows.

**`button-pill-primary`** — A smaller, fully rounded variant (40px height, `{rounded.full}`) used for compact CTAs like "Add to Cart" in product cards, consultation entry points, and sticky mobile CTAs. Same red fill and white text but in `{typography.button-sm}` (14px).

### Text Inputs
**`text-input`** — Standard form input with white background, 1px hairline border, 8px radius, and 48px height. Focus state thickens the border to 2px and switches to brand red. Error state uses a red border with `{colors.error}`. Labels sit above in `{typography.caption}` with muted gray. Placeholder text uses `{colors.muted-soft}`. Used across consultation forms, checkout, and account settings.

**`select-dropdown`** — Matches text-input styling but includes a custom dropdown arrow. Same 48px height, 8px radius, and hairline border. Focus state mirrors input focus.

**`checkbox`** and **`radio`** — 20px square/round controls with 2px muted-soft border. Checked state fills with brand red. Used in treatment selection, consent forms, and multi-step questionnaires.

### Navigation
**`top-nav`** — Fixed 80px bar with white background and 1px bottom hairline. Logo sits left at 28px height. Navigation links use `{typography.nav-link}` (Apercu 14px/600). A persistent CTA button (`{typography.button-sm}`, 36px height) sits right, using the primary red. On mobile, nav links collapse into a hamburger menu; the CTA remains visible.

**`nav-logo`** — The Keeps logotype rendered at 28px height. The "K" uses brand red; remaining letters use ink. Maintains consistent positioning across breakpoints.

### Product Cards
**`product-card`** — White card with 1px soft hairline border and 8px radius. Contains a square image (1:1 aspect ratio, 4px radius), title in `{typography.title-sm}`, price in bold 16px, and optional badge. Badges use `{typography.badge}` (11px uppercase, 700 weight) with red or green background. Star ratings use `{colors.star-rating}` (#f1c40f). Cards stack in a 2-column grid on desktop, single column on mobile.

### Hero Section
**`hero-section`** — Full-width white canvas with 64px vertical padding. Headline uses `{typography.display-xl}` (TiemposHeadline 36px/700) capped at 600px width. Subhead in `{typography.body-md}` with muted gray. Primary CTA sits below with 24px top margin. On mobile, headline reduces to 28px and padding compresses to 32px.

### Consultation Card
**`consultation-card`** — A soft gray card (`{colors.surface-soft}`) with 1px soft hairline border and 8px radius. Contains numbered steps (24px red circles with white numbers) and step titles. Used in the "How It Works" section and the consultation flow itself. Padding is 24px.

### Badges
**`badge-green`** and **`badge-red`** — Small uppercase labels (11px/700) with 4px radius and 2px/8px padding. Green for "In Stock" or "FDA Approved," red for "Best Seller" or "Limited Time." Always sit top-right on product cards or inline with titles.

### Footer
**`footer`** — Full-width dark section using `{colors.ink}` background with white text. Links use `{typography.link}` in `{colors.muted-soft}` and lighten to white on hover. Padding is 48px vertical, 24px horizontal. Contains legal text, support links, and social icons. On mobile, links stack vertically.

### Dividers
**`divider`** and **`divider-soft`** — 1px horizontal rules. Standard divider uses `{colors.hairline}` (#e7e7e7); soft variant uses `{colors.hairline-soft}` (#dcd7ce). Used between sections, in accordions, and in card layouts.

### Progress Bar
**`progress-bar`** — 4px tall, fully rounded, with gray background. Fill uses brand red. Used in multi-step consultation flows and treatment progress tracking.

### Tooltip
**`tooltip`** — Dark background (`{colors.ink}`) with white text in 12px/400. 4px radius, 4px/8px padding. Appears on hover for informational icons, dosage guides, and medical disclaimers.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; product cards stack vertically; hero padding reduces to 32px; top-nav height stays 80px but nav links collapse to hamburger; CTAs become full-width; consultation steps stack; footer links stack |
| Tablet | 744–1128px | Two-column product grid; hero headline at 32px; nav links visible as text; consultation steps in 2-column grid; footer links in 2 columns |
| Desktop | 1128–1440px | Full layout: 2-column product grid, 80px nav with all links, hero at 36px headline, consultation in 3-column grid, footer in 4 columns |
| Wide | > 1440px | Content max-width at 1200px centered; hero headline max-width at 700px; extra whitespace on sides |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain minimum 44px tap target height
- Primary CTAs are 48px tall for comfortable tapping
- Checkbox and radio controls are 20px with 44px hit area via padding
- Nav links have 44px minimum tap area on mobile
- Product card CTAs are 40px tall (pill variant) or 48px (standard)

### Collapsing Strategy
- Top nav: Links collapse into hamburger menu below 744px; logo and CTA remain visible
- Product grid: 2-column collapses to 1-column below 744px
- Consultation steps: 3-column collapses to 2-column at tablet, 1-column at mobile
- Footer links: 4-column collapses to 2-column at tablet, 1-column at mobile
- Hero: Side-by-side content (text + image) collapses to stacked below 744px
- Multi-step forms: Step indicators collapse from horizontal to vertical on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (buttons, links, cards) are inferred from common patterns; exact color transitions and durations not extracted
- Active/focus states for text inputs, checkboxes, and radios are based on standard accessibility patterns; brand-specific focus ring styles (color, offset, width) not confirmed
- Error message styling (text color, background, iconography) for form validation not extracted
- Dark mode: no evidence of dark theme support on live site
- Sub-brand or promotional palettes (seasonal campaigns, limited editions) not captured
- Typography scale for mobile (font-size reductions) not extracted; values above are desktop-first
- Spacing values for specific component gaps (card grid gaps, section margins) are estimates based on common patterns
- Animation and transition timing (hover fade, page transitions, loading states) not extracted
- Icon set: specific SVG styles, stroke widths, and color assignments for icons not captured
- Loading states (skeleton screens, spinner styles) not observed
- Accessibility: focus-visible styles, skip-to-content, and ARIA patterns not verified
- Print stylesheet behavior not documented
- The extracted color list includes many framework-default colors (iOS system blues, greens, reds, grays) that are likely from third-party widgets (Shopify Pay, Klarna, Afterpay) rather than brand colors. The true brand palette is concentrated around #231e20, #fafaf5, #e22631, #5c5c5c, #808080, #e7e7e7, #dcd7ce, #3c3839, #d7ece1, #f5f3ed, #38a169, and #fdecf0. The remaining colors (#3498db, #07bc0c, #f1c40f, #e74c3c, #4cd964, #5ac8fa, #007aff, #34aadc, #5856d6, #ff2d55, #bb86fc) are excluded as non-brand.
- Font-family declarations include system fallbacks (-apple-system, BlinkMacSystemFont, etc.) and common web fonts (Roboto, Oxygen, etc.) that may not be actively used; the primary brand fonts are Apercu (with Bold and Light variants), TiemposHeadline, Knockout, and ApercuMono.
