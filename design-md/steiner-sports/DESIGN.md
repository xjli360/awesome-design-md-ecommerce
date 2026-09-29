---
version: alpha
name: "Steiner Sports"
source_url: "https://www.steinersports.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every product page on Steiner Sports functions as a certificate of authenticity first and a shopping experience second — the design language is built around credentialing: serial-number holograms, league-official lockups, and the dense, championship-banner typography that communicates provenance rather than aspiration. The primary palette anchors on a deep navy approaching near-black (#0e1a2b), punctuated by a championship red (#c8102e) that routes every primary CTA, sale badge, and authentication callout. A muted gold (#c9a84c) surfaces on premium tiers — Hall of Fame editions, Yankee Stadium seat collections, rookie-year signings — functioning as a rarity signal rather than a general accent. Canvas stays white with a light warm-gray surface (#f5f5f5) for card grids, keeping photography of jerseys, bats, and signed helmets as the primary visual event. Typography skews toward compressed, all-caps headline stacks with tight tracking — the kind of weight an arena scoreboard uses — while body copy stays in a utilitarian sans-serif that does not compete with product imagery. The product card is the core workhorse: a ratio-locked photograph of the item, an athlete name in bold title text, a sport/team badge, a price in red, and an authenticated-by ribbon along the lower edge. Authentication is a product feature, not fine print: "100% Authentic" banners and hologram-badge graphics appear in the component layer at roughly the same visual weight as product titles. Navigation carries a top-bar mega-menu segmented by sport (MLB, NFL, NBA, NHL, Soccer) and by format (Autographs, Game-Used, Photos, Framed), with a secondary strip for clearance and featured athlete drops. The overall mood is trophy-case gravity — serious about provenance, leaning into the collector's trust that a serialized sticker and a league hologram confer — rather than the lifestyle-forward softness of a modern DTC apparel brand.

colors:
  primary: "#c8102e"
  primary-active: "#a30d25"
  primary-disabled: "#f0a0ac"
  ink: "#0e1a2b"
  body: "#1f2d3d"
  muted: "#5a6a7a"
  hairline: "#dde1e6"
  hairline-soft: "#eeeff1"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#0e1a2b"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  gold: "#c9a84c"
  gold-light: "#f0d98e"
  badge-sale: "#c8102e"
  badge-new: "#1a6b2e"
  badge-authenticated: "#c9a84c"
  star: "#c9a84c"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Arial Black', 'Impact', 'Franklin Gothic Heavy', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Arial Black', 'Franklin Gothic Heavy', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.3px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Arial Black', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase
  price-display:
    fontFamily: "'Arial Black', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  athlete-name:
    fontFamily: "'Arial Black', Arial, sans-serif"
    fontSize: 17px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
  xl: 16px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.ink}"
    padding: 10px 22px
    height: 44px
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.on-dark}"
    padding: 10px 22px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocused: "2px solid {colors.ink}"
    padding: 10px 14px
    height: 42px
    placeholderColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    iconColor: "{colors.muted}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.none}"
      width: 48px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 52px
    borderBottom: "3px solid {colors.primary}"
  nav-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    border: "2px solid {colors.primary}"
    shadow: "0 4px 16px rgba(0,0,0,0.18)"
    sectionHeadColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
    imageRatio: "4/3"
    athleteNameTypography: "{typography.athlete-name}"
    priceTypography: "{typography.price-sm}"
    teamTagTypography: "{typography.badge-label}"
    authRibbonColor: "{colors.gold}"
    authRibbonText: "{colors.ink}"
    hoverShadow: "0 6px 20px rgba(0,0,0,0.14)"
    hoverBorderColor: "{colors.primary}"
    padding: "{spacing.sm}"
  badge-authenticated:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-game-used:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.gold}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    border: "1px solid {colors.gold}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    ctaButton: "{components.button-primary}"
    overlayScrim: "linear-gradient(to right, rgba(14,26,43,0.85) 40%, transparent 100%)"
    minHeight: 480px
  authentication-callout:
    backgroundColor: "{colors.surface-soft}"
    borderLeft: "4px solid {colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    iconColor: "{colors.gold}"
  sport-category-tile:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.sm}"
    border: "2px solid transparent"
    hoverBorder: "2px solid {colors.primary}"
    overlayScrim: "rgba(14,26,43,0.55)"
    labelPosition: bottom-center
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    originalPriceTypography: "{typography.body-sm}"
    originalPriceColor: "{colors.muted}"
    textDecoration: line-through
  athlete-spotlight:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    nameTypography: "{typography.display-md}"
    statTypography: "{typography.body-md}"
    accentColor: "{colors.gold}"
    padding: "{spacing.xxl}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.button-md}"
    headingColor: "{colors.gold}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Flat red (#c8102e) fill with white uppercase text at 700 weight and a minimal 2px radius, echoing the no-nonsense rectangular forms seen on arena scoreboard graphics. Hover darkens to `{colors.primary-active}` (#a30d25) with no transition delay; disabled state washes to a pale rose `{colors.primary-disabled}`. Height is locked at 44px with generous horizontal padding.

**`button-secondary`** — White fill with a 2px ink border and the same uppercase typographic treatment as primary, used for secondary purchase actions (Add to Wishlist, Compare) and modal cancel targets. On dark backgrounds, `button-secondary-dark` substitutes a transparent fill with a white border.

**`button-ghost`** — Transparent background with red text, used for inline "View All" and "See More" links within category grids. No border, minimal padding.

### Navigation
**`nav-top-strip`** — A 32px-tall red band at the absolute top, carrying shipping threshold notices and login/account links in small caption type. This strip is the first authentication-trust signal the page delivers.

