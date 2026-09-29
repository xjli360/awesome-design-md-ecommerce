---
version: alpha
name: "Little Passports"
source_url: "https://www.littlepassports.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy anchor (#20366a) grounds the entire experience, appearing in the top navigation, footer backgrounds, and primary button fills — a color choice that signals trust and the weight of world exploration for a young audience. Against this, a bright cyan accent (#00b3f0) and a warm coral (#f05636) create a playful, energetic counterpoint, often used for interactive elements like hover states, secondary buttons, and illustrative accents. The brand’s typography mixes a custom display font, Kookie, for headlines and playful moments, with Poppins for body text and UI labels, creating a contrast between whimsy and readability. Rounded corners are generous but not pill-like — cards and buttons use a consistent 12px radius (`{rounded.md}`), while larger containers like the hero section’s call-to-action panel use 20px (`{rounded.lg}`). The overall layout is airy, with generous whitespace and a clean white canvas (`#ffffff`) that lets the navy and accent colors breathe. Illustrations and photography of children engaged in hands-on activities are central to the brand’s storytelling, often framed by soft, rounded corners and subtle drop shadows. The design feels approachable and educational without being childish — the navy provides authority, the coral injects energy, and the cyan suggests discovery and digital-native interaction.

colors:
  primary: "#20366a"
  primary-active: "#0e2b57"
  primary-disabled: "#8d8d8d"
  ink: "#111010"
  body: "#242424"
  muted: "#5d5d5d"
  muted-soft: "#8d8d8d"
  hairline: "#cacaca"
  hairline-soft: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f1f1f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#00b3f0"
  accent-coral: "#f05636"
  accent-marigold: "#ffa211"
  accent-teal: "#01b7ac"
  accent-mint: "#16ccac"
  accent-sky: "#dcf4fd"
  accent-deep-blue: "#0067b7"
  accent-orange: "#be5404"
  accent-red: "#d63e20"
  accent-gold: "#e3ba15"

typography:
  display-xl:
    fontFamily: "'Kookie', 'Poppins', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Kookie', 'Poppins', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Kookie', 'Poppins', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Poppins', sans-serif"
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.md}"
  button-accent-cyan:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: 2px solid "{colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: 2px solid "{colors.accent-coral}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-cyan}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    boxShadow: 0px 2px 8px rgba(0, 0, 0, 0.08)
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: 64px 24px
  hero-cta-panel:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    padding: 32px
    boxShadow: 0px 4px 16px rgba(0, 0, 0, 0.1)
  badge-new:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  badge-age:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: 1px solid "{colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-cyan}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 16px
  progress-bar-track:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.accent-teal}"
    rounded: "{rounded.full}"
    height: 8px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Subscribe Now," "Get Started," and checkout flows. Filled with the deep navy `{colors.primary}`, it sits on a white or light gray canvas. On hover, it shifts to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}`. Text is always white and set in Poppins 600 with 0.5px letter spacing.

**`button-secondary`** — An outlined or ghost variant used for "Learn More" and secondary actions. It has a white background with navy text and a 1px navy border. On hover, the background shifts to `{colors.surface-soft}` and text to `{colors.primary-active}`.

**`button-accent-cyan`** — A high-energy variant used for promotional banners, age-group selectors, or interactive quiz CTAs. The bright cyan `{colors.accent-cyan}` background with dark ink text creates a playful, digital-native feel.

**`button-accent-coral`** — Used sparingly for urgent or celebratory actions like "Claim Your Free Gift" or "Limited Time Offer." The coral `{colors.accent-coral}` on white text provides strong contrast against the navy-heavy system.

### Cards
**`product-card`** — The primary content container for subscription boxes, individual products, and country kits. It uses a white background, a soft drop shadow, and `{rounded.md}` corners. The image area is slightly less rounded (`{rounded.sm}`). The title uses `{typography.title-sm}` in ink, and the price is set in `{typography.body-md}` in the primary navy.

**`hero-cta-panel`** — A larger, elevated card used in the hero section to house the main value proposition and primary CTA. It has `{rounded.lg}` corners, a white background, and a more pronounced shadow to create visual hierarchy against the hero background.

### Navigation
**`nav-bar`** — The persistent top navigation bar, filled with the deep navy `{colors.primary}`. It contains the logo, nav links, and a search icon. The height is 72px on desktop. Nav links are white with 0.3px letter spacing. The active or hover state for a nav link uses the bright cyan `{colors.accent-cyan}`.

