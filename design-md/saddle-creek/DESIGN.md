---
version: alpha
name: "Saddle Creek"
source_url: "https://www.saddlecreek.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A record label turned community brand that runs on a cyan voltage (#40d9f1) against a deep near-black ink (#191919), a pairing that reads more like an indie label's merch drop than a real-estate developer's website — which makes sense given the site's actual page title describes a masterplan community in Calaveras County. The cyan appears sparingly: as a hover underline on navigation links, as a badge background for "NEW" tags, as the fill on small icon buttons, and as the primary CTA background that sits on a white canvas (#ffffff). The body text runs at #222222 on white, with secondary copy in #767676 and hairline borders in #e6e6e6, creating a clean editorial hierarchy that lets the cyan act as the single moment of color surprise. Typography uses Montserrat for headings (weight 600–700, tight tracking at -0.3px) and Lora for body copy, a serif+sans pairing that signals both literary credibility and approachable warmth. Cards use soft rounding ({rounded.sm} at 8px), while buttons and badges use pill shapes ({rounded.full}), giving the interface a friendly, collectible feel — like a vinyl sleeve you want to pick up. The footer stacks four columns of links in #8d8d8d on #f7f7f7, with the cyan reappearing only on hover, a restrained use that makes the brand color feel earned rather than decorative.

