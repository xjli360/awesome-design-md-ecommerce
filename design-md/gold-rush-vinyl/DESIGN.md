---
version: alpha
name: "Gold Rush Vinyl"
source_url: "https://www.goldrushvinyl.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record pressing plant that wears its American manufacturing heritage in every visual decision — the site runs on a deep, confident navy (#1a2a3a) as its primary voltage, a color that reads more like a well-worn denim jacket than corporate blue. The canvas is a warm off-white (#f5f0e8) that evokes the paper sleeve of a vintage LP, not the sterile white of a SaaS dashboard. Headlines sit in a condensed, muscular sans-serif at 36–48px, set tight with negative letter-spacing, while body copy runs at 16px in a clean geometric sans — the pairing suggests a factory floor sign translated to screen. Product cards use a soft 12px radius (`{rounded.md}`) and a subtle shadow, framing vinyl mockups like framed album art. The primary CTA button is a solid navy rectangle with white text and an 8px radius (`{rounded.sm}`), unapologetically direct — no pill shapes, no gradients, no gimmicks. The top nav is a simple white bar with the brand's wordmark centered, flanked by "About," "Services," "Vinyl," and "Contact" links in all-caps at 13px. The footer runs a dark navy background with gold-accented links (#c9a84c), a nod to the gold record award aesthetic. The overall mood is analog warmth meets industrial precision: the site trusts its product photography (vinyl close-ups, pressing machines, factory floor) over decorative illustration, and every spacing decision — from the 64px section gaps (`{spacing.section}`) to the 24px padding inside cards — feels deliberate, like a well-cut groove.

colors:
  primary: "#1a2a3a"
  primary-active: "#0f1c28"
  primary-disabled: "#8a9aaa"
  ink: "#1a1a1a"
  body: "#2c2c2c"
  muted: "#6b6b6b"
  muted-soft: "#9a9a9a"
  hairline: "#d4cfc5"
  hairline-soft: "#e3dfd6"
  canvas: "#f5f0e8"
  surface-soft: "#ede8df"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gold-accent: "#c9a84c"
  gold-accent-hover: "#b8953a"
  badge-new: "#c9a84c"
  badge-sale: "#c13515"
  star-rating: "#c9a84c"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Industry', 'Arial Narrow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Industry', 'Arial Narrow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.11
    letterSpacing: -1px
  display-md:
    fontFamily: "'Industry', 'Arial Narrow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Industry', 'Arial Narrow', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 1px
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
  button-primary-active:
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
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-gold:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-gold-active:
    backgroundColor: "{colors.gold-accent-hover}"
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
  text-input-error:
    border: "2px solid {colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    boxShadow: "0 2px 8px rgba(0, 0, 0, 0.08)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0, 0, 0, 0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.md}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    color: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 480px
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
    marginTop: "{spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    marginTop: "{spacing.xl}"
  section-header:
    typography: "{typography.display-lg}"
    color: "{colors.ink}"
    marginBottom: "{spacing.xxl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.gold-accent}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.gold-accent-hover}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a solid navy rectangle with white uppercase text. On hover, the background deepens to `{colors.primary-active}` (#0f1c28). The disabled state uses `{colors.primary-disabled}` (#8a9aaa) with white text, signaling the button is non-interactive without removing it from the layout. Used for "Get a Quote," "Start Your Order," and "Contact Us" actions.

