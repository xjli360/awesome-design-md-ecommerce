---
version: alpha
name: "Saatva"
source_url: "https://www.saatva.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Saatva's design language is a study in restrained luxury — the brand sells mattresses and bedding, but the interface reads more like a heritage textile house than a sleep startup. The palette is anchored by warm earth tones: `#6b6257` and `#463f38` form the primary ink and body, while `#fafafb` and `#f6f5f3` create a canvas that feels like soft linen rather than sterile white. Accents of `#b19780` and `#d5aa63` appear in badges and decorative elements, evoking the gilded edges of a well-bound book. The brand's signature green — `#597554` — surfaces in sustainability badges and eco-notes, while `#c80000` provides a restrained alert red. Typography leans on Georgia and Source Serif Pro for display roles, pairing with Open Sans for body — a classic editorial combination that signals trust and permanence. Buttons use `{rounded.sm}` (8px) — soft but not pillowy — and cards use `{rounded.md}` (12px), suggesting a brand that values comfort without sacrificing structure. The overall mood is hushed, substantial, and tactile: every `{hairline}` in `#d2d2d2` and `{muted-soft}` in `#909090` reinforces the sense of a space designed for quiet, not noise.

colors:
  primary: "#6b6257"
  primary-active: "#463f38"
  primary-disabled: "#c7c6c4"
  ink: "#282828"
  body: "#3a3a3a"
  muted: "#8c8273"
  muted-soft: "#909090"
  hairline: "#d2d2d2"
  hairline-soft: "#e3e3e3"
  canvas: "#fafafb"
  surface-soft: "#f6f5f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#d5aa63"
  accent-green: "#597554"
  accent-teal: "#62c2b1"
  accent-sage: "#b19780"
  accent-blush: "#c19678"
  accent-red: "#c80000"
  badge-sale: "#c80000"
  badge-new: "#597554"
  badge-eco: "#62c2b1"
  star-rating: "#d5aa63"
  scrim: "#000000"
  footer-bg: "#282828"
  footer-text: "#f8f8f8"

typography:
  display-xl:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Georgia', 'Times New Roman', Times, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', Times, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif"
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
    padding: 14px 32px
    height: 48px
  button-primary-hover:
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
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-tertiary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-gold-hover:
    backgroundColor: "#c49a4f"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
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
    rounded: "{rounded.sm}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
    rounded: "{rounded.sm}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  top-nav-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  product-card-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-eco:
    backgroundColor: "{colors.badge-eco}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 40px"
    height: 56px
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
    rounded: "{rounded.full}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-gold}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.footer-text}"
  accordion-trigger:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
    rounded: "{rounded.sm}"
  accordion-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.md} {spacing.lg}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  review-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
    rounded: "{rounded.md}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Shop Now", "Add to Cart", and "See Details" actions. Uses the brand's warm taupe `{colors.primary}` background with white text in uppercase Open Sans 600 weight. Hover state deepens to `{colors.primary-active}` (#463f38) for a tactile press feel. Disabled state fades to `{colors.primary-disabled}` (#c7c6c4) with no shadow. All primary buttons maintain `{rounded.sm}` (8px) corners — soft enough to feel approachable, square enough to feel substantial.

**`button-secondary`** — An outlined variant for secondary actions like "Compare Models" or "Learn More". Uses a white `{colors.canvas}` background with a 2px `{colors.primary}` border and matching text. On hover, the button fills solid with `{colors.primary}` and text inverts to white — a satisfying reversal that signals readiness.

**`button-tertiary`** — A text-only button for subtle actions like "Cancel" or "Skip". Transparent background with `{colors.primary}` text, no border. Hover adds a `{colors.surface-soft}` background wash for a gentle affordance without competing with primary/secondary buttons.