**`nav-bar`** — Deep navy (#0e1a2b) background, 52px tall, with a 3px red bottom border anchoring the bar against the canvas. Sport categories (MLB, NFL, NBA, NHL, Soccer) render in all-caps 700-weight nav-link type in white. A search input occupies the right side with a red submit button flush to its trailing edge.

**`nav-mega-menu`** — Drops down on sport-category hover with a white panel bordered in red, organized into columns: Athletes, Teams, Product Format (Autographs, Game-Used, Framed, Photos). Section headers use `{colors.primary}` in `{typography.title-md}`. The shadow (0 4px 16px at 18% opacity) lifts the menu clearly off the product grid.

### Product Card
**`product-card`** — A 1px hairline-bordered card with 4px radius and a soft drop-shadow. The photograph occupies a 4:3 locked aspect ratio at the top; below it sits the athlete name in `{typography.athlete-name}` (Arial Black, 17px), the team/sport tag in `{typography.badge-label}` uppercase at muted color, and the price in red `{typography.price-sm}`. An authentication ribbon in gold `{colors.gold}` runs horizontally above the price row bearing "100% Authentic" in `{typography.badge-label}`. On hover the border flips to `{colors.primary}` and the shadow deepens.

### Badges
**`badge-authenticated`** — Gold fill with dark ink text; the primary trust signal appearing on every authenticated item. **`badge-game-used`** — Dark navy background with gold text and a 1px gold border; signals a higher provenance tier (actual game-used equipment). **`badge-sale`** — Red fill, white text, used on clearance and promotional events. **`badge-new`** — Green fill, white text, for new arrivals and recent athlete signings.

### Hero Banner
**`hero-banner`** — Full-width dark cinematic panel (minimum 480px tall) using a left-to-right scrim over athlete photography. Headline sits at `{typography.display-xl}` in all-caps white, sub-headline at `{typography.display-sm}`, followed by a primary CTA button. The scrim fades from 85% navy on the left to transparent on the right so athlete imagery reads cleanly.

### Authentication Callout
**`authentication-callout`** — A soft-gray card with a 4px gold left border, used within PDP pages to explain the authentication process (who signed it, what league hologram is affixed, COA serial number). The gold border signals premium certification without using a badge.

### Sport Category Tiles
**`sport-category-tile`** — Square grid tiles for sport navigation (MLB, NFL, NBA, etc.) using a dark overlay scrim over action photography. Sport name renders centered at bottom in `{typography.display-sm}` white. Hover lifts the border from transparent to a 2px red stroke, providing a clear selection affordance.

### Price Block
**`price-block`** — Sale price in `{typography.price-display}` (Arial Black, 22px) in `{colors.primary}` red. Original price in `{typography.body-sm}` with `text-decoration: line-through` in `{colors.muted}`. This stack conveys urgency on clearance items without needing a separate badge.

### Footer
**`footer`** — Deep ink (#0e1a2b) background with a 4px red top border. Column headings in gold `{colors.gold}` uppercase `{typography.button-md}`; body links in white `{typography.body-sm}` that shift to red on hover. Includes league-partner logo strip (MLB, NFL, NBA, NHL official partner lockups) as a trust-credentialing band above the legal copy row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + sport-icon strip; hero shrinks to 280px with text overlay at bottom; badges remain full-size; price block stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level sport tabs without mega-menu dropdown; hero at 380px; athlete spotlight collapses to single row |
| Desktop | 1128–1440px | Three- or four-column product grid; full mega-menu nav; hero at 480px; authentication callout sidebar visible on PDP |
| Wide | > 1440px | Grid caps at four columns centered in a max-width container (~1400px); hero may extend to five columns with side-by-side product spotlight |

### Touch Targets
- All CTA buttons minimum 44px tall
- Nav-bar sport links minimum 44px tap target height despite 52px bar (vertical centering provides clearance)
- Product card touch target covers the full card face; "Add to Cart" secondary button inside card is explicitly 44px
- Badge tap area padded to minimum 32×24px for filter interactions

### Collapsing Strategy
- Mega-menu nav collapses to a slide-in drawer on mobile, with sport icons as visual anchors rather than text tabs
- Authentication callout moves from PDP sidebar into an inline collapsible accordion on mobile
- Footer four-column layout stacks to two columns on tablet, single column on mobile with accordions per section
- Hero text overlay transitions from left-aligned desktop positioning to bottom-anchored overlay on mobile
- Athlete spotlight section reflows from horizontal band to stacked card on tablet and below

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted** — the site returned an Access Denied response; all hex values above are drawn from brand knowledge of Steiner Sports' documented visual identity (navy/red/gold scheme). They should be verified against live site inspection.
- **No fonts extracted** — font stack is inferred from the sports-memorabilia category aesthetic; Steiner Sports may use a licensed display font or a webfont not captured here. Arial Black is a safe fallback placeholder.
- **Exact border-radius values** unknown; 2–6px range assumed from category conventions; actual site may use 0px (fully square) for a harder, more authoritative register.
- **Specific authentication ribbon component geometry** (width, exact gold hex, hologram graphic dimensions) not available without live DOM inspection.
- **League-partner logo strip** dimensions and layout in the footer are estimated; official placement rules from MLB/NFL/NBA licensing agreements may constrain these.
- **Breakpoints** are estimated; actual Steiner Sports breakpoints should be read from the site's CSS media queries.
- **Sale/discount badge logic** (threshold for displaying, stacking order with Game-Used and Authenticated badges) is inferred from typical sports-memorabilia retail patterns.
