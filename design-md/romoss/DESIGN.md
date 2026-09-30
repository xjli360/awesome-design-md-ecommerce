---
version: alpha
name: "Romoss"
source_url: "https://www.romoss.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Electric cyan (#00dbdb) pulses through Romoss's interface like current through a charging cable — a single, unmistakable voltage that marks every primary CTA, progress indicator, and product highlight against an otherwise restrained gray-and-white canvas. The color system draws from adjacent teal (#2cb2c2) for hover and active states, creating a subtle thermal gradient that reinforces the brand's energy-transfer identity without ever feeling garish. Typography runs entirely on Outfit, a geometric sans-serif whose open counters and uniform stroke width give technical specifications the same visual clarity as marketing headlines; display sizes stay at 600–700 weight while body copy sits at 400, trusting the font's inherent legibility over heavy contrast. OPPOSansM appears as a secondary CJK stack for Chinese-language content, maintaining the same geometric DNA across scripts. Surface architecture is flat and panel-based: product cards lift on `{rounded.sm}` corners with barely-there `{colors.hairline}` borders, hero sections run full-bleed on `{colors.canvas}` with oversized product photography dominating the viewport, and specification tables alternate between `{colors.surface-soft}` and white rows for scanability. The near-black ink (#231815) carries a warm brown undertone that softens the otherwise clinical tech aesthetic, while a generous neutral palette (#f5f5f5, #f0f0f0, #e5e5e5) provides layering without visual noise. Warning and error states borrow from a standard utility palette — coral (#f56c6c) for alerts, amber (#e6a23c) for cautions — keeping the cyan channel exclusively for brand affirmation. Button radii stay compact at `{rounded.xs}` to `{rounded.sm}`, projecting precision over friendliness, while pill shapes (`{rounded.full}`) appear only on tags and status badges. Spacing is generous at the section level (`{spacing.section}`) but tight within product grids, compressing information density where shoppers compare mAh ratings and port counts side by side.

colors:
  primary: "#00dbdb"
  primary-active: "#2cb2c2"
  primary-disabled: "#99eff0"
  ink: "#231815"
  body: "#444444"
  muted: "#b8bdc1"
  hairline: "#e5e5e5"
  hairline-soft: "#ebedef"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-muted: "#f0f0f0"
  surface-alt: "#f8f8f8"
  surface-warm: "#f4f4f4"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#f56c6c"
  warning: "#e6a23c"
  link: "#007aff"
  border: "#dadada"
  border-light: "#e8e8e8"
  bg-secondary: "#ebe9e9"
  cyan-alt: "#00d9d9"

typography:
  display-xl:
    fontFamily: "'Outfit', 'OPPOSansM', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  spec-value:
    fontFamily: "'OutfitBold', 'Outfit', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  spec-unit:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Outfit', 'OPPOSansM', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 12px 32px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 11px 31px
    height: 44px
    border: 1px solid {colors.border}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.primary}
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 40px
    border: 1px solid {colors.border}
    focusBorder: 1px solid {colors.primary}
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 64px
    boxShadow: 0 2px 8px rgba(0,0,0,0.06)
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.sm}"
    hoverTransform: translateY(-2px)
    hoverShadow: 0 8px 24px rgba(0,0,0,0.08)
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-spec:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 560px
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
  spec-highlight:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.spec-value}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  spec-highlight-unit:
    typography: "{typography.spec-unit}"
    textColor: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid {colors.primary}
    padding: 12px 20px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid transparent
    padding: 12px 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    opacity: 0.75
    hoverOpacity: 1.0
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  product-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    thumbnailSize: 64px
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorderActive: 2px solid {colors.primary}
  charging-progress-bar:
    backgroundColor: "{colors.border-light}"
    fillColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 6px
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    altBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline-soft}
  spec-table-label:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"

---

## Components

### Buttons

