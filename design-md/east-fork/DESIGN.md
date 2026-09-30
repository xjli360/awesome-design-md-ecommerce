---
version: alpha
name: "East Fork"
source_url: "https://eastfork.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  East Fork is a pottery and home goods brand rooted in Asheville, North Carolina, where the craft of wheel-thrown ceramics meets a deeply considered, earthy aesthetic. The brand’s visual language is anchored by a warm, off-white canvas of `#f4f3ee`, a color that feels like sun-dried clay, and is punctuated by the rich, terracotta-like `#ac624b` and the deep, grounding `#272d45` — a palette that mirrors the natural landscape of the Appalachian mountains. Signature design moves include generous use of soft, pill-shaped buttons (`{rounded.full}`) and cards with rounded corners (`{rounded.lg}`), creating a tactile, approachable feel that echoes the handmade quality of the products. The typography, while relying on system font stacks, is set in a clean, readable `body-md` at 16px, allowing the pottery’s texture and form to take center stage. Accents of `#ffcf2a` (a muted gold) and `#0e7a82` (a deep teal) appear sparingly, adding moments of unexpected warmth and depth without disrupting the overall calm. The brand feels unhurried and honest — every spacing unit, from `{spacing.sm}` (8px) to `{spacing.section}` (64px), is designed to breathe, creating a sense of quiet luxury that invites the user to slow down and appreciate the object in hand. This is not a brand that shouts; it’s one that speaks in the language of clay, light, and craft.

colors:
  primary: "#ac624b"
  primary-active: "#a1654f"
  primary-disabled: "#d4aaa9"
  ink: "#272d45"
  body: "#2c3e50"
  muted: "#676986"
  muted-soft: "#8396a0"
  hairline: "#d3d4dd"
  hairline-soft: "#e5e5eb"
  canvas: "#f4f3ee"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#ffcf2a"
  accent-teal: "#0e7a82"
  accent-sage: "#6c9183"
  accent-stone: "#c2bb99"
  accent-blush: "#f6eae3"
  accent-sky: "#1990c6"
  accent-ocean: "#136f99"
  badge-new: "#b2f9e9"
  badge-sale: "#e5e5e5"
  star-rating: "#ffcf2a"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "inherit, 'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "inherit, 'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "inherit, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "inherit, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "inherit, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "inherit, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "inherit, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "inherit, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "inherit, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "inherit, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px

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
    padding: 12px 28px
    height: 44px
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
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-pill-accent:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
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
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
    shadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-hover:
    shadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  section-heading:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} 0"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button with a warm terracotta fill (`{colors.primary}`). On hover, it deepens to `{colors.primary-active}` for tactile feedback, and when disabled, it fades to a soft blush (`{colors.primary-disabled}`). The text is set in `{typography.button-md}` with generous horizontal padding (28px) and a comfortable 44px height, making it feel substantial yet approachable.
**`button-secondary`** — A secondary action that sits on the canvas with a subtle hairline border (`{colors.hairline}`). On active state, the border darkens to `{colors.ink}` and the background shifts to `{colors.surface-soft}`, providing a clear visual hierarchy without competing with the primary button.
**`button-tertiary-text`** — A text-only button for low-emphasis actions, with no background or border. It inherits the ink color and uses the same `{typography.button-md}` sizing, relying on spacing and placement for differentiation.
**`button-pill-accent`** — An accent button using the muted gold (`{colors.accent-gold}`) for promotional or highlight actions. It maintains the pill shape and a slightly shorter 40px height, ideal for inline use.

### Cards
**`product-card`** — The core product display component, featuring a white surface (`{colors.surface-card}`) with a soft shadow and `{rounded.lg}` corners. On hover, the shadow deepens to create a subtle lift effect. Product badges (e.g., "New" or "Sale") are positioned as overlays using `product-card-badge`, which uses a pill shape and `{colors.badge-new}` or `{colors.badge-sale}` backgrounds.
**`hero-banner`** — A full-width hero section with a canvas background and large serif display text (`{typography.display-xl}`). It uses `{spacing.section}` for vertical padding and a minimum height of 400px, often featuring a single product or lifestyle image as the visual anchor.

