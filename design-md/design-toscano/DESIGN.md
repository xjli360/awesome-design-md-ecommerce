---
version: alpha
name: "Design Toscano"
source_url: "https://www.designtoscano.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Carved stone meets coastal fog in the one color extracted from Design Toscano's pre-launch state — #45768d, a muted steel-teal that reads like weathered verdigris on garden bronze left through three seasons of rain. The site's relaunch tagline, "Reimagined. Refined. Returning.", signals an editorial recalibration for a catalog built on European antiquities: gargoyles watching from garden walls, medieval knights standing sentry at front doors, Venetian masks and life-size Romanov statues sold with the conviction that a home should feel like a private museum. Where garden decor brands typically invoke terra cotta and cottage-garden sage, Design Toscano has long anchored its identity in weight and shadow — the density of cast resin, the theatrical scale of a life-size figure, the moral seriousness of a Gothic frieze. The UI should carry that gravitational pull without tipping into dusty catalogue. Canvas reads warm parchment ({colors.canvas}), not clinical white. Editorial serif type — proportioned for museum wall labels — handles display and product names; a clean sans-serif covers navigation and utility copy. Primary CTAs inherit the extracted teal ({colors.primary}), which holds legibility against both the dark hero backdrops that will anchor the relaunch campaign and the warm surface cards beneath product grids. A secondary gilt token ({colors.gold-accent}) appears on "new arrival" badges, sale ribbon accents, and hover states on featured collection links — the one place the catalog allows itself a flourish. Rounded tokens are deliberately restrained: {rounded.xs} on badges, {rounded.sm} on primary buttons, {rounded.md} on product cards — nothing approaches a pill; a bubbly border-radius would be incongruous next to a life-size stone lion. Section spacing is theatrical at {spacing.section}, product grids breathe rather than compress, and hero zones run edge-to-edge. Because the 2026 extraction caught only one distinctive hex and zero web fonts, all type stacks and supporting palette entries below are derived from documented brand aesthetics and should be revisited once the relaunched site is publicly accessible.

colors:
  primary: "#45768d"
  primary-hover: "#3d6b7f"
  primary-active: "#345f73"
  primary-disabled: "#a8c4d0"
  gold-accent: "#8c6914"
  gold-soft: "#c9a84c"
  ink: "#1c1917"
  body: "#2f2d2a"
  muted: "#6b6560"
  muted-soft: "#9b9590"
  hairline: "#d6d0c8"
  hairline-soft: "#e8e3dc"
  canvas: "#faf8f5"
  surface-soft: "#f2ede6"
  surface-card: "#ffffff"
  surface-dark: "#1c1917"
  on-primary: "#ffffff"
  on-dark: "#f2ede6"
  badge-sale: "#8c1a1a"
  on-badge: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Jost', 'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.03em
  body-md:
    fontFamily: "'Jost', 'Inter', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', 'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', 'Inter', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  uppercase-tag:
    fontFamily: "'Jost', 'Inter', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', 'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Inter', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Jost', 'Inter', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  product-name:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  price-lg:
    fontFamily: "'Jost', 'Inter', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Jost', 'Inter', system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.12em
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    borderWidth: 0
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    borderColor: "{colors.ink}"
    borderWidth: 1px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    borderColor: "{colors.on-dark}"
    borderWidth: 1px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottomColor: "{colors.hairline}"
    borderBottomWidth: 1px
  nav-bar-logo:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  nav-dropdown-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    borderTopColor: "{colors.hairline}"
    borderTopWidth: 1px
    padding: "{spacing.xl} {spacing.section}"
    headingTypography: "{typography.uppercase-tag}"
    headingColor: "{colors.muted}"
  hero-full-bleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 640px
    overlayOpacity: 0.45
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    contentPaddingX: "{spacing.xxl}"
    contentPaddingY: "{spacing.section}"
  hero-tagline-badge:
    textColor: "{colors.gold-soft}"
    typography: "{typography.uppercase-tag}"
    marginBottom: "{spacing.md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    imageAspectRatio: "4/5"
    nameTypography: "{typography.product-name}"
    nameColor: "{colors.ink}"
    priceTypography: "{typography.price-lg}"
    priceColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "{spacing.md}"
    badgePosition: top-left
    shadow: "0 2px 12px rgba(28,25,23,0.08)"
  product-card-hover:
    shadow: "0 6px 24px rgba(28,25,23,0.15)"
    imageScale: 1.04
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-badge}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-gold:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.on-badge}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.uppercase-tag}"
    paddingY: "{spacing.xl}"
    borderTopColor: "{colors.hairline}"
    borderBottomColor: "{colors.hairline}"
    borderWidth: 1px
  collection-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    iconColor: "{colors.muted}"
  search-bar-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  newsletter-band:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.section}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.uppercase-tag}"
    headingColor: "{colors.gold-soft}"
    linkColor: "{colors.muted-soft}"
    borderTopColor: "{colors.gold-accent}"
    borderTopWidth: 2px
    paddingY: "{spacing.section}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  price-was:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textDecoration: line-through
  price-now:
    textColor: "{colors.badge-sale}"
    typography: "{typography.price-lg}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "transparent"
    inactiveTextColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    typography: "{typography.button-sm}"
    height: 40px
    minWidth: 40px
  tooltip:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 8px 12px

