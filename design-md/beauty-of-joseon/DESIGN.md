---
version: alpha
name: "Beauty of Joseon"
source_url: "https://beautyofjoseon.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A heritage-rooted Korean skincare brand that marries Joseon dynasty wisdom with modern dermatological science, expressed through a palette as refined as a porcelain jar. The brand's visual language is anchored by a warm, earthy coral `#cf9370` — the meta theme-color that sets a tone of gentle luxury — and a vibrant primary red `#e15a5b` that appears in CTAs, badges, and accent details, evoking the red clay seals on traditional Korean paintings. The canvas is a soft off-white `#fcfbf9` that feels like aged hanji paper, while surfaces use a whisper of warmth `#f4f0e8` and `#f7f7f8` to avoid clinical sterility. Typography leans into contrast: a refined serif (Amiri) for display moments that whisper tradition, paired with a clean sans-serif (Figtree or Inter) for body text at `#212121` ink weight. The brand's signature "hanbang" (herbal medicine) story is told through muted sage `#9da1a0`, dusty rose `#cd9ba1`, and soft gold `#dab668` accents that appear in ingredient callouts and product badges. Rounded corners are generous but never cartoonish — cards use `{rounded.md}` (12px), buttons `{rounded.sm}` (8px), and the occasional pill shape `{rounded.full}` for search or filter elements. The overall mood is calm, scholarly, and tactile — like unboxing a hand-lettered apothecary jar wrapped in linen.

colors:
  primary: "#e15a5b"
  primary-active: "#c94a4b"
  primary-disabled: "#f0b0b1"
  ink: "#212121"
  body: "#484848"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  border-strong: "#d3d4dd"
  canvas: "#fcfbf9"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  surface-warm: "#f4f0e8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-gold: "#dab668"
  accent-rose: "#cd9ba1"
  accent-sage: "#9da1a0"
  accent-coral: "#cf9370"
  badge-new: "#e15a5b"
  badge-sale: "#ff5742"
  star-rating: "#dab668"
  ingredient-callout: "#94654b"
  scrim: "#141414"
  deep-navy: "#272d45"
  light-pink: "#f8e4e9"
  warm-beige: "#eace93"

typography:
  display-xl:
    fontFamily: "'Amiri', 'Georgia', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Amiri', 'Georgia', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Amiri', 'Georgia', serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Inter', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
    textTransform: uppercase
  ingredient-label:
    fontFamily: "'Amiri', 'Georgia', serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
    fontStyle: italic

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
    padding: 14px 28px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
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
    padding: 14px 0
  button-pill-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-active:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  top-nav-logo:
    maxHeight: 32px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  mobile-hamburger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: 8px
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline-soft}"
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    shadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-hover:
    shadow: "0 8px 24px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  ingredient-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ingredient-callout}"
    typography: "{typography.ingredient-label}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.accent-coral}"
  star-rating:
    textColor: "{colors.star-rating}"
    fontSize: 16px
  review-count:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    padding: "0 0 {spacing.base}"
    typography: "{typography.body-md}"
  footer:
    backgroundColor: "{colors.deep-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    textTransform: uppercase
    letterSpacing: 0.5px
  newsletter-input:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid rgba(255,255,255,0.2)"
    placeholderColor: "rgba(255,255,255,0.5)"
  newsletter-button:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  cart-item:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-item-image:
    rounded: "{rounded.sm}"
    width: 80px
    height: 80px
  cart-item-title:
    typography: "{typography.title-sm}"
  cart-item-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  cart-total:
    typography: "{typography.title-lg}"
    textColor: "{colors.ink}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  toast-success:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  toast-error:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, using the brand's signature red `{colors.primary}` on a clean white label. On hover, it deepens to `{colors.primary-active}` for tactile feedback. Disabled state fades to a soft pink `{colors.primary-disabled}`. All primary buttons use `{rounded.sm}` (8px) corners and 14px vertical padding for a substantial but not heavy feel.

**`button-secondary`** — An outlined alternative for less prominent actions, using a white background with `{colors.ink}` text and a `{colors.hairline}` border. Active state swaps the border to `{colors.ink}` and adds a subtle `{colors.surface-soft}` background. Ideal for "Add to Wishlist" or "Learn More" contexts.

**`button-tertiary-text`** — A text-only button in `{colors.primary}` for inline actions like "View All" or "See Details". No background or border — just the typography of `{typography.button-md}` with 14px vertical padding for clickable area.

**`button-pill-gold`** — A special accent button using the warm gold `{colors.accent-gold}` for premium moments like "Shop Bestsellers" or "Limited Edition" callouts. Uses `{rounded.full}` for a pill shape that feels luxurious and intentional.

**`button-pill-outline`** — A transparent pill with a `{colors.hairline}` border, used for filter toggles or secondary navigation pills. The outline keeps it light while maintaining clear boundaries.

### Cards
**`product-card`** — The core product display unit, a white card with `{rounded.md}` (12px) corners and a subtle shadow `0 2px 8px rgba(0,0,0,0.06)`. On hover, the shadow deepens to `0 8px 24px rgba(0,0,0,0.10)` for a gentle lift effect. The image area occupies the top with a 1:1 aspect ratio and rounded top corners only.

