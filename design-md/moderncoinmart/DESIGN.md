---
version: alpha
name: "ModernCoinMart"
source_url: "https://www.moderncoinmart.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The single confirmed color from ModernCoinMart's live site is #116600 — a deep forest green that sits closer to oxidized copper patina than to mint-fresh currency ink, darker and more organic than institutional money-green. That one anchor does considerable work in a trust-dense vertical where coin grading certificates, precious-metal spot prices, and authentication seals must project expertise over aspiration. Product cards rely on high-resolution coin photography against neutral backgrounds, letting the metallic surfaces — gold, silver, platinum, bronze — supply the warmth and luster; the interface stays restrained, with the forest green reserving itself for primary CTAs, category headers, and nav signifiers. Navigation is encyclopedic by necessity: coins are organized by metal type, denomination, mint year, grade, and country of origin, demanding a multi-tier dropdown structure with deep filter faceting. A spot-price ticker for gold and silver runs near the top of the experience — a live data ribbon that marks the site as a serious trading destination rather than a hobbyist storefront. Grade badges (PCGS, NGC, MS70, PR70) overlay product imagery, carrying more trust weight than any decorative element could. Typography likely runs a serif stack for display and a clean sans-serif for UI chrome — a split common in numismatics to signal tradition and expert curation — though no font families were confirmed during extraction. The green primary at full saturation communicates transactional urgency while muted surfaces keep precious-metal photography front and center: the coins are the hero, not the chrome.

colors:
  primary: "#116600"
  primary-active: "#0d4f00"
  primary-disabled: "#a8d4a0"
  primary-light: "#e8f5e4"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gold-accent: "#b8860b"
  gold-light: "#f5e6a3"
  silver-accent: "#8c8c8c"
  spot-up: "#1a7a1a"
  spot-down: "#c0392b"
  badge-certified: "#003366"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  spot-ticker:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.25px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoHeight: 40px
  nav-bar-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1:1"
    padding: "{spacing.base}"
    priceTypography: "{typography.price-display}"
  spot-price-ticker:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spot-ticker}"
    upColor: "{colors.spot-up}"
    downColor: "{colors.spot-down}"
    height: 36px
    padding: "0 {spacing.base}"
  grade-badge:
    backgroundColor: "{colors.badge-certified}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: none
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    height: 44px
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
  trust-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
    minHeight: 400px
  metal-swatch:
    gold:
      backgroundColor: "{colors.gold-light}"
      borderColor: "{colors.gold-accent}"
      textColor: "{colors.ink}"
      typography: "{typography.caption}"
      rounded: "{rounded.xs}"
    silver:
      backgroundColor: "{colors.surface-soft}"
      borderColor: "{colors.silver-accent}"
      textColor: "{colors.ink}"
      typography: "{typography.caption}"
      rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    linkColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Solid `{colors.primary}` forest-green fill with white type at `{typography.button-md}`, 44px height, and `{rounded.sm}` corners. Active state deepens to `{colors.primary-active}`; disabled state pulls to a washed sage `{colors.primary-disabled}` that preserves the green signal without implying clickability. Primary CTA for Add to Cart, Buy Now, and all checkout progression steps.

**`button-secondary`** — White background with a `{colors.primary}` border and matching text, paired directly beneath or beside `button-primary` in two-CTA layouts (e.g., Add to Cart / Add to Wishlist). Hover fills with `{colors.primary-light}` to signal interactivity without full inversion.

### Navigation
**`nav-bar`** — White canvas at 64px height with a `{colors.hairline}` bottom border. Links use `{typography.nav-link}` — a weighted sans-serif needed to survive a deep category tree covering Gold, Silver, Platinum, Copper, Collectibles, Graded Coins, and Bullion. Above the main nav, `nav-bar-top-strip` renders as a full-width `{colors.primary}` band containing trust signals, a phone number, and spot-price proximity links in `{typography.caption}` white text — the green strip functions as an implicit brand stamp on every page load.

### Search
**`search-bar`** — A prominent 44px input with a `{colors.primary}` submit button flush to the right edge. Coin searches require keyword precision across year, mint mark, denomination, and grade, so the field is generously padded and always visible in the header. Focus shifts the border from `{colors.hairline}` to a 2px `{colors.primary}` ring.

### Product Card
**`product-card`** — Centered square coin photography in a 1:1 aspect ratio framed by a `{colors.hairline}` border and `{rounded.sm}` corners on a white `{colors.surface-card}` ground. Price renders in `{typography.price-display}` — a monospaced stack that signals real market data rather than lifestyle pricing. When a coin carries a certified grade, a `grade-badge` sits in the upper corner of the image, anchoring authenticity directly to the product visual.

