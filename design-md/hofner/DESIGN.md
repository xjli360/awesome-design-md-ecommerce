---
version: alpha
name: "Hofner"
source_url: "https://www.hofner.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, resonant crimson #680202 anchors the Hofner digital presence — the same shade that has defined the brand's iconic violin and bass finishes for decades, here serving as primary voltage for CTAs, navigation accents, and product highlights against a near-white canvas of #f4f4f4. The palette is deliberately restrained: a warm silver-grey #b3b2b2 for secondary elements, a cooler #aaaaaa for muted text, and a precise #eeeeee for soft surfaces, creating a hierarchy that lets the burgundy carry all emotional weight. Typography runs Lato across the system, from generous display sizes at 700 weight down to compact captions at 400, with the brand's signature italic cut (Lato-BlaIta) reserved for heritage callouts and product-series names. Rounded corners are minimal — {rounded.xs} on cards and {rounded.sm} on buttons — reflecting the precision of luthier craftsmanship rather than friendly consumer softness. The product grid uses a tight 8px gutter ({spacing.sm}) and 16px card padding, echoing the close tolerances of instrument joinery. A secondary accent of muted violet #5f5e97 appears sparingly on limited-edition badges and artist-collaboration tags, adding a subtle counterpoint to the dominant crimson without competing for attention. The overall feel is that of a workshop catalog: clean, authoritative, and deferential to the instruments themselves.

colors:
  primary: "#680202"
  primary-active: "#4d0101"
  primary-disabled: "#c4a0a0"
  ink: "#1a1a1a"
  body: "#404040"
  muted: "#858585"
  muted-soft: "#ababab"
  hairline: "#b8b8b8"
  hairline-soft: "#e8e8e8"
  canvas: "#f4f4f4"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-violet: "#5f5e97"
  accent-violet-soft: "#7c7bad"
  heritage-gold: "#d39e00"
  error: "#bd2130"
  success: "#1e7e34"
  info: "#117a8b"
  warning: "#856404"

typography:
  display-xl:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  heritage-italic:
    fontFamily: "'Lato-BlaIta', 'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: 0.5px
    fontStyle: italic

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 700
  product-card-badge:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-banner-subtitle:
    typography: "{typography.display-sm}"
    textColor: "{colors.on-primary}"
    opacity: 0.9
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(104,2,2,0.15)"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  badge-heritage:
    backgroundColor: "{colors.heritage-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.heritage-italic}"
    rounded: "{rounded.xs}"
    padding: "4px 12px"
  badge-limited:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.xs}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    fontWeight: 600
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's deep crimson #680202 and white text. Used for "Add to Cart", "Buy Now", and primary form submissions. On hover, darkens to #4d0101 (`{colors.primary-active}`). Disabled state uses a muted rose #c4a0a0 (`{colors.primary-disabled}`) with white text. Height is 44px with 12px vertical padding and 24px horizontal, set in Lato Bold 15px with 0.3px letter spacing. Corners are softly squared at `{rounded.sm}` (8px).

**`button-secondary`** — Outlined variant with a white fill, crimson border, and crimson text. Maintains the same 44px height and typography as primary. On hover, fills with crimson and inverts to white text. Used for secondary actions like "View Details" or "Compare Models".

**`button-tertiary`** — Text-only button with no background or border. Crimson text with 12px vertical padding. Used for "Learn More" links and dismissible actions within cards. No rounded corners applied.

### Cards
**`product-card`** — The core product display unit. A white card with `{rounded.xs}` (4px) corners and 16px padding. Contains a 4:3 aspect ratio image with matching 4px rounded corners, a product title in Lato Semi-Bold 16px, and a price in Lato Bold 16px colored crimson. On hover, elevates with a subtle box shadow. Badges (limited edition, new, heritage series) appear in the top-left corner using `{colors.accent-violet}` or `{colors.heritage-gold}` backgrounds.

