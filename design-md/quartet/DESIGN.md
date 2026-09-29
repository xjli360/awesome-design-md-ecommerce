---
version: alpha
name: "Quartet"
source_url: "https://www.quartet.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The steel frame of a Quartet glass board sits close to #313131 — a warm near-black that recedes when the white writing surface fills with marker strokes and color-coded sticky notes. That single confirmed extraction, all the site's anti-bot wall permitted through, encodes a coherent brand posture: a workspace brand whose own visual identity steps back to let the working surface be the hero. The complete system-font stack (system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue) reinforces that disposition — no proprietary typeface, no brand-font signature, just assured legibility at product specification tables and dimension callouts.

  Quartet's catalog stratifies by board material — glass at the premium end, porcelain in the mid-range, melamine at value — and that three-tier logic likely maps directly into the digital layer as distinct tier badges, filtered rail tabs, and price-range visual anchors. The palette built here is a cautious inference from #313131 plus B2B office product conventions. A professional blue (#0057A8) carries primary CTAs, consistent with a brand that distributes through enterprise dealers and educational procurement channels. The confirmed charcoal anchors nav strokes, headlines, and body text; canvas stays white; two surface-gray steps create depth behind product imagery without competing with the boards' clean white faces.

  Shape language is deliberately undramatic: `{rounded.xs}` on tier badges and spec chips, `{rounded.sm}` on buttons and text inputs, `{rounded.md}` on product cards. The nav bar is a flat 64px white rail with the Quartet wordmark left-anchored in `{colors.ink}` and a sparse utility cluster (search, account, cart) at right. Below it, a sticky category rail segments the catalog by product family using `{typography.caption}` labels with a 2px `{colors.primary}` underline on the active tab. Four-column desktop grids run `{spacing.lg}` gutters; image tiles pull `{colors.surface-soft}` backgrounds to isolate white-edged board photography. Section rhythm uses `{spacing.section}` vertical beats with a single `{colors.hairline}` rule between product families.

colors:
  primary: "#0057A8"
  primary-active: "#003F80"
  primary-disabled: "#99BBD9"
  ink: "#313131"
  body: "#4A4A4A"
  muted: "#717171"
  hairline: "#E0E0E0"
  canvas: "#FFFFFF"
  surface-soft: "#F4F4F4"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  accent-tier-glass: "#B8922A"
  accent-tier-porcelain: "#5B8DB8"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
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
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  label-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1.5px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  category-rail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.caption}"
    borderBottom: "1px solid {colors.hairline}"
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 2px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    bodyTypography: "{typography.body-sm}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    ctaButton: "{components.button-primary}"
  tier-badge-glass:
    backgroundColor: "{colors.accent-tier-glass}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  tier-badge-porcelain:
    backgroundColor: "{colors.accent-tier-porcelain}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  tier-badge-melamine:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1.5px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
  feature-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.canvas}"
    mutedTextColor: "{colors.muted}"
    headingTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"

---

## Components

### Buttons

