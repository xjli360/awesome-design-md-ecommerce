---
version: alpha
name: "Radtke Sports"
source_url: "https://radtkesports.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep navy-purple (#221155) anchors Radtke Sports' palette — an unusual choice for an autographs dealer that might default to team reds and stadium blues, but one that reads as vault-serious: collectible-grade, slightly ceremonial, the color of velvet display cases. Against that foundation, electric blue (#3858e9) fires across every primary action — buy buttons, cart CTAs, active navigation states — with an urgency that mirrors a live auction countdown rather than a passive browse. A sports red (#cc1818) punctuates sale flags and alert states, while amber (#f0b849) signals trophy-tier items and premium highlights, the closest this palette comes to a trophy gleam. Forest green (#4ab866) carries authentication confirmation marks — the verified-signature visual that is the brand's core trust signal. Type runs entirely on the system stack (Arial, Helvetica, -apple-system) at standard weights, because the product photography does the heavy lifting: signed helmets, framed jerseys, and authenticated lithographs need clear hierarchy, not typographic showmanship. Spacing is compact by collector-site convention — product grids run dense so shoppers can scan inventory efficiently, the way a collector flips through a binder. Rounded corners are minimal: cards sit at {rounded.xs} to {rounded.sm}, keeping the UI squared off in a way that echoes the rigid frames, protective cases, and slabs that physical collectibles arrive in. The overall register is sports-shop utility with a vault-grade presentation layer — no decorative flourishes, just tight hierarchy, authentication trust signals in green and amber, and enough visual gravity in that navy-purple foundation to make every signed item feel genuinely significant and provenance-worthy.

colors:
  primary: "#221155"
  primary-active: "#1a0d40"
  primary-disabled: "#8b85a8"
  cta: "#3858e9"
  cta-active: "#183ad6"
  cta-disabled: "#a0b0f5"
  accent-red: "#cc1818"
  accent-red-deep: "#710d0d"
  accent-gold: "#f0b849"
  accent-green: "#4ab866"
  accent-teal: "#0e5376"
  accent-purple: "#7a00df"
  ink: "#212121"
  body: "#3f3f3f"
  muted: "#757575"
  muted-light: "#949494"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#fafafa"
  surface-dark: "#1e1e1e"
  on-primary: "#ffffff"
  on-cta: "#ffffff"
  on-dark: "#ffffff"
  sale-bg: "#cc1818"
  sale-text: "#ffffff"
  auth-bg: "#4ab866"
  auth-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  category-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hoverBackgroundColor: "{colors.cta-active}"
  button-primary-disabled:
    backgroundColor: "{colors.cta-disabled}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
    hoverBackgroundColor: "{colors.surface-soft}"
  button-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hoverBackgroundColor: "{colors.primary-active}"
  button-sm:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 34px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.cta}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
    placeholderColor: "{colors.muted-light}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 58px
    borderBottom: "none"
    logoArea: 180px
  nav-utility-bar:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 34px
  nav-link-hover:
    textColor: "{colors.accent-gold}"
    transition: color 0.15s ease
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "4/3"
    padding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.primary}"
    hoverBorderColor: "{colors.cta}"
    hoverShadow: "0 2px 8px rgba(56,88,233,0.15)"
  product-card-badge:
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
    rounded: "{rounded.xs}"
    typography: "{typography.badge}"
  sale-badge:
    backgroundColor: "{colors.sale-bg}"
    textColor: "{colors.sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  auth-badge:
    backgroundColor: "{colors.auth-bg}"
    textColor: "{colors.auth-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 420px
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    subtitleColor: "{colors.accent-gold}"
    ctaButton: "{components.button-primary}"
    overlayGradient: "linear-gradient(135deg, {colors.primary} 0%, {colors.cta} 100%)"
    padding: "{spacing.xxl} {spacing.xl}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.category-label}"
    rounded: "{rounded.xs}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
    borderFocus: "2px solid {colors.cta}"
    height: 44px
    iconColor: "{colors.muted}"
    submitButtonBackgroundColor: "{colors.cta}"
    submitButtonTextColor: "{colors.on-cta}"
    submitButtonRounded: "{rounded.xs}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-light}"
    hoverTextColor: "{colors.cta}"
  price-block:
    currentPriceTypography: "{typography.price-display}"
    currentPriceColor: "{colors.primary}"
    originalPriceTypography: "{typography.price-sm}"
    originalPriceColor: "{colors.muted}"
    originalPriceDecoration: line-through
    salePriceColor: "{colors.accent-red}"
  authentication-seal:
    backgroundColor: "{colors.surface-soft}"
    border: "2px solid {colors.accent-green}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    iconColor: "{colors.accent-green}"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.accent-gold}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "3px solid {colors.cta}"
    padding: "{spacing.xxl} 0"
  pagination:
    activeBackgroundColor: "{colors.cta}"
    activeTextColor: "{colors.on-cta}"
    inactiveBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.button-sm}"
    height: 36px
    minWidth: 36px
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.primary}"
    optionTypography: "{typography.body-sm}"
    optionColor: "{colors.body}"
    activeOptionColor: "{colors.cta}"
    dividerColor: "{colors.hairline-soft}"

