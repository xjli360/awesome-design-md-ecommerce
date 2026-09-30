---
version: alpha
name: "Elenco"
source_url: "https://www.elenco.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Snap Circuits' numbered grid panels and primary-colored components snap together with a satisfying click — that modular clarity is the organizing principle behind Elenco's digital presence. Where competitor STEM brands chase dark, garage-maker aesthetics, Elenco holds to a bright, classroom-optimized palette: bold red (`#c8202d`) against white canvas, with navy (`#1e3a6e`) anchoring navigation and institutional messaging, and safety-orange (`#f47920`) carrying age-range badges and promotional callouts. The effect is trusted educational catalog rather than startup — visual language shaped by decades of shipping kits to parents, teachers, and gift-buyers who need immediate legibility over atmosphere.

  Typography runs clean and weight-forward: display headings at 700 weight help non-technical buyers scan product grids quickly, body copy holds at 16px with a relaxed 1.6 line-height to accommodate instruction-heavy product descriptions and multi-item kit contents lists. Button labels are uppercase bold with modest letter-spacing — they read as confident and directive without being aggressive. Radius choices sit in the middle register: `{rounded.sm}` on buttons and cards avoids both the hard corners of industrial supply catalogs and the full-pill softness of consumer apps, landing on a register that signals reliability.

  Product cards are the workhorse of the layout: a white `{colors.surface-card}` surface with a 1px `{colors.hairline}` border, image-first hierarchy at a 4:3 aspect ratio, age badge in `{colors.accent}` orange as the highest-priority scan target, a skill-level chip in `{colors.surface-soft}` gray as secondary metadata, and a right-aligned price in bold before the primary CTA. Snap Circuits kits appear in flat-lay overhead photography — components spread across the numbered base panel — which communicates the assembly experience instantly even at card thumbnail scale.

  A persistent educator layer threads through the layout: a navy utility strip above the main nav signals institutional credibility (educator pricing, support line, dealer locator), and a full-width red `{colors.primary}` educator strip between the hero and product grid pitches directly to teachers and curriculum directors. This dual-audience structure — family gift-buyer and school buyer — is visible in the nav taxonomy, which carries product categories alongside an "Educator Resources" link at the same hierarchy level.

colors:
  primary: "#c8202d"
  primary-active: "#a01825"
  primary-disabled: "#e8a0a5"
  accent: "#f47920"
  accent-active: "#d45f08"
  secondary: "#1e3a6e"
  secondary-active: "#162c54"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  hairline: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  label-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
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
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
    hover:
      backgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "10px 22px"
    height: 48px
    hover:
      backgroundColor: "{colors.surface-soft}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
    hover:
      backgroundColor: "{colors.accent-active}"
  button-utility:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    height: 36px
    hover:
      backgroundColor: "{colors.secondary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "10px 16px 10px 42px"
    height: 44px
  nav-bar-top-strip:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.caption}"
    height: 32px
    padding: "0 {spacing.xl}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "2px solid {colors.primary}"
    logoHeight: 40px
    padding: "0 {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    captionTypography: "{typography.body-sm}"
    hover:
      boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  age-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  skill-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
    ctaComponent: button-accent
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.secondary}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    hover:
      borderColor: "{colors.primary}"
      backgroundColor: "{colors.canvas}"
  educator-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
    ctaComponent: button-secondary
  kit-contents-list:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.label-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — The main CTA carries Elenco red (`{colors.primary}`) at full saturation on a 48px-tall rectangle with `{rounded.sm}` corners and uppercase bold lettering in `{typography.button-md}`. On hover, the background deepens to `{colors.primary-active}` without animation delay; the disabled variant washes to `{colors.primary-disabled}`, a desaturated rose that signals unavailability without disappearing from the layout.

**`button-secondary`** — A white `{colors.canvas}` field with a 2px `{colors.primary}` border and matching red label text; identical height and radius to the primary, used for secondary actions like "Learn More" or "Compare Kits." On hover the fill lifts to `{colors.surface-soft}`, confirming interaction without competing with an adjacent primary button.

