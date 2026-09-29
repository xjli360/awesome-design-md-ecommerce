---
version: alpha
name: "R&R Games"
source_url: "https://rnrgames.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A game publisher that uses a sharp lime-green #97c300 as its primary voltage — not the warm amber of a family-game night or the deep blue of strategy titles, but a high-frequency, almost acidic green that reads as modern and competitive. That green sits against a near-white canvas of #f6f6f6 and #f9f9f9, with secondary accents in gold (#eebe00, #e8af00) for badges and callouts, and a coral-red #ff4f60 for urgency signals like sale tags or limited-time banners. The typography runs Roboto at clean, readable weights — no display black or ultra-bold; the brand trusts game photography and bold color blocks rather than typographic hierarchy to carry energy. Buttons use the lime green with white text, corners at {rounded.sm} (8px) — soft enough to feel approachable, not pill-shaped like a social app. The extracted palette reveals a heavy reliance on grays (#8c8c8c, #444444, #eeeeee) for structural elements: hairline borders, muted body text, and secondary backgrounds. This is a system built for a catalog of dozens of game titles — the design recedes enough to let each product's box art and photography lead, while the green and gold provide consistent brand grip across product cards, nav bars, and CTAs. The footer and legal areas drop into darker grays (#2c2c2c) and deep green (#045304), creating a clear visual basement. There is no hero gradient, no large display type — the brand's design language is modular, grid-based, and built for scale across hundreds of SKUs.

colors:
  primary: "#97c300"
  primary-active: "#7c9a16"
  primary-disabled: "#d0e68a"
  ink: "#2c2c2c"
  body: "#444444"
  muted: "#8c8c8c"
  muted-soft: "#aaaaaa"
  hairline: "#d0d0d0"
  hairline-soft: "#e7e7e7"
  canvas: "#f9f9f9"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#eebe00"
  accent-gold-active: "#e8af00"
  accent-coral: "#ff4f60"
  accent-coral-active: "#e04550"
  deep-green: "#045304"
  footer-bg: "#2c2c2c"
  footer-text: "#ababab"
  badge-new: "#ffcd46"

typography:
  display-xl:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary-active}"
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-gold-active:
    backgroundColor: "{colors.accent-gold-active}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "2px solid {colors.accent-coral}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "12px 16px 4px"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 600
    padding: "0px 16px 12px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-award:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the brand's lime green #97c300 with white text. On hover, it shifts to a deeper green #7c9a16. The disabled state drops to a pale green #d0e68a, maintaining the brand color while signaling non-interactivity. Used for "Add to Cart," "Shop Now," and primary form submissions.

**`button-secondary`** — An outlined variant with a white fill and a 2px green border. On hover, the background fills with the soft canvas tone #f6f6f6 and the border shifts to the active green. Used for "Learn More" and secondary actions alongside primary buttons.

**`button-gold`** — A warm accent button using #eebe00 gold with dark ink text. On hover it deepens to #e8af00. Used sparingly for premium calls-to-action, limited-edition game launches, or special promotions where the green would feel too aggressive.

### Cards
**`product-card`** — A clean white card with a soft hairline border and no padding at the container level (image fills top edge). On hover, the border turns green and a subtle box shadow lifts the card. The title uses 16px semibold Roboto, and the price appears in the primary green at 16px weight 600. Used for every game in the catalog grid.

**`badge-new`**, **`badge-sale`**, **`badge-award`** — Small uppercase labels that sit at the top-left corner of product images. The "New" badge uses warm yellow #ffcd46, the "Sale" badge uses coral #ff4f60, and award badges use gold #eebe00. All badges share the same 11px bold uppercase typography and 4px corner radius.

### Navigation
**`nav-bar`** — A 64px white bar with a soft bottom border. Navigation links use 15px medium-weight Roboto; the active link gets a green underline and green text, while inactive links sit in muted gray #8c8c8c. The logo sits left-aligned, and the search bar sits right-aligned.

**`nav-link-active`** — Active state with green text and a 2px green bottom border. No background fill — the brand avoids nav tabs in favor of underlined text links.

**`nav-link-inactive`** — Muted gray text with no underline. On hover, text shifts to the ink color #2c2c2c.

### Forms
**`text-input`** — Standard input fields with a white background, 1px hairline border, and 8px corner radius. On focus, the border becomes a 2px green line. Error states swap the border to coral #ff4f60. Height is 44px with 10px vertical padding for comfortable touch targets.

**`search-bar`** — A pill-shaped search field with a soft gray background #f6f6f6 and a 1px hairline border. On focus, it expands to a white background with a 2px green border. The pill shape differentiates it from standard form inputs and signals a lightweight, discoverable action.

### Footer
**`footer`** — A dark basement using #2c2c2c background with light gray text #ababab. Links hover to white. The footer is divided into columns with semibold white headings. Deep green #045304 appears in the copyright bar or secondary footer area, adding a subtle brand anchor at the very bottom of the page.

### Hero
**`hero-banner`** — A full-width section using the soft canvas background #f6f6f6 with large 28px bold display type. The primary CTA button sits at 48px height with generous 14px/32px padding. No gradient or image overlay — the hero relies on product photography and the green CTA for visual energy.

### Category Tags
**`category-tag`** — Small pill-shaped tags for filtering games by category (e.g., "Strategy," "Family," "Party"). Inactive tags use a soft gray background with muted text; active tags flip to green background with white text. Height is 32px with 6px/16px padding.

### Pagination
**`pagination-button`** — Numbered page buttons with a white background and 1px hairline border. The active page uses the green fill. Used at the bottom of catalog pages for browsing multiple game pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero padding reduces to 32px; search bar moves below nav; category tags wrap to 2 rows |
| Tablet | 744–1128px | Nav shows full links; product cards in 2-column grid; hero uses 24px display type; category tags in single scrollable row |
| Desktop | 1128–1440px | Product cards in 3-column grid; full nav with search bar; hero uses 28px display type; footer columns in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; additional whitespace on hero sides |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Category tags at 32px height are below the 44px recommendation — these are secondary interactions and appear in scrollable strips where tap accuracy is less critical
- Search bar at 40px height is slightly below recommendation; the pill shape and generous width compensate
- Product card links (title, image, button) each have independent 44px+ tap targets within the card

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px; the logo and cart icon remain visible
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 to 2 at tablet, then to a single column at mobile
- Category tag strips become horizontally scrollable on mobile rather than wrapping to multiple rows
- Hero banner collapses from side-by-side text/image to stacked layout below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns — the extracted CSS did not include `:hover` pseudo-classes for all elements
- Error and validation styling for forms (error messages, success states, helper text) was not present in extracted data
- Dark mode is not supported — the palette has no dark-mode equivalents for cards, text, or borders
- Dropdown menus (for account, cart, or mobile nav) were not captured — their background, shadow, and animation tokens are unknown
- The extracted font list only includes "Roboto" and "emporium-icons" — the icon font's usage and available glyphs are undocumented
- Modal/overlay styling (for quick-view, newsletter signup, or cart drawer) was not extracted
- The extracted hex list includes #146ff8 (a blue) and #ffff99 (a pale yellow) that may belong to third-party widgets or checkout integrations — these were excluded from the brand palette
- Animation tokens (transition durations, easing curves, micro-interactions) were not present in extracted data
- The brand's secondary green #045304 appears only once in the extracted list and may be a deep-green accent for footer or legal areas — its exact usage is inferred
- No typography scale beyond Roboto was detected; heading sizes and weights are inferred from common e-commerce patterns rather than extracted CSS