**`button-primary`** — Solid cyan (#00dbdb) fill with white text, compact 4px radius (`{rounded.xs}`) that reads as precision-engineered rather than playful. Active state darkens to the deeper teal (#2cb2c2) with no scale transform. Disabled state lightens to a washed-out cyan at reduced opacity — the button shape remains visible but clearly inactive.

**`button-secondary`** — White fill with a 1px `{colors.border}` stroke and dark ink text. On hover the border color transitions to `{colors.primary}`, signaling interactivity without competing with the primary CTA. Padding mirrors the primary button for consistent alignment when placed side-by-side.

**`button-ghost`** — Transparent background with cyan text, used for tertiary actions like "Learn More" links within product sections. No border, no background — relies purely on the brand color to signal clickability.

### Navigation

**`nav-bar`** — Fixed 64px white bar with a subtle bottom hairline. Logo sits left, navigation links center in `{typography.nav-link}` (Outfit 500 at 15px), and utility icons (search, cart, account) cluster right. On scroll, the hairline drops away in favor of a soft box-shadow for depth separation.

**`category-tab-active` / `category-tab-inactive`** — Horizontal tab strip for product category filtering. Active state shows cyan text with a 2px cyan bottom border; inactive shows muted gray with transparent border. Transition between states is a 200ms color fade.

### Product Cards

**`product-card`** — Soft gray background (`{colors.surface-soft}`) with `{rounded.sm}` corners. Product image fills the upper portion on matching rounded corners. Below the image: title in `{typography.title-sm}`, a one-line spec summary in `{typography.caption}` muted text, and price in `{typography.title-md}`. On hover, the card lifts 2px with an expanded shadow, creating a subtle depth cue without color change.

**`product-card-spec`** — Inline capacity/wattage callouts rendered in muted caption text directly below the product title. Common patterns: "40000mAh · 65W" or "20000mAh · PD 3.0".

### Hero & Marketing Sections

**`hero-section`** — Full-width white canvas with a minimum height of 560px. Product photography dominates 60% of the viewport width (typically right-aligned), while the headline and subhead stack left. No background gradients — the product image itself provides visual weight.

**`hero-headline`** — Display-xl (48px, weight 700) in near-black ink. Headlines tend toward short, punchy claims about capacity or charging speed rather than lifestyle language.

**`hero-subhead`** — Body-lg (16px, weight 400) in `{colors.body}` gray, providing technical context for the headline claim. Sits 12px below the headline.

### Specification Displays

**`spec-highlight`** — Rounded panel (`{rounded.md}`) on `{colors.surface-soft}` background showcasing a single key metric. The numeric value renders in `{typography.spec-value}` (32px bold) in cyan, with the unit label in `{typography.spec-unit}` (14px, medium weight) in body gray below it. Used in grids of 3–4 to summarize capacity, wattage, ports, and weight.

**`spec-table-row`** — Alternating white/gray rows for detailed specification lists. Label left-aligned in muted text, value right-aligned in bold ink. Separated by `{colors.hairline-soft}` bottom borders.

### Progress & Status

**`charging-progress-bar`** — Thin (6px) pill-shaped (`{rounded.full}`) track in light gray with a cyan fill that animates left-to-right. Used on product pages to visualize charging speed comparisons or battery level demonstrations.

**`badge-new` / `badge-sale` / `badge-warning`** — Pill-shaped (`{rounded.full}`) status indicators. "NEW" badges use cyan fill; sale/discount badges use coral (#f56c6c); stock warnings use amber (#e6a23c). All use uppercase 11px bold white text.

### Search

**`search-bar`** — Pill-shaped (`{rounded.full}`) input on a soft gray background with a hairline border. On focus, the border transitions to cyan. Placeholder text in muted gray, input text in ink. Height matches the primary button (44px) for visual consistency in the nav area.

### Product Gallery

**`product-gallery`** — Soft gray container with `{rounded.sm}` housing a main image area and a row of 64px square thumbnails below. Active thumbnail receives a 2px cyan border; inactive thumbnails show no border. Supports swipe navigation on touch devices.

### Footer

**`footer`** — Dark ink (#231815) background with white text at reduced opacity (75%) for links, full opacity for headings. Four-column grid on desktop collapsing to accordion on mobile. Social icons and payment method badges sit at the very bottom separated by a subtle white/10% hairline.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks vertically (image above, text below); nav collapses to hamburger + logo + cart icon; spec highlights stack 2×2; footer accordion |
| Tablet | 744–1128px | Two-column product grid; hero image shrinks to 50% width; nav shows top 4 links with overflow in "More" dropdown; spec highlights in single row of 4 |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at full 60/40 split; footer in 4-column grid |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid may expand to 4 columns; additional whitespace on hero flanks |

### Touch Targets

- Minimum tap target: 44×44px on all interactive elements
- Product card entire surface is tappable, not just the image or title
- Category tabs have 12px horizontal padding extending the tap zone beyond visible text
- Mobile hamburger icon: 48×48px tap area with 16px inset from screen edge
- Gallery thumbnails: 64×64px with 8px gap ensuring no accidental adjacent taps

### Collapsing Strategy

- Navigation links collapse to a slide-in drawer at mobile breakpoint; drawer overlays content with a scrim
- Product specification grids reflow from horizontal (4-across) to 2×2 grid below 744px
- Hero sections invert from side-by-side to stacked, with the product image maintaining aspect ratio via object-fit: contain
- Footer columns collapse to vertically-stacked accordions with chevron toggles; each section closed by default
- Spec tables remain full-width but label/value pairs stack vertically below 480px instead of sitting in a two-column row

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No CSS custom properties or design tokens file was detected — colors and typography likely injected via a bundled JS framework or build pipeline
- OPPOSansM licensing and character coverage scope unclear; fallback behavior for Latin-only contexts not confirmed
- Exact box-shadow values on hover states not extractable from static analysis
- Icon system (beyond swiper-icons) not identified — likely inline SVGs or a proprietary icon sprite
- Animation/transition timing functions and durations not captured
- Dark mode support not detected; unclear if the brand offers one
- The near-duplicate cyans (#00dbdb vs #00d9d9) may be aliased or represent a rendering inconsistency rather than intentional differentiation
- Mobile navigation drawer transition and overlay opacity values not confirmed
- Form validation styling (focus rings, error message positioning) inferred from standard patterns rather than direct extraction
