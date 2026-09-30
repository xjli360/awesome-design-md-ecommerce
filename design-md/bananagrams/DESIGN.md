---
version: alpha
name: "Bananagrams"
source_url: "https://bananagrams.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A riot of saturated color erupts from a near-black canvas (#070707), where #00b6a7 teal, #0097cf cerulean, #ab4399 magenta, #faa61a marigold, #f1647d coral, and #cddc29 chartreuse collide like a bag of letter tiles spilled across a table. The brand’s primary voltage is that electric teal (#00b6a7), a hue that feels less like a corporate accent and more like the glow of a neon sign in a game arcade — it powers every primary button, navigation highlight, and product badge. The palette is deliberately unsubtle: six saturated accents that could each be a brand’s entire identity are deployed together, creating a visual language that says “this is a game, not a utility.” White (#ffffff) serves as the canvas for product photography and card surfaces, while the near-black ink (#070707) grounds headlines and body text with absolute contrast. Rounded corners are generous but not pillowy — buttons sit at {rounded.sm} (8px), product cards at {rounded.md} (12px), and the signature search bar at {rounded.full} (9999px), a single friendly gesture in an otherwise angular, grid-based layout. Typography runs a single sans-serif family at moderate weights (500–700), with display sizes at 28px and body text at 16px, letting the color do the heavy lifting. The overall mood is carnival-meets-arcade: loud, joyful, and impossible to ignore, with every design decision calibrated to make picking up a game feel like the start of a party.

