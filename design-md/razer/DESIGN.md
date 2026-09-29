---
version: alpha
name: "Razer"
source_url: "https://www.razer.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A neon-green voltage (#44d62c) cuts through a blackout canvas (#111111, #222222, #040404) — this is the visual signature of a brand built for competitive gaming, where every pixel serves speed and clarity. The primary green is not an accent; it is the single source of light, used for primary CTAs, active states, category highlights, and the three-headed snake logo that marks every product. The palette is aggressively binary — near-black backgrounds, white text on dark surfaces, and that green as the only chromatic permission. Secondary accents like #ff9c07 (amber) and #c8323c (red) appear sparingly, typically for warning states or limited-edition hardware, while #28aadc (cyan) occasionally surfaces in software UI. Typography runs Open Sans at modest weights (400 for body, 600–700 for headings), set at 14–16px for readability during long sessions, with display sizes rarely exceeding 28px. The system avoids decorative type entirely — every character choice prioritizes legibility at a glance. Corners are sharp (`{rounded.none}`) on hardware imagery and navigation, but inputs and buttons use a small `{rounded.sm}` (4px) radius to prevent visual harshness at scale. The brand's design language is one of controlled intensity: generous padding (`{spacing.lg}`–`{spacing.xxl}`) around content blocks, high-contrast borders (`{colors.hairline}` at #444444 on dark surfaces), and a complete absence of gradient, shadow, or blur effects. Every component feels engineered for reaction time — the interface is a cockpit, not a brochure.

