---
version: alpha
name: "Copper Canyon Press"
source_url: "https://www.coppercanyonpress.org"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A literary press that trusts the weight of a single serif letterform over any decorative flourish, built on a near-white canvas (#fefefe) and a deep, almost-black ink (#0a0a0a) that gives poetry pages the gravity of a letterpress sheet. The extracted palette reveals a restrained editorial system — the warm accent is a muted cerulean (#2ba6cb) that appears in navigation links and subtle UI signals, while a secondary rust-red (#c60f13) surfaces only in critical actions like cart or error states, never competing with the poetry itself. Typography leans on Adobe Caslon Pro for display and body text, a choice that signals literary tradition without museum-like stiffness; Open Sans handles UI labels and buttons, creating a quiet tension between old and new. Rounded corners are minimal — `{rounded.xs}` on cards and `{rounded.sm}` on buttons — because the brand treats the page as a reading surface, not a product interface. The footer and sidebar use a muted gray (#cacaca) for hairline borders that organize information without shouting, and a soft surface (#f0f0f0) for secondary panels that feel like the endpapers of a hardcover book. This is a design system built for the long poem, the single-author collection, the chapbook that arrives in the mail — every token serves the text.

colors:
  primary: "#2ba6cb"
  primary-active: "#165366"
  primary-disabled: "#8a8a8a"
  ink: "#0a0a0a"
  body: "#222222"
  muted: "#757575"
  muted-soft: "#949494"
  hairline: "#cacaca"
  hairline-soft: "#e6e6e6"
  canvas: "#fefefe"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rust: "#c60f13"
  accent-green: "#5da423"
  accent-gold: "#ffae00"
  link-blue: "#003388"
  link-hover: "#165366"
  error-bg: "#f8f2ed"
  error-text: "#63080a"

typography:
  display-xl:
    fontFamily: "'adobe-caslon-pro', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'adobe-caslon-pro', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'adobe-caslon-pro', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'adobe-caslon-pro', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'adobe-caslon-pro', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'adobe-caslon-pro', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'adobe-caslon-pro', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'adobe-caslon-pro', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  footer-link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted}"
  button-accent-rust:
    backgroundColor: "{colors.accent-rust}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.link-blue}"
    typography: "{typography.link}"
    padding: 4px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(43, 166, 203, 0.15)"
  text-input-error:
    border: "1px solid {colors.accent-rust}"
    backgroundColor: "{colors.error-bg}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    color: "{colors.primary-active}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(10, 10, 10, 0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "3/4"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-rust}"
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
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
  sidebar-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 24px
    border: "1px solid {colors.hairline-soft}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.footer-link}"
    padding: "48px 0"
  footer-link-hover:
    color: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "80px 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart," "Subscribe," and "Donate." Uses the cerulean accent (#2ba6cb) as background with white text. On hover, darkens to #165366. Disabled state drops to a muted gray (#8a8a8a). The `{rounded.sm}` corners keep the button approachable without feeling casual.

**`button-secondary`** — Outlined alternative for secondary actions like "Learn More" or "View Details." White background with a thin hairline border (#cacaca). Hover fills with the soft surface (#f0f0f0) and darkens the border to muted (#757575).

**`button-accent-rust`** — Reserved for destructive or urgent actions (e.g., "Remove from Cart," "Cancel Subscription"). Uses the rust-red (#c60f13) to signal caution without alarm. Same height and padding as primary for layout consistency.

**`button-text-link`** — A text-only button styled as an inline link, used for "Read More" in poetry excerpts or "View All" in category headers. Uses the link blue (#003388) and inherits the serif body typography to blend with surrounding text.

### Cards
**`product-card`** — The core unit for displaying book covers and metadata. A white card with a thin soft hairline border and `{rounded.xs}` corners. Hover adds a subtle shadow and darkens the border to standard hairline. The image area maintains a 3:4 aspect ratio (standard book proportions) with matching corner radius.

**`sidebar-panel`** — Used for author bios, series descriptions, and newsletter signup forms. Rendered on the soft surface (#f0f0f0) to visually recede behind the main content. Padding matches the `{spacing.lg}` rhythm of the body text.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height with white background and a soft hairline bottom border. Navigation links use Open Sans in uppercase with 0.5px letter spacing. Active state underlines with the cerulean primary; hover shifts to the darker active shade.

**`search-bar`** — A pill-shaped input field on the soft surface, used for searching titles, authors, and collections. On focus, the background returns to white and the border switches to primary blue. The `{rounded.full}` shape contrasts with the otherwise minimal corner system, making the search action feel distinct.

### Badges
**`badge-new`** — Green (#5da423) badge for recent releases or new editions. Uses uppercase Open Sans at 11px with tight padding. Appears in the top-right corner of product cards.

**`badge-sale`** — Rust-red (#c60f13) badge for discounted titles. Same typography and placement as the new badge, but color-coded for urgency.

**`badge-award`** — Gold (#ffae00) badge for prize-winning titles (e.g., National Book Award, Pulitzer). Uses dark text (#0a0a0a) for contrast against the bright background.

### Forms
**`text-input`** — Standard input field for search, newsletter signup, and checkout forms. White background with hairline border and `{rounded.xs}` corners. Focus state adds a subtle blue glow (3px spread at 15% opacity). Error state swaps the border to rust-red and tints the background to the warm error tone (#f8f2ed).

### Footer
**`footer-section`** — A dark footer on the near-black ink (#0a0a0a) with white text. Links use Open Sans at 13px with normal weight. Hover shifts links to the cerulean primary. The footer is divided into columns for About, Books, Events, and Support sections.

### Dividers
**`divider`** — Standard hairline (#cacaca) used between major sections and within sidebar panels. **`divider-soft`** uses the lighter hairline (#e6e6e6) for less visual weight, typically within cards or between related items.

### Tags
**`tag`** — Small pill-shaped labels for genre, format, or series categorization. Rendered on the soft surface with muted text. Used in search filters, book detail pages, and category navigation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack full-width; hero text reduces to 32px; sidebar panels move below main content |
| Tablet | 744–1128px | Two-column grid for product cards; nav links remain visible but compact; sidebar appears as a collapsible panel; hero text at 40px |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; persistent sidebar; hero text at 48px |
| Wide | > 1440px | Max-width container at 1440px; increased whitespace margins; four-column product grid on category pages |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Search bar expands to full width on mobile with 48px height
- Hamburger menu icon has 48x48px tap area
- Product card images remain tappable with no minimum size constraint

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px; dropdown menus become accordion panels
- Sidebar panels collapse below 744px, revealed by a "Filters" toggle button
- Product grid reduces from 4 columns to 1 column on mobile
- Footer columns stack vertically on mobile, with section headers as accordion toggles
- Search bar hides behind an icon on mobile, expanding to full-width overlay on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors include many generic framework defaults (Foundation CSS grays, blues, greens) — the true brand palette likely has fewer, more intentional colors. The cerulean (#2ba6cb) and rust (#c60f13) are the most distinctive signals, but their exact usage (hover states, active states, disabled states) is inferred from common patterns rather than extracted.
- Font stack is inferred from extracted declarations — Adobe Caslon Pro appears as a web font reference, but exact weights and sizes are estimated from typical literary press usage. The site may use additional weights (italic, semibold) not captured.
- No dark mode tokens could be extracted; the system assumes light mode only.
- Error states, focus rings, and disabled styling are based on accessibility best practices rather than extracted values.
- The extracted palette includes several near-duplicate grays (#e9e9e9, #eeeeee, #f1f1f1) — these may represent different surfaces (cards, panels, hover states) but exact mapping is speculative.
- No animation or transition timing values were extracted (hover transitions, page loads, menu animations).
- The extracted theme-color (#ffffff) suggests no browser chrome theming; this may change with a future redesign.
