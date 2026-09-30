---
version: alpha
name: "Willow Hygiene"
source_url: "https://willow-hygiene.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Where most hygiene brands reach for hospital white and institutional navy, Willow drops anchor in sage — a green that registers as botanical rather than medicinal, closer to the undersides of willow leaves than to surgical scrub. The primary (#5C8F7F) is warm enough to suggest touch, cool enough to suggest cleanliness; it carries every primary CTA and the brand's logo-mark stroke, the two places where color must earn trust rather than merely decorate. Type sits in a humanist sans-serif at scales deliberately larger than standard e-commerce convention demands: the body floor is 16px with a 1.6 line-height rather than the typical 14px, a quiet acknowledgment that reading glasses and small screens co-exist in the daily lives of the brand's core audience — elderly users and the adult children who order on their behalf. Card corners land at {rounded.md} — soft enough to read as approachable, firm enough to structure a grid of products whose packaging shares similar shapes. The brand's signature component is a warm cream surface ({colors.willow-cream}, #FAF7F2) used for care-guide strips beneath product photography, printed in {typography.body-sm} at slightly open letter-spacing, turning instruction into something closer to a pamphlet than a warning label. Trust chips — 'Fragrance-Free', 'Gentle pH', 'Hypoallergenic' — live as {rounded.full} pills in {colors.surface-soft} on every product page, set in {typography.badge} at weight 600, because for this audience compliance certification is a purchase prerequisite rather than a footnote. Warm gold accents ({colors.accent-warm}, #D4A96A) appear in exactly two contexts: the caregiver-discount banner and star-rating fills, grounding moments of human connection in a palette that otherwise holds to sage, cream, and white.

colors:
  primary: "#5C8F7F"
  primary-active: "#426B5D"
  primary-disabled: "#B0D0C8"
  ink: "#1E2B27"
  body: "#374740"
  muted: "#768A85"
  hairline: "#D1DFD9"
  hairline-soft: "#E8F0EE"
  canvas: "#FFFFFF"
  surface-soft: "#F3F8F6"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  willow-cream: "#FAF7F2"
  accent-warm: "#D4A96A"
  accent-warm-muted: "#F2E5CC"
  error: "#C0392B"
  success: "#3E7D5A"

typography:
  display-xl:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.1px
  caption:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  badge:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
  button-md:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'DM Sans', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
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
    padding: "14px 28px"
    minHeight: 52px
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
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "13px 27px"
    minHeight: 52px
  button-reorder:
    backgroundColor: "{colors.willow-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    minHeight: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "14px 16px"
    minHeight: 52px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    mutedColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
  trust-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "5px 12px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    subtitleColor: "{colors.muted}"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  care-guide-strip:
    backgroundColor: "{colors.willow-cream}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption}"
    borderLeft: "3px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  caregiver-cta:
    backgroundColor: "{colors.accent-warm-muted}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-warm}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  star-rating:
    fillColor: "{colors.accent-warm}"
    emptyColor: "{colors.hairline}"
    typography: "{typography.caption}"
    mutedColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    mutedColor: "{colors.muted}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} {spacing.lg}"

## Components

### Buttons

**`button-primary`** — 52px minimum height, 8px radius, sage green fill with white {typography.button-md} at weight 600. The elevated height — above the standard 44px WCAG target — accommodates reduced motor precision without signaling accommodation. Active state deepens to #426B5D with no scale or shadow transform; disabled softens to #B0D0C8 while retaining white text for legibility. Used for Add to Cart, Subscribe, and primary checkout actions.

**`button-secondary`** — White background with a 1.5px sage border and matching text color, same 52px height and 8px radius as primary. Deployed for 'View Details', 'Compare', and secondary navigation actions where the sage fill would compete with product photography. The border at rest is {colors.primary}; hover darkens it to {colors.primary-active}.

**`button-reorder`** — A warm cream ({colors.willow-cream}) pill with ink text at 44px height, reserved exclusively for account and order-history flows where repeat purchase is the expected action. The cream color signals familiarity and routine rather than urgency, distinguishing it from primary acquisition CTAs.

### Forms

**`text-input`** — 52px height, 8px radius, 1.5px border transitions from {colors.hairline} to {colors.primary} on focus with no animation delay. Body-md at 16px prevents iOS auto-zoom. Placeholder in {colors.muted}; error state swaps border to {colors.error}. The generous padding (14px vertical) accommodates users who may have difficulty with tap precision.

### Navigation

**`nav-bar`** — 72px tall, white canvas background, hairline-soft bottom border. Logo anchors left; primary nav links center in {typography.nav-link} at 15px/weight 500; cart and account icons sit right with individual 44px tap targets. On scroll, the bar gains a soft drop-shadow without changing height or color. Mobile collapses to a hamburger with a full-height slide-out drawer.

### Cards

**`product-card`** — 1px bordered card at {rounded.md} with {spacing.base} padding. Product name in {typography.title-md}/weight 600; volume or variant descriptor in {typography.caption}/{colors.muted}; price in {typography.title-sm}/weight 600 below. A horizontal row of up to three trust chips ({components.trust-chip}) sits directly beneath the product image, before the name — putting certification before branding in the visual hierarchy. Star rating in {colors.accent-warm} anchors the bottom row beside the Add to Cart button.