colors:
  primary: "#44d62c"
  primary-active: "#00cc00"
  primary-disabled: "#1b5811"
  ink: "#111111"
  body: "#222222"
  muted: "#555555"
  muted-soft: "#717171"
  hairline: "#444444"
  hairline-soft: "#555555"
  canvas: "#111111"
  surface-soft: "#1a1a1a"
  surface-card: "#222222"
  on-primary: "#111111"
  on-dark: "#ffffff"
  accent-amber: "#ff9c07"
  accent-red: "#c8323c"
  accent-cyan: "#28aadc"
  error: "#d0021b"
  error-bg: "#4e1317"
  link: "#6d9df7"
  white: "#ffffff"
  off-white: "#e6e6e6"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
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
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-tertiary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.white}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.white}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.white}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.white}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.white}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
    border: "1px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.md}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.md}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.white}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.white}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.white}"
    margin: "{spacing.sm} 0 {spacing.xs} 0"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 700
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    padding: "{spacing.section} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.white}"
    marginBottom: "{spacing.lg}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
    marginBottom: "{spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.white}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.white}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 48px
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.white}"
    marginBottom: "{spacing.md}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.white}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-limited:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.white}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.white}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.white}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  quantity-selector-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.white}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.white}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    padding: "{spacing.sm} 0"
  tooltip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.white}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  modal:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.white}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  modal-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.7)"
  notification-success:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.white}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  notification-error:
    backgroundColor: "{colors.error-bg}"
    textColor: "{colors.white}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.error}"
  notification-info:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.white}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.accent-cyan}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  slider:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  slider-thumb:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  slider-thumb-hover:
    backgroundColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  tab-hover:
    backgroundColor: transparent
    textColor: "{colors.white}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.white}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 {spacing.xs}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.white}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  rating-stars:
    textColor: "{colors.accent-amber}"
    fontSize: 14px
  loading-spinner:
    color: "{colors.primary}"
    height: 24px
    width: 24px
  loading-spinner-large:
    color: "{colors.primary}"
    height: 48px
    width: 48px
  skeleton:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    height: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the entire site, rendered in Razer green (#44d62c) with dark text for maximum contrast. On hover, the green deepens to `{colors.primary-active}` (#00cc00). Disabled state drops to a muted green `{colors.primary-disabled}` (#1b5811) with gray text, signaling unavailability without visual noise. All primary buttons use uppercase 14px Open Sans at weight 700 with 0.5px letter spacing — the typography of a command, not a suggestion.
**`button-secondary`** — An outlined variant on a dark card background, using a 2px green border and green text. On hover, the button fills solid green, inverting the color relationship. Used for "Learn More" and secondary purchase paths where visual hierarchy must be preserved without competing with the primary CTA.
**`button-tertiary`** — A text-only button with green label on transparent background. On hover, a subtle `{colors.surface-soft}` background appears. Used for "View Details" links and inline actions where a full button would feel heavy.
**`button-ghost`** — The lightest touch: white text on transparent, used in hero sections and overlays where the background is already dark. Hover reveals a soft surface background and shifts text to green. Typically paired with `{spacing.sm}` padding for compact layouts.

### Cards
**`product-card`** — The primary content container for hardware listings, built on a `{colors.surface-card}` (#222222) background with `{rounded.sm}` corners. Contains an image area, title in `{typography.title-sm}`, and price in green at 700 weight. A `{colors.primary}` badge overlays the top-left corner for new or featured items. Cards use `{spacing.base}` padding and sit on the `{colors.canvas}` (#111111) page background, creating a subtle layered effect.
**`product-card-badge`** — Small green label with dark text, positioned absolutely on the card image. Variants include `badge-sale` (red background for discounts) and `badge-limited` (amber background for limited editions). All badges use 11px bold type with `{rounded.xs}` corners.

### Navigation
**`nav-bar`** — A fixed 72px bar at `{colors.ink}` (#222222) with white nav links in 13px uppercase Open Sans at 600 weight. The Razer logo sits left, primary category links center, and utility icons (search, cart, account) right. Active links glow green (`{colors.primary}`), inactive links sit at `{colors.muted-soft}` (#717171), and hover lifts to full white. No dropdown menus — navigation is flat and immediate.
**`nav-link-active`** — The active state for top-level navigation items, distinguished by green text color. No underline or background change — the color shift alone signals the current section.

### Forms
**`text-input`** — Dark card background (#222222) with a `{colors.hairline}` (#444444) border and white text at 16px. On focus, the border switches to `{colors.primary}` green. Error state uses a red border (`{colors.error}`) on a dark red background (`{colors.error-bg}`). All inputs use `{rounded.sm}` and 48px height for comfortable touch targets.
**`checkbox`** — A 20px square with `{rounded.xs}` and a hairline border. Checked state fills with `{colors.primary}` green. No animation — the transition is instant, matching the brand's no-delay ethos.
**`toggle`** — A pill-shaped switch at 44x24px, using `{colors.hairline}` for off and `{colors.primary}` for on. The circular thumb is white. Used for settings and filters where binary choice is required.

### Hero
**`hero-section`** — Full-width dark canvas (`{colors.ink}`) with `{spacing.section}` vertical padding. The hero title uses `{typography.display-xl}` (28px, 700 weight) in white, with a subtitle in `{colors.muted-soft}` at 16px. A single `hero-cta` button in green anchors the bottom. No carousel — hero content is static and declarative, often featuring a single product hero image bleeding to the edges.

### Search
**`search-bar`** — A dark input field with hairline border, 48px height, and `{rounded.sm}`. Focus triggers green border. The search icon sits left, placeholder text reads "Search Razer..." in white. Results appear in a dropdown panel with the same dark card styling.

### Footer
**`footer`** — A full-width dark section (`{colors.ink}`) with `{spacing.xxl}` vertical padding. Links are `{colors.muted-soft}` at 14px, turning green on hover. Column headings use `{typography.title-sm}` in white. A thin `{colors.hairline}` divider separates content from the legal/copyright row. No newsletter signup — the footer is purely navigational and informational.

### Badges
**`badge-new`** — Green label for new product launches. **`badge-sale`** — Red label for discounts and promotions. **`badge-limited`** — Amber label for limited-edition hardware. All badges share the same 11px bold type, `{rounded.xs}`, and 2px vertical padding. They appear on product cards, category pages, and the top nav for "NEW" indicators.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu. Product cards go single-column. Hero padding reduces to `{spacing.xl}`. Search bar moves to a full-width overlay. Footer columns stack vertically. |
| Tablet | 744–1128px | Nav shows top-level categories only (no sub-links). Product cards display in 2-column grid. Hero maintains `{spacing.section}` padding but reduces title to 24px. Footer displays 2-column layout. |
| Desktop | 1128–1440px | Full nav with all links. Product cards in 3-column grid. Hero at full size. Footer in 4-column layout. Sidebar filters visible on category pages. |
| Wide | > 1440px | Max-width container at 1440px, centered. Product cards in 4-column grid. Additional whitespace on sides. Hero content remains centered with max-width 1200px. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target.
- Nav links have 48px minimum height on mobile.
- Quantity selector buttons are 40x40px.
- Icon buttons are 40x40px with 44x44px touch area via padding.
- Checkboxes and toggles are 20px+ with surrounding 44px tap area.

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with a full-screen overlay menu.
- Product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile).
- Footer collapses from 4 columns → 2 columns → stacked single column.
- Hero reduces vertical padding by half on mobile.
- Search transforms from inline bar to full-screen overlay on mobile.
- Sidebar filters on category pages become a bottom sheet on mobile.
- Breadcrumbs truncate to show only current and parent page on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; actual hover timing and micro-interactions (e.g., button press animation, card lift) could not be extracted.
- Error styling for forms (red border + error-bg background) is based on the presence of #4e1317 and #d0021b in the extracted palette, but exact error message typography and placement are assumed.
- Dark mode is the default and only mode observed; no light mode tokens were extracted.
- Sub-brand palettes (Razer Chroma RGB, Razer Gold, Razer Silver) were not extractable from the main site — these may use additional accent colors beyond the extracted set.
- Font stack is inferred from extracted declarations; exact font weights and sizes are based on common gaming UI patterns and may differ from the live site's actual CSS.
- Component spacing (padding, margin) is estimated from typical gaming hardware e-commerce layouts; exact values may vary.
- No animation or transition durations were extractable — the system uses instant state changes (no fade, no slide) based on the brand's performance-first ethos, but this is an assumption.
- The extracted color list includes several generic web colors (#007eff, #6d9df7, #ebf5ff) that likely belong to third-party widgets (payment buttons, social icons) and are not part of the Razer design system. These have been excluded from the primary palette but noted here for transparency.
