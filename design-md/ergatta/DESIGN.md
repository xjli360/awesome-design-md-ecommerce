---
version: alpha
name: "Ergatta"
source_url: "https://ergatta.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep teal (#205b65) anchors Ergatta — not as a sporty accent but as the room itself, the water, the space you enter. This is a rowing-machine brand that borrows more from premium wellness studios and game-ui design than from gym equipment catalogs. The palette runs from that primary teal through a warm marigold (#fbcd0a) used sparingly for score highlights and achievement badges, a coral-orange (#fe663f) for secondary energy, and a soft lavender (#a89cc8) that surfaces in illustration and motion backgrounds. The canvas is a near-white (#f9fafb) with subtle warmth, not clinical hospital white. Type uses Nunito Sans for body and display — a rounded, open humanist sans that avoids the mechanical feel of typical fitness branding — and Pressura Light for select headline moments, a compressed sans that adds a sharp, editorial contrast. Buttons and cards use generous {rounded.sm} and {rounded.md} radii, but the signature move is the full-pill button ({rounded.full}) for primary actions like "Start Workout" or "Join Race", giving the interface a game-console, ready-to-play feel. The nav bar is a floating translucent panel over the hero, not a solid strip, and the hero itself is often a full-bleed video of water or rowing motion, overlaid with a scrim (#142435 at 50% opacity). Badges are compact pills with uppercase micro-labels, and the footer is a dense, dark teal (#142435) block with generous {spacing.section} padding. The overall mood is immersive, calm, and focused — a digital dojo rather than a leaderboard.

colors:
  primary: "#205b65"
  primary-active: "#1a4a52"
  primary-disabled: "#a3c8cc"
  ink: "#142435"
  body: "#3f4a56"
  muted: "#7b7b7b"
  muted-soft: "#9aa6b4"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#fbcd0a"
  accent-coral: "#fe663f"
  accent-lavender: "#a89cc8"
  accent-teal-light: "#c1e6e6"
  accent-teal-soft: "#edf5f5"
  scrim: "#142435"
  footer-bg: "#142435"
  footer-text: "#9aa6b4"
  error: "#df340d"
  star-rating: "#fbcd0a"

typography:
  display-xl:
    fontFamily: "'Pressura Light', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0

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
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 16px 32px
    height: 56px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  button-accent-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-pill-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
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
  nav-bar:
    backgroundColor: "rgba(249, 250, 251, 0.9)"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    backdropFilter: "blur(8px)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-overlay:
    backgroundColor: "rgba(20, 36, 53, 0.5)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-lavender:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  rating-stars:
    color: "{colors.star-rating}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Uses the deep teal `#205b65` fill with white text and a full pill shape (`{rounded.full}`), giving it a game-console or premium-appliance feel. On hover, it shifts to `{colors.primary-active}` (`#1a4a52`). Disabled state uses `{colors.primary-disabled}` (`#a3c8cc`). Height is 56px for the large variant, with 16px/32px padding.

**`button-secondary`** — An outlined variant with a white fill, `{colors.primary}` text, and a 2px solid border. Used for "Learn More" or secondary actions alongside primary buttons. Active state darkens the border and text to `{colors.primary-active}`.

**`button-accent-gold`** — A high-energy variant using the marigold `#fbcd0a`. Used for achievement-related actions, score highlights, or "Join Race" CTAs. Text is the dark ink `#142435` for contrast.

**`button-accent-coral`** — A warm coral `#fe663f` variant for limited-time offers, urgency, or secondary game-like actions. White text.

**`button-pill-sm`** — A compact 36px pill for inline actions, filter tags, or "Shop Now" badges. Uses the primary teal.

### Cards
**`product-card`** — The standard card for rower product listings. White background, `{rounded.md}` (12px), with a softly rounded image area (`{rounded.sm}`). Title uses `{typography.title-md}` in `{colors.ink}`, body copy in `{typography.body-sm}` in `{colors.body}`. Padding is `{spacing.base}` (16px) on all sides.

