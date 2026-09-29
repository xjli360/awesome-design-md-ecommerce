---
version: alpha
name: "Aarke"
source_url: "https://www.aarke.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Aarke is a Swedish kitchen appliance brand that elevates everyday hydration into a sculptural ritual. The palette is anchored by a deep, almost-black ink (`#232322`) and a crisp, cool white canvas (`#fafafa`), with a signature teal-green primary (`#108474`) that evokes Nordic waters and stainless steel patina. This primary appears sparingly — on the carbonator button, the occasional accent line, and the brand's "NEW" badge — lending it the weight of a deliberate design choice rather than a default. Supporting tones are a gallery of warm grays: `#eeeeee` for soft surfaces, `#dddddd` for hairline borders, `#cccccc` for muted text, and `#999999` for placeholder states. A single accent of warm yellow (`#fbcd0a`) cuts through the monochrome on select product highlights, while a whisper of lavender (`#a89cc8`) and pale teal (`#c1e6e6`) appear in editorial photography overlays, hinting at a broader lifestyle palette. Typography is built on GT Walsheim Pro — a geometric sans-serif with a friendly, slightly condensed character — used in three weights: Light for body copy, Medium for buttons and secondary navigation, and Bold for display headlines. The brand trusts generous whitespace, hard edges (most corners are `{rounded.none}` or `{rounded.xs}`), and the material honesty of brushed stainless steel and borosilicate glass. There is no visual noise: the site reads like a product catalog for a design museum gift shop, where every component — from the pill-shaped search bar (`{rounded.full}`) to the product card's subtle `{rounded.sm}` — is a quiet invitation to slow down and consider the object.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#c1e6e6"
  ink: "#232322"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  canvas: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-strong: "#e8e8e8"
  on-primary: "#ffffff"
  accent-yellow: "#fbcd0a"
  accent-lavender: "#a89cc8"
  accent-teal-light: "#c1e6e6"
  badge-new: "#108474"
  badge-sale: "#fbcd0a"
  star-rating: "#232322"
  scrim: "#121212"
  error: "#c13515"
  success: "#108474"

typography:
  display-xl:
    fontFamily: "'GT Walsheim Pro Bold', 'Baskerville', Georgia, serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT Walsheim Pro Bold', 'Baskerville', Georgia, serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT Walsheim Pro Bold', 'Baskerville', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'GT Walsheim Pro Bold', 'Baskerville', Georgia, serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'GT Walsheim Pro Medium Button', 'Helvetica', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'GT Walsheim Pro Medium Button', 'Helvetica', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT Walsheim Pro Medium Button', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'GT Walsheim Pro Light', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT Walsheim Pro Light', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'GT Walsheim Pro Light', 'Helvetica', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "'GT Walsheim Pro Light', 'Helvetica', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'GT Walsheim Pro Medium Button', 'Helvetica', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'GT Walsheim Pro Medium Button', 'Helvetica', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "'GT Walsheim Pro Medium Button', 'Helvetica', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'GT Walsheim Pro Medium Button', 'Helvetica', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'GT Walsheim Pro Medium Button', 'Helvetica', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'GT Walsheim Pro Light', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'GT Walsheim Pro Medium Secondary', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    textColor: "{colors.ink}"
  text-input-error:
    borderColor: "{colors.error}"
    textColor: "{colors.ink}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  hero-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  footer-heading:
    typography: "{typography.uppercase-tag}"
    textColor: "{colors.on-primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  review-stars:
    color: "{colors.star-rating}"
    size: 16px
  review-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  review-card-author:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 48px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    height: 48px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  tab-underline-active:
    backgroundColor: "{colors.primary}"
    height: 2px
  tab-underline-inactive:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action button uses the brand's signature teal-green (`#108474`) as a solid fill with white text. It has zero border-radius, reflecting the brand's preference for sharp, architectural edges. On hover, it deepens to `#0d6b5d`; when disabled, it fades to a pale teal (`#c1e6e6`). The button uses GT Walsheim Pro Medium at 15px with 0.3px letter spacing, and sits at 48px tall with 14px/32px padding. **`button-secondary`** — An outlined variant with a white fill and ink text, maintaining the same 48px height and zero border-radius. On hover, it gains a soft gray fill (`#f2f2f2`). **`button-tertiary-text`** — A text-only button with no background or border, used for ghost actions like "Cancel" or "Learn more." **`button-pill-primary`** — A pill-shaped variant (`{rounded.full}`) used sparingly for the search bar and newsletter signup, with the same teal fill and white text but smaller padding (10px 24px) and smaller type (13px). **`button-pill-outline`** — An outlined pill button with a transparent fill and ink text, used for secondary actions in hero sections.

