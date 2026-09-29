---
version: alpha
name: "Cauldron Films"
source_url: "https://www.cauldron-films.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A film distribution brand that opens with a closed door — the entire site is a single "Opening Soon" page rendered in a muted slate-blue (#557b97) that reads more like a library archive than a movie studio. The palette is deliberately restrained: near-black (#121212) for the single line of body copy, a mid-gray (#444444) for the secondary text, and a warm silver (#dedede) for the hairline that separates the sparse layout from the browser chrome. There are no hero images, no film stills, no trailer embeds — just a centered column of text on a white canvas, the brand name in what appears to be a condensed serif at display scale, and a single CTA button that uses the slate-blue as its fill. The design language is anti-blockbuster: where most film brands lead with spectacle, Cauldron Films leads with absence. The `{rounded.xs}` on the primary button and the `{rounded.sm}` on the input field suggest a system that will eventually support product cards and navigation, but for now the only component that matters is the waitlist signup — a text input and a submit button, both set at `{spacing.lg}` padding to give the form the same breathing room as a gallery wall. The meta theme-color of #557b97 tints the mobile browser chrome, extending the brand's quiet authority into the OS chrome itself. This is a brand that trusts a single color, a single typeface, and a single interaction to carry its entire identity until the cauldron is ready to boil.

colors:
  primary: "#557b97"
  primary-active: "#4a6d86"
  primary-disabled: "#a1bccf"
  ink: "#121212"
  body: "#444444"
  muted: "#666666"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Playfair Display', 'Times New Roman', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', 'Times New Roman', Georgia, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Playfair Display', 'Times New Roman', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.15px
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(85, 123, 151, 0.15)"
  text-input-error:
    border: "1px solid #c13515"
    boxShadow: "0 0 0 3px rgba(193, 53, 21, 0.15)"
  waitlist-form:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
    gap: "{spacing.md}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 100vh
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "2/3"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-genre:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.body}"
    typography: "{typography.link}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
  social-icon-hover:
    textColor: "{colors.primary}"
  loading-spinner:
    border: "3px solid {colors.hairline-soft}"
    borderTop: "3px solid {colors.primary}"
    height: 24px
    width: 24px
    rounded: "{rounded.full}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The single call-to-action on the opening-soon page. Uses the slate-blue fill (`{colors.primary}`) with white text, set at `{rounded.xs}` for a subtle squareness that avoids the friendliness of pills. On hover, darkens to `{colors.primary-active}`; disabled state fades to `{colors.primary-disabled}`. The 44px height matches the text input for a clean form row.

**`button-secondary`** — An outlined variant for secondary actions on future pages (e.g., "Browse Catalog" or "Learn More"). Uses the slate-blue as text and border color on a white background. Active state shifts to `{colors.primary-active}` with a soft background fill.

### Forms
**`text-input`** — The email input for the waitlist signup. Clean white background with a `{colors.hairline}` border, `{rounded.xs}` corners, and 44px height to match the submit button. Focus state adds a subtle blue ring (`{colors.primary}` at 15% opacity) and solid border. Error state uses a warm red (#c13515) with matching ring — the only non-blue accent in the system.

**`waitlist-form`** — The primary interaction on the opening-soon page. A centered column with the text input and submit button stacked at `{spacing.md}` gap, padded with `{spacing.section}` top and bottom to create a generous breathing room on the white canvas.

### Navigation
**`nav-bar`** — A 64px white bar with a bottom hairline, holding the brand name on the left and nav links on the right. The active link uses the slate-blue underline — the only color accent in the navigation. On mobile, the nav collapses into a hamburger menu with a slide-down drawer.

**`nav-link-active`** — The active page indicator: slate-blue text with a 2px bottom border in the same color. Inactive links use `{colors.ink}` with no underline.

### Cards
**`product-card`** — A film release card with a white background, soft border, and `{rounded.sm}` corners. The card holds a 2:3 aspect ratio poster image at the top (`{rounded.xs}`), followed by the film title, director, and year. Hover state adds a subtle shadow and slightly darker border. The card uses `{spacing.base}` padding for a compact but readable layout.

**`badge-new`** — A small slate-blue badge for new releases, using uppercase 11px type at `{rounded.xs}`. Sits in the top-left corner of the product card image.

**`badge-genre`** — A pill-shaped genre tag (e.g., "Horror", "Giallo", "Exploitation") in soft gray with `{rounded.full}` corners. Used in a horizontal strip below the film title on product cards.

### Footer
**`footer`** — A soft gray section (`{colors.surface-soft}`) with muted text and a top hairline. Contains copyright, social links, and secondary navigation. Links use `{colors.body}` for readability. Social icons are circular (`{rounded.full}`) at 36px, with hover state shifting to the slate-blue.

### Loading & Dividers
**`loading-spinner`** — A 24px circular spinner with a gray track and slate-blue leading arc. Used during form submission and page transitions.

**`divider`** / **`divider-soft`** — Horizontal rules at 1px height. The standard divider uses `{colors.hairline}` for strong separation; the soft variant uses `{colors.hairline-soft}` for subtle section breaks.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero text reduces to `{typography.display-lg}`; waitlist form fills full width with `{spacing.base}` padding; product cards stack vertically at full width |
| Tablet | 744–1128px | Two-column product grid; nav links visible; hero retains `{typography.display-xl}` but reduces padding; waitlist form centered at 480px max-width |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at max-width 800px; waitlist form at 480px max-width; footer shows three columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero and waitlist form remain centered at their max-widths; footer expands to four columns |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain minimum 44px height for touch accessibility
- Nav links and social icons have 44x44px tap areas even when visually smaller
- Product cards have full-card tap targets for the primary action (view film)
- Badge and genre tags are not interactive — they are visual-only labels

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px, with a slide-down drawer showing all links
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport narrows
- Footer columns collapse from 4 → 2 → 1, with the copyright line always at the bottom
- Hero section reduces vertical padding on mobile, from `{spacing.section}` to `{spacing.xxl}`
- Waitlist form switches from horizontal row (desktop) to vertical stack (mobile) at 480px breakpoint

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site; the serif (Playfair Display) and sans-serif (Inter) choices are inferred from the brand's editorial tone and common DTC film-distribution patterns — these should be verified against the actual site assets or design files
- Only four hex colors were extracted from the live site, and they form a generic web palette (slate blue, two grays, near-black) — the slate-blue (#557b97) is the most distinctive and is used as primary, but the brand may have additional accent colors (e.g., for genre tags, sale badges, or seasonal campaigns) that are not present on the opening-soon page
- Hover, focus, and active states for all components are inferred from common patterns — actual interaction states should be verified against the live site when it launches
- Error styling for forms (text color, iconography, animation) is not documented — the red accent (#c13515) is borrowed from common error patterns and may not match the brand's actual error language
- No dark mode tokens are defined — the brand may introduce a dark theme for the film-viewing experience or catalog browsing
- Typography scale is speculative beyond the opening-soon page — the brand may use additional weights (e.g., 300 for light body text, 800 for heavy display) or different font families for multilingual support
- Spacing scale is based on common 4px/8px systems — the brand may use a custom scale (e.g., 6px increments) that should be confirmed from design files
- No animation or transition tokens are defined — the brand may use specific easing curves and durations for page transitions, hover effects, or loading states
- The product card, badge, footer, and navigation components are speculative — they represent a reasonable extension of the brand's minimal opening-soon page into a full catalog experience, but the actual component library may differ significantly
- Shopify platform dependencies (checkout widgets, payment buttons, cart UI) are not documented — these may introduce additional colors and components that are outside the brand's direct control
