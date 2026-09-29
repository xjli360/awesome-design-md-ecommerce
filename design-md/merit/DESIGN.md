---
version: alpha
name: "Merit"
source_url: "https://www.meritbeauty.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A study in quiet confidence, Merit’s design system is the digital embodiment of “skin-first, makeup-second” — a warm, tactile minimalism that feels like a deep breath in a cluttered world. The palette is anchored by a creamy off-white canvas (`#f9f8f5`) that reads as unbleached linen rather than sterile white, paired with a soft putty (`#f2f0ec`) and a range of warm grays (`#c8c8c8`, `#959593`, `#a9a9a9`) that never tip into cold industrial gray. The brand’s signature voltage comes from a restrained burnt-orange accent (`#dc4a12`) used sparingly on primary CTAs and select highlights, while a deep slate (`#1e1e1e`) and near-black (`#121212`) provide grounding for body text. A surprising flash of cobalt (`#0057ff`) appears in select links and interactive elements, adding a subtle, unexpected energy. Typography is where Merit truly differentiates: the elegant, slightly condensed serif of Instrument Serif for display headings, paired with the utilitarian clarity of Akzidenz-Grotesk for body and UI. This mix of refined editorial serif and workhorse sans-serif creates a system that feels both aspirational and approachable. Rounded corners are generous but not cartoonish — `{rounded.md}` (12px) on cards and `{rounded.full}` on pill buttons — while `{rounded.sm}` (8px) on inputs keeps the interface feeling polished. Spacing is generous, with `{spacing.section}` (64px) creating breathing room between major content blocks, and `{spacing.lg}` (24px) providing comfortable internal padding. The overall effect is one of effortless sophistication: a brand that trusts its products, its photography, and its customer enough to get out of the way.

colors:
  primary: "#dc4a12"
  primary-active: "#c13515"
  primary-disabled: "#f2d0c0"
  ink: "#121212"
  body: "#1e1e1e"
  muted: "#62605e"
  muted-soft: "#959593"
  hairline: "#d3d3d3"
  hairline-soft: "#eae6dd"
  canvas: "#f9f8f5"
  surface-soft: "#f2f0ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#0057ff"
  accent-blue-active: "#4778d9"
  accent-teal: "#1990c6"
  accent-teal-active: "#136f99"
  badge-new: "#dc4a12"
  star-rating: "#121212"
  error: "#c13515"
  success: "#2d4051"

typography:
  display-xl:
    fontFamily: "'Instrument Serif', 'adobe-caslon-pro', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Instrument Serif', 'adobe-caslon-pro', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Instrument Serif', 'adobe-caslon-pro', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Instrument Serif', 'adobe-caslon-pro', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'akzidenz-grotesk', 'akzidenz-grotesk-std', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'akzidenz-grotesk', 'akzidenz-grotesk-std', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'akzidenz-grotesk', 'akzidenz-grotesk-std', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'akzidenz-grotesk', 'akzidenz-grotesk-std', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.01em
  caption:
    fontFamily: "'akzidenz-grotesk', 'akzidenz-grotesk-std', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'akzidenz-grotesk', 'akzidenz-grotesk-std', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  button-sm:
    fontFamily: "'akzidenz-grotesk', 'akzidenz-grotesk-std', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  link:
    fontFamily: "'akzidenz-grotesk', 'akzidenz-grotesk-std', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.01em
    textDecoration: underline
  nav-link:
    fontFamily: "'akzidenz-grotesk', 'akzidenz-grotesk-std', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  badge:
    fontFamily: "'akzidenz-grotesk', 'akzidenz-grotesk-std', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.error}"
  text-input-placeholder:
    textColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.base}"
  hero-heading:
    typography: "{typography.display-xl}"
    maxWidth: 600px
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.ink}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  color-swatch-selected:
    border: "2px solid {colors.ink}"
  color-swatch-ring:
    border: "2px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a full-pill shape in the brand’s signature burnt orange (`{colors.primary}`). Uses uppercase Akzidenz-Grotesk at 14px with generous horizontal padding (32px) and a comfortable 48px height. On hover, it deepens to `{colors.primary-active}` (#c13515); when disabled, it fades to a soft peach (`{colors.primary-disabled}`). The pill radius (`{rounded.full}`) is a defining brand gesture — no hard corners anywhere on interactive elements.

**`button-secondary`** — A ghost button on the warm canvas background (`{colors.canvas}`) with a thin hairline border (`{colors.hairline}`). Shares the same pill shape and typography as primary, but inverts the color relationship. Active state darkens the border to `{colors.muted}` and adds a soft surface fill (`{colors.surface-soft}`). Used for “Add to Bag” alternatives, “Learn More,” and secondary checkout actions.

**`button-tertiary-text`** — A text-only button with no background or border, used for subtle actions like “View Details” or “Cancel.” Inherits the same uppercase button typography but sits at zero padding horizontally, allowing it to align with body text when needed.

**`button-pill`** — A compact, smaller pill button (36px height) used for filter tags, category toggles, and quick-add actions. Uses the smaller button typography (`{typography.button-sm}`) and the primary brand color by default, with a secondary variant using `{colors.surface-soft}` background.

