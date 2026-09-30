---
version: alpha
name: "Denon DJ"
source_url: "https://www.denondj.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A black-and-neon stage presence where #0088cc — a cold, electronic cyan — acts as the primary voltage against a deep gray scale of #555555, #777777, and #858585, with #ff5216 and #ff5501 as hot orange accents that signal power states, warning badges, and performance-critical controls. The palette reads like a DJ mixer’s interface: cool blues for connectivity and core functions, warm oranges for cue points and active channels, and a full range of grays from #c1c1c1 to #e8e8e8 that build layered surfaces without competing with the gear photography. The brand’s typography stack defaults to Open Sans and Monserrat — clean, geometric sans-serifs that stay legible under stage lighting — with monospace (Consolas, Courier New) reserved for BPM displays, timecode readouts, and firmware-style data panels. Buttons carry sharp {rounded.sm} corners rather than pills, echoing the angular hardware of DJ controllers and CDJs. The hero section on denondj.com uses full-bleed product imagery against a #f6f6f6 canvas, with cyan CTAs that float above the image rather than sitting inside cards — a deliberate move that makes the software feel as responsive as the hardware. The nav bar is a thin, dark strip (#494949) with white links, mimicking the top panel of a mixer. Product cards use soft borders (#e3e4e4) and generous padding, letting the gear’s own design language — brushed metal, backlit buttons, jog wheels — do the selling. The overall mood is professional, slightly industrial, and unapologetically electronic: this is a brand that trusts its products to be the visual hero and uses color only to guide the performer’s eye under pressure.

colors:
  primary: "#0088cc"
  primary-active: "#006bb4"
  primary-disabled: "#68a8e0"
  ink: "#222222"
  body: "#494949"
  muted: "#777777"
  muted-soft: "#858585"
  hairline: "#c1c1c1"
  hairline-soft: "#e3e4e4"
  canvas: "#f6f6f6"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#ff5216"
  accent-orange-active: "#ff5501"
  accent-green: "#0cc485"
  accent-pink: "#eb2771"
  accent-cyan: "#0ae3eb"
  nav-bg: "#494949"
  nav-text: "#e1e1e1"
  badge-warning: "#ff5216"
  badge-new: "#0cc485"
  badge-sale: "#eb2771"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Monserrat', Arial, Helvetica, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', 'Monserrat', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', 'Monserrat', Arial, Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Open Sans', 'Monserrat', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', 'Monserrat', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Monserrat', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Monserrat', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  monospace-display:
    fontFamily: "'Consolas', 'Courier New', 'Menlo', 'Monaco', monospace"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
  monospace-body:
    fontFamily: "'Consolas', 'Courier New', 'Menlo', 'Monaco', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Open Sans', 'Monserrat', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Open Sans', 'Monserrat', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Monserrat', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.hairline}"
    padding: 10px 22px
    height: 44px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-orange-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-icon-square:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 9px 15px
    height: 44px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-orange}"
    padding: 9px 15px
    height: 44px
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.nav-text}"
    typography: "{typography.nav-link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    padding: "{spacing.base}"
  product-card-title:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  product-card-price:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-warning:
    backgroundColor: "{colors.badge-warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
    padding: "9px 15px"
    height: 44px
  footer-section:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.nav-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.nav-text}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  monospace-data-panel:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.accent-cyan}"
    typography: "{typography.monospace-display}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 6px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 6px
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-knob:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-warning:
    backgroundColor: "{colors.badge-warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's cold cyan (#0088cc) with white text. Uses a sharp 4px radius (`{rounded.sm}`) that echoes the angular hardware of DJ controllers. On hover, shifts to `{colors.primary-active}` (#006bb4) for a subtle darkening effect. Disabled state fades to `{colors.primary-disabled}` (#68a8e0), maintaining readability without misleading the user.

**`button-secondary`** — A bordered variant on a white canvas with a 2px hairline stroke (`{colors.hairline}`). Used for "Learn More" and "Compare" actions that sit alongside primary CTAs. The border provides visual weight without competing with the primary cyan button.

