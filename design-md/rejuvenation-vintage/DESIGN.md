---
version: alpha
name: "Rejuvenation Vintage"
source_url: "https://www.rejuvenation.com/shop/vintage"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Antique brass (#896b27) does the work that most retail brands assign to a hero gradient — every primary CTA, price callout, and hover accent draws from the same oxidized-metal tone, placing the digital storefront in direct conversation with the cast-iron and hand-rubbed finishes it actually sells. The base palette is a period typographer's choice: near-black charcoal (#1a1818, #2b3033) borrowed from the ink of pre-war hardware catalogues, against which the brass reads warm and deliberate rather than decorative. A brick-red (#d04727) surfaces on urgent callouts and editorial accent headers, recalling the kiln-fired tones of Arts & Crafts tilework — a rare appearance that keeps it from reading as a generic clearance flag. Type runs in Gotham, a geometric American grotesque that wears surprisingly well against 1910–1940 hardware forms; its even stroke widths and closed apertures feel less Silicon Valley than they do WPA-era civic signage. Display sizes lean heavy at 36–48px/700 to anchor editorial category headers, while body copy settles at 16px/400 for unhurried browsing of condition notes and provenance details. Corner radii are minimal throughout — product cards at {rounded.xs}, input fields at {rounded.sm}, and only pill-shaped filter chips use {rounded.full} — a restraint that suits a shop where the goods predate modern consumer interface design by a century. Silver-gray (#b9babb) handles hairlines and secondary text, the visual equivalent of aged patina on a white-ground label. The overall system reads more like a museum catalogue than a trend-driven marketplace: deliberate, unhurried, and grounded in the authority of objects with documented histories.

colors:
  primary: "#896b27"
  primary-active: "#6e5420"
  primary-disabled: "#c9a96e"
  accent-brick: "#d04727"
  accent-brick-active: "#b33920"
  ink: "#1a1818"
  body: "#2b3033"
  muted: "#6b6c6e"
  hairline: "#b9babb"
  hairline-soft: "#dddcdc"
  canvas: "#ffffff"
  surface-soft: "#f5f2ed"
  surface-card: "#faf8f5"
  surface-warm: "#ede8e0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  price: "#1a1818"
  badge-new: "#896b27"
  badge-sale: "#d04727"

typography:
  display-xl:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-uppercase:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge-text:
    fontFamily: "'Gotham', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
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
    padding: 14px 28px
    height: 48px
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
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    border: "1.5px solid {colors.body}"
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
  button-brick:
    backgroundColor: "{colors.accent-brick}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "1.5px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "4/5"
    padding: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 16px rgba(26,24,24,0.08)"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-text}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-text}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-estate:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-text}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xxl}"
  category-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    padding: "{spacing.xl} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderRight: "1px solid {colors.hairline-soft}"
    labelTypography: "{typography.label-uppercase}"
    optionTypography: "{typography.body-sm}"
    width: 240px
  price-tag:
    textColor: "{colors.price}"
    typography: "{typography.price-display}"
    strikethroughColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-uppercase}"
    padding: "{spacing.section} 0"
  condition-label:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderLeft: "2px solid {colors.primary}"
    paddingLeft: "{spacing.sm}"

## Components

