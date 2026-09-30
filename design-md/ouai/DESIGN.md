---
version: alpha
name: "OUAI"
source_url: "https://theouai.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  OUAI is a haircare and body-care brand that speaks in a warm, earthy whisper rather than a shout. The palette is anchored by a deep, almost espresso brown (`#322a26`) that reads as grounded and sophisticated — not the harsh black of luxury fashion nor the sterile gray of clinical beauty. This ink tone sits alongside a soft, blush-like beige (`#d6cbc4`) that functions as the brand's primary canvas for product photography and editorial layouts, creating a gentle contrast that feels both modern and approachable. The system's primary action color is a muted teal (`#1990c6`) with a darker active state (`#136f99`), a surprising choice that avoids the typical pink or coral of beauty brands and instead signals a clean, unisex, almost apothecary-like confidence. Supporting neutrals like `#444444` for body copy, `#dedede` and `#ebebeb` for hairline borders, and a near-white canvas (`#f3f3f4`) keep the interface airy and uncluttered. Rounded corners are generous but not cartoonish — `{rounded.sm}` (8px) on buttons and `{rounded.md}` (12px) on cards — while the full pill shape (`{rounded.full}`) is reserved for search bars and toggle elements, reinforcing a tactile, human-friendly feel. Typography leans on a clean sans-serif system (likely Inter or a similar geometric sans, though no explicit font-family was extracted), with display sizes at 24–28px in medium weight and body text at 14–16px. The overall mood is relaxed, warm, and slightly editorial — like a well-curated Instagram feed or a minimalist apartment in Los Angeles. OUAI's design doesn't compete with its products; it frames them in soft light and generous whitespace, letting the pastel pinks, mint greens, and lavender tones of the actual haircare bottles provide the color story.

colors:
  primary: "#1990c6"
  primary-active: "#136f99"
  primary-disabled: "#c6e4f3"
  ink: "#322a26"
  body: "#444444"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#f3f3f4"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-warm: "#d6cbc4"
  accent-warm-soft: "#e8e0db"
  badge-new: "#1990c6"
  badge-sale: "#c13515"
  star-rating: "#322a26"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-lg:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 12px 24px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.badge-sale}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-photo:
    rounded: "{rounded.md}"
    aspectRatio: 1/1
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-pill-active:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  hero-section:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    marginTop: "{spacing.lg}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-dark}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.md}"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.md} {spacing.md}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Bag," "Shop Now," and checkout flows. Rendered in the brand's signature teal (`{colors.primary}`) with white text, it uses a modest 8px corner radius (`{rounded.sm}`) and 44px height for a balanced, touch-friendly target. On hover, it shifts to `{colors.primary-active}`; when disabled, it fades to `{colors.primary-disabled}` with no border.

**`button-secondary`** — A clean, minimal alternative for secondary actions like "Learn More" or "View Details." Uses the light canvas (`{colors.canvas}`) background with ink-colored text. The outline variant adds a 1px solid `{colors.hairline}` border for visual structure without competing with the primary button.

**`button-pill-primary`** — A compact, fully rounded (`{rounded.full}`) variant reserved for filter tags, category pills, and "Quick Add" actions on product cards. Uses smaller typography (`{typography.button-sm}`) and a shorter 36px height to sit comfortably alongside other UI elements.

### Cards
**`product-card`** — The core product display unit, used in grid and carousel layouts. A white card (`{colors.surface-card}`) with 12px rounded corners (`{rounded.md}`) frames a 1:1 product photo above a two-line title and price. The photo area uses the same corner radius to create a cohesive, modern look. On hover, a subtle shadow or slight scale transform (not captured in tokens) can be applied.

**`product-card-title`** — Set in `{typography.title-sm}` (14px, semibold) with a small top margin (`{spacing.sm}`) from the photo. The price below uses `{typography.body-sm}` in `{colors.body}` for clear hierarchy.

### Navigation
**`nav-bar`** — A fixed or sticky top bar at 64px height, using the light canvas (`{colors.canvas}`) background. Navigation links are set in uppercase (`{typography.nav-link}`) with 0.5px letter-spacing for a refined, editorial feel. The active link is underlined with a 2px solid `{colors.ink}` border; inactive links use `{colors.muted}`.

