---
version: alpha
name: "Topps"
source_url: "https://www.topps.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The product grid at Topps operates like a dealer's sorted slab vault — #bd2426 red holds every primary CTA, promotional badge, and the wordmark itself, while #163959 navy absorbs the masthead and hero banners, together reconstructing the two-tone border geometry that has printed on cardboard since the 1952 baseball series. Sport taxonomy gets its own chromatic lanes: stadium greens (#9bca3e, #bada7a) flag baseball and series product lines, stadium oranges (#f68b1f, #ee730a) bracket basketball and soccer drops, and a saturated #0051c3 blue marks premium authenticated pieces. The type stack is pure system — Arial and Helvetica Neue without a proprietary face — so the design leans on fontWeight 700 across display and button scales, uppercase tracking on sport labels and badge text, and a restrained #272727 ink that keeps card photography from competing with body copy. Cards render at a 2:3 portrait ratio with {rounded.sm} corners echoing the physical product's clipped edges; the page background sits at #ebebeb so card art pops without requiring a dark inversion. The persistent search bar and faceted filter rail reflect a catalog running hundreds of thousands of SKUs across vintage, current series, and digital releases — the UI's primary job is filtering, not brand storytelling, and the component hierarchy reflects that priority. Price callouts in {colors.primary} red and sale overlays in {colors.sport-orange} create a secondary urgency signal that collectors read without reading as generic discount-retail. Navigation runs white type on {colors.navy} at fontWeight 700, treating the top bar as a sport-vertical staging area where card grades and product categories are the primary taxonomy.

