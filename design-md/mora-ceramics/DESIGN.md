---
version: alpha
name: "Mora Ceramics"
source_url: "https://moraceramics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A tactile, earth-honoring dinnerware brand that speaks through quiet texture and warm neutrals rather than loud graphics. The canvas is a soft, almost chalky off-white (`#f3f2ee`), not a clinical bright white — it reads like unglazed stone or aged linen, setting a foundation that feels hand-touched rather than machine-perfect. Against this, the ink (`#121212`) and body (`#242833`) provide a restrained contrast that never screams; even the primary accent, a deep clay brown (`#3e2015`), emerges from the earth rather than from a Pantone brief. The brand's signature voltage comes from an unexpected sky blue (`#899df1`) — a color that appears in badges, hover states, and editorial accents — paired with a deeper cerulean (`#1990c6` and `#136f99`) that suggests hand-painted cobalt motifs on heritage pottery. Typography leans on Playfair Display for display roles, lending a serifed, editorial gravity to product names and headings, while the rest of the system stays clean and unobtrusive. Corners are softly rounded — `{rounded.sm}` (8px) on buttons, `{rounded.md}` (12px) on cards — never pill-shaped, always suggesting the gentle chamfer of a ceramic edge. The overall mood is curated but not precious: a dinner party where the host knows the provenance of every plate but doesn't mention it.

colors:
  primary: "#3e2015"
  primary-active: "#2d150e"
  primary-disabled: "#dedede"
  ink: "#121212"
  body: "#242833"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#f3f2ee"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#899df1"
  accent-blue-hover: "#1990c6"
  accent-blue-deep: "#136f99"
  badge-new: "#899df1"
  badge-sale: "#3e2015"
  star-rating: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, system-ui, Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    objectFit: contain
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid #d32f2f"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the deep clay brown (`{colors.primary}`) with white text and soft 8px rounding (`{rounded.sm}`). Uppercase label uses `{typography.button-md}` at 14px/600 weight. On hover, the background deepens to `{colors.primary-active}`. The disabled state fades to `{colors.primary-disabled}` with muted text, signaling non-interactivity without harsh contrast.

**`button-secondary`** — An outlined variant on the warm canvas background (`{colors.canvas}`) with a thin `{colors.hairline}` border. Hover promotes the border to `{colors.ink}` and fills the background with `{colors.surface-soft}`, creating a subtle elevation without competing with the primary button.

**`button-text`** — A borderless, backgroundless text button used for tertiary actions like "View details" or "Cancel." Hover shifts text to `{colors.primary}`, maintaining the brand's restrained approach to feedback.

### Cards
**`product-card`** — A white (`{colors.surface-card}`) card with soft 8px rounding, no padding on the image area, and a clean layout for title and price below. On hover, a gentle box shadow lifts the card while the image remains `object-fit: contain` to preserve the ceramic's true proportions. The title uses `{typography.title-sm}` (Playfair Display 16px/500) and the price uses `{typography.body-md}` (sans-serif 16px/400).

**`badge-new`** and **`badge-sale`** — Small, uppercase badges pinned to product cards. The "New" badge uses the brand's signature sky blue (`{colors.badge-new}`), while "Sale" uses the primary clay brown (`{colors.badge-sale}`). Both are tightly padded with 2px vertical / 8px horizontal and set in 10px bold uppercase.

### Navigation
**`nav-bar`** — A 72px-tall bar on the warm canvas background with a subtle bottom hairline (`{colors.hairline-soft}`). Navigation links are uppercase 14px/500 in `{typography.nav-link}`. The active state adds a 2px bottom border in `{colors.primary}`, while inactive links sit in `{colors.muted}`.

**`search-bar`** — A simple input with 8px rounding and a `{colors.hairline}` border. On focus, the border switches to `{colors.primary}`, providing a clear but understated active state. Height and padding match the text-input component for consistency across form elements.

### Forms
**`text-input`** — Standard 44px-tall input with 8px rounding, `{colors.hairline}` border, and `{typography.body-sm}`. Focus state uses `{colors.primary}` border. Error state uses a red border (#d32f2f) — note that error text styling and helper text patterns were not reliably extracted from the live site.

**`select-dropdown`** and **`quantity-selector`** — Both follow the same dimensions and border treatment as text inputs, ensuring a cohesive form language. The quantity selector is slightly shorter (40px) for use in cart line items.

### Footer
**`footer`** — A dark footer on `{colors.ink}` with white text. Links use `{typography.link}` (14px/400) and shift to `{colors.accent-blue}` on hover, introducing the brand's blue accent as a navigational signal rather than a primary action color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero text reduces to `{typography.display-lg}`; search bar moves to drawer; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses `{typography.display-xl}`; sidebar filters become horizontal strip |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero full-width with CTA; footer in four-column layout |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; hero content centered with max-width 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility.
- Icon buttons are 40x40px with 40px touch area.
- Nav links have minimum 44px tap targets even when text is smaller.
- Product card CTAs ("Add to Cart") are full-width on mobile for easy tapping.

### Collapsing Strategy
- Navigation: On mobile (< 744px), the full nav menu collapses into a hamburger icon with a slide-in drawer. The search icon remains visible in the header.
- Product filters: On tablet and below, sidebar filters collapse into a horizontal scrollable strip or a "Filter" button that opens a modal.
- Footer: On mobile, the four-column footer collapses into a single column with accordion-style sections for links.
- Hero: On mobile, hero images may crop or stack vertically, and the CTA button becomes full-width.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow intensity, any scale transforms) were inferred from common patterns but not directly extracted.
- Error styling for forms (error message text color, helper text patterns, validation iconography) was not reliably captured from the live site.
- Dark mode tokens are absent — the brand does not currently ship a dark theme, and no dark-mode CSS was detected.
- Sub-brand or collection-specific palettes (e.g., limited-edition colorways) were not extracted; only the global brand tokens are represented here.
- Animation tokens (transition durations, easing curves, micro-interactions) were not reliably parsed from the site's CSS.
- Focus ring styles (outline color, offset, width) for keyboard navigation were not consistently detectable.
- The `object-fit: contain` declaration was found on product images, but the exact aspect ratio or container sizing was not confirmed.
- Typography line-height values for body and caption styles are estimated based on common brand patterns; the exact extracted values may differ slightly.
