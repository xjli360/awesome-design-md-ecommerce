---
version: alpha
name: "Fluance"
source_url: "https://www.fluance.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fluance earns its audiophile credibility through restraint — nearly every surface sits in a family of cool near-whites (#f7f7f7, #f5f6f7, #fafafa) while a single alarm red, #da272a, does all the persuasive heavy lifting on CTAs, sale flags, and promotional strips. The contrast is deliberate: against clinical backgrounds, that red reads less like decoration and more like a power indicator, the kind of light that tells you the amplifier is on. Headings set in Titillium Web carry a slightly condensed, engineered geometry — the same family of letterforms found on oscilloscope labels and rack equipment panels — functioning as spec anchors rather than emotional mood-setting. Exo 2 enters at smaller scales for technical callouts and specification labels, extending the instrumentation vocabulary into the fine print where buyers verify frequency response and signal-to-noise ratios. Open Sans handles body copy, sustaining readability through long product descriptions and FAQ text without competing visually with the display type. Corner geometry follows the same logic of controlled precision: buttons sit at {rounded.xs} (4px), cards at {rounded.sm} (8px), and nothing tips into the pill shapes that signal lifestyle softness. A secondary teal, #007cad, handles informational links and secondary navigation states — it cools the palette just enough to prevent the red from reading purely as error rather than urgency. Dark surfaces appear at the footer and in promotional hero modules, where near-black (#0a0a0a) grounds reversed-out white type and gives product photography a stage-isolation effect. The layout grid is tight and rectilinear, biased toward maximum product surface area — spec tables, multi-angle image carousels, and comparison modules take priority over editorial whitespace. Sale badges and "New" callouts share the same #da272a as primary CTAs, doubling the red's semantic load: both "buy this" and "this is notable" use the same signal color, creating a tight associative loop that trained buyers learn quickly.

colors:
  primary: "#da272a"
  primary-active: "#b52025"
  primary-disabled: "#f0b4b5"
  accent: "#007cad"
  accent-dark: "#005f87"
  ink: "#111827"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  border: "#d1d5db"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f5f6f7"
  surface-alt: "#f7f9fa"
  surface-dark: "#0a0a0a"
  surface-dark-2: "#1f2937"
  surface-mid: "#4b5563"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  icon-muted: "#6e716e"
  info: "#2563eb"

typography:
  display-xl:
    fontFamily: "'Titillium Web', 'Exo 2', Arial, sans-serif"
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Titillium Web', 'Exo 2', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Titillium Web', 'Exo 2', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Titillium Web', 'Exo 2', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Titillium Web', 'Exo 2', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  button-md:
    fontFamily: "'Titillium Web', 'Exo 2', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Titillium Web', 'Exo 2', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Exo 2', 'Exo', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  price-display:
    fontFamily: "'Titillium Web', 'Exo 2', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Titillium Web', 'Exo 2', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px

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
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
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
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 26px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.accent}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoAccentColor: "{colors.primary}"
    dropdownBackground: "{colors.canvas}"
    dropdownBorder: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "1/1"
    hoverBorder: "1px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaButton: "button-primary"
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    rowPadding: "{spacing.sm} {spacing.base}"
    stripedRowBackground: "{colors.canvas}"
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  product-badge:
    backgroundColor: "{colors.surface-dark-2}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted-soft}"
  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  category-tile:
    backgroundColor: "{colors.surface-dark-2}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    overlay: "linear-gradient(to bottom, transparent 40%, rgba(0,0,0,0.75))"
    hoverScale: 1.02
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.muted-soft}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"
    borderTop: "3px solid {colors.primary}"
    iconColor: "{colors.muted-soft}"

## Components

### Buttons

**`button-primary`** — Solid #da272a fill with white uppercase Titillium Web at 14px/1px tracking, 4px radius, 44px tall. On hover the background shifts to `primary-active` (#b52025); disabled state drains to the light-pink `primary-disabled`. The uppercase tracking and compressed weight read as a command rather than an invitation, consistent with the brand's engineering register.

**`button-secondary`** — White background with a 2px #da272a border and red text, mirroring the primary's uppercase Titillium Web treatment. Used for secondary CTAs in product detail pages (e.g., "Add to Wish List", "Compare") where visual weight must stay subordinate to the primary action without disappearing entirely.

