---
version: alpha
name: "Art & Fable Puzzle Company"
source_url: "https://www.artandfablepuzzles.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Gold foil stamping on a matte-black puzzle box — that tactile promise of gallery-grade reproduction carries directly into the digital storefront, where deep teal (#1e4d4f) frames each artwork thumbnail like a museum wall panel. The canvas reads warm ivory (#faf7f2) rather than clinical white, giving product imagery the soft ambient light of a private viewing room. Display headlines arrive in a refined serif stack reminiscent of exhibition catalogs, set large and light-weighted to defer to the artwork itself; body copy drops to a clean geometric sans at 16px for legibility against those warm backgrounds. Navigation stays spare — a single sticky bar with the logotype left-justified and a minimal icon cluster right — because the art does the selling. Product cards float on `{rounded.sm}` with generous `{spacing.lg}` gutters, each one a self-contained gallery frame showing puzzle image, piece count badge, and artist attribution in `{typography.caption}`. The primary CTA (#c49a3c, a burnished gold drawn from frame-gilding tradition) appears only where purchase intent lives: "Add to Cart," "Shop Now," quick-view overlays. Hover states deepen to #a67f2a, reinforcing the brass-to-patina metaphor. A secondary dark teal (#1e4d4f) anchors the footer, newsletter module, and category navigation links, establishing a two-anchor palette — gold for commerce, teal for wayfinding. Piece-count badges use small pill shapes (`{rounded.full}`) in the surface-soft tone, keeping the visual hierarchy art-first, metadata-second. Spacing is deliberately generous: section gaps run 64–80px, card grids breathe at 24px, and the hero area often surrenders 60%+ of viewport to a single painting detail at full bleed.

colors:
  primary: "#c49a3c"
  primary-active: "#a67f2a"
  primary-disabled: "#e4d3a8"
  secondary: "#1e4d4f"
  secondary-active: "#163b3d"
  secondary-disabled: "#a3c4c5"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#6b6b6b"
  muted-soft: "#999999"
  hairline: "#ddd8d0"
  hairline-soft: "#eae6df"
  canvas: "#faf7f2"
  surface-soft: "#f3efe8"
  surface-card: "#ffffff"
  surface-dark: "#1e4d4f"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  on-dark: "#faf7f2"
  badge-bg: "#f3efe8"
  badge-text: "#3d3d3d"
  artist-credit: "#6b6b6b"
  star-rating: "#c49a3c"
  overlay-scrim: "rgba(26,26,26,0.55)"

typography:
  display-xl:
    fontFamily: "'Playfair Display', 'Georgia', 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', 'Georgia', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Playfair Display', 'Georgia', serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Playfair Display', 'Georgia', serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.1px
  artist-name:
    fontFamily: "'Playfair Display', 'Georgia', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    fontStyle: italic
  piece-count:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.4px
  uppercase-tag:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
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
  section-lg: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.secondary}"
  button-secondary-active:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: 8px 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.secondary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.04)"
    hoverBoxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    transition: "box-shadow 0.2s ease, transform 0.2s ease"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
    objectFit: cover
  piece-count-badge:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.piece-count}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 520px
    padding: "{spacing.section} {spacing.xl}"
    typography: "{typography.display-xl}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-dark}"
    opacity: 0.85
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} 0 {spacing.lg}"
    textAlign: center
  artist-attribution:
    typography: "{typography.artist-name}"
    textColor: "{colors.artist-credit}"
    padding: "{spacing.xs} 0"
  difficulty-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  newsletter-module:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl} {spacing.xl}"
  newsletter-input:
    backgroundColor: "rgba(255,255,255,0.12)"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid rgba(255,255,255,0.25)"
    focusBorder: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-secondary}"
    typography: "{typography.nav-link}"
    opacity: 0.8
    hoverOpacity: 1
  quick-view-overlay:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 16px 48px rgba(0,0,0,0.18)"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: "/"
    activeColor: "{colors.ink}"
  star-rating:
    fillColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: "{spacing.xxs}"
---

## Components

### Buttons

**`button-primary`** — The gold CTA used for purchase-intent actions ("Add to Cart," "Shop Now," "Subscribe"). Background `{colors.primary}` with white text at `{typography.button-md}`. On hover, deepens to `{colors.primary-active}`. Disabled state fades to `{colors.primary-disabled}` at reduced opacity. Corner radius is a restrained `{rounded.xs}` — just enough softness to avoid clinical sharpness without becoming playful.

**`button-secondary`** — A teal-outlined button for secondary actions ("View Collection," "Learn More"). Transparent fill with a 1.5px `{colors.secondary}` border. On hover, fills with `{colors.secondary}` and inverts text to white. Used where gold would compete with artwork imagery.

**`button-tertiary`** — Underlined text link for inline contextual actions ("See all artists," "Read more"). No background, no border, just `{typography.button-sm}` with underline decoration. Hover deepens text to full ink.

### Navigation

**`nav-bar`** — A 64px sticky header on warm ivory `{colors.canvas}` with a subtle bottom hairline. Logo (likely wordmark) sits left; navigation links in `{typography.nav-link}` center or right; cart icon and search icon cluster at far right. On scroll, the hairline gives way to a delicate drop shadow (`nav-bar-scrolled`). The bar never competes with artwork below.

**`breadcrumb`** — Displayed below the nav on collection and product pages. Uses `{typography.caption}` in `{colors.muted}` with "/" separators. The final (active) segment renders in `{colors.ink}`.

