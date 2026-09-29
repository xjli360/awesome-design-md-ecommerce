---
version: alpha
name: "Flamingo Estate"
source_url: "https://flamingoestate.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Flamingo Estate is a California-born bath, body, and home brand that feels like stepping into a sun-drenched garden studio where the soil is still on the tomatoes. The palette is rooted in a deep, earthy olive {colors.primary} (#45523e) that appears on primary buttons and key accents, balanced by a soft, almost chalky cream {colors.canvas} (#fcfbf6) that serves as the background for most pages. Secondary surfaces use a muted sage {colors.surface-soft} (#eff2e9), while product cards and content blocks sit on a clean white {colors.surface-card} (#ffffff). The brand’s signature red — a warm, slightly brickish tone {colors.badge-red} (#a32121) — appears on sale badges, limited-edition flags, and small accent dots, providing a pop of heat against the otherwise cool, botanical palette. Typography leans heavily on the Exposure family — a variable, expressive serif that can shift from a delicate, almost calligraphic thin weight in headlines to a sturdy, grounded medium in body text — paired with the friendly, rounded sans-serif Maison Neue for UI labels and buttons. The overall mood is one of cultivated wildness: nothing feels overly polished, yet every detail — from the generous 32px corner radius on cards to the 64px section spacing — suggests a deliberate, tactile luxury. The brand trusts its product photography to carry emotion, using generous whitespace and a restrained color system that lets the deep greens and earthy reds of the actual ingredients (rosemary, tomato, honey) do the talking. The result is a design system that feels less like a retail interface and more like a beautifully printed seed catalog — warm, honest, and just a little bit unruly.

colors:
  primary: "#45523e"
  primary-active: "#3a4534"
  primary-disabled: "#b5bab2"
  ink: "#1c1c1c"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#d3d4dd"
  hairline-soft: "#e5e5eb"
  canvas: "#fcfbf6"
  surface-soft: "#eff2e9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-red: "#a32121"
  badge-green: "#52604a"
  accent-gold: "#ffcf2a"
  accent-blue: "#4469af"
  accent-pink: "#f3768d"
  accent-light-pink: "#ffc4e6"
  star-rating: "#ffcf2a"
  scrim: "#000000"
  social-twitter: "#00aced"
  social-facebook: "#4469af"
  error: "#c8232c"

typography:
  display-xl:
    fontFamily: "'Exposure', 'Exposure VAR', 'Exposure-20', Georgia, serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Exposure', 'Exposure VAR', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Exposure', 'Exposure VAR', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-md:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Maison Neue', 'Helvetica', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  decorative-serif:
    fontFamily: "'Home Sweet Home', 'Triptych', 'Triptych Italic', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}20"
  text-input-error:
    borderColor: "{colors.error}"
    textColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
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
    padding: 12px 28px
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  badge-sustainable:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.md} {spacing.md} {spacing.lg}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  social-icon:
    color: "{colors.muted}"
    hoverColor: "{colors.primary}"
    size: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe", and key conversion points. Rendered in the deep olive {colors.primary} (#45523e) with white text and a subtle 8px corner radius. On hover, it shifts to a darker, more forest-like {colors.primary-active} (#3a4534). The disabled state uses a muted sage {colors.primary-disabled} (#b5bab2) to signal inactivity without visual noise. Text is set in Maison Neue at 14px, uppercase, with 0.5px letter spacing for a refined, editorial feel.

