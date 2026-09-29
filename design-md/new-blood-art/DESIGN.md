---
version: alpha
name: "New Blood Art"
source_url: "https://newbloodart.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Didot 06 — the optical-size letterpress revival drawn for fine-print display — opens every artist page at New Blood Art as if the screen were a gallery proof sheet: high contrast, unhurried, insisting on the serif's ink traps even at 48px. Around it the rest of the site runs a strict two-temperature system. Near-black (#272727) ink on white canvas handles the everyday layer — prices, dimensions, edition counts — while a warm sandy accent (#dbac86), the color of raw linen or a manila envelope light-struck through a window, marks every moment of collector intent: add-to-basket buttons, featured-artist pull-quotes, price-on-request labels. Nothing else in the palette is warm. Light-gray hairlines (#dde0e3) divide filter panels from browse grids; a pale-gray surface (#f3f4f6) lifts artwork cards off the page without competing with the pigment on them. Gotham Narrow compresses the utilitarian layer — medium tags, size filters, edition type labels — into tight widths that surrender maximum horizontal space to the artwork itself. A deep gallery green (#194321), borrowed from institution wall-paint rather than any digital convention, surfaces on sold confirmations and sustainability signals, lending those states the weight of physical consequence rather than a traffic-light readout. Corners are held close to straight — {rounded.sm} on cards, {rounded.xs} on badges and inputs — because the artworks supply all the organic irregularity the page needs. The browse experience is built around a persistent left filter rail (price range, medium, size, orientation, subject), reflecting an assumption that collectors arrive with a wall in mind rather than a vague desire to scroll. Artwork cards hover to reveal a frosted quick-view overlay with a sandy "Add to Cart" CTA at {rounded.xs}, keeping aggression low. The overall register is that of a well-designed contemporary-art fair catalogue: serif authority for the names, compressed geometric sans for the data, and one warm temperature accent that says — without urgency — that you can own this.

colors:
  primary: "#dbac86"
  primary-active: "#c49a72"
  primary-disabled: "#eddfc8"
  on-primary: "#272727"
  accent-green: "#194321"
  ink: "#272727"
  body: "#4b5563"
  muted: "#6d6d6d"
  muted-soft: "#9ca3af"
  hairline: "#dde0e3"
  hairline-soft: "#e5e7eb"
  canvas: "#ffffff"
  surface-soft: "#f3f4f6"
  surface-card: "#f0f0f0"
  on-dark: "#ffffff"
  price-text: "#272727"

typography:
  display-xl:
    fontFamily: "'Didot 06 A', 'Didot 06 B', Didot, Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Didot 06 A', 'Didot 06 B', Didot, Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Didot 06 A', 'Didot 06 B', Didot, Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  artist-name:
    fontFamily: "'Didot 06 A', 'Didot 06 B', Didot, Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', 'Arial Narrow', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-md:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', 'Arial Narrow', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', 'Arial Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', 'Arial Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.03em
  body-md:
    fontFamily: "Inter, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Inter, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.01em
  label-uppercase:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', 'Arial Narrow', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', 'Arial Narrow', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', 'Arial Narrow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.04em
  button-sm:
    fontFamily: "'Gotham Narrow A', 'Gotham Narrow B', 'Arial Narrow', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.04em

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
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 40px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px 10px 40px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  artwork-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.artist-name}"
    metaTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    hoverShadow: "0 2px 12px rgba(0,0,0,0.08)"
    overlayBackground: "rgba(255,255,255,0.92)"
    overlayButtonBackground: "{colors.primary}"
    overlayButtonText: "{colors.on-primary}"
    overlayButtonTypography: "{typography.button-sm}"
    overlayButtonRounded: "{rounded.xs}"
  artist-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 4px 12px
    hoverBackground: "{colors.primary}"
    hoverText: "{colors.on-primary}"
  medium-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sold-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  price-tag:
    typography: "{typography.price-display}"
    textColor: "{colors.price-text}"
  filter-pill-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  filter-rail:
    backgroundColor: "{colors.canvas}"
    borderRight: "1px solid {colors.hairline}"
    width: 260px
    padding: "{spacing.lg}"
    sectionLabelTypography: "{typography.label-uppercase}"
    sectionLabelColor: "{colors.muted}"
    optionTypography: "{typography.body-sm}"
    optionColor: "{colors.ink}"
    selectedColor: "{colors.primary}"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaBackground: "{colors.primary}"
    ctaText: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    padding: "{spacing.section} 0"
  curator-note:
    backgroundColor: "{colors.surface-soft}"
    borderLeft: "4px solid {colors.primary}"
    headlineTypography: "{typography.title-md}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  artwork-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    artistTypography: "{typography.title-lg}"
    artistColor: "{colors.body}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.price-text}"
    metaTypography: "{typography.body-sm}"
    metaColor: "{colors.muted}"
    ctaBackground: "{colors.primary}"
    ctaText: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    ctaHeight: 48px
    padding: "{spacing.xl}"
  newsletter-form:
    backgroundColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    headlineColor: "{colors.on-dark}"
    inputBackground: "{colors.canvas}"
    inputTypography: "{typography.body-sm}"
    buttonBackground: "{colors.primary}"
    buttonText: "{colors.on-primary}"
    buttonTypography: "{typography.button-md}"
    buttonRounded: "{rounded.xs}"
    padding: "{spacing.xxl}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    activeBackground: "{colors.primary}"
    activeText: "{colors.on-primary}"
    size: 36px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    sectionLabelTypography: "{typography.label-uppercase}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.section} 0 {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Sandy linen (#dbac86) fill with near-black (#272727) Gotham Narrow text at 14px/600 weight, 4px radius, 44px tall. The warm, low-saturation tone is deliberately unhurried for an art-buying context: it reads as an invitation rather than a command. Hover darkens to `primary-active` (#c49a72); disabled renders `primary-disabled` (#eddfc8) with muted text to preserve the sand family without creating false affordance.