### Navigation
**`nav-bar`** — A fixed top navigation bar with a canvas background and a soft bottom border. It uses `{typography.nav-link}` for links, with active states underlined by a 2px `{colors.primary}` border. On scroll, it collapses to a shorter 64px sticky variant (`nav-bar-sticky`).
**`nav-link-active`** — The active navigation link, distinguished by a bottom border in the primary terracotta color, signaling the current page or section.
**`nav-link-inactive`** — Inactive navigation links are rendered in `{colors.muted}` to reduce visual noise, with hover states returning to `{colors.ink}`.

### Forms
**`text-input`** — A standard text input with a canvas background, hairline border, and `{rounded.sm}` corners. On focus, the border thickens to 2px and switches to `{colors.primary}` for clear visual feedback. Error states use the same 2px primary border, as the brand avoids harsh reds for error styling.
**`search-bar`** — A pill-shaped search input with a hairline border, designed to feel integrated and unobtrusive. On focus, it adopts a 2px primary border, mirroring the text-input pattern.

### Footer
**`footer`** — A dark footer section with a deep navy background (`{colors.ink}`) and light text (`{colors.surface-soft}`). Links use `{colors.muted-soft}` and brighten to `{colors.canvas}` on hover, creating a clear contrast against the dark backdrop. The footer uses `{spacing.xxl}` for vertical padding, providing a grounded, substantial closing to the page.

### Badges
**`badge`** — A small, pill-shaped badge used for labels like "New" or "Eco-Friendly". It uses the accent teal (`{colors.accent-teal}`) for a fresh, natural feel. A `badge-sale` variant uses a neutral light gray (`{colors.badge-sale}`) for promotional tags.
**`icon-button`** — A circular icon button with no background and muted text. On hover, it gains a soft background (`{colors.surface-soft}`) and darkens to `{colors.ink}`, providing a subtle interactive cue.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; product cards stack vertically; nav-bar collapses to hamburger menu; hero-banner reduces padding to `{spacing.xl}`; buttons become full-width; search-bar moves to a collapsible drawer. |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links with a "More" dropdown; hero-banner uses `{spacing.xxl}` padding; side-by-side form layouts begin. |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar visible; hero-banner at full `{spacing.section}` padding; multi-column footer layout. |
| Wide | > 1440px | Max-width container (1440px) centered; increased whitespace around content; product grid can expand to four columns with larger card sizes. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum touch target of 44x44px.
- Icon buttons are 40x40px with 44x44px clickable area via padding.
- Product card images are tappable with a minimum 120px height on mobile.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile, with a slide-in drawer for links.
- Search bar collapses to an icon on mobile, expanding to a full-width input on tap.
- Product filters collapse to a "Filter" button on mobile, opening a modal overlay.
- Footer link columns collapse to accordion-style sections on mobile.
- Hero banners reduce text size and padding on mobile, often removing secondary copy.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components are inferred from common patterns; exact transition durations and easing curves are not extracted.
- Error styling for forms (e.g., error messages, validation icons) is not present in the extracted data; primary color is used as a fallback for error borders.
- Sub-brand or collection-specific palettes (e.g., limited-edition glazes) are not captured.
- Dark mode is not supported; all tokens assume a light theme.
- Typography details (font weights, exact line heights) are based on common system font behavior; custom font files (e.g., "oke-widget-icons") are not resolved.
- Shadow values for cards and modals are estimated; exact box-shadow CSS is not extracted.
- Animation and motion specifications (e.g., page transitions, micro-interactions) are absent.
- Accessibility contrast ratios for text on various backgrounds have not been verified.