**`nav-link`** — Individual navigation items. They are transparent by default with white text. On hover or when active, the text color changes to `{colors.accent-cyan}`. No background fill on hover — only color change.

### Forms
**`text-input`** — Standard text input for email signups, search, and account forms. It has a white background, a 1px `{colors.hairline}` border, and `{rounded.sm}` corners. On focus, the border thickens to 2px and turns `{colors.primary}`. Error state uses a 2px `{colors.accent-coral}` border.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) used in the nav bar and on search result pages. It has a white background, a subtle hairline border, and Poppins body text.

### Badges
**`badge-new`** — A small, coral-filled badge used to flag new subscriptions, products, or features. It uses uppercase Poppins 700 and `{rounded.sm}` corners.

**`badge-sale`** — A marigold-filled badge for promotional pricing or discounts. The dark ink text ensures readability against the bright yellow.

**`badge-age`** — A cyan pill badge used to indicate the recommended age range for a subscription box (e.g., "Ages 3-5"). The full rounded shape and playful color make it feel friendly and informative.

### Footer
**`footer`** — A full-width footer with a navy background. It contains link columns, social icons, and legal text. Links are white by default and turn `{colors.accent-cyan}` on hover. The layout is stacked on mobile and multi-column on desktop.

### Progress & Feedback
**`progress-bar-track`** — Used in the subscription quiz and onboarding flows. The track is a light gray pill, and the fill is a teal `{colors.accent-teal}` that progresses as the user completes steps.

**`accordion-header`** — Used in FAQ sections and product details. The header has a soft gray background and `{rounded.sm}` corners. On expand, the content area appears below with a white background and standard body text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu. Product cards stack in a single column. Hero section padding reduces to 32px. Footer links stack vertically. Search bar moves to a full-width overlay. |
| Tablet | 744–1128px | Nav bar remains horizontal but nav links may be truncated. Product cards display in a 2-column grid. Hero section uses a 50/50 split layout. Footer links in 2 columns. |
| Desktop | 1128–1440px | Full nav bar with all links visible. Product cards in a 3 or 4-column grid. Hero section uses a full-width layout with the CTA panel offset. Footer in 4 columns. |
| Wide | > 1440px | Max-width container (1200px) centers content. Hero section may have a larger background image. Product cards maintain 4-column grid with increased whitespace. |

### Touch Targets
- All buttons and interactive elements are at least 48px tall to meet WCAG touch target guidelines.
- Nav links have a minimum tap area of 44x44px.
- Accordion headers are 48px tall with generous padding.
- Badges are at least 24px tall for readability.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu on mobile (< 744px).
- The footer link columns collapse to a single column on mobile, with accordion-style expandable sections for each category.
- Product card grids reduce from 4 columns on desktop to 2 on tablet and 1 on mobile.
- The hero section's CTA panel moves from a side-by-side layout to a stacked layout on tablet and mobile.
- Search functionality shifts from an inline bar to a full-screen overlay on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover and focus states** for many components (e.g., text-input, accordion, badges) could not be reliably extracted from the static CSS. The provided active states for buttons are inferred from common patterns.
- **Error and validation styling** beyond the text-input error state is not confirmed. Form-level error messages, success states, and tooltip styling are unknown.
- **Dark mode** is not supported and no dark mode tokens exist in the extracted data.
- **Sub-brand or seasonal palettes** (e.g., holiday promotions, special edition boxes) are not captured. The accent colors provided are the most frequently occurring non-primary colors.
- **Typography scale** for Kookie is inferred from its use in display headlines. The exact font sizes and weights for Kookie in different contexts (e.g., subheadings, pull quotes) are not confirmed.
- **Iconography** — the brand uses custom icons (LP Icons font), but their specific sizes, colors, and stroke weights are not documented.
- **Animation and transition** timing values (e.g., hover fade duration, card entrance animations) are not available.
- **Spacing scale** is a best-guess based on common layout patterns. The exact `section` spacing and `xxl` values may vary across pages.
- **The extracted color list is heavily weighted toward blues and grays**, with a few bright accents. The primary `#20366a` is the most distinctive and frequently occurring color, but the brand may use a wider palette in illustrations and photography that is not captured in the CSS extraction. The accent colors listed are the most prominent non-blue, non-gray values from the extraction.
