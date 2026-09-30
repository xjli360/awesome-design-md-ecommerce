---
version: alpha
name: "Elixir Strings"
source_url: "https://www.elixirstrings.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, resonant blue (#003f56) anchors Elixir Strings — not the bright cyan of a tech brand, but the color of a midnight stage, the ink of a well-worn setlist. This primary sits alongside a crisp white canvas (#f8f0f0, a warm off-white that reads as aged paper or vintage guitar pickguard) and a sharp accent of electric blue (#00aeef) that pulses through CTA buttons and product highlights like a single bright LED on a pedalboard. The typography runs on Work Sans for display — a geometric sans-serif with a slight humanist warmth — and Inconsolata for technical specs, a monospace that whispers "engineer, luthier, player." Buttons carry a generous {rounded.sm} radius, product cards soften to {rounded.md}, and the overall spacing breathes at {spacing.lg} between elements, giving each string set room to be considered. The brand voice is less "loud rockstar" and more "master luthier explaining why phosphor bronze matters" — technical precision wrapped in quiet confidence. Signature moves include a navy-to-black gradient on hero sections, a green badge (#67c116) for "NEW" or "BEST SELLER" that feels like a vintage amp jewel light, and a persistent top nav that stays at 72px with a subtle bottom hairline (#cecdcd). The extracted palette includes several blues and grays that likely belong to checkout widgets or social icons, but the true brand identity resolves to three poles: midnight navy (#003f56), warm ivory (#f8f0f0), and electric accent (#00aeef).

colors:
  primary: "#003f56"
  primary-active: "#002d3e"
  primary-disabled: "#7a9aa8"
  ink: "#1a1a1a"
  body: "#444444"
  muted: "#717171"
  muted-soft: "#a0a0a0"
  hairline: "#cecdcd"
  hairline-soft: "#e4e4e4"
  canvas: "#f8f0f0"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-electric: "#00aeef"
  accent-green: "#67c116"
  accent-blue-soft: "#accef7"
  accent-blue-medium: "#1c84ec"
  dark-bg: "#111111"
  dark-text: "#484848"

typography:
  display-xl:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  mono-sm:
    fontFamily: "'Inconsolata', 'Roboto Condensed', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-caption:
    fontFamily: "'Inconsolata', 'Roboto Condensed', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Work Sans', 'Roboto', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px

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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-accent:
    backgroundColor: "{colors.accent-electric}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "#0099d4"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.accent-electric}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-electric}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-best-seller:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-gradient-overlay:
    background: "linear-gradient(135deg, {colors.primary} 0%, {colors.dark-bg} 100%)"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  footer-section:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.dark-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-circle-accent:
    backgroundColor: "{colors.accent-electric}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    typography: "{typography.mono-caption}"
    textTransform: uppercase
    letterSpacing: "0.5px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with midnight navy (#003f56) and white text. Used for "Shop Now", "Add to Cart", and "Learn More" on product pages and hero sections. On hover, darkens to `#002d3e` with a subtle scale transform (1.02). Disabled state drops to a muted blue-gray (#7a9aa8) with reduced opacity (0.6). The 8px radius (`{rounded.sm}`) keeps the button feeling approachable without being overly pill-shaped.

**`button-secondary`** — An outlined variant on the warm ivory canvas (`#f8f0f0`), with a 2px solid primary border and primary text. Used for "Compare Strings" and "View Details" actions. On hover, fills with primary background and inverts text to white. The 48px height matches the primary button for consistent row alignment.

