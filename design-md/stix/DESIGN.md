---
version: alpha
name: "Stix"
source_url: "https://getstix.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Pregnancy tests have lived in sterile white boxes with black clinical type for fifty years — Stix built its entire visual language as a deliberate counter-argument to that experience. The primary voltage is a warm coral (#E8645A), appearing on every CTA button, hero accent wash, and illustrative detail, but the surrounding canvas stays a clean #FFFFFF with faint blush (#FDF0EE) section fills rather than pink-saturated backgrounds, keeping the palette legible rather than precious. Typography runs a geometric sans-serif at modest weights: display text sits at 36–48px in weight 600 rather than heavy 800, trusting whitespace and product photography over typographic muscle. Body copy steps cleanly to 16px/400 weight, giving clinical instruction copy the same breathing room as lifestyle editorial — the two register the same, which is the point. Rounded corners sit at `{rounded.full}` on all primary buttons and pill badges, and `{rounded.lg}` on product cards, quiz containers, and plan selectors, producing a vocabulary that reads reassuring rather than sharp. The navigation holds slim and white at 64px, collapsing cleanly to a hamburger on mobile without sacrificing the logo or cart icon. Product photography leans into warm neutral backgrounds — cream, soft white — with packaging centered and given generous padding, so the coral accent colors land with presence rather than competing against loud backdrops. Section-level spacing runs at `{spacing.section}` (64px) on desktop; mobile condenses to `{spacing.xxl}` (48px) without crowding. A quiz-driven product-recommendation flow is a signature interaction pattern: stepped cards with a progress bar in coral, full-width answer tiles that highlight with a 2px coral border on selection, and a result page that resolves to the correct test kit. The effect is a women's health brand that reads closer to a modern wellness startup than a pharmacy shelf — the coral signals energy and approachability, the white canvas signals clarity, and the pill-shaped vocabulary signals that this was designed by people who have actually taken a pregnancy test at 6 a.m. and wanted to feel less alone.

colors:
  primary: "#E8645A"
  primary-active: "#C94B41"
  primary-disabled: "#F5C5C1"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#717171"
  hairline: "#E5DCDB"
  canvas: "#FFFFFF"
  surface-soft: "#FDF0EE"
  surface-card: "#FFFFFF"
  surface-blush: "#FDF5F4"
  on-primary: "#FFFFFF"
  coral-light: "#FAD4CF"
  success: "#4CAF7D"
  success-soft: "#E8F5EE"
  error: "#D93025"

