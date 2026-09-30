---
version: alpha
name: "Bach Brass"
source_url: "https://www.bachbrass.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep navy foundation at #000235 anchors a brand built for the orchestral and marching worlds, where gold accents at #e3d18c and #a5842a signal heritage and precision. The primary blue #003399 carries the weight of every primary CTA and navigation element, while a secondary red #a5212d appears sparingly — on sale badges and alert indicators — like a conductor’s warning tap. The canvas is a warm off-white #f4f4f4 rather than pure white, softening the technical precision of instrument photography and giving the site a workshop feel. Typography defaults to Arial across the system, set at modest weights with generous line heights that prioritize readability over display drama — the instruments themselves are the visual heroes. Cards and buttons use gentle rounding at {rounded.sm} to {rounded.md}, never fully pill-shaped, preserving a sense of crafted industrial design. The footer and secondary surfaces shift to #efefef, creating subtle depth without harsh contrast. A muted teal #0066a5 appears in hover states and secondary links, while the deep ink #171a1c handles body text. The overall system reads as serious but not cold — a brass instrument manufacturer that trusts its product photography and heritage markers over trendy UI flourishes.

colors:
  primary: "#003399"
  primary-active: "#022c42"
  primary-disabled: "#cdd7e1"
  ink: "#171a1c"
  body: "#32383e"
  muted: "#636b74"
  muted-soft: "#9fa6ad"
  hairline: "#dde7ee"
  hairline-soft: "#f0f4f8"
  canvas: "#f4f4f4"
  surface-soft: "#efefef"
  surface-card: "#fbfcfe"
  on-primary: "#ffffff"
  gold: "#e3d18c"
  gold-dark: "#a5842a"
  red-accent: "#a5212d"
  teal-link: "#0066a5"
  navy-deep: "#000235"
  green-badge: "#6a7d3f"
  green-badge-bg: "#f2fae0"
  error: "#dc2626"
  dark-surface: "#11165e"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
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
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-gold-active:
    backgroundColor: "{colors.gold-dark}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  text-input-error:
    border: "2px solid {colors.error}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    height: 60px
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    textColor: "{colors.gold}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "0 {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.red-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.green-badge}"
    textColor: "{colors.green-badge-bg}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-heritage:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.gold}"
  hero-section:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  section-header:
    typography: "{typography.display-lg}"
    color: "{colors.ink}"
    padding: "{spacing.section} 0 {spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-gold:
    backgroundColor: "{colors.gold}"
    height: 2px
  accordion-trigger:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg} {spacing.lg}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's signature blue #003399 with white text. Used for "Add to Cart," "Shop Now," and primary form submissions. On hover, shifts to the deeper navy #022c42. Disabled state uses a muted blue-gray #cdd7e1 with gray text to indicate inactivity.

**`button-secondary`** — An outlined variant with a blue border and transparent fill, used for secondary actions like "Learn More" or "View Details." On hover, fills with the primary blue and inverts text to white. Maintains the same 44px height as the primary button for visual consistency in forms.

**`button-tertiary`** — A text-only button with no background or border, used for less prominent actions like "Cancel" or "Skip." The blue text provides clear affordance without competing with primary actions.

**`button-gold`** — A special variant reserved for heritage calls-to-action and premium content sections. Uses the gold #e3d18c with dark text, evoking the brass instrument heritage. On hover, darkens to #a5842a. Typically appears in hero sections and on product detail pages for "Customize" or "Heritage Collection" actions.

### Navigation
**`nav-bar`** — A fixed top navigation bar with a deep navy #000235 background, 72px tall on desktop. Logo sits left-aligned, navigation links are center-aligned with uppercase lettering and 0.5px tracking. On scroll, the bar compresses to 60px and shifts to the primary blue #003399. Active nav links are highlighted in gold #e3d18c.

**`nav-link`** — Uppercase navigation links with generous 16px horizontal padding. The 14px font size with 600 weight provides clear hierarchy without dominating the header. Active state uses gold text to indicate current section.

### Cards
**`product-card`** — A clean white card with 8px rounding that showcases instrument photography. The image occupies the top portion at a 4:3 aspect ratio with rounded top corners. Title and price sit below with 16px padding. On hover, a subtle box shadow lifts the card. No border — the card relies on the white surface against the warm off-white canvas for separation.

**`product-card-title`** — 16px semibold text in the brand's dark ink, providing clear product identification. Sits directly below the image with 16px horizontal and 4px top padding.