colors:
  primary: "#40d9f1"
  primary-active: "#2bb8d0"
  primary-disabled: "#b3f0fa"
  ink: "#191919"
  body: "#222222"
  muted: "#767676"
  muted-soft: "#8d8d8d"
  hairline: "#e6e6e6"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#191919"
  badge-new: "#40d9f1"
  badge-sale: "#a81010"
  link-default: "#003388"
  link-hover: "#40d9f1"
  star-rating: "#222222"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Lora', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lora', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.15px
  badge:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  link:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica', Arial, sans-serif"
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
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
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-cyan:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-default:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 0"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.badge-sale}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.body-md}"
    textColor: "{colors.badge-sale}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
  footer-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    textTransform: uppercase
    letterSpacing: 0.5px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand cyan (#40d9f1) and pill-shaped ({rounded.full}). Text is set in Montserrat 600 at 14px with tight letter-spacing, in near-black (#191919) for contrast. On hover, the background shifts to a deeper cyan (#2bb8d0). The disabled state uses a pale cyan wash (#b3f0fa) with muted text (#767676), signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined alternative with a white fill and a thin hairline border (#e6e6e6). Same pill shape and typography as the primary button, but the text stays ink (#191919). On active state, the border thickens to the ink color and the background picks up the soft surface tint (#f7f7f7). Used for "Cancel," "View All," or secondary checkout actions.

**`button-text`** — A flat, borderless button with no background and no rounding. Text is ink (#191919) in Montserrat 600. On hover, the text color shifts to the brand cyan (#40d9f1), creating a subtle underline effect without an actual underline. Reserved for tertiary actions like "Learn More" links in cards or "Clear filters."

### Cards
**`product-card`** — A white card with an 8px rounded corner ({rounded.sm}) and a soft hairline border (#eeeeee). The image sits flush to the top with rounded top corners only. Title uses Montserrat 600 at 16px in ink (#191919), price uses Lora 400 at 16px. On hover, the card gains a subtle box-shadow (0 4px 12px rgba(0,0,0,0.08)) and the border shifts to a slightly stronger gray (#e6e6e6). Sale prices render in the brand's red (#a81010).

**`badge-new`** — A small pill-shaped badge filled with the brand cyan (#40d9f1). Text is Montserrat 700 at 11px, uppercase with 0.5px letter-spacing, in near-black (#191919). Used to flag new arrivals or recently added items. The `badge-sale` variant uses the brand red (#a81010) with white text. The `badge-outline` variant is transparent with a hairline border for less urgent labels like "Pre-order."

### Navigation
**`top-nav`** — A white bar 72px tall with a soft bottom border (#eeeeee). Navigation links are Montserrat 600 at 14px, uppercase with 0.5px letter-spacing. The default text color is ink (#191919). On hover, the text shifts to cyan (#40d9f1) and a 2px cyan underline appears. The active page uses a 2px ink underline instead. The nav includes a centered logo lockup and a right-aligned icon group (search, cart, account) using the `icon-button-circle` component.

**`search-bar`** — A pill-shaped input field with a soft gray fill (#f7f7f7), a thin hairline border, and placeholder text in Lora 14px (#767676). On focus, the fill turns white and the border becomes a 2px cyan ring (#40d9f1). The search icon sits inside the pill on the left, and a clear "X" appears on the right once text is entered.

### Forms
**`text-input`** — A standard rectangular input with 8px rounding ({rounded.sm}), a white fill, and a hairline border (#e6e6e6). Body text is Lora 16px (#222222) with 12px horizontal padding. On focus, the border becomes a 2px cyan ring. The error state swaps the border to the brand red (#a81010). Labels sit above the input in Montserrat 13px 500 (#767676).

### Footer
**`footer-section`** — A soft gray band (#f7f7f7) with a hairline top border, containing four columns of links. Column headings are Montserrat 13px 500, uppercase with 0.5px letter-spacing, in ink (#191919). Links are Montserrat 14px 500 in muted-soft (#8d8d8d). On hover, links shift to the brand cyan (#40d9f1). The bottom row holds legal text in caption-sm (#8d8d8d) and social icon links using the `icon-button-circle` component.

### Hero
**`hero-section`** — A full-width section with a near-black background (#191919) and white text. The headline uses Montserrat 700 at 36px with tight tracking. A single `hero-cta` button sits below the headline, using the brand cyan fill with near-black text. The hero may include a background image or pattern overlay, but the base color is always the deep ink.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack full-width; hero padding reduces to 32px; footer columns stack to 2x2 grid; search bar moves to a slide-down panel |
| Tablet | 744–1128px | Two-column product grid; top-nav shows 4–5 links; footer columns display as 2x2; hero text scales to 28px; search bar remains in nav |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; footer shows 4 columns; hero text at 36px; search bar visible in nav |
| Wide | > 1440px | Max-width container at 1440px with auto margins; product grid can show 4 columns; hero uses a wider background image; all spacing scales proportionally |

### Touch Targets
- All interactive elements (buttons, links, icons) have a minimum touch target of 44x44px.
- Icon buttons in the top nav are 40x40px circles ({rounded.full}) with 24px icons centered inside.
- Search bar height is 44px on all breakpoints to maintain tap comfort.
- Product card images are at least 200px tall on mobile to provide a tappable surface.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu below 744px. The hamburger icon is a 40x40px circle with three stacked lines in ink (#191919). The slide-out panel uses the full viewport height with a white background and links in Montserrat 600 at 18px.
- The footer's four-column layout collapses to two columns at tablet and a single column at mobile, with each column's links stacking vertically.
- The hero section's background image may crop or shift focus on smaller screens; the text and CTA remain centered and full-width.
- Product grids collapse from 4 columns on wide screens to 3 on desktop, 2 on tablet, and 1 on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is dominated by grays (#eeeeee, #e6e6e6, #222222, #aaaaaa, #444444, #8d8d8d, #888888, #efefef, #fafafa, #e2e2e2, #f7f7f7, #9a9a9a, #767676, #e4e4e4, #202020, #eaeaea, #8a8a8a, #e8e8e8, #777777, #e3e3e3, #282828, #f9f9f9, #f4f4f4) and a few blues (#003388, #5897fb, #008aff) that may be framework defaults or social-icon colors. The most distinctive non-gray color is #40d9f1 (cyan), which has been chosen as the primary brand color. The red #a81010 appears to be a sale/badge color. The actual brand may have a more nuanced palette that wasn't captured.
- Font-family declarations included "Lora" and "Montserrat" among many system fallbacks. These have been assigned as the primary heading and body fonts respectively, but the actual font weights, sizes, and pairings are inferred from common usage patterns rather than extracted CSS.
- Hover states for buttons and links are estimated based on common design patterns (darkening the primary color, adding underlines). The actual hover transitions (duration, easing, color values) were not extractable.
- Error states for forms (red border, error message styling) are assumed from the presence of #a81010 in the palette. The actual error message typography and iconography are unknown.
- Dark mode is not supported by the extracted data. The palette is entirely light-mode (white canvas, near-black ink). If a dark mode exists, it was not detected.
- The hero section's background treatment (image overlay, gradient, or solid color) is inferred from the #191919 ink color appearing frequently. The actual hero composition is unknown.
- Sub-brand or collection-specific color variations (e.g., for different artist releases or community phases) were not captured. The palette above represents the global site defaults.
- Animation durations, easing curves, and micro-interactions (button press, card lift, nav underline transition) are not documented because they could not be extracted from static CSS analysis.