typography:
  display-xl:
    fontFamily: "var(--font-heading, 'DM Sans', 'Inter', system-ui, -apple-system, sans-serif)"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "var(--font-heading, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "var(--font-heading, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "var(--font-heading, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "var(--font-heading, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "var(--font-heading, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "var(--font-body, 'DM Sans', 'Inter', system-ui, -apple-system, sans-serif)"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "var(--font-body, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "var(--font-body, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "var(--font-body, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0.2px
  button-md:
    fontFamily: "var(--font-body, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "var(--font-body, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "var(--font-body, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "var(--font-body, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "var(--font-heading, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  label:
    fontFamily: "var(--font-body, 'DM Sans', 'Inter', system-ui, sans-serif)"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
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
    padding: 14px 28px
    height: 50px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 50px
    states:
      hover:
        backgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    padding: 12px 26px
    height: 50px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1.5px solid {colors.hairline}"
    padding: 12px 16px
    height: 52px
    placeholderColor: "{colors.muted}"
    states:
      focus:
        border: "1.5px solid {colors.primary}"
        outline: "3px solid {colors.coral-light}"
      error:
        border: "1.5px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 32px
    stickyAfterScroll: 80px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.md}"
    shadow: "0 2px 12px rgba(0,0,0,0.06)"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    badgeBackgroundColor: "{colors.surface-soft}"
    badgeTextColor: "{colors.primary}"
    badgeTypography: "{typography.badge}"
    badgeRounded: "{rounded.full}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xl}"
    layout: "split 50/50 image-right on desktop, image-above-text stack on mobile"
    imageRounded: "{rounded.lg}"
  quiz-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    border: "1.5px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
    shadow: "0 4px 20px rgba(0,0,0,0.08)"
    questionTypography: "{typography.display-sm}"
    optionTypography: "{typography.body-md}"
    optionBackgroundDefault: "{colors.canvas}"
    optionBackgroundSelected: "{colors.surface-soft}"
    optionBorderSelected: "2px solid {colors.primary}"
    optionRounded: "{rounded.md}"
    progressBarColor: "{colors.primary}"
    progressTrackColor: "{colors.hairline}"
    progressBarHeight: 4px
    progressBarRounded: "{rounded.full}"
  test-result-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1.5px solid {colors.coral-light}"
  subscription-plan-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    border: "1.5px solid {colors.hairline}"
    padding: "{spacing.xl}"
    selectedBorder: "2px solid {colors.primary}"
    selectedBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    featureListTypography: "{typography.body-sm}"
    savingsBadgeBackgroundColor: "{colors.primary}"
    savingsBadgeTextColor: "{colors.on-primary}"
    savingsBadgeTypography: "{typography.badge}"
    savingsBadgeRounded: "{rounded.full}"
  trust-badge-strip:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    padding: "{spacing.base} 0"
    layout: "horizontal flex, 4 icon+label pairs across on desktop, 2×2 grid on mobile"
  pdp-quantity-selector:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    height: 44px
    stepButtonBackgroundColor: "{colors.canvas}"
    stepButtonRounded: "{rounded.full}"
    stepButtonBorder: "1px solid {colors.hairline}"
  sticky-add-to-cart:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    shadow: "0 -4px 16px rgba(0,0,0,0.06)"
    productLabelTypography: "{typography.caption}"
    priceTypography: "{typography.price}"
    ctaRounded: "{rounded.full}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkHoverColor: "{colors.coral-light}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.label}"
    padding: "{spacing.section} 0"
    dividerColor: "rgba(255,255,255,0.12)"
    legalTypography: "{typography.caption-sm}"
    legalColor: "{colors.muted}"
    emailInputRounded: "{rounded.full}"
    emailSubmitBackgroundColor: "{colors.primary}"
    emailSubmitTextColor: "{colors.on-primary}"

## Components

### Buttons
**`button-primary`** — Fully pill-shaped (`{rounded.full}`, 50px tall) in coral `{colors.primary}` with white text at `{typography.button-md}` (15px/600 weight, 0.2px letter-spacing). This is Stix's dominant CTA, appearing on hero sections, quiz completion screens, and PDP add-to-cart rails. Hover darkens to `{colors.primary-active}`; disabled state fades to `{colors.primary-disabled}` and sets cursor to not-allowed.

**`button-secondary`** — Same `{rounded.full}` pill geometry and 50px height, but white fill with a 2px solid coral border and coral text — used for lower-hierarchy CTAs that share a screen with a primary action. Hover fills with `{colors.surface-soft}` (pale blush) to signal interactivity without competing for attention.

**`button-ghost`** — Transparent fill, `{colors.hairline}` border, ink text. Applied in navigation dropdowns and filter drawers where color would create noise. Height and pill shape are consistent with primary and secondary buttons so layout grids remain stable.

### Text Input
**`text-input`** — 52px tall with `{rounded.md}` (12px) corners and a 1.5px `{colors.hairline}` border. Focus ring is a 3px `{colors.coral-light}` outline rather than a cold blue, keeping the warmth of the brand palette present in interactive states. Error state swaps the border to `{colors.error}`; placeholder text inherits `{colors.muted}` at full `{typography.body-md}` size.

### Navigation
**`nav-bar`** — 64px tall white bar with a 1px `{colors.hairline}` bottom border. Logo sits left at max 32px height; product category links center in `{typography.nav-link}` (14px/500 weight); a compact coral pill CTA anchors the right. The bar is static at page top and becomes sticky after 80px of scroll. On mobile, center links collapse to a hamburger drawer; logo and cart icon remain in the bar.

### Product Card
**`product-card`** — White surface with `{rounded.lg}` (20px) corners and a soft `0 2px 12px rgba(0,0,0,0.06)` shadow. Product image fills a `{rounded.md}` container at top; title (`{typography.title-sm}`), subtitle (`{typography.body-sm}` in `{colors.muted}`), and price (`{typography.price}`) stack below with `{spacing.sm}` gaps. Category pills rendered in `{colors.surface-soft}` with coral text and `{rounded.full}` shape overlay the image top-left. The full card surface is the tap/click target to the PDP.

### Hero Banner
**`hero-banner`** — Split 50/50 layout on desktop: left column holds headline in `{typography.display-xl}`, subhead in `{typography.body-md}` with `{colors.body}` color, and the coral pill CTA; right column holds product or lifestyle photography cropped to `{rounded.lg}`. Background is `{colors.surface-soft}` (blush), not white, providing warmth without letting the coral dominate the fold. On mobile, the image stacks above the text block and scales to full width; the text block receives `{spacing.xl}` horizontal padding.

### Quiz Card
**`quiz-card`** — Stix's guided product-recommendation quiz renders each step as a centered white card with `{rounded.lg}` corners and a `0 4px 20px rgba(0,0,0,0.08)` shadow, floating over a blush page background. The step question uses `{typography.display-sm}`; answer options are full-width tiles with `{rounded.md}` corners and a 1.5px `{colors.hairline}` border that switches to `{colors.surface-soft}` fill and a 2px `{colors.primary}` border on selection. A 4px-tall coral progress bar with `{rounded.full}` ends runs above the card, tracking completion.

### Test Result Badge
**`test-result-badge`** — A compact `{rounded.full}` pill in `{colors.surface-soft}` with coral text and a 1.5px `{colors.coral-light}` border. Applied on PDPs and quiz result pages to label product category (e.g., "Pregnancy Test", "Ovulation Kit"). Typography is `{typography.badge}` (11px/700/uppercase) so it reads clearly at small sizes without dominating.

### Subscription Plan Card
**`subscription-plan-card`** — Two or three plan options render as equal-width cards with `{rounded.lg}` corners. Default state has a 1.5px `{colors.hairline}` border; selected state upgrades to a 2px `{colors.primary}` border with a `{colors.surface-soft}` background fill. The recommended plan carries a savings pill (coral fill, white `{typography.badge}` text, `{rounded.full}`) positioned in the top-right corner. Title uses `{typography.title-md}`, price uses `{typography.price}`, feature list uses `{typography.body-sm}`.

### Trust Badge Strip
**`trust-badge-strip`** — A full-width horizontal band in `{colors.surface-blush}` housing four icon-plus-label trust signals (e.g., "FDA-registered lab," "Ships in 1–2 days," "Free returns," "Clinician-reviewed"). Icons render in `{colors.primary}` at approximately 20px; label text is `{typography.caption}` in `{colors.body}`. On mobile the four items collapse to a 2×2 grid with center alignment.

### PDP Quantity Selector
**`pdp-quantity-selector`** — A 44px-tall `{rounded.full}` pill container in `{colors.surface-blush}`. Minus and plus step buttons are small `{rounded.full}` circles in `{colors.canvas}` with a 1px `{colors.hairline}` border, flanking a centered quantity number in `{typography.title-sm}`. The pill echoes the brand's button vocabulary and avoids the boxy stepper pattern common in clinical ecommerce.

### Sticky Add-to-Cart Bar
**`sticky-add-to-cart`** — On PDP scroll past the product hero, a white bar with a 1px `{colors.hairline}` top border and a `0 -4px 16px rgba(0,0,0,0.06)` upward shadow pins to the viewport bottom on mobile. It contains the product name in `{typography.caption}`, price in `{typography.price}`, and a full-width coral `{rounded.full}` CTA button with `{spacing.base}` padding on each side.

### Footer
**`footer`** — Dark `{colors.ink}` background with white body text and `{colors.coral-light}` link hover color, providing contrast without introducing a third hue. Column headings use `{typography.label}` (12px/600/uppercase) in white. An email signup field with `{rounded.full}` geometry and a coral submit button sits in the first column. A hairline divider (`rgba(255,255,255,0.12)`) separates the link columns from a bottom legal strip in `{typography.caption-sm}` with `{colors.muted}` text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks image above text full-bleed; nav collapses to hamburger + logo + cart; product grid 1 column; quiz card full-width; trust strip 2×2 grid; sticky ATC bar visible on PDP |
| Tablet | 744–1128px | 2-column product grid; hero retains split layout at reduced scale; nav links visible and condensed; quiz card centered at 480px max-width |
| Desktop | 1128–1440px | 3-column product grid; full hero split with generous section padding; nav at full 64px with all links; trust strip 4-across |
| Wide | > 1440px | Content max-width capped at ~1280px with auto side margins; hero vertical padding increases to 80px |

### Touch Targets
- All buttons are 50px tall, exceeding the 44px WCAG touch-target minimum
- PDP quantity step buttons are 44px diameter circles
- Nav hamburger icon has a 44×44px minimum tap area
- Product cards use the full card surface as the PDP link tap target
- Footer links have a minimum 44px vertical hit area via padding

### Collapsing Strategy
- Center nav links → full-width hamburger drawer with dark overlay; links stack in `{typography.display-sm}` with `{spacing.lg}` vertical gaps
- Trust badge 4-across → 2×2 grid at tablet breakpoint; vertical list with left-aligned icons on very small viewports
- Hero 50/50 split → image-above-text stack; image goes full-bleed width, text block receives `{spacing.xl}` horizontal padding
- PDP two-column (image gallery + options sidebar) → single column, image carousel first, options and ATC below
- Footer multi-column link grid → single-column stacked sections with `{spacing.lg}` between groups on mobile
- Subscription plan cards → vertical stack (one card per row) on mobile, maintaining full border and selection state

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: The site loads its palette via JavaScript or is behind anti-bot protection — no colors were captured at extraction time. All hex values in this spec are inferred from widely-observed Stix brand presentations and should be verified against the live site or brand design files before production use.
- **No font families extracted**: Exact typeface(s) are unknown. This spec uses `DM Sans` and `Inter` as geometric sans-serif placeholders under CSS custom properties (`--font-heading`, `--font-body`). Stix may use a licensed face such as GT Walsheim, Söhne, or a similar rounded geometric — replace the var stacks once confirmed.
- **Icon and illustration style**: Whether the brand uses line icons, filled icons, or custom hand-drawn illustrations could not be confirmed. Brand context suggests line-style icons at approximately 1.5–2px stroke weight.
- **Motion and easing**: Transition timing and easing curves are not captured. Defaults of `ease-out` at 150–200ms are reasonable for hover and selection states until confirmed.
- **Exact shadow elevation tokens**: Drop-shadow values for cards and the sticky bar are estimated; real elevation tokens may differ.
- **Dark mode**: No evidence of dark mode support at extraction time; spec assumes light-only.
- **Product photography art direction**: Whether the brand uses pure white, off-white cream, or `{colors.surface-soft}` as image backgrounds was not confirmed from extraction.
- **Quiz flow depth and branching logic**: The quiz component spec describes the visual pattern; the actual number of steps, branching conditions, and result-page layout are not documented here.
