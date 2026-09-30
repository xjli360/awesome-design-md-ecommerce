---
version: alpha
name: "Flaus"
source_url: "https://getflaus.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The flosser sitting on the bathroom counter is the entire argument — Flaus built a personal care brand around a single object designed to be too beautiful to put away. That object-first logic runs through every layer of the visual system: a mint-and-white palette that reads more like skincare than oral care, rounded edges that echo the product's soft-grip silhouette, and a typographic voice that speaks in declarative sentences rather than clinical benefit lists. The primary brand color, a vivid seafoam mint estimated at approximately #5BC8A4 (see Known Gaps), is deployed as a true signal color — it appears on primary CTAs, product accent bands, and hover states, never as wallpaper. White (#FFFFFF) does most of the spatial work, giving product photography the same clean void a cosmetics brand would use for a hero serum shot. Secondary surfaces step only slightly off white to a ghosted mint wash (#F4FAF8), keeping the overall register light and airy without flattening into sterile. Body text sits in near-black (#1A1A1A), and muted copy drops to a medium gray (#767676) — both neutral enough to never compete with the mint. Typography defaults to a geometric sans-serif in the humanist tradition: display sizes run large and confident at weight 600–700, while body copy relaxes to weight 400 at a comfortable 16–17px. Button labels carry a subtle uppercase tracking at small sizes to feel branded rather than default-browser. The `{rounded.xl}` radius on primary buttons and `{rounded.full}` pill shapes on badges and tags reinforce the same soft-edged product aesthetic — nothing in the UI has a hard, utilitarian corner. `{spacing.section}` gaps between homepage modules give the layout room to breathe in a way that justifies a premium price point without requiring a single line of copy to say "premium." The overall register is a DTC oral care brand that grew up wanting to be a beauty brand, and largely succeeded.

colors:
  primary: "#5BC8A4"
  primary-active: "#3AAD8A"
  primary-disabled: "#B8E8D8"
  primary-text-on-light: "#2D9E7A"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#767676"
  muted-soft: "#9E9E9E"
  hairline: "#E0E0E0"
  hairline-soft: "#EFEFEF"
  canvas: "#FFFFFF"
  surface-soft: "#F4FAF8"
  surface-card: "#FFFFFF"
  surface-mint-wash: "#EAF7F2"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  badge-text: "#1A1A1A"
  error: "#D94F4F"
  star: "#1A1A1A"

typography:
  display-xl:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  eyebrow:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.5px

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
    rounded: "{rounded.xl}"
    padding: 14px 28px
    height: 52px
    transition: background-color 150ms ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xl}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xl}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: 13px 27px
    height: 52px
    border: "1.5px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary-text-on-light}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: 12px 20px
    textDecoration: underline
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
    padding: "0 {spacing.xl}"
  nav-bar-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: 12px 16px
    height: 52px
    placeholderColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    border: "none"
    shadow: "0 2px 12px rgba(0,0,0,0.07)"
    hoverShadow: "0 6px 24px rgba(0,0,0,0.12)"
    transition: "box-shadow 200ms ease, transform 200ms ease"
    hoverTransform: "translateY(-2px)"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    paddingY: "{spacing.section}"
    ctaGap: "{spacing.sm}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary-text-on-light}"
    maxWidth: 680px
  feature-badge:
    backgroundColor: "{colors.surface-mint-wash}"
    textColor: "{colors.primary-text-on-light}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 5px 12px
    border: "1px solid {colors.primary-disabled}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.base}"
    iconColor: "{colors.primary}"
  review-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    starColor: "{colors.star}"
    authorTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    border: "1px solid {colors.hairline-soft}"
  benefit-strip:
    backgroundColor: "{colors.surface-mint-wash}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    paddingY: "{spacing.md}"
    iconColor: "{colors.primary}"
    gap: "{spacing.xxl}"
  bundle-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.display-sm}"
    labelTypography: "{typography.eyebrow}"
    labelColor: "{colors.primary-text-on-light}"
    borderSelected: "2px solid {colors.primary}"
    borderDefault: "2px solid {colors.hairline}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    buttonSize: 36px
    border: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
  sticky-add-to-cart:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
    buttonFullWidth: true
    shadow: "0 -4px 16px rgba(0,0,0,0.06)"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    paddingY: "{spacing.section}"
    dividerColor: "#2E2E2E"

## Components

### Buttons

**`button-primary`** — The primary CTA renders in Flaus's signature mint (#5BC8A4) on a 52px-tall pill-adjacent shape (`{rounded.xl}`, 32px radius). Label weight is 600 at 15px with a gentle 0.2px tracking to keep it branded. Hover darkens to `{colors.primary-active}` (#3AAD8A) over 150ms; disabled washes to the pale `{colors.primary-disabled}` (#B8E8D8) with a not-allowed cursor. No uppercase transform — the brand speaks in sentence case.