**`button-secondary`** — Used for less prominent actions like "Learn More" or "View Details". It appears as a solid button on the cream {colors.canvas} (#fcfbf6) background with olive text. The outline variant (`button-secondary-outline`) uses a transparent background with a 1px solid border in {colors.primary}, maintaining the same typography and padding. Both variants share the same 44px height and 8px corner radius.

**`button-tertiary-text`** — A text-only button used for inline actions like "Cancel" or "Clear filters". No background or border, just the olive text in Maison Neue uppercase. Hover state adds a subtle underline.

**`button-pill-primary`** — A pill-shaped variant used for newsletter signups, filter tags, or quick-add actions. Uses the full 9999px radius with tighter padding (10px 24px) and smaller uppercase text. The outline version (`button-pill-outline`) is transparent with an olive border, perfect for secondary filter options.

### Cards
**`product-card`** — The primary content container for product listings on collection pages and the homepage. A clean white card with a 20px corner radius, no padding on the outer container (the image fills the top), and inner content padding of 16px. The title uses {typography.title-sm} in {colors.ink} (#1c1c1c), while the price sits below in {typography.body-sm} in {colors.body} (#272d45). Badges overlay the top-left corner of the image area.

**`product-card-badge`** — Small, uppercase labels that flag sale items, new arrivals, or sustainability credentials. Sale badges use the brand's signature red {colors.badge-red} (#a32121) with white text, while "New" badges use a warm gold {colors.accent-gold} (#ffcf2a) with dark text. Sustainable or garden-fresh badges use the deeper green {colors.badge-green} (#52604a). All badges share an 8px corner radius and tight 4px 10px padding.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on the cream canvas background. Navigation links are set in Maison Neue at 14px, uppercase, with 0.5px letter spacing. Active links render in {colors.primary}, inactive links in {colors.muted} (#676986). The bar includes a centered logo (typically the Flamingo Estate wordmark or icon) and a right-aligned cart icon with a badge count.

**`nav-link-active`** and **`nav-link-inactive`** — Define the active and default states for top-level navigation items. Active links use the olive primary color; inactive links use the muted gray-blue. No background change — the color shift alone signals state.

### Forms
**`text-input`** — Standard text input for email signups, search, and address forms. Rendered on the cream canvas background with 12px 16px padding and a 48px height. The focus state adds a 2px olive ring at 12.5% opacity (`{colors.primary}20`). Error state uses the brand's red {colors.error} (#c8232c) for both border and text.

**`search-bar`** — A pill-shaped search field used in the header and on collection pages. It sits on the soft sage surface {colors.surface-soft} (#eff2e9) with a full 9999px radius, 48px height, and 12px 20px padding. The placeholder text uses {colors.body} (#272d45) for readability.

### Footer
**`footer-section`** — The site footer uses a bold inversion: a deep olive {colors.primary} (#45523e) background with white text. Links are set in Maison Neue at 14px with standard weight, and headings use the title-sm token. The footer typically includes three to four columns: "Shop", "About", "Help", and "Follow Us" with social icons. Spacing uses 48px vertical padding and 24px horizontal padding.

**`footer-link`** — Footer links are white on the olive background, using the standard link typography. Hover state adds a subtle opacity shift (not captured in tokens but observed in practice).

### Accordion
**`accordion-header`** — Used on product detail pages for "Details", "Ingredients", and "Shipping" sections. A clean white background with the title-sm typography in {colors.ink}. The header includes a plus/minus icon toggle. Padding is 16px on all sides.

**`accordion-content`** — The expandable content area beneath each accordion header. Uses body-md typography in {colors.body} (#272d45) with 12px top padding and 24px bottom padding. Content typically includes bullet lists of ingredients or shipping details.

### Hero
**`hero-section`** — The full-width hero banner on the homepage and key landing pages. Uses the soft sage {colors.surface-soft} (#eff2e9) background with the display-xl typography in the Exposure serif. The hero includes a headline, a short body paragraph, and a primary CTA button. Section-level padding of 64px vertical and 24px horizontal creates generous breathing room.

**`hero-cta`** — The primary button within the hero section, identical in styling to `button-primary` but explicitly defined for hero context to allow for potential future differentiation (e.g., larger size on wide screens).

### Badges
**`badge-sale`**, **`badge-new`**, **`badge-sustainable`** — Three distinct badge types for product cards and promotional banners. Sale badges use the signature red (#a32121), new badges use gold (#ffcf2a), and sustainable/garden badges use a deeper green (#52604a). All share the same typography (11px, 700 weight, 0.8px letter spacing, uppercase) and 8px corner radius. Padding is 4px 10px for a compact, label-like appearance.

### Social Icons
**`social-icon`** — Social media icons (Instagram, Twitter, Facebook, Pinterest) used in the footer and "Follow Us" sections. Default color is {colors.muted} (#676986), shifting to {colors.primary} (#45523e) on hover. Icons are 20px in size. The brand's specific social colors (Twitter blue #00aced, Facebook blue #4469af) are defined in the color palette but used only for the icon fills themselves, not for hover states.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero text reduces to 28px; buttons become full-width; accordion becomes default for all content sections; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav remains visible but condensed; hero text at 36px; buttons remain inline; footer shows two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 48px display text; standard button sizing; footer shows four columns |
| Wide | > 1440px | Four-column product grid max; hero text scales to 56px; max-width container at 1440px with centered content; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons (cart, search, hamburger) use 40px circular touch targets
- Accordion headers have 48px minimum touch height
- Product card tap targets cover the full card area
- Filter tags and badge buttons use 36px minimum height

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Product grid reduces from 4 columns to 1 column on mobile
- Footer columns collapse from 4 to 2 on tablet, to 1 on mobile
- Hero section reduces vertical padding from 64px to 32px on mobile
- Accordion sections become the default layout for all collapsible content on mobile
- Search bar moves from inline to a full-width overlay on mobile
- Secondary navigation (category filters) collapses to a horizontal scroll strip on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (especially secondary buttons, text inputs, and footer links) were inferred from common patterns rather than extracted from live CSS — actual opacity shifts or color transitions may differ
- Error state styling for forms (text-input-error) uses the brand's red (#c8232c) but the exact border width, icon placement, and error message typography could not be verified
- Dark mode is not supported and no dark mode tokens were found in the extracted data
- Sub-brand or seasonal palette variations (e.g., holiday collections, limited-edition drops) may introduce additional accent colors not captured here
- The exact font weights and sizes for the Exposure variable font family were approximated — the actual CSS may use different axis values (weight, width, optical size) that produce subtly different visual results
- Animation and transition tokens (duration, easing, delay) were not extracted and are not included — the brand likely uses subtle fade and slide transitions that are not captured
- The "Home Sweet Home" and "Triptych" decorative fonts were found in declarations but their specific usage context (headlines, pull quotes, decorative elements) is inferred
- Social icon hover colors use the brand's primary olive, but the actual implementation may use the platform-specific brand colors (Twitter blue, Facebook blue) on hover
- The scrim color (#000000) is defined but its opacity value for modal overlays or lightboxes was not extracted
- Product card shadow or elevation values were not found in the extracted data — cards may use subtle box-shadow that is not captured
- The exact padding and spacing for mobile-specific layouts (hamburger menu, slide-out drawer) were not extracted and use standard spacing tokens as approximations
