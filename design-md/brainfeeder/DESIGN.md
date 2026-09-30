---
version: alpha
name: "Brainfeeder"
source_url: "https://www.brainfeeder.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The shop grid for Flying Lotus's Los Angeles imprint loads like a darkroom under ultraviolet light — album artwork bleeds edge-to-edge against a near-zero-luminance canvas ({colors.canvas} approximated #060608), each release functioning as its own color event rather than a tile in a conventional merchandise grid. Brainfeeder's digital identity mirrors its curatorial one: cosmic, uncompromising, and lit from within. The primary voltage is an electric violet ({colors.primary} approximated #7042f8), a frequency that sits somewhere between deep-space photography and the neural imagery anchoring the label's logo since its 2008 founding by Flying Lotus in the experimental Los Angeles tradition of Leimert Park. Typography runs lean and modern against dark surfaces — sans-serif stacks at modest weights, because the visual muscle in this system comes from artwork and color, not typographic decoration. Display headings materialize above the catalog grid without competing with it; captions and release metadata recede into the surface in muted slate ({colors.muted}), present but unobtrusive. A phosphorescent cyan ({colors.accent-cyan}) punctuates links and hover states, creating the impression of live signal rather than applied style. No hard corners appear in the shop UI; product cards carry a modest {rounded.sm} radius that softens edges without reading as consumer-friendly — a catalog of Thundercat, Lapalux, Tokimonsta, and Flying Lotus himself demands a certain earned strangeness in the container. Navigation is stripped to wordmark at top-left, a minimal link set, and a cart icon at right; the page spends its energy on the catalog grid. Releases receive room: generous {spacing.xl} gutters between cards, full-bleed cover art that saturates without compression, and a title plus artist credit pair below in body-md. The footer collapses to a dark block barely distinguishable from the canvas, housing label info and social links in caption-scale type. Buy buttons use the primary violet on dark, reversing the conventional dark-text-on-light rule — in this color system, the background is the statement and the call to action is a momentary interruption of it. Note: all hex values and font stacks below are approximations derived from brand knowledge; no live extraction data was available.

