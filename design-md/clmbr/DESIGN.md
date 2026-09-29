---
version: alpha
name: "Clmbr"
source_url: "https://clmbr.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy (#003388) anchors Clmbr's digital presence — not the generic blue of a thousand fitness apps, but a specific, almost Prussian blue that reads as serious, engineered, and premium. This primary color saturates the brand's primary CTAs, navigation elements, and key product highlights, creating a consistent voltage across the climbing-machine experience. The palette extends into a secondary blue (#282bcf) that adds a jolt of energy to secondary actions and accent elements, while a near-black (#282828) grounds body text and structural components. The brand's typography system leans heavily on Maison Neue, a geometric sans-serif that appears in multiple weights — from the bold "Plaak" display face used for hero headlines to the lighter "Maison Book" weights for body copy — creating a clear hierarchy between marketing messaging and functional interface text. Clmbr's design language is notably angular and structured, with sharp corners on buttons and cards that communicate precision and durability, contrasting with the pill-shaped softness common in consumer fitness apps. The interface uses generous whitespace and a light canvas (#eeeeee) to let product photography and the distinctive navy palette breathe, while hairline borders (#b6b6b6) provide subtle structural definition without visual noise. The overall impression is one of industrial sophistication — a brand that sells a serious piece of equipment and trusts its product's visual presence over decorative interface flourishes.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#8099bb"
  ink: "#282828"
  body: "#32373c"
  muted: "#616161"
  muted-soft: "#888888"
  hairline: "#b6b6b6"
  hairline-soft: "#dcdde1"
  canvas: "#eeeeee"
  surface-soft: "#e8e8eb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#282bcf"
  accent-orange: "#ff6900"
  accent-green: "#00d084"
  accent-red: "#cf2e2e"
  dark-bg: "#2c324c"

typography:
  display-xl:
    fontFamily: "'Plaak', 'Maison Neue', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Plaak', 'Maison Neue', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Maison Neue', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Maison Neue', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Maison Neue', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Maison Book', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Book', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Maison Neue', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Maison Neue', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Maison Book', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Maison Neue', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Maison Neue', 'Maison', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  mono:
    fontFamily: "'Maison Neue Mono', 'Consolas', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 31px
    height: 52px
    border: 2px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-accent:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 52px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: 2px solid "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-overlay:
    backgroundColor: "{colors.dark-bg}"
    opacity: 0.85
  feature-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  price-display:
    typography: "{typography.title-lg}"
    textColor: "{colors.ink}"
  price-currency:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  rating-stars:
    color: "{colors.accent-orange}"
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  icon-primary:
    color: "{colors.primary}"
  icon-muted:
    color: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Clmbr experience, rendered in the brand's deep navy (#003388) with white uppercase text. These buttons carry zero border radius — a deliberate design choice that communicates precision and industrial strength rather than the soft approachability of consumer fitness brands. On hover, the background deepens to `{colors.primary-active}` (#002266), and a subtle scale transform (1.02) provides tactile feedback. The disabled state uses `{colors.primary-disabled}` (#8099bb) to signal inactivity while maintaining brand recognition.

**`button-secondary`** — An outlined variant that inverts the primary button's logic: transparent background with a 2px navy border and navy text. This button is used for secondary actions like "Learn More" or "Compare Models" where the primary CTA needs visual competition. On hover, it fills solid with `{colors.primary}`, flipping to white text. The `{rounded.none}` treatment and uppercase `{typography.button-md}` typography maintain consistency with the primary button.

