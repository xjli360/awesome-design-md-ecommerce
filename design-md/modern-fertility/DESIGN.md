---
version: alpha
name: "Modern Fertility"
source_url: "https://modernfertility.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clinical-yet-warm reproductive health brand that uses a single, saturated accent — a deep teal-cyan (#1990c6) — to signal trust and precision across an otherwise stark white-and-charcoal canvas. The site reads like a well-designed medical dashboard: Source Sans Pro at 400 weight for body copy, with headings rarely exceeding 600 weight, giving the interface a calm, evidence-based authority rather than a pushy direct-to-consumer energy. That teal accent appears on every primary CTA button, every active nav link, and every progress indicator in the quiz flow — it's the brand's only color voltage, and it's used sparingly enough that it never feels promotional. Cards and containers use soft 8px rounding (`{rounded.sm}`), while pill-shaped buttons (`{rounded.full}`) and the search bar create a friendly entry point. The fertility-test quiz — the brand's core conversion tool — uses a multi-step form with a thin progress bar, large radio-button cards, and generous 48px section spacing (`{spacing.section}`) that gives each question room to breathe. There is no pink, no pastel, no stereotypical "women's health" palette; the design deliberately avoids gendered visual cues in favor of a clean, unisex clinical interface. Footer links are small (13px), muted, and organized in dense columns, while the top nav stays minimal — logo left, thin nav links right, no mega-menu. The overall mood is that of a thoughtful health service that happens to sell directly to consumers: trustworthy, uncluttered, and built around a single teal thread that guides the eye from headline to CTA.

colors:
  primary: "#1990c6"
  primary-active: "#1478a8"
  primary-disabled: "#a0d4eb"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d0d0d0"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  quiz-progress: "#1990c6"
  quiz-progress-track: "#e0e0e0"
  error: "#c13515"
  success: "#2e7d32"
  badge-new: "#1990c6"
  badge-sale: "#c13515"

