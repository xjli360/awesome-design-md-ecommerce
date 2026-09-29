---
version: alpha
name: "ECM"
source_url: "https://www.ecm.de/en"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  ECM's brand lives at the intersection of two temperatures — the deep royal blue (#003399) of precision instrument panels and the warm near-black (#100a05) of roasted coffee grounds. These two colors carry almost all chromatic work: a cool engineering blue beside a pigment so dark it reads as black with a trace of the roast embedded in it. The site canvas arrives in barely-warm gray (#e6e5e3) rather than paper white, a choice that keeps stainless-steel machine photography from floating on too clinical a ground. Every CTA arrives in that royal blue; no secondary accent competes for primary hierarchy. The red (#dc3232) surfaces only in system error states — it is not a brand color.

  The font stack extracted from the site returns only monospace and code-editor fallbacks — WordPress Gutenberg editor palette defaults — meaning ECM's heading face loads through JavaScript or custom theme assets and escaped extraction. What shows through element geometry and spacing is a preference for weight contrast: headline copy runs heavy at 700 with compressed letter-spacing against lighter body text at relaxed line-height. No display serifs, no decorative lettering — this is the typographic culture of a technical specification sheet elevated to editorial.

  Corner radius sits near zero throughout. The 2–4px `{rounded.xs}` and `{rounded.sm}` tokens replicate the machined-edge aesthetic of the Synchronika or Mechanika grouphead — a precise corner with only the smallest relief. Pill-shaped and full-radius buttons are absent; they would import consumer-brand softness incompatible with German precision engineering. Product cards carry only the lightest hairline border; hover state promotes the primary blue as a frame, signaling selection rather than delight animation.

  Machine detail pages function as technical portfolios: spec tables with uppercase wide-tracked labels beside values, boiler-configuration badges in primary blue, finish options surfaced as swatches. The dealer-locator is a first-class page element — ECM does not sell direct in most markets, so the purchase path runs through authorized service partners. An EN/DE language toggle anchors top-right, confirming that this German manufacturer addresses a global specialty audience on equal terms without relegating internationalization to a footer footnote.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99aad4"
  ink: "#100a05"
  body: "#313131"
  muted: "#444444"
  muted-soft: "#abb8c3"
  hairline: "#e5e7eb"
  hairline-warm: "#e6e5e3"
  canvas: "#ffffff"
  surface-soft: "#e6e5e3"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  error: "#dc3232"
  near-black: "#100a05"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.2px
  logo-display:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 2px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 72px
    logoTypography: "{typography.logo-display}"
    logoColor: "{colors.primary}"
  nav-lang-toggle:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderLeft: "1px solid {colors.hairline}"
    paddingLeft: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    badgeTypography: "{typography.spec-label}"
    padding: "{spacing.lg}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 20px rgba(0,51,153,0.10)"
  hero-full:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    imageFit: cover
    minHeight: 600px
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
  hero-split:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    imagePosition: right
    padding: "{spacing.section} 0"
  spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowStripe: "{colors.surface-soft}"
    rowBorder: "1px solid {colors.hairline}"
  machine-badge-boiler:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  machine-badge-category:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    border: "1px solid {colors.hairline}"
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    optionLabelTypography: "{typography.body-sm}"
    selectedBorder: "2px solid {colors.primary}"
  finish-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    outlineSelected: "1px solid {colors.primary}"
  dealer-locator:
    backgroundColor: "{colors.surface-soft}"
    inputBg: "{colors.canvas}"
    inputBorder: "1px solid {colors.hairline}"
    inputRounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    labelTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    mapPinColor: "{colors.primary}"
    ctaTypography: "{typography.button-sm}"
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "#aaaaaa"
    linkColor: "{colors.surface-soft}"
    borderTop: "3px solid {colors.primary}"
    headingTypography: "{typography.spec-label}"
    linkTypography: "{typography.body-sm}"
    copyrightTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Solid royal blue (#003399) fill, white text, 48px tall, 2px near-square corner (`{rounded.xs}`), 28px horizontal padding. Hover darkens to `{colors.primary-active}` (#002277); disabled drains to the muted `{colors.primary-disabled}` tint while holding identical geometry. This is the only button variant that appears above the fold — one CTA per viewport section, no competing primaries.

**`button-secondary`** — Transparent fill with a 2px royal-blue border and matching ink-blue text. Shares height (48px) and corner radius with the primary; used for secondary actions on product pages such as "Download spec sheet" beside a "Find a dealer" primary.

**`button-ghost`** — 1px `{colors.hairline}` border, `{colors.ink}` text, smaller `{typography.button-sm}`. Used for pagination controls, filter resets, and tertiary actions within spec-table footers and accessory panels.

### Text Input

**`text-input`** — White fill, 1px `{colors.hairline}` border at rest, transitions to a 1px `{colors.primary}` focus border. Near-square `{rounded.xs}` corners maintain the machined-edge grammar. 48px height aligns with button height for inline form rows in the dealer-locator search and newsletter signup.

### Navigation

**`nav-bar`** — 72px white bar with a 1px `{colors.hairline}` underline. Logo renders in `{colors.primary}` using wide-tracked uppercase (`{typography.logo-display}`). Category links sit at `{typography.nav-link}` weight 500 with no mega-menu animation or flyout panels — a flat horizontal list. The `{components.nav-lang-toggle}` (EN/DE) anchors at far right, separated by a hairline vertical rule, presenting bilingual identity as engineering spec rather than afterthought.

### Product Card

**`product-card`** — White card, 1px `{colors.hairline}` border, 4px corner (`{rounded.sm}`). Image zone fills `{colors.surface-soft}` warm gray so stainless-steel finish photographs separate cleanly from canvas. Machine name in `{typography.title-md}`, boiler type and finish variant in `{typography.body-sm}`. On hover the border transitions to `{colors.primary}` with a faint blue shadow — 10% opacity, no lift transform. `{components.machine-badge-boiler}` overlays the image corner at top-left with the boiler configuration label.

### Hero

**`hero-full`** — Full-bleed `{colors.near-black}` panel compositing machine photography against a black sweep background. Display headline in `{typography.display-xl}` white, supporting copy in `{typography.body-md}` at reduced opacity, a single primary CTA. No carousel, no autoplay — static and declarative. Minimum 600px tall on desktop; image center-crops on mobile.

**`hero-split`** — Two-column layout on `{colors.surface-soft}` warm gray: left column carries the headline in `{typography.display-md}` and body copy with a CTA; right column contains the machine at 3/4-angle at full bleed to the panel edge. Used for category landing pages (Prosumer, Commercial) where the machine is the primary argument.

### Spec Table

**`spec-table`** — Two-column row table. Label column in `{typography.spec-label}` (11px, uppercase, 1.2px tracked, `{colors.muted}`); value column in `{typography.body-sm}` `{colors.ink}`. Alternating rows use `{colors.surface-soft}` stripe. Hairline bottom borders separate rows. No hover state — read-only reference material. Standard ECM specs: boiler configuration, boiler volume (L), pump pressure (bar), heating element wattage, dimensions (W×D×H mm), weight (kg).

### Machine Badges

**`machine-badge-boiler`** — Solid primary-blue badge: `{colors.primary}` fill, `{colors.on-primary}` text, `{typography.spec-label}`, 2px `{rounded.xs}` corners, 4px×10px padding. Labels dual-boiler or heat-exchanger configuration on product cards and hero panels. Single badge per machine — never stacked.

**`machine-badge-category`** — Hairline-bordered neutral badge on `{colors.surface-card}` fill; same `{typography.spec-label}` and `{rounded.xs}` geometry as the boiler badge. Used for market segment labels (Home, Prosumer, Commercial). Neutral palette prevents competition with the primary-blue boiler badge when both appear together.

### Configurator Panel

**`configurator-panel`** — White panel, 1px `{colors.hairline}` border, `{rounded.sm}` corners, `{spacing.xl}` padding. Appears on machine detail pages for selecting finish color and optional accessories. Title in `{typography.title-md}`, option row labels in `{typography.body-sm}`. Selected option row gains a 2px `{colors.primary}` border inset. Finish colors use `{components.finish-swatch}` circles (32px, `{rounded.full}`) that gain a primary-blue outline ring on selection — the only circular element in the UI.

### Dealer Locator

**`dealer-locator`** — `{colors.surface-soft}` warm gray container with a full-width text input (`{rounded.xs}`, `{colors.hairline}` border), a scrollable partner results list, and a map panel. Results show dealer name in `{typography.title-sm}` and address in `{typography.body-sm}`. Map pins render in `{colors.primary}`. Column headings above filter controls use `{typography.spec-label}` to maintain the spec-register throughout. Link to open partner detail uses `{typography.button-sm}` styling.

### Footer

**`footer`** — `{colors.near-black}` ground with a 3px `{colors.primary}` top border as the sole brand-color signal in the dark field. Column headings in `{typography.spec-label}` rendered white, links in `{typography.body-sm}` at #aaaaaa, copyright line in `{typography.caption}`. Social icons are outline style at 20px. Language toggle repeats in the footer column for deep-page users who arrived without scrolling the nav.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero-full switches to portrait crop at 100vw; spec table scrolls horizontally inside fixed viewport |
| Tablet | 744–1128px | Two-column product grid; split hero maintains two columns with reduced padding; configurator panel moves below machine image |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav bar; split hero at 50/50 column split; spec table beside configurator panel |
| Wide | > 1440px | Max-width container 1280px centered; hero image expands while copy column holds fixed width; footer grid widens column gutters |

### Touch Targets

- All buttons minimum 48px height across all breakpoints
- Finish swatches expand to 44×44px touch target via invisible padding on mobile; visible swatch remains 32px
- Dealer search input holds 48px height at all breakpoints
- Nav drawer links minimum 48px row height with full-width tap area
- Badge elements are display-only and do not require tap targets

### Collapsing Strategy

- Navigation: horizontal link row collapses to hamburger drawer with full-height overlay at < 744px; language toggle relocates inside drawer bottom
- Product grid: 3-col → 2-col at tablet → 1-col at mobile; card images shift to 4:3 aspect ratio on mobile
- Hero full: maintains full-bleed at all breakpoints; headline drops from 48px to 32px on mobile; CTA button goes full-width
- Hero split: stacks to single column (image above, copy below) at < 744px; image becomes 16:9 cropped banner
- Spec table: wraps in horizontal-scroll container on mobile with left column sticky for label legibility
- Configurator panel: side-by-side with machine image on desktop → stacked below image on tablet and mobile; swatch rows reflow to wrap grid
- Footer: 4-column link grid → 2-column at tablet → single-column accordion (headings are expand triggers) at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Brand typeface not captured**: all extracted font-family values are WordPress Gutenberg editor defaults (monospace stacks — Andale Mono, Courier, Monaco, consolas). ECM's heading and body face loads via JavaScript or a custom theme bundle. All typography tokens fall back to system-ui sans-serif; true weight distribution and optical sizing may differ materially.
- **True root canvas color**: site may use pure white (#ffffff) for the document root; the warm gray (#e6e5e3) readings may originate from section backgrounds rather than the page ground, and `{colors.surface-soft}` vs `{colors.canvas}` assignments may need inversion.
- **No meta theme-color**: mobile browser chrome color not confirmed; `{colors.primary}` (#003399) assumed for PWA address-bar treatment but unverified.
- **Dark mode**: unknown whether ECM provides a prefers-color-scheme dark variant; near-black elements are observed only in hero sections of the light theme.
- **Price and configurator typography**: purchase-price display scale and configurator option pricing style not extractable; `{typography.title-md}` and `{typography.spec-label}` are approximations.
- **Icon system**: navigation icons and product-page pictograms not inspectable from extraction; outline/line style at 20–24px assumed based on category conventions.
- **Animation and easing**: no transition duration or easing curve values captured; 150–200ms ease-out assumed throughout.
- **Many extracted colors are Gutenberg defaults**: #00d084, #0693e3, #7a00df, #34e2e4, #ab1dfe, #4721fb and similar are WordPress editor palette colors, not ECM brand colors — excluded from the palette.