**`button-accent`** — Orange (`{colors.accent}`) CTA reserved for promotional surfaces — hero banners, sale callouts — where the red primary would clash with surrounding red marketing context. Same uppercase bold and 48px height as primary. Hover darkens to `{colors.accent-active}`.

**`button-utility`** — A compact 36px navy `{colors.secondary}` button used inside the top utility strip for "Find a Dealer" and account actions. Smaller `{rounded.xs}` corners and `{typography.button-sm}` sizing keep the utility row dense without crowding.

### Inputs
**`text-input`** — Standard form field at 44px height: white background, 1px `{colors.hairline}` border that upgrades to a 2px `{colors.primary}` ring on focus. Used across checkout, contact, and newsletter forms; label always positioned above the field, never floated inside, to preserve legibility on mobile.

**`search-bar`** — Wider variant with `{rounded.md}` corners and a 42px left offset accommodating a search magnifier icon in `{colors.muted}`. On mobile it expands to full width below the logo. The submit button attached to the right uses `button-primary` at standard padding.

### Navigation
**`nav-bar-top-strip`** — A 32px navy bar above the main header carries order tracking, educator pricing, and dealer-locator links in `{typography.caption}` white. It communicates institutional trust signals without competing with the primary nav's product categories; hidden entirely on mobile, with critical links surfaced in the hamburger drawer.

**`nav-bar`** — The 72px white main nav holds the Elenco logo at left, category links (Snap Circuits, Electronics, Physics, Biology, STEM, Educator Resources) in `{typography.nav-link}` centered or left-grouped, and search plus cart icons at right. A 2px `{colors.primary}` bottom border anchors the header without a drop shadow, visually connecting the red brand identity to the navigation layer.

### Product Cards
**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.sm}` corners. The image zone occupies the top 4:3 area; below it: kit name in `{typography.title-sm}`, a horizontal chip row with `age-badge` and `skill-badge`, a one-line teaser in `{typography.body-sm}`, price in `{typography.title-md}`, then a full-width `button-primary`. On hover the card lifts with a soft 16px blur shadow. The age badge appears at top-left of the image zone as an overlay, not below it, because age is the primary purchase filter in this category.

**`age-badge`** — Orange `{colors.accent}` pill in `{typography.badge}` — "Ages 8+", "Ages 14+" — positioned as an image overlay at top-left on product cards. High visual priority: age suitability is the first decision parents and gift-buyers make before reading the kit name.

**`skill-badge`** — Lower-contrast chip in `{colors.surface-soft}` with a 1px `{colors.hairline}` border — "Beginner", "Intermediate", "Advanced". Uses the same `{typography.badge}` scale as the age badge but lower contrast deliberately; it is a second-pass scan target for buyers who already know the recipient's age.

### Hero
**`hero-banner`** — Full-width navy `{colors.secondary}` banner with heading at `{typography.display-xl}` white, a descriptor line at `{typography.body-md}` white, and a `button-accent` CTA. The right half of the banner carries a product hero image — typically a Snap Circuits kit in use or a flat-lay of components. Minimum 480px tall on desktop. On mobile, the image stacks above the text block, capped at 240px height, and the CTA goes full-width.

### Category Navigation
**`category-tile`** — Homepage grid tile: `{colors.surface-soft}` gray background, a category icon centered above the title in `{typography.title-md}` navy, and a short descriptor in `{typography.body-sm}`. On hover the border upgrades from `{colors.hairline}` to `{colors.primary}` red and the background lifts to `{colors.canvas}` white. Four columns on desktop, two on tablet, one on mobile.

### Educator Resources Strip
**`educator-strip`** — Full-width `{colors.primary}` red band with a two-line pitch: heading in `{typography.title-md}` white, body in `{typography.body-sm}` white, and a `button-secondary` (white-border outlined) CTA right-aligned on desktop. Appears between the hero and the product grid on the homepage, and repeats at the base of category pages. The red background and white-outline button inversion is the only surface in the design system where the secondary button reads clearly without switching to a dark variant.

### Kit Contents List
**`kit-contents-list`** — On product detail pages, a `{colors.surface-soft}` box lists included components (IC count, wire lengths, base panel size, component names) in `{typography.body-sm}`. The box uses `{rounded.sm}` and a `{colors.hairline}` border. Items render as a definition list: component name flush left, quantity right-aligned. This is a category-specific UI pattern reflecting Elenco's builder audience; parents cross-check component lists against age-range upgrade kits.

### Breadcrumb
**`breadcrumb`** — Single-row path above the product title: "Home / Snap Circuits / Snap Circuits Jr." in `{typography.caption}` `{colors.muted}`, final segment in `{colors.ink}`. Slash separator, transparent background, no underlines on intermediate links until hover.

### Footer
**`footer`** — Full-width navy `{colors.secondary}` block with four columns (Products, Support, Educators, Company) using `{typography.label-sm}` uppercase headers and `{typography.body-sm}` link rows in `{colors.hairline}` gray. The navy footer matches the top utility strip, creating a bookend frame around the white content area. A bottom strip inside the footer carries copyright and legal links in `{typography.caption}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hamburger nav; search bar moves below logo; product grid 1-up; hero image stacks above text block capped at 240px; category tiles 2-column; educator-strip stacks vertically with full-width CTA; top utility strip hidden |
| Tablet | 744–1128px | Two-column product grid; condensed nav with icon-only cart and search; category tiles 2-column; hero retains side-by-side layout at reduced padding; educator-strip horizontal |
| Desktop | 1128–1440px | Four-column product grid; full horizontal nav with all category labels visible; hero at full 480px height; category tiles 4-column; educator-strip with right-aligned CTA |
| Wide | > 1440px | Content container max-width ~1280px centered on canvas; hero gains lateral whitespace; product grid stays 4-column but card widths grow; body copy max-width capped at 72ch |

