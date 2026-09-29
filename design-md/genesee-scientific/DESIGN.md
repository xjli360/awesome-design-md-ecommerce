---
version: alpha
name: "Genesee Scientific"
source_url: "https://www.geneseesci.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The lime jolt of #78be20 sits where most lab-supply brands would reach for a cautious navy or a clinical white — Genesee Scientific deploys it on primary CTAs, stock-available badges, and callout highlights as a signal that science can move with urgency and still look sharp doing it. Against a deep aqua-teal (#016e9f) and a near-black carrying barely perceptible violet undertones (#110011), the palette reads less like a hospital anteroom and more like a researcher who color-codes every tube rack in the cabinet. The canvas is white, but the brand never settles into the default sterility of competitor catalogs; the lime accent creates hard visual hierarchy wherever it lands, routing attention to transactional moments without needing large type or aggressive layout.

  Typography was not extractable from the live site — likely loaded via JavaScript — so the spec falls back to a neutral system sans-serif appropriate for a B2B supplier whose audience is procurement managers, lab coordinators, and researchers who want to find a SKU and check pack size quickly rather than linger on art direction. Display sizes stay proportional to catalog density: large enough to separate category headers from product names, compact enough to accommodate long scientific nomenclature without wrapping awkwardly.

  The nav carries search prominently, sized up to 44px and given a lime submit button, because a catalog spanning chemicals, reagents, consumables, and capital equipment demands a search-first mental model over a marketing-first one. Product cards surface SKU codes in monospace, reinforcing catalog precision over lifestyle branding. Category tiles use the teal (#016e9f) as a surface tint to mark the browse layer as distinct from the transactional product surface.

  The {rounded.sm} radius on inputs and cards keeps geometry clean without the coldness of {rounded.none} — professional rather than austere. The design system's compression is deliberate: three extracted colors, a single sans-serif weight, and a grid calibrated for catalog density over photography. When a brand's most expressive move is a lime green "Add to Cart" button on a page of pipette tips and buffer solutions, that restraint is doing the work.

colors:
  primary: "#78be20"
  primary-active: "#5d9a10"
  primary-disabled: "#c4e491"
  secondary: "#016e9f"
  secondary-active: "#015580"
  secondary-disabled: "#80b7cf"
  ink: "#110011"
  body: "#2a2a35"
  muted: "#6b7280"
  hairline: "#e2e8f0"
  hairline-soft: "#f1f5f9"
  canvas: "#ffffff"
  surface-soft: "#f4f9ee"
  surface-teal: "#e8f4fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  on-dark: "#ffffff"
  danger: "#dc2626"
  warning: "#f59e0b"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.2px
  sku-label:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: "10px 20px"
    height: 40px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.secondary-active}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.secondary}"
    border: "1px solid {colors.secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "9px 19px"
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    focusBorderColor: "{colors.secondary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "10px 16px"
    height: 44px
    iconColor: "{colors.muted}"
    focusBorderColor: "{colors.secondary}"
    submitButtonBg: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
    submitButtonRounded: "{rounded.md}"
  nav-top-bar:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoAreaWidth: 200px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    skuColor: "{colors.muted}"
    skuTypography: "{typography.sku-label}"
    priceTypography: "{typography.price}"
    titleTypography: "{typography.title-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-sm}"
    ctaRounded: "{rounded.sm}"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-badge-sale:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-badge-in-stock:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.sm}"
    minHeight: 360px
    padding: "{spacing.xxl} {spacing.xl}"
  category-tile:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.secondary}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    hoverBackgroundColor: "{colors.secondary}"
    hoverTextColor: "{colors.on-secondary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  data-table:
    headerBackgroundColor: "{colors.secondary}"
    headerTextColor: "{colors.on-secondary}"
    headerTypography: "{typography.caption-bold}"
    rowBackgroundColor: "{colors.canvas}"
    rowAltBackgroundColor: "{colors.surface-soft}"
    rowTextColor: "{colors.body}"
    rowTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
  alert-info:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.secondary}"
    borderLeft: "3px solid {colors.secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  alert-success:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    borderLeft: "3px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  pagination:
    activeBackgroundColor: "{colors.secondary}"
    activeTextColor: "{colors.on-secondary}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    size: 32px
  rfq-form:
    backgroundColor: "{colors.surface-teal}"
    borderColor: "{colors.secondary}"
    border: "1px solid {colors.secondary}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    headingTypography: "{typography.display-sm}"
    headingColor: "{colors.secondary}"
    inputStyle: "{text-input}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
    submitRounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Lime green (#78be20) fill with white text, `{rounded.sm}`, 40px height. The brand's highest-energy action color, applied exclusively to Add to Cart, RFQ submission, and homepage CTAs. On interaction, background darkens to `{colors.primary-active}` (#5d9a10); disabled state washes out to `{colors.primary-disabled}` with muted text, communicating unavailability without hiding the affordance.

**`button-secondary`** — Teal (#016e9f) fill with white text, identical geometry to primary. Reserved for secondary catalog actions such as "Request Quote," account navigation, and applied filter confirmation. Active state deepens to `{colors.secondary-active}`; the two filled buttons should not appear side-by-side — use `button-outline` as the counterpart.

**`button-outline`** — Transparent background with a teal border and teal text. Used for lower-priority sibling actions alongside a filled button: "Save to List" next to "Add to Cart," or "Download SDS" beside a product CTA. The 1px border keeps weight consistent with `button-secondary` at a glance.

**`button-ghost`** — Text-only in `{colors.ink}`, no background or border. Used for inline "View Details" links inside data table rows, breadcrumb-adjacent actions, and modal dismissals.

### Inputs & Search

**`text-input`** — White canvas with hairline border, 40px height, `{rounded.sm}`. On focus, the border shifts to teal `{colors.secondary}` without a colored fill or shadow, keeping the surrounding form layout stable. Sized for RFQ forms, account fields, and product quantity entry.

**`search-bar`** — Slightly taller (44px) and more rounded (`{rounded.md}`) than standard inputs, visually differentiated so users recognise it as site-wide search, not a filter field. A lime green submit button is inset at the right edge, consistent with the primary action language. This component anchors the center of the main nav bar.

### Navigation

**`nav-top-bar`** — A 36px teal band at page top, white `{typography.caption}` type. Carries account login/register links, distributor contact, and utilitarian anchor links. Establishes the teal/green palette signal above the fold before the logo renders.

**`nav-bar`** — White, 64px tall, with a subtle hairline border at the bottom. Logo anchors left, search bar centers, account and cart icons sit right. Category dropdown triggers use `{typography.nav-link}` weight 500. The nav does not carry any lime green — that color is reserved for action surfaces below the nav.

### Product Display

**`product-card`** — White surface with hairline border and `{rounded.md}`. Image rendered at 4:3 aspect ratio. Below the image: product title in `{typography.title-md}`, then SKU code in `{typography.sku-label}` (monospace, muted) to signal catalog precision over marketing copy. Price appears in `{typography.price}` — large and heavy. "Add to Cart" button in lime green spans the card width at the bottom. Badge overlays (new, sale, in-stock) appear top-left on the image.

**`product-badge-new`** — Lime green pill with white uppercase text, `{rounded.xs}`. Overlays product image corners to signal recent additions to the catalog.

**`product-badge-sale`** — Red (`{colors.danger}`) version of the same badge shape. Same geometry, higher urgency signal for discounted lines.

**`product-badge-in-stock`** — Soft green surface with dark green text (`{colors.primary-active}`). Sits below price rather than on the image. Signals availability without competing with the lime CTA.

### Layout Sections

**`hero`** — Full-width teal section, white heading in `{typography.display-xl}`, body copy in `{typography.body-md}`, single lime CTA button. Used on the homepage and major category landings. Minimum height 360px to accommodate short text without looking cramped; never uses product photography as a hero background — the teal provides sufficient brand signal.

**`category-tile`** — Soft teal surface (`{colors.surface-teal}`) with teal text and a hairline border, `{rounded.md}`. Grid of 4–6 tiles on desktop for top-level browse (Plasticware, Chemicals, Equipment, etc.). On hover the tile fills to solid teal with white text, creating a direct visual echo of the nav-top-bar color.

**`rfq-form`** — A teal-tinted card with a solid teal left-accent border, used as a persistent sidebar widget or inline section on product pages. Heading in `{typography.display-sm}` teal. Inputs follow `text-input` spec. Submit in lime green — matches the Add to Cart language so procurement users recognise both paths as primary actions.

**`data-table`** — Teal header row, white text in `{typography.caption-bold}`. Rows alternate between white and `{colors.surface-soft}` for readability of dense specification data: dimensions, chemical compatibility codes, pack sizes, catalog numbers. Rounded at `{rounded.sm}` to avoid an overly clinical feel.

### Alerts & Feedback

**`alert-info`** — Soft teal background with a 3px teal left-border stripe. Used for shipping cutoff notices, lead time disclaimers, and regulatory compliance callouts. `{typography.body-sm}` keeps density manageable.

**`alert-success`** — Soft green background with a 3px lime left-border stripe. Confirms cart additions, RFQ submissions, and account updates. The green echo of the primary CTA color ties the confirmation state back to the action that triggered it.

**`breadcrumb`** — Muted caption text with hairline separator characters. Active (current) segment in `{colors.ink}`. Essential for navigating multi-tier category hierarchies (e.g., Plasticware → Tubes → Microcentrifuge Tubes).

**`pagination`** — 32px square buttons, hairline border, `{rounded.xs}`. Active page uses teal fill with white text. Appears on catalog listing pages with SKU counts that routinely run into hundreds of items per category.

**`footer`** — Deep `{colors.ink}` (#110011) background — the near-black with its violet undertone adds warmth that a pure #000000 would not. White text throughout. Links render in lime green (`{colors.primary}`), which achieves strong contrast against the dark ground. A 3px lime green `borderTop` visually seals the page before the dark field begins. Section headings in `{typography.title-sm}`, link lists in `{typography.body-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Search collapses to icon tap; product grid goes single-column; nav-top-bar hides secondary links; hamburger drawer opens category menu; all CTAs expand to full card width |
| Tablet | 744–1128px | 2-column product grid; search bar stays visible but narrower; nav category triggers collapse to overflow dropdown at fewer than 5 primary items |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with category megamenu on hover; side filter panel visible alongside product listing |
| Wide | > 1440px | Max-width container 1400px centered with auto margins; 4-column product grid; section padding increases to accommodate generous gutters |

### Touch Targets
- All buttons enforce 44px minimum height on mobile, overriding the 40px desktop default
- Nav icon buttons (account, cart, search) carry a 44×44px invisible tap area padding on touch devices
- Pagination items expand to 44px height on mobile
- Product card CTA spans full card width on mobile for reliable thumb access
- Category tile touch targets cover the full tile including padding zone

### Collapsing Strategy
- Category megamenu converts to an accordion drawer behind a hamburger at < 1024px; drawer slides in from the left
- Side filter panel on listing pages converts to a bottom-sheet modal on mobile, opened by a persistent "Filter" sticky button
- Data tables gain horizontal scroll on mobile with a fixed first column (SKU/name) — columns are not reflowed, as column alignment carries meaning for comparison shopping
- Breadcrumbs truncate to show only the immediate parent and current page on mobile, with an ellipsis tap to expand full path
- Nav-top-bar is hidden on mobile; account and cart icons are promoted into the main nav bar at the same 64px height

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No font families extracted**: The live site likely loads fonts via JavaScript (Adobe Fonts, Google Fonts, or a licensed custom face). All `fontFamily` values fall back to system sans-serif. Inspect the rendered page's computed styles to identify the actual typeface and update every `fontFamily` key in the typography block.
- **Sparse color extraction (3 colors only)**: Only #016e9f, #78be20, and #110011 were extracted. All neutral shades — `body`, `muted`, `hairline`, `surface-soft`, `surface-teal`, `surface-card` — are inferred from B2B catalog conventions, not measured values. Validate against rendered pages before implementing.
- **Primary/secondary color role is inferential**: #78be20 is assigned as primary (most distinctive) and #016e9f as secondary (most common for nav/backgrounds). The actual implementation may reverse this or treat them as equals. Confirm by inspecting CTA and nav background colors on the live site.
- **No meta theme-color set**: Mobile browser chrome color is undefined; actual rendered behavior depends on the live implementation's `<meta name="theme-color">` value, which may be the teal or white.
- **No dark-mode tokens defined**: Extraction provided no dark-palette signal; this spec covers light mode only.
- **Product photography treatment unknown**: Whether the catalog uses white-background studio shots, lifestyle photography, or a mix affects image container padding and card aspect-ratio decisions not resolvable from extraction alone.
- **Interactive state animations unspecified**: Hover transitions, focus ring styles, and loading skeleton colors are not extractable from static hints and should be verified against the live implementation.