### Buttons
**`button-primary`** — Brass-gold (#896b27) fill with uppercase Gotham at 14px/600, tracked 0.5px, on {rounded.xs} corners that read period-appropriate rather than modern-soft. Active state deepens to #6e5420; disabled fades to {colors.primary-disabled}. The uppercase treatment is intentional: it echoes the label typography on pre-war hardware bins and catalogue index cards, tying the action to the product aesthetic rather than generic SaaS button conventions.

**`button-secondary`** — White canvas with a 1.5px charcoal ({colors.body}) border and matching uppercase type; used for secondary actions such as "Save to List" or "Compare." On hover, background warms to {colors.surface-soft} and the border tightens to {colors.ink}, signaling interactivity without introducing a color that would compete with the brass primary.

**`button-brick`** — Brick-red (#d04727) fill, same corner and type treatment as `button-primary`. Reserved for editorial urgency — promotional callouts, time-limited availability, or clearance section headers. Its rarity in the layout preserves its signal strength; overuse collapses it to visual noise.

**`filter-chip`** — The only {rounded.full} component in the system. Inactive chips carry a hairline border on white; active chips invert fully to {colors.ink} fill with {colors.on-dark} text. Used for faceted browsing by era, finish, material, or price range. The pill shape contrasts deliberately against the square-cornered product grid, visually grouping filter state as a separate interactive layer.

### Product Card
**`product-card`** — Portrait-ratio (4:5) image flush to the card edge above a compact metadata strip: item name in {typography.title-sm}, price in {typography.price-display}, and a one-line condition or era note in {typography.caption} warm gray. Cards use {rounded.xs} with a {colors.hairline-soft} border that firms and gains a 4px drop shadow on hover. Badge overlays (`badge-new`, `badge-sale`, `badge-estate`) sit flush top-left with zero radius — pressed hard against the image corner like a real price sticker, not floated softly over the photo.

### Navigation
**`nav-bar`** — 64px white bar with a {colors.hairline-soft} bottom rule; navigation labels in {typography.nav-link} track at 0.3px for legibility at small sizes. Active category underlines with a 2px {colors.primary} stroke, maintaining the brass-as-primary-signal convention. The custom `rejuvenation-icons` icon font handles category glyphs throughout; no SVG sprites.

### Hero
**`hero-banner`** — Full-bleed on {colors.body} charcoal with editorial photography, {typography.display-xl} title, and a {typography.body-md} subtitle. Minimum 480px tall on desktop. A single `button-primary` CTA floats against the dark field, where brass reads luminous without a competing highlight — the dark ground amplifies the metallic primary in a way a white field cannot.

### Badges
Zero-radius badge tokens are a deliberate period reference — price tags on vintage hardware don't have rounded corners. Brass ({colors.badge-new}) signals new arrivals; brick-red ({colors.badge-sale}) signals sale or clearance; near-black ({colors.ink}) signals curated estate provenance. All three use {typography.badge-text} at 10px/700/tracked 1px uppercase, sized to sit legibly on a product image without obscuring subject matter.

### Footer
**`footer`** — Near-black (#1a1818) field with on-dark type, {colors.hairline} gray links that warm to {colors.primary} brass on hover. Column headers in {typography.label-uppercase} (11px, tracked 1.2px) are the footer's most formally strict typographic moment: no ornamentation, just spaced columns and a warm hover state that echoes the CTA brass without confusing section labels for buttons.

### Filter Sidebar
**`filter-sidebar`** — 240px fixed-width panel, label headers in {typography.label-uppercase}, option rows in {typography.body-sm}, separated from the product grid by a {colors.hairline-soft} right border. A brass-colored checkbox check mark signals selection state without introducing a new surface color.

### Condition Labels
**`condition-label`** — Provenance and grading notes in {typography.caption} with a 2px {colors.primary} left border rule. This small component signals archival care: the brass stripe marks a curatorial annotation rather than a marketing claim, consistent with how labels appear in auction catalogues.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar becomes bottom-sheet drawer triggered by a filter button with applied-count badge; nav collapses to hamburger; hero min-height drops to 320px with reduced {spacing.lg} padding |
| Tablet | 744–1128px | Two-column product grid; filter sidebar toggles as an overlay panel; top nav shows primary categories with overflow into a "More" dropdown |
| Desktop | 1128–1440px | Three-column product grid with persistent 240px filter sidebar; full nav bar with hover-activated category mega-menus |
| Wide | > 1440px | Four-column product grid; content max-width caps at 1440px with symmetric side gutters; hero text stack gains additional leading space |

### Touch Targets
- All buttons minimum 44px height on mobile
- Filter chips minimum 36px height tap target
- Nav links minimum 44px tap area with full-row hit region
- Product cards use full-card tap affordance, not image-only

### Collapsing Strategy
- Filter sidebar collapses to a labeled sheet with applied-filter count badge on mobile
- Category sub-navigation collapses to a horizontally scrollable strip pinned below the main nav on tablet
- Hero reflows to {typography.display-md} scale on mobile with {spacing.lg} vertical padding
- Breadcrumb truncates to parent + current page on mobile; full path visible from tablet up
- Condition-label left-border rule is preserved at all breakpoints as a key visual signal

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; mobile browser chrome color is undetermined
- Gotham weight variants (Book, Medium, Bold) not confirmed from extraction; specific weights inferred from typical Rejuvenation brand usage patterns
- Product-card image aspect ratio not verified from live grid extraction; 4:5 inferred from catalog photography conventions
- Hover and focus state animation durations and easing curves not extracted
- No confirmed dark-mode palette; all tokens assume light-mode only
- Custom `rejuvenation-icons` glyph set not catalogued; icon names and codepoints unknown
- Surface-soft (#f5f2ed) and surface-warm (#ede8e0) warm-white values are aesthetic inferences, not directly extracted from the live site
- Promotional banner treatment beyond badge-level (color, height, placement) not confirmed
- The page extraction returned an error page rather than a live product grid, so component spacing measurements could not be verified against rendered layout
