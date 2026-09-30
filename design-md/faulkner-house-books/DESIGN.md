---
version: alpha
name: "Faulkner House Books"
source_url: "https://www.faulknerhousebooks.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A sanctuary for fine literature rendered in deep navy #003388, a color that reads like the spine of a vintage hardcover — authoritative, quiet, and utterly distinct from the pastels and earth tones of most independent bookstores. The brand lives in the tension between that saturated primary and a crisp white canvas (#fafafa), with accents of gold (#f0b849) and teal (#1c7c7c) that feel like the foil stamping and marbled endpapers of a rare edition. Typography leans on Georgia and Courier, serif and monospace working together to evoke the printed page and the typewriter — the tools of the literary trade. The site’s architecture is spare and intentional: a single-column hero with a full-bleed image, a navigation that reads like a table of contents, and product cards with `{rounded.sm}` corners that feel like the edges of a well-loved book. There is no visual noise, no carousel, no pop-up — just the quiet confidence of a room full of books. The primary CTA, a navy rectangle with gold text, is the only moment of high contrast, and it lands like a bookmark slipped between pages. The brand’s signature move is the use of the extracted #003388 as a full-bleed background on the hero and footer, with white text set in Georgia at a generous `{spacing.lg}` line-height, creating a reading experience that feels like settling into a leather chair. The extracted palette includes a wide range of blues and grays, but the distinctive navy and gold are the brand’s true voice — the rest are likely framework defaults and widget colors.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#99aacc"
  ink: "#1e1e1e"
  body: "#32373c"
  muted: "#757575"
  muted-soft: "#949494"
  hairline: "#dcdcde"
  hairline-soft: "#e0e0e0"
  canvas: "#fafafa"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#f0b849"
  accent-gold: "#f0b849"
  accent-teal: "#1c7c7c"
  accent-red: "#cc1818"
  star-rating: "#f0b849"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Courier', 'Courier 10 Pitch', 'Andale Mono', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Courier', 'Courier 10 Pitch', 'Andale Mono', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0, 51, 136, 0.1)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base} 0"
    borderBottom: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a solid navy rectangle with gold uppercase text. Used for "Add to Cart", "Subscribe", and "Browse Collection". On hover, the background deepens to `{colors.primary-active}` (#002266). In its disabled state, the button fades to a muted blue-gray `{colors.primary-disabled}` with white text, signaling an unavailable action. The `{rounded.sm}` (4px) corner is a deliberate choice — sharp enough to feel authoritative, soft enough to remain approachable.

**`button-secondary`** — An outlined variant with a white background, navy text, and a 2px navy border. Used for "Learn More" and "View Details" actions. The border provides visual weight without competing with the primary button. On hover, the background fills with `{colors.primary}` and text shifts to gold.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel" or "Back to Browsing" links. The text color is `{colors.primary}` and underlines on hover. This is the quietest button in the system, reserved for secondary navigation.

### Cards
**`product-card`** — A white card with a 1px soft hairline border and `{rounded.sm}` corners. Contains a book cover image, title in `{typography.title-sm}`, author name in `{typography.body-sm}`, price in `{typography.body-md}`, and optional badges. On hover, the border shifts to `{colors.primary}` and a subtle box shadow appears, creating a gentle lift effect. The card is designed to feel like a physical book on a shelf — clean, rectangular, and focused on the cover art.

**`product-card-badge`** — A small gold (`{colors.accent-gold}`) pill with dark text, used to indicate "Signed Copy", "First Edition", or "Staff Pick". The `{rounded.xs}` (2px) corner keeps it tight and unobtrusive. Badges are positioned at the top-left of the card, like a price tag on a rare book.

### Navigation
**`nav-bar`** — A fixed white bar at the top of the page, 72px tall, with a soft bottom border. The logo sits on the left, navigation links on the right. Links are set in uppercase Georgia with `{typography.nav-link}`. The active page link has a 2px navy bottom border; inactive links are muted gray. The nav is intentionally sparse — typically "Books", "Events", "About", "Contact", and a search icon.

**`nav-link-active`** — The active navigation state, distinguished by a 2px solid navy underline and navy text. This is the only visual indicator of the current page, keeping the nav clean and uncluttered.

### Forms
**`text-input`** — A white input field with a 1px hairline border and `{rounded.sm}` corners. Used for search, email signup, and contact forms. On focus, the border thickens to 2px and turns navy (`{colors.primary}`). The input height is 48px, matching the button height for consistent form layouts. Placeholder text is set in `{typography.body-md}` with `{colors.muted}` color.

### Hero
**`hero-section`** — A full-width section with a navy (`{colors.primary}`) background and white text. The hero features a large headline in `{typography.display-xl}`, a subheading in `{typography.body-lg}`, and a gold CTA button. The section has generous padding (`{spacing.section}` top and bottom) to create breathing room. The hero may include a background image overlaid with a navy scrim for readability.

**`hero-cta`** — The hero's primary button, inverted from the standard `button-primary`: gold background with navy text. This inversion creates a visual anchor against the navy hero background, drawing the eye to the single most important action on the page.

### Footer
**`footer-section`** — A full-width navy footer with white and gold text. Links are set in `{typography.link}` with gold color, shifting to white on hover. The footer typically includes a newsletter signup form, store hours, and social links. The consistent use of navy anchors the page, creating a bookend effect with the hero.

### Badges
**`badge-new`** — A teal (`{colors.accent-teal}`) badge for new arrivals, with white uppercase monospace text. The teal is a distinctive accent that stands out against both white cards and navy backgrounds.

**`badge-sale`** — A red (`{colors.accent-red}`) badge for discounted items, using the same monospace style. The red is the only warm accent in the system, reserved for urgency and savings.

### Other Components
**`rating-stars`** — Gold (`{colors.star-rating}`) star icons, 16px each, used for customer reviews. The gold matches the primary accent, tying the rating system to the brand's premium feel.

**`divider`** — A 1px hairline line used to separate sections within a page. It's the quietest structural element, providing visual hierarchy without drawing attention.

**`section-heading`** — A section title with a 2px navy bottom border, used to introduce content blocks like "New Arrivals" or "Staff Picks". The border creates a clear visual break and reinforces the brand color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; hero text reduces to `{typography.display-lg}`; product cards stack vertically; footer links stack; search bar becomes full-width |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero maintains two-column layout with text and image side by side; footer splits into two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero uses full `{typography.display-xl}`; footer uses three columns; maximum content width capped at 1128px |
| Wide | > 1440px | Content remains centered at 1128px max-width; additional whitespace on sides; hero image may extend to full viewport width; product grid can expand to four columns if content allows |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines.
- The `{spacing.base}` (16px) padding around touch targets ensures adequate spacing between tappable elements.
- The search bar and nav links are 48px tall, exceeding the minimum for comfortable tapping.
- Product cards have a minimum tap area of 44x44px for the entire card surface, not just the title or price.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu icon. The menu slides in from the right, overlaying the content with a semi-transparent scrim.
- The product grid collapses from three columns on desktop to a single column on mobile, ensuring readability on small screens.
- The hero section reduces its padding from `{spacing.section}` to `{spacing.xl}` on mobile, and the text stack reorders so the image appears above the headline.
- The footer collapses from three columns to a single stacked layout, with each section (links, newsletter, hours) separated by a `{spacing.base}` gap.
- The search bar, which is a prominent full-width element on desktop, becomes a collapsible icon on mobile that expands to a full-width input when tapped.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be reliably extracted from the static CSS. The hover states described above (button darkening, card border shift) are inferred from common patterns and the brand's aesthetic, not from live site inspection.
- Error states for form inputs (validation errors, required field indicators) were not observed on the live site. A standard red border and error message pattern is assumed but not confirmed.
- The exact font stack for body text is inferred from the extracted font list. The primary use of Georgia is assumed based on the brand's literary character, but the site may use a different serif or a mix of serif and sans-serif for different contexts.
- Dark mode is not implemented on the live site. The navy primary would likely invert to a lighter blue on dark backgrounds, but no dark mode tokens are available.
- Sub-brand palettes (e.g., for events, children's books, rare editions) were not detected. The brand may use additional accent colors for specific categories.
- The extracted color list includes many blues and grays that are likely framework defaults (WordPress admin colors, Shopify widget colors). The true brand palette is assumed to be the distinctive navy (#003388), gold (#f0b849), and teal (#1c7c7c), but the exact secondary palette is uncertain.
- Animation and transition durations (e.g., hover fade-in, menu slide) were not extracted. A standard 200-300ms ease-in-out is assumed.
- The exact line-height and letter-spacing values for typography are estimated based on common literary site patterns. The extracted CSS did not provide specific values for these properties.
- The `{rounded.full}` token is defined but not used in any component. It is reserved for potential future use (e.g., a circular author photo or a pill-shaped search bar variant).