**`button-ghost`** — Transparent background with `body` (#374151) text, no border, small Titillium Web caps. Used in nav dropdowns, pagination, and inline text actions where chrome would add unnecessary visual noise.

**`button-accent`** — Same geometry as primary but filled with teal #007cad. Reserved for informational CTAs like "Learn More" in editorial modules, preventing the overuse of red in non-transactional contexts.

### Navigation

**`nav-bar`** — White canvas bar at 64px height with a subtle 1px `hairline` bottom border. The Fluance wordmark or logo appears with a red accent treatment. Nav links use Titillium Web 14px/600 with a 0.2px letter-space; active and hover states switch to `primary` red underline. Cart and account icons sit right-aligned in `muted` gray, gaining `ink` on hover. Below 1128px, the desktop nav collapses into a hamburger drawer with the same dark-on-white type treatment.

### Product Card

**`product-card`** — Light gray (#f5f6f7) background with 1px `hairline` border and 8px radius, scaling to a `primary` red border on hover to signal selectability. Image fills the top at 1:1 aspect ratio. Below the image: product name in `title-sm` (15px/600 Titillium Web), a short attribute line in `caption` (12px Open Sans, `muted`), then the price in `price-display` (26px/700). Badge stack (sale, new, award) pins to the top-left corner of the image area, using `sale-badge`, `new-badge`, or `product-badge` as applicable. Star ratings render inline below price in `muted-soft` with a compact count.

### Hero Banner

**`hero-banner`** — Near-black (#0a0a0a) field with full-width product photography, white display headline in Titillium Web 38px/700, body copy in Open Sans 15px, and a `button-primary` CTA. A lighter variant (`hero-banner-light`) uses the `surface-soft` (#f7f7f7) background with `ink` type for mid-page feature modules. Padding is `section` (64px) vertically.

### Spec Table

**`spec-table`** — The most brand-distinctive component. Two-column layout with uppercase Exo 2 11px/600 label column in `muted` and value column in Open Sans 13px `body`. Rows alternate between `surface-soft` and white `canvas` for scanability. A 1px `hairline` border wraps the table; a 3px `primary` red left border on the table container anchors it to the brand. Used extensively on every product detail page, validating buyer decisions with measured data.

### Badges

**`sale-badge`** — Solid red (#da272a) chip with white uppercase Exo 2 spec-label type, 4px radius, 3px/8px padding. Appears over product card imagery and in-cart line items. **`new-badge`** uses the same geometry in teal (#007cad). **`product-badge`** uses dark `surface-dark-2` (#1f2937) for award or editorial callouts like "Editor's Choice" — same type scale, cooler register.

### Promo Strip

**`promo-strip`** — Full-width #da272a bar at the page top, 8px/16px padding, center-aligned Open Sans 13px white text. Carries free-shipping thresholds, limited-time sale codes, and seasonal promotions. The strip's saturation draws the eye before the nav renders, making it the highest-urgency real estate on the page.

### Category Tile

**`category-tile`** — Dark `surface-dark-2` background with full-bleed image and a bottom-gradient scrim (transparent to 75% black). Category name reversed in `on-dark` Titillium Web 18px/600 pins above the gradient. On hover the tile scales 1.02× for interactivity feedback. Used in the homepage category grid and in collection landing pages.

### Footer

**`footer`** — Near-black (#0a0a0a) background anchoring the page. A 3px `primary` red top border signals brand presence on the dark field. Four-column link grid in Open Sans 13px `on-dark` with `muted-soft` sublinks. Column headings in Titillium Web 15px/600 white. Social icons appear in `muted-soft`, gaining white on hover. Newsletter input uses a borderless dark-field variant with a `button-primary` inline submit.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav drawer slides from left; hero headline drops to display-sm (22px); spec table scrolls horizontally; promo strip wraps to 2 lines; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav still collapsed to hamburger; hero supports side-by-side image/text layout; category tiles shift to 2×2 grid; footer moves to 2-column layout |
| Desktop | 1128–1440px | Full horizontal nav bar revealed; three- to four-column product grid; hero occupies full viewport width; spec table full-width with fixed label column; footer four-column |
| Wide | > 1440px | Max content width ~1400px centered with increased lateral padding; hero imagery scales but type containers stay capped; category grid can expand to 5 columns |

### Touch Targets

- All interactive buttons minimum 44px tall (matching component height definitions)
- Nav icons and hamburger button minimum 44×44px tap area even when visually smaller
- Product card entire surface is tappable, not just the CTA
- Spec table rows are not interactive; no minimum touch target required there
- Badge chips are display-only; no tap target needed

### Collapsing Strategy

- Desktop mega-menu collapses to full-screen drawer on tablet/mobile with back-navigation breadcrumb
- Spec table switches from two-column inline layout to accordion rows on mobile to prevent horizontal scroll where possible; falls back to horizontal scroll for comparison tables
- Hero banner switches from overlay-text-on-image to stacked (image above, text below) at mobile breakpoint
- Category tile grid reflows: 4-col desktop → 2-col tablet → 1-col mobile with reduced tile height
- Footer: 4-col → 2-col → 1-col with each section collapsible via accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` detected; browser chrome accent color for mobile is undefined
- `primary-disabled` (#f0b4b5) and `accent-dark` (#005f87) are mathematically derived from extracted primaries — not directly observed in the extracted palette
- `#4a4af4` (indigo-like) appears in extracted colors but its usage context is unclear; may be a UI framework default or an unrelated icon color rather than a brand token — excluded from palette
- `#2563eb` appears to be a Tailwind utility default (blue-600); retained as `info` but not confirmed as intentional brand blue
- Baskerville appears in font stacks but its usage context is unconfirmed — likely present for a third-party widget or embedded content rather than Fluance brand typography
- Exact font weights available in the Titillium Web and Exo 2 variable or static instances on the live site are not confirmed; 600 and 700 assumed from typical web deployments
- No design token export or public design system documentation observed; all component sizing is inferred from visual inspection patterns
- Dark-mode or high-contrast variant not observed; assumed light-mode only
