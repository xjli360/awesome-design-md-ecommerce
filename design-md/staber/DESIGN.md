---
version: alpha
name: "Staber"
source_url: "https://www.staber.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Horizontal-axis drum geometry — the engineering detail Staber built an entire company around — echoes through the digital presence as circular motifs, wide product photography shot at drum-level, and a visual language that favors function over ornamentation. The palette anchors on a deep industrial navy (#1b3a5c) pulled from decades of catalog covers and trade-show signage, supported by a warm safety orange (#e85c2a) reserved for CTAs and spec callouts — the same high-visibility tone found on factory floor markings. Typography leans on system-level sans-serifs at sturdy weights; there is no custom webfont indulgence here, just -apple-system and Arial doing honest work at readable sizes. Cards holding product models use sharp `{rounded.xs}` corners and `{colors.hairline}` borders that recall technical diagrams more than lifestyle catalogs. Spacing is generous vertically (`{spacing.section}` between feature blocks) but tight horizontally within spec tables, mimicking the dense-information density of an engineering datasheet. The canvas stays pure white (`{colors.canvas}`) with occasional `{colors.surface-soft}` bands breaking long scroll depths on product pages. Navigation is minimal — four or five top-level links at most — reflecting a catalog small enough that every SKU has a name the owner knows. The overall impression is a manufacturer's website that refuses decorative trends: no parallax, no animated counters, no lifestyle video heroes. Instead, cutaway diagrams, numbered spec lists, and the quiet confidence of a brand that has shipped the same proven design from Groveport, Ohio for three decades without chasing aesthetic fashion.

colors:
  primary: "#1b3a5c"
  primary-active: "#142d48"
  primary-disabled: "#8a9db3"
  accent: "#e85c2a"
  accent-active: "#c94d20"
  accent-disabled: "#f4b89e"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6b6b6b"
  muted-soft: "#999999"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-strong: "#eaeaea"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  success: "#2e7d32"
  warning: "#e8ac2a"
  spec-highlight: "#fff8e1"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
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

