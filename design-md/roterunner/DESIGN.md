---
version: alpha
name: "Roterunner"
source_url: "https://roterunner.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Four verbs in sequence — Dream, Plan, Act, Achieve — set the brand's conversational rhythm before a single product is shown, and the visual system echoes the same four-beat logic: an indigo primary (#5873f9) for action-state CTAs, amber (#fcab2f) for aspiration and urgency, teal (#00caaa) for completion and reward, and deep navy (#0d1925) as the grounding anchor that gives the lighter signals room to land. Plus Jakarta Sans carries body and UI text at modest weights — the geometric letterforms feel engineered without tipping into cold — while EB Garamond appears sparingly in editorial moments, lending a brief paper-planner intimacy to what is otherwise a screen-native system. Surfaces are stratified into three luminance bands: a near-white canvas (#f7f7f8) for the base layer, soft blue-gray panels (#e5e5eb, #dbdde4) for card lift, and the dark navy stack (#272d45, #0d1925) for high-contrast hero blocks and sticky nav on scroll. Corners are mostly soft — {rounded.sm} to {rounded.md} — never fully pill-shaped for form fields, preserving a structured, grid-conscious feel consistent with a product built around structure and scheduling. The amber accent (#fcab2f) reads as a highlight marker, a literal nod to the physical practice of underlining goals; the teal (#00caaa, #b2f9e9 for the softer tint) closes the feedback loop as the "done" signal. Muted blue-gray body text (#676986) on light surfaces reduces the visual weight of long reading states — journaling, weekly review — so the indigo CTAs remain the sharpest element on the page. Every interaction state is distinct: hover deepens to a darker indigo, disabled bleaches toward #b8c3fd, and active states on amber compress to #d68000 to feel like a struck match.

colors:
  primary: "#5873f9"
  primary-active: "#3d57e8"
  primary-disabled: "#b8c3fd"
  accent-amber: "#fcab2f"
  accent-amber-active: "#d68000"
  accent-teal: "#00caaa"
  accent-mint: "#b2f9e9"
  accent-rust: "#9e3703"
  ink: "#0d1925"
  body: "#2c3e50"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f8"
  surface-card: "#f4f4f6"
  surface-dark: "#272d45"
  surface-darker: "#0d1925"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-amber: "#0d1925"
  on-teal: "#0d1925"

typography:
  display-xl:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-editorial:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-sm:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  overline:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.3px
  badge:
    fontFamily: "'Plus Jakarta Sans', -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    height: 48px
    hover:
      backgroundColor: "{colors.primary-active}"
    disabled:
      backgroundColor: "{colors.primary-disabled}"
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
    height: 48px
    border: "1.5px solid {colors.hairline}"
    hover:
      borderColor: "{colors.primary}"
      textColor: "{colors.primary}"
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-amber}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    hover:
      backgroundColor: "{colors.accent-amber-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focus:
      borderColor: "{colors.primary}"
      outline: "3px solid {colors.primary-disabled}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.primary}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-darker}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    hover:
      boxShadow: "0 4px 20px rgba(0,0,0,0.08)"
      transform: translateY(-2px)
  hero-dark:
    backgroundColor: "{colors.surface-darker}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
    accentColor: "{colors.accent-amber}"
  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
  goal-step-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    width: 28px
    height: 28px
    variants:
      amber:
        backgroundColor: "{colors.accent-amber}"
        textColor: "{colors.on-amber}"
      teal:
        backgroundColor: "{colors.accent-teal}"
        textColor: "{colors.on-teal}"
  achievement-chip:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  new-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-amber}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  section-overline:
    textColor: "{colors.primary}"
    typography: "{typography.overline}"
    marginBottom: "{spacing.sm}"
  editorial-quote:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.display-editorial}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
    borderLeft: "4px solid {colors.primary}"
  step-tracker:
    activeColor: "{colors.primary}"
    completeColor: "{colors.accent-teal}"
    inactiveColor: "{colors.hairline}"
    textTypography: "{typography.caption}"
    connectorHeight: 2px
  planner-feature-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.accent-teal}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    padding: 10px 16px
    height: 44px
    iconColor: "{colors.muted}"
    focus:
      borderColor: "{colors.primary}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "10px {spacing.base}"
    accentColor: "{colors.accent-amber}"
  footer:
    backgroundColor: "{colors.surface-darker}"
    textColor: "{colors.on-dark}"
    mutedColor: "{colors.muted-soft}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The main conversion driver at 48px tall in indigo (#5873f9) with {rounded.sm} corners and Plus Jakarta Sans 700 at 15px. Hover deepens to #3d57e8; disabled state bleaches to #b8c3fd with white text retained. Used for primary purchase flows, account creation, and plan-selection CTAs.

