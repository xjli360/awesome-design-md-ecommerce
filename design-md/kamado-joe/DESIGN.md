---
version: alpha
name: "Kamado Joe"
source_url: "https://www.kamadojoe.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  That unmistakable ember-red (#e2231a) hits before any headline loads — the same glaze color fired onto the ceramic dome of every Classic and Big Joe, now pulled into every CTA, price badge, and hover state on the site. The digital palette mirrors the physical product line: charcoal steel (#343738) for nav bars and footer slabs, a near-black ink (#231f20) for body copy that reads heavy and confident against generous white canvas, and a cool light gray (#dedede) used sparingly for dividers and disabled states. There is no pastel softness here; the color system runs on two voltages — the searing red and the carbonized darks — with white space acting as the only pressure release. Typography lands in a system sans-serif stack at workmanlike weights; display headings run 600–700 at 36–48px, trusting product photography (wide-angle hero shots of glowing charcoal and smoke rings) to carry the emotional load rather than decorative type. Corners stay tight — buttons and cards use `{rounded.xs}` to `{rounded.sm}`, rarely softer, channeling the machined-metal precision of the air-control dials and cast-iron hardware. Product cards sit on `{colors.surface-card}` with a subtle 1px `{colors.hairline}` border, stacking vertically on mobile with full-bleed imagery. The nav bar runs a solid `{colors.charcoal}` background with white logotype and link text, anchoring every page to that dark-on-light inversion that separates Kamado Joe from the sea of white-header e-commerce. Section spacing is generous (`{spacing.section}` at 64px+), letting each content block — configurator, comparison table, recipe carousel — breathe like a standalone billboard on the scroll.

colors:
  primary: "#e2231a"
  primary-active: "#c91d16"
  primary-disabled: "#f4a8a4"
  charcoal: "#343738"
  ink: "#231f20"
  body: "#343738"
  muted: "#6b6d6f"
  hairline: "#dedede"
  hairline-soft: "#ececec"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-smoke: "#4a4a4a"
  badge-sale: "#e2231a"
  footer-bg: "#231f20"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  uppercase-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 2px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.ink}
  text-input-error:
    border: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.xl}
  nav-bar-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    boxShadow: 0 4px 16px rgba(0,0,0,0.12)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    padding: 0
    imageAspectRatio: 1:1
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.price}"
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 560px
    padding: "{spacing.section-lg} {spacing.xl}"
    contentMaxWidth: 1440px
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-dark}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
    height: 52px
  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    cellPadding: "{spacing.base} {spacing.lg}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.uppercase-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
  configurator-option:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.hairline}
    selectedBorder: 2px solid {colors.primary}
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: 1px solid {colors.hairline}
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.uppercase-label}"
    textColor: "{colors.on-dark}"
  recipe-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    imageAspectRatio: 16:9
  recipe-card-title:
    typography: "{typography.title-md}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"

---

## Components

### Buttons