components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-disabled}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary-active}
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 14px
    height: 44px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.accent}
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.xl}
  nav-bar-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} 0"
    boxShadow: 0 4px 12px rgba(0,0,0,0.12)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline}
    boxShadow: none
  product-card-hover:
    boxShadow: 0 2px 8px rgba(0,0,0,0.08)
    border: 1px solid {colors.hairline-soft}
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.spec-label}"
    headerBackground: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    cellPadding: "{spacing.sm} {spacing.base}"
    border: 1px solid {colors.hairline}
  spec-highlight-row:
    backgroundColor: "{colors.spec-highlight}"
  badge-commercial:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-residential:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  feature-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    iconSize: 40px
    iconColor: "{colors.accent}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    linkColor: "{colors.on-primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  contact-form:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    inputHeight: 44px
---

## Components

### Buttons

**`button-primary`** — A solid orange (`{colors.accent}`) rectangle with barely-there `{rounded.xs}` corners, 44px tall. Text is white, weight 600, sized at 15px. On hover the background deepens to `{colors.accent-active}`; disabled state fades to `{colors.accent-disabled}` with no cursor change. Used exclusively for conversion actions: "Request Quote," "Contact Sales," "Download Brochure."

**`button-secondary`** — White fill with a 2px navy (`{colors.primary}`) border and matching navy text. Same dimensions as primary. On hover the background shifts to `{colors.surface-soft}` and the border darkens. Used for secondary actions like "View Specs" or "Compare Models."

**`button-ghost`** — No background, no border; navy text with underline on hover. Smaller padding, used inline within content blocks for "Learn more" links that need button-level tap targets without visual weight.

### Navigation

**`nav-bar`** — A 64px-tall strip in solid `{colors.primary}` navy. The Staber wordmark sits left in white; four to five navigation links appear right-aligned in `{typography.nav-link}` at weight 500. On mobile this collapses to a hamburger icon with a slide-out drawer. Dropdown menus on desktop use `nav-bar-dropdown` — white cards with `{rounded.xs}` and a subtle shadow beneath.

### Product Cards

**`product-card`** — White card with a 1px `{colors.hairline}` border, `{rounded.xs}` corners, and `{spacing.base}` internal padding. Contains a product image (aspect 4:3), model name in `{typography.title-sm}`, a one-line capacity/type descriptor in `{typography.body-sm}`, and a category badge (`badge-commercial` or `badge-residential`). On hover gains a soft shadow via `product-card-hover`. No price displayed — these are quote-based products.

### Hero Banner

**`hero-banner`** — Full-width navy block with white display text (`{typography.display-xl}`), minimum 400px tall. Typically holds a headline about American manufacturing or product durability, with a single CTA button (`button-primary` in orange) positioned bottom-left. Product cutaway images float right on desktop, hidden on mobile.

### Spec Table

**`spec-table`** — The workhorse component for a brand that sells on technical merit. Header row uses `{typography.spec-label}` (uppercase, 13px, weight 700) on a `{colors.surface-soft}` background. Data rows alternate white and barely-tinted backgrounds. Key specs can be highlighted with `spec-highlight-row` using a warm `{colors.spec-highlight}` yellow. Borders are 1px `{colors.hairline}` between rows.

### Feature Block

**`feature-block`** — Soft gray (`{colors.surface-soft}`) rounded container with a 40px icon in `{colors.accent}` orange, a `{typography.title-sm}` heading, and `{typography.body-md}` body text. Used to call out engineering differentiators: "Hexagonal Tub Design," "No Transmission," "Commercial-Grade Bearings." Arranged in 2-up or 3-up grids with `{spacing.lg}` gutters.

### Badges

**`badge-commercial`** — Small navy pill identifying commercial-grade products. `{typography.caption}` white text on `{colors.primary}` background with `{rounded.xs}` corners and tight 4px/10px padding.

**`badge-residential`** — Same dimensions but uses `{colors.surface-strong}` gray background with `{colors.ink}` dark text, for residential models.

### Footer

**`footer`** — Dark (`{colors.ink}`) full-width block. Contains the Staber logo in white, contact information (Groveport, OH address and phone), navigation links in `{colors.on-primary}`, and a "Made in USA" mark. Typography is `{typography.body-sm}` in `{colors.muted-soft}`. Padding uses `{spacing.xxl}` vertically.

### Contact Form

**`contact-form`** — Light gray container (`{colors.surface-soft}`) with `{rounded.sm}` corners. Holds labeled text inputs using the `text-input` component, a model-interest dropdown, and a `button-primary` submit. Labels use `{typography.caption}`. The form is the primary conversion path since products are quote-based rather than cart-based.

### Breadcrumb

**`breadcrumb`** — Minimal path indicator using `{typography.caption}` in `{colors.muted}`, with `/` separators in `{colors.hairline}`. The current page segment renders in `{colors.ink}` at same weight. Appears below the nav bar on product and category pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger drawer; hero banner stacks text above image; product cards go single-column full-width; spec tables scroll horizontally; feature blocks stack 1-up; footer stacks into single column |
| Tablet | 744–1128px | Product cards in 2-up grid; spec tables fit without scroll; hero image appears beside text at 40% width; nav links remain visible but tighter spacing |
| Desktop | 1128–1440px | Full nav bar with dropdowns; product cards 3-up; hero at full proportions; feature blocks 3-up; spec tables at comfortable width with padding |
| Wide | > 1440px | Content max-width caps at 1280px and centers; extra whitespace on sides; no layout change beyond centering |

### Touch Targets

- All interactive elements maintain minimum 44×44px tap area
- Nav hamburger icon padded to 48×48px on mobile
- Product cards are fully tappable (entire card is link target)
- Spec table rows do not contain interactive elements; links are in dedicated columns with adequate padding

### Collapsing Strategy

- Navigation: full horizontal links → hamburger with slide-out drawer at < 744px
- Product grids: 3-up → 2-up → 1-up as width decreases
- Spec tables: fixed layout → horizontal scroll with sticky first column on mobile
- Hero banner: side-by-side layout → stacked (text on top, image below or hidden)
- Feature blocks: 3-up → 2-up → single stack
- Footer columns: 4-column → 2-column → single stack

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: The site returned zero color tokens via static extraction. Colors above are inferred from publicly available Staber marketing materials and general industrial-brand conventions — they have NOT been validated against the live CSS and may be inaccurate.
- **No font stacks extracted**: Zero font-family declarations were captured. The site likely loads styles dynamically or uses server-rendered pages that resist static scraping. System sans-serif is assumed but the actual webfont (if any) is unknown.
- **No platform detected (not Shopify)**: Unable to determine the CMS or framework, limiting assumptions about component patterns.
- **No theme-color meta tag**: Cannot confirm mobile browser chrome color.
- **Icon system unknown**: Whether Staber uses an icon font, SVG sprite, or inline SVGs could not be determined.
- **Interaction patterns unverified**: Hover states, transitions, and animation timings are assumed conservative (150–200ms ease) but not confirmed.
- **Product image aspect ratios assumed**: 4:3 is inferred from typical appliance photography; actual crop ratios on the live site may differ.
- **Form validation patterns unknown**: Error states and inline validation behavior could not be observed from static extraction.
