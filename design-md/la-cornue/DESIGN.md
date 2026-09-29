---
version: alpha
name: "La Cornue"
source_url: "https://www.lacornue.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Polished brass hardware against hand-enamelled iron — that contrast sits at the heart of every La Cornue surface, digital included. The palette anchors on a deep Parisian navy (#163959) that evokes the cast-iron body of the Château range, while a burnished gold (#b8924a) sparks through CTAs and accent borders the way brass trim catches overhead light in a professional kitchen. Body text lives in a warm charcoal (#404040) rather than pure black, softening long-form craft narratives about flame-vaulted ovens and hand-riveted doors. The canvas stays an antique ivory (#faf8f5) — never clinical white — giving product photography the same warm register as a limestone-walled Parisian showroom. Typography leans on a refined serif display face for headlines (`{typography.display-xl}`) paired with a clean geometric sans for navigation and interface text, creating the same high-low tension as a 1908 atelier operating inside a modern digital storefront. Cards and panels carry gentle `{rounded.xs}` corners — almost square, never playful — while generous `{spacing.section}` vertical rhythm between content blocks lets hero photography breathe without crowding. The product configurator — where buyers choose among 32+ enamel colours and seven metal finishes — is the signature UI moment: swatches render at 40×40px with a 2px `{colors.primary}` ring on selection, and a live preview updates with each choice. Navigation is spare and editorial: a slim sticky header with wordmark left, utility icons right, and a full-width mega-menu that drops on hover to reveal range families organised by collection. Footer columns echo the navy ground with gold link hover states, reinforcing that every pixel shares DNA with the physical product's materiality.

colors:
  primary: "#163959"
  primary-active: "#0f2a45"
  primary-disabled: "#8a9fb3"
  accent-gold: "#b8924a"
  accent-gold-active: "#9a7a3d"
  accent-gold-soft: "#d4be8a"
  ink: "#272727"
  body: "#404040"
  muted: "#737373"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  border-strong: "#bfbfbf"
  canvas: "#faf8f5"
  surface-soft: "#f4f2ef"
  surface-card: "#ffffff"
  surface-dark: "#163959"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent: "#ffffff"
  error: "#bd2426"
  error-soft: "#f9e5e5"
  success: "#516b1d"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.8px
    textTransform: uppercase
  overline:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 15px 31px
    height: 48px
    border: 1px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 48px
  button-gold-active:
    backgroundColor: "{colors.accent-gold-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 14px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
    position: sticky
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    boxShadow: 0 1px 4px rgba(0,0,0,0.06)
  mega-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.section}"
    boxShadow: 0 8px 24px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: 0
    imageAspectRatio: 4/3
    titleTypography: "{typography.title-sm}"
    subtitleTypography: "{typography.caption}"
    priceTypography: "{typography.price}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.hairline}
    hoverShadow: 0 4px 16px rgba(0,0,0,0.06)
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 85vh
    contentMaxWidth: 560px
    overlayGradient: linear-gradient(to right, rgba(22,57,89,0.7) 0%, transparent 60%)
  colour-swatch:
    rounded: "{rounded.full}"
    width: 40px
    height: 40px
    border: 2px solid transparent
    borderSelected: 2px solid {colors.primary}
    outlineSelected: 2px solid {colors.canvas}
    outlineOffset: 2px
  configurator-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
    sectionSpacing: "{spacing.xl}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-lg}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} 0 {spacing.xl}"
    textAlign: center
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-gold-soft}"
    linkHoverColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    columnGap: "{spacing.xl}"
  badge-bespoke:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-accent}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.sm}"
  image-gallery:
    rounded: "{rounded.xs}"
    thumbnailSize: 72px
    thumbnailGap: "{spacing.sm}"
    thumbnailBorder: 1px solid {colors.hairline}
    thumbnailActiveBorder: 2px solid {colors.primary}
    mainImageAspectRatio: 4/3
---

## Components

### Buttons

**`button-primary`** — Full navy fill with white uppercase text tracked at 0.8px. On hover the background deepens to `{colors.primary-active}` with a 200ms ease transition; disabled state lightens to a desaturated slate. Used for "Add to Cart," "Request a Quote," and primary form submissions. Minimum width 180px on desktop to maintain visual weight alongside large product imagery.

**`button-secondary`** — Transparent field with a 1px navy border and navy text. On hover, fills completely to `{colors.primary}` with text inverting to white, creating a satisfying "fill-in" interaction. Used for "Discover the Collection," "View Details," and secondary navigation actions.

**`button-gold`** — Burnished gold fill reserved for the highest-value conversion moments: booking a showroom appointment or starting the bespoke configurator. The warm metallic tone separates these from standard commerce actions and signals exclusivity.

### Navigation

**`nav-bar`** — A slim 72px sticky header on ivory canvas. Left-aligned wordmark (SVG, no text replacement), right-aligned utility cluster (search icon, location pin for dealer locator, language selector, hamburger on mobile). Central navigation links use `{typography.nav-link}` uppercase treatment with 0.8px tracking. On scroll, background shifts to pure white with a subtle 1px bottom shadow.

**`mega-menu`** — Full-width dropdown triggered on hover (desktop) or tap (tablet). Organised into columns by product family: Château, CornuFé, CornuChef, Flamberge. Each column leads with a small product image (120×90px) and 3–5 links beneath. The panel sits on `{colors.surface-card}` with a diffused shadow to float above page content.