**`button-amber`** — A warm alternative CTA in amber (#fcab2f) with near-black text (#0d1925) for contrast. Deployed on dark hero sections where indigo would compete with the navy background, and on time-limited offer banners. Active state compresses to #d68000. Carries the brand's aspirational urgency rather than its operational authority.

**`button-secondary`** — White fill with a 1.5px hairline border (#dbdde4) and ink text. On hover the border and text both shift to indigo — a quiet signal of interactivity without adding color mass. Used as a paired "learn more" alongside a primary CTA, or as a solo action on product card overlays.

**`button-ghost`** — Transparent background, indigo text, no border. Reserved for tertiary inline actions: "See all products," "Read more," "Skip." Respects the grid without competing for attention.

### Navigation

**`nav-bar`** — 64px white bar with a 1px hairline-soft bottom border on light-background pages. The Roterunner wordmark renders in indigo using Plus Jakarta Sans 700; nav links at 14px/600 in ink with an indigo underline bar on active state. On scroll past the hero, a diffuse drop shadow activates to reinforce depth. A `nav-bar-dark` variant sits on #0d1925 with white text for use over dark hero sections — no border needed, the contrast is sufficient.

### Product Cards

**`product-card`** — White card, 1px hairline border, {rounded.md} corners. Image sits in a {rounded.sm} cropped container at top; product title in `title-md` at 18px/700; price in `price` style at 22px/800 with indigo for the current price and muted-soft strikethrough for compare-at. On hover the card lifts 2px with a diffuse 20px shadow. Badge overlays (sale, new) pin to the top-left corner of the image container.

### Hero

**`hero-dark`** — Full-bleed section on #0d1925 navy with a display-xl headline up to 48px/800. Amber (#fcab2f) marks keyword highlights or underline accents within the headline copy. Primary CTA is `button-primary` (indigo) with `button-ghost` (white text, transparent) as a secondary. Body subtext in `body-md` at muted-soft (#9a9db1). 64px vertical padding top and bottom.

**`hero-light`** — Surface-soft (#f7f7f8) variant for secondary landing sections and mid-page feature breaks. Same typographic scale, ink text. CTA switches to `button-amber` to introduce warmth contrast against the light ground, avoiding a double-indigo situation.

### Goal Step Badges

**`goal-step-badge`** — 28×28px numbered circles that appear in the four-step "Dream → Plan → Act → Achieve" feature sequences. Default indigo (#5873f9) for step 1 and 3; amber variant (#fcab2f, on-amber text) for step 2; teal variant (#00caaa, on-teal text) for step 4 — the completion node. Typography: `badge` style, vertically centered. Creates a visual drumbeat that mirrors the tagline's rhythm.

### Badges and Labels

**`achievement-chip`** — Mint-teal tinted chip (#b2f9e9, ink text) for "bestseller," "goal achieved," or "most popular" indicators. UPPERCASE badge typography at 11px/700 with {rounded.xs}. Appears on product cards and post-purchase confirmation states as a soft reward signal.

**`new-badge`** and **`sale-badge`** — Amber and indigo versions respectively, both at 4px padding with {rounded.xs}. Badge typography, UPPERCASE. Pin to product image top-left. Amber reads as news and opportunity; indigo reads as value action.

### Section Labels

**`section-overline`** — Indigo uppercase label (11px/700, 1.2px letter-spacing) placed above section headings. An 8px gap below before the display heading. Used to title every major landing-page section — "For Goal-Setters," "How It Works," "Best Sellers" — creating a consistent cadence of introduced content.

### Editorial Pull-Quote

**`editorial-quote`** — Surface-card (#f4f4f6) panel with a 4px solid indigo left border and EB Garamond 32px text for pull-quotes or founder notes. Rounded to {rounded.md} with 48px padding. The serif face and physical-planner intimacy contrast with the surrounding Plus Jakarta Sans system, marking a moment of voice rather than function.

### Step Tracker

**`step-tracker`** — Horizontal four-node progress indicator reflecting the tagline sequence. Active node in indigo (#5873f9), completed nodes in teal (#00caaa), inactive in hairline gray. Nodes connected by a 2px horizontal line. `caption` typography labels sit below each node. Used on product pages to show a planner's workflow and on checkout as a progress indicator.

### Planner Feature Cards

**`planner-feature-card`** — Dark navy card (#272d45) for use on dark grid sections. Teal accent color (#00caaa) marks the icon or category label. Title in `title-md` at on-dark white; body copy in `body-sm` at on-dark slightly reduced opacity. {rounded.md} corners, 32px padding. Used in 3-up feature grids explaining planning methodologies or product capabilities.

### Footer

**`footer`** — Full-bleed #0d1925 background. Section headings in `title-sm` at on-dark white. Link text in `body-sm` at muted-soft (#9a9db1). A 1px hairline-soft horizontal rule separates the link-column block from the legal/social bottom row. 64px vertical padding preserves the section-level spacing rhythm even at the page base.

### Promotional Banner

**`promo-banner`** — Full-width sticky strip in indigo (#5873f9) above the nav during active promotions. `body-sm` white text; percentages and deadline copy rendered in amber (#fcab2f) for scannability. Dismissible via a minimal ×icon on the right edge. On mobile, wraps to two lines at full strip width.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero headline scales to `display-md` (28px); nav collapses to hamburger drawer; product grid 1-up; step-tracker renders vertically; section padding drops to {spacing.xl} |
| Tablet | 744–1128px | 2-column product grid; hero headline at `display-lg` (36px); nav shows primary links with overflow menu; planner-feature-cards 2-up |
| Desktop | 1128–1440px | 3–4 column product grid; hero at `display-xl` (48px); full horizontal nav with all links visible; step-tracker horizontal 4-across |
| Wide | > 1440px | Max content width ~1320px centered; hero gains wider side margins; product grid caps at 4 columns with increased gutter |

### Touch Targets

- All buttons minimum 48px tall; icon-only controls 44×44px minimum
- Nav hamburger tap zone 44×44px regardless of icon render size
- Product card entire surface is a link — no separate tap target needed
- Step-tracker nodes padded to 36×36px touch zone even when displayed at 28px visually
- Promo banner dismiss button 44×44px tap zone on mobile

### Collapsing Strategy

- Primary nav collapses at 744px to a full-height right-side drawer; all links visible in `nav-link` style stacked vertically
- Hero CTA pair (primary + ghost) shifts from horizontal row to full-width vertical stack at < 480px
- Planner feature cards shift from 3-up to 2-up at tablet, 1-up at mobile
- Step-tracker flips from horizontal to vertical at mobile; connector becomes a left-aligned vertical line
- Section overlines remain visible at all breakpoints; display type steps down one scale level per breakpoint
- Editorial quote left-border collapses to top-border on mobile with reduced padding ({spacing.lg})

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Wordmark/logo asset not confirmed — indigo Plus Jakarta Sans Bold assumed based on font-stack and primary color evidence
- EB Garamond use cases inferred from font-stack presence; no confirmed page locations observed during extraction
- No icon library or illustration system confirmed — goal-step icons and feature card icons are referenced by role, not specific assets
- Dark-mode system toggle behavior unknown — dark surfaces may be section-specific only; no `prefers-color-scheme` behavior confirmed
- Exact product image aspect ratios and card padding rhythm could not be verified from extraction alone
- Animation and transition timing values not extractable — hover/active states default to 150–200ms ease-out
- Cart drawer, checkout, and account UI not captured — components above cover storefront and landing surfaces only
- Compare-at price strikethrough color assumed muted-soft (#9a9db1) based on Shopify platform conventions; not directly observed
- `accent-rust` (#9e3703) appears in the extracted palette but no clear UI role was identified; omitted from components pending confirmation
- Teal variants `#1a6c79` and `#0e7a82` extracted but may belong to a specific product colorway rather than the system palette
