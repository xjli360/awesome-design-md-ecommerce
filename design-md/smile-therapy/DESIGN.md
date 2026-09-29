---
version: alpha
name: "Smile Therapy"
source_url: "https://smile-therapy.co.uk"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Smile Therapy is a bright, optimistic oral-care brand that feels more like a self-care ritual than a clinical routine. The palette centers on a vibrant teal (#108474) that reads as fresh, clean, and approachable — it's the brand's primary voltage, used across CTAs, badges, and key accents. This is balanced by a warm gold (#ebbf20) and a brighter yellow (#ffd700) that add a sense of reward and positivity, often appearing on sale badges or promotional elements. The canvas is a soft off-white (#f9fafb), with cards and surfaces in pure white (#ffffff) and a very light teal-tinted surface (#edf5f5) that whispers the brand color without overwhelming. Text runs in a deep navy-ink (#3a3b53) for body copy, with a near-black (#141414) for high-impact headlines, and a slate gray (#545454) for muted labels and secondary information. Typography leans on Archivo for display and heading work — a geometric sans-serif with a confident, modern stance — while Inter handles body text with its excellent readability at small sizes. The system uses soft, friendly radii: buttons and inputs round at {rounded.sm} (8px), cards at {rounded.md} (12px), and pill-shaped elements like search bars and badges go full round at {rounded.full}. There is a deliberate absence of harsh corners, reinforcing the "therapy" promise of gentle, soothing interactions. The overall mood is clean, warm, and slightly playful — a brand that wants you to enjoy taking care of your teeth.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d5cc"
  ink: "#141414"
  body: "#3a3b53"
  muted: "#545454"
  muted-soft: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#f9fafb"
  surface-soft: "#edf5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#ebbf20"
  accent-yellow: "#ffd700"
  accent-yellow-soft: "#fbcd0a"
  accent-blue: "#536cae"
  accent-blue-bright: "#1990c6"
  accent-blue-deep: "#136f99"
  badge-sale: "#ebbf20"
  badge-new: "#108474"
  star-rating: "#ebbf20"
  footer-bg: "#333333"
  footer-text: "#eeeeee"
  footer-link: "#f6f6f6"

typography:
  display-xl:
    fontFamily: "'Archivo', 'Inter', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Archivo', 'Inter', sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Archivo', 'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Archivo', 'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Archivo', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archivo', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Questrial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Questrial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Questrial', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Questrial', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Archivo', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Archivo', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Archivo', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', 'Questrial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Archivo', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 38px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 38px
    border: "1.5px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1.5px solid {colors.primary}"
  text-input-error:
    border: "1.5px solid #d32f2f"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    color: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-best-seller:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1.5px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    color: "{colors.footer-link}"
    typography: "{typography.link}"
  footer-heading:
    color: "{colors.footer-text}"
    typography: "{typography.title-sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand teal (#108474) with white text. Used for "Add to Cart", "Subscribe Now", and primary checkout flows. On hover, it deepens to `{colors.primary-active}` (#0d6b5e). The disabled state uses `{colors.primary-disabled}` (#a3d5cc) to signal non-interactivity while maintaining brand color presence. All primary buttons use `{rounded.sm}` (8px) for a soft but not pill-like feel.

**`button-secondary`** — An outlined variant with a white fill and teal border, used for secondary actions like "Learn More" or "View Details". The active state darkens the border to `{colors.primary-active}`. This button maintains the same height and padding as the primary to ensure consistent vertical rhythm in forms and action bars.

**`button-ghost`** — A text-only button with no background or border, used in navigation drawers, modals, or as tertiary actions. Hover adds a subtle background tint (not yet tokenized). The ghost button respects the same typography and padding as the primary for alignment.

**`button-pill`** — A fully rounded pill button used for filter tags, category toggles, and compact actions. Uses `{rounded.full}` and smaller padding for a tighter footprint. The outline variant (`button-pill-outline`) swaps fill for a 1.5px border, ideal for "selected" states in filter groups.

### Cards
**`product-card`** — The standard product display card, used on collection pages and search results. Features a white background, `{rounded.md}` (12px) corners, and `{spacing.base}` (16px) padding. The image area uses `{rounded.sm}` (8px) to create a subtle nested radius effect. On hover, a soft box-shadow elevates the card. The card contains the product image, title, price, star rating, and a quick-add button.

**`testimonial-card`** — Used for customer reviews and social proof sections. Slightly more generous padding (`{spacing.lg}`) and a white background with `{rounded.md}` corners. The star rating uses `{colors.star-rating}` (#ebbf20) for a warm, gold-star aesthetic.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 72px height. The background is white, and links use `{typography.nav-link}` — uppercase Archivo at 14px with 0.5px letter-spacing for a clean, editorial feel. The active link is underlined with a 2px teal border. Inactive links render in `{colors.muted}` (#545454). The nav bar contains the logo, primary links, search icon, and cart icon.

**`nav-link-active`** — The active state for navigation links, distinguished by a teal underline and the brand teal color. This is used for the current page or section indicator.

### Forms
**`text-input`** — Standard text input used for email signups, search fields, and form entries. White background with a `{colors.hairline}` (#dedede) border and `{rounded.sm}` corners. On focus, the border thickens to 1.5px and switches to `{colors.primary}`. Error state uses a red border (#d32f2f) — this is a known gap as the exact error red wasn't extracted from the site.

**`select-input`** — Dropdown select fields styled consistently with text inputs, using the same height, padding, and border treatment. The dropdown arrow is a custom chevron (not yet tokenized).

**`quantity-selector`** — A compact input for adjusting product quantities, with a border and `{rounded.sm}` corners. Contains minus/plus buttons flanking a numeric display.

### Badges
**`badge-sale`** — A gold-background badge (#ebbf20) with dark text, used to flag discounted items. The uppercase Archivo typography at 11px keeps it compact and legible. Padding is minimal (2px 8px) with `{rounded.xs}` (4px) corners.

**`badge-new`** — A teal-background badge (#108474) with white text, used for new arrivals. Same typography and sizing as the sale badge, but with the brand primary color to signal freshness.

**`badge-best-seller`** — A blue-background badge (#536cae) with white text, used for top-selling products. This blue is a secondary accent that adds variety to the badge system without competing with the primary teal.

### Footer
**`footer`** — A dark footer section (`{colors.footer-bg}` #333333) with light text (`{colors.footer-text}` #eeeeee). Links render in a slightly lighter gray (#f6f6f6) for readability. The footer uses `{typography.body-sm}` for general text and `{typography.title-sm}` for column headings. Padding is generous at `{spacing.section}` (64px) top and bottom.

### Hero
**`hero-banner`** — The primary hero section on the homepage, using `{colors.surface-soft}` (#edf5f5) as a subtle teal-tinted background. The headline uses `{typography.display-lg}` (30px Archivo bold) in the dark ink color. The CTA button (`hero-cta`) is a larger version of the primary button with 14px 32px padding and 48px height for visual prominence.

### Accordion
**`accordion`** — Used for FAQ sections and product details. White background with a soft border (`{colors.hairline-soft}` #e2e2e2) and `{rounded.sm}` corners. Each accordion item has `{spacing.base}` padding. The expand/collapse icon is a plus/minus toggle (not yet tokenized).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-md}`; buttons become full-width; footer columns stack; search bar moves to a persistent bottom bar or hidden behind an icon |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but may truncate; hero maintains two-column layout with reduced image size; side-by-side form layouts become stacked; footer shows 2-3 columns |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero uses full two-column layout; forms are inline; footer shows full 4-column layout |
| Wide | > 1440px | Max-width container (1440px) with centered content; product grid expands to 4 columns; hero content is centered with generous whitespace; all elements maintain proportional scaling |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines.
- Icon-only buttons (search, cart, hamburger) are at least 44x44px.
- Quantity selector buttons are at least 40x40px.
- Accordion headers are at least 44px tall for easy tapping.
- Product card "Add to Cart" buttons are at least 44px tall on mobile.

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px.
- The search bar collapses to a magnifying glass icon on mobile, expanding to a full-width overlay on tap.
- The footer collapses from 4 columns to 2 columns on tablet, and to a single column on mobile.
- Product grids collapse from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Hero sections collapse from side-by-side text/image to stacked vertical layout on mobile.
- Multi-column form layouts collapse to single-column on mobile.
- Category filter strips collapse to a horizontal scrollable row on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for ghost buttons and text links were not reliably extracted — assume a subtle background tint or underline on hover.
- Error styling for form validation (red borders, error message typography) was inferred; exact error red (#d32f2f) is an assumption.
- Focus ring styles (outline, box-shadow) were not observed — implement a 2px teal outline for keyboard navigation.
- Dark mode is not supported; no dark palette tokens were found.
- Sub-brand or seasonal palette variations (e.g., holiday themes) are not documented.
- Animation and transition timing values (ease, duration) were not extracted — use 200ms ease-in-out as a default.
- Loading states (skeleton screens, spinners) were not observed — implement a teal spinner matching `{colors.primary}`.
- Dropdown menu styles (mega menu, sub-navigation) were not captured.
- Modal and overlay styles (background scrim, close button) were not extracted — use `{colors.scrim}` (#000000 at 50% opacity) as an assumption.
- Tooltip and popover styles are undocumented.
- The exact font weights for Archivo and Inter beyond what's listed (400, 500, 600, 700) are assumed based on common usage.
- The `textTransform: uppercase` on nav-link and badge is inferred from the brand's clean, editorial feel but was not explicitly extracted.
- The `boxShadow` values for card hover states are assumed (0 4px 12px rgba(0,0,0,0.08)) and may differ from the live site.
- The `border` property on button-secondary (2px solid) is an assumption based on common secondary button patterns.
- The `fontSize` for star-rating (16px) is an assumption; actual size may vary.
- The `height` values for buttons and inputs are based on common DTC patterns and may not match the live site exactly.