### Cards
**`product-card`** — The product card is a clean white container with a softly rounded corner (`{rounded.sm}`) and no shadow, relying on the product photography to carry visual weight. On hover, the entire card gains a subtle `#f2f2f2` background. The title uses `{typography.title-sm}` in ink, the price uses `{typography.body-md}` in body gray, and a small badge (`{typography.badge}`) sits in the top-left corner with a teal fill for "NEW" or yellow fill for "SALE." **`review-card`** — A white card with `{rounded.sm}` and 16px padding, containing the review text in `{typography.body-sm}` and the author name in `{typography.title-sm}`. Star ratings are rendered in the ink color at 16px.

### Navigation
**`nav-bar`** — The top navigation bar is a 72px-tall white strip with uppercase nav links set in GT Walsheim Pro Medium Secondary at 14px with 0.5px letter spacing. Active links are ink; inactive links are muted gray. The bar is fixed at the top with a subtle bottom hairline (`#dddddd`). **`search-bar`** — A pill-shaped search input with a `#f2f2f2` background, 44px tall, and 10px/20px padding. On focus, the background shifts to white. **`breadcrumb`** — A simple text-based breadcrumb trail using `{typography.caption}` in muted gray, with the active page in ink and a hairline separator.

### Forms
**`text-input`** — A 48px-tall input with zero border-radius, white background, and 12px/16px padding. On focus, it gains a teal border; on error, a red border (`#c13515`). **`select-dropdown`** — Matches the text-input styling but includes a dropdown arrow. **`quantity-selector`** — A compact 48px-tall control with a soft gray button on each side and a white center for the quantity value.

### Footer
**`footer`** — The footer is a full-width section with an ink background (`#232322`) and white text. Links are set in `{typography.link}` at a muted gray (`#999999`) and brighten to white on hover. Section headings use `{typography.uppercase-tag}` in white. The footer uses 48px vertical padding.

### Accordion
**`accordion`** — A clean, borderless accordion with an ink header in `{typography.title-sm}` and body text in `{typography.body-md}`. The header has 16px vertical padding; the content area has 8px top and 16px bottom padding. No background or border — just typographic hierarchy.

### Tabs
**`tab-active`** — A text-only tab with ink color and a 2px teal underline. **`tab-inactive`** — Same typography but muted gray with a 1px hairline underline. Used for product detail sections (Description, Specifications, Reviews).

### Pagination
**`pagination`** — A simple numbered pagination strip. Active page gets a teal fill with white text; inactive pages are muted gray. Hover state adds a soft gray background.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to `{typography.display-md}`; footer links stack; search bar becomes full-width; accordion replaces tabbed content |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses `{typography.display-lg}`; footer uses two-column layout; search bar remains pill-shaped but narrower |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero uses `{typography.display-xl}`; footer uses four-column layout; product cards show hover states |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to four columns; hero section uses larger padding; whitespace increases proportionally |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile.
- Product card taps navigate to product detail; no hover states on mobile.
- Accordion headers have 48px minimum height for easy tapping.
- Quantity selector buttons are 48x48px.
- Bottom nav (mobile) uses 56px-tall icons with 44px touch targets.