**`button-secondary`** — White fill with a 1.5px ink border and matching `{rounded.xl}` radius keeps secondary actions visually paired with primary. Ink (#1A1A1A) label at the same 15px/600 spec; hover may invert to ink fill with white text at the implementation layer.

**`button-ghost`** — Used for low-priority nudges (e.g., "Learn more," "See all reviews"). Transparent background, mint-on-light text (#2D9E7A), underline decoration. No border.

**`button-pill`** — Compact pill (`{rounded.full}`) at 36px height for inline contexts: badge-adjacent CTAs, nav bar shop button, floating chips. Button-sm typography with tight uppercase tracking.

### Navigation

**`nav-bar`** — 68px white bar with a 1px hairline bottom border. Logo anchored left at 28px height. Navigation links centered in humanist 15px/500. Cart icon and a mint pill CTA ("Shop Now" or "Get Flaus") anchored right. On scroll, bar gains a soft drop shadow rather than changing color, keeping the white-on-white relationship intact.

### Product Card

**`product-card`** — White card, `{rounded.lg}` corners, a subtle 2px lift shadow that deepens and rises 2px on hover over 200ms — the motion echoes picking up the physical product. Image fills the top portion with `{rounded.md}` clip. Title in `{typography.title-md}` and price in `{typography.title-sm}` both in ink. Feature badges (`{feature-badge}`) may float over the image corner in mint-wash with a mint border.

### Hero

**`hero-section`** — White canvas, copy left-aligned, product render or lifestyle photo right-aligned in a 50/50 split on desktop. Headline at `{typography.display-xl}` (52px/700). An eyebrow label in uppercase mint above the headline anchors the product category without cluttering. Two CTA buttons side by side: primary mint, secondary outlined. Section padding `{spacing.section}` top and bottom.

### Trust & Social Proof

**`benefit-strip`** — A full-width mint-wash band (`{colors.surface-mint-wash}`) below the hero carries 3–4 short benefit statements with mint icon glyphs, separated by `{spacing.xxl}` horizontal gaps. Caption-size text, no heading — it reads as ambient proof rather than a sales argument.

**`review-card`** — Lightly bordered card (`{rounded.lg}`) with star row in ink, author name in `{typography.title-sm}`, and review body in `{typography.body-sm}` body color. Arranged in a 3-column grid on desktop, single column on mobile, with 24px gaps.

**`trust-badge`** — Small surface-soft tile with a mint icon (recycled packaging, dentist-recommended, etc.) and a single caption line. Appears in a horizontal row below product detail or in the footer zone.

### Bundles & Purchase UX

**`bundle-card`** — Rounded XL card in surface-soft with a 2px border that switches from hairline to mint when selected. Eyebrow label in uppercase mint names the tier ("Starter," "Complete Kit"). Title in `{typography.display-sm}`. Used in a horizontal scroll or 2-column grid for multi-SKU selection.

**`quantity-selector`** — Compact minus/plus control in a surface-soft pill with `{rounded.md}`. Active button color is mint. Quantity number in `{typography.title-sm}`. Placed inline with the add-to-cart row.

**`sticky-add-to-cart`** — Fixed bottom bar on mobile PDP, white fill, 1px hairline top, soft upward shadow. Full-width mint primary button fills the interior. Appears after user scrolls past the above-fold CTA.

### Footer

**`footer`** — Deep ink (#1A1A1A) background, white headings, muted-soft (#9E9E9E) links that lighten to white on hover. Four-column grid on desktop, stacked on mobile. Section padding top and bottom with a slightly darker internal divider (#2E2E2E) above the legal row.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; hero stacks copy over image; nav collapses to hamburger + cart icon; benefit strip scrolls horizontally; sticky add-to-cart bar visible on PDP |
| Tablet | 744–1128px | 2-column product grid; hero remains split but at tighter padding; nav shows links without hamburger; bundle cards scroll horizontally |
| Desktop | 1128–1440px | 3-column product grid; hero at full 50/50 split; nav fully expanded with pill CTA; benefit strip static row |
| Wide | > 1440px | Max content width clamped ~1360px; outer margins grow symmetrically; hero image scales up within fixed column bounds |

### Touch Targets

- All interactive controls minimum 44×44px on mobile
- Quantity selector buttons at 36px desktop / 44px mobile
- Nav hamburger 44×44px tap area with 8px inner icon
- Product card entire tile is tappable; no separate "Add" micro-button on mobile grid view

### Collapsing Strategy

- Hero: image moves below copy block on mobile, retains aspect ratio; headline drops from 52px to 32px (`{typography.display-md}`)
- Benefit strip: horizontal overflow-x scroll with snap points, no wrap
- Bundle cards: horizontal scroll on mobile, no grid collapse
- Footer: 4-column → 2-column at tablet → single stacked accordion on mobile
- Nav: links hidden behind hamburger below 1128px; cart icon always visible

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All hex colors are brand-knowledge estimates** — the site returned no extractable color tokens (likely JS-injected CSS variables or anti-bot blocking). The mint primary (#5BC8A4), active state (#3AAD8A), and all surface values should be verified against the live site's computed styles before implementation.
- **Font stack unconfirmed** — zero font-family declarations were extracted. The `Inter`/`DM Sans` stack is a reasonable geometric-humanist placeholder; the actual typeface (potentially a licensed custom font) must be confirmed from the site's network waterfall or brand style guide.
- **Exact button radius unknown** — `{rounded.xl}` (32px) is inferred from product photography silhouette logic; actual CSS border-radius should be inspected.
- **No theme-color meta tag present** — could not confirm primary brand color from a meta signal; mint estimate is based on widely available brand imagery and packaging.
- **Dark mode support unknown** — no data on whether a dark-mode palette exists; footer ink values are assumed intentional brand choice rather than a system dark-mode surface.
- **Icon set and illustration style** — no asset extraction possible; icon style (line vs. filled, stroke weight) is unconfirmed.
