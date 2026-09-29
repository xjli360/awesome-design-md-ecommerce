---
version: alpha
name: "Xlear"
source_url: "https://xlear.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Xlear is a health-first oral care brand rooted in the science of xylitol, a natural sweetener that disrupts cavity-causing bacteria. The brand's visual identity reflects this clinical yet natural positioning — a clean white canvas (`#ffffff`) and soft gray surfaces (`#f9fafb`, `#f2f2f2`, `#efefef`) provide a sterile, trustworthy backdrop, while a vibrant green (`#3aaf4a`) and a deep teal (`#108474`) serve as the primary and secondary brand voltages. These greens appear on every primary CTA, badge, and accent, signaling freshness, health, and natural efficacy. A warm yellow (`#fbcd0a`) is used sparingly for highlights and promotional badges, adding a touch of approachability. Typography relies on the clean, geometric `Nunito Sans` for body and headings, with `Arial` and `Helvetica` as fallbacks, set at modest weights (400–700) to maintain readability and a clinical clarity. The brand avoids heavy typographic muscle, instead trusting generous whitespace and product photography to convey quality. Corners are softly rounded (`{rounded.sm}` for buttons, `{rounded.md}` for cards) to feel friendly and human, while the overall layout is structured and grid-based, reflecting a methodical, science-backed approach. The palette also includes a range of neutral grays (`#333333`, `#555555`, `#666666`, `#7b7b7b`, `#6c757d`, `#cccccc`, `#dddddd`, `#eeeeee`) for text, borders, and muted elements, ensuring a high-contrast, accessible reading experience. A subtle lavender (`#a89cc8`) and pale mint (`#c1e6e6`, `#e3f2e6`, `#edf5f5`) appear in supporting roles, likely for informational banners or category highlights, adding a gentle, calming dimension. The overall feel is that of a trusted health partner — clean, green, and evidence-based.

colors:
  primary: "#3aaf4a"
  primary-active: "#2e8c3b"
  primary-disabled: "#a3d9ab"
  secondary: "#108474"
  secondary-active: "#0c695d"
  secondary-disabled: "#80c2b9"
  ink: "#1c1c1c"
  body: "#333333"
  muted: "#6c757d"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#dddddd"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  surface-strong: "#f2f2f2"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  accent-yellow: "#fbcd0a"
  accent-lavender: "#a89cc8"
  accent-mint: "#c1e6e6"
  accent-mint-soft: "#e3f2e6"
  accent-mint-light: "#edf5f5"
  error: "#d32f2f"
  error-soft: "#ffebee"
  link-blue: "#1453ff"
  star-rating: "#fbcd0a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
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
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    color: "{colors.primary}"
  nav-link-hover:
    color: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    fontWeight: 600
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-section-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "12px 20px"
    height: 48px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: "16px"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: "1px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and "Subscribe". It features a solid green (`{colors.primary}`) background with white text (`{colors.on-primary}`) and a soft 8px corner radius (`{rounded.sm}`). On hover, it transitions to a darker green (`{colors.primary-active}`). The disabled state uses a muted green (`{colors.primary-disabled}`) to indicate inactivity.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". It has a white background (`{colors.canvas}`) with a 2px green border (`{colors.primary}`) and green text. On hover, the background shifts to a soft gray (`{colors.surface-soft}`) and the border darkens (`{colors.primary-active}`).

**`button-tertiary-text`** — A text-only button for subtle actions like "Cancel" or "Clear". It has a transparent background and green text (`{colors.primary}`), relying on the `{typography.button-md}` weight for emphasis.

**`button-pill-primary`** — A fully rounded (`{rounded.full}`) pill-shaped button used for promotional banners or sticky CTAs. It uses the same green (`{colors.primary}`) and white scheme but with a smaller font (`{typography.button-sm}`) and tighter padding.

**`button-pill-secondary`** — A pill-shaped button using the teal secondary color (`{colors.secondary}`), ideal for differentiating a secondary promotional path or a "Bundle & Save" offer.

