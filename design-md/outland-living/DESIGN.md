---
version: alpha
name: "Outland Living"
source_url: "https://outlandliving.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep navy (#2f4a7e) anchors every hero banner and call-to-action on a site built around the primal draw of an open flame on a back deck — a color family that runs from the darkest watch-dial blue (#1d2d5f) through the mid-tone steel of secondary UI (#3e5875) to the quiet haze of muted badge text (#98a7ba). The palette reads like dusk settling over a patio: near-black ink (#000a12) for headlines, cool grays (#444444, #9b9b9b) for body and caption copy, and a generous spread of soft neutrals (#f3f4f4, #f9fafb, #f6f6f6) that keep product photography — always fire pits glowing amber against evening skies — the loudest element on every viewport. A sharp yellow (#ffff00) appears sparingly for promotional callouts and sale badges, the only warm spike in an otherwise cool-temperature system. Typography pairs Gotham for display, navigation, and button labels with Source Sans Pro for body paragraphs and fine print — Gotham's geometric lowercase and squared counters lend industrial authority at 32–40px display sizes, while Source Sans Pro's open apertures maintain comfortable reading at 14–16px on product descriptions and FAQ accordions. Corner radii stay modest: product cards and image containers use `{rounded.sm}` (8px), buttons sit at `{rounded.xs}` (4px) for a squared-off, hardware-catalog feel, and only avatar circles and tag pills reach `{rounded.full}`. Spacing is utilitarian — `{spacing.lg}` (24px) between card grid items, `{spacing.section}` (64px) between page zones — letting the photography breathe without decorative filler. The star-rating glyphs rendered by JudgemeStar sit inline with review counts in `{typography.caption}`, tying social proof tightly to the product card without extra visual weight. Navigation is a single sticky bar at 64px height, collapsing to a hamburger drawer on mobile, with the Outland Living wordmark left-aligned in Gotham Medium and cart/account icons right-aligned in the same navy primary.

colors:
  primary: "#2f4a7e"
  primary-dark: "#263f6f"
  primary-deeper: "#1d2d5f"
  primary-active: "#344a7a"
  primary-disabled: "#8897aa"
  accent-sky: "#8bb4ca"
  accent-highlight: "#ffff00"
  ink: "#000a12"
  body: "#444444"
  body-alt: "#4a4a4a"
  muted: "#9b9b9b"
  muted-blue: "#98a7ba"
  muted-slate: "#99a7b9"
  hairline: "#dedede"
  hairline-soft: "#e4e4e4"
  border-mid: "#bbbbbb"
  border-light: "#d6d6d6"
  border-cool: "#d2d8e0"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-warm: "#f6f6f6"
  surface-card: "#ffffff"
  surface-muted: "#f3f4f4"
  surface-gray: "#eeeeee"
  slate-mid: "#3e5875"
  gray-mid: "#979797"
  near-black: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000a12"

typography:
  display-xl:
    fontFamily: "'Gotham Medium', 'Gotham Book', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0
  title-lg:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham Book', 'Gotham Medium', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Source Sans Pro', Roboto, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Sans Pro', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  body-semibold:
    fontFamily: "'Source Sans Pro Semibold', 'Source Sans Pro', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Source Sans Pro Bold', 'Source Sans Pro', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  overline:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  price-lg:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "'Gotham Medium', 'Gotham Book', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  star-rating:
    fontFamily: "JudgemeStar, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px

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
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary-active}
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
    width: 100%
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.border-mid}
    focusBorder: 1px solid {colors.primary}
  text-input-label:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.border-mid}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    position: sticky
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 2px 8px rgba(0,10,18,0.08)
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    boxShadow: 0 8px 24px rgba(0,10,18,0.12)
  mobile-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    width: 300px
    padding: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 520px
    padding: "{spacing.section} {spacing.lg}"
    overlay: linear-gradient(rgba(0,10,18,0.35), rgba(0,10,18,0.55))
  hero-subtitle:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-dark}"
    maxWidth: 560px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 36px
    height: 52px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.border-mid}
    transition: box-shadow 0.2s ease, border-color 0.2s ease
    hoverShadow: 0 4px 16px rgba(0,10,18,0.08)
  product-card-image:
    backgroundColor: "{colors.surface-muted}"
    rounded: "{rounded.sm} {rounded.sm} {rounded.none} {rounded.none}"
    aspectRatio: 1 / 1
    objectFit: cover
  product-card-body:
    padding: "{spacing.md} {spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.primary}"
  product-card-rating:
    typography: "{typography.star-rating}"
    textColor: "{colors.accent-highlight}"
  sale-badge:
    backgroundColor: "{colors.accent-highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  review-stars:
    typography: "{typography.star-rating}"
    textColor: "{colors.accent-highlight}"
  review-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  review-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
  review-author:
    typography: "{typography.caption-bold}"
    textColor: "{colors.ink}"
  feature-grid:
    backgroundColor: "{colors.surface-muted}"
    padding: "{spacing.section} {spacing.lg}"
  feature-icon-circle:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 56px
    width: 56px
  feature-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  feature-description:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
  spec-table-header:
    backgroundColor: "{colors.surface-gray}"
    typography: "{typography.caption-bold}"
    textColor: "{colors.ink}"
    padding: "{spacing.md} {spacing.base}"
  spec-table-row:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline-soft}
  accordion-faq:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: 1px solid {colors.hairline}
  accordion-faq-body:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
  comparison-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} {spacing.base}"
  comparison-cell:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline-soft}
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: "/"
  breadcrumb-active:
    typography: "{typography.caption-bold}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-heading:
    typography: "{typography.overline}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.md}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-blue}"
    hoverColor: "{colors.on-dark}"
  footer-bottom:
    typography: "{typography.caption}"
    textColor: "{colors.muted-slate}"
    borderTop: 1px solid rgba(255,255,255,0.12)
    padding: "{spacing.lg} 0"
  newsletter-input:
    backgroundColor: rgba(255,255,255,0.1)
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid rgba(255,255,255,0.2)
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    border: 1px solid {colors.border-mid}
  image-gallery:
    rounded: "{rounded.sm}"
    gap: "{spacing.sm}"
  image-gallery-thumb:
    rounded: "{rounded.xs}"
    border: 2px solid transparent
    activeBorder: 2px solid {colors.primary}
    height: 72px
    width: 72px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 40px
    textAlign: center
  search-overlay:
    backgroundColor: "rgba(0,10,18,0.5)"
  search-modal:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    boxShadow: 0 16px 48px rgba(0,10,18,0.2)
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px 12px 44px
    height: 48px
    border: none