### Navigation
**`nav-bar`** — A floating, translucent bar at 72px height with a `rgba(249, 250, 251, 0.9)` background and `backdropFilter: blur(8px)`. Links use `{typography.nav-link}` (15px, weight 600). Active link has a 2px bottom border in `{colors.primary}`. The bar sits over the hero section, not as a solid strip.

### Forms
**`text-input`** — Standard input fields for sign-up, login, and checkout. White background, `{rounded.sm}` (8px), 48px height, with a 1px `{colors.hairline}` border. On focus, the border thickens to 2px and turns `{colors.primary}`.

### Badges
**`badge-primary`** — Compact pills (4px/12px padding) with uppercase 11px bold type. Used for "NEW", "BEST SELLER", or feature tags. Available in primary teal, gold, coral, and lavender variants to match the accent palette.

### Footer
**`footer-section`** — A dense, dark block using `{colors.footer-bg}` (`#142435`) with `{colors.footer-text}` (`#9aa6b4`) for links and body copy. Links hover to white. Padding is `{spacing.section}` (64px) top and bottom, `{spacing.lg}` (24px) sides.

### Hero
**`hero-section`** — Full-bleed video or image background with a dark scrim overlay (`rgba(20, 36, 53, 0.5)`). Text is white, with the headline using `{typography.display-xl}` (Pressura Light, 48px) and subtext in `{typography.body-lg}`. CTA buttons sit centered or left-aligned.

### Dividers
**`divider`** — A 1px line in `{colors.hairline}` (`#dedede`) for section breaks. **`divider-soft`** uses `{colors.hairline-soft}` (`#e9e9e9`) for lighter separation within cards or lists.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero text scales down to `{typography.display-md}` (28px); buttons become full-width; product cards stack vertically; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero maintains two-column split (text left, media right); buttons remain inline but may shrink to `{typography.button-md}` |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses full `{typography.display-xl}`; standard padding and spacing |
| Wide | > 1440px | Max-width container at 1440px; hero may use wider aspect ratio media; additional whitespace on sides; product grid can expand to four columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon-only buttons (e.g., cart, search, menu) are at least 44x44px with `{rounded.full}`.
- Nav bar hamburger icon is 48x48px on mobile.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu. The full link set appears in a slide-out panel from the left or right.
- The product card grid collapses from 3-4 columns to 1 column.
- The hero section reduces padding and stacks text above media.
- Footer link columns collapse to a single vertical list.
- Search bar may collapse to an icon that expands on tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover/active states** for most components (e.g., badge hover, footer link hover color, card hover shadow) were not reliably extracted from the live site CSS. The active states provided for buttons are inferred from common darkening patterns.
- **Error and validation styling** for forms (error text color, border color on error, success states) was not observed. The `error` color (`#df340d`) is extracted but its usage context is unconfirmed.
- **Dark mode** is not present on the live site; no dark-mode tokens are defined.
- **Sub-brand or campaign-specific palettes** (e.g., seasonal promotions, limited-edition rower colors) may exist but were not captured.
- **Animation and motion tokens** (e.g., transition durations, easing curves, scroll-triggered animations) were not extracted.
- **Font weights for Pressura Light** are assumed to be 300 based on the name "Light", but the exact weight declaration in CSS was not confirmed.
- **The extracted font list includes JudgemeIcons and JudgemeStar** — these are third-party review widget fonts, not brand fonts. They have been excluded from the typography block.
- **The extracted color list is large (30+ hex values)** and includes many near-whites and grays that may be Shopify checkout defaults or stock-image tones. The brand's true palette is inferred from the most distinctive colors: `#205b65` (teal), `#fbcd0a` (gold), `#fe663f` (coral), `#a89cc8` (lavender), and `#142435` (dark ink). The remaining grays and whites are treated as utility/background tokens.