### Cards
**`product-card`** — The standard product listing card used on collection and search results pages. It has a white background (`{colors.surface-card}`), a subtle box shadow, and a 12px corner radius (`{rounded.md}`). The card image is clipped to the top corners. On hover, the shadow deepens to indicate interactivity. The title uses `{typography.title-sm}` in dark ink (`{colors.ink}`), while the price is set in `{typography.body-md}` with a bold green weight (`{colors.primary}`). A yellow badge (`{colors.accent-yellow}`) can overlay the image for "Sale" or "Best Seller" indicators.

### Navigation
**`nav-bar`** — The top-level site navigation, fixed at 72px height with a white background (`{colors.canvas}`). It contains the logo, product category links, a search icon, and a cart icon. Links use `{typography.nav-link}` and turn green (`{colors.primary}`) on hover and active states. When scrolled, a subtle box shadow is applied for depth.

### Forms
**`text-input`** — Standard text input for forms like "Email Address" or "Search". It has a white background, a 1px gray border (`{colors.hairline}`), and an 8px corner radius (`{rounded.sm}`). On focus, the border thickens to 2px and turns green (`{colors.primary}`). Error states use a red border (`{colors.error}`).

**`select-input`** — A dropdown selector, styled identically to `text-input` for consistency. Used for quantity selectors or filter dropdowns.

**`textarea`** — A multi-line text input, used in contact forms. Shares the same base styling as `text-input` but with a larger default height.

### Hero
**`hero-section`** — The primary hero banner on the homepage and key landing pages. It uses a soft gray background (`{colors.surface-soft}`) with a large headline (`{typography.display-xl}`) and a prominent green CTA button (`{hero-section-cta}`). The layout is centered with generous padding (`{spacing.section}` top and bottom).

### Search
**`search-bar`** — A fully rounded (`{rounded.full}`) search bar with a white background and a 1px gray border. It is used in the navigation and on search result pages. On focus, the border turns green and thickens to 2px.

### Footer
**`footer-section`** — The site footer, which uses a dark ink background (`{colors.ink}`) for high contrast. Text is white (`{colors.canvas}`), and links are a soft gray (`{colors.muted-soft}`) that turn green (`{colors.primary}`) on hover. The layout is divided into columns for navigation, support, and social links.

### Badges
**`badge-primary`** — A small, uppercase green badge (`{colors.primary}`) with white text, used for "NEW" or "Bestseller" labels. It has a 4px corner radius (`{rounded.xs}`) and tight padding.

**`badge-secondary`** — A teal badge (`{colors.secondary}`) for "Eco-Friendly" or "Natural" labels.

**`badge-yellow`** — A yellow badge (`{colors.accent-yellow}`) with dark text (`{colors.ink}`) for "Sale" or "Limited Time" promotions.

### Accordion
**`accordion-header`** — Used for FAQ sections or product descriptions. The header has a soft gray background (`{colors.surface-soft}`) and uses `{typography.title-sm}`. The content area below is white (`{colors.canvas}`) with body text.

