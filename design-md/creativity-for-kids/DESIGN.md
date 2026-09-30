---
version: alpha
name: "Creativity for Kids"
source_url: "https://www.fabercastell.com/pages/creativity-for-kids"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep forest-green (#05301a) anchors the brand as a grounding, earthy presence — not the bright primary of a toy aisle, but the color of a pine needle floor in a shaded woods. That green runs through the primary buttons, the footer background, and the header logo area, while a warm off-white canvas (#f6f6f0) — like unbleached paper or natural linen — replaces pure white everywhere, softening the reading experience. The palette leans heavily on a muted, almost monochromatic gray system (#707170, #787878, #aaaaaa, #d5d5d5, #eeeeee) that creates a quiet, uncluttered stage for product photography and craft materials. A single accent of marigold yellow (#eedd22) appears sparingly — perhaps on sale badges or age-range indicators — and a restrained red (#c60808) marks errors or limited-time callouts. Typography defaults to system sans-serif (Arial, Georgia for serif moments), suggesting the brand prioritizes readability and low visual friction over typographic personality. Cards and buttons use soft rounding (`{rounded.sm}` for buttons, `{rounded.md}` for cards), and the generous spacing (`{spacing.lg}` between elements, `{spacing.section}` between major blocks) gives the page the unhurried rhythm of a craft table where materials are laid out one at a time. The overall impression is not of a children's brand shouting for attention, but of a thoughtful, nature-connected space that trusts the creativity of the child — and the calm of the parent — to fill the silence.

colors:
  primary: "#05301a"
  primary-active: "#042614"
  primary-disabled: "#8a9e8f"
  ink: "#111111"
  body: "#444444"
  muted: "#707170"
  muted-soft: "#a4a4a4"
  hairline: "#d5d5d5"
  hairline-soft: "#eeeeee"
  canvas: "#f6f6f0"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#eedd22"
  accent-red: "#c60808"
  accent-red-soft: "#fdd0d0"
  accent-sage: "#a79d79"
  accent-gold: "#c7bd98"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 12px 28px
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
    padding: 12px 28px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 0
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  badge-age:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the deep forest green (#05301a) with white text. Uses a soft 8px radius and bold Arial at 16px with 0.5px letter spacing for a confident, readable label. On hover, the background darkens to `{colors.primary-active}` (#042614). In its disabled state, the button shifts to a muted sage green (`{colors.primary-disabled}`) to signal non-interactivity without visual noise.

**`button-secondary`** — An outlined variant with a transparent fill, green text, and a 2px solid green border. Maintains the same dimensions and typography as the primary button. On hover, it fills with the primary green, inverting the color relationship — a clean, satisfying micro-interaction that rewards exploration.

**`button-tertiary`** — A text-only link styled as a button, used for "Shop All" or "Learn More" links within product cards and category sections. No background, no border, just the green text at 13px bold with tight padding. The absence of a container keeps the page feeling open and unhurried.

**`button-accent-yellow`** — A warm marigold variant (#eedd22) with dark ink text, used sparingly for high-visibility actions like "Add to Cart" on promotional items or age-filtered collections. The yellow provides a cheerful counterpoint to the predominantly green-and-gray palette without competing with the brand's earthy core.

### Cards & Product Display
**`product-card`** — A white card with 12px rounded corners and 16px padding, sitting on the off-white canvas background. The card contains a square-ratio product image with its own 8px rounding, a title in `{typography.title-md}`, a price in `{typography.body-md}`, and an optional age badge. On hover, a subtle drop shadow lifts the card from the page — the only motion effect, keeping interactions gentle.

**`badge-age`** — A pill-shaped yellow badge indicating the recommended age range (e.g., "Ages 5+"). Uses uppercase 11px bold type with 0.5px letter spacing, positioned at the top-left corner of the product image. The yellow stands out against the product photo without overwhelming it.

**`badge-new`** — A green pill badge for new arrivals, matching the primary brand color. Same typography and shape as the age badge, but signals freshness rather than suitability.

**`badge-sale`** — A red pill badge (#c60808) for discounted items. The red is the only saturated non-green, non-yellow accent in the system, so its appearance is immediately legible as a price event.

### Navigation
**`nav-bar`** — A 72px-tall fixed header on the off-white canvas, containing the brand logo on the left and navigation links in 15px semibold Arial with 0.2px letter spacing. On scroll, a subtle box shadow appears beneath the bar to separate it from page content. The navigation links use `{colors.ink}` for active/current pages and `{colors.muted}` for inactive ones.

**`search-bar`** — A full-rounded pill input on the canvas background with a 1px hairline border. The pill shape echoes the badge treatment, creating a consistent organic geometry across the interface. Placeholder text uses `{colors.muted-soft}`.

**`category-chip`** — A pill-shaped filter chip in the soft gray surface color (`{colors.surface-soft}`) with muted text. Active chips fill with the primary green and white text, providing clear visual feedback for the currently selected category filter.

### Forms & Inputs
**`text-input`** — Standard form fields with 8px rounding, 48px height, and 16px horizontal padding. The border is a single hairline stroke in `{colors.hairline}`. On focus, the border thickens to 2px and turns primary green. Error states switch to a 2px red border (#c60808) with the error message appearing below in `{colors.accent-red}`.

### Footer
**`footer`** — A full-width deep green (#05301a) footer with white text. Links are set in `{typography.link}` (14px regular Arial) and remain white on hover. The footer uses generous vertical padding (`{spacing.section}`) to create a grounded, weighty bottom edge to the page — like the heavy base of a pottery piece.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero text reduces to `{typography.display-md}`; category chips scroll horizontally; buttons go full-width |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero uses `{typography.display-xl}` at 32px; category chips wrap to 2 rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full display-xl size; category chips in a single row |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid on category pages; hero may include a full-bleed background image |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height and 44px width for touch accessibility
- Category chips are at least 36px tall with 16px horizontal padding
- Search bar is 44px tall with comfortable 20px horizontal padding
- Nav links have 48px touch targets (padding extends clickable area)

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer
- Product filters collapse into a single "Filter" button that opens a modal overlay
- The hero section reduces image height by 40% and stacks text below the image
- Footer columns stack vertically with accordion-style expandable sections
- Category chip rows become horizontally scrollable with a fade-to-white edge indicator

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is heavily weighted toward grays and neutrals (20+ of the 30 extracted colors are in the gray/silver range), suggesting the live site uses a very restrained palette with only a few brand accents. The true brand primary (#05301a) and the marigold yellow (#eedd22) were identified as the most distinctive colors in the list, but their exact usage ratios (how much green vs. how much yellow) could not be determined from frequency alone.
- No custom font family was detected — the site uses system fonts (Arial, Georgia). This may be intentional (low-friction, fast-loading) or a gap in extraction. If the brand has a custom typeface, it was not present in the extracted CSS.
- Hover states for text inputs, category chips, and footer links are inferred from common patterns, not extracted from the live site.
- Error states (validation messages, empty states, 404 pages) are not represented in the extracted data.
- Dark mode is not supported and no dark-mode tokens were found.
- The accent red (#c60808) and its soft variant (#fdd0d0) appear in the extraction but their exact role (error vs. sale vs. limited-time) is inferred from context.
- The brand's sub-brand or collection-specific palettes (e.g., seasonal craft kits, licensed characters) are not captured.
- Animation timing, easing curves, and transition durations are not available from the extraction.