**`button-primary`** — Solid Kamado Joe red (#e2231a) fill with white text at weight 600, tight 4px radius. On hover, darkens to `{colors.primary-active}` (#c91d16) with no transform or shadow — the color shift alone signals interactivity. Disabled state fades to a washed salmon `{colors.primary-disabled}`. Used for Add to Cart, Shop Now, and configurator confirmation actions.

**`button-secondary`** — White fill with a 2px solid `{colors.ink}` border and dark text. On hover, inverts fully to dark fill with white text, creating a bold toggle effect. Used for secondary actions like "Compare Models", "View Details", and filter toggles.

**`button-dark`** — Charcoal (#343738) fill with white text, same tight radius. Appears in hero overlays and dark-background sections where the primary red would clash with photography. Hover lightens slightly to differentiate from static state.

### Navigation

**`nav-bar`** — A 64px-tall solid charcoal bar spanning full viewport width. The Kamado Joe wordmark sits left in white; navigation links are set in `{typography.nav-link}` (14px, weight 500, white). Dropdowns emerge as white panels with `{rounded.xs}` corners and a soft box-shadow, containing category links and promotional imagery. Mobile collapses to a hamburger icon with a full-screen slide-out drawer on `{colors.charcoal}` background.

**`announcement-bar`** — A 40px red banner above the nav bar for promotions and free-shipping messaging. White text in `{typography.caption}`, centered. Dismissible via an X icon on the right edge.

### Product Cards

**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.sm}` corners. Product image fills the top at 1:1 aspect ratio with no internal padding. Below the image: product title in `{typography.title-sm}`, price in `{typography.price}` (bold, 20px), and a red "Sale" badge when discounted. On hover, a subtle 0 2px 8px shadow lifts the card without any scale transform.

### Hero Section

**`hero-section`** — Full-width dark background (either `{colors.surface-dark}` solid or a high-contrast lifestyle photograph with a dark gradient overlay). Minimum height 560px. Headline in `{typography.display-xl}` (white, 48px, bold) with subhead in `{typography.body-lg}`. CTA button uses a slightly larger variant (52px height, 40px horizontal padding) of `button-primary`. Content is left-aligned on desktop, centered on mobile.

### Configurator

**`configurator-panel`** — The grill configurator uses a light gray panel (`{colors.surface-soft}`) with individual option tiles (`configurator-option`) that show a 2px red border when selected. Options display color swatches, size labels, or accessory thumbnails. The panel groups options by category (Size, Color, Stand Type) with `{typography.title-md}` section headers.

### Comparison Table

**`comparison-table`** — A structured grid for comparing grill models (Classic I vs II vs III, Big Joe). Header row uses `{colors.surface-soft}` background. Cells are separated by `{colors.hairline}` borders. Feature rows alternate checkmarks and specs in `{typography.body-sm}`. Table scrolls horizontally on mobile with sticky first column.

### Recipe Cards

**`recipe-card`** — 16:9 aspect-ratio hero image on top (smoke-filled food photography), title in `{typography.title-md}` below, with cook-time and difficulty metadata in `{typography.caption}`. Cards appear in a horizontal carousel on desktop, vertical stack on mobile.

### Footer

**`footer`** — Deep near-black (#231f20) background with white text. Column headings in `{typography.uppercase-label}` (11px, 700 weight, 1.2px letter-spacing). Link lists in `{typography.body-sm}`. Social icons at 24px, newsletter signup input + red CTA button inline. Bottom row contains legal links and copyright in `{typography.caption}`.

### Badges

**`badge-sale`** — Small red pill with white uppercase text ("SALE", "NEW LOW PRICE"). Positioned absolutely over the top-left corner of product card images with 8px offset from edges.

**`badge-new`** — Same dimensions but in charcoal fill, used for new product launches and accessories.

### Search

**`search-bar`** — 44px-tall input with `{rounded.xs}` and 1px gray border. Placeholder text in `{colors.muted}`. On focus, border transitions to `{colors.ink}`. Search icon sits inline-left. Results dropdown appears below with product thumbnails, titles, and prices in a white panel.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger + slide drawer. Hero headline drops to 28px (`{typography.display-md}`). Product cards stack vertically full-width. Configurator options become a scrollable horizontal strip. Comparison table scrolls horizontally with sticky model-name column. Footer stacks into accordion sections. |
| Tablet | 744–1128px | Two-column product grid. Nav links remain visible but compress spacing. Hero height reduces to 440px. Configurator panel sits below product image rather than beside it. Recipe cards show 2-up in carousel. |
| Desktop | 1128–1440px | Three-column product grid. Configurator sits side-by-side with product imagery (60/40 split). Full nav with dropdowns. Hero at full 560px+ height. Comparison table shows all columns without scroll. |
| Wide | > 1440px | Content max-width caps at 1440px, centered. Outer margins fill with `{colors.canvas}`. Product grid may expand to 4 columns on collection pages. Hero image scales to cover with fixed content width. |

### Touch Targets

- All interactive elements maintain minimum 44×44px tap area on mobile
- Product card entire surface is tappable, not just the title link
- Nav drawer links have 48px row height with full-width tap zones
- Configurator option tiles are minimum 56px tall for comfortable selection
- Close/dismiss icons (announcement bar, modals) use 44px invisible hit area around 16px visible icon

### Collapsing Strategy

- Navigation: full link bar → hamburger + slide-out drawer at <744px
- Product grid: 4-col → 3-col → 2-col → 1-col as viewport narrows
- Comparison table: fixed layout → horizontal scroll with sticky first column
- Footer: multi-column → stacked accordion with expand/collapse per section
- Configurator: side panel → below-image stacked panel → horizontal option strip
- Hero CTA: maintains full width on mobile, never shrinks below 48px height
- Announcement bar: text truncates with ellipsis on narrow viewports, maintains single-line height

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font families could not be reliably extracted (site returns `inherit` for all font-family stacks — likely loaded via JavaScript or a Shopify theme font loader). System sans-serif stack used as fallback; the actual brand typeface may differ.
- Only 5 hex colors were extractable from static HTML. Additional surface colors, gradient stops, and interactive-state colors are inferred from the extracted palette rather than directly observed.
- Icon system (style, size grid, stroke weight) could not be determined from extraction.
- Exact box-shadow values, transition durations, and easing curves are not available from static analysis.
- Product image treatment (zoom behavior, lazy-load placeholder color) not captured.
- Klaviyo/email-signup modal styling not observed in static extraction.
- Mobile drawer animation (slide direction, duration, overlay opacity) is JS-driven and unextractable.
