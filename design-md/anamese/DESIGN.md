---
version: alpha
name: "Anamese"
source_url: "https://www.anamese.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Terracotta warmth rendered in pixels — Anamese opens with a coral accent (#fb8077) that echoes kiln-fired clay against a restrained grayscale field, an unusual chromatic choice for a garden brand that signals handcraft over horticulture. The typographic pairing is equally deliberate: Abel, a condensed geometric sans-serif, handles display and navigation with the vertical economy of a nursery plant tag, while Alegreya — a humanist serif with calligraphic stroke modulation — carries body copy and product descriptions, lending the prose a texture closer to letterpress than screen. This split personality (industrial precision up top, artisanal warmth in the paragraph) mirrors the product line itself: architecturally clean planter silhouettes finished with organic glazes and patinas. The layout breathes through generous section spacing (`{spacing.section}`) and a near-white canvas (#ffffff) that lets product photography — typically a single vessel against a poured-concrete or raw-linen backdrop — dominate the viewport without chromatic competition. Cards sit at `{rounded.sm}` with hairline borders (#e2e2e2), never casting heavy shadows; the containers sell weight and material, so the UI stays paper-thin. Navigation employs `{typography.nav-link}` in Abel at 600 weight, uppercase with restrained letter-spacing, reading like gallery signage. Buttons pull the coral forward at full saturation for primary actions, dropping to a ghost outline for secondary interactions — the brand trusts the single warm hit to carry hierarchy without needing a second accent. On mobile, the condensed display type holds up at narrower widths than a proportional sans would, keeping headlines punchy without multi-line wrapping down to 320px. The overall system reads as a ceramics-studio lookbook transplanted into e-commerce: quiet, materially honest, and anchored by that one unmistakable blush of fired earth.

colors:
  primary: "#fb8077"
  primary-active: "#e5665d"
  primary-disabled: "#fdc8c4"
  ink: "#191919"
  body: "#555555"
  muted: "#777777"
  hairline: "#e2e2e2"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  coral-light: "#fff0ef"
  footer-bg: "#191919"
  footer-text: "#e2e2e2"

typography:
  display-xl:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.3px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase
  title-md:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.15px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
    textTransform: uppercase
  body-md:
    fontFamily: "'Alegreya', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Alegreya', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  product-title:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  product-price:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  footer-link:
    fontFamily: "'Abel', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  mono:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 0
    border: none
    borderBottom: 1px solid {colors.primary}
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 1px 0 {colors.hairline}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: none
    imageAspectRatio: 1 / 1
    titleTypography: "{typography.product-title}"
    priceTypography: "{typography.product-price}"
    padding: 0
    gap: "{spacing.sm}"
  product-card-hover:
    opacity: 0.85
    transition: opacity 0.3s ease
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 85vh
    padding: "{spacing.section-lg} {spacing.xl}"
    textAlign: center
  hero-split:
    backgroundColor: "{colors.canvas}"
    imageWidth: 55%
    contentWidth: 45%
    contentPadding: "{spacing.section} {spacing.xxl}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} 0 {spacing.lg}"
    textAlign: center
    borderBottom: 1px solid {colors.hairline-soft}
  category-badge:
    backgroundColor: "{colors.coral-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.footer-link}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  search-overlay:
    backgroundColor: "rgba(25, 25, 25, 0.6)"
    contentBackground: "{colors.canvas}"
    inputTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    maxWidth: 640px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    thumbnailSize: 72px
    thumbnailBorder: 1px solid {colors.hairline}
    thumbnailActiveBorder: 1px solid {colors.ink}
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  pagination:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    gap: "{spacing.sm}"
    height: 36px

---

## Components

### Buttons

