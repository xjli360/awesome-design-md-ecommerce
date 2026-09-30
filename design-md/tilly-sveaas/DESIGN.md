---
version: alpha
name: "Tilly Sveaas"
source_url: "https://www.tillysveaas.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Two typefaces divide the site into two distinct grammars: Gaisyr Light handles every editorial moment — campaign headlines, collection introductions, long-form copy — while Gaisyr Mono claims the product layer entirely, appearing on prices, material descriptors, nav links, and filter labels. The split gives pages the feel of a printed archive where story and commerce are typographically separated rather than stylistically blurred. The palette is stranger than it first looks: a cool seafoam mint (#e6f7f4) functions as the brand's ambient field color, surfacing behind editorial text sections and campaign imagery, which is an atypical move for demi-fine — most brands in this space stay in warm creams or pale blush. A champagne gold (#dec292) grounds the mint in something mineral and warm, appearing on material chips and plating callouts. Calls-to-action run near-black charcoal (#272727), reading at high contrast without the harshness of pure black. Steel-blue gray (#b1b7c3) and its desaturated sibling (#999ea8) carry secondary text, placeholder copy, and form states, giving the UI a cool-toned neutrality that sits comfortably beside the mint. Corners lean sharp — `{rounded.xs}` on buttons and `{rounded.none}` on cards — with no pill shapes in the brand-facing UI, a choice that echoes the geometry of precise metalwork. Navigation is typographically minimal: Gaisyr Mono in fine uppercase tracking across a slim top bar, no icons, product categories accessed through clean horizontal links. Deep navy (#121f36) appears in the darkest overlay and footer states. Photography carries the retail weight; the design system's job is to stand aside and not interrupt it.

colors:
  primary: "#272727"
  primary-active: "#1c1c1c"
  primary-disabled: "#cecece"
  ink: "#272727"
  body: "#4c4c4c"
  muted: "#888888"
  muted-light: "#9b9b9b"
  hairline: "#e8e8e8"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  seafoam: "#e6f7f4"
  gold: "#dec292"
  cream: "#fef3e2"
  navy: "#121f36"
  steel-blue: "#b1b7c3"
  steel-muted: "#999ea8"
  scrim: "#171722"
  error: "#ea0202"
  error-bg: "#f8d7da"
  error-text: "#721c24"
  success: "#155724"
  success-bg: "#d4edda"
  warning-bg: "#fff3cd"
  warning-text: "#856404"

typography:
  display-xl:
    fontFamily: "'Gaisyr Light', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Gaisyr Light', Georgia, serif"
    fontSize: 34px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Gaisyr Light', Georgia, serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.15px
  title-md:
    fontFamily: "'Gaisyr Light', Georgia, serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Gaisyr Light', Georgia, serif"
    fontSize: 15px
    fontWeight: 300
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gaisyr Light', Georgia, serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: 0
  product-title:
    fontFamily: "'Gaisyr Light', Georgia, serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'Gaisyr Mono', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Gaisyr Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gaisyr Mono', 'Courier New', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gaisyr Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  label-mono:
    fontFamily: "'Gaisyr Mono', 'Courier New', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  caption:
    fontFamily: "'Gaisyr Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    padding: 14px 28px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.steel-muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.product-title}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.seafoam}"
    textColor: "{colors.navy}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 60vh
  editorial-band:
    backgroundColor: "{colors.seafoam}"
    textColor: "{colors.navy}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  material-chip:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  plating-badge:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.body}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  collection-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    titleTypography: "{typography.title-md}"
    itemPriceTypography: "{typography.price}"
    borderLeft: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.muted-light}"
    headingTypography: "{typography.label-mono}"
    bodyTypography: "{typography.caption}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Near-black fill (#272727) at `{rounded.xs}` (2px), sitting nearly square-cornered. Typography is Gaisyr Mono uppercase at 0.12em tracking, which reads as precise and restrained rather than loud. Hover darkens to `{colors.primary-active}` (#1c1c1c); disabled state drops fill to light gray `{colors.primary-disabled}` with `{colors.muted}` text. Height is 44px rather than the more common 48px, keeping the button proportionally slim.

**`button-secondary`** — White canvas with a 1px solid ink border, identical mono uppercase typography and 2px radius. The solid/outline pairing appears side-by-side on product pages for primary versus secondary actions (e.g. "Add to Bag" + "Save to Wishlist"). Active state uses `{colors.surface-soft}` background rather than a color shift.

**`button-tertiary`** — Transparent background with underlined Gaisyr Mono ink text. Deployed for low-hierarchy actions like "Continue Shopping" or "View All" within editorial sections. No border, no hover fill — only the underline communicates interactivity.

### Nav Bar

**`nav-bar`** — 56px height, white canvas, thin bottom hairline. Wordmark renders centered in Gaisyr Light at `{typography.display-sm}`. Navigation links sit in horizontal flanks at `{typography.nav-link}` — fine Gaisyr Mono uppercase with generous tracking — with no icons and no visible dropdown until hover. On mobile, the links collapse behind a minimal drawer; the wordmark remains centered with a line-icon trigger.