**`button-gold`** — A special accent button reserved for premium offers, loyalty rewards, and "Saatva Insider" program calls-to-action. Uses `{colors.accent-gold}` (#d5aa63) background with dark `{colors.ink}` text — the gold reads as luxury without being ostentatious. Hover deepens to #c49a4f.

### Cards
**`product-card`** — The core product display unit, used on collection pages and category grids. A white `{colors.surface-card}` background with `{rounded.md}` (12px) corners. The card image area uses `{rounded.md} {rounded.md} 0 0` to keep the top corners rounded while the bottom meets the content area squarely. On hover, a subtle `boxShadow` lifts the card — 0 4px 12px rgba(0,0,0,0.08) — creating a gentle float effect. Title uses `{typography.title-sm}` in `{colors.ink}`, price uses `{typography.body-md}` in `{colors.primary}`. Badges (sale, new, eco) sit in the top-left corner with `{rounded.xs}` (4px) and appropriate background colors.

**`review-card`** — Customer testimonial cards with a white background, `{rounded.md}` corners, and a `1px solid {colors.hairline-soft}` border. Star ratings render in `{colors.star-rating}` gold (#d5aa63). On hover, a lighter shadow (0 2px 8px rgba(0,0,0,0.06)) provides a subtle lift without competing with product cards.

### Navigation
**`top-nav`** — A fixed-position navigation bar at 72px height on desktop, collapsing to 64px on scroll with a faint `boxShadow`. Background is `{colors.canvas}` white, links are uppercase Open Sans 600 weight in `{colors.ink}`. Active nav items underline with a 2px `{colors.primary}` border. The nav includes a logo lockup (typically the Saatva wordmark in Georgia serif), a search icon, and a cart icon. On mobile, the nav collapses to a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — Standard form inputs for checkout, account creation, and contact forms. White `{colors.canvas}` background, `{colors.body}` text, `{rounded.sm}` corners, and a `1px solid {colors.hairline}` border. Focus state thickens the border to 2px `{colors.primary}`. Error state uses `{colors.accent-red}` (#c80000) border with an error icon and message below. Height is 48px for comfortable touch targets.

**`select-input`** — Dropdown selectors styled consistently with text inputs. Same dimensions, border, and focus behavior. The dropdown arrow is a custom SVG chevron in `{colors.muted}`.

### Hero Section
**`hero-section`** — The primary brand storytelling area on the homepage and key landing pages. Uses `{colors.surface-soft}` (#f6f5f3) as a warm, off-white backdrop that feels like natural linen. Headline uses `{typography.display-xl}` (48px Georgia) in `{colors.ink}`. The hero CTA button is a larger variant at 56px height with 16px 40px padding — intentionally bigger than standard buttons to anchor the page. The hero often includes a lifestyle image of a bed in a serene bedroom setting, with the text overlay positioned left or centered depending on the campaign.

### Footer
**`footer-section`** — A dark footer using `{colors.footer-bg}` (#282828) with `{colors.footer-text}` (#f8f8f8) for readability. Organized in a multi-column grid with `{typography.title-sm}` headings and `{typography.link}` text links. Link hover state shifts to `{colors.accent-gold}` (#d5aa63) for a warm, premium feel against the dark background. Includes legal text, social media icons, and a newsletter signup form.

### Accordion
**`accordion-trigger`** — Used for FAQ sections and product details. White background with `{colors.ink}` text in `{typography.title-sm}`. Padding of 16px 12px with `{rounded.sm}` corners. A chevron icon rotates on open. The `accordion-panel` below uses `{typography.body-md}` in `{colors.body}` with padding 12px 24px.

### Badges
**`badge-sale`** — Red badge (#c80000) with white text, used for promotional pricing. 11px uppercase Open Sans 700, `{rounded.xs}` (4px), padding 4px 8px.
**`badge-new`** — Green badge (#597554) with white text, used for new arrivals.
**`badge-eco`** — Teal badge (#62c2b1) with dark text (#282828), used for sustainable materials and eco-friendly certifications.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger nav, stacked product cards, hero text centered, font sizes reduce by ~20%, buttons become full-width |
| Tablet | 744–1128px | Two-column product grids, nav links collapse to hamburger, hero maintains left-aligned text but reduces padding, footer stacks to 2 columns |
| Desktop | 1128–1440px | Full multi-column layout, expanded top nav with all links visible, three-column product grids, hero at full padding, footer at 4 columns |
| Wide | > 1440px | Max-width container at 1440px, centered content, hero scales proportionally, product grids can show 4 columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are each at least 48px tall
- Accordion triggers are 48px tall for easy finger tapping
- Nav links on mobile are 48px tall with full-width tap areas
- Search bar is 48px tall with 24px horizontal padding

### Collapsing Strategy
- Top nav collapses to hamburger menu at tablet breakpoint (744px) and below
- Product grids collapse from 4 columns to 2 to 1 as viewport shrinks
- Footer collapses from 4 columns to 2 to a single stacked column
- Hero section reduces padding and font sizes, centering text on mobile
- Review cards collapse from 3-column grid to single column
- Accordion panels remain functional at all breakpoints
- Search bar collapses to icon-only on mobile, expanding to full input on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns but not verified against live site interactions
- Error styling for forms (error messages, icon positions) is assumed based on industry standards
- Dark mode is not implemented on the current site and no dark mode tokens exist
- Sub-brand palettes (Saatva Classic, Loom & Leaf, Zenhaven) may have distinct color variations not captured here
- Animation timing and easing curves are not extracted — assumed 200-300ms ease-in-out for transitions
- Focus ring styles (keyboard accessibility) are not documented — assumed 2px solid `{colors.primary}` with 2px offset
- Loading states (skeleton screens, spinners) are not captured
- Modal and dialog styling is not documented
- Tooltip and popover patterns are not extracted
- Print stylesheet behavior is unknown
- Internationalization (RTL support) is not addressed
