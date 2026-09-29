---
version: alpha
name: "Golden Coil"
source_url: "https://www.goldencoil.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Golden Coil planners arrive as blank-canvas systems where the coil binding itself — that literal gilded spiral — is the only fixed element; every cover material, interior layout, and tab configuration is chosen by the customer before production begins. The brand's identity is built around that moment of customization, which means the UI must carry the same sense of considered selection: warm creams and amber golds that evoke physical paper stock rather than a generic digital surface, and a serif-to-sans pairing that signals editorial craft without tipping into wedding-stationery fussiness. The signature gold (#C4973D) carries all primary actions — add-to-cart, personalize, select — and it reads less like a button color and more like an approval stamp on a bespoke order. Background surfaces stay in the ivory range (#FAF8F5 for canvas, #F2EFE9 for soft panels), keeping the warmth of uncoated paper while remaining screen-legible. Typography splits between a Cormorant-family serif at display scale — generous at 36–48px, light at weight 300–400 to avoid heaviness — and a clean geometric sans (Jost or equivalent) for all functional UI text, body copy, and labels. Rounded corners are conservative: cards and inputs sit at {rounded.sm} (8px), product configurator panels at {rounded.md} (12px), and pill badges at {rounded.full}. There are no sharp 0px corners in the customer-facing flow. Spacing is generous: the product configurator needs room to breathe so each option choice feels deliberate rather than dense. The overall voice is warm and systematic at once — a brand that takes planning seriously but presents the process as pleasurable.

colors:
  primary: "#C4973D"
  primary-active: "#A67D2A"
  primary-disabled: "#E4CC9A"
  primary-hover: "#D4A84D"
  ink: "#1E1A15"
  body: "#3A3228"
  muted: "#7A6E62"
  muted-soft: "#A89E94"
  hairline: "#DEDAD3"
  hairline-soft: "#EDEBE6"
  canvas: "#FAF8F5"
  surface-soft: "#F2EFE9"
  surface-card: "#FFFFFF"
  surface-warm: "#F7F3EC"
  on-primary: "#FFFFFF"
  accent-gold-light: "#F0E0B8"
  accent-gold-subtle: "#FBF5E8"
  error: "#C0392B"
  success: "#4A7C59"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'Cormorant', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant Garamond', 'Cormorant', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant Garamond', 'Cormorant', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Cormorant Garamond', 'Cormorant', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Nunito Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.3px
  title-sm:
    fontFamily: "'Jost', 'Nunito Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
  body-md:
    fontFamily: "'Jost', 'Nunito Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.1px
  body-sm:
    fontFamily: "'Jost', 'Nunito Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.1px
  caption:
    fontFamily: "'Jost', 'Nunito Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  caption-upper:
    fontFamily: "'Jost', 'Nunito Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', 'Nunito Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Nunito Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.9px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Jost', 'Nunito Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  price-display:
    fontFamily: "'Cormorant Garamond', 'Cormorant', Georgia, serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  label-upper:
    fontFamily: "'Jost', 'Nunito Sans', system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.5px
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
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1.5px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: "1.5px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  text-input-error:
    border: "1.5px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoTypography: "{typography.display-sm}"
  nav-bar-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "4/5"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    textColor: "{colors.ink}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 16px rgba(30,26,21,0.08)"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
    labelTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
  configurator-option-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    padding: "10px 16px"
  configurator-option-selected:
    backgroundColor: "{colors.accent-gold-subtle}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
  color-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.primary}"
    outlineOffset: 2px
    outline: "2px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-warm}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
    ctaMarginTop: "{spacing.lg}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  badge-bestseller:
    backgroundColor: "{colors.accent-gold-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  progress-step:
    activeColor: "{colors.primary}"
    inactiveColor: "{colors.hairline}"
    completedColor: "{colors.primary-active}"
    labelTypography: "{typography.caption-upper}"
    connectorHeight: 2px
  section-divider:
    color: "{colors.hairline-soft}"
    marginY: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "#C8C0B5"
    linkColor: "#E0D8CF"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    logoColor: "{colors.primary}"
    padding: "{spacing.xxl} 0"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xl}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption-upper}"
    textColor: "{colors.body}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    height: 44px
    padding: "0 {spacing.base}"
    iconColor: "{colors.muted}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"

## Components

### Buttons