**`button-accent-orange`** — The hot orange variant (`{colors.accent-orange}` #ff5216) reserved for high-stakes actions: "Add to Cart", "Buy Now", and firmware update triggers. On hover, shifts to `{colors.accent-orange-active}` (#ff5501). This orange is the brand's secondary voltage, used sparingly to avoid desensitization.

**`button-ghost`** — A transparent background with cyan text, used for tertiary actions like "View Details" inside product cards. The text color inherits `{colors.primary}` and the button maintains the same 44px height and padding as solid variants for alignment consistency.

**`button-icon-square`** — A 40x40px square button with a soft gray background (`{colors.surface-soft}`) and centered icon. Used for utility actions: search toggle, cart icon, menu hamburger. The icon color uses `{colors.body}` (#494949) for adequate contrast against the light gray fill.

### Cards
**`product-card`** — The primary content container for gear listings. A white surface (`{colors.surface-card}`) with a soft 1px border (`{colors.hairline-soft}` #e3e4e4) and 8px rounded corners (`{rounded.md}`). Padding is 16px (`{spacing.base}`) on all sides. On hover, the border strengthens to `{colors.hairline}` (#c1c1c1) and a subtle box shadow lifts the card — mimicking the way hardware sits on a display shelf.

**`product-card-title`** — The product name inside the card, set in `{typography.title-sm}` (16px, weight 600). Color is `{colors.ink}` (#222222) for maximum readability against the white card surface.

**`product-card-price`** — The price line, set in `{typography.body-md}` (16px, weight 400) with `{colors.muted}` (#777777). The muted gray prevents the price from dominating the product name, keeping focus on the gear itself.

**`product-card-badge`** — Small uppercase labels (11px, weight 700) that flag product status. Three variants exist: green (`{colors.badge-new}` #0cc485) for "NEW", orange (`{colors.badge-warning}` #ff5216) for "BACKORDER" or "LOW STOCK", and pink (`{colors.badge-sale}` #eb2771) for "SALE". Each uses 2px radius corners (`{rounded.xs}`) and tight 2px/8px padding.

### Navigation
**`nav-bar`** — A dark, thin strip (`{colors.nav-bg}` #494949) at 56px height, running full-width across the top of the site. Links are set in `{typography.nav-link}` (14px, weight 600, uppercase, 0.5px letter-spacing) with `{colors.nav-text}` (#e1e1e1). The dark bar creates a visual separation between the brand's identity and the page content, much like the top panel of a DJ mixer.

**`nav-link-active`** — The active page link receives a 2px cyan underline (`{colors.primary}`) and white text (`{colors.on-primary}`). The underline is the only indicator — no background fill, no pill shape — keeping the nav clean and hardware-like.

**`nav-link-inactive`** — Inactive links remain in `{colors.nav-text}` (#e1e1e1) with no underline. On hover, they shift toward white without an underline, providing a subtle brightness cue.

### Forms
**`text-input`** — Standard text input fields use a white canvas (`{colors.canvas}` #f6f6f6) with a 1px hairline border (`{colors.hairline}` #c1c1c1) and 4px radius (`{rounded.sm}`). The 44px height matches button heights for alignment in form rows. On focus, the border thickens to 2px and turns cyan (`{colors.primary}`), providing a clear active state without animation.

**`text-input-error`** — Error state swaps the cyan focus border for an orange one (`{colors.accent-orange}` #ff5216). The orange signals urgency without the red/green accessibility pitfalls, as the brand's error palette is warm rather than alarmist.

**`select-dropdown`** — Matches the text-input styling: 44px height, 4px radius, hairline border. The dropdown arrow is rendered as a CSS pseudo-element in `{colors.muted}` (#777777) to keep the interface clean.

### Search
**`search-bar`** — A 44px tall input with 8px radius (`{rounded.md}`) — slightly rounder than buttons to differentiate the interaction type. Uses a white canvas with a 1px hairline border. On focus, the border thickens to 2px cyan, matching the text-input focus pattern.

**`search-bar-focus`** — The focused state uses the same 2px cyan border as text inputs, ensuring consistency across all form elements. The 8px radius is maintained.

### Footer
**`footer-section`** — A dark footer matching the nav bar (`{colors.nav-bg}` #494949) with 64px vertical padding (`{spacing.section}`). Links are set in `{typography.link}` (14px, weight 400) with `{colors.nav-text}` (#e1e1e1). On hover, links shift to white (`{colors.on-primary}`) for a subtle brightness cue.

**`footer-link`** and **`footer-link-hover`** — Standard and hover states for footer links. The hover state uses white text without underline, maintaining the brand's clean, hardware-inspired aesthetic.

### Data Display
**`monospace-data-panel`** — A dark panel (`{colors.ink}` #222222) with cyan monospace text (`{colors.accent-cyan}` #0ae3eb) used for BPM counters, timecode displays, and firmware version readouts. Uses `{typography.monospace-display}` (24px, weight 700, 1px letter-spacing) with 8px padding (`{spacing.sm}`) horizontally and 16px (`{spacing.base}`) vertically. The 4px radius (`{rounded.sm}`) keeps it consistent with other UI elements.

### Progress & Toggles
**`progress-bar`** — A thin 6px bar with full rounding (`{rounded.full}`) and a soft gray background (`{colors.hairline-soft}` #e3e4e4). The fill uses `{colors.primary}` (#0088cc) with the same full rounding, creating a pill-shaped progress indicator.

**`progress-bar-fill`** — The active fill of the progress bar, inheriting the brand's cyan. The full rounding ensures the fill has rounded ends regardless of width.

**`toggle-switch`** — A 44x24px pill-shaped toggle with a gray background (`{colors.hairline}` #c1c1c1) in the off state. The active state fills with `{colors.primary}` (#0088cc). The knob is a 20px white circle (`{colors.surface-card}`) that slides horizontally within the track.

**`toggle-switch-active`** — The active state of the toggle, using the brand's cyan fill. The knob remains white for clear contrast.

**`toggle-switch-knob`** — The circular knob inside the toggle switch, 20px in diameter with full rounding. White color ensures visibility against both the gray off-state and cyan on-state backgrounds.

### Badges
**`badge-new`** — A green badge (`{colors.badge-new}` #0cc485) for "NEW" product labels. Uses `{typography.badge}` (11px, weight 700, uppercase) with 2px radius (`{rounded.xs}`) and tight 2px/8px padding. The green signals freshness without the urgency of orange or the sale connotation of pink.

**`badge-warning`** — An orange badge (`{colors.badge-warning}` #ff5216) for "BACKORDER", "LOW STOCK", or "PRE-ORDER" labels. Matches the badge-new structure but uses the brand's hot orange for attention.

**`badge-sale`** — A pink badge (`{colors.badge-sale}` #eb2771) for "SALE" labels. The pink is distinctive within the brand's otherwise cool palette, making sale items immediately recognizable.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero text reduces to 28px; search bar becomes full-width; product cards stack vertically with reduced padding (12px); footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduce font-size to 12px; hero uses 32px display; search bar is 60% width; product cards use 16px padding |
| Desktop | 1128–1440px | Three-column product grid; full nav with uppercase links; hero uses 42px display; search bar is 40% width; product cards use standard 16px padding; footer columns display in 3-4 columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero uses 48px display; search bar is 30% width; product cards may show additional metadata (BPM range, connectivity icons) |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons are 40x40px, meeting the 44px touch target recommendation when accounting for padding
- Toggle switches are 44px wide, providing adequate tap area
- Product card tap targets (title, price, CTA) are separated by at least 12px (`{spacing.md}`) to prevent mis-taps
- Nav links on mobile have 48px tap height when expanded in hamburger menu

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with the brand logo remaining centered
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Hero section reduces vertical padding from 64px to 32px on mobile
- Search bar transitions from inline (desktop) to full-width block (mobile)
- Footer columns collapse from 4 columns (desktop) to 2 (tablet) to 1 (mobile)
- Product card badges stack vertically on mobile if multiple badges are present
- Monospace data panels reduce font-size from 24px to 18px on mobile to prevent overflow

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards and buttons were inferred from common patterns; exact box-shadow values and transition durations could not be extracted from the live site
- Error message styling (text color, background, iconography) was not visible in the extracted data; the error input border color was chosen to match the brand's orange accent
- Dark mode is not present on the live site; all extracted colors assume a light theme
- The exact font stack order is uncertain — "Monserrat" appears in the extracted declarations but may be a misspelling of "Montserrat"; "pagebuilder-font" and "porto-icons" are likely theme-specific and not part of the brand's core typography
- Sub-brand or product-line-specific color variations (e.g., Prime series vs. SC series) were not extractable
- Animation durations, easing curves, and micro-interaction details (button press states, card entrance animations) are not documented
- The accent colors (#0cc485, #eb2771, #0ae3eb) appeared in the extracted hex list but their specific usage contexts (badges, data displays, decorative elements) were inferred from industry convention rather than direct observation
- The monospace font usage for data panels is an assumption based on the presence of Consolas and Courier New in the extracted font declarations; actual implementation may use a different monospace face
- Focus ring styles (outline color, offset, width) for keyboard navigation were not extractable
- The nav bar's exact height (56px) is an estimate based on common e-commerce patterns; the live site may use a different value
- Color contrast ratios for accessibility compliance (WCAG 2.1 AA/AAA) have not been verified against the extracted palette
