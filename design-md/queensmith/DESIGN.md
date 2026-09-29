---
version: alpha
name: "Queensmith"
source_url: "https://www.queensmith.co.uk"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Walking into Queensmith begins with the question, not the object — the site positions the jeweler not as a catalog to browse but as a collaborator, opening on an invitation to design your own engagement ring rather than on a product grid. The near-black ink (#313131) on white canvas is the single confirmed chromatic fact the live site yields (behind its Cloudflare gate), and it reads with unusual precision: no blush-pink lifestyle gradients, no promotional red, no candy-colored hero. The palette operates in the register of a bespoke architect's practice — dark type on white, photography given room without interference.

  A warm champagne gold — presumed here as #c09a50, representative of the fine jewelry category — punctuates call-to-action surfaces and product details with the restraint of precious metal deployed only where it earns its place. Rings surface on a creamy canvas ({colors.surface-soft}), with a fine hairline ({colors.hairline}) separating content panels rather than heavy borders or drop shadows. Type is built from system fonts in this specification (no brand web font was extractable; see Known Gaps), leaning serif at display sizes for the solemnity of the occasion and clean sans-serif at body for consultation-document legibility. Tracking-widened uppercase labels on buttons enforce a formal register without requiring a custom typeface.

  Components resolve into showroom furniture rather than e-commerce fixtures: product cards hold ring photography at a generous aspect ratio with metal type and carat weight in small-caps captions; a ring-configurator module tabs through cut, metal, and stone style on a sharp-cornered ({rounded.none}) tab row; appointment-booking CTAs appear as high-contrast ink bands, signaling that the true purchase journey begins with a studio visit. Pill filter chips ({rounded.full}) let shoppers navigate by stone shape or setting style without leaving the imagery context. Trust credentials — ethical sourcing, London studio provenance, gem certifications — run in a restrained footer tier in {colors.muted} beneath category links.

  Across breakpoints, the side-by-side ring configurator on desktop collapses to a stacked swipeable selector on mobile, where stone photography dominates the viewport and specifications scroll beneath. The net effect is contemporary without coldness: serious about craft, warmly aware of the occasion.

colors:
  primary: "#c09a50"
  primary-active: "#a07e3a"
  primary-disabled: "#e2cfa0"
  ink: "#313131"
  body: "#4a4540"
  muted: "#7a756e"
  muted-soft: "#a09a94"
  hairline: "#e5e0d9"
  hairline-soft: "#f0ece7"
  canvas: "#ffffff"
  surface-soft: "#faf8f5"
  surface-card: "#ffffff"
  surface-dark: "#1e1c1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  gold-light: "#e8d5a8"
  rose-gold: "#c4937a"
  platinum: "#d4d4d4"
  certification-green: "#3a6b52"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.03em
  small-caps-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.04em

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
    rounded: "{rounded.none}"
    padding: "14px 32px"
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "13px 31px"
    height: 48px
    border: "1px solid {colors.ink}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 32px"
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: "12px 16px"
    height: 48px
    placeholderColor: "{colors.muted}"
    errorBorder: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    imageAspectRatio: "4/3"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    metaTypography: "{typography.small-caps-label}"
    metaColor: "{colors.muted}"
  ring-configurator-tab:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    inactiveTextColor: "{colors.body}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "12px 24px"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.small-caps-label}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    activeBorder: "1px solid {colors.ink}"
  appointment-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.none}"
    padding: "48px 64px"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    overlayAlignment: left
    ctaRounded: "{rounded.none}"
    minHeight: 600px
  pdp-image-viewer:
    backgroundColor: "{colors.surface-soft}"
    thumbnailBorder: "1px solid {colors.hairline}"
    activeThumbnailBorder: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    imagePadding: "{spacing.lg}"
  metal-swatch:
    size: 32px
    rounded: "{rounded.full}"
    activeBorder: "2px solid {colors.ink}"
    inactiveBorder: "1px solid {colors.hairline}"
    yellowGold: "{colors.primary}"
    roseGold: "{colors.rose-gold}"
    whiteMetal: "{colors.platinum}"
  stone-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.certification-green}"
    typography: "{typography.small-caps-label}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "4px 10px"
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption}"
    titleTypography: "{typography.title-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "24px 0"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    headingTypography: "{typography.small-caps-label}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "48px 0 32px"

---

## Components

### Buttons