### Touch Targets
- All buttons minimum 44×44px; primary, secondary, and accent buttons 48px tall by default
- Mobile hamburger drawer rows spaced at minimum 48px row height for category links
- Age and skill badges are not interactive; the entire product card surface is the tap target
- Cart and search icons padded to 44×44px hit area regardless of rendered icon size
- Form inputs 44px tall; labels always above the field on mobile to preserve the tap target

### Collapsing Strategy
- Top utility strip hidden on mobile; "Find a Dealer" and educator pricing links move into the hamburger drawer bottom section
- Main nav collapses to logo + hamburger + cart icon on mobile; category nav becomes a vertically scrollable drawer
- On tablet, category nav shows abbreviated labels or icon-only chips in a horizontal scroll row
- Product grid: 4-col desktop → 2-col tablet → 1-col mobile
- Kit contents list collapses to an accordion disclosure on mobile to reduce page height
- Educator strip: 2-column horizontal → single-column stacked on mobile with full-width outlined CTA

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: the site returned a redirect/anti-bot response at crawl time — zero color values were captured. All colors above are inferred from Elenco's publicly visible product photography, logo assets, and catalog imagery; the actual primary red may differ from `#c8202d` and should be verified against live CSS or brand guidelines.
- **No font stacks extracted**: Open Sans is a plausible inference for an educational brand of this era and audience, but the production webfont may differ. Inspect `<link rel="preload">` or `@font-face` declarations in the live page source to confirm.
- **No meta theme-color**: mobile browser chrome color unknown; default to `{colors.primary}` as the likely candidate.
- **Platform unconfirmed**: marked non-Shopify, but the actual e-commerce platform (Magento, WooCommerce, custom) is unknown, which may affect cart, checkout, and account component patterns not described here.
- **Educator portal UI**: the educator pricing and quote-request flows are inferred from category knowledge; the actual UI patterns for institutional buyers (PO upload, quote cart, tax-exempt checkout) were not observable.
- **Snap Circuits compatibility matrix**: circuit-complexity ratings and inter-kit compatibility indicators are category-inferred; whether these appear as on-site UI components or only in PDF documentation is unconfirmed.