colors:
  primary: "#bd2426"
  primary-active: "#521010"
  primary-disabled: "#de5052"
  ink: "#272727"
  body: "#404040"
  muted: "#737373"
  muted-soft: "#bfbfbf"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  navy: "#163959"
  navy-mid: "#2f7bbf"
  accent-blue: "#62a1d8"
  accent-blue-bright: "#0051c3"
  sport-green: "#9bca3e"
  sport-green-light: "#bada7a"
  sport-green-dark: "#516b1d"
  sport-orange: "#f68b1f"
  sport-orange-alt: "#ee730a"
  sport-orange-dark: "#904b06"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  sport-label:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
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
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.navy-mid}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.navy}"
    rounded: "{rounded.xs}"
    padding: 10px 40px 10px 14px
    height: 42px
    iconColor: "{colors.muted}"
    submitButtonBackgroundColor: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
  nav-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: none
    logoColor: "{colors.on-primary}"
    activeIndicatorColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "2/3"
    padding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    hoverBorder: "1px solid {colors.navy-mid}"
    badgeOffset: "{spacing.xs}"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  sport-badge:
    backgroundColor: "{colors.sport-green}"
    textColor: "{colors.sport-green-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.sport-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  price-tag:
    textColor: "{colors.primary}"
    typography: "{typography.price-display}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
    borderHover: "1px solid {colors.navy-mid}"
    backgroundHover: "{colors.canvas}"
  series-banner:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl} {spacing.section}"
  sport-nav-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.sport-label}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    activeBackgroundColor: "{colors.navy}"
    activeTextColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    dividerColor: "#2f4a63"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Red (#bd2426) fill with white uppercase type and a tight {rounded.xs} radius. Hover deepens to `primary-active` (#521010); disabled washes to `primary-disabled` (#de5052) while retaining shape. Height is 44px with generous 24px horizontal padding so the label reads at a glance even in dense card-grid contexts.

**`button-secondary`** — Navy (#163959) fill, same geometry as primary. Used for secondary purchase actions like "Add to Wishlist" or sport-vertical navigation CTAs that should anchor without pulling focus away from the primary red.

**`button-ghost`** — Transparent fill with a 2px #bd2426 border and matching red text. Used for filter resets, "View All" links, and secondary actions on dark hero surfaces where a filled button would compete with the background image.

### Search Bar

**`search-bar`** — Full-width input with a 1px #dedede border at rest; border transitions to #163959 navy on focus. A magnifier icon sits at 14px left inset in {colors.muted}; the right edge holds a compact #bd2426 submit button. The bar is persistent in the desktop masthead and collapses to an icon tap on mobile.

### Navigation

**`nav-bar`** — #163959 navy bar at 60px height. Sport-vertical links (Baseball, Basketball, Football, Soccer, Wrestling) run white fontWeight 700 at 14px with 0.3px letter-spacing. Active items receive a #bd2426 underline indicator. Logo locks to the left; cart and account icons sit right in white.

**`sport-nav-pill`** — Horizontal scrollable row of pill chips below the primary nav on mobile and as a secondary filter row on desktop. Inactive: {colors.surface-soft} background with {colors.body} text. Active: {colors.navy} fill with white text. Uppercase 10px tracking emphasizes sport-vertical identity.

### Cards

**`product-card`** — White surface with a 1px #dedede border and {rounded.sm} corners. Card image occupies the top 2:3 portrait slot; below it sits a title in fontWeight 700 at 15px, seller rating line in {colors.muted} at 12px, and a price callout in {colors.primary} at 22px bold. Hover sharpens the border to #2f7bbf. Badge overlays (SALE, NEW, HOT) sit at the top-left corner of the image at {spacing.xs} offset.

### Badges

**`sport-badge`** — #9bca3e green with #516b1d dark-green text, uppercase 11px. Maps the card's sport-vertical at a glance. A complementary orange variant (`new-badge`) uses #f68b1f for limited-release drops.

**`sale-badge`** — Solid #bd2426 fill, white uppercase 11px. Positioned as a flag overlay on the card image top-left. Signals price reduction without requiring the user to parse the price line.

### Hero

**`hero-banner`** — Full-bleed #163959 navy field with headline in `display-xl` (40px, fontWeight 700, white) and a supporting body line in `body-md`. Primary CTA button uses #bd2426 fill with white uppercase label. Minimum 480px height on desktop to give card artwork room to breathe as a secondary visual layer.

### Promotional Bands

**`series-banner`** — #62a1d8 accent-blue band used for mid-page series callouts (e.g., "2024 Topps Chrome Baseball"). Headline at `display-md` in white; sub-label in `body-sm`. No border radius — edge-to-edge strips the layout of decorative framing so the product name carries full visual weight.

### Footer

**`footer`** — #163959 navy field divided by a subtle #2f4a63 rule into columns for Sport, Help, Company, and Social links. Column heads in `title-sm` white fontWeight 700; links in `body-sm` white at normal weight with 0.85 opacity at rest, full opacity on hover.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column card grid (2-up); search bar collapses to icon tap expanding to full-width overlay; sport-nav-pill scrolls horizontally; nav-bar reduces to hamburger + logo + cart |
| Tablet | 744–1128px | 3-column card grid; search bar visible inline at 60% width; sport-nav-pill visible as row; full nav links in dropdown |
| Desktop | 1128–1440px | 4-column card grid; persistent search bar in masthead; sport-vertical nav full-width; hero-banner activates secondary card artwork layer |
| Wide | > 1440px | Grid locks to max 1440px container centered; hero imagery expands edge-to-edge behind constrained content column; section padding scales to {spacing.section} on both sides |

### Touch Targets

- All interactive badges and category chips use a minimum 44px tap target height even when visually smaller
- Sport-nav-pill chips maintain 36px height on mobile with 8px horizontal padding expanded by invisible tap area
- Product card tap target covers full card surface; price and title are not separately tappable
- Nav icons (cart, account, search) minimum 44×44px

### Collapsing Strategy

- Primary nav collapses sport-vertical links into a full-screen drawer at < 744px; drawer opens with a slide-in from left at 85vw
- Hero-banner secondary card artwork (decorative) is hidden below 744px to reduce visual noise
- Series-banner copy truncates to one line headline only below 744px; sub-label hidden
- Footer columns stack vertically on mobile into an accordion pattern; each column head is a tap-to-expand trigger

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site was blocked by Cloudflare anti-bot at extraction time; font and token data reflects framework defaults rather than live Topps CSS — a full extraction pass after unblocking may surface a custom typeface or proprietary display font
- No meta theme-color tag found; browser chrome color behavior on mobile is unspecified
- Canvas white (#ffffff) is inferred as the default surface; it was not directly extracted from the palette
- Exact border-radius values for cards and inputs are estimated at 4–8px based on visual brand conventions; not confirmed from CSS source
- Sport-coded color assignments (which hex maps to which sport vertical) are inferred from palette ordering and brand knowledge — confirmed sport-to-hex pairing requires live CSS inspection
- Animation durations, easing curves, and transition behavior for hover states and drawer open/close are not captured
- Typography for authenticated/graded-card detail pages (PSA/BGS grade display, population report tables) not scoped — likely a distinct type hierarchy from the storefront
- Dark-mode or high-contrast variant not confirmed; no evidence of a `prefers-color-scheme` implementation in the extracted hints