## Components

### Buttons
**`button-primary`** — Uppercase-tracked label in `{typography.button-md}` on a `{colors.primary}` teal ground, 48px tall with `{rounded.sm}` corners. Hover shifts to `{colors.primary-hover}`, active to `{colors.primary-active}`, disabled fades to `{colors.primary-disabled}` — all three preserve the radius so the button never changes shape. The 14px 28px padding gives CTAs room to breathe beside dramatic sculpture imagery without overwhelming the visual.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border and matching label — an outlined sibling that pairs with `button-primary` in two-CTA rows ("Add to Cart" / "View Full Collection"). On dark hero surfaces, swap to `button-secondary-on-dark`, where both border and label shift to `{colors.on-dark}` for contrast against the deep backdrop.

**`button-ghost`** — No border, no fill; `{colors.primary}` label in `{typography.button-sm}`. Reserved for "Read More" inline links, "Back to Top" triggers, and secondary navigation actions where a contained button would read as too assertive.

### Navigation
**`nav-bar`** — 68px fixed header on `{colors.canvas}` parchment with a 1px `{colors.hairline}` bottom rule. Links in `{typography.nav-link}` (13px, uppercase, tracked 0.1em) sit centrally; the brand wordmark inherits `{typography.display-sm}` in `{colors.ink}`. On scroll past 80px the bar compresses to 52px and gains a subtle drop shadow to signal elevation change.

**`nav-dropdown-panel`** — Full-width mega-menu on `{colors.canvas}` with category headings in `{typography.uppercase-tag}` and links in `{typography.body-sm}`. Drops flush below the nav bar with a `{colors.hairline}` top rule rather than a shadow — the bar appears to extend downward rather than float a separate layer. Category imagery tiles sit to the right of link columns.

### Hero
**`hero-full-bleed`** — Edge-to-edge imagery at minimum 640px tall, overlaid at 45% `{colors.surface-dark}` scrim so richly detailed sculpture photos don't compete with type. Headline in `{typography.display-xl}` and optional subhead in `{typography.body-md}`, both `{colors.on-dark}`. The `hero-tagline-badge` preheader — `{typography.uppercase-tag}` in `{colors.gold-soft}` — floats above the main title to establish collection or season context before the headline lands.

### Product Cards
**`product-card`** — `{rounded.md}` card on `{colors.surface-card}` with a 4:5 portrait image ratio, allowing tall statue silhouettes and standing figures to read without cropping. Product name in `{typography.product-name}` (Cormorant Garamond 18px), price in `{typography.price-lg}`. A soft shadow lifts the card from the `{colors.surface-soft}` grid background; hover deepens the shadow and scales the image 1.04× within the card clip. Badges (`badge-new`, `badge-sale`, `badge-gold`) pin to the top-left corner and stack vertically when multiples apply.

### Badges
**`badge-new`** — `{colors.primary}` fill, `{colors.on-primary}` label in `{typography.badge}` uppercase with `{rounded.xs}` corners. Appears when items enter live inventory. **`badge-sale`** — deep crimson `{colors.badge-sale}`, reserved strictly for markdown events to preserve urgency signal. **`badge-gold`** — `{colors.gold-accent}` fill for "Editor's Pick" and "Staff Favorite" designations within curated collection pages — the gilt finish reads as curatorial authority rather than promotion.

### Search
**`search-bar`** — Inset in the nav bar or opened as a full-width overlay. `{colors.surface-soft}` background, `{rounded.xs}`, 1px `{colors.hairline}` border, placeholder in `{colors.muted}`. On focus, border upgrades to 2px `{colors.primary}` — matching `text-input-focus`. Icon color is `{colors.muted}` at rest, transitions to `{colors.ink}` when the field is active.

