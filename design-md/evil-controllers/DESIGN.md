---
version: alpha
name: "Evil Controllers"
source_url: "https://www.evilcontrollers.com"
captured_at: "2026-09-28T04:43:54.937730+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Evil Controllers markets modded and custom gaming controllers for PS5, PS4,
  Xbox and accessible gaming setups. The extracted CSS shows a dark-first
  interface: the header and header placeholder are pure black (#000000),
  with a saturated green (#81BD41) used consistently for hover states, link
  focus, and primary buttons, paired with a darker green (#5a852d) on
  button hover. Button text on the green fill is pure black per the
  observed `button.btn` rule, establishing black as an on-primary text
  color in that context. Montserrat is confirmed via multiple selectors
  (nav links, dropdown menus, buttons, inputs) as the primary interface
  typeface; Arial and Open-Sans appear in the broader font stack and are
  treated here as inferred body-copy fallbacks since no body-text selector
  was captured. The wider palette includes cooler and warmer accents
  (blue #0098CE, orange #FF8400/#FF9635, yellow #FFDF66) which are not tied
  to specific selectors in the evidence and are proposed here as sale,
  badge, and callout accents consistent with the sitewide-sale messaging
  in the page text. Neutral grays (#efefef–#959595) are proposed as
  surface and hairline tones for card and form layouts, since no explicit
  surface selectors were supplied. Layout structure (grid columns, spacing
  rhythm) is not observed and is proposed only.

colors:
  primary: "#81BD41"
  primary-hover: "#5a852d"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#959595"
  hairline: "#cccccc"
  surface-soft: "#f9f9f9"
  surface-card: "#efefef"
  on-primary: "#000000"
  accent-blue: "#0098ce"
  accent-orange: "#ff8400"
  accent-orange-alt: "#f98b25"
  accent-yellow: "#ffdf66"
  border-strong: "#3f3f3f"
typography:
  display-xl: {fontFamily: "'Montserrat', sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Montserrat', sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "'Montserrat', sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Open-Sans', Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Open-Sans', Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Open-Sans', Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Montserrat', sans-serif", fontSize: "14px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0.5px"}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.border-strong}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    hoverBackground: "{colors.primary}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  controller-config-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    activeBorder: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components
- **button-primary**: The confirmed green (`#81BD41`) fill with black text mirrors the `button.btn` rule and its uppercase Montserrat label; hover shifts to the darker green (`#5a852d`) with white text, both directly observed.
- **button-secondary**: Proposed black-fill variant for lower-emphasis actions (e.g. secondary CTAs in forms), reusing header ink for visual consistency; hover/focus states are proposed, not observed.
- **text-input**: Inferred layout for form fields (email signup, accessible-request form) using Montserrat per the `input.form-control` font rule; border and radius are proposed defaults.
- **nav-bar**: Reflects the observed black header background and green hover/focus link states; dropdown menus also confirmed to use Montserrat. Mobile collapse behavior is proposed, not observed.
- **product-card**: Represents the featured-controllers grid; white product-name text on a dark tile is confirmed, but the card's own background/border here uses proposed neutral surface tones since the grid container's fill was not captured.
- **hero**: Proposed full-width dark section for homepage promo (e.g. sitewide sale banner), using ink background and canvas text consistent with header treatment; exact hero markup not observed.
- **footer**: Structured from the footer link groups in the page text (Shop, Company, Support, Sign up); dark background is inferred from the site's overall dark chrome, not a captured footer selector.
- **badge**: Proposed sale/percentage-off tag using an unassigned warm accent (`#FF8400`) from the palette, since "50% OFF SITEWIDE" messaging appears in copy but no badge selector was supplied.
- **search**: Proposed light-surface search affordance for the header search icon/overlay mentioned in page text ("Search Close"); styling is inferred, not observed.
- **controller-config-selector**: A category-specific proposed component for choosing controller variant (e.g. Esports Shift vs Master Mod), using the primary green as an active-state border to align with the brand's confirmed accent color.

## Responsive Behavior
Recommended, non-measured breakpoints:

| Breakpoint | Width      | Notes (proposed) |
|-----------|-----------|-------------------|
| mobile    | 0–599px   | Single-column product grid; nav collapses to hamburger/off-canvas menu |
| tablet    | 600–959px | 2-column product grid; header condenses icon menu |
| desktop   | 960–1279px| Full nav-main-menu with dropdown megamenu shown |
| wide      | 1280px+   | Max-width container; featured-controllers grid expands to 4+ columns |

Touch targets are recommended at a minimum 44x44px for buttons and nav items. Dropdown megamenus should collapse into accordion-style panels below tablet width. None of this reflects measured site behavior; it is a proposed responsive strategy consistent with the observed component classes.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction only; no rendered layout, computed spacing, or grid structure was observed.
- Body copy font (Open-Sans vs Arial) is inferred from the font-family stack list; no selector explicitly ties body text to either.
- Card, hero, footer, search, and badge backgrounds/borders are proposed from the general neutral/accent palette, not tied to captured selectors for those exact components.
- All spacing, rounded corner, and breakpoint values are proposed conventions, not measured from the live site.
- Hover/focus/active interaction states beyond `.btn`, nav links, and dropdown links are proposed, not confirmed.
- Mobile/tablet layout behavior (menu collapse, grid reflow) was not observed and is a recommendation only.
- Font licensing/self-hosting status for Montserrat, Open-Sans, and Baskerville was not verified from the supplied evidence.