**`button-primary`** — Gold-fill rectangle with zero border-radius, tracking-widened all-caps label in `{typography.button-md}`. The sharp-cornered shape reads as precision over friendliness; hover transitions to `{colors.primary-active}` over 150ms ease. Disabled state uses `{colors.primary-disabled}` with the white label preserved. Appears on product pages ("Add to Wishlist", "Start Designing") and the appointment-booking flow.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, same all-caps tracking as the primary. Sits alongside `button-primary` in side-by-side CTA pairs ("Design Your Ring" / "Book a Consultation"), maintaining visual parity without color competition.

**`button-dark`** — Ink-fill rectangle with white label at full 48px height. Reserved for CTAs that appear on the `{colors.surface-soft}` hero background or inside the `appointment-banner` dark band, creating direct light/dark contrast rather than relying on the gold accent.

**`button-ghost`** — Transparent background with underlined `{colors.ink}` text. Used for tertiary in-context actions: "Learn more about the 4Cs", "Compare settings", or editorial inline links that must not compete with primary CTAs.

### Inputs

**`text-input`** — No border-radius, consistent with the brand's straight-cornered philosophy. A 1px `{colors.hairline}` border transitions to 1px `{colors.ink}` on focus, with no color flash or shadow — the focus state is purely a border darkening. Placeholder text in `{colors.muted}`. Error state adds `{colors.error}` border. Used across appointment booking, ring-builder finger-size entry, and newsletter signup.

### Navigation

**`nav-bar`** — 64px white canvas bar with a 1px `{colors.hairline}` bottom border. Logo renders in `{colors.ink}`. Links use `{typography.nav-link}` at regular weight; on mobile, secondary categories collapse behind a hamburger trigger. A persistent "Book a Consultation" link may resolve to `button-dark` styling, anchoring the conversion intent in every context.

### Product Display

**`product-card`** — Borderless card on `{colors.surface-soft}` background; ring photography at 4:3 aspect ratio with no additional frame or shadow. Below the image: ring name in `{typography.title-md}`, metal type and stone spec in `{typography.small-caps-label}` / `{colors.muted}`, price in `{typography.price-display}`. No border-radius on the card container. On hover, a subtle background lift to `{colors.hairline-soft}` signals interactivity without disrupting the grid calm.

**`pdp-image-viewer`** — Product detail page gallery: large primary image on `{colors.surface-soft}` with a horizontal thumbnail strip beneath. Active thumbnail carries a 1px `{colors.ink}` border; inactive thumbnails carry `{colors.hairline}`. No rounded corners. Where a 360° or try-on view is present, it triggers from within the same frame rather than opening a separate modal.

**`metal-swatch`** — 32px circle (`{rounded.full}`) representing metal finish: yellow gold (`{colors.primary}`), rose gold (`{colors.rose-gold}`), white gold/platinum (`{colors.platinum}`). Active swatch carries a 2px `{colors.ink}` outer ring with a 2px white gap; inactive carries a 1px `{colors.hairline}`. Minimum touch target 44px via transparent outer padding.

### Ring Configuration

**`ring-configurator-tab`** — Horizontal tab row without border-radius. Active tab fills with `{colors.ink}`, label in `{colors.on-dark}`; inactive tabs sit on white with `{colors.body}` text. Tabs span: Cut, Stone, Metal, Setting Style. On desktop the component occupies the left column of a side-by-side layout (tabs + options left, ring preview right); on mobile it stacks above the preview image and the options list scrolls vertically.

**`filter-chip`** — Pill-shaped (`{rounded.full}`) chip with `{typography.small-caps-label}` label. Default state: `{colors.surface-soft}` fill, `{colors.hairline}` border. Active state: `{colors.ink}` fill, `{colors.on-dark}` text. Used above product grids to filter by stone shape (round, emerald, pear, oval, cushion) or setting style (solitaire, pavé, halo). On mobile, the chip row becomes horizontally scrollable rather than wrapping.

### Conversion

**`appointment-banner`** — Full-width dark band (`{colors.ink}` background) with a large serif headline in `{typography.display-sm}` and a single body sentence in `{typography.body-md}` / `{colors.on-dark}`. A `button-primary` CTA labeled "Book Your Appointment" sits immediately below. Vertical padding is 48px — the generous whitespace makes the module read as a formal invitation rather than a promotional strip. Appears at mid-page on the homepage and at the base of collection pages.

### Trust and Provenance

