---
version: alpha
name: "Hey Maeve"
source_url: "https://www.heymaeve.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Ovo serif — an old-style typeface with the gentle stroke contrast of hand-lettering — carries every headline at Hey Maeve, a choice that immediately separates it from the grotesque-heavy pack of DTC accessories brands. That editorial gravity anchors a palette of studied softness: the hero action color is a dusty rose (#c87480), muted enough to read as elegant against the near-white canvas (#f8fafc) rather than saccharine. Blush surfaces (#f0dede) appear as background washes behind editorial and collection headers — the same pink family as the primary, but dialed down to a whisper. Near-black (#121212) stands in for true black everywhere text runs long, shaving the harshest edge off high-contrast screens. Ink-level grays (#374151, #64748b) handle metadata and secondary copy, while blue-grays (#e2e8f0, #cbd5e0) serve as border and divider strokes — the Tailwind-adjacent slate family doing structural work without calling attention to itself. Buttons run at full-radius (`{rounded.full}`), consistent with the brand's soft femininity; inputs and cards take a gentle `{rounded.sm}` so edges read as contemporary rather than clinical. Navigation lives in Inter — small, moderately spaced, nearly invisible — letting product photography lead. The Ovo–Inter pairing is the central typographic tension: a serif that says slow down and an interface sans that says get there efficiently, balanced by white space rather than weighted toward either pole. Product cards surface price cleanly in Inter numerals, with minimal badge treatment and no aggressive discounting vocabulary. The site leans on the accessory-as-object frame — single-product hero moments, close-cropped material shots, and an absence of lifestyle clutter that keeps the jewelry's own finish and scale readable.

colors:
  primary: "#c87480"
  primary-active: "#b5606c"
  primary-hover: "#d4858f"
  primary-disabled: "#e8b8be"
  ink: "#121212"
  body: "#374151"
  muted: "#64748b"
  hairline: "#e2e8f0"
  hairline-mid: "#cbd5e0"
  divider: "#dedede"
  canvas: "#f8fafc"
  surface-soft: "#f0dede"
  surface-card: "#ffffff"
  surface-neutral: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Ovo', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Ovo', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Ovo', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  price-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.03em
  label-tag:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 10px
    fontWeight: 600
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline-mid}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-mid}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
    focusBorderColor: "{colors.primary}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline-mid}"
    padding: 12px 20px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-link-active:
    textColor: "{colors.ink}"
    textDecoration: underline
    textUnderlineOffset: 3px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-sm}"
    textColor: "{colors.body}"
    priceColor: "{colors.ink}"
    gap: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  quick-add-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    height: 36px
    padding: 0 16px
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.xl}"
  pdp-title:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  pdp-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  pdp-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  filter-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline-mid}"
    padding: 6px 14px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons
