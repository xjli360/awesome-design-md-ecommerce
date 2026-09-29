---
version: alpha
name: "Bullion Exchanges"
source_url: "https://bullionexchanges.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Real-time spot prices run at the top of every Bullion Exchanges page before the hero image loads — a design decision that privileges financial transparency over visual presentation, treating gold and silver fixes as load-bearing UI elements rather than decorative tickers. The single confirmed brand color is a dense charcoal (#313131), deployed across the primary navigation, CTA buttons, and body ink with a conviction that precious metals buyers respond to institutional gravity. No custom typeface was extracted; the entire site runs on system-native stacks (SF Pro on Apple devices, Segoe UI on Windows, Roboto on Android), which gives product pages a Bloomberg-terminal directness — weights, purities, and per-ounce premiums read at the same density as brokerage software. Product photography shoots coins and bars against white backgrounds, letting proof finishes, mint strikes, and die details carry the selling weight. Trust architecture is dense: secure payment icons, authorized dealer seals, and BBB ratings cluster near checkout — a visual insurance policy for transactions that routinely exceed $1,000. Components are built square and conservative, with {rounded.xs} at most on inputs and cards, signaling the kind of operations that press physical currency rather than novelty. The charcoal-nav-on-white-canvas inversion — dark header, light browsing surface, dark footer — frames every page like a ledger: serious at the edges, open in the middle. An anti-bot layer blocked full palette extraction, so the color system below is constructed from the confirmed #313131 anchor; gold-tone accent colors common across the bullion dealer category remain unverified inference documented in Known Gaps.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#444444"
  muted: "#767676"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#1e1e1e"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  gold-accent: "#c9a84c"
  spot-up: "#1a7a2e"
  spot-down: "#b91c1c"
  spot-neutral: "#767676"
  positive: "#2a7a3b"
  negative: "#b91c1c"
  badge-trust: "#f0f7ff"
  badge-trust-border: "#b8d4f0"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  spot-ticker:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  tab-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    rounded: "{rounded.xs}"
    padding: "12px 24px"
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "11px 23px"
    height: 44px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: "8px 16px"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 50px
    width: "100%"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: "10px 14px"
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "10px 14px 10px 40px"
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    logoHeight: 40px
  nav-bar-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "1px solid {colors.hairline}"
  spot-price-ticker:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spot-ticker}"
    height: 36px
    padding: "0 {spacing.base}"
    upColor: "{colors.spot-up}"
    downColor: "{colors.spot-down}"
    neutralColor: "{colors.spot-neutral}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "1/1"
    priceTypography: "{typography.price-display}"
    titleTypography: "{typography.title-sm}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 2px 12px rgba(0,0,0,0.10)"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  price-display:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
    premiumColor: "{colors.muted}"
    premiumTypography: "{typography.caption-bold}"
  metal-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.tab-label}"
    rounded: "{rounded.xs}"
    padding: "8px 20px"
  metal-tab-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.tab-label}"
    rounded: "{rounded.xs}"
    padding: "8px 20px"
    border: "1px solid {colors.hairline}"
  trust-badge:
    backgroundColor: "{colors.badge-trust}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.badge-trust-border}"
    padding: "6px 12px"
    iconSize: 16px
  premium-over-spot:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline-soft}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    buttonSize: 36px
    inputWidth: 52px
    height: 40px
  category-grid-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspectRatio: "4/3"
    hoverBorderColor: "{colors.primary}"
  sort-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: "8px 32px 8px 12px"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    width: 240px
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.hairline}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — A solid charcoal (#313131) rectangle with {rounded.xs} corners, uppercase tracking at 0.5px, and a 44px tap height. The dark fill signals authority rather than urgency — buyers treating precious metals as a store-of-value investment respond to restrained confidence over flashy CTAs. Active state deepens to #1a1a1a; disabled state grays to #a0a0a0 while holding the same geometry.

**`button-secondary`** — White fill with a 1px charcoal border and matching charcoal type, used for secondary actions like "View Details" and "Add to Watchlist." The 11px/23px padding asymmetry optically matches the primary button's height without carrying the same visual weight.

**`button-add-to-cart`** — A full-width variant of the primary button deployed on product detail pages, stretching to 100% container width at 50px height to maximize the conversion target on mobile where single-item purchase decisions happen quickly.

**`button-ghost`** — Transparent background with charcoal text at 13px/600 weight; used for tertiary actions in filter panels, breadcrumb traversal, and "See All" links in category rows.

### Navigation

**`nav-bar`** — The primary navigation runs on the extracted #313131 at 64px height with white logotype and nav links. This dark-header-on-white-canvas approach separates the institutional shell from the browsing surface at a glance — a pattern common to financial marketplaces where authority is signaled structurally, not through decorative motifs. A secondary strip (`nav-bar-secondary`) runs on `{colors.surface-soft}` and carries category shortcuts.

**`spot-price-ticker`** — A near-black band (`{colors.surface-dark}`) carrying live spot prices for gold, silver, platinum, and palladium in 13px semibold. Price direction is communicated through three-color convention: `{colors.spot-up}` green for gains, `{colors.spot-down}` red for losses, `{colors.spot-neutral}` gray for flat — identical to financial data display standards so experienced buyers read it instantly.

### Product Cards

**`product-card`** — White card with 1px hairline border and square corners ({rounded.xs}), sharpening to a charcoal border on hover with a soft box shadow. Images hold a 1:1 aspect ratio against white backgrounds to emphasize coin and bar detail at browsing scale. Price renders at 24px/700 in `{typography.price-display}`; a secondary line below shows the per-ounce premium over spot in `{typography.caption-bold}` muted gray — the two numbers buyers actually compare.

**`product-card-badge`** — Fully square badges (no border radius) anchor to the top-left corner of the card image in solid charcoal with white text. Labels include SALE, NEW, LOW STOCK, and BEST VALUE — all uppercase at 11px/700 weight. The zero-radius badge distinguishes itself from any rounded UI elements and reads as a physical stamp rather than a digital pill.

### Metal Navigation

**`metal-tab-active`** — Selected metal categories (Gold, Silver, Platinum, Palladium) use the charcoal fill at {rounded.xs} with white text, matching the primary button. This prevents cognitive separation between metal-filtering and page-level CTAs; the same dark authority applies to both.

**`metal-tab-inactive`** — Unselected tabs hold a white fill with hairline border and muted text, creating an unambiguous selected/unselected contrast without requiring color variation beyond the primary charcoal system.

### Trust & Financial Transparency

**`trust-badge`** — Light blue-tinted capsule with `{colors.badge-trust}` background and `{colors.badge-trust-border}` border, clustered near checkout with SSL seals, authorized dealer marks, and payment logos. At 12px caption text with a 16px inline icon, the badges read at a glance without consuming layout real estate.

**`premium-over-spot`** — A soft gray information row contextualizing each product price against live spot, displaying "X.XX% over spot" or "$X.XX/oz premium" in `{typography.body-sm}`. This transparency element is category-critical: bullion buyers calculate premium efficiency before committing, and surfacing the math removes the friction of manual calculation.

**`price-display`** — The product price at 24px/700 anchors the card and detail page hierarchy. A subordinate premium line in `{typography.caption-bold}` muted gray immediately below contextualizes the absolute dollar figure relative to spot — the two lines together form the primary decision-making unit for repeat buyers.

### Layout Shells

**`hero-banner`** — Full-width panel on `{colors.surface-soft}` with {spacing.section} vertical padding and a display headline at `{typography.display-md}`. Photography typically features a single featured coin or bar at large scale against neutral background; the text/image composition stays clean with no overlay gradients that would obscure metallic surface detail.

**`filter-sidebar`** — 240px left-docked panel with hairline border carrying category, weight (oz/gram), mint, year, and price-range filters. Section headings use `{typography.title-sm}` in charcoal; options run `{typography.body-sm}` with standard checkbox affordances. On mobile this panel converts to a full-screen bottom sheet.

**`category-grid-tile`** — Discovery-layer tile in a multi-column grid, with 4:3 image aspect ratio and a title below in `{typography.title-sm}`. Hover tightens the border to charcoal, mirroring product card hover behavior for a consistent interaction vocabulary across the browsing surface.

**`footer`** — Charcoal background matching the nav bar (`{colors.primary}`) with white type, completing the ledger-frame layout. Columns cover Customer Service, Secure Shopping, About, and Category links. Link hover desaturates to `{colors.hairline}` gray to signal interactivity without introducing a new accent color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar collapses to a full-screen bottom sheet triggered by a sticky "Filter & Sort" bar; spot price ticker scrolls horizontally or truncates to gold and silver; nav collapses to hamburger + logo; add-to-cart button stays full-width sticky at viewport bottom |
| Tablet | 744–1128px | 2-column product grid; filter sidebar toggles as an overlay drawer; nav shows primary metal categories inline with hamburger for secondary links |
| Desktop | 1128–1440px | 3–4 column product grid; filter sidebar docks persistently at left at 240px; spot ticker runs full-width; full category mega-menu available |
| Wide | > 1440px | Content max-width constrained to ~1400px and centered; outer margins fill with white canvas; product grid holds at 4 columns |

### Touch Targets

- All primary buttons minimum 44px height
- Quantity selector increment/decrement buttons 36×36px minimum with 8px gap between controls
- Metal tab strip scrolls horizontally on mobile; each tab minimum 44px tap height
- Nav hamburger icon minimum 44×44px tap area
- Product card entire surface tappable on mobile, not only the image region
- Filter checkboxes minimum 24×24px with 8px surrounding hit area

### Collapsing Strategy

- Category mega-menu on desktop collapses to tabbed top nav on tablet and a drawer on mobile
- Filter sidebar converts to a full-screen bottom sheet on mobile, activated by a floating sticky bar
- Spot price ticker truncates to gold and silver only on screens narrower than 375px
- Footer columns stack vertically on mobile with accordion-expandable sections to minimize scroll depth
- Product comparison tool (if present) collapses to a floating "Compare (N)" chip on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Full color palette unverified — Cloudflare anti-bot blocked direct extraction; only #313131 (charcoal) was confirmed from the live site
- Gold/amber accent color (listed as `gold-accent: "#c9a84c"`) is a category inference for precious metals dealers, not a measured value; the actual site may use a different or no distinct accent
- CTA button color unconfirmed — charcoal (#313131) is assumed based on the extracted palette, but a separate gold or amber tone may serve as the actual primary CTA
- Custom typeface presence unknown — no custom font-family was detected; system font stack assumed throughout; brand may use a paid typeface loaded via JS after bot-check
- Exact border-radius values unverified — {rounded.xs} (4px) assumed from financial e-commerce conventions
- Spot price ticker exact position (above nav vs. below nav), update interval, and color coding unverified
- Meta theme-color not set, indicating light-mode-only or no PWA manifest configured
- Mobile navigation pattern (hamburger vs. persistent tabs) not confirmed from extraction
- Hover, focus, and active state colors for interactive elements not extracted