**`button-primary`** — A solid `{colors.primary}` blue rectangle at 44px tall with `{rounded.sm}` corners and 12px/24px padding. Typography is `{typography.button-md}` (15px, weight 600, 0.1px tracking) in `{colors.on-primary}` white. Active state deepens to `{colors.primary-active}` (#003F80); disabled washes out to `{colors.primary-disabled}`. No shadow — flat and functional in every context.

**`button-secondary`** — Identical dimensions to primary but inverted: white `{colors.canvas}` fill with a 1.5px `{colors.primary}` border and `{colors.primary}` label text. Used for secondary product actions (Compare, Add to Wishlist) adjacent to the primary CTA without competing visually.

### Text Input

**`text-input`** — 44px tall with `{rounded.sm}` corners and a 1px `{colors.hairline}` border that sharpens to 1.5px `{colors.primary}` on focus. `{typography.body-md}` at `{colors.ink}` inside; placeholder in `{colors.muted}`. The 10px/14px padding gives filter forms and address fields room to breathe without reading as oversized.

### Navigation

**`nav-bar`** — A 64px flat white rail with a single bottom `{colors.hairline}` divider. The Quartet wordmark sits left-anchored in `{colors.ink}`; right cluster holds search icon, account, and cart. Link text runs `{typography.nav-link}` (14px, weight 500); hover state is underline only — no background fills.

**`category-rail`** — A 44px secondary sticky bar immediately below the main nav, segmenting the catalog by product family (Whiteboards, Cork Boards, Glass Boards, Planners, Accessories). Tab labels use `{typography.caption}` (uppercase, 0.2px tracking) in `{colors.body}`; the active tab shifts to `{colors.primary}` text with a 2px `{colors.primary}` bottom indicator. The rail remains sticky while the user scrolls through the product grid below.

### Product Card

**`product-card`** — White `{colors.surface-card}` card with `{rounded.md}` corners and `{spacing.base}` inner padding. The image tile occupies the upper portion against a `{colors.surface-soft}` background to cleanly isolate white-bordered board photography. Product name renders in `{typography.title-md}`, price in `{typography.body-md}`, and supporting spec detail in `{typography.body-sm}`. A tier badge (`tier-badge-glass`, `tier-badge-porcelain`, or `tier-badge-melamine`) overlays the image top-left corner. No shadow at rest; a subtle box-shadow lifts the card on hover.

### Hero Banner

**`hero-banner`** — The primary brand moment: a full-width dark section on `{colors.ink}` (#313131) with headline copy in `{typography.display-xl}` white and supporting body in `{typography.body-md}`. A `{components.button-primary}` CTA anchors the bottom of the text block. Padding is `{spacing.xxl}` vertical, `{spacing.section}` horizontal. On desktop the layout splits — text left, product photography right; on mobile the image stacks above text.

### Tier Badges

**`tier-badge-glass`** — A `{colors.accent-tier-glass}` gold chip at `{rounded.xs}` corners, carrying `{typography.label-sm}` (11px, uppercase, 700 weight) in white, padded 3px × 8px. Signals premium glass-surface boards at a glance. **`tier-badge-porcelain`** uses `{colors.accent-tier-porcelain}` steel blue for mid-tier boards. **`tier-badge-melamine`** uses `{colors.muted}` gray for value-range products. All three share identical shape and typography; only fill color distinguishes tier.

### Search Bar

**`search-bar`** — 40px tall with `{rounded.sm}` and a `{colors.surface-soft}` fill at rest, transitioning to white fill with 1.5px `{colors.primary}` border on focus. A `{colors.muted}` magnifying-glass icon sits left-inset; `{typography.body-md}` governs input text. The search bar appears in two scales: compact inside the nav utility cluster and full-width in category page headers.

### Feature Tag

**`feature-tag`** — A small horizontal chip in `{colors.surface-soft}` with a 1px `{colors.hairline}` border and `{rounded.xs}` corners. Carries spec descriptors such as "Magnetic," "Self-Healing," "Reversible," or "Dry-Erase" in `{typography.body-sm}` `{colors.body}`. Appears as a wrapping row of chips below the product headline in detail views and catalog cards at wider breakpoints.

### Promo Banner

**`promo-banner`** — A 36px slim full-width bar in `{colors.primary}` sitting above the nav bar. Promotional copy (free shipping thresholds, seasonal offers) renders in `{typography.caption}` uppercase white, center-aligned. Dismissible on mobile; persistent on desktop.

### Footer

**`footer`** — `{colors.ink}` background with `{colors.canvas}` text and a four-column link grid on desktop. Section headings in `{typography.caption}` uppercase; body links in `{typography.body-sm}`. The hard cut from white canvas to charcoal reads as its own visual divider — no top border required. Padding `{spacing.xxl}` vertical, `{spacing.section}` horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category-rail collapses to a horizontally scroll-snapping chip row; hero stacks image above text block; nav condenses to hamburger + wordmark + cart icon |
| Tablet | 744–1128px | Two-column product grid with `{spacing.base}` gutters; category-rail displays as full tab bar; hero splits 50/50 image/text; nav shows top-level links without secondary expansion |
| Desktop | 1128–1440px | Four-column product grid with `{spacing.lg}` gutters; full nav bar and sticky category rail; hero full-bleed with 40/60 text/image split; tier badges visible on product cards |
| Wide | > 1440px | Content caps at 1440px with outer gutters growing symmetrically; product grid stays at four columns; section horizontal padding scales to `{spacing.section}` on each side |

### Touch Targets

- All interactive elements (buttons, inputs, category tabs) maintain a minimum 44px tap height
- Category rail tabs each carry at least 80px width for reliable tap contact
- Product cards are fully tappable surface-to-edge — no precision targeting of a label or CTA required
- Compressed nav icons (cart, account, search) carry 44×44px tap zones enforced via padding, not element size

### Collapsing Strategy

- Navigation collapses at < 744px to a hamburger drawer; category-rail converts to a horizontal scroll-snap chip row pinned below the nav bar
- Four-column product grid steps to two columns at tablet (`{spacing.base}` gutters) and one column at mobile (`{spacing.sm}` gutters)
- Hero text/image split stacks at mobile: image first at constrained aspect ratio, text block below with reduced vertical padding
- Footer four-column link grid steps to two columns at tablet and single-column accordion sections at mobile, each expandable by tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Color palette nearly unextractable**: only `#313131` (ink/charcoal) was confirmed from the live site — the page returned an anti-bot challenge before full rendering. All other colors (primary blue, surface grays, tier accents) are inferred from B2B workspace conventions and are unverified against actual brand assets.
- **No custom brand font detected**: extraction returned only system font stacks. Quartet may load a licensed typeface via `@font-face` or a third-party CDN blocked by the anti-bot wall. All typography here uses the confirmed system-ui stack as a fallback.
- **Primary brand color unconfirmed**: the professional blue (#0057A8) used for CTAs is a category-informed inference. Quartet's actual primary could differ substantially — navy, teal, and gray-blue are all plausible in this product segment.
- **Tier color system placeholder**: `accent-tier-glass` (#B8922A gold) and `accent-tier-porcelain` (#5B8DB8 blue) are speculative. The actual material-tier palette requires a live authenticated site pass to confirm.
- **Interactive state colors unconfirmed**: hover, active, and focus variants for all components are derived arithmetically from the inferred primary; actual brand-specified values are unknown.
- **Icon system unknown**: Quartet likely maintains a custom or licensed icon set for product-family navigation and feature callouts; no icon assets or sprite references were reachable.
- **Meta theme-color absent**: no `<meta name="theme-color">` was present, indicating the brand does not assert a mobile browser chrome accent.
- **Promotional and sale color system**: clearance badges, sale pricing, and urgency states (low stock, limited time) typically use a distinct red or orange in this category; no extraction was possible.
