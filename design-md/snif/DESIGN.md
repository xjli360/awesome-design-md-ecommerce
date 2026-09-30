---
version: alpha
name: "Snif"
source_url: "https://snif.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Snif is a warm, tactile, and slightly irreverent fragrance brand that feels like a cozy evening in a candle-lit room with a friend who has impeccable taste. The brand’s palette is built on a foundation of deep, earthy browns and creamy, blush-adjacent neutrals, anchored by a primary of rich mahogany (`#523228`) and a canvas of soft, barely-there blush (`#f5e8e2`). This isn’t a stark, minimalist white-label scent; it’s a sensory experience that leans into comfort and intimacy. The primary action color, a vibrant, almost urgent red (`#e32c2b`), provides a jolt of energy against the otherwise muted, grounded tones, used sparingly for critical CTAs and sale badges. Typography is a playful mix of the chunky, hand-drawn feel of `ExtraChunkPlease Regular` for headlines and the refined, serifed elegance of `GrandSlang Roman` for body copy, creating a deliberate tension between the casual and the luxurious. The system relies heavily on pill-shaped inputs and buttons (`{rounded.full}`), soft card corners (`{rounded.md}`), and generous whitespace (`{spacing.section}`) to create a feeling of approachability and calm. The overall mood is one of curated, accessible indulgence—a brand that doesn’t take itself too seriously but is deeply serious about the quality of its scents.

colors:
  primary: "#523228"
  primary-active: "#6c4739"
  primary-disabled: "#a49087"
  ink: "#252121"
  body: "#212121"
  muted: "#6c4739"
  muted-soft: "#a3928a"
  hairline: "#d6c8c0"
  hairline-soft: "#e9d8d0"
  canvas: "#f5e8e2"
  surface-soft: "#fef2ec"
  surface-card: "#f7eee6"
  on-primary: "#f5e8e2"
  accent-red: "#e32c2b"
  accent-blue: "#1990c6"
  accent-blue-active: "#136f99"
  scrim: "#121212"
  badge-new: "#e32c2b"
  badge-sale: "#e32c2b"

typography:
  display-xl:
    fontFamily: "'ExtraChunkPlease Regular', 'Impact', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'ExtraChunkPlease Regular', 'Impact', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ExtraChunkPlease Regular', 'Impact', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-xl:
    fontFamily: "'GrandSlang Roman', 'Georgia', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'GrandSlang Roman', 'Georgia', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Sharp Grotesk Book 21', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Sharp Grotesk Book 21', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  body-md:
    fontFamily: "'GrandSlang Roman', 'Georgia', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GrandSlang Roman', 'Georgia', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Sharp Grotesk Book 19', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Sharp Grotesk Medium 23', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Sharp Grotesk Book 23', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Sharp Grotesk Book 21', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textDecoration: underline
  nav-link:
    fontFamily: "'Sharp Grotesk Book 21', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Sharp Grotesk Semi Bold 23', 'Arial', sans-serif"
    fontSize: 10px
    fontWeight: 600
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
    rounded: "{rounded.full}"
    padding: 14px 28px
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
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-red-active:
    backgroundColor: "#c41e1d"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 14px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} 0 0 0"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-subtle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
    height: 56px
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "14px 24px"
    height: 56px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.on-primary}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"
  toggle-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  toggle-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for adding items to cart, submitting forms, and primary navigation prompts. It uses the brand's signature mahogany (`{colors.primary}`) on a blush canvas (`{colors.on-primary}`) with a fully pill-shaped (`{rounded.full}`) silhouette. On hover or active state, it shifts to a slightly lighter brown (`{colors.primary-active}`). The disabled state fades to a muted taupe (`{colors.primary-disabled}`), signaling non-interactivity.

**`button-secondary`** — A secondary action button with a transparent background and a subtle hairline border (`{colors.hairline}`). It is used for "Learn More" links, secondary checkout options, or cancel actions. On active state, the border thickens and darkens to the ink color (`{colors.ink}`) for clear focus.

**`button-accent-red`** — A high-energy, urgent CTA reserved for sale items, limited drops, and clearance events. It uses the brand's vibrant red (`{colors.accent-red}`) to create a strong visual contrast against the otherwise earthy palette. The active state darkens to a deeper crimson.

**`button-ghost`** — A minimal, borderless button used for text-based actions within cards or modals. It inherits the ink color and relies on the `button-md` typography for clarity.