**`product-card-badge`** — An absolute-positioned badge in `{colors.primary}` for "New" or "Bestseller" labels. Uses `{typography.badge}` (11px uppercase) with `{rounded.xs}` (4px) corners. A sale variant uses `{colors.badge-sale}` (#ff5742) for urgency, and a gold variant uses `{colors.accent-gold}` for premium collections.

### Navigation
**`top-nav`** — A fixed-height 72px bar on `{colors.canvas}` with a subtle bottom border `{colors.hairline-soft}`. Navigation links use `{typography.nav-link}` (14px uppercase) for a refined, editorial feel. Active links gain a 2px `{colors.primary}` bottom border. The logo sits at a max height of 32px, maintaining brand presence without overwhelming.

**`mobile-hamburger`** — A minimal transparent button with `{colors.ink}` icon, using `{rounded.xs}` for the touch target. Padding ensures a comfortable 44px minimum tap area.

### Forms
**`text-input`** — Standard input fields with `{colors.canvas}` background, `{colors.hairline}` border, and `{rounded.sm}` corners. On focus, the border switches to `{colors.ink}` for clear active state. Error state uses `{colors.primary}` border to signal issues. Placeholder text is `{colors.muted-soft}` (#9a9db1) for legibility without distraction.

**`select-dropdown`** — Matches text-input styling for visual consistency, with a custom dropdown arrow in `{colors.muted}`.

**`newsletter-input`** — A footer-specific input on `{colors.deep-navy}` background, using a semi-transparent white border and placeholder. The companion `newsletter-button` uses `{colors.accent-gold}` to draw attention without competing with the primary red.

### Badges & Tags
**`ingredient-badge`** — A unique component for the brand's hanbang storytelling. Uses `{colors.surface-warm}` background, `{colors.ingredient-callout}` (#94654b) text, and a `{colors.accent-coral}` border. The typography is `{typography.ingredient-label}` — a 14px italic serif that evokes herbal apothecary labels. Rounded full for a soft, organic feel.

**`filter-chip`** — Pill-shaped toggle chips for product filtering. Default state is white with `{colors.hairline}` border. Active state inverts to `{colors.ink}` background with white text for clear selection feedback.

### Footer
**`footer`** — A deep navy `{colors.deep-navy}` (#272d45) footer that contrasts sharply with the warm, light palette above. All text is white with reduced opacity (0.8) for links, creating a calm, authoritative closing section. Headings are uppercase with generous letter-spacing for structure.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, hero collapses to 300px min-height, filter chips wrap to 2 columns, search bar becomes full-width |
| Tablet | 744–1128px | 2-column product grid, top nav shows limited links (4-5), footer splits into 2 rows, hero maintains 400px with centered text |
| Desktop | 1128–1440px | 3-4 column product grid, full top nav with all links, footer in single row, hero at full 500px with left-aligned text |
| Wide | > 1440px | Max-width container at 1440px, 4-column product grid, additional whitespace on hero sides, footer max-width constrained |

### Touch Targets
- All interactive elements maintain minimum 44px tap target (buttons, links, filter chips)
- Product cards have 48px minimum touch area for "Add to Cart" buttons
- Quantity selector buttons are 44px × 44px minimum
- Mobile hamburger icon has 48px × 48px tap area
- Filter chips are 44px minimum height with 16px horizontal padding

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with slide-out drawer for navigation links
- Product grid collapses from 4 columns to 2 columns at tablet, single column at mobile
- Footer sections stack vertically on mobile, with accordion-style expandable link groups
- Hero banner text centers and reduces font size on mobile (display-xl scales to 28px)
- Search bar collapses from inline to full-width overlay on mobile
- Product detail page switches from side-by-side to stacked layout below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card badges and ingredient badges not fully extracted — assumed subtle opacity or color shift
- Error styling for form validation (red border assumed from primary color, but error message typography and iconography not confirmed)
- Dark mode palette not present on site — no dark theme tokens available
- Sub-brand or collection-specific palettes (e.g., "Ginseng" vs "Green Plum" lines) may have unique accent colors not captured
- Animation tokens (transition durations, easing curves) not extracted — assumed 200-300ms ease-in-out for interactive states
- Focus ring styling (outline color, offset, width) not confirmed — recommended `{colors.primary}` with 2px offset
- Loading states (skeleton screens, spinner colors) not documented
- Modal/dialog overlay opacity and animation not extracted
- Dropdown menu shadow and z-index values not confirmed
- Print stylesheet not available
- Accessibility contrast ratios not verified against extracted colors (particularly `{colors.muted}` #676986 on `{colors.canvas}` #fcfbf9 may need checking)
- Custom checkbox and radio button styling not extracted
- Swatch/color picker component for product variants not documented
- Quantity selector increment/decrement icon specifics not confirmed
- Mobile bottom navigation bar (if any) not present on desktop extraction
- Cookie consent banner styling not available
- 404 page design not extracted
- Success/error toast iconography and animation not documented
- Star rating component half-star rendering not confirmed
- Accordion expand/collapse icon (chevron vs plus/minus) not extracted
- Image lazy loading and placeholder behavior not documented
- Font loading strategy (swap vs optional) not confirmed
- CSS custom property naming conventions not fully reverse-engineered
- Shopify-specific components (cart drawer, product form, variant selector) may have additional states not captured
- Internationalization (RTL support, multi-language typography adjustments) not available
- Print stylesheet for receipts or product details not extracted
- Keyboard navigation focus order not documented
- Reduced motion preferences not confirmed in existing stylesheets
