---
version: alpha
name: "Kumi Contemporary"
source_url: "https://www.kumicontemporary.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  EB Garamond at display sizes runs against expectations here — a sixteenth-century European serif deployed as the primary editorial voice for Japanese pop art and contemporary screenprint, producing a productive friction that the site wears without apology. The interactive layer belongs to a blue family that feels calibrated rather than chosen: #4885cd anchors links and primary CTAs, deepening to #1e4cbb under active pressure and stepping up toward #5996ca and #5a91d2 for softer hover states. This blue is not an accent sitting atop a neutral canvas — it is the site's primary visual temperature, cooling the warm near-white ground (#f7f7f6, #fdfdfd) that reads closer to aged vellum than clinical exhibition white. Red enters with clear intent: #ce0a0a marks pricing and sale conditions, escalating through #d74242 to #ff5858 when urgency calls, a convention borrowed from auction-house culture and applied to a measured gallery context. Lato carries navigation and body copy at unhurried weights, functioning as a neutral infrastructure that refuses to compete with photography. Warm earth tones — #d1b38d (tea-stained paper) and #de6d1a (iron-red ink) — appear as supplementary accents alongside a quiet olive at #888929, material echoes rather than decorative choices. Cards breathe inside a surface-card of #eeeeee; hairlines hold at #e0e0e0. Corners are minimally rounded, inputs and small buttons taking {rounded.xs}, the design deliberately avoiding the pill shapes that read as SaaS rather than gallery. The dark foundation — #111111 for type, #121212 for footer field — grounds without going full void.

colors:
  primary: "#4885cd"
  primary-active: "#1e4cbb"
  primary-hover: "#5996ca"
  primary-light: "#5a91d2"
  primary-disabled: "#b0c8e8"
  accent-red: "#ce0a0a"
  accent-red-hover: "#d74242"
  accent-red-bright: "#ff5858"
  accent-warm: "#de6d1a"
  accent-earth: "#d1b38d"
  accent-olive: "#888929"
  ink: "#111111"
  body: "#222222"
  muted: "#7a7a7a"
  muted-light: "#888888"
  hairline: "#e0e0e0"
  hairline-soft: "#ececec"
  canvas: "#fdfdfd"
  surface-soft: "#f5f5f6"
  surface-card: "#eeeeee"
  surface-strong: "#e8e8e8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  dark-ground: "#121212"
  near-black: "#171717"

typography:
  display-xl:
    fontFamily: "'EB Garamond', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Conv_AvenirLTStd-Book', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Conv_AvenirLTStd-Book', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Lato', 'Conv_AvenirLTStd-Book', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Conv_AvenirLTStd-Book', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Conv_AvenirLTStd-Book', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Lato', 'Conv_AvenirLTStd-Book', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Lato', 'Conv_AvenirLTStd-Book', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Lato', 'Conv_AvenirLTStd-Book', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  price-display:
    fontFamily: "'Lato', 'Conv_AvenirLTStd-Book', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  artwork-label:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  artist-name-lg:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  tag-label:
    fontFamily: "'Lato', 'Conv_AvenirLTStd-Book', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.8px
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
    hoverBackgroundColor: "{colors.primary-hover}"
    activeBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    hoverBackgroundColor: "{colors.surface-soft}"
  button-enquire:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 36px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.ink}"
    activeLinkColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageContainerBackground: "{colors.surface-card}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
    artworkTitleTypography: "{typography.artwork-label}"
    artistTypography: "{typography.artist-name-lg}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.accent-red}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    hoverShadow: "0 2px 12px rgba(0,0,0,0.10)"
  artwork-hero:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    artistTypography: "{typography.display-sm}"
    artistColor: "{colors.body}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.body}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.accent-red}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.xl}"
  artist-profile-header:
    backgroundColor: "{colors.canvas}"
    nameTypography: "{typography.display-md}"
    nameColor: "{colors.ink}"
    bioTypography: "{typography.body-md}"
    bioColor: "{colors.body}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.xl}"
  category-badge:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.muted}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  price-badge:
    textColor: "{colors.accent-red}"
    typography: "{typography.price-display}"
  availability-badge-available:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  availability-badge-sold:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  filter-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    labelTypography: "{typography.nav-link}"
    labelColor: "{colors.body}"
    activeLabelColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    paddingVertical: "{spacing.md}"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
    iconColor: "{colors.muted}"
    focusBorderColor: "{colors.primary}"
    focusBackgroundColor: "{colors.canvas}"
  gallery-section-header:
    typography: "{typography.display-sm}"
    color: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.md}"
    marginBottom: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.dark-ground}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary-light}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    paddingVertical: "{spacing.xxl}"
  lightbox-overlay:
    scrimColor: "rgba(17,17,17,0.92)"
    imageBackground: "{colors.near-black}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.on-dark}"
    closeButtonColor: "{colors.on-dark}"