### Category Strip
**`category-strip`** — Horizontal band of category labels on `{colors.surface-soft}` with 1px `{colors.hairline}` borders top and bottom. Labels in `{typography.uppercase-tag}`, `{colors.ink}`. Active category receives a 2px `{colors.primary}` underline indicator. At desktop widths the strip sits in a single centered row; at tablet and mobile it scrolls horizontally with a right-edge fade gradient indicating overflow.

### Collection Heading
**`collection-heading`** — Section titles in `{typography.display-md}` (Cormorant Garamond 28px) above the product grid, with optional subtitle in `{typography.body-md}` `{colors.muted}`. Margin-bottom of `{spacing.xl}` preserves the editorial breathing room between the heading block and the first grid row.

### Newsletter Band
**`newsletter-band`** — Full-width block in `{colors.primary}` teal with white headline (`{typography.display-md}`) and body copy (`{typography.body-md}`). A `newsletter-input` sits inline beside a `button-primary` on desktop; both stack vertically on mobile with the input expanding to full width.

### Footer
**`footer`** — Dark canvas (`{colors.surface-dark}`) with a 2px `{colors.gold-accent}` top border — the one instance where the gilt accent carries structural weight rather than decorative emphasis. Column headings in `{typography.uppercase-tag}` tinted `{colors.gold-soft}`, links in `{typography.body-sm}` at `{colors.muted-soft}` resting and `{colors.on-dark}` on hover. Legal and copyright copy at bottom in `{typography.caption}`.

### Pricing States
**`price-was`** — Struck-through original price in `{colors.muted}` via `{typography.body-sm}`, set to the left. **`price-now`** — Current sale price in `{colors.badge-sale}` crimson via `{typography.price-lg}`, placed immediately right of the struck figure; the color contrast between muted gray and crimson red makes the discount legible at a glance without requiring a badge.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark; hero min-height 480px; category strip horizontal-scroll with fade; newsletter stacks vertically; footer single-column accordion |
| Tablet | 744–1128px | 2-column product grid; nav shows primary links, overflow in hamburger; hero 560px min-height; mega-menu replaced by modal drawer with back-navigation |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-menu panel; hero 640px min-height; newsletter inline; footer 4-column |
| Wide | > 1440px | Grid max-width 1400px centered; hero background bleeds edge-to-edge while content column stays within max-width; `display-xl` scales to 64px |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Product card tap zone covers the full card surface, including the image area
- Nav hamburger 48×48px tap area
- Badges are display-only; parent card handles the touch event
- Pagination items minimum 44px square tap area
- Category strip items padded to 44px height even when label text is shorter

### Collapsing Strategy
- Nav: full desktop link row → primary-links-only at tablet → hamburger drawer at mobile
- Footer: 4-column grid → 2-column grid → single-column accordion with tap-to-expand headings
- Product grid: 4-col → 2-col → 1-col; card padding reduces from `{spacing.md}` to `{spacing.sm}`
- Hero headline: `display-xl` (56px) → 40px at tablet → 30px at mobile, preserving Cormorant Garamond throughout
- Category strip: single centered row at desktop → horizontal scroll at tablet/mobile with right-edge opacity fade
- Collection heading `display-md` (28px) → 22px at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Only one hex color extracted** (#45768d); the full brand palette — background tones, gold accents, error/sale states, footer darks — is inferred from documented brand aesthetics and publicly visible catalog imagery, not extracted tokens. Every color entry except `primary` should be treated as provisional until the relaunched site is live and scannable.
- **Zero web fonts detected**; the site was behind a pre-launch holding page at extraction time. Typography stacks (Cormorant Garamond for serif display, Jost for sans UI) are brand-aesthetics inferences — the 2026 relaunch may use entirely different typefaces. Confirm before shipping any consumer-facing UI.
- **No meta theme-color set**; this should be established at launch. Recommend `{colors.primary}` (#45768d) for light-mode and `{colors.surface-dark}` (#1c1917) for dark/hero contexts.
- **Platform unknown** (confirmed not Shopify); the e-commerce framework and its default component patterns are unconfirmed. Component padding, height, and input styling may need adjustment to match the actual checkout and cart UX.
- **Gold accent palette** (#8c6914, #c9a84c) is inferred from the brand's heavily documented use of gilt-finish imagery and European antique positioning. Exact brand gold values should be extracted from the live relaunched site and reconciled with these provisional entries.
- **Responsive breakpoints and mobile behavior** are unconfirmed from extraction — the responsive table above reflects standard DTC practice, not observed Design Toscano behavior. Validate against the live 2026 site.