**`button-primary`** — Gold-filled (#C4973D) with white uppercase text at 0.8px letter-spacing; 48px tall with {rounded.sm} corners, giving it substance without pill softness. Hover lifts to #D4A84D and active presses to #A67D2A; disabled washes to #E4CC9A so the gold hue is preserved but clearly inert. This is the only button color that uses the brand gold — all CTA weight routes through it.

**`button-secondary`** — White canvas background with 1.5px hairline border; text and typography match primary but the treatment reads as a companion choice rather than a main action. Hover fills the background with surface-soft (#F2EFE9) and darkens the border to muted-soft, keeping the interaction within the warm neutral family.

**`button-ghost`** — Transparent background with primary-colored text and an underline, used for secondary text links like "Learn more" or "View all options." No border, no fill — reserves visual weight for primary actions in the configurator.

### Configurator

**`configurator-panel`** — The heart of the product page experience. A surface-soft (#F2EFE9) panel with {rounded.md} corners and a 1px hairline border encloses each customization step (size, cover, interior, add-ons). Labels use {typography.title-sm} in uppercase; helper text drops to {typography.caption}. Generous {spacing.xl} padding prevents the option grid from feeling cramped.

**`configurator-option-button`** — Each selectable option (layout name, date format, accessory) renders as a canvas-background button with 1.5px hairline border and {rounded.sm}. On selection it transitions to the accent-gold-subtle (#FBF5E8) fill with a 1.5px primary gold border — subtle enough to not compete with the primary CTA but unmistakably confirmed.

**`color-swatch`** and **`color-swatch-selected`** — 32×32px circles at {rounded.full}. Unselected swatches show the material color with no ring; selected adds a 2px primary gold outline with a 2px offset gap, the "selected" ring pattern familiar from physical product lookbooks.

**`progress-step`** — A horizontal stepper above the configurator tracks completion (Cover → Interior → Details → Review). Active step uses primary gold, completed steps shift to primary-active (#A67D2A), pending steps render in hairline gray. Step labels use {typography.caption-upper} in all-caps for a structured, form-like feel.

### Navigation

**`nav-bar`** — 64px tall, canvas white with a hairline-soft bottom border. The wordmark "Golden Coil" renders in {typography.display-sm} using the serif family at a moderate weight — it reads as a logotype, not a nav item. Nav links sit at {typography.nav-link} in Jost; hover shifts link color to primary gold. Cart and account icons are 20px, ink-colored.

### Product & Browse

**`product-card`** — 4:5 aspect ratio image (covers fill the frame edge-to-edge), with title in {typography.title-md} and price in {typography.price-display} (the serif at 24px, weight 500 — reads as a deliberate styling choice). A subtle 1px hairline-soft border frames the card; hover adds a soft drop shadow and darkens the border. No hover-zoom on the image — the brand prefers stillness over interaction theatrics.

**`category-chip`** — Pill-shaped filter chips at {rounded.full} in surface-soft. Active state fills with primary gold. Used on the browse/shop page to filter by planner type, size, or use-case.

**`badge-new`** and **`badge-bestseller`** — Two badge types ride over product card images. "NEW" sits in primary gold with white text; "BESTSELLER" uses accent-gold-light (#F0E0B8) background with primary-active text — a lighter, earned distinction. Both use {typography.label-upper} at 1.5px letter-spacing for legibility at small scale.

### Hero & Editorial

**`hero-section`** — Full-width section with surface-warm (#F7F3EC) background. Heading in {typography.display-xl} (serif, weight 300) feels editorial rather than promotional. Subheadline drops to {typography.body-md} in Jost. CTA button sits {spacing.lg} below the subhead. On homepage, a product image stack (fanned planners showing cover options) occupies the right column.

### Feedback & Utility

**`testimonial-card`** — White card with {rounded.md} and hairline-soft border. Quote text in {typography.body-md} at 1.65 line-height for readability; author attribution in {typography.caption-upper} below a {spacing.sm} gap. Cards display in a 3-column grid on desktop, single-column on mobile.

**`footer`** — Dark ink (#1E1A15) background with warm off-white link and body text. The Golden Coil wordmark renders in primary gold (#C4973D) at top-left. Column headers in {typography.title-sm} uppercase; body links in {typography.body-sm}. Four columns on desktop collapse to two on tablet and one on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; configurator panels stack vertically full-width; nav collapses to hamburger + wordmark; hero switches to stacked image-over-text; category chips scroll horizontally |
| Tablet | 744–1128px | 2-column product grid; configurator uses a split layout (steps left, preview right) at 50/50; nav shows primary links, secondary links move to overflow menu |
| Desktop | 1128–1440px | 3-column product grid; configurator panel is 40% width with sticky preview pane at 60%; nav fully expanded with all links visible |
| Wide | > 1440px | Max content width capped at 1440px with auto side margins; hero image expands to fill; product grid may show 4 columns |

### Touch Targets

- All configurator option buttons minimum 44×44px on mobile
- Color swatches expand to 40×40px on touch screens with 8px gap minimum between swatches
- Nav hamburger touch target 44×44px regardless of visible icon size
- Progress step labels hidden on mobile (only dots shown) to maintain 44px tap width per step

### Collapsing Strategy

- Configurator collapses step-by-step: each section (Cover, Interior, Details) is an accordion panel on mobile — only one open at a time
- Product card price and title remain visible at all breakpoints; secondary caption text (e.g., page count) hides below 744px
- Footer collapses columns into an accordion on mobile; legal links collapse to a single scrolling row
- Hero subheadline font size scales from 16px (mobile) to 18px (tablet+) via responsive class, not fluid type

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site returned a redirect page (anti-bot or geo-gate) and yielded zero color tokens. All palette values in this file are inferred from brand-knowledge (the gold/cream/warm-neutral aesthetic associated with premium stationery brands and the brand name "Golden Coil"). Verify every color against the live product pages before shipping.
- **No font stacks extracted** — zero font-family data was returned. Typography assignments (Cormorant Garamond for serif display, Jost for sans) are based on the aesthetic register of the brand and common choices in the premium planner/stationery category. Confirm by inspecting live CSS.
- **Configurator interaction details unknown** — Golden Coil's build-your-own flow is central to the brand but the exact step structure, preview behavior, and validation states could not be verified from the extracted page.
- **Brand illustration or icon style** — unknown whether the brand uses custom iconography, line icons, or emoji-style glyphs in the UI. No assets were extractable.
- **Actual corner radius values** — all {rounded.*} assignments are inferred from category norms; may differ from production values.
- **Promotional/sale states** — strikethrough pricing, discount badge styles, and sale banner patterns are unconfirmed.
- **Email capture modal** — common for this category but design details (overlay style, timing, dismiss behavior) are not available from the extracted data.