colors:
  primary: "#7042f8"
  primary-active: "#5530d4"
  primary-disabled: "#3a2080"
  ink: "#ffffff"
  body: "#d8d8e8"
  muted: "#8888a0"
  hairline: "#2a2a3a"
  hairline-soft: "#1e1e2a"
  canvas: "#060608"
  surface-soft: "#0e0e16"
  surface-card: "#12121c"
  on-primary: "#ffffff"
  accent-cyan: "#00e5ff"
  accent-pink: "#ff3b6b"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  release-meta:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.36
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px

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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    hoverTextColor: "{colors.ink}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline-soft}"
    height: 64px
    padding: "0 {spacing.xl}"
    logoColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "1/1"
    imageOverflow: hidden
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    padding: "{spacing.sm}"
    hoverTransform: scale(1.02)
    hoverTransition: 200ms ease
  hero-grid:
    backgroundColor: "{colors.canvas}"
    columns: 2
    gap: "{spacing.base}"
    padding: "{spacing.section}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.body}"
  release-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-cyan}"
    typography: "{typography.release-meta}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
  catalog-filter:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    activeBorder: "1px solid {colors.hairline}"
    typography: "{typography.release-meta}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    hoverTextColor: "{colors.body}"
  search-overlay:
    backgroundColor: "{colors.scrim}"
    backdropOpacity: 0.92
    inputBackgroundColor: "{colors.surface-soft}"
    inputTextColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    resultHoverColor: "{colors.surface-card}"
    accentColor: "{colors.accent-cyan}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xxl} {spacing.xl}"
  cart-drawer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderLeft: "1px solid {colors.hairline}"
    width: 380px
    overlayColor: "{colors.scrim}"
    overlayOpacity: 0.7
  artist-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    hoverBorder: "1px solid {colors.primary}"
    hoverTextColor: "{colors.ink}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline-soft}"
    paddingBottom: "{spacing.md}"
    marginBottom: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — Electric violet (#7042f8) fill on dark canvas with uppercase spaced label in `{typography.button-md}`. The low-contrast environment inverts conventional hierarchy: the button reads as a burst of color rather than a structural element. Active state deepens to `{colors.primary-active}` (#5530d4); disabled collapses to `{colors.primary-disabled}` with muted label. Corner radius is minimal `{rounded.xs}` — just enough to break the mechanical rectangle without softening the brand's harder edge.

**`button-secondary`** — Transparent fill with a `{colors.hairline}` border on `{colors.canvas}`, matching the label's preference for restraint outside the primary CTA. Hover gains a subtle `{colors.surface-soft}` fill so the interaction registers without introducing a new color. Used for secondary actions like "View All" and genre-filter triggers.

**`button-ghost`** — No border, no fill; `{colors.muted}` label that brightens to `{colors.ink}` on hover. Used for in-grid navigation, sort controls, and tertiary actions where any additional visual weight would compete with album art.

### Text Input

**`text-input`** — Dark surface (`{colors.surface-soft}`) with `{colors.hairline}` border, transitioning to `{colors.primary}` border on focus. Matches the site's ambient dark tone so the form field reads as a recess in the page rather than a floating white box. Placeholder text in `{colors.muted}` disappears gracefully without calling attention to itself.

### Navigation

**`nav-bar`** — Full-width `{colors.canvas}` strip at 64px height, anchored by a label wordmark left and cart icon right. `{typography.nav-link}` links sit in the center region (Shop, Artists, About) at `{colors.body}` with a `{colors.ink}` hover. The `{colors.hairline-soft}` bottom border is subtle enough to read as a shadow rather than a structural divide. On scroll past 100px the bar gains a `{colors.surface-card}` background upgrade for legibility over content.

### Product Card

**`product-card`** — The catalog's primary unit. Square aspect ratio (1:1) image fills the card top; a thin `{spacing.sm}` pad below carries the release title in `{typography.title-md}` and artist + format in `{typography.caption}` / `{colors.muted}`. Card background is `{colors.surface-card}` (#12121c), keeping each artwork island dark even before the image loads. On hover the artwork scales 1.02× over 200ms, communicating interactivity without lifting the card off the plane. `{rounded.sm}` corners prevent the grid from reading as a rigid matrix.

### Hero Grid

**`hero-grid`** — The featured-release zone at the top of the shop. Two-column layout on desktop, full-bleed image on left, text block on right. Title in `{typography.display-xl}` with `{colors.ink}`, subtitle / release blurb in `{typography.body-md}` / `{colors.body}`. `{spacing.section}` padding isolates it from the catalog below. The left image may be full-bleed to the viewport edge on wide breakpoints.

### Release Badge

**`release-badge`** — Inline label used to mark new releases, limited editions, or format variants (LP, Cassette, Digital). `{colors.accent-cyan}` text on `{colors.surface-soft}` background in `{typography.release-meta}` uppercase. The cyan reads as a phosphorescent highlight against the near-black surface — consistent with the label's light-from-within visual logic. Placed top-left on product-card images or inline next to release titles.

### Catalog Filter

**`catalog-filter`** — Pill-shaped `{rounded.full}` toggle row above the grid for filtering by format or artist. Inactive pills show `{colors.muted}` label on transparent ground; active gains a `{colors.hairline}` border and `{colors.ink}` label. `{typography.release-meta}` uppercase keeps the row visually subordinate to the grid below it.

### Search Overlay

**`search-overlay`** — Full-viewport scrim at 92% opacity with a centered `{text-input}` variant. Results list below the input uses `{colors.surface-card}` row hover. The phosphorescent `{colors.accent-cyan}` marks the matched text fragment in each result. Dismissed by Escape or clicking outside.

### Footer

**`footer`** — Minimal dark strip. `{typography.caption}` links in `{colors.body}` brighten to `{colors.ink}` on hover. Label copyright and social icons (Bandcamp, Instagram, Twitter/X) are the only occupants. The `{colors.hairline-soft}` top border is the sole divider from page content; the footer does not introduce a new background tier.

### Cart Drawer

**`cart-drawer`** — Slides in from the right at 380px width. `{colors.surface-card}` background with `{colors.hairline}` left border. Line items show artwork thumbnail at 64×64, title in `{typography.title-md}`, format/price in `{typography.body-sm}`. Checkout button at base uses `button-primary`. Background scrim at 70% `{colors.scrim}`.

### Artist Pill

**`artist-pill`** — Small `{rounded.full}` chip linking to an artist's catalog page. Used in release metadata rows and on artist index pages. `{colors.surface-soft}` background, `{colors.body}` label, hover adds a `{colors.primary}` border — the violet signals the label's identity without overriding the neutral default state.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column catalog grid; nav collapses to hamburger menu with full-screen dark drawer; hero becomes single-column stack with image above text; cart drawer goes full-width |
| Tablet | 744–1128px | Two-column catalog grid; nav links visible but compressed; hero grid maintains two columns at reduced padding; filter pills scroll horizontally |
| Desktop | 1128–1440px | Three-column catalog grid; full nav with all links; hero grid at full spec; filter pills wrap naturally |
| Wide | > 1440px | Four-column catalog grid; hero image bleeds to viewport edge on left; content max-width ~1440px centered |

### Touch Targets

- All interactive elements (pills, card overlays, nav links) minimum 44×44px tap target
- Filter pills padded to 44px height on mobile even if visually shorter
- Cart icon touch target extends to full nav-bar height (64px)
- Product cards fill column width; full card area is tappable

### Collapsing Strategy

- Primary nav collapses to hamburger at < 744px; drawer opens over scrim with label links in `{typography.display-md}` scale for legibility
- Hero grid stacks vertically below 744px; image takes full viewport width at 56vw height
- Release badges remain visible at all breakpoints but reduce padding to 3px 6px on mobile
- Footer links reflow to two-column grid on mobile rather than single horizontal row
- Cart drawer becomes full-width bottom sheet on mobile (height: 80vh, `{rounded.lg}` top corners)

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex values are approximations** — the live site returned no extractable hex tokens. Colors are derived from brand knowledge of Brainfeeder's documented dark/cosmic aesthetic, not from a live crawl. Treat as starting estimates requiring visual verification against the actual site.
- **Font stacks unverified** — no `font-family` declarations were extracted. The Inter fallback stack used here is a placeholder; the site may use a custom or licensed typeface (e.g. a grotesque with optical sizing or a display face for the wordmark).
- **Primary accent color unconfirmed** — the electric violet (#7042f8) reflects the label's general psychedelic palette but has not been confirmed from source CSS. The site may use a different primary hue (electric blue, deep magenta, or a shifting gradient).
- **Component interaction states** — hover, focus, and active state timing and easing values are estimated; no motion tokens were extractable.
- **Shopify or custom platform unknown** — platform-shopify returned False but the underlying e-commerce stack is unconfirmed; checkout flow components (address form, payment, order confirmation) are not modeled here.
- **Logo and wordmark assets** — exact logo treatment, sizing, and dark/light variant availability not verified.
- **Limited-edition or drop mechanics** — the label may operate countdown timers, waitlist components, or exclusive-access gates for limited releases; these are not modeled due to insufficient data.