**`product-card-price`** — 16px regular weight text in the primary blue, creating a subtle but clear visual cue that the price is actionable. Sits below the title with 16px horizontal and bottom padding.

### Badges
**`badge-sale`** — A compact red badge (#a5212d) with white uppercase text, used to flag discounted instruments. The 11px bold type with 0.5px tracking ensures readability at small sizes. Positioned at the top-left of product card images.

**`badge-new`** — A green badge (#6a7d3f) with a light green background (#f2fae0), used for newly added products. The muted green avoids competing with the red sale badge while still providing clear visual distinction.

**`badge-heritage`** — A gold badge (#e3d18c) with dark text, reserved for instruments from the Heritage Collection or limited editions. The gold directly references the brass instrument finish and brand history.

### Forms
**`text-input`** — Standard text input with a white background, 1px hairline border, and 8px rounding. On focus, the border thickens to 2px and turns primary blue. Error state uses a 2px red border (#dc2626). All inputs maintain a consistent 44px height for alignment with buttons.

**`search-bar`** — A pill-shaped search input with full rounding, used in the header and on search results pages. The rounded shape contrasts with the more angular primary buttons, suggesting a more casual, exploratory interaction. On focus, the border shifts to primary blue.

### Footer
**`footer`** — A deep navy (#000235) footer section with muted gray text (#9fa6ad). Links are 14px regular weight and turn gold on hover. The footer contains four columns: About, Products, Support, and Connect. Social media icons appear in the bottom bar, rendered in white with gold hover states.

### Sections
**`hero-section`** — Full-width hero with deep navy background and white text. The display-xl headline sits at 36px with -0.5px tracking. A gold CTA button provides the primary action point. Background may feature instrument photography or a subtle pattern overlay.

**`section-header`** — 28px bold section titles with -0.25px tracking, used to introduce product categories, collection highlights, and informational sections. Sits above content with 64px top padding and 24px bottom padding.

**`divider`** — A 1px hairline separator used between sections and within product lists. A gold variant at 2px height is used for more prominent visual breaks, such as between the hero and featured products.

**`accordion-trigger`** — Used on product detail pages for specifications, care instructions, and warranty information. White background with 16px padding and 8px rounding. On click, expands to reveal the accordion panel below.

**`accordion-panel`** — The expanded content area below accordion triggers, containing product specifications in body-md type. Maintains the white background for visual continuity.

**`tooltip`** — Dark tooltips with white text, used for icon explanations and technical specifications. The 12px type with 4px padding keeps tooltips compact and unobtrusive.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to 24px; search bar moves to secondary menu; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains full-width with 28px text; footer shows two columns per row |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full 36px display; footer in four columns; side-by-side product detail layout |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; additional whitespace in margins; hero content centered with max-width |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch accessibility
- Navigation links have 16px horizontal padding for comfortable tapping
- Product cards are fully tappable, with minimum 120px height per card
- Accordion triggers have 44px minimum height with 16px padding
- Search bar maintains 44px height with generous internal padding
- Footer links have 8px vertical padding for touch targets

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px, with slide-out drawer from left
- Product grid reduces from 4 columns to 3 to 2 to 1 as viewport narrows
- Hero section reduces font size progressively: 36px → 28px → 24px
- Footer columns collapse from 4 to 2 to 1, with the "Connect" column appearing first
- Search bar moves from inline in nav to a toggleable overlay on mobile
- Product detail page shifts from side-by-side to stacked layout below 744px
- Accordion panels remain functional at all breakpoints, with no collapse needed

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components were inferred from common patterns; exact transition durations and easing curves not extracted
- Error styling for forms (validation messages, error icons) not confirmed from live site
- Dark mode preferences not detected; no dark mode tokens exist
- Sub-brand or collection-specific color palettes (e.g., Artist Series, Heritage Collection) not extracted
- Font family extraction returned only generic system fonts (Arial, sans-serif); the brand may use a custom web font not detected
- Button loading states and disabled styling for secondary/tertiary variants not confirmed
- Focus ring styles (outline, offset, color) not extracted
- Modal and overlay components not observed on live site
- Animation and motion specifications (duration, easing, keyframes) not available
- Print stylesheet behavior unknown
- Accessibility contrast ratios not verified against extracted color pairs
- Social media icon colors may be brand-specific but were filtered as generic
- The extracted color list contains many blues and grays typical of generic web frameworks; the true brand palette may be more limited than the 30+ colors listed