### Cards
**`product-card`** — The primary product display unit, a softly rounded (`{rounded.md}`) white card on the warm canvas background. Contains a product image with its own `{rounded.sm}` corners, a title in `{typography.title-sm}`, and a muted price. The card has 16px padding and sits on the `{colors.canvas}` background, creating a subtle floating effect. No shadow by default — Merit trusts clean edges over drop shadows.

**`hero-section`** — A full-width section with a soft putty background (`{colors.surface-soft}`) that serves as the brand’s primary storytelling canvas. The heading uses the largest serif display (`{typography.display-xl}`) at 48px, constrained to a readable 600px max-width. Subheadings sit in body weight at 16px with muted color, creating a clear typographic hierarchy that lets product photography do the heavy lifting.

### Navigation
**`nav-bar`** — A fixed-height (72px) navigation bar on the warm white canvas, separated from content by a soft hairline (`{colors.hairline-soft}`). Navigation links use uppercase Akzidenz-Grotesk at 14px with 0.04em letter-spacing. Active links are indicated by a 2px bottom border in `{colors.ink}`; inactive links fade to `{colors.muted}`. The nav is intentionally sparse — typically 4-5 links (Shop, Best Sellers, About, Rewards, Search).

### Forms
**`text-input`** — Clean, minimal input fields with 8px rounded corners (`{rounded.sm}`) — the only place in the system where corners are less than full-pill. A 1px hairline border (`{colors.hairline}`) keeps the input subtle against the canvas. On focus, the border switches to solid `{colors.ink}`. Error states use `{colors.error}` (#c13515). Placeholder text is set in `{colors.muted-soft}` (#959593) for a gentle prompt.

### Badges
**`badge-new`** — A small, full-pill badge in the primary orange (`{colors.badge-new}`) used to flag new arrivals and limited editions. Uses 11px uppercase Akzidenz-Grotesk with 4px vertical and 10px horizontal padding. **`badge-sale`** uses the inverse approach — soft surface background with ink text — for promotional markers.

### Search
**`search-bar`** — A full-pill search input (48px height) with a 1px hairline border, designed to sit prominently in the nav or on collection pages. On focus, the border transitions to `{colors.ink}`. The pill shape aligns with the button system, reinforcing the brand’s rounded design language.

### Footer
**`footer-section`** — A full-width footer on the soft putty background (`{colors.surface-soft}`) with links in muted gray (`{colors.muted}`) that darken to `{colors.ink}` on hover. Uses 14px body weight type with generous vertical spacing (`{spacing.xxl}`) for a clean, editorial feel. Links are underlined by default, a small touch that aids scannability.

### Accordion
**`accordion`** — Used for product details (ingredients, how to use) and FAQ sections. Each accordion item is separated by a soft hairline border. The header uses `{typography.title-sm}` with 16px vertical padding; content area adds another 16px below. No icons or chevrons by default — Merit trusts clear typographic hierarchy over decorative indicators.

### Color Swatches
**`color-swatch`** — A 32px circular swatch used in product detail pages to show shade options. Selected state is indicated by a 2px solid ink border; unselected swatches have a thin hairline ring. The swatch itself is a full pill (`{rounded.full}`), continuing the system’s commitment to rounded forms.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero heading reduces to `{typography.display-lg}` (36px); buttons become full-width; search bar moves to drawer; footer links stack |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero maintains two-column layout with reduced padding; side-by-side product details |
| Desktop | 1128–1440px | Full three-column product grid; expanded nav with all links; hero at full width with 64px section padding; product cards show hover states |
| Wide | > 1440px | Max-width container (1440px) centered; hero content constrained to 1200px; product grid can expand to four columns; generous whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets are the full card area, not just text links
- Color swatches are 32px with 4px touch padding (effective 40px target)
- Accordion headers are full-width tap targets at minimum 48px height
- Mobile nav hamburger icon is 44x44px

### Collapsing Strategy
- Primary nav links collapse into a hamburger drawer below 744px
- Product filters collapse into a slide-out panel on mobile
- Footer link columns collapse into accordion-style sections below 744px
- Hero section reduces from two-column (text + image) to stacked single-column on mobile
- Product image galleries collapse from thumbnail strip to dot indicators on mobile
- Search bar collapses from inline to icon-triggered overlay on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (scale, shadow, or overlay treatment) could not be reliably extracted
- Error state styling for form validation (inline messages, iconography) is inferred from general brand patterns
- Dark mode palette is not defined — the brand currently operates in light mode only
- Sub-brand or limited-edition color palettes (e.g., holiday collections) are not captured
- Micro-interaction timing and easing curves (transitions, animations) are not specified
- Focus ring styles for keyboard navigation (color, width, offset) are not documented
- Loading states (skeleton screens, spinners) are not defined in the current system
- Dropdown and select menu styling (native vs. custom) is not captured
- Tooltip and popover component specifications are missing
- Video player controls and overlay styling are not documented
- Print stylesheet specifications are absent
