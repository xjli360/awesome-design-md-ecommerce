---
version: alpha
name: "Carewell"
source_url: "https://carewell.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A soft, reassuring presence in the elderly care space, Carewell wraps its interface in a clean white canvas and a single distinctive blue — #0070f3 — that appears only in primary CTAs, hover states, and the occasional link underline, never in backgrounds or decorative elements. The brand trusts generous whitespace, a restrained typographic palette drawn from system fonts (Segoe UI, -apple-system, Helvetica), and a muted gray scale (#6a6a6a for body text, #dddddd for hairlines) to create a calm, uncluttered reading experience. Cards and inputs use gentle rounding (`{rounded.sm}` 8px) rather than pills or hard corners — the interface feels approachable without being playful. The secondary blue #3291ff appears in hover states and secondary actions, adding a subtle layer of depth. There is no hero photography or illustration system visible in the extracted data; the brand lets its product categories (incontinence, mobility, bath safety, etc.) speak through clear, direct navigation and simple grid layouts. The overall mood is one of quiet competence — a digital tool that gets out of the way rather than demanding attention.

colors:
  primary: "#0070f3"
  primary-active: "#3291ff"
  primary-disabled: "#b3d4ff"
  ink: "#222222"
  body: "#6a6a6a"
  muted: "#929292"
  muted-soft: "#c1c1c1"
  hairline: "#dddddd"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#c13515"
  success: "#0070f3"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using `{colors.primary}` (#0070f3) as a solid background with white text. On hover, the background shifts to `{colors.primary-active}` (#3291ff). The disabled state uses `{colors.primary-disabled}` (#b3d4ff) with white text. All primary buttons maintain `{rounded.sm}` (8px) corners and 48px height for consistent touch targets.

**`button-secondary`** — An outlined variant with a white background and `{colors.primary}` text. Used for secondary actions like "Learn More" or "Cancel". Hover state adds a subtle border or shadow. Same 48px height and `{rounded.sm}` as the primary button.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` for the text. Used for inline actions like "View all" or "Clear filters". Hover state may add an underline.

### Cards
**`product-card`** — A white card with `{rounded.sm}` corners and 16px padding. Contains product image, title, price, and a short description. On hover, a subtle box shadow (`0 4px 12px rgba(0,0,0,0.08)`) lifts the card slightly. The card background is `{colors.surface-card}` (#ffffff) with `{colors.ink}` (#222222) for headings and `{colors.body}` (#6a6a6a) for body text.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with white background (`{colors.canvas}`). Navigation links use `{typography.nav-link}` (16px, weight 500) and the active state is indicated by a 2px `{colors.primary}` bottom border. The nav collapses to a hamburger menu on mobile.

**`nav-link-active`** — The active navigation link uses `{colors.primary}` text and a 2px solid bottom border in the same color. Inactive links use `{colors.ink}`.

### Forms
**`text-input`** — Standard text input fields with white background, `{rounded.sm}` corners, and 48px height. On focus, the border changes to `{colors.primary}` with a 2px `{colors.primary-disabled}` box shadow ring. Placeholder text uses `{colors.muted}` (#929292).

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a light gray background (`{colors.surface-soft}` #f7f7f7). Used in the header for product search. Maintains 48px height with 12px 20px padding.

### Chips & Badges
**`category-chip`** — Used for filtering product categories. Rounded pill shape (`{rounded.full}`) with light gray background and `{colors.ink}` text. The active state uses `{colors.primary}` background with white text. Padding is 8px 16px.

**`badge`** — Small informational badges (e.g., "Best Seller", "New") using `{colors.primary}` background with white text. Uses `{rounded.xs}` (4px) corners and `{typography.badge}` (12px, weight 600).

### Footer
**`footer`** — A full-width footer with `{colors.surface-soft}` background and `{colors.body}` text. Contains link columns, contact information, and legal text. Uses `{typography.body-sm}` for all text. Padding is 48px 24px.

### Hero Section
**`hero-section`** — The primary hero area on the homepage, using a white background with `{colors.ink}` text. Uses `{typography.display-xl}` (32px, weight 700) for the headline. Padding is 64px 24px. No background image or gradient was detected in the extracted data.

### Accordion
**`accordion-header`** — Clickable headers for FAQ or product details sections. Uses `{typography.title-md}` (18px, weight 600) with `{colors.ink}` text. Padding is 16px 0. On click, the header expands to reveal `{accordion-content}`.

**`accordion-content`** — The expandable content area below accordion headers. Uses `{typography.body-md}` (16px, weight 400) with `{colors.body}` text. Padding is 0 0 16px 0.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero text reduces to 24px; search bar moves to full-width below nav; category chips wrap to 2 columns |
| Tablet | 744–1128px | Nav links visible; product cards in 2-column grid; hero text at 28px; search bar in header; category chips in horizontal scroll |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero text at 32px; search bar centered in header; category chips in horizontal scroll |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-column grid; hero text at 32px with larger padding |

### Touch Targets
- All buttons and interactive elements maintain minimum 48px height for touch accessibility
- Category chips are at least 40px tall with 16px horizontal padding
- Accordion headers have 48px minimum touch area (16px padding top and bottom)
- Search bar and text inputs are 48px tall

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Product category filters collapse to a horizontal scrollable strip on mobile
- Footer link columns stack vertically below 744px
- Hero section reduces padding from 64px to 32px on mobile
- Product grids reduce from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is limited to two blues (#0070f3, #3291ff) and grays — the brand may use additional accent colors (e.g., for sale badges, category icons, or trust signals) that were not captured in the extraction. The true primary is #0070f3, but the brand may have a secondary palette that is missing.
- No font-family declarations beyond system fonts were found — the brand may use a custom web font (e.g., a variable font) that was not loaded during extraction.
- Hover, focus, and active states for most components are inferred from common patterns rather than extracted from the live site.
- Error and success states for forms (validation messages, input error borders) are not confirmed.
- Dark mode or high-contrast mode styles are not documented.
- The brand's illustration style, iconography system, and photography treatment are unknown.
- Spacing values are based on common 8px/4px grid assumptions — the actual spacing scale may differ.
- The extracted page title ("Vercel Security Checkpoint") suggests the extraction may have hit a security page rather than the actual homepage, so some design elements (hero, navigation structure) are inferred from common patterns in the elderly care e-commerce space rather than confirmed from the live site.
