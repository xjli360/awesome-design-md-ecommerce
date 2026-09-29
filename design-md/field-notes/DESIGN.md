---
version: alpha
name: "Field Notes"
source_url: "https://fieldnotesbrand.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sixty-four pages stapled into a 3.5 × 5.5-inch kraft cover generated an entire visual identity around the discipline of what fits in a shirt pocket. The primary voltage is a dense cobalt (#003399) — the kind of blue that appears on government stationery and railway timetables rather than on product landing pages — and it carries every CTA, link, and structural accent against a warm khaki ground (#aea288, also the meta theme-color) that reads like aged bond paper under incandescent light. A third tone, steel blue (#3f8da7), steps in for mid-hierarchy product tags and catalog callouts without competing with the cobalt's authority. New Century Schoolbook (newcenturyschoolw01-rg) does nearly all the editorial work: its bracketed serifs and generous x-height trace back to nineteenth-century American newspaper composition, giving price lines and body copy a ledger quality rather than a designed-in affect. At large sizes with tight tracking, the same family becomes the display voice, recalling the rubber-stamp labels pressed into memo book covers. Corner radii stay minimal — product cards sit at `{rounded.xs}`, interactive elements at `{rounded.sm}`, structural panels at `{rounded.none}` — because the memo book itself has no rounded corners. Spacing mirrors the economy of a narrow-ruled page: `{spacing.base}` and `{spacing.lg}` run the grid, `{spacing.section}` appears only at editorial breaks between the catalog runs that separate new editions from archive stock. The warm putty of `{colors.brand-tan}` avoids both beige and brown, reading as something found on a workshop bench; it anchors the palette against the risk of the cobalt drifting into tech-brand territory. Limited-edition releases rotate through custom cover colors each quarter, but the nav chrome, footer grid, and button system hold constant — that structural consistency is what makes seasonal variety legible rather than chaotic. Every badge, strip, and label in the UI echoes the product itself: terse, stamped-looking, confident in a very small amount of space.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99aad9"
  primary-link: "#003399"
  primary-link-hover: "#002277"
  ink: "#1c1c1a"
  body: "#333330"
  muted: "#6b6860"
  hairline: "#d6d1c7"
  hairline-soft: "#e8e4de"
  canvas: "#ffffff"
  surface-soft: "#f5f2ec"
  surface-card: "#ffffff"
  surface-warm: "#ede9e1"
  on-primary: "#ffffff"
  brand-tan: "#aea288"
  brand-steel: "#3f8da7"
  brand-steel-active: "#2e718a"

typography:
  display-xl:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', 'Century Schoolbook', Georgia, serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', 'Century Schoolbook', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.1px
  edition-label:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'New Century Schoolbook', 'newcenturyschoolw01-rg', Georgia, serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 60px
    logoColor: "{colors.ink}"
  nav-link:
    textColor: "{colors.ink}"
    textColorHover: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline-soft}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
  edition-badge:
    backgroundColor: "{colors.brand-tan}"
    textColor: "{colors.ink}"
    typography: "{typography.edition-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  edition-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.edition-label}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  edition-strip:
    backgroundColor: "{colors.brand-tan}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    padding: "{spacing.base} {spacing.xl}"
    borderBottom: "2px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: 8px 14px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.brand-tan}"
    linkColorHover: "{colors.canvas}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.section}"
  newsletter-signup:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    inputBorderColor: "{colors.hairline}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  memo-cover-label:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    letterSpacing: 2px
    textTransform: uppercase
  catalog-section-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    borderBottom: "2px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
  product-tag:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.brand-steel}"
    typography: "{typography.edition-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  pagination:
    textColor: "{colors.muted}"
    activeColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"

## Components

### Buttons