**`stone-badge`** — Small sharp-cornered badge in `{typography.small-caps-label}` with a 1px `{colors.hairline}` border. Certification labels: "GIA Certified", "Conflict-Free", "Ethically Sourced". Accent tinted with `{colors.certification-green}` for the icon or leading dot. Sits beneath stone specification details on PDPs and in the ring configurator detail panel.

**`trust-bar`** — A light horizontal band (`{colors.surface-soft}`, `{colors.hairline}` top border) with three to four equal columns of icon + heading + body-copy. Icons tinted `{colors.primary}`; headings in `{typography.title-sm}` / `{colors.ink}`; body in `{typography.caption}` / `{colors.muted}`. Topics: ethical sourcing, Hatton Garden studio, lifetime warranty, complimentary resizing. Padding 24px vertical, sits between the main content and the footer.

### Footer

**`footer`** — White canvas footer, 1px `{colors.hairline}` top border. Column headings in `{typography.small-caps-label}` / `{colors.ink}`. Links in `{typography.body-sm}` / `{colors.body}`, darkening to `{colors.ink}` on hover. Social icons and fine print in `{colors.muted}`. A "Book a Consultation" CTA may repeat in a narrow ink or gold band immediately above the link columns, extending the conversion emphasis through the bottom of the page.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger. Ring configurator tabs stack vertically above swipeable preview. Product cards 1-per-row. Appointment banner text centers, padding reduces to 32px. Hero crops portrait; headline overlays bottom third. Filter chips horizontally scroll. |
| Tablet | 744–1128px | Two-column product grid. Ring configurator shows tab row above full-width preview. Nav retains primary links; secondary links collapse to a "More" trigger. Trust bar becomes 2×2 grid. |
| Desktop | 1128–1440px | Side-by-side ring configurator (options left, ring preview right). Three- to four-column product grid. Full nav with all primary categories visible. Appointment banner expands to full prose layout. |
| Wide | > 1440px | Max-width container (~1280px) centered on canvas. Trust bar expands to four equal columns. Hero fills remaining canvas width beside a constrained text column. |

### Touch Targets
- All buttons minimum 48px height
- Filter chips minimum 44px touch area via transparent vertical padding extension
- Metal swatches 32px visual, 44px touch target via transparent outer ring
- Nav hamburger trigger 44×44px minimum
- Thumbnail strip items minimum 56px height on mobile
- Stone badge and stone-type swatches in configurator minimum 44px tap zone

### Collapsing Strategy
- Ring configurator collapses from side-by-side (options | preview) to stacked (preview above, options below) below 744px
- Filter chip row switches from wrapping flex to single-row horizontal scroll below 744px; no wrapping
- Price display (`{typography.price-display}`) scales from 28px to 22px on mobile via a utility class, not a separate token
- Appointment banner padding reduces from 48px to 32px vertical; headline drops from `{typography.display-sm}` to `{typography.title-md}` sizing at 24px on mobile
- Footer link columns collapse to accordion sections on mobile with `{colors.ink}` chevrons
- PDPimage viewer switches from horizontal thumbnail strip to dot-indicator carousel on mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Palette is critically sparse** — only `#313131` was extracted; the live site was behind Cloudflare anti-bot protection ("Just a moment..."). All other color values — champagne gold primary, surface tones, hairline, muted grays, certification green — are category-inferred defaults, not live extraction. Verify the actual primary CTA color, surface palette, and any accent or hover states before production use.
- **No brand web font detected** — font-family stacks returned entirely OS system fonts with no web font loaded server-side. Queensmith almost certainly uses a licensed or custom typeface (likely a serif for display headings given the category register). Inspect Network → Fonts in DevTools on the live site with anti-bot bypass or a residential IP.
- **Primary color is speculative** — `#c09a50` (warm champagne gold) is a representative default for the fine jewelry category, not an extraction artifact. The actual primary could be a different gold register, rose gold, a muted platinum tone, or even the ink color (#313131) used directly as the primary CTA fill.
- **Border-radius decisions are inferred** — `{rounded.none}` throughout is based on the brand register of a bespoke London jeweler; the actual site may use a small radius (xs/sm) on cards or inputs. Measure from live screenshots.
- **No meta theme-color** — mobile chrome bar treatment is unknown.
- **Ring configurator interaction model unverified** — step structure, 3D ring preview capability, stone filtering logic, and animation timing have not been observed on the live site.
- **Ethical sourcing / certification badge copy** — specific badge labels ("GIA Certified", "Conflict-Free") are category-typical placeholders; verify exact copy and icon treatments from the live PDP.
