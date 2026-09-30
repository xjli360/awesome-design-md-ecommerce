---
version: alpha
name: "Field Company"
source_url: "https://fieldcompany.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Field Company brings a quiet, rugged warmth to cookware, built on a palette of deep navy-blues and steely grays that evoke a well-seasoned skillet and the workshop where it was forged. The brand’s canvas is a soft off-white (`#f8f7f7`) that feels tactile rather than sterile, with ink tones (`#0b1e2f`) and body text (`#3a3a3a`) that read as sturdy and grounded. Signature accents like `#f9c23c` (a warm, buttery gold) and `#0e7a82` (a teal inspired by patina) appear sparingly — on badges, hover states, and secondary CTAs — adding just enough brightness against the dominant `#557b97` (the meta theme-color and primary blue) and `#434e4e` (a muted olive-gray used for secondary text). Typography leans heavily on GT America for clean, utilitarian body copy and Beaufort for display headings that carry a slight serif warmth, echoing the brand’s blend of heritage craftsmanship and modern precision. Rounded corners are restrained (`{rounded.sm}` on buttons, `{rounded.md}` on cards), never pill-shaped, keeping the interface honest and tool-like. The overall mood is confident, unpretentious, and deeply material — like a cast-iron pan that only gets better with use.

colors:
  primary: "#557b97"
  primary-active: "#136f99"
  primary-disabled: "#d3d4dd"
  ink: "#0b1e2f"
  body: "#3a3a3a"
  muted: "#434e4e"
  muted-soft: "#676986"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#f8f7f7"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#f9c23c"
  accent-teal: "#0e7a82"
  badge-new: "#f9c23c"
  badge-sale: "#0e7a82"
  star-rating: "#f9c23c"
  scrim: "#070707"

typography:
  display-xl:
    fontFamily: "'Beaufort', 'GTSuperDisplay-Light', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Beaufort', 'GTSuperDisplay-Light', Georgia, serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'GT America', 'MetricWeb-Regular', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'GT America', 'MetricWeb-Regular', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'GT America', 'MetricWeb-Regular', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT America', 'MetricWeb-Regular', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  caption:
    fontFamily: "'GT America', 'MetricWeb-Regular', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'GT America', 'MetricWeb-Regular', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'GT America', 'MetricWeb-Regular', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'GT America', 'MetricWeb-Regular', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'GT America', 'MetricWeb-Regular', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'GT America', 'MetricWeb-Regular', Helvetica, Arial, sans-serif"
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  hero-cta:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart" and "Shop Now" across the site. It uses the brand’s signature blue (`{colors.primary}`) with white text and a subtle `{rounded.sm}` corner. On hover, it deepens to `{colors.primary-active}`; when disabled, it fades to `{colors.primary-disabled}` with muted text. The uppercase label (`{typography.button-md}`) reinforces the brand’s no-nonsense, tool-like feel.

**`button-secondary`** — An outlined or ghost-style button for secondary actions like "Learn More" or "View Details." On a light canvas, it uses a clean white background with ink text; on hover, it inverts to a solid ink fill. The same uppercase typography and `{rounded.sm}` corners maintain consistency with the primary button.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Skip." It inherits the same uppercase typography and hover state as the secondary button, but remains transparent to reduce visual weight.

### Cards
**`product-card`** — The core product display component, featuring a white surface (`{colors.surface-card}`) with `{rounded.md}` corners and a soft shadow. The card contains an image with matching rounded corners, a title in `{typography.title-sm}`, a price in `{typography.body-md}`, and an optional badge. Hover states may include a subtle elevation or border highlight.

**`product-card-badge`** — A small, gold (`{colors.accent-gold}`) label pinned to the top-left of product cards, used for "New" or "Best Seller" tags. It uses `{typography.badge}` with tight padding and `{rounded.xs}` corners.

### Navigation
**`nav-bar`** — A fixed top navigation bar with a white background and 72px height. Links use `{typography.nav-link}` in uppercase, with the active state highlighted in `{colors.primary}`. The bar may include a logo, search icon, and cart icon, all aligned to the brand’s clean, utilitarian grid.