**`trust-chip`** — Pill-shaped at {rounded.full}, soft sage surface background, 11px/weight-600 badge type at 0.4px letter-spacing. Labels are functional ('Fragrance-Free', 'pH Balanced', 'Dermatologist Tested') not aspirational. Maximum three chips per card; overflow is suppressed rather than scrolled, preserving a clean grid.

### Hero & Banners

**`hero-banner`** — {colors.surface-soft} background with product photography right-aligned on desktop, stacked above copy on mobile. Headline in {typography.display-xl} (32px/weight 600), supporting sentence in {typography.body-md} at {colors.muted}, primary CTA below. A one-line care reassurance ('Gentle on skin. Trusted by caregivers.') runs beneath the CTA in {typography.caption}/{colors.muted} — it is the only line on the page not selling anything.

**`announcement-bar`** — Full-width sage bar pinned above the nav, {spacing.sm} vertical padding, white {typography.body-sm} text. Single message only — no carousel — because slow-moving content is easier to parse. Reserved for free-shipping thresholds, caregiver discount codes, and product restock alerts.

### Specialty

**`care-guide-strip`** — A {colors.willow-cream} panel with a 3px left border in {colors.primary}, used beneath product photography on all PDPs. Step-by-step usage instructions in {typography.body-sm} with bold {typography.caption} step labels ('Step 1', 'Step 2'). The left border echoes the brand's primary without overwhelming a block of instructional text. Corners at {rounded.md}.

**`caregiver-cta`** — An {colors.accent-warm-muted} panel with a top accent line in {colors.accent-warm}, appearing once per page above the footer or in a desktop right-rail. Heading in {typography.title-md}, body copy in {typography.body-sm}. Used for caregiver discount enrollment, subscription sign-up, and bulk ordering prompts. The gold accent makes it the warmest panel on the page — human rather than promotional.

**`star-rating`** — Five-star row with {colors.accent-warm} fills and empty stars in {colors.hairline}. Review count in {typography.caption}/{colors.muted}, inline right of the stars. This is one of only two places warm gold appears in standard product UI, keeping the accent legible against both the canvas and card surfaces.

**`footer`** — {colors.surface-soft} background with {spacing.section} top/bottom padding and a 1px top border in {colors.hairline}. Four columns on desktop (Shop, Learn, Support, Newsletter); single accordion on mobile with one section open by default. All links in {typography.body-sm}; legal row in {typography.caption}/{colors.muted}. Every link is padded to {spacing.xxl} minimum vertical hit target — the footer is not an afterthought for users who rely on deliberate navigation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger with full-height slide-out; product cards fill viewport width; hero stacks copy above image; trust chips wrap to two rows; sticky add-to-cart bar pins to bottom of viewport on PDP |
| Tablet | 744–1128px | Two-column product grid; hero splits 50/50 text and image; nav shows top four links with overflow in hamburger; care-guide-strip spans full width below product gallery |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero background extends edge-to-edge with content capped at 1200px; caregiver-cta occupies a right-sidebar column on PDP |
| Wide | > 1440px | All content locked at 1200px max-width; side margins fill with canvas white; no additional layout zones introduced |

### Touch Targets

- All interactive elements minimum 52px height on mobile, exceeding the WCAG 2.5.5 44px target
- Footer links padded to {spacing.xxl} (48px) vertical tap area
- Nav hamburger icon: 48×48px tap zone with 4px invisible padding extension
- Product card tap zone covers the full card surface, not only the button
- Form inputs minimum 52px height to reduce mis-tap on small screens with fine motor limitations
- Trust chips are non-interactive display elements; no minimum target needed

### Collapsing Strategy

- Desktop 4-column nav → tablet 4-link bar with hamburger overflow → mobile full hamburger slide-out panel
- 3-column product grid → 2-column tablet → 1-column mobile (full-bleed cards, 16px margin)
- Hero: side-by-side text/image → stacked image-above-copy below 744px
- Care-guide-strip: right-rail aside on desktop → full-width strip below product gallery on tablet and mobile
- Caregiver-cta: right-sidebar on desktop → full-width banner above footer on tablet and mobile
- Footer: 4-column → 2-column → single accordion, one section open by default on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site; the entire palette above is inferred from brand name, category conventions, and accessibility requirements — treat as hypothesis requiring validation against actual brand assets and CSS custom properties
- No font-family stack was extracted; 'DM Sans' / 'Inter' is a reasonable accessible default but must be verified against computed styles or brand guidelines
- No meta theme-color was present; primary sage (#5C8F7F) is a reasoned inference, not a confirmed brand value
- The site may be behind anti-bot protection, a Cloudflare challenge, or may load all design tokens via JavaScript — manual browser inspection of computed CSS is the recommended next step to confirm the real palette and type scale
- Logo mark details (wordmark style, icon shape, behavior on dark or colored backgrounds) are entirely unknown
- Motion and animation preferences (reduced-motion policy, hover transition durations, scroll behavior) not confirmed
- Product photography style, aspect ratios, and background treatment on imagery are not confirmed
- Whether the brand uses a custom or licensed webfont versus system fonts cannot be determined from extraction alone
- Dark-mode support and any alternate surface colors are unknown