### Product Display

**`product-card`** — The primary commerce unit. A white card (`{colors.surface-card}`) with `{rounded.sm}` corners and barely-there shadow. The image area fills a 1:1 aspect ratio with `{rounded.xs}` inner radius. Below the image: puzzle title in `{typography.title-sm}`, artist name in `{typography.artist-name}` (italic serif), and a `piece-count-badge` pill. On hover, the card lifts slightly with an enhanced shadow and subtle scale transform.

**`piece-count-badge`** — A small pill (`{rounded.full}`) in `{colors.badge-bg}` displaying "500 pcs" or "1000 pcs" in `{typography.piece-count}`. Positioned below the title or overlaid on the card image depending on context. Communicates complexity at a glance.

**`artist-attribution`** — Italic serif text (`{typography.artist-name}`) in `{colors.artist-credit}` that credits the original artwork. Appears on product cards and prominently on PDP pages. The italic serif creates intentional contrast against the geometric sans body.

**`difficulty-tag`** — An uppercase micro-label in `{colors.surface-soft}` background, used on product detail pages to indicate puzzle difficulty tier. `{typography.uppercase-tag}` with tight letter-spacing.

### Hero & Marketing

**`hero-section`** — Full-width banner in `{colors.surface-dark}` (deep teal) with a large artwork image as background or split-panel. Text overlay uses `{typography.display-xl}` in `{colors.on-dark}`. A gold `button-primary` CTA anchors the composition. Minimum height 520px ensures artwork gets gallery-worthy real estate.

**`collection-header`** — Centered section title using `{typography.display-md}` above grid layouts. Generous top padding (`{spacing.xxl}`) separates it from the preceding section. Used to introduce "New Arrivals," "Artist Spotlight," or themed collections.

**`newsletter-module`** — A teal (`{colors.surface-dark}`) rounded container prompting email signup. Heading in `{typography.display-sm}`, body in `{typography.body-md}` at reduced opacity. The input field uses a semi-transparent white background with the gold-focused border state. Subscribe button is `button-primary`.

### Footer

**`footer`** — Deep teal background (`{colors.secondary}`) with ivory text. Organized in a 4-column grid on desktop: brand story, shop links, customer service, and social icons. Links use `{typography.nav-link}` at 80% opacity, brightening to full on hover. Bottom row contains copyright and payment icons.

### Utility

**`text-input`** — Standard form field at 48px height with `{rounded.xs}` radius. Resting border is `{colors.hairline}`; focus transitions to `{colors.secondary}` (teal). Used in newsletter signup, search, and checkout forms.

**`quick-view-overlay`** — Modal card (`{rounded.md}`) with substantial shadow, triggered on product card interaction. Shows enlarged artwork, full title, artist credit, piece count, price, and Add to Cart button without leaving the grid page.

**`star-rating`** — Five-star display using `{colors.star-rating}` (gold) for filled stars and `{colors.hairline}` for empty. 16px size with `{spacing.xxs}` gaps. Appears on product cards and PDP reviews section.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text stacks above image; nav collapses to hamburger + cart icon; section padding reduces to 40px; display-xl drops to 32px |
| Tablet | 744–1128px | Two-column product grid; hero becomes 50/50 split; nav shows top-level links with overflow in dropdown; collection headers remain centered |
| Desktop | 1128–1440px | Three- or four-column product grid with 24px gutters; full nav visible; hero at full 520px+ height; footer in 4-column layout |
| Wide | > 1440px | Content max-width caps at 1440px centered; product grid stays 4-column with increased card size; hero artwork scales proportionally with max-height constraint |

### Touch Targets
- All interactive elements maintain 44px minimum tap target on mobile
- Product cards are full-width tap targets on single-column mobile layout
- Navigation hamburger icon padded to 48×48px touch area
- Badge and tag elements are non-interactive; no tap target requirement

### Collapsing Strategy
- Product grid: 4 → 3 → 2 → 1 columns as viewport narrows
- Footer columns collapse from 4-across to 2×2 stack on tablet, then single column accordion on mobile
- Hero section transitions from side-by-side to stacked (image above, text/CTA below) at tablet breakpoint
- Filter/sort bar becomes a sticky bottom sheet trigger on mobile rather than inline controls
- Artist bio sections on PDP collapse from two-column (portrait + text) to single column with smaller portrait

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — site likely loads styles via JavaScript bundles or is behind anti-bot protection. All color values above are inferred from Art & Fable's visual brand positioning (art gallery, gold-and-teal palette visible in their packaging and social media) but have NOT been verified against live CSS. Treat as directional.
- **No font stacks extracted** — Playfair Display and Inter are informed guesses based on the brand's gallery-catalog aesthetic; actual typefaces may differ. Inspect live site with JS enabled to confirm.
- **No platform confirmed** — unable to verify if Shopify, custom, or other CMS. Component structure may need adjustment based on actual template system.
- **Icon system unknown** — no data on whether the site uses SVG sprites, an icon font, or inline SVGs. Icon sizing and grid alignment are assumptions.
- **Animation/transition values unverified** — hover transitions, page-load animations, and scroll behaviors are common-sense defaults, not extracted from source.
- **Exact border-radius values unverified** — the rounded scale uses standard design-system increments; actual site may use non-standard values (e.g., 6px instead of 8px).
- **Product grid column count unverified** — responsive breakpoints and grid configuration are inferred from typical e-commerce patterns for art-focused brands.
