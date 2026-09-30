---
version: alpha
name: "Kronaby"
source_url: "https://www.kronaby.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every page on kronaby.com opens against uncompromising black — meta theme-color #000000 is the single color reliably extracted from a site otherwise shielded behind a Vercel security checkpoint. That black is not a dark-mode toggle or a seasonal campaign choice; it is the persistent ground state of a Swedish hybrid watch brand that has staked its identity on the idea that a smartwatch can be invisible as a smartwatch. Kronaby's physical watches — Sekel, Apex, Alto, Nord — carry traditional sweeping second hands, date windows, and slim dials that could pass for a purely mechanical piece at a glance. The site mirrors this ethos: a dark canvas where product photography provides the only warmth, where typography is kept light-weight and open-spaced rather than punchy and bold, and where the absence of any glowing notification iconography is itself a design statement. Because the live extraction returned only Vercel's own checkpoint colors (#0070f3, #3291ff — discarded as non-brand) and system-font fallback stacks, the palette and type scale below are reconstructed from Kronaby's documented brand materials and product photography: near-black surfaces, high-contrast white copy, a warm champagne accent (#c8a864) that echoes the gilt indices and sunray dials across the physical product range, and a secondary warm gray for supporting text. Typography defers to the confirmed system stack — -apple-system and Helvetica — in light weights (300–400) with wide letter-spacing at display sizes, the mark of a brand that treats whitespace and restraint as premium signals rather than filling every pixel with feature claims. Components sit in tight zero-radius or near-zero-radius rectangles rather than pill shapes: a brand selling clean dial geometry would not undercut itself with bubbly UI. The overall rhythm is generous — wide section margins, sparse navigation, and a product card that presents the watch against a single color field with minimal text below.

colors:
  primary: "#ffffff"
  primary-active: "#cccccc"
  primary-disabled: "#444444"
  ink: "#ffffff"
  body: "#d0d0d0"
  muted: "#888888"
  hairline: "#2a2a2a"
  canvas: "#000000"
  surface-soft: "#0f0f0f"
  surface-card: "#1a1a1a"
  on-primary: "#000000"
  accent-champagne: "#c8a864"
  accent-champagne-dim: "#8a7040"
  surface-overlay: "rgba(0,0,0,0.72)"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 64px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.04em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.06em
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.08em
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.02em
  tag-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2em
    textTransform: uppercase

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageAspect: "1/1"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 100vh
    layout: split-column
    paddingX: "{spacing.xxl}"
  hero-eyebrow:
    typography: "{typography.tag-label}"
    textColor: "{colors.accent-champagne}"
    marginBottom: "{spacing.sm}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 640px
  hero-subtext:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    maxWidth: 480px
    marginTop: "{spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-champagne}"
    textColor: "{colors.canvas}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  badge-collection:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 4px 10px
  swatch-selector:
    size: 24px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.primary}"
    gap: "{spacing.xs}"
  product-detail-price:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  feature-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    paddingY: "{spacing.md}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
  collection-filter-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid transparent"
    padding: 8px 16px
  collection-filter-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 8px 16px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    paddingY: "{spacing.section}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.base}"

## Components

### Buttons

