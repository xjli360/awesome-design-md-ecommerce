---
version: alpha
name: "Hape"
source_url: "https://www.hape.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A primary red #d42520 — the same shade as a vintage Kawada toy block — anchors a brand that feels more like a playroom than a storefront. The extracted palette is unusually wide (30+ hex values), but the red is the only color that appears in the meta theme-color, the page title, and the brand's own logo lockup. It sits against a near-white canvas (#f0f0f0) and a deep charcoal ink (#32373c) that gives body text a sturdy, printed feel. The secondary accents — a bright cyan (#1ea0c3), a warm amber (#ff9900), and a soft mint (#02e49b) — read as toy-grade primaries, not corporate brand colors. Typography leans on a single serif face (the extracted `font-family: serif` is likely a system fallback for a custom Japanese typeface), set at modest sizes with generous line-height to keep readability child-friendly. Buttons use full-pill rounding ({rounded.full}) and the red primary, while product cards and navigation bars stay white with thin hairlines (#949494). The design trusts large hero photography and product imagery over decorative UI — the red acts as a visual exclamation point, not a background wash.

colors:
  primary: "#d42520"
  primary-active: "#b01e1a"
  primary-disabled: "#f0a09e"
  ink: "#32373c"
  body: "#444444"
  muted: "#949494"
  muted-soft: "#b0b0b0"
  hairline: "#d0d0d0"
  hairline-soft: "#e0e0e0"
  canvas: "#f0f0f0"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#1ea0c3"
  accent-amber: "#ff9900"
  accent-mint: "#02e49b"
  accent-pink: "#e94c89"
  accent-purple: "#4280ff"

