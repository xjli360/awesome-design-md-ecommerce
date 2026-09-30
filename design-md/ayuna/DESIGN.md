---
version: alpha
name: "Ayuna"
source_url: "https://ayuna.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Ayuna is a conscious skincare brand that speaks in quiet, deliberate tones — a palette anchored on a soft off-white canvas (#f0f0f0) and a muted ink (#1e1f26) that reads more like charcoal than pure black. The brand's signature voltage comes from a warm amber accent (#eac078) that appears sparingly, like sunlight catching the edge of a glass bottle, and a secondary teal (#1ea0c3) that adds a clinical, clean counterpoint. The most frequently occurring hex values — #555555, #949494, #cccccc, #dddddd — reveal a system that trusts tonal grays over high-contrast extremes; body text sits at #555555 rather than pure black, giving every page a breathable, editorial feel. Typography leans on system serifs and monospace faces (Consolas, Menlo, Monaco) for a lab-notebook authenticity, while sans-serif fallbacks keep the reading experience clean. Buttons and interactive elements use the amber (#eac078) as a primary CTA color, with a deeper variant (#ff9900) for active states, and all corners are softly rounded — `{rounded.sm}` (8px) for buttons, `{rounded.md}` (12px) for cards — avoiding the pill-shaped exuberance of consumer marketplaces. The brand's mood is one of considered minimalism: generous whitespace, a restrained accent palette that includes blush (#e94c89) and mint (#02e49b) for seasonal or limited-edition cues, and a typographic system that never shouts. This is a design system for a brand that wants you to read the ingredient list, not just the headline.

colors:
  primary: "#eac078"
  primary-active: "#ff9900"
  primary-disabled: "#dddddd"
  ink: "#1e1f26"
  body: "#555555"
  muted: "#949494"
  muted-soft: "#cccccc"
  hairline: "#dddddd"
  hairline-soft: "#f0f0f0"
  canvas: "#f0f0f0"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#1e1f26"
  accent-teal: "#1ea0c3"
  accent-teal-dark: "#0693e3"
  accent-blush: "#e94c89"
  accent-mint: "#02e49b"
  accent-blue: "#4280ff"
  accent-orange: "#f45800"
  badge-new: "#02e49b"
  badge-sale: "#e94c89"
  star-rating: "#eac078"
  scrim: "#1e1f26"

