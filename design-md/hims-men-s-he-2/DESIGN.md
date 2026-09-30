---
version: alpha
name: "Hims"
source_url: "https://forhims.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep forest green on warm cream is the whole argument — #1B4332 against #F5F0E8, held without apology across hero sections, primary CTAs, and the brand wordmark alike. Where most men's health companies default to clinical blue or urgent red, Hims chose the color of old-growth trees and pressed it into every touchpoint that matters: the pill-shaped "Get started" button, the subscription plan border on selection, the progress bar tracking completion inside the intake quiz. The grid is generous and unhurried; a 96px section rhythm at desktop means each condition category — Hair, ED, Skin, Mental Health, Primary Care — gets a full breath before the next. Type runs a clean geometric sans at compact weight 400 for body and a confident 600–700 for display, set large enough that copy reads as a statement rather than a disclaimer. Product photography leans warm: skin tones against cream backgrounds, the occasional dark-green prop, no harsh shadows or stark white studio floors. Condition cards use {rounded.lg} corners and a {colors.surface-soft} fill, softening what could read as a clinical checklist into something closer to a wellness menu. Badges are restrained — no garish sale tags, only subdued {colors.surface-soft} pills in {typography.caption} — because the brand's authority is built on understatement. The quiz and intake flows feel like a conversation: single-question pages, dot-based progress, zero medical-form density. The footer inverts to {colors.surface-dark}, reversing to {colors.on-dark} type, a quiet structural signal that regulatory weight lives at the bottom while approachability governs everything above.

colors:
  primary: "#1B4332"
  primary-active: "#145228"
  primary-hover: "#1E4D3A"
  primary-disabled: "#8FAD9C"
  ink: "#1A1A1A"
  ink-dark: "#111111"
  body: "#3D3D3D"
  muted: "#767676"
  muted-soft: "#999999"
  hairline: "#E0DDD6"
  hairline-soft: "#EDE9E1"
  canvas: "#F5F0E8"
  surface-soft: "#EDE9E1"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A1A"
  on-primary: "#FFFFFF"
  on-dark: "#F5F0E8"
  accent-warm: "#C9956A"
  success: "#2D6A4F"
  error: "#C62828"

typography:
  display-xl:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-xs:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.1px
  label-uppercase:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  price-display:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
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
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 52px
    minWidth: 180px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 52px
    border: "2px solid {colors.primary}"
  button-secondary-light:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 52px
    border: "2px solid {colors.on-dark}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
  condition-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadMaxWidth: 560px
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
  plan-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "2px solid {colors.hairline}"
    priceTypography: "{typography.price-display}"
    labelTypography: "{typography.caption}"
  plan-card-selected:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "2px solid {colors.primary}"
    priceTypography: "{typography.price-display}"
    labelTypography: "{typography.caption}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 52px
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
  quiz-option:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.primary}"
    selectedBackground: "{colors.surface-soft}"
    minHeight: 56px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 12px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
    ratingColor: "{colors.primary}"
    nameTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    disclaimerTypography: "{typography.caption-xs}"
    disclaimerColor: "{colors.muted-soft}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xl}"
  sticky-cta-mobile:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    buttonFullWidth: true

## Components

