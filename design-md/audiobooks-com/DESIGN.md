---
version: alpha
name: "Audiobooks.com"
source_url: "https://www.audiobooks.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A single dark anchor — `#313131` — holds the entire listening experience, a deep charcoal that appears in the site's navigation bar, footer, and primary text, giving the interface the weight and permanence of a well-bound book. The brand operates on a stark white canvas (`#ffffff`) with this near-black ink as its sole structural color, creating a high-contrast reading environment that disappears behind the content. There are no brand colors beyond this monochrome axis — no accent hue for CTAs, no secondary palette for categories — which means every button, link, and interactive element must earn its visibility through typographic weight and spacing rather than color. The font stack is the system default cascade (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif`), a pragmatic choice that prioritizes legibility across devices over brand distinctiveness. Rounded corners are minimal (`{rounded.sm}` ~8px on buttons, `{rounded.md}` ~12px on cards), never reaching the pill shapes of consumer lifestyle brands. The result is a utilitarian, library-like interface where the audiobook covers and metadata do all the emotional work — the chrome is deliberately invisible.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#d32f2f"
  success: "#2e7d32"
  link: "#1565c0"
  link-visited: "#6a1b9a"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0

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
    height: 48px
  button-primary-hover:
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
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-tertiary-text-hover:
    textColor: "{colors.primary-active}"
    textDecoration: underline
  button-cta-large:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  text-input-helper:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  top-nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  top-nav-link-hover:
    textDecoration: underline
  top-nav-logo:
    height: 32px
  top-nav-search-icon:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 40px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  footer-link-hover:
    textColor: "{colors.muted-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
    marginTop: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  search-bar-icon:
    textColor: "{colors.muted}"
    marginRight: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-subtitle:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
    height: 56px
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
    border: "1px solid {colors.hairline-soft}"
  category-chip-hover:
    backgroundColor: "{colors.hairline-soft}"
    border: "1px solid {colors.hairline}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    textDecoration: underline
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    margin: "0 {spacing.xs}"
  loading-spinner:
    border: "3px solid {colors.hairline-soft}"
    borderTop: "3px solid {colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
  error-message:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.error}"
  success-message:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.success}"
  tooltip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  modal-overlay:
    backgroundColor: "rgba(0, 0, 0, 0.5)"
  modal-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    maxWidth: 600px
  modal-close-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px

## Components

