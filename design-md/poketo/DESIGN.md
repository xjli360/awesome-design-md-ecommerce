---
version: alpha
name: "Poketo"
source_url: "https://www.poketo.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Two anchoring colors do the full tonal work across the Poketo store: a charged periwinkle (#4d65ff) that reads closer to an inkpad stamp than a digital primary, and a deep bottle green (#084935) that carries the brand's more grounded, editorial register. The page title — "Home | Pattern Brands" — reveals that Poketo lives inside a parent portfolio, yet the color identity is resolutely its own. The periwinkle takes hero backgrounds, CTAs, and announcement bars; the green surfaces in footers and secondary callouts. That two-act chromatic architecture is the organizing principle everything else defers to. Font stacks loaded via JavaScript and were not extractable, so typography defaults conservatively to a system sans-serif; based on widely-documented Poketo brand presentations, expect a geometric grotesque in the Aktiv Grotesk register — confident weight at headings, low-contrast body, tight tracking at display sizes, and a small all-caps label style with expanded spacing for category chips and badges.

  Corner radius is one of the more legible signals in the system: buttons and pill-shaped badges run `{rounded.full}` to echo the joyful, product-design-inflected voice, while product image frames stay nearly rectangular at `{rounded.sm}`, keeping photography as clean-edged as a printed catalog page. Section padding is generous — 64px — so that dense grid layouts of notebooks, totes, and calendars never crowd. The color-block hero pattern appears to flip between periwinkle and green depending on promotional context, creating a page rhythm that functions like a two-color risograph print: flat, bold, deliberately un-gradated. Swatches on product cards are small circular chips at `{rounded.full}`, framed by a hairline border against white. Price and product title share the same body weight with no bold differentiation — browsing takes precedence over transactional urgency. The cart drawer slides from the right over a light scrim without claiming its own background color, preserving the canvas beneath. The overall system argues that color is content — every surface assignment is a deliberate chromatic statement rather than a neutral container.