### Buttons
**`button-primary`** — The dominant CTA in forest green (#1B4332) on cream or white surfaces, pill-shaped at `{rounded.full}`, 52px tall, minimum 180px wide on desktop. Carries "Get started," "Continue," and all subscription CTAs; hover deepens to `{colors.primary-hover}`, active to `{colors.primary-active}`, and disabled mutes to `{colors.primary-disabled}`. On mobile, typically stretches full-width.

**`button-secondary`** — Outlined variant with a 2px `{colors.primary}` border and matching text on a transparent background, identical height to primary. Appears in two-CTA rows alongside primary ("See plans" next to "Get started"). On dark hero sections, swap to `button-secondary-light` which reverses border and label to `{colors.on-dark}`.

**`button-text`** — Inline link-style CTA in `{colors.primary}` with underline, no padding or height constraint. Used for "Learn more," secondary navigation, and "See all" actions embedded in body copy.

### Navigation
**`nav-bar`** — 72px cream bar with a `{colors.hairline}` bottom border. Brand wordmark left, condition mega-nav center (Hair · ED · Skin · Mental Health · Primary Care), account and cart icons right. Swaps to `nav-bar-dark` when the page hero uses a dark background. Condition links use `{typography.nav-link}` at weight 500; hover state shows a `{colors.primary}` underline without any fill change. Collapses to hamburger + wordmark at tablet breakpoint.

### Product & Condition Cards
**`product-card`** — White surface with `{rounded.lg}` corners and a single `{colors.hairline}` border. Stacks product image (square crop, top), name in `{typography.title-md}`, price in `{typography.price-display}`, a trust-badge showing subscription pricing, and a full-width `button-primary`. Hover state may lift slightly with a subtle shadow.

**`condition-card`** — `{colors.surface-soft}` fill, `{rounded.lg}`, no border. Used in the condition-selection grid with a simple icon, condition name in `{typography.title-md}`, and a one-line descriptor in `{typography.body-sm}`. Grid is 2-column on mobile, 3-column on tablet, 4–5-column on desktop.

### Plan Cards
**`plan-card`** and **`plan-card-selected`** — White cards at `{rounded.lg}` with 2px borders toggling between `{colors.hairline}` (unselected) and `{colors.primary}` (selected). Each holds a plan duration label in `{typography.label-uppercase}`, price-per-period in `{typography.price-display}`, savings callout in `{typography.caption}`, and a short inclusion list in `{typography.body-sm}`. Arranged in a horizontal row on desktop; stack vertically on mobile.

### Quiz & Intake Flow
**`quiz-option`** — Single-select answer tile in white with `{rounded.md}` corners. At rest: `{colors.hairline}` border. On selection: border upgrades to `{colors.primary}` and fill shifts to `{colors.surface-soft}`. Label in `{typography.body-md}`. Pages are deliberately single-question; a `progress-bar` at the top of the viewport tracks percentage complete. Minimum 56px height for comfortable mobile tapping.

**`text-input`** — Form field for name, date, address, and medical context in the intake flow. White fill, `{rounded.sm}`, hairline border that strengthens to `{colors.primary}` on focus. 52px height matches primary button for visual alignment.

### Trust & Social Proof
**`trust-badge`** — `{colors.surface-soft}` pill in `{typography.caption}` for claims like "FDA-approved," "HSA/FSA eligible," and "Rx included." Appears in product cards, hero sections, and checkout header. Always small, never bold, never colored — restraint is the proof.

**`review-card`** — White surface with `{rounded.lg}`, star rating in `{colors.primary}` (green stars, not gold — a deliberate brand distinction), reviewer name in `{typography.title-sm}`, body in `{typography.body-sm}`. Displayed as a carousel on desktop (3 visible), single-card on mobile.

### Hero Sections
**`hero-section`** — Cream canvas with `{spacing.section}` vertical padding. Headline in `{typography.display-xl}`, subhead in `{typography.body-md}` capped at 560px max-width. CTA row follows: primary button with optional secondary `button-text`. Photography anchors the right column (60/40 split) on desktop, collapses image-above-text on mobile. `hero-dark` uses `{colors.surface-dark}` and `{colors.on-dark}` type for flagship subscription and brand moments.

### Footer
**`footer`** — Full-bleed dark canvas (`{colors.surface-dark}`) with cream text (`{colors.on-dark}`). Four-column link grid at desktop (Treatments · Company · Support · Legal), each column heading in `{typography.label-uppercase}`, links in `{typography.body-sm}` at `{colors.muted-soft}`. Social icons row-aligned at bottom. Legal disclaimer in `{typography.caption-xs}` at `{colors.muted-soft}`. Collapses to accordion on mobile.

### Sticky Mobile CTA
**`sticky-cta-mobile`** — Fixed bottom bar visible on condition and product pages once the hero CTA scrolls out of view. Cream fill, `{colors.hairline}` top border, `{spacing.base}` padding all around. Contains a single full-width `button-primary`. Dismissed automatically at checkout entry.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; condition grid 2×N; hero image stacks above headline; nav collapses to hamburger + wordmark; `sticky-cta-mobile` appears; plan cards stack vertically; section padding reduces to 48px |
| Tablet | 744–1128px | Two-column hero (50/50); condition grid 3-col; plan cards in horizontal 3-col row; nav shows top-level condition links, secondary items hidden |
| Desktop | 1128–1440px | Full 12-col grid, content max-width ~1080px centered; condition nav fully expanded; hero 60/40 split with image bleed right; review carousel shows 3 cards simultaneously |
| Wide | > 1440px | Container locks at 1280px; outer canvas visible as cream gutter; hero image scales in place, text column width fixed |

### Touch Targets
- All buttons minimum 52px height; full-width on mobile for primary CTAs
- Quiz option tiles minimum 56px height for single-thumb tap comfort
- Nav hamburger icon 44×44px tap zone
- Plan card selection area padded to minimum 44px touch target regardless of visible border
- Trust badge pills are display-only, not interactive; no touch target required

### Collapsing Strategy
- Condition mega-nav collapses to hamburger first, at approximately 1000px
- Three-column plan card row collapses to vertical single-column stack below 744px
- Review carousel reduces from 3 visible cards to 1 on mobile, with swipe gesture
- Hero two-column layout stacks image-above-text on mobile; image scales to full container width
- Footer four-column link grid collapses to single-column accordion with expand/collapse per section on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — forhims.com likely renders design tokens via JavaScript or sits behind anti-bot protection at crawl time; all hex values above (#1B4332 primary green, #F5F0E8 canvas cream, #C9956A accent warm) are approximations drawn from published brand audits and press coverage. Verify all swatches against DevTools → Computed Styles on live production before shipping.
- **No font families extracted** — Typography stack attributed to Neue Haas Grotesk based on DTC brand identity references; this may be a different licensed Grotesk variant or a custom cut. Confirm via DevTools → Network → Fonts tab on a cold load.
- **Dark/light nav switching behavior** — Exact scroll-trigger threshold and transition timing for nav-bar ↔ nav-bar-dark swap not confirmed; requires live inspection of scroll event handlers.
- **Prescription and post-auth UI** — Medical intake screens, photo upload flow, physician-review status, and pharmacy tracking pages are behind authentication and were not accessible; components above cover pre-auth marketing surfaces only.
- **Custom icon library style** — Hims uses proprietary iconography in condition cards and nav; exact stroke weight, corner rounding, and fill style not verified from extraction.
- **Animation and motion tokens** — Transition duration, easing curves, and animation behavior for quiz-option selection, plan-card border toggle, progress-bar fill, and sticky-CTA appearance are unconfirmed.
- **Accent color usage scope** — `{colors.accent-warm}` (#C9956A) appears in photography art direction and occasional UI moments but its exact usage rules (which components, which contexts) need live verification.
