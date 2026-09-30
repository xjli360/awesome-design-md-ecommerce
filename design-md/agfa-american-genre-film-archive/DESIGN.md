---
version: alpha
name: "AGFA (American Genre Film Archive)"
source_url: "https://www.americangenrefilm.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A neon-drenched archive of cult, exploitation, and underground cinema, AGFA’s identity is a deliberate collision of VHS-era grit and institutional clarity. The brand’s primary voltage comes from a deep, authoritative blue (#003388) — not a friendly sky blue, but the kind of saturated, serious blue you’d expect on a revival-house marquee or a collector’s edition Blu-ray spine. This blue anchors the entire system, appearing on primary buttons, navigation bars, and key interactive elements. Against a near-black canvas (#121212), the site reads as a dark, immersive theater lobby — the kind where the only light comes from the screen and the neon EXIT sign. Accents of cyan (#02e49b) and orange (#ff9900) puncture the darkness like arcade cabinet glow or faded poster ink, used sparingly for badges, price tags, and hover states. Typography runs Lato and futura-pt — clean, geometric, slightly condensed — set at modest weights (400–600) that never compete with the movie posters and stills that do the real storytelling. Buttons are hard-cornered ({rounded.none}) and compact, echoing the no-frills utility of a ticket booth or a VHS clamshell case. Cards and modals use a soft 8px radius ({rounded.sm}) for a hint of approachability, but the overall mood remains stark, archival, and unapologetically analog. The site’s grid is generous but disciplined — whitespace is used to isolate each film poster as an artifact, not a thumbnail. The result is a digital space that feels less like a streaming platform and more like walking into a repertory cinema that’s been running 35mm prints since 1976.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#6688bb"
  ink: "#121212"
  body: "#32373c"
  muted: "#949494"
  muted-soft: "#eeeeee"
  hairline: "#444444"
  hairline-soft: "#f0f0f0"
  canvas: "#121212"
  surface-soft: "#1e1f26"
  surface-card: "#24292d"
  on-primary: "#ffffff"
  accent-cyan: "#02e49b"
  accent-orange: "#ff9900"
  accent-pink: "#e94c89"
  accent-red: "#ea4434"
  badge-new: "#02e49b"
  badge-sale: "#ff9900"
  star-rating: "#ff9900"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'futura-pt', 'Lato', 'Arial', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'futura-pt', 'Lato', 'Arial', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'futura-pt', 'Lato', 'Arial', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'futura-pt', 'Lato', 'Arial', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'futura-pt', 'Lato', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Lato', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'futura-pt', 'Lato', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'futura-pt', 'Lato', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Lato', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'futura-pt', 'Lato', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase

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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.on-primary}"
  button-secondary-active:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  icon-button:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
    border: "1px solid {colors.primary}"
  product-card-title:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-meta:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-format:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: "400px"
  hero-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: "0.6"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  modal:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  modal-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: "0.8"
  divider:
    backgroundColor: "{colors.hairline}"
    height: "1px"
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: "1px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand’s deep blue (#003388) with white uppercase text. Hard corners ({rounded.none}) and compact 44px height give it a no-nonsense, ticket-booth feel. On hover, the background shifts to `{colors.primary-active}` (#002266). The disabled state uses a muted blue (`{colors.primary-disabled}`) to signal inactivity without breaking the system’s color logic.

**`button-secondary`** — An outlined variant for secondary actions. Uses a transparent background with a 2px white border, maintaining the same 44px height and uppercase `{typography.button-md}`. On hover, the button inverts to a solid white background with dark text (`{colors.ink}`), creating a crisp, high-contrast state.