colors:
  primary: "#4d65ff"
  primary-active: "#2e48e8"
  primary-disabled: "#b8c2ff"
  secondary: "#084935"
  secondary-active: "#053326"
  secondary-soft: "#e8f2ed"
  ink: "#111111"
  body: "#333333"
  muted: "#6b6b6b"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f4f5ff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.6px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 34px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  label-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.01em
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.01em
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    border: "1px solid {colors.ink}"
    height: 44px
  button-green:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1:1"
    gap: "{spacing.sm}"
  hero-periwinkle:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    displayTypography: "{typography.display-xl}"
    padding: "{spacing.section}"
    rounded: "{rounded.none}"
  hero-green:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    displayTypography: "{typography.display-xl}"
    padding: "{spacing.section}"
    rounded: "{rounded.none}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 36px
    textAlign: center
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: "3px 9px"
  badge-sale:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: "3px 9px"
  color-swatch:
    rounded: "{rounded.full}"
    size: 20px
    border: "1.5px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    width: 400px
    boxShadow: "-8px 0 32px rgba(0,0,0,0.10)"
  footer:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — A periwinkle (#4d65ff) pill with white text, `{rounded.full}` radius, 44px height, and 12px/28px padding. On hover, the fill deepens to `{colors.primary-active}` (#2e48e8) with no shadow or lift. Disabled state uses the washed `{colors.primary-disabled}` fill, keeping text white. No border or outline variant — the full pill silhouette carries all affordance.

**`button-secondary`** — White fill with a 1px ink border and matching pill radius. Shares height and padding with the primary so the two sit flush when paired side by side. Hover inverts to a very light periwinkle tint drawn from `{colors.surface-soft}`.

**`button-green`** — A deep-green CTA (#084935) reserved for footer regions and secondary promotional modules where the periwinkle hero has already been spent. Same pill geometry as `button-primary`.

### Text Input

**`text-input`** — White background, 1px `{colors.hairline}` border at rest, transitioning to a 1px ink border on focus. Radius is `{rounded.sm}` (8px) rather than the full pill of buttons — a deliberate contrast to read as a form element rather than a navigation affordance.

### Navigation

**`nav-bar`** — White canvas, 60px tall, with a hairline bottom border. Links render at `{typography.nav-link}` (14px/500 weight). The logo sits left; utility icons (search, cart, account) anchor right. No background color shift on scroll — the bar remains flat white to preserve color hierarchy for the hero below it.

### Product Card

**`product-card`** — Square image crop at 1:1 aspect ratio with `{rounded.sm}` corners. Product name in `{typography.body-md}` (16px/400) sits beneath the image with `{spacing.sm}` gap; price follows immediately in `{typography.price}` (15px/500) without bold differentiation. Color swatches appear as 20px circles below the price, each using `{color-swatch}` with a hairline ring. No hover overlay, no quick-add button on desktop — the card is deliberately browse-passive.

### Hero Blocks

**`hero-periwinkle`** and **`hero-green`** — Full-width color blocks that alternate down the homepage, using `{colors.primary}` and `{colors.secondary}` respectively as the entire background. Display text is white at `{typography.display-xl}`, CTAs sit as white-text pills. No gradient, no imagery — the color surface is the content. Section padding is `{spacing.section}` (64px) on all sides, creating generous breathing room.

### Announcement Bar

**`announcement-bar`** — A 36px periwinkle strip pinned above the nav, centered text at `{typography.body-sm}`. Promotional copy and free-shipping thresholds live here. Shares its fill with `{colors.primary}` so the bar and any periwinkle hero below it read as one continuous color plane on first load.

### Badges

**`badge-new`** and **`badge-sale`** — Pill-shaped micro labels at `{typography.label-sm}` (11px/700/uppercase). New badges use periwinkle; sale badges use deep green. Both float in the top-left corner of product card images with 3px/9px padding.

### Category Chips

**`category-chip`** — Pill chips using the soft periwinkle surface (`{colors.surface-soft}`) with `{typography.caption}` text for inactive browse filters. **`category-chip-active`** swaps to the full `{colors.primary}` fill with white text, using identical geometry — no border is added, just the fill swap.

### Cart Drawer

**`cart-drawer`** — Right-anchored slide-in at 400px width. White background, no radius (flush to the viewport edge), with a directional box-shadow to separate it from page content. Closes with an X icon or backdrop tap.

### Footer

**`footer`** — The green (#084935) ground that anchors the scroll. White text on the dark field; heading labels in `{typography.title-sm}` (small caps style), links in `{typography.body-sm}`. Section padding creates a roomy, magazine-footer feel. The sudden shift to the dark green after a periwinkle or canvas session functions as a visual chapter-end.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero display type scales to `{typography.display-md}`; announcement bar wraps to two lines if needed; cart drawer expands to full-screen |
| Tablet | 744–1128px | Two-column product grid; nav shows abbreviated links (Shop, About, Cart); hero type stays at `{typography.display-xl}` but hero padding reduces to `{spacing.xxl}`; category chips scroll horizontally |
| Desktop | 1128–1440px | Three or four-column product grid depending on category; full nav with all text links; hero blocks at full 64px section padding; footer switches to a multi-column layout |
| Wide | > 1440px | Grid capped at max-width ~1280px, centered with auto margins; hero color blocks bleed full-width while text content observes the max-width container |

### Touch Targets

- All buttons minimum 44px height (already set in component specs)
- Color swatches expand to 32px touch targets on mobile while rendering visually at 20px
- Nav icons minimum 44×44px tap zones
- Cart drawer close button at 44×44px regardless of visual icon size

### Collapsing Strategy

- Navigation: hamburger at < 744px; full text links from 744px up
- Product grid: 1 col → 2 col → 3–4 col across breakpoints
- Hero text: `{typography.display-xl}` (52px) on desktop, `{typography.display-md}` (34px) on mobile
- Footer columns stack vertically on mobile; three or four columns on desktop
- Category chip rows become horizontal scroll containers on mobile rather than wrapping to multiple rows

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font families**: No font stacks were extractable from the live build — all typography tokens load via JavaScript bundles or are inlined in CSS-in-JS. All `fontFamily` values currently default to a system sans-serif stack. The actual brand face (likely a geometric grotesque such as Aktiv Grotesk or similar) should be substituted once confirmed from the live stylesheet or brand guide.
- **Extended palette**: Only two hex values were extracted (#4d65ff, #084935). All muted tones, surface colors, hairline values, and disabled states are derived proportionally and should be verified against the live site.
- **Meta theme-color**: No theme-color meta tag was present, which may indicate the brand has not specified a mobile chrome color or it is set dynamically.
- **Hover and focus states**: Interactive state colors beyond primary-active are inferred from standard hue-shift conventions; exact transition timing and easing curves are unknown.
- **Typeface weights and variable axes**: Without confirmed font files, weight ranges and any optical-size or width axes are unknown — the typography scale uses static weight values that may need adjustment.
- **Animation system**: Motion tokens (duration, easing, stagger) are entirely absent from the extraction and are not specced here.