**`button-primary`** — Full-radius dusty-rose pill (#c87480 fill, white label) in uppercase Inter 13px with 0.1em tracking. Height locks at 48px with generous horizontal padding; the pill shape is consistent across all contexts. Hover brightens to `{colors.primary-hover}` (#d4858f) and active press darkens to `{colors.primary-active}` (#b5606c). Disabled state washes out to pale blush `{colors.primary-disabled}` (#e8b8be) with no pointer events.

**`button-secondary`** — Identical pill geometry, white fill, `{colors.hairline-mid}` border. Used for alternate actions — "View Details," "Add to Wishlist" — where the rose primary would crowd the primary CTA.

**`button-ghost`** — Transparent fill with a `{colors.primary}` border and rose label text. Surfaces in editorial and lookbook sections where a solid rose button would overwhelm a blush background.

### Inputs
**`text-input`** — 48px tall, `{rounded.sm}` corners, Inter body-md, `{colors.hairline-mid}` border at rest. Focus shifts the border to `{colors.primary}` — a quiet rose signal that ties form interactions back to the brand color. Placeholder text in `{colors.muted}` (#64748b).

**`newsletter-input`** — Full-radius pill for email capture in the footer and editorial callouts. Always paired inline or stacked with a `button-primary`.

### Navigation
**`nav-bar`** — 64px tall, white background, `{colors.hairline}` (#e2e8f0) bottom border. Links in Inter 13px/500 with 0.03em tracking. Active state uses a thin underline at 3px offset — no background highlight or pill treatment, keeping focus on imagery. Cart and search icons right-aligned; logo area uses Ovo display treatment.

### Product Cards
**`product-card`** — White card, `{rounded.sm}` on container and image. Title in `{typography.body-sm}` (Inter 14px/400), price in `{typography.price-sm}` (Inter 14px/500), `{spacing.sm}` gap between image and text. No drop shadow — cards breathe on the grid's white space rather than floating. New and Bestseller labels appear as `product-card-badge` rose pills in `{colors.primary}`.

**`quick-add-button`** — A compact rose pill (36px tall) that surfaces on card hover, overlaid on the image corner. Hidden on touch devices; standard PDP add-to-cart handles the mobile flow.

### Hero
**`hero`** — Full-bleed section with a `{colors.surface-soft}` (#f0dede) background wash. Headline in Ovo `{typography.display-xl}` (48px/400), body copy in Inter `{typography.body-md}`. `{spacing.section}` (64px) vertical padding. On mobile the headline drops to `{typography.display-md}`.

### Collection & PDP
**`collection-banner`** — Section header over a blush surface, `{typography.display-md}` Ovo headline with Inter caption below for category description. Padding at `{spacing.xxl}` top/bottom.

**`pdp-title`** — Ovo `{typography.display-sm}` (24px/400), the first serif element the user reads on a product detail page. **`pdp-price`** follows immediately in Inter `{typography.price-display}` (18px/600) — a serif-to-sans rhythm that reads as editorial without being precious.

### Filters
**`filter-pill`** — `{rounded.full}` pill, white fill, `{colors.hairline-mid}` stroke, Inter caption text. Active state inverts to `{colors.ink}` fill with `{colors.on-dark}` text — binary, no intermediate states or gradients.

### Footer
**`footer`** — Near-black (#121212) background, white text. Column headlines in `{typography.title-sm}` (Inter 14px/600), link rows in `{typography.body-sm}` (Inter 14px/400). Generous vertical padding at `{spacing.xxl}` with `{spacing.section}` horizontal padding on desktop. Newsletter email capture sits above the link columns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to `display-md`; nav collapses to hamburger + logo + cart; filter pills scroll horizontally; quick-add hidden |
| Tablet | 744–1128px | Two-column product grid; nav may remain full or semi-collapsed depending on category depth; hero splits text-left / image-right |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav; hero runs full-bleed with centered or left-anchored text overlay |
| Wide | > 1440px | Content centers in a ≈1440px max-width container; side margins grow; product grid stays at four columns |

### Touch Targets
- All buttons minimum 44px tall (48px preferred) to meet WCAG touch sizing
- Filter pills padded to minimum 44px tap height on mobile via increased vertical padding
- Nav icons (cart, search, hamburger) minimum 44×44px tap area
- Product cards have full-card tap area on mobile, not just the title or image link

### Collapsing Strategy
- Primary navigation collapses to a left-sliding drawer at < 744px
- Category filter tabs condense to horizontal scroll strip on mobile rather than wrapping rows
- Footer link columns stack vertically on mobile; accordion expand is optional
- PDP image gallery collapses to a swipeable single-image carousel on mobile; desktop shows stacked vertical scroll or two-column grid

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom wordmark or logo file — Ovo is the closest match from extracted fonts but the logotype may use a separate asset or custom lettering; verify before rendering the logo as text
- The #2563eb blue appears in extracted palette but likely originates from Shopify admin or a framework default; no brand UI use-case identified and excluded from all tokens
- Exact button padding, input height, and card gap values not DOM-measured — estimates follow the 48px accessibility baseline and common Shopify theme patterns
- Animation easing curves and transition durations not extractable from static extraction snapshot
- Dark mode or alternate seasonal theme not observed; site appears single-theme
- Exact letter-spacing and optical sizing on Ovo display headings not captured from live CSS; values here are editorial estimates calibrated to the font's published metrics
- Cart drawer, search overlay, mobile nav drawer, and modal overlay styles not confirmed from extraction
