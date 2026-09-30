---
version: alpha
name: "Home Science Tools"
source_url: "https://www.homesciencetools.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The masthead runs #03354c — a deep-sea navy that reads closer to a microscope casing than a corporate navy — and it sets an immediate visual contract between the brand and its parent-educator audience: authoritative enough to anchor a curriculum, warm enough to invite a ten-year-old. Amber (#f1a500) breaks against that dark ground wherever a purchase action needs to happen, giving every "Add to Cart" button and sale ribbon the visual temperature of a Bunsen burner lit in a dark lab. The type pairing divides labor cleanly: Montserrat carries display headings and category labels in geometric uppercase that scans the way a supply-cabinet index should, while Outfit handles body copy, nav labels, and price figures with open apertures and generous x-height suited to a parent skimming a 200-item product grid between lesson blocks. The palette doesn't stop at one blue — it walks five distinct steps from #03354c through #395663, #4f7a92, and #4496f6 out to the sky-wash #5cbceb, letting section backgrounds, hover states, and informational callouts all coexist in the same cool hue family without competing. Teal-green (#5fb19a) marks new arrivals and ecology kit collections; red (#d14343) appears only under duress — error states, expiring-sale countdowns — because the brand reserves alarm for moments that earn it. Corner radii sit at a measured middle register: {rounded.sm} on buttons and form inputs, {rounded.md} on product cards, approachable enough for a homeschool family interface without sliding into the hyper-soft vocabulary of children's entertainment products. Grade-level badge tags, kit-type chips, and "New" markers are first-class card objects — this is a reference catalog as much as a storefront, and the entire layout from the mega-nav subject grid to the pill-shaped search bar with its navy submit orb is built around the question a parent always asks first: does this work for my kid's grade?

colors:
  primary: "#03354c"
  primary-active: "#022537"
  primary-disabled: "#4f7a92"
  primary-light: "#395663"
  primary-mid: "#4f7a92"
  accent: "#f1a500"
  accent-warm: "#f5b03d"
  accent-light: "#fff3cc"
  link: "#476bef"
  link-hover: "#3c64f4"
  sky: "#5cbceb"
  teal: "#5fb19a"
  error: "#d14343"
  error-hot: "#e42a11"
  ink: "#444444"
  body: "#444444"
  muted: "#757575"
  hairline: "#e5e5e5"
  hairline-soft: "#f5f5f5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  category-label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'Outfit', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', sans-serif"
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-navy:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-sm:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    focusBorderColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    submitBackground: "{colors.primary}"
    submitColor: "{colors.on-primary}"
    submitRounded: "{rounded.full}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-utility-strip:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  mega-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.category-label}"
    linkTypography: "{typography.body-sm}"
    topBorder: "3px solid {colors.accent}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
    columnDividerColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 4px 16px rgba(3,53,76,0.12)"
  grade-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  kit-type-tag:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.category-label}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    hoverBackground: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaBackground: "{colors.accent}"
    ctaTextColor: "{colors.on-accent}"
    ctaRounded: "{rounded.sm}"
  announcement-bar:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.body-sm}"
    height: 40px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  section-heading:
    textColor: "{colors.primary}"
    typography: "{typography.display-sm}"
    borderBottom: "3px solid {colors.accent}"
    paddingBottom: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.sky}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    dividerColor: "{colors.primary-light}"

## Components

### Buttons