**`button-secondary`** — White canvas background, 1px solid ink border, matching Gotham Narrow type, same 44px height and padding as `button-primary`. Used for "Request More Info," "Save to Wishlist," and other secondary collector actions. The ink border keeps it readable without introducing any extra color.

**`button-ghost`** — Transparent with a 1px hairline (#dde0e3) border. Used for tertiary actions — Share, Print, pagination arrows — where visual weight must stay far below the artwork. Identical type and sizing to the other buttons so layout spacing is consistent.

### Search and Inputs

**`search-bar`** — Surface-soft (#f3f4f6) fill with a 40px left-pad zone for a loupe icon. At rest the border is hairline; on focus it transitions to sandy `primary` (#dbac86), the only moment of warmth in what is otherwise a cool-gray interface shell. Placeholder text runs in muted-soft (#9ca3af) Gotham Narrow at 14px. Lives in the nav-bar on desktop; expands to full-width on mobile below the collapsed header.

**`text-input`** — White background, hairline border at rest, ink border on focus. Feeds enquiry forms, newsletter capture, and account fields. Body-sm Inter at 14px / 1.57 line-height keeps form copy legible without competing with Didot headings nearby.

### Navigation

**`nav-bar`** — White canvas, 64px tall, a single hairline bottom border. The New Blood Art wordmark sits left in Didot 06 at `display-sm` (24px, 400 weight) — the serif signals gallery lineage immediately. Navigation items use Gotham Narrow `nav-link` (14px, 500, 0.03em tracking) in a horizontal row: Shop, Artists, Themes, Gifts, New In. A search icon and account/basket icon anchor the right end. No background tint, no drop shadow — the nav disappears into the page until the user needs it.

### Artwork Cards

**`artwork-card`** — White canvas, hairline-soft border, 8px radius. The artwork image occupies full card width at a consistent aspect ratio (typically 4:3 or 1:1 depending on medium). Below the image: artist name in Didot 06 `artist-name` (20px, 400), artwork title in Inter `body-sm`, then price in Gotham Narrow `price-display` (18px, 500). On hover, a 2px shadow lifts the card and a frosted white overlay fades in on the lower portion of the image, revealing a sandy "Quick View" button at `button-sm` scale — deliberately small so it does not dominate the artwork.

**`medium-badge`** — Small uppercase Gotham Narrow label (11px, 0.08em tracking) in surface-soft gray. Sits just above the artwork title to communicate medium — Oil on Canvas, Limited Edition Print, Giclée — without competing with the Didot artist name below it.

**`sold-badge`** — Same geometry as `medium-badge` but filled with deep gallery green (#194321) and white text. The green borrows from institution wall-paint rather than e-commerce traffic-light conventions, so a sold work reads as celebrated rather than blocked.

**`artist-chip`** — Rounded-full pill in surface-soft gray with body-sm Inter text. Used to link to an artist's full profile from within an artwork card or detail page. On hover, fills with sandy `primary` (#dbac86) and near-black text — the one piece of warm color the browse grid shows before a full artwork-detail page opens.

### Filters

**`filter-rail`** — Fixed 260px left column, white, hairline right border. Section headings in 11px uppercase Gotham Narrow in muted gray (#6d6d6d). Options in 14px Inter, near-black. When an option is selected, its text shifts to sandy `primary` (#dbac86) — no filled background, no pill — keeping the rail visually secondary to the artwork grid. Supports: Price Range (slider), Medium, Size, Orientation, Subject, Style, Colour. On mobile collapses to a full-screen bottom drawer triggered by a floating "Filter (n)" pill.

**`filter-pill-inactive / active`** — Horizontally scrollable pill row above the artwork grid for quick-access filters (Most Popular, Under £100, New In, etc.). Inactive pills: white with hairline border. Active: ink-black fill, white text. The binary visual shift means the active state is unambiguous without introducing any extra hue.

### Editorial

**`hero-editorial`** — Full-width surface-soft panel. Didot 06 `display-xl` (48px, 400) headline in near-black ink, Inter `body-md` subhead in body gray, and a sandy `button-primary` CTA. The layout is a 50/50 split — editorial copy left, full-bleed artwork photography right — rather than a text-over-image banner, so the art is never obscured by copy.

**`curator-note`** — A surface-soft card with a 4px left border in sandy `primary` (#dbac86). Used for editorial commentary, artist biography excerpts, and thematic curatorial text that contextualises a collection. Headline in Gotham Narrow `title-md` (16px, 600); body in Inter `body-md` (16px, 400, 1.6 line-height). The warm left border visually connects these notes to the CTA system without making them feel like promotional callouts.

**`artwork-detail-panel`** — Right-column layout on desktop (below image on mobile). Title in Didot 06 `display-md` (32px, 400), artist name in Gotham Narrow `title-lg` (18px, 600) in body gray, price in `price-display` (18px, 500). Below: a metadata grid in `body-sm` Inter for dimensions, edition number, medium, year, and framing options — each row separated by a hairline rule. "Add to Collection" button uses full `button-primary` at 48px height. A ghost "Enquire About This Work" button sits below for POA and high-value pieces.

**`newsletter-form`** — Full-width ink-dark (#272727) section between the browse grid and footer. Didot 06 `display-sm` (24px, 400) headline in white, a white-background `text-input`, and a sandy `button-primary`. The dark background creates a visual pause that reinforces the catalogue-page metaphor — the newsletter strip reads like a back-page insert.

### Footer

**`footer`** — Surface-soft gray (#f3f4f6), single hairline top border. A four-column link grid: Shop, Artists, About, Help. Section headings in 11px uppercase Gotham Narrow in muted gray. Links in 14px Inter, ink color. A baseline row carries copyright, legal links, and social icons in caption size. No bright colors, no gradients — the footer defers entirely to everything above it.

### Pagination

**`pagination`** — Compact numbered row: white canvas buttons with hairline borders and `button-sm` Gotham Narrow text, 36px square. Active page fills sandy `primary` (#dbac86) with on-primary text. Consistent with the ghost/secondary button family's minimal visual language.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; filter-rail collapses to full-screen bottom drawer; nav collapses to hamburger + logo; hero becomes single-column stacked; filter-pill row scrolls horizontally with scroll-snap; artwork-card padding reduces to {spacing.sm} |
| Tablet | 744–1128px | Two-column artwork grid; filter-rail becomes collapsible sidebar toggled by icon button; nav shows top-level items, secondary nav hidden; hero switches to 50/50 split at reduced headline size |
| Desktop | 1128–1440px | Three-column artwork grid with persistent 260px filter-rail; full horizontal nav; hero at full editorial split; artwork-detail panel in two-column layout |
| Wide | > 1440px | Four-column artwork grid; canvas max-width 1440px centered; filter-rail and detail panel hold fixed widths; outer margins absorb excess whitespace |

### Touch Targets

- All buttons minimum 44px height, 44px minimum width
- Filter pills minimum 36px height with 16px horizontal padding
- Nav hamburger: 44×44px tap target
- Artwork cards: full-card tap target, no isolated small hit zones
- Quick-view overlay CTA: minimum 44px height on touch
- Pagination buttons: 36px — acceptable on desktop; expand to 44px on touch breakpoints
- Artist chip: minimum 36px height; padding ensures readable tap zone

### Collapsing Strategy

- Filter rail → full-screen bottom-sheet drawer at < 744px; triggered by a floating "Filter (n)" pill anchored above the artwork grid
- Nav → hamburger icon at < 744px; slide-in panel shows full category hierarchy
- Hero split-column → image stacks above editorial text on mobile; headline drops to `display-md` (32px)
- Artwork grid reflows 4 → 3 → 2 → 1 column across breakpoints
- Filter-pill horizontal row: scroll-snapping on mobile with fade-out edge gradient indicating overflow
- Curator notes and newsletter section span full width at all breakpoints; internal padding scales with breakpoint

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta `theme-color` set; mobile browser chrome color is indeterminate
- Primary (#dbac86) is the most distinctive non-framework color extracted; it is identified as brand primary but could be a secondary accent — exact usage hierarchy not confirmed from extraction alone
- The majority of extracted colors (#2979ff, #0d6efd, #1266f1, #6610f2, #6f42c1, #d63384, #fd7e14, #0dcaf0, #20c997, #198754, #2563eb) are Bootstrap / MDB utility palette defaults and were excluded from the design system as framework noise, not brand choices
- Exact logo lockup — wordmark vs. symbol, color on dark backgrounds — not confirmed
- Dark-mode support not confirmed
- Exact grid breakpoint pixel values not extracted; values above inferred from Bootstrap 5 defaults the framework appears to use
- Icon set (custom, Font Awesome, Feather, etc.) not identified
- Animation durations, easing curves, and transition behavior not extracted
- Whether Didot 06 is used for the logo wordmark specifically, or only editorial headings, is not confirmed from extraction