**`button-accent-cyan`** and **`button-accent-orange`** — Accent buttons for promotional or high-energy actions (e.g., “Add to Cart” on a sale item, “Watch Trailer”). Use the brand’s cyan (#02e49b) and orange (#ff9900) respectively, with dark text (`{colors.ink}`) for readability. These buttons are intentionally rare — they function like a neon sign in a dark theater lobby.

**`icon-button`** — A square 44px button for icon-only actions (search, menu, close). Transparent background by default, with a `{colors.surface-soft}` hover state. No border or radius — the icon itself is the affordance.

### Navigation
**`top-nav`** — A fixed 64px dark bar (`{colors.ink}`) with a subtle bottom border (`{colors.hairline}`). Navigation links use `{typography.nav-link}` (futura-pt, 14px, uppercase, 500 weight). Active links are indicated by a 2px `{colors.primary}` bottom border. Inactive links are muted (`{colors.muted}`). The nav feels archival and serious — no dropdowns, no mega-menus, just a clean row of destinations.

**`nav-link-active`** and **`nav-link-inactive`** — Active links inherit the full white text and a primary-colored underline. Inactive links are gray (`{colors.muted}`) with no underline. Hover on inactive links transitions to white text.

### Cards
**`product-card`** — The core content container for film listings. A dark card (`{colors.surface-card}`) with a 1px hairline border (`{colors.hairline}`) and 8px radius (`{rounded.sm}`). On hover, the border switches to `{colors.primary}`, creating a subtle selection glow. The card contains a poster image (full-bleed top), then the `product-card-title` and `product-card-meta` components stacked below.

**`product-card-title`** — The film title, set in `{typography.title-sm}` (Lato, 16px, 600 weight, white). Padding is 16px on sides, 16px top, 8px bottom.

**`product-card-meta`** — Metadata like year, director, runtime, format. Set in `{typography.caption}` (Lato, 13px, 400 weight, `{colors.muted}`). Padding is 8px sides, 8px bottom.

### Forms & Inputs
**`search-bar`** — A dark input field (`{colors.surface-soft}`) with a 1px hairline border and 8px radius. Text is white, placeholder is `{colors.muted}`. On focus, the border switches to `{colors.primary}` and the background lightens to `{colors.surface-card}`. Height is 44px to match button alignment.

**`text-input`** — Standard form input, sharing the same styling as the search bar. Used for email signups, checkout fields, and filter controls. Focus state mirrors the search bar.

### Badges
**`badge-new`** — A cyan (#02e49b) badge with dark text, used to flag new arrivals or recent additions. Hard corners, 11px uppercase futura-pt.

**`badge-sale`** — An orange (#ff9900) badge for sale items or limited-time offers. Same typography and structure as `badge-new`.

**`badge-format`** — A neutral badge for format labels (Blu-ray, DVD, Digital). Uses `{colors.surface-soft}` background, `{colors.muted}` text, and a 1px hairline border. These badges sit quietly in the card meta, providing information without competing with the poster.

### Hero & Overlays
**`hero-section`** — A full-width hero area for featured films or collections. Minimum height of 400px, dark background (`{colors.ink}`), white text using `{typography.display-xl}`. Content is padded with `{spacing.section}` top/bottom and `{spacing.xl}` sides.

**`hero-overlay`** — A semi-transparent black overlay (`{colors.scrim}` at 60% opacity) used to ensure text readability against variable poster images.

### Footer
**`footer`** — A dark footer matching the nav bar, with a top border (`{colors.hairline}`). Text is muted (`{colors.muted}`) at `{typography.body-sm}`. Links are `{typography.link}` and transition to white on hover.

**`footer-link`** and **`footer-link-hover`** — Standard footer links in muted gray, switching to white on hover. No underline — the color change is the only affordance.

### Modal
**`modal`** — A centered dialog for quick-view, video trailers, or confirmation prompts. Uses `{colors.surface-card}` background, 8px radius, and a 1px hairline border. Padding is `{spacing.xl}` (32px) on all sides.

**`modal-overlay`** — A full-screen black scrim at 80% opacity, darker than the hero overlay to create a stronger focus lock.

### Dividers
**`divider`** — A 1px solid line in `{colors.hairline}` (#444444). Used between sections or card elements.

**`divider-soft`** — A lighter 1px line in `{colors.hairline-soft}` (#f0f0f0), used sparingly for subtle separation within cards or forms.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for product cards. Top nav collapses to hamburger menu. Hero section reduces to 300px min-height. Search bar moves below nav. Footer stacks vertically. |
| Tablet | 744–1128px | Two-column product grid. Top nav remains visible but collapses secondary links into a "More" dropdown. Hero text reduces to `{typography.display-lg}`. |
| Desktop | 1128–1440px | Three-column product grid. Full top nav visible. Hero at full 400px height. Sidebar filters appear on collection pages. |
| Wide | > 1440px | Four-column product grid. Max-width container at 1440px. Hero text uses `{typography.display-xl}` at full 36px. |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines.
- Icon buttons are 44x44px squares.
- Product cards are tappable as a single unit — the entire card is a link.
- Badges are not interactive and do not require touch targets.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu. The menu overlay uses `{colors.surface-card}` with full-height links.
- The search bar collapses from a full-width input to an icon button that expands on tap.
- Product card metadata (year, director, runtime) collapses to a single line on mobile, with full details revealed on tap.
- The footer’s multi-column link layout collapses to a single vertical stack on mobile.
- Hero content (title, subtitle, CTA) stacks vertically on mobile, with the CTA button moving below the text.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color list is heavily weighted toward generic web blues and grays — the true brand palette likely includes more distinctive accents (the cyan #02e49b and orange #ff9900 appear to be intentional, but their exact usage rules are inferred from context).
- Font-family declarations were mixed: Lato and futura-pt appear alongside Arial, Baskerville, and adobe-garamond-pro. The primary brand fonts are assumed to be Lato and futura-pt based on usage patterns, but this is not confirmed.
- No extracted hover states, focus rings, or active states for interactive elements beyond what’s inferred from color relationships.
- Error styling (form validation, 404 pages, empty states) is not present in the extracted data.
- Dark mode is not relevant — the site already uses a dark canvas (#121212) as its default.
- Sub-brand or collection-specific color variations (e.g., “Drive-In Double Feature” vs. “VHS Archive”) are not documented.
- Animation and transition timing values (ease-in-out, duration) are not extracted.
- The meta theme-color (#121212) matches the canvas, confirming the dark theme is intentional.
- No extracted data for loading states, skeleton screens, or progress indicators.