### Spot Price Ticker
**`spot-price-ticker`** — A full-width dark ribbon (`{colors.ink}` background) at 36px displaying live spot prices for gold, silver, platinum, and palladium. Price movement renders in `{colors.spot-up}` (green) or `{colors.spot-down}` (red) per conventional financial data standards. The monospaced `{typography.spot-ticker}` ensures numeric columns stay optically aligned as values update.

### Grade Badge
**`grade-badge`** — A small navy (`{colors.badge-certified}`) pill in all-caps `{typography.badge}` with `{rounded.xs}` corners. Displays the certification body (PCGS, NGC) and numeric grade (MS70, PR70, PF69). This component is unique to the numismatic vertical and carries outsized trust weight — users comparing listings scan for grade badges before reading titles.

### Category Chips
**`category-chip`** and **`category-chip-active`** — `{rounded.full}` pill filters for browsing by metal type, coin series, or decade. Inactive: `{colors.surface-soft}` fill with `{colors.hairline}` border. Active: solid `{colors.primary}` fill with `{colors.on-primary}` text. Deployed in horizontal scroll rows on mobile and as a sidebar facet block on desktop.

### Metal Swatch
**`metal-swatch`** — A pair of small labeled swatches (gold / silver variants) used in product detail and category headers to indicate the underlying metal. Gold swatch draws from `{colors.gold-light}` and `{colors.gold-accent}`; silver from `{colors.surface-soft}` and `{colors.silver-accent}`. Typography uses `{typography.caption}` to keep the swatch label compact.

### Trust Badge
**`trust-badge`** — A light-green tinted chip (`{colors.primary-light}` fill, `{colors.primary}` border) in `{typography.caption}` for authentication signals: "PCGS Certified," "NGC Graded," "Price Match Guarantee." Positioned near the cart CTA on product pages or in a horizontal trust rail above the footer.

### Hero Banner
**`hero-banner`** — A full-width dark section (`{colors.ink}` background) with `{typography.display-xl}` headline in `{colors.on-primary}`. Metallic coin photography or gradient overlays provide warmth against the dark ground. Minimum height 400px; `{spacing.section}` padding on all sides. Used for category landing pages (Gold Coins, Silver Eagles) and promotional campaigns.

### Footer
**`footer`** — Dark `{colors.ink}` ground with `{colors.muted-soft}` body copy and `{colors.on-primary}` links, bookending the predominantly white content area. Section headings in `{typography.title-sm}` serif. Standard columns: Shop by Metal, Graded Coins, Sell to Us, Customer Service, About MCM.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category chips in horizontal scroll row; spot ticker collapses to gold + silver only; nav becomes hamburger with full-screen flyout |
| Tablet | 744–1128px | Two-column product grid; filter sidebar becomes collapsible drawer; spot ticker shows all four metals; search bar remains visible in header |
| Desktop | 1128–1440px | Three- to four-column product grid; persistent left-rail filter panel with facets; full multi-tier dropdown nav; spot ticker pinned above nav |
| Wide | > 1440px | Content max-width ~1400px centered; five-column grid option; spot ticker may expand to include currency conversion rates |

### Touch Targets
- All primary and secondary buttons minimum 44px height
- Category chips minimum 36px height on mobile
- Nav hamburger icon minimum 44×44px tap area
- Entire product card surface is tappable, not just the title text
- Grade badge is display-only, not interactive; no tap target needed

### Collapsing Strategy
- Multi-tier nav collapses to hamburger at < 1024px; top categories become a slide-in drawer with accordion sub-levels
- Filter facets collapse to a modal bottom sheet on mobile, triggered by a fixed "Filter" pill
- Spot price ticker abbreviates from full-metal ribbon to a compact two-metal row on mobile
- Product detail layout (image column + purchase sidebar) stacks vertically below 768px, with the purchase sidebar dropping below the image carousel

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex value (#116600) was confirmed during extraction; all other palette tokens (gold accent, silver accent, spot-up/down colors, badge navy, surface tints) are inferred from category convention and are not verified
- No font families were extractable; the serif/sans-serif split in typography is inferred from numismatic industry norms and is not confirmed — the actual site may use a single sans-serif stack throughout
- Exact button radius, component sizing, and spacing scale could not be confirmed; values follow reasonable e-commerce defaults
- No meta theme-color was present; the site likely loads visual tokens via JavaScript or is behind anti-bot protection that prevented full extraction
- Spot price ticker refresh interval, metal ordering, and currency denomination (USD only vs. multi-currency) were not confirmed
- Whether the site uses a proprietary design system, a CSS framework (Bootstrap, Tailwind), or a hybrid is unknown
- Gold and silver accent colors are inferred from precious-metals category convention, not extracted from the live site
