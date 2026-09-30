---
version: alpha
name: "Tineco"
source_url: "https://www.tineco.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Midnight navy (#01007f) anchors the Tineco visual system with a near-indigo weight that reads closer to precision instruments or professional AV gear than to the bright-plastic floor-care category it competes in. Nav bars, primary buttons, and hero overlays all carry this same saturated dark — creating a consistent foreground authority that lets product photography (metallic cordless wands, LED-ringed brush heads, OLED status displays) do the persuasion work against a light canvas beneath. Poppins handles all type: a geometric humanist face comfortable between the clinical sans-serifs of appliance documentation and the warmer faces of lifestyle retail. Display sizes run weight 600–700 at generous scale; body copy drops to 400 with 1.6× line-height so spec-dense product pages stay legible on small screens without requiring type-size inflation.

  The palette is structured in three temperature registers, each mapping to a distinct function. The navy family (#01007f → #305996 → #6684b1 → #99adcb) serves brand identity, navigation, and primary interactive states. A coral-to-terracotta band (#e7aca4 → #dc8377 → #cf5747) marks urgency — sale callouts, limited-run badges, and "Add to Cart" hover states that need visible contrast against the dark primary. An olive-gold register (#62623a → #929457 → #c6c775) appears to tag specific product sub-lines, giving Tineco's expanding SKU catalog a visual taxonomy that survives across category grid pages without requiring a full brand redesign for each new family.

  Geometry is restrained. Card corners sit at {rounded.sm} (8px), form inputs at {rounded.xs} (4px), and primary CTA buttons hold the same 4px to read as deliberate and machine-like rather than playful. Badge chips are the sole concession to full-radius softness, using {rounded.full} pill shapes to create contrast with the otherwise angular system. Spacing rhythm follows a 4-point base grid; section breaks breathe at {spacing.section} (64px), separating hero, feature strip, product grid, and social proof without crowding. The overall register — dark primary, structured grid, three-temperature palette — positions Tineco against Dyson's silver-and-purple design-object aesthetic by leaning into technical credibility over aspirational object-hood.

colors:
  primary: "#01007f"
  primary-active: "#000060"
  primary-disabled: "#99adcb"
  accent: "#cf5747"
  accent-active: "#b84035"
  accent-light: "#e7aca4"
  accent-mid: "#dc8377"
  navy-mid: "#305996"
  navy-soft: "#6684b1"
  navy-light: "#99adcb"
  olive-dark: "#62623a"
  olive: "#929457"
  olive-light: "#c6c775"
  ink: "#1a1a1a"
  body: "#444444"
  muted: "#606166"
  muted-light: "#909199"
  hairline: "#cfcfcf"
  hairline-soft: "#c2c4cf"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  label-caps:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-was:
    fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    border: "2px solid {colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-light}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-soft}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceWasTypography: "{typography.price-was}"
    priceWasColor: "{colors.muted-light}"
    priceWasDecoration: line-through
    descTypography: "{typography.body-sm}"
    descColor: "{colors.muted}"
    badgeRounded: "{rounded.full}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.navy-light}"
    minHeight: 560px
    padding: "{spacing.xxl} {spacing.section}"
    contentMaxWidth: 640px
    ctaVariant: button-accent
  feature-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.caption}"
    iconColor: "{colors.primary}"
    padding: "{spacing.xl} 0"
    itemGap: "{spacing.xxl}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
  badge-promo:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-olive:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  product-line-tab:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.surface-soft}"
    inactiveTextColor: "{colors.muted}"
    inactiveBorder: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 40px
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.primary}"
    selectedOffset: 2px
    unselectedBorder: "1px solid {colors.hairline}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  rating-bar:
    fillColor: "{colors.olive}"
    trackColor: "{colors.hairline}"
    height: 6px
    rounded: "{rounded.full}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted-light}"
    linkHoverColor: "{colors.canvas}"
    dividerColor: "#333333"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The midnight navy (#01007f) fill with Poppins 600 and a hard 4px radius ({rounded.xs}) is Tineco's workhorse CTA: it appears on product landing pages, comparison panels, and sticky add-to-cart bars. At 48px tall with 28px horizontal padding it meets WCAG touch targets with room to spare. Hover darkens to #000060 ({colors.primary-active}); disabled state bleaches to the extracted light blue (#99adcb, {colors.primary-disabled}) so the slot shape is preserved without misleading users.

**`button-accent`** — Coral (#cf5747) is reserved for the highest-urgency surface: "Add to Cart" within sale contexts, hero panels where the navy background creates maximum coral-on-navy contrast, and promotional banner CTAs. Hover deepens to #b84035 ({colors.accent-active}). This color should not appear more than once per viewport to preserve its urgency signal.

**`button-secondary`** — Transparent fill with a 2px navy border and navy text. On hover it floods with navy and inverts text to white, delivering a sharp-edged binary state change that avoids the soft gray most Shopify themes default to. Used for "Learn More," "Compare," and secondary action slots beneath a primary button.

**`button-ghost`** — White border and white text for use on dark panels (hero, navy feature bands, footer). Maintains the same 4px radius and 48px height for geometric consistency across all button tiers. Hover state fills semi-opaque white over the dark surface.

### Navigation

**`nav-bar`** — 64px white bar with a 1px hairline ({colors.hairline}) bottom border. Navigation links use Poppins 500 at 14px ({typography.nav-link}) in ink color; on desktop these expand to dropdown mega-menus organized by product family. The sticky variant activates on scroll, adding a soft 8px-blur drop shadow to separate from page content. The brand logo uses the primary navy (#01007f).

### Product Card

**`product-card`** — White surface with 1px hairline border at 8px radius ({rounded.sm}). The image well uses {colors.surface-soft} to float products with transparent or near-white backgrounds. Product name renders in Poppins 600 at 16px ({typography.title-sm}); current price in the dedicated {typography.price-display} at 22px bold; was-price in {typography.price-was} struck through in {colors.muted-light}. Badge chips ({badge-promo}, {badge-new}, {badge-olive}) overlay the image top-left, using pill radius ({rounded.full}) as their only soft-corner moment.

### Hero

**`hero`** — Full-bleed navy panel ({colors.primary}) with white display type at {typography.display-xl} (Poppins 700 at 48px). Subtitle text uses {colors.navy-light} (#99adcb) rather than flat white, creating a subtle layered luminosity within the dark field. The accent coral button ({button-accent}) sits against the navy to exploit the highest-contrast color pairing in the palette. Content column is constrained to 640px max-width even on wide viewports; product imagery bleeds to the panel edge on the opposite side.

### Feature Strip

**`feature-strip`** — A light gray band ({colors.surface-soft}) with a 1px hairline top and bottom border, housing a 4-up icon-and-caption grid for USPs: battery runtime, suction power rating, HEPA filtration, and app/Wi-Fi connectivity. Icons render in primary navy ({colors.primary}); caption copy uses {typography.caption} at {colors.muted}. On tablet the strip wraps to 2×2; on mobile it scrolls horizontally.

### Badges

Three badge tiers serve distinct semantic roles without clashing: `badge-promo` (coral #cf5747) for sale and urgency signals; `badge-new` (navy #01007f) for product launches and "just arrived" shelf states; `badge-olive` (#929457) for product-family sub-line tags (e.g. FLOOR ONE, PURE ONE). All three use all-caps 11px Poppins 700 with 1.2px letter-spacing ({typography.label-caps}) and pill shape ({rounded.full}) for instant visual taxonomy.

### Product Line Tabs

**`product-line-tab`** — Pill-shaped filter tabs that switch the product grid between Tineco families. Active state fills navy with white Poppins 600 ({typography.button-sm}); inactive shows light gray fill with muted text and a hairline border. The pill form ({rounded.full}) is the consistent soft-radius exception in an otherwise angular button system, distinguishing filter tabs from CTAs at a glance.

### Color Swatch

**`color-swatch`** — 24px circular chips with a 2px navy ring ({colors.primary}) offset by 2px on the selected state, creating a halo effect without a heavy border. Unselected chips carry a 1px hairline border. Chips scale to 32px on mobile to maintain usable touch targets without layout reflow.

### Spec Table

**`spec-table`** — A soft gray surface ({colors.surface-soft}) with alternating row borders in {colors.hairline}. Attribute labels use {typography.title-sm} in {colors.ink}; values use {typography.body-sm} in {colors.body}. The container uses {rounded.sm} (8px) and {spacing.base} padding, matching card geometry so spec tables feel native to the product page rather than borrowed from a documentation system.

### Footer

**`footer`** — Near-black (#1a1a1a, {colors.ink}) background with white section headings in Poppins 600 ({typography.title-sm}) and #909199 ({colors.muted-light}) link text that brightens to white on hover. Column layout at four across on desktop; collapses to a stacked accordion on mobile with 44px tap-height disclosure rows.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo mark; hero stacks image above copy block, display drops to {typography.display-md}; feature strip becomes horizontal scroll row; footer becomes single-column accordion |
| Tablet | 744–1128px | Two-column product grid; top nav shows primary categories inline, secondary links hidden behind overflow; hero runs 50/50 split layout; feature strip wraps to 2×2 grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with mega-menu dropdowns; hero full-bleed with content column capped at 640px; feature strip 4-across |
| Wide | > 1440px | Content column centers at max 1440px; hero background bleeds to viewport edges while text content stays constrained; grid holds at 3–4 columns with increased gutter |

### Touch Targets

- All interactive buttons minimum 48px height and 48px width
- Nav hamburger and icon buttons minimum 44px × 44px
- Color swatches scale from 24px (desktop) to 32px (mobile)
- Product cards use full-card tap region on mobile — not just title or price row
- Product line filter tabs minimum 40px height with 20px horizontal padding

### Collapsing Strategy

- Three-column product grid → two columns at tablet → single column at mobile
- Desktop horizontal feature strip → 2×2 grid at tablet → horizontal scroll row at mobile
- Mega-menu nav → top-level category bar at tablet → full-height drawer at mobile
- Side-by-side hero (copy + product image) → stacked image-over-text at mobile
- Four-column footer → two-column at tablet → single-column accordion at mobile
- Spec table rows stay full-width; label stacks above value on viewports under 400px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Canvas white (#ffffff) and `surface-soft` were not directly extracted — likely filtered as framework defaults; values are inferred from standard Shopify canvas conventions
- Exact primary CTA color (navy vs. coral) for "Add to Cart" on non-sale PDPs could not be confirmed from extraction alone; the accent/primary assignment is inferred from contrast logic
- Specific border-radius values were not confirmed from live extraction; 4px / 8px assignments are estimated from the brand's tech-premium positioning
- Poppins weight assignments (400 / 500 / 600 / 700) are inferred from convention — actual weight loading per text role was not extractable
- The olive register (#62623a / #929457 / #c6c775) function (product sub-line tagging vs. secondary UX element) is inferred from palette clustering, not confirmed from DOM role extraction
- No dark-mode token set was extracted; it is unclear whether Tineco AU runs a dark-mode variant
- No motion or animation tokens extracted (transition duration, easing curves, scroll-triggered animation parameters)
- No elevation or shadow scale extracted beyond the sticky nav inference
- `primary-active` (#000060) is a derived darker shade — not directly present in the extracted palette