**`button-primary`** — Cobalt fill (#003399) with white type set in `{typography.button-md}` (New Century Schoolbook Bold, 15px, +0.5px tracking). Square-edged at `{rounded.sm}` (4px), 44px tall, padding 12 × 24px. Active state darkens to `{colors.primary-active}` (#002277); disabled washes to a light cobalt tint via `{colors.primary-disabled}`. The bold serif on a block-color ground deliberately echoes a rubber stamp on kraft paper — short, emphatic, no ornamentation.

**`button-secondary`** — White canvas fill with a 1.5px cobalt border and cobalt type. Mirrors primary dimensions exactly so the pair can sit side-by-side without height mismatch. Active state shifts fill to `{colors.surface-soft}` and border to `{colors.primary-active}`. Used for secondary purchase actions ("Add to Wish List") and nav-level CTAs that should recede from the primary.

### Text Input

**`text-input`** — White fill, 1px `{colors.hairline}` border, focuses to a solid 1px `{colors.primary}` outline with no box-shadow glow. Body-md serif type keeps form fields editorial rather than app-like. 42px height, `{rounded.sm}` corners, placeholder in `{colors.muted}`. The same chrome handles email, search, and quantity fields throughout.

### Navigation

**`nav-bar`** — White background, 60px tall, separated from the page body by a 1px `{colors.hairline}` bottom border. The wordmark renders in `{colors.ink}` with no color fill. Nav links use `{typography.nav-link}` and step to `{colors.primary}` on hover; no dropdown card backgrounds or megamenu panels — just text links spaced at `{spacing.lg}` intervals. The restraint is structural: the nav is a ledger header, not a feature surface.

**`nav-link`** — 14px New Century Schoolbook, resting in `{colors.ink}`, hovering to `{colors.primary}`. No underline at rest; underline appears on hover. No indicator dots, no notification badges in the primary nav.

### Product Card

**`product-card`** — White card, 1px `{colors.hairline-soft}` border, `{rounded.xs}` (2px) corners, `{spacing.md}` internal padding. Title in `{typography.title-sm}`, price in `{typography.price-display}`, SKU or brief descriptor in `{typography.caption}`. Edition badges (`edition-badge` or `edition-badge-new`) pin flush to the top-left corner of the cover image. No box-shadow; cards separate from the `{colors.surface-soft}` page ground via their hairline border alone.

### Hero Banner

**`hero-banner`** — Full-width section in `{colors.surface-soft}`, headline in `{typography.display-xl}` (52px serif, −1.5px tracking), subtext in `{typography.body-md}`. Padding is `{spacing.xxl}` top/bottom, `{spacing.section}` left/right. Hero images are flush-right crops of memo book covers against the warm background — the cover object is always the subject; lifestyle photography appears only in editorial runs below the fold.

### Edition Badges

**`edition-badge`** — Khaki fill (`{colors.brand-tan}`), ink type, all-caps `{typography.edition-label}` (11px, +1.5px tracking), `{rounded.none}`, 3 × 8px padding. Used for returning seasonal and archive editions (e.g., "ARCHIVE", "LIMITED"). **`edition-badge-new`** swaps fill to `{colors.primary}` with white type for first-run releases. Both badges are non-interactive on cards; on PDPs they navigate to the edition landing page.

### Edition Strip

**`edition-strip`** — Full-width header strip for category and collection pages, `{colors.brand-tan}` fill, `{typography.display-sm}` headline (26px serif), 2px bottom border in `{colors.hairline}`. Padding is `{spacing.base}` vertical, `{spacing.xl}` horizontal. The strip directly references the horizontal color band on memo book covers — it is the closest the digital UI comes to replicating the physical object's visual grammar.

### Search Bar

**`search-bar`** — `{colors.surface-soft}` fill, `{colors.hairline}` border, focuses to `{colors.primary}`. 40px tall, `{rounded.sm}`, magnifier icon in `{colors.muted}` on the left interior. Lives in the nav-bar right zone on desktop; collapses to a 44 × 44px icon-only trigger on mobile that expands to a full-width overlay input.

### Footer

**`footer`** — Dark ground (`{colors.ink}`), white body type, `{colors.brand-tan}` links that step to `{colors.canvas}` on hover. Four-column grid on desktop (Shop, Learn, Company, Newsletter), two columns on tablet, single stacked accordion on mobile. Colophon line at base uses `{typography.caption}` for the copyright and country-of-origin copy. The dark footer against the warm-canvas page reads as the back cover of the memo book.

### Newsletter Signup

**`newsletter-signup`** — Warm surface band (`{colors.surface-warm}`) with a `{typography.title-md}` headline. Email input shares `text-input` chrome; submit button uses full `button-primary` styles. `{rounded.sm}` on both elements. Embedded as a full-bleed band directly above the footer on most pages; the heading copy follows the Field Notes voice — terse, imperative, no marketing filler.

### Memo Cover Label

**`memo-cover-label`** — Transparent background, `{colors.ink}` text, `{typography.display-sm}` with +2px letter spacing and uppercase transform. Used in editorial and lookbook contexts to simulate the printed text stamped into product cover images. Not an interactive element; renders over photography at large breakpoints and disappears or scales down at mobile.

### Catalog Section Header

**`catalog-section-header`** — `{colors.surface-soft}` fill, `{typography.display-md}` headline (36px), 2px `{colors.hairline}` bottom border. `{spacing.lg}` top/bottom padding, flush to the grid edges horizontally. Titles the major runs within the catalog ("Memo Books," "Journals," "Limited Editions") and resets the visual rhythm between product grids.

### Product Tag

**`product-tag`** — `{colors.surface-warm}` fill, `{colors.brand-steel}` text, all-caps `{typography.edition-label}`. `{rounded.xs}` corners, 2 × 6px padding. Used for product-type identifiers ("MEMO BOOK", "JOURNAL", "PLANNER") on search results and collection grids. The steel blue reads as a secondary accent coordinated with `{colors.brand-steel-active}` on hover.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline steps down to `{typography.display-md}`; search expands to full-screen overlay; edition strip text scales to `{typography.title-md}`; footer stacks into single-column accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links, secondary items in dropdown; hero retains `{typography.display-xl}` at reduced padding; footer in two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav at 60px; hero at full padding; edition strips at `{typography.display-sm}`; footer four columns |
| Wide | > 1440px | Content max-width capped at 1440px, centered with increased side padding; typography and component chrome unchanged |

### Touch Targets

- All nav items: minimum 44 × 44px touch area regardless of visible label size
- Product cards: full-card tap target, not just title text
- Add-to-cart and checkout buttons: 44px minimum height satisfied by default `button-primary` height
- Edition badges: invisible padding extends touch target to 44 × 24px minimum; taps navigate to edition landing page
- Search icon: padded to 44 × 44px before expansion to input field

### Collapsing Strategy

- Navigation: full horizontal bar on desktop/tablet → hamburger drawer sliding from the left on mobile; no flyout or hover panel on mobile
- Product grid: 4-up → 3-up → 2-up → 1-up as breakpoints narrow
- Hero: side-by-side text + cover image on desktop → stacked image-above-text on mobile
- Edition strip: full `{typography.display-sm}` on desktop/tablet → `{typography.title-md}` on mobile, same background color block retained
- Footer: 4-column → 2-column → accordion (each section header tappable to expand/collapse) on mobile
- Search: persistent inline bar in nav on desktop → icon-only with full-screen expand on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only three hex values were extracted; Field Notes publishes editions with wildly varying cover colors (yellow, red, orange, green) that rotate seasonally — per-edition accent tokens are not derivable without scraping individual PDPs
- No font weights or secondary display typeface detected; a condensed grotesque may be loaded via JS for certain campaign or editorial pages and would not appear in static extraction
- No shadow, transition, or easing tokens were extractable; hover elevation behavior on product cards is inferred from brand aesthetic rather than measured values
- No grid gutter widths or column count declarations found; responsive column behavior is estimated from standard e-commerce conventions
- Checkout flow, cart drawer, and account pages were not reached during extraction; those surfaces may carry different chrome from the storefront catalog
- The steel blue (#3f8da7) source context is unclear — it may belong to a specific edition or a nav/callout element; its usage scope is inferred rather than observed
