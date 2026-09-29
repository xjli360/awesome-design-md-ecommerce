---
version: alpha
name: "Uni-ball"
source_url: "https://uniballco.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Four ink colors run through the Uni-ball palette exactly as they do through a capped marker set: coral (#ec7965), teal (#108474), maroon (#8b1538), and golden yellow (#f7c970) map directly to the pigment breadth across the product catalog, making the interface itself a demonstration of what these pens can produce. Primary surfaces anchor on a near-black charcoal (#292933) against clean off-whites (#f5f5f5, #f9fafb), giving the color accents the same contrast you would see inked onto white cartridge paper. The teal (#108474) is the brand's primary action color — an unusual choice in a category that defaults to corporate navy — and carries every Add-to-Cart button, hover state, and interactive focus ring. A secondary coral (#ec7965) surfaces in promotional callouts and editorial highlight strips, while maroon (#8b1538) and golden yellow (#f7c970) serve as collection and category accent badges, extending the brand's pen-color logic into page furniture. Typography defaults to the system sans stack — the only custom font detected in the extraction is a review-widget glyph font — keeping the reading experience clean and neutral, trusting product photography and the ink-color system to carry the visual identity. Buttons use `{rounded.sm}` across all sizes, inputs match, and product cards take `{rounded.md}`, landing in a disciplined register that signals precision without the hard 0px edges of luxury goods or the pill-shaped softness of consumer lifestyle brands. A light teal wash (`{colors.surface-teal}`) appears as a soft background for category sections, connecting structural UI back to the ink-color logic. Color swatch chips and ink-type badges — rendered as small `{rounded.xs}` pills — serve as the primary SKU differentiator across product listings: the right color, the right surface, the right chemistry, communicated without prose.