### Product Card

**`product-card`** — No border radius, flush square edges. Portrait image at 3:4 ratio fills the card top; product name in Gaisyr Light `{typography.product-title}` sits immediately below with `{spacing.sm}` gap; price renders in Gaisyr Mono `{typography.price}` on the line below. No quick-add overlays, no hover state fills — the card is entirely image-forward and relies on photography to communicate finish and weight.

### Material Chip & Plating Badge

**`material-chip`** — Zero-radius rectangular label on champagne gold (#dec292) background. Gaisyr Mono uppercase at `{typography.label-mono}` in ink text. Used on product pages to denote metal type (Sterling Silver, 18ct Gold Vermeil). The gold fill communicates plating warmth without an icon. **`plating-badge`** is the cream (#fef3e2) variant for non-gold finishes such as oxidised silver, keeping the label format consistent while visually differentiating the metal family.

### Hero

**`hero`** — Full-bleed section with seafoam mint (#e6f7f4) background and deep navy (#121f36) text. Headline at `{typography.display-xl}` (Gaisyr Light, 52px, weight 300); body at `{typography.body-md}`. Minimum 60vh height with `{spacing.section}` top and bottom padding. The seafoam-on-navy pairing is the clearest brand signal on the site — no other section uses this combination.

### Editorial Band

**`editorial-band`** — A narrower content section that reuses the seafoam background (#e6f7f4) with navy text for campaign copy or material storytelling placed between collection grids. Headline at `{typography.display-md}`, body at `{typography.body-md}`, vertical padding at `{spacing.xxl}`. Functions as a visual breath between product rows rather than a full-height hero.

### Collection Filter

**`collection-filter`** — Sharp-cornered filter tags in `{colors.surface-soft}` that invert to `{colors.ink}` fill with `{colors.on-primary}` text on selection. Gaisyr Mono uppercase at `{typography.button-sm}`. 1px hairline border on unselected state. No animated transition — state changes are immediate, consistent with the brand's preference for hard edges over soft transitions.

### Cart Drawer

**`cart-drawer`** — Slides in from right at 400px width, white canvas, 1px hairline left border as the only container demarcation. Drawer title in Gaisyr Light `{typography.title-md}`; individual item prices in Gaisyr Mono `{typography.price}`. No rounded treatment on the container. Checkout CTA inside the drawer follows `button-primary` spec.

### Footer

**`footer`** — Near-black (#171722) background with `{colors.surface-soft}` body text. Column headings in Gaisyr Mono uppercase at `{typography.label-mono}`; links and legal text at `{typography.caption}`. Link hover state shifts to `{colors.muted-light}`. Padding is `{spacing.section}` top and bottom with `{spacing.xl}` horizontal gutters.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to centered wordmark + line-icon drawer; hero min-height drops to 50vh; cart drawer becomes full-width overlay |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible in compressed horizontal form; hero retains seafoam band at reduced padding |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with category links; hero at full 60vh; editorial bands switch to text-image split layout |
| Wide | > 1440px | Content width capped ~1400px with auto side margins; hero imagery can run full-bleed behind a contained centered text column |

### Touch Targets

- All buttons minimum 44px height for tap accessibility
- Nav links padded to minimum 44px tap zone on mobile
- Product cards link the full image and title block, not just the text label
- Material chips and filter tags padded to minimum 36px touch height on mobile

### Collapsing Strategy

- Navigation links move behind a slide-in drawer below 744px; scrim overlay uses `{colors.scrim}` at partial opacity
- Collection filter bar converts to horizontally scrollable strip on mobile, no wrapping
- Material chips stack below product title on narrow viewports rather than sitting inline
- Cart drawer becomes full-screen width below 744px; 400px fixed width resumes at tablet and above
- Editorial band switches from side-by-side text-image to stacked text-over-image on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Gaisyr is a contemporary typeface with limited public documentation; numeric font-weight for "Light" is inferred as 300 and could not be confirmed from extraction
- Exact button height (44px vs 48px) was not directly measurable from static hints — 44px is an inference from the brand's proportional preference
- Whether Gaisyr Mono appears in all nav contexts or only specific product/label zones could not be fully confirmed from font-stack extraction alone
- No explicit hover color token for gold (#dec292) material chip was confirmed — behavior is inferred from common demi-fine patterns
- Animation and transition timing values are not extractable from static hints
- Grid gutter widths and exact max-content-width breakpoints not confirmed
- Logo mark format (SVG wordmark vs text render), precise sizing, and kerning adjustments not confirmed
- Mobile nav drawer design (close button position, overlay opacity, animation direction) not confirmed from extraction
- The colors #d4edda, #383d41, #d0d0d0, #d1d5db appear to be Shopify theme system defaults (success/neutral states) rather than brand-authored tokens