**`button-primary`** — Solid coral (#fb8077) fill with white uppercase Abel text tracked at 1.2px. Corners are barely broken (`{rounded.xs}` = 2px), reading almost square to match the geometric precision of the planter forms. On hover the fill darkens to `{colors.primary-active}`; disabled state fades to a blush pink (`{colors.primary-disabled}`) and suppresses pointer events.

**`button-secondary`** — Ghost button with a 1px ink border and uppercase ink text. On hover the fill inverts to solid ink with white text, creating a decisive flip rather than a gradual transition. Used for "View Collection" and secondary CTAs where the coral would compete with product imagery.

**`button-ghost`** — Text-only link-button in coral with a 1px bottom border. No background, no side padding. Appears inline within editorial blocks as a "Shop Now →" or "Learn More" prompt.

### Navigation

**`nav-bar`** — Fixed 72px white bar with a subtle hairline bottom border. Logo centered or left-aligned, nav links in `{typography.nav-link}` spaced at `{spacing.lg}`. On scroll, the hairline disappears in favor of a soft box-shadow to lift the bar off content. Mobile collapses to a hamburger with a full-screen slide-in panel.

**`announcement-bar`** — 36px-tall strip in solid ink (#191919) at the viewport top, carrying one line of `{typography.caption}` text in white. Used for wholesale minimum-order notices or shipping thresholds.

### Product Display

**`product-card`** — Zero-radius card with a square 1:1 image container and no visible border. Product title in `{typography.product-title}` (Abel uppercase) sits directly below the image with `{spacing.sm}` gap. Price in `{typography.product-price}`. On hover the entire image fades to 85% opacity — no scale transform, no shadow — keeping the grid visually stable. The absence of decoration forces the pottery to be the only texture on screen.

**`image-gallery`** — Product detail page gallery with a large hero image on a soft-gray background and a horizontal thumbnail strip below. Thumbnails are 72px squares with a hairline border; the active thumbnail switches to an ink border. No rounded corners anywhere — consistent with the product-card language.

### Layout Sections

**`hero-section`** — Full-bleed section at 85vh minimum with centered `{typography.display-xl}` headline and `{typography.body-md}` subtitle. Background is either a flat `{colors.surface-soft}` tint or a full-width lifestyle photograph of planters in situ. Text overlays on images use a subtle dark gradient scrim from bottom.

**`hero-split`** — Two-column layout with a 55/45 image-to-content ratio. The image panel bleeds to the edge; the content panel carries headline, body copy, and a primary CTA with `{spacing.section}` vertical padding. Used for featured collections or brand-story blocks.

**`collection-header`** — Centered `{typography.display-md}` title with generous top padding (`{spacing.xxl}`) and a hairline-soft bottom border. Introduces the product grid without competing for attention.

### Utility Components

**`category-badge`** — Small pill in `{colors.coral-light}` background with `{colors.primary-active}` text. `{rounded.xs}` corners and tight padding. Used within product cards or collection pages to tag material or finish types (e.g., "GLAZED", "FIBER CLAY").

**`breadcrumb`** — Muted-tone path segments in `{typography.caption}` separated by "/" characters. The final (current) segment renders in `{colors.ink}`. Sits below the nav with `{spacing.base}` top margin.

**`search-overlay`** — Modal overlay with a 60% dark scrim. A centered white panel (max 640px) contains a full-width text input and instant results list. No border-radius — the panel reads as a clean sheet laid over the viewport.

**`pagination`** — Compact row of page numbers in `{typography.caption}`, the active page set in `{colors.ink}` while inactive pages stay in `{colors.muted}`. No background shapes — pure typographic pagination.

### Footer

**`footer`** — Dark ink background (#191919) with `{typography.footer-link}` text in a warm light gray (#e2e2e2). Multi-column grid with section headings in `{typography.title-sm}`. Newsletter signup input maintains the same `{rounded.xs}` treatment as site-wide inputs. Social icons render at 20px in the footer text color.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2-up on 375px+), hero at 100vh with stacked text, nav collapses to hamburger + slide panel, footer stacks to single column, section padding drops to `{spacing.xl}` |
| Tablet | 744–1128px | 3-column product grid, hero-split stacks image above content, nav links visible but tighter spacing, footer 2-column |
| Desktop | 1128–1440px | 4-column product grid, hero-split side-by-side at 55/45, full nav with all links and search icon, `{spacing.section}` vertical rhythm |
| Wide | > 1440px | Content max-width 1440px centered, product grid may expand to 5 columns, hero imagery scales to fill with object-fit: cover, increased lateral padding |

### Touch Targets

- All interactive elements maintain a 44px minimum tap target on mobile
- Product card tap area covers the full card surface including image and text
- Nav hamburger icon padded to 48×48px hit zone
- Pagination numbers spaced at minimum `{spacing.base}` to prevent mis-taps
- Ghost buttons receive 12px vertical padding boost on touch devices

### Collapsing Strategy

- Navigation links collapse into a full-screen overlay panel (not a dropdown) with `{typography.title-md}` sized links stacked vertically
- Product grid transitions from 4 → 3 → 2 columns; never falls to single column above 375px
- Hero-split sections stack vertically with image on top at tablet breakpoint; image maintains 16:9 aspect ratio when stacked
- Footer columns collapse from 4 → 2 → 1 with `{spacing.lg}` gaps between groups
- Announcement bar text truncates with ellipsis on very narrow viewports; critical content limited to 40 characters

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No CSS custom properties or design-token JSON were exposed in the page source; color extraction relies on computed styles of rendered elements
- Abel weight range could not be confirmed — Google Fonts hosts it as a single 400-weight file; if the live site uses a variable or multi-weight version, actual weight values may differ
- Alegreya italic and bold variants usage on the live site could not be verified from static extraction
- Exact border-radius values are estimated from visual inspection; the site may use 0px universally (all observed corners appeared square)
- Hover/focus transition durations and easing functions were not captured
- Specific box-shadow values for elevated states (modals, dropdowns) could not be extracted
- The monospace font stack appears in the extracted data but its application context (code blocks, SKU displays, or input formatting) is unclear
- Wholesale-specific UI patterns (login gate, price tiers, minimum-order warnings) may exist behind authentication and were not observed