### Buttons
**`button-primary`** — The primary action button, filled with `{colors.primary}` (#313131) and white text. Uses `{typography.button-md}` (16px/600 weight) with `{rounded.sm}` (8px) corners. On hover, the background deepens to `{colors.primary-active}` (#1a1a1a). The disabled state uses `{colors.primary-disabled}` (#a0a0a0) with no hover change. Padding is 12px vertical, 24px horizontal, producing a 48px-tall button that works equally well in hero sections and modal footers.

**`button-secondary`** — An outlined variant with a white background, `{colors.primary}` text, and a 2px solid border matching the text color. Hover shifts both border and text to `{colors.primary-active}` and adds a `{colors.surface-soft}` background. This button sits alongside primary CTAs when there are two equal-priority actions (e.g., "Try Free" vs. "Learn More").

**`button-tertiary-text`** — A text-only button with no background or border, using `{typography.button-md}` in `{colors.primary}`. On hover, the text darkens to `{colors.primary-active}` and gains an underline. Used for "Cancel," "Skip," or "View All" links that need less visual weight than a full button.

**`button-cta-large`** — The hero-level call to action, 56px tall with 16px/32px padding and `{typography.button-lg}` (18px/600 weight). Same `{colors.primary}` fill and `{rounded.sm}` corners as the standard primary, but scaled up for prominence on landing pages and promotional banners.

### Forms
**`text-input`** — A standard text input with a white background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. Focus state thickens the border to 2px `{colors.primary}`. Error state swaps to a 1px `{colors.error}` (#d32f2f) border. The input is 48px tall with 12px/16px padding and `{rounded.sm}` corners. Labels use `{typography.caption}` (13px) in `{colors.muted}`, placed 4px above the input. Helper text sits below in `{typography.caption-sm}` (12px).

**`select-input`** — Matches the text-input dimensions and border styling, with a dropdown arrow icon in `{colors.muted}`. The same focus and error states apply.

**`checkbox`** — A 20px × 20px square with `{rounded.xs}` (4px) corners and a 2px `{colors.hairline}` border. The checked state fills the box with `{colors.primary}` and displays a white checkmark icon.

### Navigation
**`top-nav`** — A 64px-tall bar with `{colors.primary}` background and white text. The logo sits left-aligned at 32px height. Navigation links use `{typography.nav-link}` (15px/500 weight) with 8px/16px padding and underline on hover. A search icon button sits on the right side, 40px tall with no background. The nav is fixed at the top of every page.

**`breadcrumb-link`** — Links in the breadcrumb trail use `{typography.caption}` (13px) in `{colors.muted}` with underline. The current page label uses `{colors.ink}` with no underline. Separators are `{colors.muted-soft}` with 4px horizontal margin.

### Cards
**`product-card`** — An audiobook listing card with a white background, 1px `{colors.hairline-soft}` border, and `{rounded.md}` (12px) corners. Padding is 16px all around. On hover, the border strengthens to `{colors.hairline}` and a subtle shadow appears (0 2px 8px rgba(0,0,0,0.08)). The cover image occupies a 1:1 aspect ratio with `{rounded.sm}` (8px) corners. Below it: the title in `{typography.title-sm}` (16px/600), the author in `{typography.body-sm}` (14px/400, `{colors.muted}`), a star rating in `{typography.caption}`, and the price in `{typography.title-sm}` using `{colors.primary}`.

**`product-card-badge`** — Small labels (e.g., "Bestseller," "Exclusive") using `{typography.badge}` (11px/600, uppercase, 0.5px letter-spacing) on a `{colors.surface-soft}` background with `{rounded.xs}` (4px) corners and 2px/8px padding. A "New" variant uses `{colors.success}` (#2e7d32) background with white text.

### Search
**`search-bar`** — A pill-shaped (`{rounded.full}`) search input, 48px tall with 12px/20px padding, white background, and a 1px `{colors.hairline}` border. A search icon sits inside at the left in `{colors.muted}`. Focus state thickens the border to 2px `{colors.primary}`. Used in the hero section and on search results pages.

**`category-chip`** — Filter chips for browsing genres, 36px tall with `{rounded.full}` shape, `{colors.surface-soft}` background, and a 1px `{colors.hairline-soft}` border. Text uses `{typography.button-sm}` (14px/600) in `{colors.ink}`. Hover darkens the background to `{colors.hairline-soft}`. The active state fills with `{colors.primary}` and white text.

### Feedback & Overlays
**`loading-spinner`** — A 24px circle with a 3px `{colors.hairline-soft}` border and a 3px `{colors.primary}` top border, animated with CSS rotation. `{rounded.full}` ensures a perfect circle.

**`error-message`** — A banner with `{colors.surface-soft}` background, `{colors.error}` (#d32f2f) text, 1px `{colors.error}` border, `{rounded.sm}` corners, and 12px/16px padding. Uses `{typography.body-sm}`.

**`success-message`** — Same structure as error-message but with `{colors.success}` (#2e7d32) for text and border.

**`tooltip`** — A small label with `{colors.primary}` background, white text, `{typography.caption}`, `{rounded.xs}` (4px) corners, and 4px/8px padding.

**`modal-overlay`** — A semi-transparent black overlay (rgba(0,0,0,0.5)) covering the full viewport. The modal card sits centered with a white background, `{rounded.md}` (12px) corners, 24px padding, and a max-width of 600px. A close button in the top-right corner uses a 32px circle with `{colors.surface-soft}` background and `{colors.muted}` icon.

### Pagination
**`pagination-button`** — Numbered page buttons, 36px tall with 8px/12px padding, white background, 1px `{colors.hairline}` border, and `{rounded.sm}` (8px) corners. The active page uses `{colors.primary}` fill with white text. Disabled buttons use `{colors.surface-soft}` background and `{colors.muted-soft}` text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; top-nav collapses to hamburger menu; product cards stack vertically; hero section reduces padding to 32px; search bar moves below hero title; category chips scroll horizontally with overflow-x |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (logo, search, account); hero uses 48px padding; category chips wrap to 2 rows |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; hero uses 64px padding; category chips display in full rows |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero section centers content with 80px padding; category chips expand to show all genres |

### Touch Targets
- All interactive elements (buttons, links, inputs, chips) maintain a minimum 44px × 44px touch target area
- Top-nav hamburger menu icon is 48px × 48px
- Category chips are 36px tall with 16px horizontal padding, exceeding the 44px width minimum
- Pagination buttons are 36px × 36px — below ideal touch target; consider 44px minimum on mobile
- Checkbox hit area extends to 44px × 44px via invisible padding

### Collapsing Strategy
- Top-nav navigation links collapse into a hamburger menu below 744px
- Category chip rows collapse from 4+ rows to a single horizontally scrollable strip below 744px
- Product grid collapses from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Footer link columns collapse from 4 columns to a single stacked list below 744px
- Hero section collapses from side-by-side (text + image) to stacked (text above image) below 744px
- Search bar in the top-nav collapses into an expandable icon on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (`#313131`) was extracted from the live site; the full color palette (especially hover states, error/success colors, link colors) has been inferred from common web patterns and may not match the brand's actual choices
- No brand-specific font family was found — the site uses the system font stack; a custom typeface may exist but was not detected in the extracted CSS
- Meta theme-color was absent, suggesting no PWA-style browser chrome customization
- The site returned a "Just a moment..." page title, indicating Cloudflare or similar protection; the extracted data may represent a fallback page rather than the full production experience
- No extracted data for: dark mode, focus ring styles, animation durations/easing, shadow tokens, gradient usage, icon set (likely Font Awesome or similar), or sub-brand palettes
- Button hover, focus, and active states for all variants are inferred from common patterns, not extracted from live CSS
- Form validation styling (error icons, success checkmarks) is assumed based on industry conventions
- No data on mobile navigation patterns (hamburger menu animation, drawer behavior) — the collapsing strategy is based on common e-commerce patterns
- Pricing and badge colors (success green, error red) are standard web defaults and may not match the brand's actual semantic palette
- The extracted font stack includes Apple Color Emoji and Noto Color Emoji, suggesting emoji support is intentional but no brand-specific icon system was detected