**`search-bar-pill`** — A fully rounded search input (`{rounded.full}`) that sits in the nav bar or hero section. Uses a white card background and 48px height for easy tapping. On focus, a 2px `{colors.primary}` border appears to guide the user's attention.

### Forms
**`text-input`** — Standard form fields for email signups, address entry, and account forms. A white background with 8px rounded corners (`{rounded.sm}`) and 48px height. Focus state adds a 2px `{colors.primary}` border; error state switches to `{colors.badge-sale}` (#c13515) for clear validation feedback.

### Footer
**`footer`** — A dark, full-width footer using the deep ink (`{colors.ink}`) as background, with white text for maximum contrast. Links are set in `{typography.link}` (14px, medium weight) and spaced generously. The footer typically contains columns for "Shop," "Learn," "Support," and social links, plus a newsletter signup form.

### Badges
**`badge-new`** — A small, teal pill badge (`{colors.badge-new}`) used to flag new arrivals or limited-edition products. Set in 11px uppercase bold with 4px rounded corners (`{rounded.xs}`) and tight padding (2px 8px) so it sits neatly on product photos or cards.

**`badge-sale`** — Identical structure to `badge-new` but using a warm red (`{colors.badge-sale}`) for sale or clearance items, creating immediate visual distinction.

### Accordion
**`accordion`** — Used for FAQ sections and product details (ingredients, how to use). A collapsible panel with a `{colors.canvas}` background, `{typography.title-sm}` header, and `{typography.body-sm}` content area. The header includes a plus/minus or chevron icon (not captured in tokens) to indicate expand/collapse state.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger menu; hero section uses stacked layout with reduced padding; search bar moves to full-width below nav; footer columns stack vertically; accordion becomes default for product details |
| Tablet | 744–1128px | Two-column product grid; nav bar shows limited links with "More" dropdown; hero uses side-by-side layout; search bar remains in nav; footer shows 2–3 columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav bar with all links visible; hero uses full-width layout with generous padding; search bar in nav; footer shows 4 columns |
| Wide | > 1440px | Max-width container (1440px) centered; product grid can expand to 5 columns; hero uses larger typography and spacing; all layouts scale proportionally |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Product card tap targets (title, price, image) are at least 48px tall.
- Nav bar links and icons have a minimum 44px tap area.
- Search bar and form inputs are 48px tall for easy tapping on mobile.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger menu with a slide-out drawer.
- Product grids collapse from 4 columns to 2 (tablet) to 1 (mobile).
- Footer columns stack vertically on mobile, with accordion-style sections for each column.
- Hero sections switch from side-by-side (desktop) to stacked (mobile) layout.
- Search bar moves from inline in the nav to a full-width bar below the nav on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links beyond the primary color shift could not be reliably extracted (e.g., shadow, scale, or underline animations).
- Focus and active states for form inputs (beyond border color) are not fully documented (e.g., box-shadow, outline styles).
- Error messaging styling (text color, icon placement, background) for form validation is not captured.
- Dark mode palette and behavior are not defined; the brand currently uses a light-only scheme.
- Sub-brand or seasonal palette variations (e.g., holiday collections, limited-edition drops) are not included.
- Typography font-family is inferred as Inter based on common DTC beauty brand usage; the actual font-family declaration was not found in extracted data.
- Animation and transition durations (e.g., button hover, card hover, accordion expand) are not specified.
- Icon set and icon button styles (e.g., social media icons, cart icon, wishlist heart) are not documented.
- Dropdown menu and mega-menu patterns for the nav bar are not captured.
- Loading states, skeleton screens, and spinner designs are not included.
- Modal and overlay (e.g., quick-view, size selector) styling is not documented.
- Rating and review component (stars, count) is referenced in colors but not fully specified.
- Quantity selector and size picker UI patterns are missing.
- Newsletter signup form (inline in footer) styling is not captured beyond generic text-input tokens.