## Components

### Buttons

**`button-primary`** — Electric blue (#3858e9) fill with white uppercase label at 15px/700 weight, 4px radius, 44px tall. Pressing darkens to `{colors.cta-active}` (#183ad6); disabled state fades to `{colors.cta-disabled}`. Used for all primary commerce actions: Add to Cart, Buy Now, Search submit.

**`button-dark`** — Deep navy-purple (#221155) fill variant for hero sections and dark-background contexts where the electric blue would have insufficient contrast against the background. Hovers to `{colors.primary-active}` (#1a0d40). Keeps the same uppercase label treatment as `button-primary`.

**`button-secondary`** — White canvas with a 2px solid navy-purple border and navy-purple uppercase label. Used for secondary actions — Wishlist, Share, Compare. Hover fills background with `{colors.surface-soft}`. Same 44px height as primary for visual alignment in button groups.

**`button-sm`** — Compact 34px electric blue button at 13px/700 uppercase for inline actions: grid-level "Add to Cart," filter apply, quick-view triggers.

### Navigation

**`nav-utility-bar`** — A slim 34px strip above the main nav in `{colors.primary-active}` (#1a0d40) carrying shipping thresholds, authentication guarantees, and account links in 12px white caption type. Functions as a trust-signal banner before the user reaches product content.

**`nav-bar`** — 58px deep navy-purple (#221155) bar with white nav links at 14px/600. Hover state shifts link color to amber (#f0b849), a warm contrast that reads as "trophy" against the dark field. Logo sits in a 180px reserved left zone. Cart, account, and search icons appear on the right in white.

### Product Cards

**`product-card`** — Near-white (#fafafa) card with a 1px `{colors.hairline}` border and 4px radius, housing a 4:3 image followed by a compact content block: product title in 15px/600, price in 20px/700 navy-purple. Hovering sharpens the border to electric blue and adds a subtle blue-tinted box shadow, signaling interactivity without animation overhead. Badge slots (sale, authentication) float absolutely over the image top-left.

**`sale-badge`** — Sports red (#cc1818) filled pill at 11px uppercase tracking for discount percentage or "SALE" labels. Sits atop product card images at `{spacing.sm}` inset.

**`auth-badge`** — Green (#4ab866) filled badge for "AUTHENTICATED" or "CERTIFIED" status marks. Critical trust signal in a category where provenance is the product. Appears on card images and expanded product detail.

### Hero

**`hero`** — 420px minimum-height section with a diagonal gradient from `{colors.primary}` to `{colors.cta}`, giving the navy-to-electric-blue sweep of a stadium lighting effect. Headline runs at 36px/700 in white; subheadline drops to 20px/700 in amber (#f0b849). Primary CTA button overlays the gradient. Used for sport-category landings and featured-signing promotions.

### Authentication Seal

**`authentication-seal`** — A distinct component unique to the memorabilia category: a `{colors.surface-soft}` panel with a 2px green border and green checkmark icon, carrying 15px/600 label ("Certificate of Authenticity") and 12px caption text with certificate number or issuer name. Placed prominently on product detail pages below the price block — the single most important trust conversion element on the page.

### Search

**`search-bar`** — Full-width input with 2px hairline border, sharpening to 2px electric blue on focus. A square electric-blue submit button (matching `{rounded.xs}`) sits flush to the right edge. Placeholder text in `{colors.muted}`. Deployed in the nav bar on desktop and as a full-width block on mobile category pages.

### Filters

**`category-chip`** — Compact uppercase label chips for sport (Baseball, Football, Basketball), category (Jerseys, Helmets, Photos), and player filters. Default state is `{colors.surface-soft}` with hairline border; active state inverts to navy-purple fill with white text. Stack horizontally on desktop, scroll horizontally on mobile.

**`filter-sidebar`** — Desktop-only panel with hairline border and section headings in navy-purple 15px/600. Checkboxes for category, sport, price range, authentication type. Collapses into a modal drawer on tablet and below.

### Footer

**`footer`** — Dark surface (#1e1e1e) with a 3px electric blue top border as the only dividing accent. White body text at 14px; links in `{colors.hairline}` (#e0e0e0) warming to amber on hover. Columns cover: About, Customer Service, Authentication Partners, Social links. Navy-purple is avoided in the footer — the dark surface creates its own gravity without re-using the primary brand hue.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero reduces to 280px min-height; filter sidebar becomes full-screen drawer; category chips scroll horizontally; utility bar collapses to a single line or hides |
| Tablet | 744–1128px | 2-column product grid; nav shows logo + primary links + icons, secondary links move to hamburger overflow; hero 360px; filter sidebar becomes a horizontal chip row above grid |
| Desktop | 1128–1440px | 3–4 column product grid; full nav bar + utility bar; filter sidebar panel fixed-left 220px; hero full 420px with split layout (text left, feature image right) |
| Wide | > 1440px | Max content width 1400px centered; product grid can expand to 4–5 columns; hero gains more horizontal breathing room; footer columns widen |

### Touch Targets
- All buttons minimum 44×44px on mobile (button-sm sits at 34px on desktop only; expands to 44px on touch viewports)
- Nav icons minimum 44px tap zones via padding compensation
- Pagination controls minimum 44px height on mobile
- Filter chip height expands from 30px desktop to 40px on touch

### Collapsing Strategy
- Filter sidebar → full-screen modal drawer triggered by a "Filters" button bar above the grid
- Utility bar → hidden on mobile to preserve vertical space for product content
- Multi-level navigation → hamburger menu with accordion-style sport/category sub-menus
- Breadcrumb → truncates intermediate segments to ellipsis on narrow viewports, keeping first and last crumb visible
- Authentication seal → collapses from horizontal layout to stacked vertical layout at mobile breakpoint

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-custom typeface detected; all typography inferred from system font stacks (Arial, Helvetica, -apple-system). If Radtke Sports uses a licensed display font, it is loaded via JavaScript or third-party CDN not captured in extraction.
- No meta theme-color was set, so mobile browser chrome color is undefined — likely defaults to white or system.
- Platform is non-Shopify; specific CMS or framework token structure (grid gutters, breakpoint values, component variants) not extractable from static hints.
- Exact button border-radius values not confirmed from live rendering — {rounded.xs} (4px) is inferred from the squared-off sports-shop visual convention in the color palette.
- Dark mode support status unknown; color system above assumes light-mode-only.
- Logo dimensions and lockup (wordmark, icon, or combination mark) not available from extraction.
- Specific authentication partner badges (PSA, JSA, Beckett, Fanatics Authentic) may carry their own color rules that override the brand system in authentication seal contexts.
- Exact grid gutter width and sidebar breakpoint pixel values not captured.