**`nav-link-active`** — The active navigation link state, distinguished by the brand’s primary blue (`{colors.primary}`) to indicate the current page or section.

### Forms
**`text-input`** — A standard text input field with a white background, `{rounded.sm}` corners, and `{typography.body-md}` text. On focus, it gains a `{colors.primary}` border. Used for search, email signup, and checkout forms.

**`search-bar`** — A dedicated search input with a similar style to `text-input`, but may include a search icon and a slightly larger height. It appears in the nav bar and on the hero section for product discovery.

### Hero
**`hero-section`** — The full-width hero banner at the top of the homepage, using a soft gray background (`{colors.surface-soft}`) and large display typography (`{typography.display-xl}`). It features a headline, a subheadline in `{typography.body-md}`, and a primary CTA (`{hero-cta}`) in gold (`{colors.accent-gold}`) to draw attention.

**`hero-cta`** — The hero’s primary button, using the brand’s accent gold (`{colors.accent-gold}`) with ink text. It shares the same `{rounded.sm}` corners and uppercase typography as other buttons, but stands out against the hero’s muted background.

### Footer
**`footer-section`** — A dark footer with an ink background (`{colors.ink}`) and white text. It contains links in `{colors.muted-soft}` (`{typography.link}`), a newsletter signup form, and social icons. The footer uses `{spacing.section}` padding for generous breathing room.

**`footer-link`** — Links within the footer, styled in `{typography.link}` with a muted-soft color (`{colors.muted-soft}`) to reduce contrast against the dark background. On hover, they may lighten to `{colors.canvas}`.

### Badges
**`badge-new`** — A gold badge (`{colors.badge-new}`) with ink text, used to flag new products or features. It uses `{typography.badge}` with `{rounded.xs}` corners and tight padding.

**`badge-sale`** — A teal badge (`{colors.badge-sale}`) with white text, used for sale or limited-time offers. It shares the same typography and corner radius as `badge-new`.

### Ratings
**`star-rating`** — A star rating component using the brand’s gold (`{colors.star-rating}`) for filled stars and a muted gray for empty ones. The font size is 16px, and it appears on product cards and reviews.

### Accordion
**`accordion`** — A collapsible accordion component used for product details, FAQs, and shipping information. It has a white background, `{rounded.sm}` corners, and uses `{typography.title-sm}` for the header. The expanded state may include a border or background change.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav bar collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-md}`; buttons become full-width. |
| Tablet | 744–1128px | Two-column grid for product cards; nav bar shows limited links; hero retains two-column layout with reduced padding. |
| Desktop | 1128–1440px | Full three-column grid for products; nav bar shows all links; hero uses `{typography.display-xl}` with generous padding. |
| Wide | > 1440px | Max-width container (1440px) centered; extra whitespace on sides; hero may include larger imagery. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile.
- Nav bar hamburger icon is at least 48x48px.
- Product card CTAs are at least 44px tall.

### Collapsing Strategy
- Nav bar collapses to a hamburger menu on mobile (< 744px).
- Product grid collapses from 3 columns to 2 (tablet) to 1 (mobile).
- Hero section collapses from two-column (text + image) to stacked single-column on mobile.
- Footer links collapse from multi-column to single-column on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components (e.g., button-secondary hover, text-input focus border) are inferred from brand colors; exact transitions and shadows are not extracted.
- Error and validation styling for forms (e.g., red borders, error messages) is not available from the live site.
- Dark mode palette is not defined; the brand currently uses a light-only theme.
- Sub-brand or seasonal color palettes (e.g., holiday collections) are not captured.
- Specific font weights for GT America and Beaufort beyond what is listed are not confirmed; weights are estimated based on common usage.
- Animation durations and easing curves (e.g., button hover transitions) are not extracted.
- Iconography and illustration styles are not defined; only color and typography tokens are provided.
- Spacing values for specific components (e.g., product-card padding) are inferred from the brand’s general spacing scale and may not match exact production values.
- The `oke-widget-icons` font family is used for review widgets (Okendo) but is not part of the core brand typography; it is excluded from the design system.