colors:
  primary: "#00b6a7"
  primary-active: "#00978a"
  primary-disabled: "#80dbd3"
  ink: "#070707"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#00b6a7"
  accent-cerulean: "#0097cf"
  accent-magenta: "#ab4399"
  accent-marigold: "#faa61a"
  accent-coral: "#f1647d"
  accent-chartreuse: "#cddc29"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
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
  button-accent-magenta:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-chartreuse:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
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
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-limited:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  category-tile-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.accent-coral}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  checkbox:
    accentColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  radio:
    accentColor: "{colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  modal-overlay:
    backgroundColor: "rgba(7, 7, 7, 0.6)"
  modal-content:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand’s signature teal (#00b6a7) and white text. On hover, it shifts to a deeper teal (#00978a); when disabled, it fades to a muted pastel (#80dbd3). The 8px corner radius (`{rounded.sm}`) keeps it friendly without sacrificing clarity. Used for “Add to Cart,” “Shop Now,” and primary navigation actions.

**`button-secondary`** — An outlined variant with a white fill and near-black (#070707) text, maintaining the same 44px height and 8px radius. The border uses `{colors.hairline}` (#cccccc) and darkens to `{colors.ink}` on hover. Ideal for secondary actions like “Learn More” or “View Details.”

**`button-accent-magenta` / `button-accent-marigold` / `button-accent-coral` / `button-accent-chartreuse`** — A family of accent-colored buttons that mirror the primary button’s structure but swap the fill for one of the brand’s saturated accent colors. These are used sparingly for promotional CTAs, limited-edition drops, or category-specific actions. The marigold and chartreuse variants use near-black text for contrast; magenta and coral use white.

**`button-pill-teal`** — A compact, fully rounded pill button (36px tall) used for filter tags, quick-add actions, and mobile navigation. The teal fill and white text echo the primary button but at a smaller scale.

### Navigation
**`top-nav`** — A 72px white bar spanning the full viewport width. Navigation links use `{typography.nav-link}` (14px, weight 600) with a 0.3px letter-spacing for a slightly tighter, more deliberate feel. The active link is underlined by the primary teal; inactive links sit in `{colors.muted}`. The logo (a stylized banana or wordmark) sits left-aligned, with a search icon and cart icon right-aligned.

**`nav-link-active` / `nav-link-inactive`** — Active links inherit the primary teal color; inactive links are muted gray. No background fill — the color shift alone signals state.

### Cards
**`product-card`** — A white card with a 12px radius (`{rounded.md}`) and 16px padding. The image area occupies a 1:1 aspect ratio with a soft gray placeholder background. Below, the title uses `{typography.title-sm}` (14px, weight 600) and the price uses `{typography.body-sm}` (14px, weight 400). Badges (new, sale, limited) overlay the top-left corner of the image.

**`product-card-badge`** — A small, uppercase label (10px, weight 700) with 0.5px letter-spacing, set on a magenta background with white text. The 4px radius (`{rounded.xs}`) keeps it compact. Used for “NEW,” “SALE,” or “LIMITED EDITION” flags.

**`category-tile` / `category-tile-active`** — A 16px-padded tile with a 12px radius, used for category browsing (e.g., “Word Games,” “Family Games,” “Travel Games”). The default state has a soft gray background; the active state fills with the primary teal and inverts the text to white.

### Forms
**`text-input`** — A 48px-tall input with a 1px solid border in `{colors.hairline}` and 12px horizontal padding. On focus, the border shifts to the primary teal. Error states use the coral accent (#f1647d) for the border and an optional error message below.

**`select-dropdown`** — Matches the text-input structure but includes a dropdown arrow icon. The chevron is rendered in `{colors.muted}` and rotates on open.

**`checkbox` / `radio`** — Standard form controls with the primary teal as the accent color. Checkboxes use a 4px radius; radios are circular. Both have a 16px touch target minimum.

**`toggle`** — A 24px-tall pill switch. The inactive state is `{colors.hairline}`; the active state fills with the primary teal. The circular knob is white.

### Feedback & Overlays
**`loading-spinner`** — A 24px rotating circle in the primary teal. Used for async actions (add to cart, loading product lists).

**`tooltip`** — A near-black (#070707) pill with white text, 4px radius, and 4px/8px padding. Appears on hover for icon buttons, truncated text, or feature explanations.

**`modal-overlay`** — A 60% opacity black scrim (#070707) behind modal dialogs. The modal content is a white card with a 12px radius and 24px padding.

**`divider` / `divider-soft`** — A 1px horizontal rule. The standard divider uses `{colors.hairline}` (#cccccc); the soft variant uses `{colors.hairline-soft}` (#e6e6e6). Used between sections, product details, and footer link groups.

### Footer
**`footer`** — A near-black (#070707) section with 48px vertical padding. Text is `{colors.muted-soft}` (#999999) at 14px. Links are underlined on hover and use the same muted-soft color. The footer contains three columns: “Shop” (product categories), “Support” (FAQ, shipping, returns), and “Connect” (social links, newsletter signup).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero section reduces padding to 32px; category tiles become a horizontal scroll strip |
| Tablet | 744–1128px | Two-column product grid; top-nav shows all links but search bar collapses to icon; footer stacks to two columns |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with search bar; footer displays three columns; hero section uses full-width background image |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; hero section centers content with 120px padding |

### Touch Targets
- All interactive elements (buttons, links, form controls) have a minimum touch target of 44x44px on mobile.
- Icon buttons (search, cart, hamburger) are 40x40px with a 24px icon inside.
- Product card images are tappable and link to the product detail page.
- Category tiles in the horizontal scroll strip are 120px wide and 48px tall.

### Collapsing Strategy
- The top navigation collapses from a full horizontal bar on desktop to a hamburger menu on mobile (below 744px).
- The search bar collapses from an expanded input to a magnifying-glass icon on tablet and mobile.
- The footer collapses from three columns on desktop to two columns on tablet and a single column on mobile.
- Product grids collapse from four columns (wide) to three (desktop) to two (tablet) to one (mobile).
- The hero section’s headline reduces from 28px to 20px on mobile, and the CTA button shrinks from 48px to 40px tall.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extracted from the live site; the typography block uses Montserrat as a reasonable sans-serif match for the brand’s bold, geometric style, but this should be verified against the actual site CSS.
- Hover and focus states for all components (beyond buttons and text inputs) are inferred from common patterns rather than extracted.
- Error, success, and warning color tokens are not present in the extracted palette and are not defined.
- Dark mode tokens are not available; the brand appears to use a light-only scheme.
- Sub-brand or seasonal palette variations (e.g., holiday collections) are not captured.
- The extracted hex list includes six saturated accent colors that are likely brand-specific, but their exact usage hierarchy (which accent is used for what purpose) is inferred from the site’s visual prominence rather than documented rules.
- Animation and transition durations (e.g., button hover, modal open) are not specified.
- The brand’s iconography style (line vs. filled, stroke weight) is not documented.
- Typography scale for mobile (e.g., reduced display sizes) is not extracted and should be verified.