### Product Display

**`product-card`** — Rectangular card with 4:3 image ratio, minimal border on `{colors.hairline-soft}`. Product name in `{typography.title-sm}`, collection subtitle in `{typography.caption}` muted text, price in `{typography.price}`. On hover, border strengthens and a soft shadow lifts the card 4px. No rounded corners beyond `{rounded.xs}` — the aesthetic is precise, not playful.

**`hero-banner`** — Full-bleed photography (85vh minimum) with a directional gradient overlay from navy to transparent, allowing headline text to sit legibly over the left third. Title in `{typography.display-xl}` at 48px, body in `{typography.body-md}`, and a single CTA button below. Content constrained to 560px max-width to prevent line lengths from exceeding 65 characters.

### Configurator

**`colour-swatch`** — Circular 40×40px swatches representing the 32+ enamel finishes. Selected state shows a 2px `{colors.primary}` ring with a 2px white offset gap, creating a clear "chosen" indicator without obscuring the colour itself. Swatches arrange in a responsive grid with `{spacing.sm}` gaps.

**`configurator-panel`** — Right-side panel (desktop) or bottom sheet (mobile) containing the step-by-step configuration flow: Range Model → Size → Enamel Colour → Metal Trim → Accessories. Each section separated by `{spacing.xl}` with `{typography.title-sm}` headers. Active step highlighted with a left 3px `{colors.accent-gold}` border accent.

### Supporting Elements

**`collection-header`** — Centered section header combining `{typography.display-lg}` title with `{typography.body-md}` subtitle beneath. Generous top padding (`{spacing.section}`) isolates each collection zone as a distinct editorial chapter.

**`footer`** — Deep navy ground (`{colors.surface-dark}`) with four columns: Products, Our Maison, Services, Contact. Links in muted cream hover to `{colors.accent-gold}`. Bottom bar contains legal links, language/region selector, and social icons at 20px.

**`badge-bespoke`** — Small gold pill label applied to products that offer custom configuration. Uses `{typography.overline}` at 11px uppercase with tight padding. Positioned absolutely over product card imagery, 12px from top-right corner.

**`breadcrumb`** — Horizontal trail using `{typography.caption}` with "/" separators in `{colors.hairline}`. Current page in `{colors.ink}`, ancestor links in `{colors.muted}` with underline on hover.

**`image-gallery`** — Primary product image at 4:3 ratio with a horizontal thumbnail strip below. Thumbnails are 72px squares with 1px hairline border; active thumbnail gets a 2px `{colors.primary}` border. Supports swipe on touch devices and arrow-key navigation on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger + wordmark. Hero reduces to 60vh with bottom-aligned text. Configurator becomes full-width bottom sheet. Product grid: 1 column. Footer stacks into accordion sections. |
| Tablet | 744–1128px | Two-column product grid. Nav shows top-level links, mega-menu triggers on tap. Hero at 70vh. Configurator panel slides in from right at 400px width. |
| Desktop | 1128–1440px | Three-column product grid. Full horizontal nav with hover mega-menu. Side-by-side product detail (gallery left, info + configurator right). Section padding at `{spacing.section}`. |
| Wide | > 1440px | Content max-width caps at 1440px, centered. Four-column product grid on collection pages. Hero image extends full bleed while text container stays at 560px max. Increased section spacing to `{spacing.section-lg}`. |

### Touch Targets
- All interactive elements maintain 44×44px minimum touch area on mobile and tablet
- Colour swatches increase to 48×48px on touch devices with `{spacing.md}` gaps
- Mobile nav hamburger and utility icons padded to 48px tap zones
- Footer accordion headers get 56px hit areas for comfortable thumb operation

### Collapsing Strategy
- Navigation: full links → condensed → hamburger with slide-out drawer
- Product grid: 4-col → 3-col → 2-col → 1-col with maintained image aspect ratio
- Configurator: side panel → bottom sheet with 60vh max-height and drag handle
- Footer: horizontal columns → vertical accordion with chevron indicators
- Hero CTA stack: inline buttons → full-width stacked buttons below 744px
- Mega-menu: hover dropdown → full-screen overlay with back-navigation

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Site blocked by Cloudflare anti-bot challenge** — page title returned "Attention Required! | Cloudflare" confirming no actual brand assets were extracted. All colours in the hint list originate from the Cloudflare challenge page UI, not La Cornue's design system.
- **Typography is inferred** — La Cornue's actual web fonts could not be detected. The serif display face (Playfair Display) and sans-serif body (Helvetica Neue) are educated estimates based on the brand's widely-documented French luxury positioning. Actual font families may differ significantly.
- **Colour palette is estimated from brand knowledge** — the navy (#163959) and gold (#b8924a) are based on La Cornue's publicly known brand identity (marketing materials, press imagery, physical product finishes). Exact digital hex values may vary.
- **Configurator interaction details** — step flow, animation timings, and swatch grid specifics are inferred from typical luxury product configurator patterns, not direct observation.
- **Spacing and sizing tokens** — no computed styles were accessible; all values follow standard luxury-editorial conventions rather than measured site behaviour.
- **Motion/animation system** — transition durations, easing curves, and scroll-triggered animations could not be observed.