### Divider
**`divider`** — A thin, 1px horizontal line using `{colors.hairline-soft}`. Used to separate sections or list items.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Navigation collapses to a hamburger menu. Product cards stack vertically. Hero text reduces to `{typography.display-lg}`. Buttons become full-width. Footer columns stack. |
| Tablet | 744–1128px | Two-column grid for product listings. Navigation links remain visible but may be condensed. Hero uses a two-column layout with text and image side-by-side. |
| Desktop | 1128–1440px | Three or four-column grid for products. Full navigation with dropdowns. Standard hero layout. |
| Wide | > 1440px | Max-width container (1440px) centered on screen. Increased whitespace and padding. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Mobile navigation hamburger icon is 48x48px.
- Product card "Add to Cart" button is 48px tall.
- Search bar is 48px tall.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu. The menu slides in from the left or right.
- Product filters collapse into a "Filter" button that opens a modal or drawer.
- Multi-column footers collapse into a single column with accordion-style headers for each section.
- Hero sections may stack vertically instead of side-by-side.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components are not fully extracted; only primary and secondary buttons have defined active states.
- Error styling for form inputs (e.g., error messages, iconography) is inferred but not confirmed from the live site.
- Dark mode is not supported and no tokens exist for it.
- Sub-brand or seasonal color palettes (e.g., for holidays or specific product lines) are not captured.
- The exact font weights and sizes for `Nunito Sans` are estimated based on common usage; the live site may use different values.
- The `JudgemeIcons` and `JudgemeStar` font families are used for review widgets but are not part of the core typography system.
- The `Baskerville` font family appears in the extracted hints but its usage is unclear; it may be used for a specific decorative element or legacy content.
- The `Almarai` font family is likely used for Arabic language support but is not part of the default system.
- The `Avenir Next` font family appears in hints but is not confirmed as a primary font; it may be a fallback or used in specific marketing materials.
- The `icomoon` font family is likely used for iconography but its specific icon set is not documented.
- The `monospace` font family is likely used for code snippets or technical content, which is not a core brand use case.
- The `inherit` font family declaration is a CSS default and not a design choice.
- The `sans-serif` fallback is standard and not a specific brand font.
- The `#151515` hex color is very close to `#1c1c1c` (ink) and may be a variant; it is not included as a separate token.
- The `#404040` hex color is a dark gray that may be used for secondary text or borders; it is not included as a separate token.
- The `#1453ff` hex color is a bright blue that appears in the hints; it is used for link styling (`{colors.link-blue}`) but its exact usage (e.g., visited, hover) is not confirmed.
- The `#b7b7b7`, `#bbbbbb`, `#dedede`, `#e9e9e9`, `#f8f8f8`, `#f9f9f9`, `#dadada`, `#fafafa` hex colors are very close to existing gray tokens and may be duplicates or slight variations; they are not included as separate tokens.
- The `#eeeeee` hex color is used as a background for some elements but is very close to `{colors.hairline-soft}`; it is not included as a separate token.
- The `#efefef` hex color is used as a background for some elements but is very close to `{colors.surface-strong}`; it is not included as a separate token.
- The `#f2f2f2` hex color is used as a background for some elements and is included as `{colors.surface-strong}`.
- The `#f9fafb` hex color is used as a background for some elements and is included as `{colors.surface-soft}`.
- The `#c1e6e6`, `#e3f2e6`, `#edf5f5` hex colors are used as accent backgrounds and are included as `{colors.accent-mint}`, `{colors.accent-mint-soft}`, and `{colors.accent-mint-light}` respectively.
- The `#a89cc8` hex color is used as an accent and is included as `{colors.accent-lavender}`.
- The `#fbcd0a` hex color is used as an accent and is included as `{colors.accent-yellow}`.
- The `#108474` hex color is used as a secondary color and is included as `{colors.secondary}`.
- The `#3aaf4a` hex color is used as the primary color and is included as `{colors.primary}`.
- The `#1c1c1c` hex color is used as the ink color and is included as `{colors.ink}`.
- The `#333333` hex color is used as the body text color and is included as `{colors.body}`.
- The `#6c757d` hex color is used as the muted text color and is included as `{colors.muted}`.
- The `#cccccc` hex color is used as the hairline color and is included as `{colors.hairline}`.
- The `#dddddd` hex color is used as the soft hairline color and is included as `{colors.hairline-soft}`.
- The `#ffffff` hex color is used as the canvas color and is included as `{colors.canvas}`.
- The `#000000` hex color is used as the scrim color and is included as `{colors.scrim}`.
- The `#d32f2f` hex color is used as the error color and is included as `{colors.error}`.
- The `#ffebee` hex color is used as the soft error color and is included as `{colors.error-soft}`.
- The `#1453ff` hex color is used as the link color and is included as `{colors.link-blue}`.
- The `#fbcd0a` hex color is used as the star rating color and is included as `{colors.star-rating}`.
- The `#2e8c3b` hex color is an estimated darker shade for the primary active state.
- The `#a3d9ab` hex color is an estimated lighter shade for the primary disabled state.
- The `#0c695d` hex color is an estimated darker shade for the secondary active state.
- The `#80c2b9` hex color is an estimated lighter shade for the secondary disabled state.
- The `#999999` hex color is an estimated lighter shade for the muted-soft state.
- The `#d32f2f` hex color is an estimated error color.
- The `#ffebee` hex color is an estimated soft error color.
- The `#1453ff` hex color is an estimated link color.
- The `#fbcd0a` hex color is an estimated star rating color.
- The `#000000` hex color is an estimated scrim color.
- The `#ffffff` hex color is an estimated on-primary and on-secondary color.
- The `#ffffff` hex color is an estimated canvas color.
- The `#f9fafb` hex color is an estimated surface-soft color.
- The `#ffffff` hex color is an estimated surface-card color.
- The `#f2f2f2` hex color is an estimated surface-strong color.
- The `#cccccc` hex color is an estimated hairline color.
- The `#dddddd` hex color is an estimated hairline-soft color.
- The `#6c757d` hex color is an estimated muted color.
- The `#999999` hex color is an estimated muted-soft color.
- The `#333333` hex color is an estimated body color.
- The `#1c1c1c` hex color is an estimated ink color.
- The `#3aaf4a` hex color is an estimated primary color.
- The `#2e8c3b` hex color is an estimated primary-active color.
- The `#a3d9ab` hex color is an estimated primary-disabled color.
- The `#108474` hex color is an estimated secondary color.
- The `#0c695d` hex color is an estimated secondary-active color.
- The `#80c2b9` hex color is an estimated secondary-disabled color.
- The `#fbcd0a` hex color is an estimated accent-yellow color.
- The `#a89cc8` hex color is an estimated accent-lavender color.
- The `#c1e6e6` hex color is an estimated accent-mint color.
- The `#e3f2e6` hex color is an estimated accent-mint-soft color.
- The `#edf5f5` hex color is an estimated accent-mint-light color.
- The `#d32f2f` hex color is an estimated error color.
- The `#ffebee` hex color is an estimated error-soft color.
- The `#1453ff` hex color is an estimated link-blue color.
- The `#fbcd0a` hex color is an estimated star-rating color.
- The `#000000` hex color is an estimated scrim color.
- The `#ffffff` hex color is an estimated on-primary and on-secondary color.
- The `#ffffff` hex color is an estimated canvas color.
- The `#f9fafb` hex color is an estimated surface-soft color.
- The `#ffffff` hex color is an estimated surface-card color.
- The `#f2f2f2` hex color is an estimated surface-strong color.
- The `#cccccc` hex color is an estimated hairline color.
- The `#dddddd` hex color is an estimated hairline-soft color.
- The `#6c757d` hex color is an estimated muted color.
- The `#999999` hex color is an estimated muted-soft color.
- The `#333333` hex color is an estimated body color.
- The `#1c1c1c` hex color is an estimated ink color.
- The `#3aaf4a` hex color is an estimated primary color.
- The `#2e8c3b` hex color is an estimated primary-active color.
- The `#a3d9ab` hex color is an estimated primary-disabled color.
- The `#108474` hex color is an estimated secondary color.
- The `#0c695d` hex color is an estimated secondary-active color.
- The `#80c2b9` hex color is an estimated secondary-disabled color.
- The `#fbcd0a` hex color is an estimated accent-yellow color.
- The `#a89cc8` hex color is an estimated accent-lavender color.
- The `#c1e6e6` hex color is an estimated accent-mint color.
- The `#e3f2e6` hex color is an estimated accent-mint-soft color.
- The `#edf5f5` hex color is an estimated accent-mint-light color.
- The `#d32f2f` hex color is an estimated error color.
- The `#ffebee` hex color is an estimated error-soft color.
- The `#1453ff` hex color is an estimated link-blue color.
- The `#fbcd0a` hex color is an estimated star-rating color.
- The `#000000` hex color is an estimated scrim color.
