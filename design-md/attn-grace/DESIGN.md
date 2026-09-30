---
version: alpha
name: "Attn: Grace"
source_url: "https://attngrace.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  #dedc00 is not a color that asks for permission — a hard-edged chartreuse that Attn: Grace deploys as its primary action signal, sitting against warm cream (#fbf5ef) the way a handwritten correction lands on good stationery: direct, personal, slightly irreverent. The choice refuses the muted-lavender register that wellness packaging habitually assigns to aging women, and it is the first design decision that announces this brand was built from the inside by the women it serves. Acre drives the headlines, a typeface carrying editorial authority rather than hospital-legible oversized type, while BentonMod handles body copy and UI labels with a quieter register — finishing sentences that Acre starts.

  The palette moves through three distinct emotional zones that never fully merge. The foreground layer is warm and lit: ivory canvases (#fbf5ef, #ebe2d8) grounding electric yellow (#dedc00) and golden amber (#ffcf2a), with peach and warm orange (#fac8a7, #fb9650) threading through illustration details and badge surfaces. A slate-navy depth layer (#272d45, #2c3e50, #384b57) appears in dark hero sections and footer surfaces, lending a seriousness that reads as engineering credibility rather than aspirational softness. The third zone is a teal family (#00caaa, #b2f9e9, #0e7a82) used for certifications, active form states, and clean-science signals — positioned far from botanical warmth, closer to lab verification.

  Corner radii hold at a measured middle: {rounded.sm} on input fields and claim chips, {rounded.md} on product and testimonial cards, {rounded.full} reserved for badges calling out "skin-safe" and "fragrance-free." Touch targets run at 48px minimum height — not a concession retrofitted at the end of the design process, but baked into the component baseline from the start. Section gaps run at {spacing.section} and internal padding at {spacing.xxl}, using whitespace as a confidence signal: a brand that knows what it has does not need to fill every centimeter with copy.

colors:
  primary: "#dedc00"
  primary-active: "#c4c200"
  primary-hover: "#e8e600"
  primary-disabled: "#f2f199"
  accent-gold: "#ffcf2a"
  accent-teal: "#00caaa"
  accent-teal-light: "#b2f9e9"
  accent-teal-deep: "#0e7a82"
  accent-peach: "#fac8a7"
  accent-orange: "#fb9650"
  slate-deep: "#272d45"
  slate-navy: "#2c3e50"
  slate-mid: "#676986"
  slate-muted: "#9a9db1"
  ink: "#1d1d1b"
  body: "#4f4f4f"
  muted: "#828282"
  hairline: "#e5e5e5"
  hairline-soft: "#dbdde4"
  canvas: "#fbf5ef"
  surface-soft: "#f4f4f6"
  surface-warm: "#ebe2d8"
  surface-card: "#ffffff"
  on-primary: "#1d1d1b"
  on-dark: "#fbf5ef"

typography:
  display-xl:
    fontFamily: "'Acre', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Acre', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Acre', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Acre', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  label-upper:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'BentonMod', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'Acre', sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: 0
    textDecoration: underline
  button-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1.5px
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    borderColor: "{colors.accent-teal}"
    outlineColor: "{colors.accent-teal-light}"
    outlineWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
    padding: "0 {spacing.xl}"
  nav-bar-dark:
    backgroundColor: "{colors.slate-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    shadow: "0 8px 24px rgba(0,0,0,0.08)"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageRounded: "{rounded.md}"
    shadow: none
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.body-sm}"
    captionColor: "{colors.muted}"
  product-card-hover:
    shadow: "0 4px 16px rgba(0,0,0,0.08)"
    border: "1px solid {colors.hairline-soft}"
  badge-claim:
    backgroundColor: "{colors.accent-teal-light}"
    textColor: "{colors.accent-teal-deep}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-tag:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  announcement-bar:
    backgroundColor: "{colors.slate-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    linkColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.xxl} {spacing.xl}"
    imagePosition: right
  hero-dark:
    backgroundColor: "{colors.slate-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "{spacing.xxl} {spacing.xl}"
  section-label:
    textColor: "{colors.accent-teal-deep}"
    typography: "{typography.label-upper}"
    marginBottom: "{spacing.sm}"
  ingredient-callout:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    labelTypography: "{typography.label-upper}"
    labelColor: "{colors.accent-teal-deep}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xl}"
  trust-strip:
    backgroundColor: "{colors.slate-deep}"
    textColor: "{colors.on-dark}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption}"
    height: 48px
    gap: "{spacing.xl}"
  quiz-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl}"
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    quoteTypography: "{typography.body-md}"
    attributionTypography: "{typography.caption}"
    attributionColor: "{colors.muted}"
    padding: "{spacing.xl}"
  before-after-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    labelTypography: "{typography.label-upper}"
    labelColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    borderColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.label-upper}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