**`button-primary`** — A solid white rectangle on the dark canvas, zero-radius (`{rounded.none}`), carrying uppercase letter-spaced labels via `{typography.button-md}` (13px, weight 500, 0.12em tracking). On dark backgrounds this inverts the conventional light-site pattern: white is the active foreground, not a neutral surface. Hover shifts to `{colors.primary-active}` (#cccccc); disabled state uses `{colors.primary-disabled}` with `{colors.muted}` text so it recedes into the surface. Height is fixed at 48px with 32px horizontal padding.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` hairline border, pairing cleanly with `button-primary` on the same dark surface. Used for secondary CTAs ("Learn More", "View Collection") that should not compete with a primary add-to-cart. Typography and sizing match `button-primary` exactly.

**`button-ghost`** — Hairline-bordered, `{colors.muted}` text, 40px height. Used for tertiary actions: filter resets, ancillary navigation, and size or color variant selectors. Uppercase 11px at 0.15em tracking (`{typography.button-sm}`) keeps it legible without commanding attention.

### Navigation

**`nav-bar`** — A 72px bar against `{colors.canvas}` black with a subtle `{colors.hairline}` bottom border separating it from the page. Logo anchors left; product family links (Sekel, Apex, Alto, Nord) render in `{typography.nav-link}` at 13px with 0.08em tracking. A right-side cluster holds search, account, and cart icon buttons as 44px touch targets. On scroll the bar stays hard-black — no frosted-glass blur would be consistent with Kronaby's uncompromising dark identity.

### Product Card

**`product-card`** — `{colors.surface-card}` tile with a 2px radius (`{rounded.xs}`), square 1:1 image aspect, and a tight text block below carrying the model name in `{typography.title-sm}` at `{colors.body}` and price in `{typography.price}` at `{colors.ink}`. A `swatch-selector` row sits beneath the image showing available dial and strap combinations as 24px filled circles. On hover, a quiet image-scale animation or a white CTA overlay is expected; the card never introduces new colors or decorative chrome.

### Hero Section

**`hero-section`** — Full-viewport-height dark canvas (min-height 100vh) in a split-column layout: copy on the left half, watch photography bleeding to the right edge. An eyebrow line in `{typography.tag-label}` uppercase at `{colors.accent-champagne}` names the collection or feature callout ("HYBRID. ANALOG. CONNECTED."). The headline follows in `{typography.display-xl}` — 64px at weight 300 — spanning up to 640px. Supporting copy at `{typography.body-md}` in `{colors.muted}` leads into the primary white CTA. The champagne eyebrow is the only warm color on the page; everything else is monochrome.

### Badges

**`badge-new`** — Zero-radius pill-free tag in `{colors.accent-champagne}` fill with `{colors.canvas}` text in `{typography.tag-label}`. Sits in the upper corner of product tiles for new arrivals. The champagne gold echoes the gilt hour-markers and sunray-finished dials in the physical watch range — a rare visual bridge between screen and object.

**`badge-collection`** — Hairline-bordered, transparent background version for collection labels ("SEKEL COLLECTION", "NORD SERIES"). Same `{typography.tag-label}` scale, no fill, `{colors.muted}` text. Used inline with the product name to orient the user within the family hierarchy without adding chromatic noise.

### Swatches

**`swatch-selector`** — 24px full-circle dots (`{rounded.full}`) representing dial colorways and strap materials. The selected swatch gains a 2px `{colors.primary}` ring with a 2px gap between dot and ring, a convention borrowed from jewelry and footwear configurators. Displayed inline beneath the product image in both card and PDP contexts, typically 3–5 options per product.

### Feature Strip

**`feature-strip`** — A horizontal band in `{colors.surface-soft}` separating content sections, with thin `{colors.hairline}` borders top and bottom and `{spacing.md}` vertical padding. Contains 3–4 short smartwatch feature callouts ("Step Tracking", "Sleep Monitoring", "Water Resistant 5ATM", "Smartphone Notifications") in `{typography.caption}` with 0.06em letter-spacing. This substitutes for an icon grid in compact layout, keeping the page from feeling like a feature checklist.

### Collection Filter Tabs

**`collection-filter-tab`** — Borderless by default, `{colors.muted}` text, uppercase 11px (`{typography.button-sm}`). **`collection-filter-tab-active`** gains a 1px `{colors.primary}` border and white `{colors.ink}` text to signal the active category filter. These are zero-radius inline buttons, not pill toggles — consistent with the brand's hard-edge geometry.

### Footer

**`footer`** — `{colors.surface-soft}` with a top `{colors.hairline}` border and `{spacing.section}` (64px) vertical padding. Column headings render in `{typography.title-sm}` at `{colors.body}`, body links in `{typography.body-sm}` at `{colors.muted}`. Typical columns: Shop, Support, About, Social. A newsletter input (`text-input`) and legal text anchor the bottom row. The footer is the one place muted gray reads warmly — a slight step up from pure black that signals the page has ended.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero collapses to stacked layout with full-width watch photography above copy block; nav collapses to hamburger drawer; filter tabs scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; hero uses reduced split-column proportions; nav links may truncate to an overflow menu at narrow tablet widths |
| Desktop | 1128–1440px | Three-column product grid; full split-column hero at designed proportions; nav fully expanded with all family links visible |
| Wide | > 1440px | Max-width container (~1400px) centered on viewport; hero photography scales with container; section padding increases to {spacing.section} horizontal |

### Touch Targets

- All interactive elements target minimum 44×44px hit areas regardless of visual size
- Swatch selectors (24px visual dot) expand touch area with 10px padding on all sides
- Nav bar maintains 72px height on mobile; hamburger icon is at least 44×44px
- Filter tabs gain extra vertical padding on mobile to reach 44px tap height
- CTA buttons are already 48px height — no adjustment needed on touch

### Collapsing Strategy

- Primary nav collapses to a left-side drawer at < 744px; drawer slides over the dark canvas with full category tree and close button
- Product grid steps: 1 col → 2 col at 744px → 3 col at 1128px
- Hero copy column reflows to full-width below the watch photography on mobile; eyebrow and headline stack vertically
- Feature strip wraps to a 2×2 grid on mobile, a single horizontal row on desktop
- Footer columns collapse from a 4-column grid to 2-column at tablet breakpoint and single column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Full palette unextractable**: The live site was blocked by a Vercel security checkpoint. Extracted hex values (#0070f3, #3291ff) are Vercel's own checkpoint UI colors, not Kronaby brand colors — they have been discarded entirely. The color palette above is reconstructed from brand knowledge and product photography.
- **No custom typeface confirmed**: All font stacks extracted are system/framework defaults (-apple-system, Helvetica, Arial). Kronaby may use a licensed geometric sans (e.g., a Neue Haas Grotesk or similar) loaded via CSS not captured by the extraction layer.
- **Champagne accent is inferred**: The accent color (#c8a864) is derived from Kronaby's physical product photography (gilt hour-markers, champagne sunray dials) — it was not extracted from the site and may differ from any digital brand accent.
- **No spacing, radius, or motion tokens confirmed**: Padding, gap, border-radius, and animation values are inferred from Kronaby's premium-minimal aesthetic and comparable Scandinavian watch brand conventions.
- **No cart, checkout, or account UI data**: Form validation states, error colors, and transactional component styling are entirely unconfirmed.
- **Dark-mode vs. light-mode unknown**: Whether the site is dark-only or offers a light-mode variant is unconfirmed. The dark-first palette above is based solely on meta theme-color: #000 and known brand positioning.
- **No confirmed nav structure or footer content**: Link labels, product family tree, and footer column layout are estimated from Kronaby's known product lines (Sekel, Apex, Alto, Nord) and may not match current site information architecture.
