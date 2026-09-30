---
version: alpha
name: "Stones Throw Records"
source_url: "https://www.stonesthrow.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record label and shop where the primary voltage is a burnt orange #ff8900 that reads like a vintage amp pilot light — warm, slightly faded, and unmistakably analog in a digital storefront. That orange carries every add-to-cart button, every badge, every active nav state, while the rest of the system stays in a tight gray spectrum (#212121 ink, #323232 body, #9b9b9b muted, #d8d8d8 hairline) on a #f9f9f9 canvas that feels like uncoated paper stock. The typography runs LL Brown and General Sans Variable — a pairing that splits the difference between a 1970s jazz LP liner note and a modern sans-serif utility — with display heads at 24–28px in weight 600 and body copy at 14–16px in weight 400. Product cards use soft {rounded.sm} corners, but the search bar and primary buttons go full pill ({rounded.full}), creating a tension between the angular album art grid and the friendly, grabable CTAs. The shop runs on Shopify, so checkout flows inherit a secondary palette of #00d084 (green) and #0693e3 (blue) from payment widgets, but the brand's own world stays in orange, gray, and white — a deliberate restraint that lets the album covers do the color work.

colors:
  primary: "#ff8900"
  primary-active: "#ff8200"
  primary-disabled: "#fc7f1b"
  ink: "#212121"
  body: "#323232"
  muted: "#9b9b9b"
  muted-soft: "#d9d9d9"
  hairline: "#d8d8d8"
  hairline-soft: "#e5e5e5"
  canvas: "#f9f9f9"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-new: "#ff9f00"
  badge-sale: "#e94c89"
  accent-green: "#00d084"
  accent-blue: "#0693e3"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'LL Brown', 'General Sans Variable', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'LL Brown', 'General Sans Variable', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'LL Brown', 'General Sans Variable', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'General Sans Variable', 'LL Brown', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'General Sans Variable', 'LL Brown', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'General Sans Variable', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'General Sans Variable', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'General Sans Variable', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  badge:
    fontFamily: "'General Sans Variable', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'General Sans Variable', 'LL Brown', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'General Sans Variable', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  link:
    fontFamily: "'General Sans Variable', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'LL Brown', 'General Sans Variable', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
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
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    opacity: 0.5
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 0
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 48px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a full-pill orange button on white canvas. Uses `{colors.primary}` (#ff8900) background with white text at 14px weight 600. On hover, shifts to `{colors.primary-active}` (#ff8200) — a slightly deeper orange. Disabled state drops opacity to 0.5 and uses `{colors.primary-disabled}` (#fc7f1b). The pill shape (`{rounded.full}`) gives the button a grabable, friendly feel that contrasts with the sharp edges of album art grids.

**`button-secondary`** — An outlined or ghost variant for less prominent actions. White background (`{colors.canvas}`) with `{colors.ink}` text, same pill shape and sizing as primary. Active state fills with `{colors.surface-soft}` (#f0f0f0). Used for "View Cart", "Continue Shopping", and secondary checkout actions.

**`button-text`** — A text-only button with no background or border. Uses `{colors.primary}` for the text color and `{typography.button-md}`. Reserved for inline actions like "Clear filters" or "See all" links within sections.

### Cards
**`product-card`** — The core product display unit for vinyl, merch, and digital releases. White background (`{colors.surface-card}`) with `{rounded.sm}` (8px) corners. The card contains a square-ratio product image (typically album art), followed by a title using `{typography.title-sm}` in `{colors.ink}`, and a price using `{typography.body-sm}` in `{colors.muted}` (#9b9b9b). No shadow by default — the card relies on the contrast between the white surface and the `{colors.canvas}` (#f9f9f9) page background.

**`badge-new`** and **`badge-sale`** — Small uppercase labels pinned to the top-left corner of product cards. `badge-new` uses `{colors.badge-new}` (#ff9f00) — a lighter orange variant — while `badge-sale` uses `{colors.badge-sale}` (#e94c89), a pink that signals discount. Both use `{typography.badge}` at 11px weight 700 with 0.5px letter spacing, uppercase, on `{rounded.xs}` (4px) corners.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height on white background. Contains the Stones Throw wordmark (typically in `{colors.ink}`), a set of uppercase nav links using `{typography.nav-link}` at 13px weight 500 with 0.5px letter spacing, and a search icon. Active nav links render in `{colors.primary}` (#ff8900), inactive in `{colors.muted}` (#9b9b9b). On mobile, the nav collapses into a hamburger menu.

**`nav-link-active`** and **`nav-link-inactive`** — State tokens for navigation items. Active state uses the brand orange; inactive uses muted gray. No underline or background — the color shift alone signals the current section.

### Forms
**`text-input`** — Standard text input for search, email signup, and checkout fields. White background with `{rounded.sm}` (8px) corners, 40px height, and `{typography.body-sm}` at 14px. Border uses `{colors.hairline}` (#d8d8d8) by default. Focus state would use `{colors.primary}` border (not extracted — noted in Known Gaps).

**`search-bar`** — The site search input, rendered as a pill shape (`{rounded.full}`) on `{colors.surface-soft}` (#f0f0f0) background. 40px height with 10px 20px padding. The pill shape distinguishes it from standard form inputs and aligns with the button system's rounded language.

### Hero
**`hero-section`** — Full-width hero banner used on the homepage and collection pages. White background with `{colors.display-xl}` (28px weight 600) for the headline and 64px vertical padding. Typically features a full-bleed background image (album art or artist photo) with the headline overlaid. No rounded corners — the hero extends edge-to-edge to maximize visual impact.

### Footer
**`footer`** — Dark footer on `{colors.ink}` (#212121) background with `{colors.muted-soft}` (#d9d9d9) text at `{typography.body-sm}` (14px). Contains links to Shop, Artists, About, and social channels. 48px vertical padding. Links use `{typography.link}` and inherit the muted-soft color, with hover state likely shifting to white (not extracted — see Known Gaps).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 items per row), nav collapses to hamburger, hero text reduces to `{typography.display-md}` (24px), buttons go full-width, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid (3-4 items per row), nav links visible but condensed, hero maintains `{typography.display-xl}` with reduced padding (48px) |
| Desktop | 1128–1440px | Three-column product grid (4-5 items per row), full nav bar, hero at 64px padding, standard button widths |
| Wide | > 1440px | Max-width container at 1440px with centered content, product grid expands to 5-6 columns, hero may include parallax or larger imagery |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (per Apple HIG) — `button-primary` and `button-secondary` at 44px, `text-input` and `search-bar` at 40px (slightly under but standard for text fields)
- Nav links have minimum 48px tap area on mobile (padding expands hit zone)
- Product card images are tappable as links — no minimum size enforced beyond the card's image ratio

### Collapsing Strategy
- Top nav collapses from horizontal link list to hamburger icon at < 744px
- Product grid collapses from 4-5 columns to 2 columns at tablet, then 1-2 columns at mobile
- Footer link columns stack vertically on mobile (from 3-4 columns to single column)
- Hero section reduces vertical padding from 64px to 48px on tablet, 32px on mobile
- Search bar may collapse to icon-only on mobile, expanding to full input on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only `button-primary` and `button-secondary` hover states were reliably extracted. Hover colors for links, nav items, and product cards are inferred from brand patterns but not confirmed from the live site.
- **Focus states**: No focus ring colors or styles were extracted. Standard practice would use `{colors.primary}` with a 2px offset ring, but this is unconfirmed.
- **Error states**: Form validation colors (error text, error borders) were not extracted. The extracted palette includes #e94c89 (pink) which could serve as an error accent, but this is speculative.
- **Dark mode**: No dark mode palette was extracted. The footer uses `{colors.ink}` (#212121) as a dark surface, but a full dark mode system (with inverted text, muted backgrounds, etc.) is not documented.
- **Sub-brand palettes**: Stones Throw may have artist-specific or release-specific color treatments (e.g., for Madlib, J Dilla, or Mndsgn albums) that diverge from the core system. These are not captured.
- **Checkout colors**: The extracted palette includes Shopify payment widget colors (#00d084 green, #0693e3 blue, #0757fe blue) that are not part of the brand system. These are noted but excluded from the primary palette.
- **Font weights**: Only weight 400, 500, 600, and 700 were observed. Weight 300 (light) and 800 (heavy) may exist but were not extracted.
- **Spacing scale**: The spacing tokens are based on common 8px/4px grid patterns inferred from the site's layout. Exact padding/margin values for specific components (e.g., product card internal spacing, grid gaps) were not extracted and may vary.
- **Animation/transition**: No transition durations, easing curves, or animation patterns were extracted. The brand likely uses subtle fades or slides, but specifics are unknown.