**`button-accent`** — A high-energy variant using `{colors.accent-blue}` (#282bcf) for actions that need to stand out from the primary navy system — typically used for promotional CTAs, limited-time offers, or "Shop Now" buttons on featured products. Same structural properties as `button-primary` but with a distinctly different color voltage.

### Navigation
**`nav-bar`** — A fixed-position top navigation bar at 72px height, using `{colors.canvas}` (#eeeeee) as background with `{colors.ink}` (#282828) text. The navigation uses `{typography.nav-link}` at 14px with 0.3px letter spacing for a refined, slightly spaced-out appearance. Active nav items are indicated by a 2px bottom border in `{colors.primary}` and navy text color. The logo sits left-aligned, typically rendered in the primary navy or as a white version on dark hero sections.

### Cards
**`product-card`** — Product display cards with zero border radius, white backgrounds, and subtle shadow (0 2px 8px rgba(0,0,0,0.08)). These cards feature a full-width product image at the top with no rounded corners, followed by product title, price, and a rating display. The card maintains generous internal padding (`{spacing.base}`) and uses `{typography.body-sm}` for descriptive text. On hover, the shadow deepens to 0 4px 16px rgba(0,0,0,0.12) and a subtle translateY(-2px) provides lift.

### Forms
**`text-input`** — Clean, rectangular input fields with a 1px `{colors.hairline}` border and white background. On focus, the border thickens to 2px and adopts `{colors.primary}` (#003388), creating a clear active state without additional visual noise. Input height is 48px with 12px vertical padding and 16px horizontal padding. Placeholder text uses `{colors.muted}` (#616161) at `{typography.body-md}` weight.

### Hero Section
**`hero-section`** — Full-width hero blocks that use `{colors.primary}` (#003388) as background with white text, creating dramatic contrast for headline messaging. The hero accommodates `{typography.display-xl}` (48px) headlines, optional overlay text on product imagery, and primary CTAs. On pages with product photography, an optional `hero-overlay` component with `{colors.dark-bg}` at 85% opacity ensures text readability against varied image backgrounds.

### Footer
**`footer`** — A dark footer section using `{colors.dark-bg}` (#2c324c) as background with white text at 80% opacity for links. The footer organizes content in a multi-column layout with section headings in `{typography.title-md}` and body links in `{typography.link}`. Link hover states increase opacity to 100% for clear interaction feedback. The footer includes brand logo, product links, support resources, and social media icons.

### Badges
**`feature-badge`** — Small rectangular badges using `{colors.accent-orange}` (#ff6900) for promotional flags like "New", "Best Seller", or "Limited Edition". These badges use `{typography.badge}` (11px uppercase) with tight padding (4px 8px) and zero border radius, sitting flush against product card edges or hero section overlays.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero text reduces to `{typography.display-lg}` (36px); product cards stack vertically; buttons become full-width; footer collapses to single column |
| Tablet | 744–1128px | Two-column product grid; nav remains expanded with condensed link spacing; hero maintains two-column layout with reduced padding; side-by-side content sections |
| Desktop | 1128–1440px | Full three-column product grid; expanded nav with all links visible; hero at full padding; multi-column footer; standard content section spacing |
| Wide | > 1440px | Max-width container (1440px) centered; hero background extends full-width while content remains constrained; product grid can accommodate 4 columns; increased whitespace around content sections |

### Touch Targets
- All interactive elements maintain minimum 44px touch target height
- Buttons at 52px height exceed minimum accessibility requirements
- Nav links have 44px minimum tap area even when text is smaller
- Product card CTAs are full-width on mobile for easy tapping

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Multi-column footer collapses to single column below 744px
- Product grid reduces from 3 columns → 2 columns → 1 column as viewport shrinks
- Hero section reduces from two-column layout to stacked single column below 744px
- Side-by-side feature sections stack vertically below 744px
- Search functionality collapses to icon-only trigger below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for most components were inferred from common patterns rather than extracted from live CSS — actual implementations may vary
- Error states for form inputs (validation styling, error messages) were not extractable from the live site
- Dark mode preferences or alternate color schemes were not detected
- Sub-brand or campaign-specific color variations (e.g., limited edition product pages) could not be extracted
- Animation timing and easing curves (transitions, hover effects) were not reliably extractable
- The exact font weight for "Plaak" display face is inferred — the extracted CSS showed "Plaak" as a font-family but did not specify available weights
- Spacing values for section padding and component margins are estimated based on common patterns rather than extracted measurements
- The extracted color list includes many generic web palette colors (grays, blues, standard accent colors) — the true brand palette likely focuses on the distinctive navy (#003388) and accent blue (#282bcf) with supporting neutrals
- Icon system details (SVG vs icon font, specific icon set, sizing conventions) were not extractable
- Loading states, skeleton screens, and empty states were not observable from the static site analysis
- The "Maison" font family appears in multiple variants (Maison, Maison Book, Maison Neue) — exact usage rules between these variants could not be fully determined