typography:
  display-xl:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "Consolas, Menlo, Monaco, monospace"
    fontSize: 10px
    fontWeight: 400
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
    padding: 11px 23px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
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
    borderWidth: 1px
  text-input-error:
    borderColor: "{colors.accent-orange}"
    borderWidth: 1px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} 0"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.md} 0"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  ingredient-list:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    lineHeight: 1.6

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in warm amber (#eac078) with dark ink text. Used for add-to-cart, subscribe, and primary form submissions. Hover transitions to a deeper gold (#ff9900) with a subtle 0.2s ease-in-out. Disabled state drops to a muted gray (#dddddd) with muted text (#949494). The monospace uppercase label at 14px with 1px letter-spacing gives the button a deliberate, almost scientific feel.

**`button-secondary`** — An outlined or ghost variant on the soft canvas background (#f0f0f0), with a 1px solid hairline border (#dddddd) and ink text. Used for secondary actions like "Learn More" or "View Ingredients." Hover state fills the background with a soft tint (#f0f0f0 to #eac078 at 10% opacity). Active state uses the primary-active color.

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Read More" or "Close." Hover state adds a subtle underline. Color matches the surrounding body text (#555555) or ink (#1e1f26) depending on context.

**`button-accent-teal`** — A secondary accent button using the brand's teal (#1ea0c3) on a white or soft canvas background. Used for "Book a Consultation" or "Ask an Expert" CTAs. Hover state darkens to #0693e3. This button signals a different kind of action — educational or consultative rather than transactional.

### Cards
**`product-card`** — A softly rounded card (12px radius) on a white surface (#ffffff) with a subtle drop shadow (0 2px 8px rgba(30,31,38,0.06)). Contains a product image, title in serif body-sm, price in monospace caption, and optional badges. The card never uses hard corners, maintaining the brand's soft, tactile feel. Hover state lifts the shadow slightly (0 4px 16px rgba(30,31,38,0.1)).

**`product-card-badge`** — Small monospace badges (10px, uppercase) that sit on product cards to indicate "New," "Limited Edition," or "Best Seller." The mint badge (#02e49b) signals newness, while the blush badge (#e94c89) signals sale or limited availability. Badges use 4px corner radius and tight padding.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on the soft canvas background (#f0f0f0). Navigation links use monospace uppercase at 13px with 1px letter-spacing. The active link is indicated by a 2px solid underline in the primary amber (#eac078). Inactive links sit in muted gray (#949494). The bar contains the brand logo (typically in ink), navigation links, a search icon, and a cart icon.

**`nav-link-active`** / **`nav-link-inactive`** — Active links use ink (#1e1f26) with an amber underline; inactive links use muted gray (#949494). Hover state transitions from muted to ink with a 0.15s ease.

### Forms
**`text-input`** — A standard text input on a white surface (#ffffff) with a 1px hairline border (#dddddd) and 8px corner radius. Body text at 16px in serif. Focus state shifts the border to primary amber (#eac078). Error state uses the accent orange (#f45800) border. The input height of 48px provides comfortable touch targets.

**`search-bar`** — A compact search input at 44px height with a white surface and soft border. Uses body-sm typography (14px serif) for placeholder text. The search icon sits to the left in muted gray (#949494).

### Hero
**`hero-section`** — A full-width hero section with generous vertical padding (64px top and bottom) on the soft canvas background. The headline uses the monospace display-xl at 32px with negative letter-spacing for a refined, editorial look. A subtle bottom hairline (#dddddd) separates the hero from the content below. The hero may include a primary CTA button and a supporting image or video.

### Footer
**`footer`** — A dark footer on the ink background (#1e1f26) with muted-soft text (#cccccc) for readability. Links use the link typography (14px serif) and hover to a lighter shade. The footer contains brand information, navigation links, social icons, and a newsletter signup form. Padding is generous at 48px top and bottom.

### Accordion
**`accordion-header`** — Used for FAQ sections and ingredient details. The header uses title-md typography (20px serif) on the canvas background, with a clickable area that expands to reveal content. A chevron icon rotates on open. The header has padding on top and bottom (12px) with a hairline separator.

**`accordion-content`** — The expanded content area uses body-sm typography (14px serif) with muted body text (#555555). Content fades in with a 0.2s ease. Bottom padding of 12px maintains spacing before the next accordion item.

### Badges & Labels
**`product-card-badge`** — Small monospace badges (10px, uppercase) that sit on product cards to indicate "New," "Limited Edition," or "Best Seller." The mint badge (#02e49b) signals newness, while the blush badge (#e94c89) signals sale or limited availability. Badges use 4px corner radius and tight padding.

**`rating-stars`** — Star ratings rendered in the primary amber (#eac078) at 16px. Used on product cards and review sections. Empty stars use muted-soft (#cccccc). The star color is the same as the primary CTA, creating a visual link between quality signals and action.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to 24px; buttons become full-width; footer stacks links vertically |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero text at 28px; side-by-side content sections; accordions remain single-column |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero at full display-xl (32px); multi-column footer; side panels for ingredient details |
| Wide | > 1440px | Max-width container at 1440px; content centered; additional whitespace on sides; product grid can expand to four columns; larger hero imagery |

### Touch Targets
- All interactive elements maintain minimum 44x44px touch targets (buttons, links, icons)
- Product card tap targets are the entire card surface, not just text
- Accordion headers have 48px minimum tap height
- Nav bar icons (search, cart, hamburger) are 44x44px tap areas
- Form inputs are 48px tall for comfortable touch interaction

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px
- Product grid collapses from 3 columns to 2 at tablet, to 1 at mobile
- Footer link columns collapse to a single stacked column below 744px
- Hero section reduces vertical padding from 64px to 32px on mobile
- Accordions remain single-column at all breakpoints
- Side-by-side ingredient details collapse to stacked layout on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted from the live site; transitions and animations are inferred from brand behavior
- Error states for forms (validation messages, error icons) are not documented
- Dark mode values are not present in the extracted data; the brand may not support dark mode
- Sub-brand or seasonal palette variations (e.g., holiday collections, limited editions) are not captured
- Specific font weights beyond 400 are not confirmed; the brand may use additional weights
- Iconography system (stroke vs. filled, sizes, color usage) is not documented
- Loading states, skeleton screens, and empty states are not captured
- Modal and overlay specifications (backdrop color, animation, sizing) are absent
- Typography hierarchy for mobile may differ from desktop; responsive font sizes are inferred
- The brand's use of serif vs. monospace in different contexts is based on frequency analysis, not explicit documentation
- Shadow and elevation tokens are not defined; current values are inferred from common design patterns
- Print stylesheet specifications are not available
- Accessibility contrast ratios between text and background colors have not been verified against WCAG standards
