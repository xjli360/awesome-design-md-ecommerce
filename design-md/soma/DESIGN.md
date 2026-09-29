---
version: alpha
name: "Soma"
source_url: "https://drinksoma.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Orange as ripe as a California sunset (#f15623) punctuates every call-to-action on a site that otherwise breathes in glacial pale blue-greens and whisper-soft grays — the visual equivalent of pouring filtered water into a sunlit glass. Soma pairs Cormorant, a high-contrast transitional serif, with Instrument Sans for body copy, creating a tension between editorial elegance and lab-clean utility that mirrors the brand's pitch: beautiful objects that happen to remove microplastics. Display headlines land large in Cormorant at 600-weight, their hairline serifs implying precision; below, Instrument Sans at 400-weight holds ingredient lists and filter specs in neat, readable stacks. A secondary electric chartreuse (#e8ff7a) flashes on promotional badges and hover states — an unexpected, almost neon punctuation that keeps the palette from drifting into spa-brochure territory. Cards and product tiles float on `{colors.surface-card}` (#ffffff) with `{rounded.md}` corners and a single-pixel `{colors.hairline}` border, while section backgrounds alternate between pure canvas and `{colors.surface-soft}` (#f8f8f8) tinted with the faintest aqua undertone (`{colors.surface-mist}` #ebf2f2). The layout grid caps at 1440px, padding generously with `{spacing.section}` between feature blocks so each filtration claim — microplastic removal, sustainable materials, carbon offset — occupies its own visual room. Navigation is minimal: a sticky top bar at 64px with Poppins medium links, a single search icon, and the orange cart indicator. Touch targets on mobile run 48px minimum, and the product card grid collapses from three columns to a single swipeable rail below 744px. The overall rhythm is slow and confident — long scroll sections, oversized product photography bleeding to container edges, and generous 48px vertical gaps between content clusters — letting water imagery and white space do the persuasion that most DTC brands delegate to dense copy.

colors:
  primary: "#f15623"
  primary-active: "#d94a1c"
  primary-disabled: "#f9a88e"
  accent-lime: "#e8ff7a"
  accent-lime-active: "#d4eb60"
  ink: "#111111"
  body: "#121212"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-mist: "#ebf2f2"
  surface-card: "#ffffff"
  surface-cool: "#dbe7e8"
  surface-info: "#eaf7fc"
  on-primary: "#ffffff"
  on-accent-lime: "#111111"
  error: "#e45f5f"
  error-deep: "#c25151"
  warning: "#f0b743"

typography:
  display-xl:
    fontFamily: "'Cormorant', 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant', 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant', 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Cormorant', 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Poppins', 'Instrument Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Instrument Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Poppins', 'Instrument Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.1px
  overline:
    fontFamily: "'Instrument Sans', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  badge-label:
    fontFamily: "'Poppins', 'Instrument Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.4px
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: 1.5px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  button-accent:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-accent-lime}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-lime-active}"
    textColor: "{colors.on-accent-lime}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
    position: sticky
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 1px 4px rgba(0,0,0,0.06)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    hoverShadow: 0 4px 16px rgba(0,0,0,0.08)
    imageRatio: 4/5
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
  hero-section:
    backgroundColor: "{colors.surface-mist}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 85vh
  hero-headline:
    typography: "{typography.display-xl}"
    maxWidth: 680px
  hero-subheadline:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    maxWidth: 520px
  badge-promo:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.on-accent-lime}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  feature-block:
    backgroundColor: "{colors.surface-cool}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    textColor: "{colors.ink}"
  feature-block-title:
    typography: "{typography.display-md}"
  feature-block-body:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    typography: "{typography.overline}"
    textColor: "{colors.hairline}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.hairline-soft}"
  search-modal:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    boxShadow: 0 16px 48px rgba(0,0,0,0.12)
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    width: 420px
    padding: "{spacing.lg}"
    boxShadow: -4px 0 24px rgba(0,0,0,0.1)
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.surface-cool}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.hairline}
    activeBorder: 2px solid {colors.primary}
---

## Components

### Buttons