typography:
  display-xl:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-lg:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  quiz-question:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  quiz-option:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  logo:
    height: 28px
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-lg}"
    textColor: "{colors.body}"
  quiz-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.quiz-option}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    height: 56px
    border: "1px solid {colors.hairline}"
  quiz-card-selected:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.surface-soft}"
  quiz-card-disabled:
    opacity: 0.5
  quiz-progress-bar:
    backgroundColor: "{colors.quiz-progress-track}"
    height: 4px
    rounded: "{rounded.full}"
  quiz-progress-fill:
    backgroundColor: "{colors.quiz-progress}"
    height: 4px
    rounded: "{rounded.full}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "1px solid {colors.primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0 0 0"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered as a full teal pill (`{rounded.full}`) with white text. Used for "Start the Quiz", "Order Your Kit", and "Subscribe" actions. On hover, shifts to `{colors.primary-active}` (#1478a8). Disabled state uses `{colors.primary-disabled}` (#a0d4eb) with reduced opacity. The pill shape is deliberate — it softens the clinical feel of the teal and makes the action feel approachable.
**`button-secondary`** — An outlined variant with a white fill and teal border, used for "Learn More" and "Compare Kits" actions. Active state deepens the border to `{colors.primary-active}`. This button sits alongside the primary on hero sections and product pages, offering a secondary path without competing for visual weight.
**`button-tertiary-text`** — A text-only link styled as a button, used for "View Details" and "See All" links within cards and sections. No background or border, just teal text that underlines on hover. Keeps the interface clean while maintaining the brand's teal thread.

### Cards
**`quiz-card`** — A selectable option card used in the multi-step fertility quiz. White background with a 1px hairline border, soft 8px rounding, and 56px height. Selected state swaps to a 2px teal border with a light teal-tinted background (`{colors.surface-soft}`). Each card contains a radio-button indicator (hidden on desktop, visible on mobile) and the option text. Disabled cards drop to 50% opacity. The generous height and padding make the quiz feel less like a form and more like a conversation.
**`product-card`** — A compact card for displaying fertility test kits and related products. White background, soft border, 8px rounding, and 16px padding. Contains a product image (with 4px rounding), title in `{typography.title-sm}`, price in bold body text, and optional badge overlays. Cards are arranged in a 3-column grid on desktop, collapsing to 2 on tablet and 1 on mobile.

### Navigation
**`top-nav`** — A minimal 64px header with the Modern Fertility logo (28px height) on the left and a set of uppercase nav links on the right. Links use `{typography.nav-link}` — 14px, 600 weight, 0.3px letter spacing — in muted gray, with the active page highlighted in teal. The nav has a thin bottom border (`{colors.hairline-soft}`). On mobile, the nav links collapse into a hamburger menu with a slide-out drawer. No mega-menu, no dropdowns — the brand keeps navigation deliberately simple.
**`footer`** — A dense, information-rich footer on a soft gray background (`{colors.surface-soft}`). Contains 4-5 columns of links (About, Tests, Support, Resources, Legal) with small 13px caption text. Column headings use `{typography.title-sm}` in ink. Links are muted gray and turn teal on hover. The footer also includes a newsletter signup form (a pill-shaped email input with a teal submit button) and social media icons. Padding is generous at 64px top and bottom.

### Forms
**`text-input`** — Standard text input for name, email, and address fields. White background, 48px height, 8px rounding, and a 1px hairline border. Active state swaps the border to teal. Error state uses `{colors.error}` (#c13515) for the border and shows an inline error message below. Disabled inputs get a soft gray background and muted text. The 16px padding and 16px font size ensure readability on all devices.
**`select-input`** — A styled dropdown for state, month, and year selections. Same dimensions and styling as `text-input`, with a custom chevron icon in teal. The dropdown menu itself uses white background with 8px rounding and a subtle shadow.
**`textarea`** — A multi-line text input for "Additional Notes" or "Message" fields. Same styling as `text-input` but with a minimum height of 120px and no fixed height. Used sparingly — most forms on the site are short and focused.

### Quiz Flow
**`quiz-progress-bar`** — A thin 4px progress indicator at the top of the multi-step quiz. The track is light gray (`{colors.quiz-progress-track}`), and the fill is teal (`{colors.quiz-progress}`). Both ends are fully rounded. The progress bar animates smoothly between steps, giving users a clear sense of how far they've come and how many questions remain.
**`quiz-card`** — (See Cards section above.) The quiz uses these cards for multiple-choice questions, with one card per option. Questions are displayed in `{typography.quiz-question}` (22px, 600 weight) above the cards. The layout is centered with a max-width of 600px, creating a focused, distraction-free experience.

### Badges
**`badge`** — A small teal pill badge used for "NEW", "Best Seller", and "FDA-Reviewed" labels. 11px uppercase text with 0.5px letter spacing, 4px rounding, and 2px vertical padding. Sale badges use `{colors.badge-sale}` (#c13515) instead of teal. Badges sit in the top-left corner of product cards and hero images, adding urgency or authority without cluttering the design.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top nav collapses to hamburger; quiz cards stack vertically; product cards go 1-per-row; hero padding reduces to 32px; footer columns stack to single column; font sizes reduce by 2-4px |
| Tablet | 744–1128px | Two-column product grid; quiz cards in 2-column layout; top nav remains expanded; hero padding at 48px; footer in 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full top nav; quiz centered at 600px max-width; hero at 1128px max-width; footer in 4-column grid |
| Wide | > 1440px | Content max-width at 1440px with centered layout; hero and sections use full width with inner max-width containers; larger whitespace margins |

### Touch Targets
- All interactive elements (buttons, inputs, cards) maintain a minimum 44px height for touch accessibility.
- Quiz cards are 56px tall, providing generous tap targets for radio-button selection.
- Nav links on mobile have 48px tap targets in the hamburger drawer.
- Footer links have 40px minimum tap targets.

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px; the drawer slides in from the right with a semi-transparent scrim.
- Product grid collapses from 3 columns to 2 at tablet, to 1 at mobile.
- Quiz card grid collapses from 2 columns to 1 at mobile.
- Footer columns collapse from 4 to 2 at tablet, to 1 at mobile.
- Hero section reduces vertical padding from 64px to 32px at mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors were minimal (only a few hex values from the captcha page); the teal (#1990c6) was identified as the most distinctive accent but its exact usage (hover states, disabled states, secondary variants) is inferred from common DTC health brand patterns rather than extracted from the live site.
- Font-family declarations only returned "Source Sans Pro, sans-serif" — no secondary or fallback fonts were detected. The `fontFamily` values in typography use common system fallbacks.
- No meta theme-color was found, so the browser chrome color is unknown.
- The site was behind a captcha during extraction, so full page content (hero, quiz, product cards) could not be scraped. Component descriptions are based on the brand's known design language and common patterns in the fertility-testing DTC space.
- Hover states for all components (except buttons and links) are inferred from standard web patterns.
- Error styling (error messages, validation states) is based on common patterns rather than extracted from the live site.
- Dark mode support is unknown; the palette assumes a light-only interface.
- Sub-brand or campaign-specific palettes (e.g., for seasonal promotions or partnerships) are not captured.
- Animation durations, easing curves, and transition properties are not documented.
- Iconography style (custom illustrations vs. icon library) could not be determined from the captcha page.
- The quiz flow's exact step count, question types, and conditional logic are not captured.