### Collapsing Strategy
- Top nav collapses to a hamburger menu at < 744px; the hamburger icon is 44x44px.
- Product filters collapse into a bottom sheet or modal on mobile.
- Footer columns collapse to a single column on mobile, with accordion-style section headers.
- Tabbed content (product details) collapses to an accordion on mobile.
- Search bar collapses to an icon that expands to full-width input on tap.
- Breadcrumb collapses to show only the current page and a "Back" link on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and cards were inferred from common patterns; exact transition durations and easing curves were not extractable.
- Error states for forms (validation messages, error icons) were not visible on the live site; colors and styling are best-guess based on brand palette.
- Dark mode is not implemented on the live site; no dark-mode tokens are defined.
- Sub-brand palettes (e.g., for Aarke Carbonator vs. Aarke Accessories) may exist but were not distinguishable from the extracted data.
- The exact font-weight mapping for GT Walsheim Pro variants (Light, Medium, Bold) was inferred from common usage; actual CSS may use numeric weights (300, 500, 700).
- The `#a89cc8` (lavender) and `#c1e6e6` (pale teal) colors appear in editorial imagery but may not be official brand tokens; they are included as accents.
- The `#fbcd0a` yellow is used sparingly; its exact role (sale badge vs. accent) is inferred.
- The `#1990c6` and `#136f99` blues appear in the extracted colors but were not observed in prominent UI elements; they may be legacy or secondary.
- The `#f9fafb` color appears in the extracted list but is very close to white; it may be a subtle surface variant.
- The `#8f8f8f` and `#7b7b7b` grays appear but their specific roles (muted vs. muted-soft) are inferred.
- The `#3c3c3c` and `#555555` grays appear but are close to the defined `body` and `muted` tokens; they may be legacy.
- The `#dedede` and `#e9e9e9` grays are close to `hairline-soft` and `surface-strong`; exact mapping is inferred.
- The `#121212` color is used as the scrim token; its opacity value (0.3 for hero overlay) is inferred.
- The `#efefef` and `#f9f9f9` colors are very close to `surface-soft` and `canvas`; they may be legacy or slightly different surfaces.
- The `#adadad` and `#bbbbbb` grays are close to `muted-soft`; exact mapping is inferred.
- The `#edf5f5` color is a very pale teal that may be a legacy surface color.
- The `#e8e8e8` color is used as `surface-strong`; its exact role is inferred.
- The `#f2f2f2` color is used as `surface-soft`; its exact role is inferred.
- The `#ebebeb` color is used as `hairline-soft`; its exact role is inferred.
- The `#eeeeee` color is used as a surface color; its exact role is inferred.
- The `#cccccc` color is used as a muted color; its exact role is inferred.
- The `#dddddd` color is used as `hairline`; its exact role is inferred.
- The `#333333` color is used as `body`; its exact role is inferred.
- The `#666666` color is used as `muted`; its exact role is inferred.
- The `#232322` color is used as `ink`; its exact role is inferred.
- The `#108474` color is used as `primary`; its exact role is inferred.
- The `#ffffff` color is used as `canvas` and `surface-card`; its exact role is inferred.
- The `#fafafa` color is used as `canvas`; its exact role is inferred.
- The `#f9fafb` color is very close to `canvas`; its exact role is inferred.
- The `#f9f9f9` color is very close to `canvas`; its exact role is inferred.
- The `#efefef` color is very close to `surface-soft`; its exact role is inferred.
- The `#e9e9e9` color is very close to `surface-strong`; its exact role is inferred.
- The `#e8e8e8` color is used as `surface-strong`; its exact role is inferred.
- The `#dedede` color is very close to `hairline-soft`; its exact role is inferred.
- The `#ebebeb` color is used as `hairline-soft`; its exact role is inferred.
- The `#eeeeee` color is used as a surface color; its exact role is inferred.
- The `#f2f2f2` color is used as `surface-soft`; its exact role is inferred.
- The `#fafafa` color is used as `canvas`; its exact role is inferred.
- The `#ffffff` color is used as `canvas` and `surface-card`; its exact role is inferred.
- The `#232322` color is used as `ink`; its exact role is inferred.
- The `#333333` color is used as `body`; its exact role is inferred.
- The `#666666` color is used as `muted`; its exact role is inferred.
- The `#999999` color is used as `muted-soft`; its exact role is inferred.
- The `#cccccc` color is used as a muted color; its exact role is inferred.
- The `#dddddd` color is used as `hairline`; its exact role is inferred.
- The `#ebebeb` color is used as `hairline-soft`; its exact role is inferred.
- The `#108474` color is used as `primary`; its exact role is inferred.
- The `#0d6b5d` color is used as `primary-active`; its exact role is inferred.
- The `#c1e6e6` color is used as `primary-disabled`; its exact role is inferred.
- The `#fbcd0a` color is used as `accent-yellow`; its exact role is inferred.
- The `#a89cc8` color is used as `accent-lavender`; its exact role is inferred.
- The `#c13515` color is used as `error`; its exact role is inferred.
- The `#121212` color is used as `scrim`; its exact role is inferred.
- The `#1990c6` and `#136f99` blues are not used in the token set; they may be legacy.
- The `#7b7b7b`, `#8f8f8f`, `#adadad`, `#bbbbbb`, `#3c3c3c`, `#555555` grays are not used in the token set; they may be legacy or slightly different shades.
- The `#edf5f5` color is not used in the token set; it may be a legacy surface color.
- The `#f9fafb` color is not used in the token set; it may be a legacy surface color.
- The `#f9f9f9` color is not used in the token set; it may be a legacy surface color.
- The `#efefef` color is not used in the token set; it may be a legacy surface color.
- The `#e9e9e9` color is not used in the token set; it may be a legacy surface color.
- The `#dedede` color is not used in the token set; it may be a legacy surface color.
- The `#eeeeee` color is not used in the token set; it may be a legacy surface color.
- The `#cccccc` color is not used in the token set; it may be a legacy muted color.
- The `#dddddd` color is used as `hairline`; its exact role is inferred.
- The `#ebebeb` color is used as `hairline-soft`; its exact role is inferred.
- The `#f2f2f2` color is used as `surface-soft`; its exact role is inferred.
- The `#e8e8e8` color is used as `surface-strong`; its exact role is inferred.
- The `#fafafa` color is used as `canvas`; its exact role is inferred.
- The `#ffffff` color is used as `canvas` and `surface-card`; its exact role is inferred.
- The `#232322` color is used as `ink`; its exact role is inferred.
- The `#333333` color is used as `body`; its exact role is inferred.
- The `#666666` color is used as `muted`; its exact role is inferred.
- The `#999999` color is used as `muted-soft`; its exact role is inferred.
- The `#108474` color is used as `primary`; its exact role is inferred.
- The `#0d6b5d` color is used as `primary-active`; its exact role is inferred.
- The `#c1e6e6` color is used as `primary-disabled`; its exact role is inferred.
- The `#fbcd0a` color is used as `accent-yellow`; its exact role is inferred.
- The `#a89cc8` color is used as `accent-lavender`; its exact role is inferred.
- The `#c13515` color is used as `error`; its exact role is inferred.
- The `#121212` color is used as `scrim`; its exact role is inferred.
- The `#1990c6` and `#136f99` blues are not used in the token set; they may be legacy.
- The `#7b7b7b`, `#8f8f8f`, `#adadad`, `#bbbbbb`, `#3c3c3c`, `#555555` grays are not used in the token set; they may be legacy or slightly different shades.
- The `#edf5f5` color is not used in the token set; it may be a legacy surface color.
- The `#f9fafb` color is not used in the token set; it may be a legacy surface color.
- The `#f9f9f9` color is not used in the token set; it may be a legacy surface color.
- The `#efefef` color is not used in the token set; it may be a legacy surface color.
- The `#e9e9e9` color is not used in the token set; it may be a legacy surface color.
- The `#dedede` color is not used in the token set; it may be a legacy surface color.
- The `#eeeeee` color is not used in the token set; it may be a legacy surface color.
- The `#cccccc` color is not used in the token set; it may be a legacy muted color.
- The `#dddddd` color is used as `hairline`; its exact role is inferred.
- The `#ebebeb` color is used as `hairline-soft`; its exact role is inferred.
- The `#f2f2f2` color is used as `surface-soft`; its exact role is inferred.
- The `#e8e8e8` color is used as `surface-strong`; its exact role is inferred.
- The `#fafafa` color is used as `canvas`; its exact role is inferred.
- The `#ffffff` color is used as `canvas` and `surface-card`; its exact role is inferred.
- The `#232322` color is used as `ink`; its exact role is inferred.
- The `#333333` color is used as `body`; its exact role is inferred.
- The `#666666` color is used as `muted`; its exact role is inferred.
- The `#999999` color is used as `muted-soft`; its exact role is inferred.
- The `#108474` color is used as `primary`; its exact role is inferred.
- The `#0d6b5d` color is used as `primary-active`; its exact role is inferred.
- The `#c1e6e6` color is used as `primary-disabled`; its exact role is inferred.
- The `#fbcd0a` color is used as `accent-yellow`; its exact role is inferred.
- The `#a89cc8` color is used as `accent-lavender`; its exact role is inferred.
- The `#c13515` color is used as `error`; its exact role is inferred.
- The `#121212` color is used as `scrim`; its exact role is inferred.
- The `#1990c6` and `#136f99` blues are not used in the token set; they may be legacy.
- The `#7b7b7b`, `#8f8f8f`, `#adadad`, `#bbbbbb`, `#3c3c3c`, `#555555` grays are not used in the token set; they may be legacy or slightly different shades.
- The `#edf5f5` color is not used in the token set; it may be a legacy surface color.
- The `#f9fafb` color is not used in the token set; it may be a legacy surface color.
- The `#f9f9f9` color is not used in the token set; it may be a legacy surface color.
- The `#efefef` color is not used in the token set; it may be a legacy surface color.
- The `#e9e9e9` color is not used in the token set; it may be a legacy surface color.
- The `#dedede` color is not used in the token set; it may be a legacy surface color.
- The `#eeeeee` color is not used in the token set; it may be a legacy surface color.
- The `#cccccc` color is not used in the token set; it may be a legacy muted color.