## Components

### Buttons
**`button-primary`** — A 40px blue (#4885cd) button with 4px corners and Lato semi-bold 14px at 0.5px tracking, used for "Add to Cart," "View Work," and newsletter sign-up. Hover lifts to #5996ca; active state presses to #1e4cbb, maintaining coherence within the blue family. Disabled renders in #b0c8e8 at reduced visual weight.

**`button-secondary`** — Same 40px dimensions, stroked in primary blue against near-white canvas. Used for supporting actions like "View Artist Profile" and "Back to Gallery." Hover shifts the fill to surface-soft while holding the border color — a conservative treatment that keeps the hierarchy clear.

**`button-enquire`** — An ink-black (#111111) CTA used on artwork detail pages for collector inquiry. The dark tone signals gravity and deliberateness, separating the act of inquiry from the lighter e-commerce add-to-cart gesture. No hover color shift — opacity drops to 0.85 instead.

### Text Input & Search
**`text-input`** — 36px, 4px corners, 1px hairline border in resting state. Focus upgrades the border to primary blue with no background shift. Placeholder in muted gray (#7a7a7a). Used in enquiry forms, contact pages, and checkout fields.

**`search-input`** — Softer variant: surface-soft fill (#f5f5f6) at rest, collapsing to canvas on focus. Icon in muted gray sits inset right. 8px corners give it a fractionally warmer appearance than the sharp form inputs. Appears in the top-right nav region at 36px tall.

### Navigation
**`nav-bar`** — 60px fixed header on canvas white. Lato 13px with 0.5px letter-spacing — the tracking introduces a gallery-appropriate formality without requiring uppercase. Kumi wordmark left in ink-black; right side carries search icon, cart, and account. Primary menu items render in body color (#222222) and turn primary blue on hover or active state. A hairline-soft border (#ececec) separates the bar from content.

### Product / Artwork Cards
**`product-card`** — Square or portrait image on surface-card (#eeeeee) with no border-radius applied to the image container. Below the image: artwork title in EB Garamond 18px, artist name in EB Garamond 20px, price in Lato 700 colored accent-red (#ce0a0a), availability badge as a caption-size tag. The card frame itself has no rounded corners. On hover, a 12px diffuse shadow lifts the card without animation distraction.

### Artwork Hero
**`artwork-hero`** — The primary detail view. Title in {typography.display-xl} (EB Garamond 48px, weight 400) — the low weight is intentional, keeping the serif from overwhelming the adjacent photography. Artist credit renders in {typography.display-sm} at #222222. Price runs large in accent-red below. Description body copy at Lato 15px / 1.6 line-height accommodates catalogue-length provenance and medium notes. The enquire button sits below price at full width on mobile, 40px on desktop.

### Artist Profile Header
**`artist-profile-header`** — Name in {typography.display-md} (EB Garamond 32px), biography in {typography.body-md} below. A 1px hairline below the bio block separates the header region from the work grid. No hero imagery required by default — the name-and-text pairing is treated as sufficient orientation for a collector audience.

### Category & Filter Badges
**`category-badge`** — Uppercase Lato 11px (0.8px letter-spacing) on surface-strong (#e8e8e8). Interactive: hover fills with primary blue and inverts text to white, giving the filter tags a toggle-style feel. Used for medium and genre filters (Ukiyo-e, Pop Art, Screenprint, Limited Edition, etc.).

**`filter-bar`** — Horizontal strip of nav-link-size category labels, the active one marked by a 2px primary-blue bottom border (no background fill). Sits directly below the nav on index and artist pages. Scrolls horizontally on mobile without wrapping.

### Price & Availability
**`price-badge`** — Inline Lato 700 16px in accent-red (#ce0a0a). No background or container border — the red weight alone signals the figure as a purchase anchor. Sold or unavailable works grey the price to {colors.muted}.

**`availability-badge-available`** and **`availability-badge-sold`** — Small caption-size tags (12px, 4px corners). Available state: surface-soft background with hairline border. Sold state: surface-strong with muted text. Both appear below the price in cards and on the detail view.

### Gallery Section Header
**`gallery-section-header`** — Section titles (e.g., "Featured Works," "New Arrivals") in EB Garamond 24px at ink-black, with a 1px hairline beneath and 32px margin below before the grid. The serif header over a flush grid reads as catalogue chapter-opening rather than product listing.

### Footer
**`footer`** — Dark-ground (#121212) field. Section headings in title-sm (Lato 700 14px, 0.2px tracking) at on-dark white. Links rendered in primary-light (#5a91d2) for visibility on the dark field without requiring full brightness. Newsletter input sits inline with a primary-colored submit button. Column grid: 4-up desktop, 2-up tablet, stacked mobile.

### Lightbox Overlay
**`lightbox-overlay`** — A 92% black scrim over site content. Image centered on near-black (#171717) field. Caption and medium/dimensions below in caption typography at on-dark white. Close control top-right, minimum 44×44px hit area.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; nav collapses to hamburger; artwork-hero stacks vertically with enquire button full-width; filter-bar scrolls horizontally; display-xl scales to 32px |
| Tablet | 744–1128px | 2-column artwork grid; nav shows primary categories, collapses secondary into dropdown; artwork-hero side-by-sides image and detail panel |
| Desktop | 1128–1440px | 3-column artwork grid; nav fully expanded; artwork-hero holds 50/50 image–detail split with generous internal padding |
| Wide | > 1440px | Max-width 1440px centered; optional 4-column grid; section padding increases to accommodate wider whitespace |

### Touch Targets
- All nav links padded to minimum 44px height on mobile
- Filter-bar labels padded to 44px tall touch targets on mobile
- Card interactions converted from hover to tap with immediate border feedback
- Lightbox close button enforces 44×44px minimum hit area regardless of icon size
- Enquire and primary buttons minimum 44px height on mobile (override desktop 40px)

### Collapsing Strategy
- Primary nav: full horizontal labels → hamburger menu at < 744px; search icon persists in both states
- Filter bar: horizontal overflow scroll on mobile — no wrapping, no stacking
- Artwork hero: stacks image over title/artist/price/enquire on mobile; EB Garamond display-xl reduces from 48px to 32px
- Footer: 4-column → 2-column → single-column at each breakpoint; newsletter row goes full-width at mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `Conv_AvenirLTStd-Book` is a converted private font file; additional weight and italic cuts not confirmed — Lato used as functional fallback throughout
- Exact button height for primary CTA on artwork detail pages not confirmed from extraction; 40px assumed from observed gallery UI conventions
- Hover and active transition timing values (duration, easing) not extracted
- Whether EB Garamond loads via Google Fonts API or self-hosted file not confirmed
- Mobile navigation pattern (slide drawer vs. fullscreen overlay) not confirmed from extraction
- Exact grid column count and gutter width for artwork index pages not extracted
- Dark mode support not confirmed; extraction suggests light-only treatment
- Specific padding values inside product cards not extracted; {spacing.md} is an informed estimate
- Font Awesome 5 Pro icon set referenced in font stacks but specific icons used for UI controls not catalogued
