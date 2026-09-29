---
version: alpha
name: "Boka"
source_url: "https://www.boka.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Boka is mindful oral care that feels more like a morning ritual than a hygiene chore. The brand lives in a warm, tactile space anchored by a near-black ink (`#090909`) and a soft, creamy canvas (`#fafaf5`) that reads as natural and unbleached — like uncoated paper or a stoneware mug. A dusty rose accent (`#fae5db`) and a muted coral (`#f19a7e`) provide the brand's signature warmth, appearing in product highlights, badges, and hover states, while a deep teal (`#1990c6`) and a darker navy (`#136f99`) add a clean, clinical counterpoint for ingredient callouts and secondary CTAs. The typography is a deliberate mix of the sturdy, geometric Archivo for headlines and the refined Cera Pro family for body and buttons — CeraProMedium at 14–16px for navigation, CeraProRegular for product descriptions, and CeraProLight for captions. A single italic accent (`IvarDisplayItalic`) appears sparingly, likely for pull quotes or editorial moments. The system uses generous `{rounded.full}` pill shapes for buttons and search bars, `{rounded.lg}` (20px) for product cards, and `{rounded.sm}` (8px) for input fields — a mix that balances approachability with precision. The overall mood is calm, considered, and slightly elevated: a DTC brand that trusts soft color, clean type, and negative space over aggressive marketing.

colors:
  primary: "#090909"
  primary-active: "#121212"
  primary-disabled: "#dedede"
  ink: "#090909"
  body: "#212529"
  muted: "#767676"
  muted-soft: "#989494"
  hairline: "#dedede"
  hairline-soft: "#fafaf5"
  canvas: "#fafaf5"
  surface-soft: "#fae5db"
  surface-card: "#ffffff"
  on-primary: "#fafaf5"
  accent-coral: "#f19a7e"
  accent-teal: "#1990c6"
  accent-navy: "#136f99"
  accent-green: "#5a9447"
  badge-warm: "#fae5db"
  badge-coral: "#f19a7e"

typography:
  display-xl:
    fontFamily: "'Archivo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Archivo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Archivo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Archivo', 'Helvetica', 'Arial', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'CeraProMedium', 'Helvetica', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'CeraProMedium', 'Helvetica', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'CeraProRegular', 'Helvetica', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'CeraProRegular', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'CeraProLight', 'Helvetica', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'CeraProMedium', 'Helvetica', 'Arial', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'CeraProMedium', 'Helvetica', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'CeraProRegular', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'CeraProMedium', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  badge:
    fontFamily: "'CeraProBold', 'Helvetica', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  pull-quote:
    fontFamily: "'IvarDisplayItalic', 'Georgia', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
    fontStyle: italic

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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.accent-coral}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    border-bottom: "2px solid {colors.ink}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
    aspectRatio: "1 / 1"
    objectFit: "contain"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-sale:
    backgroundColor: "{colors.badge-coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-ingredient:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
    height: 56px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg} {spacing.lg} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border-bottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-active:
    backgroundColor: "{colors.accent-teal}"
  toggle-switch-thumb:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button with a near-black background (`#090909`) and warm off-white text (`#fafaf5`). On hover, the background deepens to `#121212`; when disabled, it fades to `#dedede` with muted text. The button uses CeraProMedium at 15px with 0.5px letter-spacing for a refined, intentional feel. **`button-secondary`** — An outlined variant on the warm canvas background (`#fafaf5`) with a thin `#dedede` border. Hover state darkens the border to `#090909` and fills with the soft `#fae5db` surface. **`button-accent-coral`** and **`button-accent-teal`** — Used for promotional or secondary flows (e.g., "Shop Sale" or "Learn About Ingredients"), leveraging the brand's coral (`#f19a7e`) and teal (`#1990c6`) accents respectively.

### Cards
**`product-card`** — A white card (`#ffffff`) with 20px rounded corners (`{rounded.lg}`) that cradles product imagery. The image area uses `object-fit: contain` to preserve product proportions, with top corners rounded to match the card. Title uses CeraProMedium at 16px, price in CeraProRegular at 14px in muted gray (`#767676`). Cards sit on the warm canvas background with generous spacing between them. **`hero-section`** — A full-width banner using the canvas background with large Archivo headlines (48px) and a prominent pill-shaped CTA. The hero uses the brand's signature negative space, with text and imagery balanced rather than stacked.

### Navigation
**`nav-bar`** — A fixed 72px bar on the warm canvas background, with navigation links in CeraProMedium at 14px (0.5px letter-spacing). Active links have a 2px bottom border in `#090909`; inactive links render in `#767676`. The bar includes a centered logo and a cart icon with a subtle badge. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — A clean input field with 8px rounded corners (`{rounded.sm}`), white background, and a `#dedede` border. Focus state shifts the border to `#090909`; error state uses the coral accent (`#f19a7e`). Inputs use CeraProRegular at 16px for readability. **`newsletter-input`** — A pill-shaped input (`{rounded.full}`) paired with a teal submit button, used in the footer for email capture. The input has a `#dedede` border and sits on the dark footer background.

### Badges
**`badge-new`** — A warm pill badge (`#fae5db`) with uppercase CeraProBold at 11px, used to flag new products. **`badge-sale`** — A coral badge (`#f19a7e`) with white text for promotional items. **`badge-ingredient`** — A green badge (`#5a9447`) used to highlight key ingredients like "Nano-Hydroxyapatite" or "Charcoal."

### Footer
**`footer`** — A dark section with `#090909` background and warm off-white text. Links render in a muted warm gray (`#989494`) and use CeraProRegular at 14px. The footer includes a newsletter signup, a column of links, and social icons. Spacing is generous with 48px padding.

### Accordion
**`accordion`** — Used for FAQ and product details, with a white background and a thin `#fafaf5` bottom border. The header uses CeraProMedium at 18px; the expanded content uses CeraProRegular at 14px in `#212529`. No icons — relies on subtle text styling and spacing to indicate expandability.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to 32px; buttons become full-width; footer links stack |
| Tablet | 744–1128px | Two-column product grid; nav remains visible but compresses; hero uses 40px display; side padding reduces to 24px |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 48px; standard side padding of 32px |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid can expand to four columns; hero remains centered |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 48px.
- Icon buttons and cart icons are at least 44x44px.
- Accordion headers have 48px tap targets.
- Nav links have 48px tap areas on mobile.

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px, with a full-screen overlay.
- Product grids reduce from 3–4 columns to 2 columns on tablet, 1 column on mobile.
- Footer link columns stack vertically on mobile.
- Hero sections stack image and text vertically on mobile.
- Accordion content is hidden by default on all breakpoints.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., text-input, accordion, footer links) could not be fully extracted.
- Error and success states for forms (e.g., validation messages, input borders) are inferred from common patterns but not confirmed.
- Dark mode is not present on the live site; all tokens assume a light theme.
- Sub-brand or collection-specific palettes (e.g., "Boka for Kids") may exist but were not observed.
- Animation and transition durations (e.g., button hover, accordion expand) are not specified.
- Specific font weights for Cera Pro variants (e.g., CeraProBlack, CeraProBold) are declared but their exact usage contexts are inferred.
- The `IvarDisplayItalic` font appears only in limited contexts; its full usage (pull quotes, editorial) is assumed.
- Product card hover states (e.g., shadow, scale) are not confirmed.
- Search overlay or dropdown behavior is not documented.
- Accessibility focus indicators (e.g., `:focus-visible` outlines) are not specified.