**`button-accent`** — The electric blue (#00aeef) variant reserved for high-energy CTAs like "Find Your Perfect String" or "Limited Edition" drops. On hover, shifts to a slightly deeper cyan (#0099d4). This button carries the brand's voltage — it's the one that says "click here for something exciting."

**`button-pill`** — A fully rounded pill shape (`{rounded.full}`) used for filter tags, category navigation, and "NEW" product badges. Smaller padding (10px 24px) and smaller typography (`{typography.button-sm}`) allow it to sit inline with other pills in a horizontal strip.

### Cards
**`product-card`** — The core product display unit: a white card (`{colors.surface-card}`) with 12px rounded corners (`{rounded.md}`), 16px padding, and a 1:1 aspect ratio product image at the top. The image sits in a slightly smaller radius (`{rounded.sm}`) to create a nested-corner effect. On hover, a soft box-shadow lifts the card 4px. Below the image: product name in `{typography.title-sm}`, gauge/type in `{typography.body-sm}`, and price in `{typography.title-md}`. Badges (NEW, BEST SELLER, SALE) overlay the top-left of the image at `{spacing.sm}` offset.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on the warm ivory canvas (`#f8f0f0`). The brand logo sits left-aligned; primary links (Strings, Accessories, Learn, Support) are center-aligned with 15px Work Sans at weight 500. The active link gets a 2px bottom border in primary blue. A thin 1px hairline (`#cecdcd`) separates the nav from the page content. On mobile, the nav collapses into a hamburger menu with a slide-down drawer.

### Forms
**`text-input`** — Standard text input fields for search, newsletter signup, and account forms. White background, 1px hairline border, 8px radius, 48px height. On focus, the border thickens to 2px and shifts to electric blue (#00aeef). Placeholder text uses `{colors.muted}` (#717171). Error state adds a 2px red border (not yet extracted — see Known Gaps).

### Hero
**`hero-section`** — Full-width hero banners that use the primary navy as base, often with a gradient overlay fading to near-black (#111111) at the bottom. White text at `{typography.display-xl}` (48px) sits left-aligned with generous left padding. A secondary headline in `{typography.display-md}` (28px) sits below at `{spacing.base}` offset. The hero includes a primary CTA button and often a small monospace spec line (e.g., "80/20 Bronze | Light Gauge | 6-String Set") in `{typography.mono-sm}`.

### Footer
**`footer-section`** — A dark footer on `#111111` background with muted gray text (#484848). Links in `{typography.link}` at `#a0a0a0` lighten to white on hover. The footer is divided into 3-4 columns: Products, Support, Company, and Social. A thin hairline divider separates the top section from the bottom legal bar (copyright, privacy, terms). Social icons sit in 40px circles (`{icon-circle}`) with a soft gray background.

### Badges
**`badge-new`** — A green (#67c116) badge for new product launches. All-caps 11px Work Sans at weight 700 with 0.5px letter spacing. 4px radius, 2px vertical padding, 8px horizontal. Sits at the top-left of product card images.
**`badge-sale`** — Electric blue (#00aeef) badge for promotional pricing. Same typography and dimensions as `badge-new`.
**`badge-best-seller`** — Navy (#003f56) badge for top-selling products. Same typography and dimensions as `badge-new`.

### Dividers
**`divider`** — A 1px line in `#cecdcd` used between nav and content, between footer sections, and in spec tables.
**`divider-soft`** — A 1px line in `#e4e4e4` used for more subtle separations, like between product card metadata rows.

### Spec Tables
**`spec-table`** — A bordered table for technical string specifications (gauge, material, tension, winding). White background, 1px hairline borders, 8px radius. Headers use `{typography.mono-caption}` in all-caps with a soft gray background (`#f2f2f2`). Body cells use `{typography.mono-sm}` (13px Inconsolata). This is where the brand's technical precision lives — the monospace font signals that these are engineering specs, not marketing copy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero text drops to 28px; product cards go single-column; search bar moves below nav; footer stacks vertically |
| Tablet | 744–1128px | Nav links remain visible but font-size drops to 14px; product cards in 2-column grid; hero text at 36px; search bar integrated into nav |
| Desktop | 1128–1440px | Full nav with 15px links; product cards in 3-column grid; hero at 48px; search bar prominent in nav center |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero text scales to 56px; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px standard)
- Icon circles at 40px with 44px touch area (using transparent padding)
- Nav links have 48px tap area even when text is smaller
- Product card tap targets include the entire card surface
- Search bar at 48px height for comfortable tapping

### Collapsing Strategy
- Top nav: links collapse into hamburger menu below 744px; brand logo remains visible
- Product grid: 4-column → 3-column → 2-column → 1-column as viewport shrinks
- Hero section: left-aligned text becomes centered on mobile; gradient overlay remains
- Footer: 4-column layout collapses to 2-column at tablet, single-column at mobile
- Spec tables: horizontal scroll on mobile with sticky first column
- Badge overlays: remain top-left but scale down slightly on mobile (8px font)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons (scale transform, shadow depth) are inferred from common patterns — exact values not extracted
- Error styling for form inputs (red border hex, error message typography) not present in extracted data
- Active/visited link colors beyond nav not confirmed
- Dark mode palette not present on the live site (no meta theme-color, no CSS media query found)
- Sub-brand or collection-specific palettes (e.g., "Optiweb" vs "Polyweb" vs "Nanoweb" coatings) may use different accent colors — not extracted
- Loading states (spinner hex, skeleton color) not found
- Focus ring styles (outline color, offset) not extracted
- The extracted font list includes "Roboto Condensed" and "inherit" — these may be fallbacks or unused declarations; primary display font appears to be Work Sans based on usage frequency
- Several extracted hex colors (#007aff, #1c84ec, #accef7) are likely from Apple Pay/Shopify Pay buttons or social media icons, not brand elements — use with caution
- The warm ivory (#f8f0f0) may be a background tone that shifts slightly between sections — exact surface-soft (#f2f2f2) and canvas (#f8f0f0) are best approximations
- Animation durations and easing curves not extracted
- Print stylesheet behavior unknown
