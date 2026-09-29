---
version: alpha
name: "Olive Films"
source_url: "https://olivefilms.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A single hex value — #aba000, a muted olive-gold — carries the entire brand voltage of Olive Films, appearing on every primary CTA, navigation highlight, and hover state across a site that otherwise trusts a near-white canvas and generous negative space. The typography runs system-ui and sans-serif at modest weights (400–500 for body, 600 for headings), never competing with the film stills and poster art that do the real storytelling. Product cards use {rounded.sm} corners and a soft {colors.hairline} border, letting the cover art breathe inside a clean container. The top nav is a simple horizontal strip with dropdown menus, the search bar a full-width input with a {colors.primary} focus ring, and the footer a dense grid of links and legal text in {colors.muted}. There is no hero animation, no parallax, no decorative illustration — the brand treats its catalog as the only ornament it needs, and the olive-gold accent is the single signature move that says "this is Olive Films" without saying it in words.

colors:
  primary: "#aba000"
  primary-active: "#8f8600"
  primary-disabled: "#d4cb80"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  star-rating: "#aba000"
  badge-new: "#aba000"
  badge-sale: "#cc3333"
  link: "#aba000"
  link-hover: "#8f8600"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px

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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    height: 36px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 36px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  top-nav-item:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    height: 64px
  top-nav-item-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  top-nav-item-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  top-nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} 0"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  top-nav-dropdown-item:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  top-nav-dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0 {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "2/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-subtitle:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    border: "1px solid {colors.primary}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  filter-chip-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  pagination-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    height: 36px
  pagination-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 36px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0 {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.badge-sale}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0 {spacing.base}"
    height: 44px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    height: 20px
    border: "1px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    height: 20px
  radio:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    border: "1px solid {colors.hairline}"
  radio-checked:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 20px
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.5
  modal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
  modal-close-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    height: 24px
  loading-spinner-large:
    color: "{colors.primary}"
    height: 48px
  skeleton:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
  skeleton-text:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
    height: 14px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, filled with {colors.primary} and white text. On hover, it shifts to {colors.primary-active} for a subtle darkening effect. When disabled, it uses {colors.primary-disabled} to signal inactivity without losing brand identity. The {rounded.sm} corners keep it crisp and modern.

**`button-secondary`** — A white button with a {colors.hairline} border and {colors.ink} text, used for secondary actions like "Cancel" or "View Details". On active state, the border thickens to {colors.ink} and the background shifts to {colors.surface-soft}. Maintains the same 44px height as the primary button for alignment in forms.

**`button-tertiary-text`** — A text-only button in {colors.primary} with no background or border, used for inline actions like "See all" or "Learn more". On hover, the text darkens to {colors.primary-active}. Minimal footprint for contexts where a full button would be too heavy.

**`button-pill-primary`** — A fully rounded variant of the primary button, used for filter chips, tag-like actions, or compact CTAs. Uses {typography.button-sm} and tighter padding (8px 20px) to fit in tighter spaces like category strips or mobile menus.

### Cards
**`product-card`** — The core content container for film listings. A white card with a {rounded.sm} corner and a soft {colors.hairline-soft} border. The image area occupies the top with a 2:3 aspect ratio (standard poster proportion). Title, subtitle (year/director), and price stack below with consistent padding. On hover, the border strengthens to {colors.hairline} and a subtle shadow lifts the card. No overlay or animation — the poster art does the work.

**`product-card-image`** — The top section of the product card, with rounded top corners and a 2:3 aspect ratio. Designed to display film posters or key art at their native proportions. No border-radius on the bottom edge so the image bleeds cleanly into the text area below.

### Navigation
**`top-nav`** — A fixed-height 64px bar with a white background and a soft bottom border. Navigation items sit at {typography.nav-link} with {colors.muted} text, switching to {colors.ink} on the active page with a 2px {colors.primary} underline. Hover state shifts text to {colors.primary}. Dropdown menus appear on hover with a white background, soft shadow, and {rounded.sm} corners.

**`top-nav-dropdown`** — A floating panel triggered by hover on nav items. White background, {rounded.sm} corners, and a subtle drop shadow. Items inside use {typography.body-sm} and 8px vertical padding. On hover, items get a {colors.surface-soft} background and {colors.primary} text.