---

## Components

### Buttons

**`button-primary`** — Navy fill (#2f4a7e) with white text in Gotham Medium 16px, squared at `{rounded.xs}` (4px). On hover the background shifts to `{colors.primary-active}` (#344a7a) with a subtle 0.15s transition. Disabled state uses `{colors.primary-disabled}` (#8897aa) at reduced opacity. All primary buttons carry 0.3px letter-spacing for optical stability at the 14–16px range.

**`button-secondary`** — White fill with a 2px navy border and navy text. Hover fills `{colors.surface-soft}` and darkens the border to `{colors.primary-active}`. Used for secondary actions on product pages (e.g., "View Specs," "Compare Models") where the primary CTA is already present.

**`button-add-to-cart`** — Full-width variant of the primary button at 52px height, slightly taller than the standard 48px to emphasize purchase intent. Lives below the quantity selector on product detail pages.

**`button-small`** — Compact 36px-height button in `{typography.button-sm}` (12px) used inside product cards for quick-add actions and inside comparison tables for model selection.

### Navigation

**`nav-bar`** — 64px sticky header with a white background and a 1px `{colors.hairline}` bottom border that transitions to a soft box-shadow on scroll. Logo sits left in Gotham Medium, primary nav links center-aligned using `{typography.nav-link}`, and cart/account icons pin right. Dropdown menus (`nav-dropdown`) appear with `{rounded.sm}` corners and a 24px shadow depth.

**`mobile-drawer`** — A 300px slide-in drawer from the left, triggered by a hamburger icon on viewports below 744px. Nav items are stacked vertically in `{typography.title-md}` with `{spacing.base}` gaps, and nested subcategories indent with `{spacing.lg}`.

**`announcement-bar`** — Full-width navy strip above the nav at 40px height, centered caption-bold text in white. Used for shipping promotions, seasonal sales, and warranty messaging. Dismissible via a close icon on the right edge.

### Hero

**`hero-banner`** — Full-bleed lifestyle photography (fire pits lit at dusk) behind a dark gradient overlay, minimum 520px tall. Display-xl headline in white, body-lg subtitle capped at 560px width, and a single hero-cta button. The overlay gradient runs from 35% to 55% opacity to ensure text legibility regardless of the underlying photo brightness.

### Product Cards

**`product-card`** — White card with a 1px `{colors.hairline-soft}` border, `{rounded.sm}` corners, and no padding around the image container (image bleeds to card edges under top-radius clipping). On hover, the border darkens to `{colors.border-mid}` and a subtle 4px shadow appears. The card body holds the title in `{typography.title-sm}`, price in `{typography.price-md}` colored navy, and a star-rating row rendered with JudgemeStar glyphs in yellow (#ffff00) followed by a muted review count.

**`sale-badge`** — Bright yellow (#ffff00) pill positioned absolutely over the product-card image top-left corner with 4px corners, uppercase overline text in ink. Used sparingly for clearance or seasonal promotions.

**`category-badge`** — Navy-filled variant of the badge used on collection pages to distinguish product lines (e.g., "PROPANE," "NATURAL GAS").

### Reviews

**`review-card`** — Light `{colors.surface-soft}` background with `{rounded.sm}` corners and a hairline-soft border. Yellow star row at top, author name in caption-bold, review body in body-md. Cards stack vertically on mobile and arrange in a 2-column masonry on desktop.

### Product Details

**`spec-table`** — Alternating-row specification table with a gray header row (`{colors.surface-gray}`) and hairline-soft row separators. Caption-bold headers, body-sm values. Used to display BTU output, dimensions, fuel type, ignition method, and weight for each fire pit model.

**`accordion-faq`** — Borderless accordion with a bottom hairline separator. Title-sm triggers with a rotatable chevron; body content fades in with a 0.2s ease transition. Commonly holds FAQ items, safety information, and warranty details.

**`comparison-table`** — Side-by-side model comparison with a navy header row bearing white title-md text. Body cells in body-sm with hairline-soft bottom borders. Horizontally scrollable on mobile viewports with a sticky first column for feature labels.

**`quantity-selector`** — Inline minus/plus stepper with a centered numeric input, 44px tall, bordered in `{colors.border-mid}`. Buttons are 44x44px touch targets.

**`image-gallery`** — Main product image at 1:1 aspect ratio with `{rounded.sm}` corners, a row of 72x72px thumbnails below with `{rounded.xs}` corners. Active thumbnail gains a 2px navy border.

### Feature Grid

**`feature-grid`** — Section with `{colors.surface-muted}` background, typically 3-column on desktop, 1-column on mobile. Each cell contains a 56px navy circle icon, a title-md heading, and a body-sm description. Used to highlight key product benefits (CSA certified, auto-ignition, wind guard included).

### Footer

**`footer`** — Near-black (#121212) background with four-column layout on desktop. Column headings in overline uppercase white, link lists in body-sm `{colors.muted-blue}` that brighten to white on hover. Bottom bar separated by a subtle white-12% opacity border, holding copyright in caption and `{colors.muted-slate}`.

**`newsletter-input`** — Semi-transparent white input field inside the footer with a matching navy submit button. Sits within a "Stay Connected" section alongside social media icon links.

### Search

**`search-overlay`** — Full-viewport scrim at 50% opacity over `{colors.scrim}`. The `search-modal` is a centered white card with `{rounded.sm}` corners, containing a search input with a magnifying-glass icon inset left. Results appear below the input as a live-updating list of product-card-like rows.

### Breadcrumb

**`breadcrumb`** — Slash-separated path rendered in `{typography.caption}` muted gray, with the final segment in caption-bold ink. Sits below the nav-bar on collection and product pages with `{spacing.base}` vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger + mobile drawer. Hero height drops to 380px with display-lg instead of display-xl. Product grid switches to 2-column with reduced card padding. Comparison table scrolls horizontally with sticky first column. Footer stacks to single-column accordion sections. |
| Tablet | 744–1128px | Product grid moves to 2–3 columns. Hero holds at 460px. Nav remains horizontal but hides tertiary links behind a "More" dropdown. Feature grid becomes 2-column. Spec table shows full width without horizontal scroll. |
| Desktop | 1128–1440px | Full 3–4 column product grid. Sticky nav at 64px. Hero at 520px with full display-xl headline. Side-by-side image gallery + product info on PDP. Footer renders 4 columns. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Side gutters grow with `{spacing.section-lg}`. Product grid may expand to 4 columns. Hero image scales proportionally. |

### Touch Targets

- All interactive elements maintain a minimum 44x44px tap target on mobile viewports.
- Quantity selector buttons are explicitly sized at 44x44px.
- Navigation links in the mobile drawer have `{spacing.base}` vertical padding ensuring 48px row height.
- Product card tap area covers the entire card surface, not just the title text.
- Close/dismiss icons on modals and announcement bar use 44x44px hit zones regardless of visual icon size.

### Collapsing Strategy

- Navigation collapses to a hamburger icon + left-sliding drawer at the mobile breakpoint (< 744px).
- Footer columns collapse into expandable accordion sections on mobile, with overline headings as triggers.
- Product comparison table maintains all columns but enables horizontal scroll with a sticky feature-label column on viewports below 1128px.
- Feature grid drops from 3 columns to 2 at tablet, then 1 on mobile, maintaining consistent icon-circle sizing.
- Image gallery thumbnails shift from a horizontal row to a scrollable filmstrip on mobile.
- Spec tables remain full-width but gain horizontal scroll on mobile rather than stacking rows.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No CSS custom-property tokens or Shopify theme variables were extractable from the static page load; color values are inferred from computed styles.
- Gotham web-font weights beyond Book (400) and Medium (500) could not be confirmed — Bold (700) may exist in the actual font files but was not observed in extracted stacks.
- Exact border-radius values on the live site may differ by 1–2px from the token-mapped values here; the site likely uses pixel values rather than a formal token scale.
- Animation/transition durations and easing curves are estimated (0.15s–0.2s ease) — no explicit motion tokens were extracted.
- The yellow (#ffff00) accent was observed in limited contexts and may be a review-star color rather than a deliberate brand accent; its use in sale badges is inferred from common Shopify patterns.
- JudgemeStar font is a third-party review-widget font; its exact glyph mapping and size may be controlled by the Judge.me app rather than brand-level CSS.
- Dark-mode or alternate theme support was not detected.
- Exact max-width container values and grid column counts could not be confirmed from static extraction.