**`button-primary`** — Full-radius pill in Soma orange (#f15623) with white Poppins medium text. On hover the background deepens to `{colors.primary-active}` with a subtle 120ms ease transition. Disabled state fades to `{colors.primary-disabled}` with reduced opacity. Used for Add to Cart, Subscribe, and primary CTAs throughout the funnel.

**`button-secondary`** — White pill outlined in 1.5px `{colors.ink}` that inverts to solid dark fill on hover/active, swapping text to white. Appears alongside primary buttons for "Learn More" or alternate actions where the orange would compete with the main CTA.

**`button-accent`** — Electric chartreuse (#e8ff7a) pill with dark text, reserved for promotional moments: limited-time offers, referral rewards, or seasonal campaigns. The lime pops against both white canvas and the pale blue-green feature blocks without clashing with the orange primary.

### Navigation

**`nav-bar`** — Sticky 64px bar with the Soma wordmark left-aligned, centered navigation links in Poppins medium 14px, and right-aligned icon cluster (search, account, cart with orange dot indicator). A 1px `{colors.hairline-soft}` bottom border appears at rest; on scroll, border drops away in favor of a diffused box shadow for depth.

**`announcement-bar`** — Solid `{colors.ink}` strip above the nav at 40px height, centered caption text in white. Typically carries free-shipping thresholds or subscription promos. Dismissible via an × icon that collapses the bar with a 200ms slide-up.

### Product Display

**`product-card`** — White card with `{rounded.md}` corners and a soft hairline border. Product image fills the top at a 4:5 aspect ratio with object-fit cover. On hover, the card lifts with a 4px/16px shadow and the image scales 1.03× over 300ms. Title in `{typography.title-sm}`, price in bold `{typography.body-md}`, subscription savings shown in a small `{badge-promo}` chip below.

**`subscription-toggle`** — Inline selector on PDP letting users choose one-time purchase vs. subscribe-and-save. Two side-by-side options in a `{rounded.sm}` container; the active option gets a 2px orange border and `{colors.surface-cool}` background fill, the inactive stays neutral. Savings percentage rendered in `{colors.primary}` bold.

### Hero & Feature Sections

**`hero-section`** — Full-bleed section in `{colors.surface-mist}` (the pale aqua-tinted gray) occupying 85vh minimum on desktop. Headline in Cormorant display-xl caps at 680px width; subheadline in Instrument Sans body-lg sits below with a 12px gap. A primary pill button anchors the bottom of the text stack. Product imagery — typically a carafe or pitcher — floats right on desktop, stacking below text on mobile.

**`feature-block`** — Rounded `{rounded.lg}` container in `{colors.surface-cool}` (the blue-green tint) holding a display-md Cormorant headline, body-md description, and often an inline illustration or icon. Used in a 2-up or 3-up grid to communicate filtration technology, sustainability claims, or material sourcing stories.

### Utility Components

**`search-modal`** — Centered overlay with `{rounded.lg}` corners and a generous drop shadow. Input auto-focuses on open; predictive results appear in a scrollable list below with product thumbnails, titles, and prices. Backdrop is a semi-transparent scrim.

**`cart-drawer`** — Right-anchored 420px slide-out panel with line items stacked vertically. Each item shows a small square thumbnail, title, quantity stepper, and line price. Sticky footer contains the subtotal and a full-width `button-primary` for checkout. The drawer casts a soft left-edge shadow.

**`badge-promo`** / **`badge-new`** — Small pill badges using `{rounded.full}`. Promo badges sit in chartreuse for subscription/sale callouts; new badges use `{colors.primary}` orange for recently launched products. Both use the `{typography.badge-label}` uppercase treatment at 11px.

### Footer

**`footer`** — Dark `{colors.ink}` background spanning full width with generous `{spacing.section}` vertical padding. Column headings use `{typography.overline}` in muted gray; links below in `{typography.body-sm}` lighten to `{colors.hairline-soft}`. Bottom row holds copyright, payment icons, and social links in a single horizontal line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger + cart icon. Hero stacks vertically (text above image). Product grid becomes horizontal swipe rail. Feature blocks stack full-width. Cart drawer becomes full-screen overlay. Display-xl drops to 36px. |
| Tablet | 744–1128px | Two-column product grid. Hero image shrinks to 50% width beside text. Nav links remain visible but spacing tightens. Feature blocks arrange in 2-up grid. Section padding reduces to 48px. |
| Desktop | 1128–1440px | Three-column product grid. Full nav with all links visible. Hero runs side-by-side at roughly 55/45 text-to-image split. Full 64px section spacing. Cart drawer at 420px width. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Side margins grow symmetrically. Image assets scale to higher resolution. Hero image can extend slightly beyond content boundary for dramatic effect. |

### Touch Targets
- All interactive elements maintain 48px minimum tap target on mobile
- Cart quantity steppers use 44px square touch zones with 8px gap between + and −
- Navigation hamburger icon padded to 48×48px hit area
- Product card entire surface is tappable, not just the title text
- Dismiss/close icons (announcement bar, modals) padded to 40×40px minimum

### Collapsing Strategy
- Top navigation links collapse into a full-screen slide-over menu below 744px, with links stacked vertically at 56px row height
- Product filter bar on collection pages collapses into a bottom-sheet modal on mobile
- Footer columns collapse into accordions with `{typography.title-sm}` headings and chevron indicators
- Feature block grids move from 3-up → 2-up → stacked single column as viewport narrows
- Announcement bar text truncates with ellipsis on very narrow viewports; a "Details" tap expands it

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius values on product cards could not be confirmed to the pixel; `{rounded.md}` (12px) is an approximation based on visual inspection
- Cormorant font weight mapping (whether the site uses 500 vs 600 for display) could not be verified from extraction alone
- Poppins usage scope is inferred — it may be limited to buttons and navigation or extend further into UI chrome
- No motion/animation tokens were extractable; transition durations (120ms, 200ms, 300ms) are estimated from typical Shopify theme patterns
- Icon system (line weight, size grid, stroke vs fill) was not captured in extraction
- Dark-mode palette is not present; the site appears to be light-only
- Exact max-width of content container (assumed 1440px) could not be confirmed
- Cart drawer width and subscription toggle specifics are inferred from common Shopify DTC patterns rather than direct measurement