### Forms
**`text-input`** — A standard 44px input with a {colors.hairline} border and {rounded.sm} corners. On focus, the border becomes a 2px {colors.primary} stroke. Error state uses {colors.badge-sale} (#cc3333) for the border. Placeholder text uses {colors.muted-soft}. Used for search, email signup, and checkout fields.

**`select-input`** — Matches the text-input dimensions and styling, used for dropdown selectors like genre filters or sort options. Same 44px height, {rounded.sm} corners, and {colors.hairline} border.

**`checkbox`** and **`radio`** — 20px interactive elements with {colors.hairline} borders. Checked state fills with {colors.primary}. Radio buttons use {rounded.full} for the circular shape, checkboxes use {rounded.xs}. Used in filter sidebars and preference forms.

**`toggle`** — A 24px tall pill-shaped toggle with {colors.hairline} background. Active state fills with {colors.primary}. Used for binary settings like "Notify me" or "Show in stock only".

### Badges
**`badge`** — A small uppercase label in {colors.primary} with white text, used for "New Release", "Exclusive", or "Staff Pick". Tight padding (2px 6px) and {rounded.xs} corners keep it unobtrusive. The sale variant uses {colors.badge-sale} for urgency. An outline variant exists for secondary labeling.

### Filters
**`filter-chip`** — A pill-shaped button for category or genre filtering. White background with a {colors.hairline} border and {rounded.full} corners. Active state fills with {colors.primary} and white text. Hover state darkens the border to {colors.ink}. Used in horizontal scroll strips above the product grid.

### Pagination
**`pagination-button`** — A 36px square button for page navigation. Default state is transparent with {colors.body} text. Active page uses {colors.primary} fill with white text. Hover state uses {colors.surface-soft} background. Used at the bottom of search results and category pages.

### Footer
**`footer`** — A full-width section with {colors.surface-soft} background and {colors.muted} text. Links use {typography.link} and turn {colors.primary} on hover. Headings use {typography.title-sm} in {colors.ink}. Padding of {spacing.section} top and bottom creates breathing room. The footer contains multiple columns of links, legal text, and social icons.

### Modals
**`modal-overlay`** — A semi-transparent black scrim at 50% opacity behind modal dialogs. The modal card itself is white with {rounded.md} corners, 24px padding, and a deeper shadow (8px 32px). A close button sits in the top-right corner with a circular hover state.

### Loading States
**`loading-spinner`** — A 24px spinning indicator in {colors.primary}. A larger 48px variant exists for full-page loading. **`skeleton`** placeholders use {colors.hairline-soft} with {rounded.xs} corners, matching the dimensions of the content they replace.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), top nav collapses to hamburger menu, search bar moves to a dedicated page, filter chips stack vertically, footer columns stack to single column, hero banner reduces padding to {spacing.lg} |
| Tablet | 744–1128px | Two-column product grid, top nav shows limited items with "More" dropdown, search bar remains visible but narrower, filter chips scroll horizontally, footer shows 2 columns |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all items visible, search bar at full width, filter chips in a horizontal strip, footer shows 4 columns |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, top nav and footer expand to full width with content constrained, hero banner can accommodate larger imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 36px minimum with 44px touch area via padding
- Filter chips are 36px tall with 44px touch area
- Pagination buttons are 36px squares
- Modal close buttons are 32px with 44px touch area

### Collapsing Strategy
- Top nav collapses to a hamburger menu below 744px, with a slide-out drawer for navigation items
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport shrinks
- Filter chips move from horizontal scroll to vertical stack below 744px
- Footer columns collapse from 4 → 2 → 1
- Hero banner reduces padding and font sizes below 744px
- Search bar becomes a full-screen overlay on mobile, triggered by an icon button

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one extracted hex color (#aba000) was available from the live site analysis. The remaining colors in this design system are inferred from common patterns in the movies/entertainment e-commerce space and may not match the actual site. The primary color is confirmed from extraction.
- No font-family declarations beyond "sans-serif" and "system-ui" were found. The typography block uses system-ui as the primary stack, which is a reasonable default but may not match the brand's actual typeface.
- Hover and active states for all components are inferred from standard interaction patterns, not extracted from the live site.
- Error states, validation styling, and form feedback patterns are not confirmed from the live site.
- Dark mode support is not confirmed — the current system assumes a light theme only.
- The brand's logo, icon set, and illustration style are not documented here as they require visual extraction.
- Animation durations, easing curves, and transition properties are not available from the extracted data.
- The checkout flow, payment forms, and cart interactions may have additional styling not captured here.
- Accessibility contrast ratios have not been verified against WCAG standards for the inferred color pairings.