**`button-primary`** — Amber (#f1a500) fill, white Montserrat 700 label, 8px radius, 44px tall. This is the "Add to Cart" and primary checkout action; on hover it softens to `{colors.accent-warm}` (#f5b03d). Disabled state falls back to `{colors.hairline}` background with `{colors.muted}` text, keeping the form readable without competing with active amber elsewhere on the page.

**`button-navy`** — Full `{colors.primary}` fill used for editorial and browse CTAs ("Shop All Kits", "Browse by Grade"). Visually separates informational actions from transactional amber buttons so teachers can immediately distinguish catalog exploration from purchase commitment.

**`button-secondary`** — White canvas with a 2px `{colors.primary}` navy border and navy text. Appears alongside primary buttons for secondary choices ("Save for Later", "Compare") or as a standalone action in non-commerce contexts like "Download Teacher Guide."

**`button-sm`** — Compact 32px amber button in 13px Montserrat 700 for in-grid quick actions (Quick View overlays, wishlist toggles). Matches the primary amber contract at reduced scale so hover states remain recognizable without annotation.

### Search

**`search-bar`** — Pill-shaped (`{rounded.full}`) input bar with a `{colors.primary}` circular submit button inset at the right edge, containing a white magnifier icon. Placeholder in `{colors.muted}` Outfit 16px. On focus the outer border transitions to `{colors.primary}` navy. The pill form factor distinguishes search from all other rectangular form inputs on the page.

### Navigation

**`nav-bar`** — Full-width `{colors.primary}` (#03354c) bar at 60px carrying logo left, category links center, and cart/account icons right, all in white. A slimmer `{colors.primary-light}` (#395663) utility strip above it displays shipping threshold copy and phone number at `{typography.caption}` scale.

**`mega-nav`** — White dropdown panel with a 3px `{colors.accent}` amber top border and a 24px soft shadow. Content arranges into a 4–6 column grid of `{typography.category-label}` uppercase subject names with icon thumbnails (Chemistry, Biology, Physics, Earth Science, etc.), separated by `{colors.hairline}` vertical dividers. A "Featured" column on the right promotes seasonal kits with thumbnail images.

### Product Card

**`product-card`** — White card at `{rounded.md}` (12px) with a 1px `{colors.hairline}` border. On hover, border activates to `{colors.primary}` and a shallow directional shadow lifts the card. Image fills the top ~55% at a fixed 4:3 aspect ratio. Below: `grade-badge` and optionally `sale-badge` or `new-badge` stack top-left; product title in `{typography.title-sm}` Montserrat 600; price in `{typography.price}` Outfit 700; a compact amber `button-sm` anchor at card bottom.

### Badges

**`grade-badge`** — Navy-teal (#395663) chip in all-caps 11px Montserrat 700. Carries grade range text ("Grades 3–8") as the first filter signal a parent reads when scanning a grid. Always present on products with defined grade targets.

**`sale-badge`** — Amber (#f1a500) chip. Shares the accent voltage with primary CTAs to create an intentional visual linkage between discounted price and purchase action.

**`new-badge`** — Teal-green (#5fb19a) chip distinguishes catalog additions from promotional pricing so "new" doesn't read as discount.

**`kit-type-tag`** — Light gray (`{colors.hairline-soft}`) chip in `{colors.primary}` navy text used for product taxonomy labels ("Refill Kit", "Complete Set", "Dissection Kit") that aren't grade-specific or promotional.

### Hero Banner

**`hero-banner`** — Full-width `{colors.primary}` navy band with headline in `{typography.display-xl}` Montserrat 700 white, supporting copy in `{typography.body-md}` Outfit at reduced opacity, and a prominent `{colors.accent}` amber CTA button. Product photography or a lifestyle image sits right-aligned over the navy field. Seasonal themes (Back to School, Summer Science) swap image and headline copy while the navy/amber color contract stays fixed.

### Announcement Bar

**`announcement-bar`** — 40px amber (#f1a500) strip pinned at top viewport for site-wide promotions ("Free shipping on orders over $50"). Single-line `{typography.body-sm}` Outfit white, centered, with optional dismiss X on the right edge. Disappears on scroll past the nav on mobile.

### Category Tile

**`category-tile`** — Soft gray surface card (`{colors.surface-soft}`) with subject icon, category name in `{typography.category-label}` navy text, `{rounded.md}` corners, and a 1px `{colors.hairline}` border. On hover transitions to `{colors.primary}` background with white text — a deliberate full-fill inversion that confirms the hover without animation dependency.

### Section Heading

**`section-heading`** — `{colors.primary}` navy text in `{typography.display-sm}` Montserrat 600, with a 3px `{colors.accent}` amber underline border at the bottom of the heading block. Used on homepage section dividers ("Featured Kits", "Shop by Subject") to carry the amber accent into editorial layout without requiring a button.

### Footer

**`footer`** — `{colors.primary}` full-width navy, 4-column grid: Shop, Resources, About, Contact. Column headings in `{typography.title-sm}` Montserrat 600 white; links in `{typography.body-sm}` Outfit `{colors.sky}` (#5cbceb) for adequate contrast against the dark navy ground. Bottom bar repeats the `{colors.primary-light}` (#395663) strip with legal copy and social icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; mega-nav collapses to slide-in hamburger drawer with accordion subjects; search bar moves to full-width row below the logo; hero banner stacks text above image; announcement bar truncates to one line with no dismiss |
| Tablet | 744–1128px | 2-column product grid; top nav shows 4 primary subject links only, remainder behind "More" chevron; search bar inline in nav at reduced width; hero banner side-by-side, image scales down |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-nav on hover; search bar spans center nav region; section headings display amber accent rule; announcement bar shows full copy |
| Wide | > 1440px | Content max-width ~1400px centered with balanced gutters; 4-column product grid; hero image scales to fill available right half without upscaling |

### Touch Targets

- All primary and secondary buttons minimum 44×44px
- Cart, account, and hamburger nav icons minimum 48×48px tap area
- Category tiles minimum 72px tall in mobile grid layout
- Mega-nav accordion rows 48px height per subject on mobile
- Badge chips not independently tappable — taps resolve to the parent card

### Collapsing Strategy

- Mega-nav collapses to a full-height right-to-left slide drawer; first-level subjects are 48px tappable rows; second level expands inline with a chevron toggle
- Footer 4-column layout collapses to single-column accordion on mobile; each column heading is a 48px tap target
- Product card grid shifts 4-col → 3-col → 2-col → 1-col across Wide → Desktop → Tablet → Mobile
- Announcement bar reduces to single-line condensed copy on Tablet; collapses entirely on Mobile if user has dismissed in session
- Grade and sale badges stack vertically in top-left card corner when both present; never overlap image

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The "hst" font-family token in extracted stacks likely indicates a custom icon font or a CSS font-face alias for brand icons; actual glyph usage was not confirmed — all components default to Montserrat/Outfit
- No meta theme-color was detected, so the mobile browser chrome color is unconfirmed; `{colors.primary}` (#03354c) is the logical choice
- Exact nav bar height, announcement bar height, and mega-nav column count are estimated from visual convention rather than extracted layout data
- Precise border-radius values were not returned by extraction; `{rounded.sm}` and `{rounded.md}` are inferred from observed visual softness on buttons and cards
- Cart drawer, checkout, and account-page component color treatment (whether amber or navy leads conversion steps) is inferred from PDP/PLP patterns — not directly observed
- Dark mode or high-contrast variant was not detectable from extraction hints; no alternate palette is defined
- Exact letter-spacing values for Outfit body sizes were not extracted and reflect typographic defaults for the typeface