colors:
  primary: "#108474"
  primary-active: "#0a6358"
  primary-disabled: "#edf5f5"
  accent-coral: "#ec7965"
  accent-coral-active: "#d45e50"
  accent-maroon: "#8b1538"
  accent-maroon-deep: "#7b1830"
  accent-yellow: "#f7c970"
  accent-red: "#db3d34"
  ink: "#292933"
  ink-deep: "#211f1f"
  body: "#302f2f"
  muted: "#7b7b7b"
  muted-soft: "#a4a4a4"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f9fafb"
  canvas-neutral: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#f9f9f9"
  surface-teal: "#edf5f5"
  on-primary: "#ffffff"
  on-dark: "#f5f5f5"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
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
    padding: 12px 24px
    height: 46px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 46px
  button-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 46px
  button-coral-active:
    backgroundColor: "{colors.accent-coral-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline-soft}"
    height: 64px
    logoHeight: 32px
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  hero-banner-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  ink-badge:
    rounded: "{rounded.xs}"
    size: 20px
    border: "2px solid {colors.hairline}"
    borderSelected: "2px solid {colors.ink}"
  ink-type-tag:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  collection-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  collection-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid transparent"
    padding: "{spacing.sm} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    iconColor: "{colors.muted}"
  promo-strip:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  promo-strip-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-grid:
    columns: 4
    gap: "{spacing.lg}"
    padding: "{spacing.section} {spacing.xl}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    padding: "{spacing.lg}"
    border: "none"
  footer:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Teal (#108474) fill, white text at `{typography.button-md}` weight, `{rounded.sm}` corners, 46px tall. Hover shifts to `{colors.primary-active}` (#0a6358) with no scale or shadow transform — interactions stay flat and precise. Disabled state uses the light teal surface `{colors.primary-disabled}` with `{colors.muted}` text, preserving the teal family signal without implying interactivity.

**`button-secondary`** — Off-white canvas background with a 1.5px `{colors.ink}` border; mirrors primary sizing at 46px. Used for secondary actions on product pages (Add to Wishlist, Compare, View Details). On hover the border transitions from `{colors.ink}` to `{colors.primary}`, grounding secondary actions in the brand teal without competing with the primary CTA.

**`button-coral`** — Coral (#ec7965) fill with white text; deployed in promotional and marketing contexts where the teal would read as too utilitarian. Active state deepens to `{colors.accent-coral-active}`. Intentionally kept off the product page — coral signals campaign energy, not transactional completion.

### Product Card
**`product-card`** — `{colors.surface-card}` background with a soft `{colors.hairline-soft}` border and `{rounded.md}` corners. Product image renders on a `{colors.surface-soft}` stage within the card, keeping pen photography on a consistent neutral field. Title uses `{typography.title-sm}`, price `{typography.price}` in bold below. Ink-type tags (`ink-type-tag`) stack beneath the title, surfacing ink chemistry — gel, pigment, water-resistant — before the customer reaches the detail page. On hover, the card border lifts to `{colors.hairline}`.

### Ink Badge & Color Swatches
**`ink-badge`** — A 20×20px `{rounded.xs}` swatch chip rendering the physical ink color of each SKU. Resting state shows a `{colors.hairline}` border ring; selected state upgrades to a `{colors.ink}` ring to mark the active choice without requiring a fill change. The chip color itself is the product's actual ink hex rather than a palette token — the interface borrows from the physical product, not the design system.

**`ink-type-tag`** — Small all-caps label on `{colors.surface-teal}` in `{colors.primary}` text, `{rounded.xs}`, carrying the ink chemistry descriptor (e.g. "PIGMENT INK", "GEL", "ARCHIVAL"). The teal background is a deliberate callback to the primary brand color, making chemistry information feel native rather than appended. Appears below the product name in both listing and detail views.

### Navigation
**`nav-bar`** — 64px tall, `{colors.canvas}` background with a 1px `{colors.hairline-soft}` bottom border. Logo left-anchored, primary navigation links in `{typography.nav-link}` spanning product categories, search icon and cart count badge at the far right. A `{colors.ink}` count bubble in `{typography.badge}` appears on the cart icon when items are present. The `nav-bar-dark` variant swaps to `{colors.ink}` background with `{colors.on-dark}` text for hero sections that bleed behind the nav.

**`collection-tab-active / inactive`** — Horizontal tab strip beneath the nav for collection or category filtering. Active state shows a 2px `{colors.primary}` underline with full `{colors.ink}` text; inactive tabs use `{colors.muted}` text and a transparent underline. No background fill on either state — the underline alone carries the selection signal, keeping the tab rail visually light.

### Hero
**`hero-banner`** — Full-width dark-field banner on `{colors.ink}` with headline in `{typography.display-xl}` white and supporting copy in `{typography.body-md}`, minimum 480px height. The ink-black canvas makes the pen photography and color accents read at maximum contrast. The `hero-banner-teal` variant swaps the dark field for `{colors.primary}` teal, deployed for collection launches and seasonal promotions where warmth is preferred over authority.

### Promo Strip
**`promo-strip`** — Coral (#ec7965) full-width band pinned to the viewport top, centered text at `{typography.label}`. Used for shipping thresholds, flash sales, and new-arrival announcements. The `promo-strip-dark` variant uses `{colors.ink}` background and `{colors.on-dark}` text for limited edition drops that warrant a lower-urgency signal.

### Search
**`search-bar`** — Pill-shaped (`{rounded.full}`) input on `{colors.surface-soft}`, `{colors.muted-soft}` placeholder, soft hairline border. Focus shifts border to `{colors.primary}` teal with no shadow. The pill shape is a deliberate break from the squared button and card system — it reads as exploratory rather than transactional, visually separating browse behavior from buy behavior.

### Sale Badge
**`sale-badge`** — `{colors.accent-red}` fill, white `{typography.badge}` text, `{rounded.xs}`, appearing as an absolute-positioned chip on the product card image corner. Red maps directly to one of the brand's extracted ink colors, so the urgency signal and product identity share the same visual vocabulary.

### Footer
**`footer`** — Deep near-black `{colors.ink-deep}` (#211f1f) background, `{typography.body-sm}` link text in `{colors.muted-soft}` lifting to `{colors.on-dark}` on hover. Generous `{spacing.xxl}` vertical padding. Houses newsletter signup with a `text-input` and `button-primary` inline, link columns (Help, About, Products, Careers), and social icons in the same muted-to-white hover pattern.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger drawer nav over ink scrim; hero stacks headline above full-bleed image; promo strip truncates to one line; collection tabs scroll horizontally with momentum |
| Tablet | 744–1128px | Two-column product grid; nav condenses to icon+label pairs; hero overlays text on image with translucent scrim; search collapses to tap-to-expand icon |
| Desktop | 1128–1440px | Four-column product grid; full horizontal nav with mega-menu dropdowns; hero at full 480px with side-by-side text and image; collection tab rail fully visible |
| Wide | > 1440px | Layout max-width capped ~1440px and centered; section padding scales to `{spacing.xxl}`; hero image expands to fill; no structural layout change beyond margin auto-centering |

### Touch Targets
- All buttons minimum 44×44px; primary CTA buttons span full column width on mobile at 46px height
- Ink swatch badges scale from 20px to 36px on touch screens to meet tap-target minimums
- Collection tab strip items padded to 44px tap height on mobile with horizontal scroll
- Nav icons (search, cart, hamburger) padded to 44px tap area independent of visual icon size

### Collapsing Strategy
- Desktop dropdown nav collapses to left-slide drawer on mobile; drawer overlays with a `{colors.ink}` 60%-opacity scrim
- Four-column product grid collapses 4 → 2 → 1 at tablet and mobile breakpoints; gap narrows from `{spacing.lg}` to `{spacing.md}` at mobile
- Hero shifts from side-by-side (desktop) to text-over-image (tablet) to full-bleed image with text panel below (mobile)
- Promo strip stays fixed at all breakpoints; body copy font-size scales down to `{typography.caption}` on mobile
- Footer link columns reflow 4-across → 2×2 grid on tablet → stacked accordions on mobile; newsletter input stacks above submit button

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand typeface detected — only "JudgemeStar" (a Judgeme review-widget glyph font) was present in the extraction; the actual brand font likely loads via JavaScript or a third-party CDN not captured statically. System sans stack used throughout; verify against a live font inspection.
- `primary-active` (#0a6358) and `accent-coral-active` (#d45e50) are derived by darkening extracted hues ~10%; neither appears in the raw extraction.
- Meta theme-color was absent; likely set dynamically by JavaScript on page load.
- No explicit disabled, focus, or error state colors extracted for form fields; teal-border focus inferred from standard Shopify patterns.
- Icon set and category illustration style not captured; Uni-ball likely uses custom line-art product icons — verify in live DevTools.
- `on-primary` (#ffffff) is inferred as pure white and does not appear in the extracted list; confirm against actual rendered CTA buttons.
- Animation and transition tokens (duration, easing curves) are not recoverable from static extraction; no motion tokens included.
- Maroon (#8b1538) and yellow (#f7c970) roles — whether they are category colors, limited-edition accents, or promotional-only — could not be confirmed from extraction alone.