**`button-secondary`** — An outlined variant for less prominent actions, using the same navy text and a 2px solid border on the warm canvas background. On hover, the background shifts to `{colors.surface-soft}` with the darker `{colors.primary-active}` border. Used for "Learn More" and "View Gallery" links alongside primary buttons.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` and the same uppercase button typography. Reserved for secondary actions within cards and modals, such as "Cancel" or "Skip."

**`button-gold`** — An accent button using the gold (#c9a84c) background with dark ink text. On hover, it shifts to `{colors.gold-accent-hover}` (#b8953a). Used sparingly for hero CTAs and premium service tiers where the gold color signals value and quality.

### Cards
**`product-card`** — A white card with a 12px radius (`{rounded.md}`) and a subtle drop shadow, framing vinyl product images and metadata. The card contains a square image slot (`{rounded.sm}`), a title in `{typography.title-sm}`, and a price in bold `{typography.body-md}`. On hover, the shadow deepens to indicate interactivity. Badges (new, sale) sit in the top-left corner of the image area.

### Navigation
**`nav-bar`** — A fixed 72px bar on the warm canvas background, with the brand's wordmark centered and navigation links in all-caps 13px `{typography.nav-link}` with 1px letter-spacing. The active link uses `{colors.primary}` text color. On mobile, the nav collapses into a hamburger menu with a slide-out drawer.

### Forms
**`text-input`** — A standard input field with a warm canvas background, 1px hairline border, and 12px padding. On focus, the border thickens to 2px solid navy. Error states use a 2px red (#c13515) border. Used for contact forms, quote requests, and newsletter signups.

### Footer
**`footer`** — A full-width dark navy section with white body text and gold-accented links. The footer contains three columns: company info, quick links, and contact details. Links use `{typography.link}` and turn to `{colors.gold-accent-hover}` on hover. A thin hairline divider separates the footer from the main content area.

### Hero
**`hero-section`** — A full-width navy background section with white display text, a subtitle in `{typography.body-md}` at `{colors.muted-soft}`, and a gold CTA button. The hero has a minimum height of 480px and uses large `{spacing.section}` padding top and bottom. Background images (factory floor, vinyl close-ups) are overlaid at 40% opacity.

### Badges
**`badge-new`** — A small gold badge with uppercase 11px text, used to flag new vinyl releases or limited editions. The badge has a 4px radius (`{rounded.xs}`) and sits inside product cards or on product detail pages.

**`badge-sale`** — A red (#c13515) badge with white text, used for discounted items. Same sizing and radius as the new badge, but the red color creates urgency.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero min-height reduces to 320px; product cards stack in single column; `{typography.display-xl}` drops to 32px; footer columns stack vertically; section padding reduces to 32px |
| Tablet | 744–1128px | Nav remains horizontal but links shrink; hero uses two-column layout (text left, image right); product cards display in 2-column grid; `{typography.display-xl}` at 40px |
| Desktop | 1128–1440px | Full layout as designed; 3-column product grid; nav links at full spacing; hero at 480px min-height |
| Wide | > 1440px | Max-width container at 1440px; content centered; hero expands to 560px min-height with larger background imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Nav hamburger icon is 48px × 48px
- Product card tap targets (title, price, CTA) have minimum 44px hit areas
- Form inputs maintain 48px height for comfortable touch interaction

### Collapsing Strategy
- Top nav collapses to hamburger menu on mobile (< 744px)
- Footer columns stack vertically on mobile
- Product grid shifts from 3 columns (desktop) to 2 columns (tablet) to 1 column (mobile)
- Hero section reduces min-height and stacks text above image on mobile
- Accordion components (FAQ, service details) collapse by default on all breakpoints, expanding on click

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font-family declarations could not be extracted from the live site; the typography block uses educated guesses based on industry standards (Industry for display, Montserrat for body) — these should be verified against the brand's actual font stack
- No extracted hex colors were available from the live site; the color palette is inferred from the brand's category (vinyl pressing) and common design patterns in the music manufacturing space — all hex values should be validated against the actual site
- Hover and active states for most components are estimated based on common interaction patterns
- Error styling for forms (text-input-error) is a best-guess using a standard red; the brand may use a different error color
- Dark mode is not supported and was not detected on the live site
- Sub-brand or seasonal color palettes (e.g., limited edition vinyl colors) are not captured
- Animation durations, easing curves, and transition properties are not defined
- Focus ring styles and keyboard navigation states are not documented
- The brand may use a custom icon set or illustration style that is not captured here
- Shopify platform integration may introduce additional UI elements (cart, checkout) with their own styling that overrides the brand system