### Navigation
**`nav-bar`** — The primary site navigation, a fixed-height bar with a clean white canvas background (`{colors.canvas}`) and a soft bottom hairline (`{colors.hairline-soft}`). It houses the brand logo, navigation links using `{typography.nav-link}`, and utility icons (search, account, cart). The active link state uses the primary brown (`{colors.primary}`) to indicate the current page.

**`nav-link-active`** — The active state for a navigation link, distinguished by a color change to the primary brown. No background or underline is used, keeping the nav bar clean and uncluttered.

### Cards
**`product-card`** — The standard product display card, used on collection pages and search results. It features a soft, warm off-white background (`{colors.surface-card}`) and moderately rounded corners (`{rounded.md}`). The card contains a product image with matching rounded corners, a title using `{typography.title-sm}`, and a muted price. It is designed to feel tactile and inviting, like a physical product tag.

### Badges
**`badge-new`** — A small, prominent badge used to denote newly launched products. It uses the accent red (`{colors.badge-new}`) on a white background to draw immediate attention. The fully rounded shape and uppercase `{typography.badge}` text give it a tag-like appearance.

**`badge-sale`** — Identical in style to `badge-new`, but used specifically for sale or discounted items. The red color signals a deal or limited-time offer.

**`badge-subtle`** — A softer badge used for non-urgent labels like "Best Seller" or "Subscription." It uses a soft surface background (`{colors.surface-soft}`) and muted text (`{colors.muted}`) to provide information without competing with primary CTAs.

### Forms & Inputs
**`text-input`** — A standard text input field for email signups, search queries, and form fields. It has a fully pill-shaped (`{rounded.full}`) design, a clean white background, and a subtle hairline border. On focus, the border changes to the primary brown (`{colors.primary}`) for clear visual feedback.

**`search-bar-pill`** — The primary search input, larger than a standard text input to accommodate a prominent search icon and placeholder text. It maintains the pill shape and is often used in the hero section or a dedicated search page.

### Footer
**`footer-section`** — The site footer, which uses an inverted color scheme: a deep primary brown background (`{colors.primary}`) with light text (`{colors.on-primary}`). This creates a strong visual closure for the page. Links within the footer use the `footer-link` style, which is an underlined version of the `link` typography in the light color.

### Toggles & Filters
**`toggle-pill`** — A filter or option toggle used on collection pages (e.g., "Scent Type: Fresh | Warm | Woody"). Inactive pills have a soft background and muted text. The active state (`toggle-pill-active`) fills with the primary brown and white text, clearly indicating the selected filter.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Product cards stack vertically. Nav bar collapses to a hamburger menu. Hero section reduces `display-xl` to `display-lg`. Search bar moves below hero. Footer links stack. |
| Tablet | 744–1128px | Two-column product grid. Nav bar remains horizontal but with reduced link padding. Hero section uses `display-lg`. Sidebar filters become a horizontal toggle strip. |
| Desktop | 1128–1440px | Three-column product grid. Full nav bar with all links visible. Hero section uses `display-xl`. Sidebar filters are persistent. |
| Wide | > 1440px | Max-width container (1440px) centered. Product grid can expand to four columns. Increased whitespace around hero and section content. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 48px to meet accessibility standards.
- Icon buttons and toggle pills have a minimum touch area of 44x44px.
- Nav bar links have a minimum touch area of 48x48px.

### Collapsing Strategy
- On mobile, the primary navigation collapses into a full-screen overlay menu triggered by a hamburger icon.
- The product filter sidebar collapses into a horizontal, scrollable strip of toggle pills.
- The footer's multi-column layout collapses into a single column with accordion-style sections for link groups.
- The hero section's side-by-side layout (image + text) collapses into a stacked layout with the image above the text.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and focus states for all components (e.g., `text-input-hover`, `product-card-hover`) were not reliably extracted from the live site and are inferred from standard patterns.
- Error styling for form inputs (e.g., error border color, error message typography) is not available.
- Dark mode color tokens are not defined, as the brand appears to use a light theme exclusively.
- Sub-brand or seasonal palette variations (e.g., holiday collections) are not captured.
- The specific `fontWeight` values for the `ExtraChunkPlease Regular` and `GrandSlang Roman` fonts are assumed to be 400 (Regular) as the extracted data did not include weight variants.
- The `letterSpacing` values for display fonts are estimated based on common brand usage and may differ from the actual site.
- The `textTransform: uppercase` on the `caption` typography is inferred from the brand's use of small, all-caps labels.
- The exact `border` width and color for `button-secondary` active state is an assumption based on standard design patterns.
- The `height` for `search-bar-pill` is an estimate based on its visual prominence compared to standard inputs.