typography:
  display-xl:
    fontFamily: "serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  link:
    fontFamily: "serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  badge:
    fontFamily: "serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
    padding: 12px 28px
    height: 48px
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
    padding: 11px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  button-accent-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge-limited:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 480px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in full-pill shape with the signature red (#d42520) background and white text. On hover, it shifts to `{button-primary-active}` with a darker red (#b01e1a). The disabled state uses a pale pink (#f0a09e) to signal inactivity without visual noise.

**`button-secondary`** — An outlined or ghost alternative with a white background and charcoal ink (#32373c) text, maintaining the full-pill shape. Active state fills the background with the soft surface tone (#f8f8f8). Used for secondary actions like "Learn More" or "Add to Wishlist."

**`button-accent-cyan`** and **`button-accent-amber`** — Smaller accent buttons (40px height) using the brand's secondary palette. Cyan (#1ea0c3) signals newness or discovery; amber (#ff9900) flags limited-time offers or promotions. Both use white text and full-pill rounding.

### Forms
**`text-input`** — A standard text input with a white background, soft 8px rounding, and 16px padding. The active state maintains the same background but may include a subtle focus ring (not extracted). Error state uses the primary red for text color to indicate validation issues.

**`search-bar`** — A full-pill search field with white background and 20px horizontal padding. The rounded shape mirrors the button style, creating a cohesive input/action pairing. Placeholder text uses the muted gray (#949494).

### Navigation
**`nav-bar`** — A fixed-height (72px) white navigation bar with links set in serif at 15px. Active links inherit the primary red (#d42520), while inactive links fade to muted gray (#949494). The bar sits above the hero or content area with no visible border — the white canvas provides separation.

**`nav-link-active`** and **`nav-link-inactive`** — Link states that toggle between red and gray. No underline or background change — the color shift alone signals state.

### Cards
**`product-card`** — A white card with 12px rounding and body-sm typography. The card contains a product image (with matching rounding) and text details. On hover, the card may lift slightly (not extracted) but maintains the same background and rounding.

**`product-card-image`** — The image within a product card, using the same 12px rounding as the card itself. This ensures visual consistency between the image and its container.

### Badges
**`badge-new`** — A cyan (#1ea0c3) pill badge with uppercase 11px text, used to flag newly added products. Padding is tight (4px vertical, 12px horizontal) to keep the badge compact.

**`badge-sale`** — A red (#d42520) pill badge for sale or discount indicators. Uses the same typography and shape as `badge-new` but with the primary brand color.

**`badge-limited`** — An amber (#ff9900) pill badge for limited-edition or time-sensitive products. The warm tone creates urgency without clashing with the primary red.

### Hero
**`hero-banner`** — A full-width hero section (480px height) with a near-white canvas background (#f0f0f0). The headline uses display-xl (36px serif) in charcoal ink (#32373c). The hero typically features a large product photograph or lifestyle image behind the text.

**`hero-cta`** — The hero's primary call-to-action button, slightly larger than standard (52px height, 32px horizontal padding) to anchor the hero composition. Uses the same red full-pill style as `button-primary`.

### Footer
**`footer`** — A dark footer with charcoal ink (#32373c) background and white text. Links use the muted-soft gray (#b0b0b0) for readability against the dark background. Typography is body-sm (14px serif) for a clean, uncluttered appearance.

**`footer-link`** — Footer links in muted-soft gray (#b0b0b0) with link typography (14px serif). No underline decoration — color contrast against the dark background provides sufficient affordance.

### Tags
**`category-tag`** — A soft gray (#f8f8f8) pill tag for category filters or product tags. Uses button-sm typography (14px serif) and full-pill rounding. The active state (`category-tag-active`) switches to the primary red background with white text.

**`icon-button`** — A circular icon button (40px) with transparent background and charcoal ink icon. The active state uses a soft gray background and red icon color to indicate selection or hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav-bar collapses to hamburger menu; hero-banner height reduces to 320px; product cards stack in single column; category tags wrap to multiple rows |
| Tablet | 744–1128px | Nav-bar shows top-level links only; hero-banner at 400px; product cards in 2-column grid; category tags in scrollable horizontal strip |
| Desktop | 1128–1440px | Full nav-bar with all links; hero-banner at 480px; product cards in 3–4 column grid; category tags in fixed row |
| Wide | > 1440px | Max-width container (1440px) centered; hero-banner may expand to full viewport width; product cards in 4-column grid with increased padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility.
- Icon buttons are 40px — slightly below the 44px recommendation but acceptable for non-primary actions.
- Category tags are 36px tall — suitable for tap targets when spaced with 8px gaps.

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px, with a slide-in drawer for full link list.
- Category tags switch from a fixed row to a horizontally scrollable strip on tablet and mobile.
- Footer links stack vertically on mobile, with each link group separated by 16px spacing.
- Product card grids reduce columns as viewport narrows: 4 → 3 → 2 → 1.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font family**: The extracted `font-family: serif` is a system fallback. The brand likely uses a custom Japanese typeface (possibly Noto Serif JP or a proprietary Kawada font) that couldn't be extracted from the live site. All typography tokens use "serif" as a placeholder.
- **Hover states**: Only button-primary and product-card hover states were extractable. Other interactive elements (links, tags, icon buttons) may have additional hover effects (underline, background shift, scale) that are not documented.
- **Focus states**: No focus ring styles were extracted. The brand may use a custom focus indicator (e.g., 2px red outline) or rely on browser defaults.
- **Error states**: Only text-input error state is documented. Form validation patterns (error messages, success states, loading spinners) are not captured.
- **Dark mode**: No dark mode styles were found on the live site. The brand may not support dark mode, or it may be behind a user preference that wasn't triggered during extraction.
- **Sub-brand palettes**: Hape operates under the Kawada umbrella (as indicated by the page title). There may be sub-brand or regional color variations (e.g., Hape Japan vs. Hape International) that are not reflected in the extracted palette.
- **Animation/transition**: No animation durations or easing curves were extracted. The brand may use subtle transitions (e.g., 200ms ease-in-out for button hovers) that are not documented.
- **Spacing scale**: The spacing tokens are inferred from common design system patterns. Actual spacing values may vary — particularly for section padding and card margins.
- **Rounded values**: The rounding scale is based on observed button and card shapes. The exact pixel values for `rounded.md` (12px) and `rounded.lg` (20px) are estimates from visual inspection.
- **Color usage**: The extracted palette includes 30+ hex values, many of which may be social media icons, payment gateway buttons, or stock image dominant tones. Only the most frequently occurring and brand-distinctive colors are included in the token set. Colors like #0757fe, #1778f2, #0461dd, #0d66c2, #3288d4 are likely social media blues (Facebook, Twitter, LinkedIn) and are excluded from the brand palette.