### Navigation
**`nav-bar`** — Fixed-height 72px white bar with a subtle bottom border. Logo sits left-aligned, nav links center-aligned. Active page links display a 2px crimson bottom border. On scroll, gains a light box shadow for sticky behavior. Mobile collapses to a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — Standard input field with white background, 1px hairline border, and 4px rounded corners. On focus, gains a 2px crimson border with a subtle crimson glow ring. Error state uses a red border (`{colors.error}`). Height is 44px with 10px vertical and 14px horizontal padding. Select inputs follow the same pattern.

### Footer
**`footer`** — Dark footer using `{colors.ink}` (#1a1a1a) background with light grey text. Links are muted grey on default and white on hover. Organized in columns with section headings in Lato Semi-Bold 16px. Contains legal text, social links, and newsletter signup. Padding is 48px vertical and 32px horizontal.

### Hero Banner
**`hero-banner`** — Full-width crimson section used for homepage and collection headers. Contains a large display title (42px, Lato Bold) and a smaller subtitle (22px, Lato Semi-Bold) in white with 90% opacity. Padding is 64px vertical and 32px horizontal. May include a background image overlay at 40% opacity.

### Search
**`search-bar`** — Pill-shaped search input with full border radius, white background, and 1px hairline border. On focus, gains a 2px crimson border with a 3px crimson glow ring. Height is 48px with 8px vertical and 16px horizontal padding. Used in the navigation and on search result pages.

### Badges
**`badge-heritage`** — Gold-background badge using the brand's italic black weight (Lato-BlaIta) for heritage and anniversary product lines. 4px rounded corners with 4px vertical and 12px horizontal padding.
**`badge-limited`** — Violet-background badge for limited edition and artist collaboration products. Uses Lato Bold uppercase 11px with 2px vertical and 8px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, stacked footer, hero banner reduces to 48px vertical padding, search bar collapses to icon-only |
| Tablet | 744–1128px | Two-column product grid, full navigation with condensed links, footer splits into two rows, hero banner maintains 64px padding |
| Desktop | 1128–1440px | Three-column product grid, full navigation, four-column footer, hero banner at full width with optional background image |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero banner extends full viewport width with content centered at 1440px |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Navigation links have 44px minimum tap area with 8px padding
- Product card CTAs are 44px tall with 16px horizontal padding
- Search bar maintains 48px height for comfortable tapping
- Pagination buttons are 32px wide with 8px padding, meeting touch targets through generous spacing

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid reduces from 3 columns to 2 at tablet, 1 at mobile
- Footer columns stack from 4 to 2 at tablet, 1 at mobile
- Hero banner text reduces from display-xl to display-lg on mobile
- Search bar collapses to icon-only trigger on mobile, expanding to full-width overlay on tap
- Breadcrumb trail truncates to show only current and parent page on mobile
- Accordion sections remain collapsed by default on all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted from the live site; primary-active and secondary-active states are inferred from the brand color
- Error, success, info, and warning colors are extracted from the site but their specific usage contexts (form validation, alerts, notifications) could not be confirmed
- The heritage italic font (Lato-BlaIta) was found in font declarations but its exact usage weight and sizing are estimated
- Dark mode or high-contrast mode styles are not present in the extracted data
- Sub-brand or collection-specific color variations (e.g., artist collaborations) could not be reliably extracted
- Animation durations, easing curves, and transition properties are not available
- Modal, tooltip, and dropdown component styles are absent from the extracted data
- The extracted color list includes many generic web colors (grays, blues) that may be framework defaults; the true brand palette is inferred from the most distinctive colors (#680202, #5f5e97, #d39e00) and the dominant greys (#f4f4f4, #eeeeee, #b3b2b2)
- Font sizes and line heights are estimated based on common Lato implementations and may not exactly match the live site
- Spacing values are inferred from common e-commerce patterns and may differ from the actual implementation