---

## Components

### Buttons

**`button-primary`** — The primary CTA button renders in #dedc00 chartreuse with near-black (#1d1d1b) text on top, making it legible without white-on-color contrast. At 48px height with {rounded.sm} corners and BentonMod medium weight, it reads as authoritative without being aggressive. Hover shifts to `#e8e600`; active presses to `#c4c200`; disabled degrades to the pale lemon `#f2f199` with muted text so the affordance disappears without confusion.

**`button-secondary`** — A 1.5px border in {colors.ink} on a transparent background, same 48px height as primary, built for side-by-side CTA pairings. Hover inverts to full {colors.ink} fill with {colors.on-dark} text — a confident binary swap rather than a mid-state gray.

**`button-ghost`** — Inline text link variant with no background and underline decoration, used for "learn more" and editorial navigation within body content. Stays in {colors.ink} to avoid color-link conventions that don't serve this content style.

**`button-teal`** — A secondary CTA variant using {colors.accent-teal} (#00caaa) for moments where the chartreuse primary would clash with surrounding yellow or gold content — most often appearing on clinical result sections and ingredient deep-dive pages.

### Form Inputs

**`text-input`** — 48px height with {rounded.sm} and a 1.5px {colors.hairline} border on a white fill. Focus ring transitions to a 2px {colors.accent-teal} border with a {colors.accent-teal-light} glow — the teal focus treatment reinforces the clean-science register without introducing a new brand hue at the interaction level.

### Navigation

**`nav-bar`** — 64px warm-cream bar with BentonMod nav-link type and a 1px {colors.hairline} underline. Sits flush to the {colors.canvas} background so the transition into page content is seamless. On category and product-listing pages, a `nav-bar-dark` variant swaps to {colors.slate-deep} (#272d45) for pages where the hero extends full-bleed dark. The announcement bar above it runs in the same slate-deep with chartreuse link highlights.

**`nav-dropdown`** — White card with {rounded.sm} and a soft box-shadow, appearing beneath top-level nav items. Uses {typography.body-sm} BentonMod with generous {spacing.lg} internal padding so sub-categories are easy to read and tap.

### Product Card

**`product-card`** — White card ({colors.surface-card}) with {rounded.md} corners, a hairline border, and no default shadow. Hover elevates a soft shadow (`0 4px 16px rgba(0,0,0,0.08)`) and softens the border, creating a lift without heavy depth. Title renders in {typography.title-sm} Acre; price in {typography.price} (Acre 700 at 20px); descriptor copy in {typography.body-sm} BentonMod with {colors.muted} color. Claim badges (`badge-claim`) stack below the title in {colors.accent-teal-light} fill with {colors.accent-teal-deep} text.

### Hero

**`hero`** — Split-layout on desktop with headline in {typography.display-xl} Acre on the left and product photography on the right, minimum 560px height. Uses the warm-cream canvas by default. The CTA drops a `button-primary` (chartreuse). `hero-dark` swaps the fill to {colors.slate-deep} for campaign moments — the chartreuse CTA pops even more dramatically against navy than against cream.

### Badges and Claims

**`badge-claim`** — Mint-filled ({colors.accent-teal-light}) pill with {colors.accent-teal-deep} text at {typography.badge} weight, {rounded.full}. Used for safety and certification claims: "dermatologist-tested," "skin-safe," "fragrance-free." Clusters of 3–5 appear beneath product headlines and on product cards.

**`badge-tag`** — Warm beige ({colors.surface-warm}) pill with {colors.body} text, {rounded.full}. Used for category and ingredient tags ("hyaluronic acid," "for dry skin") where the visual weight should be lower than claims.

**`badge-primary`** — Chartreuse fill ({colors.primary}) with {colors.on-primary} text, {rounded.full}. Reserved for promotional callouts ("new," "bestseller") where brand voltage is needed at a small scale.

### Ingredient Callout

**`ingredient-callout`** — A {colors.surface-warm} (#ebe2d8) section card with {rounded.md}, used to spotlight key active ingredients with an uppercase label in {colors.accent-teal-deep}, a title in {typography.title-md} Acre, and body copy in {typography.body-sm} BentonMod. This module appears in alternating-layout rows on product detail pages, blending editorial warmth with clinical specificity.

### Trust Strip

**`trust-strip`** — A full-width 48px band in {colors.slate-deep} with icon-and-text pairs spaced at {spacing.xl} gaps. Icons render in {colors.primary} (chartreuse) against the navy background — the strongest brand contrast moment in the entire UI. Used immediately below the hero or above the footer to punctuate transition zones with credential signals.

### Quiz CTA

**`quiz-cta`** — A full-bleed {colors.primary} section with {rounded.md} edge treatment on the inner content box. Headline in {typography.display-md} Acre with body copy in {typography.body-md} BentonMod, both in {colors.on-primary}. This is the brand's primary conversion tool — the "find your routine" quiz entry point — and the all-chartreuse fill is one of the only moments where the primary color occupies the full background rather than a button.

### Testimonials

**`testimonial-card`** — {colors.surface-soft} fill with {rounded.md}, {typography.body-md} quote text in {colors.ink}, and {typography.caption} attribution in {colors.muted}. Cards sit in a horizontal scroll rail on mobile and a three-column grid on desktop. Before-after photography pairs appear in `before-after-card` with a hairline border and uppercase timing labels ({typography.label-upper} in {colors.muted}).

### Section Label

**`section-label`** — A tight uppercase {typography.label-upper} line in {colors.accent-teal-deep} that precedes display headlines, creating a two-tier entry into each major content section: the label names the content type ("our ingredients," "what women say"), the display headline delivers the claim.

### Footer

**`footer`** — Near-black (#1d1d1b) fill with {colors.on-dark} warm-cream text. Link columns use {typography.label-upper} headings and {typography.body-sm} BentonMod links in {colors.muted} that hover to {colors.primary} chartreuse. The color switch on hover is the footer's only animation and one of the more satisfying micro-interactions in the system.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger with slide-in drawer; hero stacks vertically (text above, image below); product grid at 2 columns; section padding reduces to {spacing.base}; trust strip scrolls horizontally |
| Tablet | 744–1128px | 2–3 column product grid; hero retains side-by-side at reduced image width; primary nav shows condensed links, overflow in secondary drawer; ingredient callout rows stack 2-up |
| Desktop | 1128–1440px | Full horizontal nav with dropdown overlays; 3–4 column product grid; hero at full split with image occupying ~50% viewport right; quiz-cta at full bleed with contained content width |
| Wide | > 1440px | Content constrained to ~1280px max-width; hero image can bleed edge-to-edge within its column; grid stays at 4 columns; section padding scales to accommodate whitespace proportionally |

### Touch Targets

- All primary and secondary buttons: 48px height minimum
- Nav items and dropdown links: 44px tap height minimum
- Product cards: full-card tap area (entire card is the link target, no nested inner button)
- Badge and chip filters: 36px minimum height on mobile, 32px desktop
- Text inputs: 48px height to ensure comfortable tap and ease of use for the target demographic

### Collapsing Strategy

- Navigation: hamburger with right-side slide-in drawer on mobile; full horizontal with dropdowns on desktop; announcement bar persists at both breakpoints but font size reduces to {typography.caption-sm} on mobile
- Product grid: 2 columns mobile → 3 columns tablet → 4 columns desktop
- Hero layout: stacked (text above / image below) on mobile → 50/50 horizontal split on desktop
- Ingredient callout section: single-column vertical stack on mobile → alternating two-column rows on desktop
- Quiz CTA: full-bleed on all breakpoints, but internal padding reduces from {spacing.xxl} to {spacing.lg} on mobile
- Footer: single-column accordion on mobile; multi-column flat grid on desktop

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact corner radius values could not be confirmed from extraction — {rounded.sm} (8px) on interactive elements and {rounded.md} (12px) on cards are inferred from the brand's moderate-curve aesthetic
- Acre and BentonMod font details (specific weights available, optical sizing, VF axes) could not be confirmed — these are proprietary or licensed typefaces and the extraction returned only font-family stack names
- Full typographic scale and Acre weight pairings are inferred from editorial brand positioning, not measured from rendered DOM
- Animation and micro-interaction timings (hover transition durations, drawer easing) not extractable from static hints
- Whether dark hero sections use flat color fill or photography with a color overlay could not be determined
- Loyalty or subscription program–specific color tokens (if any exist) are not represented in the extraction
- Mobile navigation pattern (hamburger vs. bottom tab bar) not confirmed — hamburger assumed based on Shopify theme conventions
- Product rating/review star colors not confirmed; {colors.ink} assumed as default following common Shopify review widget conventions
- The slate-mid (#676986) and slate-muted (#9a9db1) colors appear in UI chrome but their precise role assignments (e.g., secondary nav text vs. form helper text) could not be confirmed
- Exact grid gutter widths and max content column width at wide breakpoints not extractable
