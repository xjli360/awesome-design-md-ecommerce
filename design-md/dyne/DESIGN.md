---
version: alpha
name: "DYNE"
source_url: "https://www.dyne.jewelry"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every surface on dyne.jewelry performs a kind of deliberate restraint — the brand's signature move is reduction: fewer stones, cleaner settings, sightlines left open so the ring becomes its own punctuation. The name itself echoes a physics unit of force, and that precision reads through into the design language. A warm near-white canvas (inferred as approximately #faf9f7) holds inventory imagery at full bleed with almost no competing UI chrome. The primary call-to-action surfaces in a burnished champagne-gold — not the saturated yellow-gold of legacy retailers, but a muted, desaturated bronze that reads closer to aged 18k than to jewelry-store yellow, suggesting the brand skews toward customers who find the Tiffany-blue-and-bold-red vocabulary overly loud. Display type is almost certainly a narrow optical serif in the tradition of Cormorant or Playfair — large, generous leading, minimal letter-spacing — letting ring names breathe as editorial headlines rather than product titles. Body copy falls to a geometric sans-serif at 15–16px, a pairing common in the contemporary fine-jewelry DTC tier where editorial gravitas at large sizes gives way to legibility utility at small ones. Corner radii are near-zero on buttons and cards; nothing competes with the organic geometry of a cut stone. The product-card silhouette is deliberately spare: a cream or white field, a single centered ring photograph, name and price in opposing weights (serif display vs. light sans), an understated "View Ring" or "Reserve" CTA that doesn't shout. Stone selectors — round, oval, emerald, pear — present as tight pill toggles, their active state in the muted gold primary rather than a generic blue. A "Book a Consultation" persistent element reflects the high-touch, assisted-sale reality of the engagement ring category. **All color and typography values in this file are inferred from category conventions; the live site returned no extractable tokens and must be verified against the actual source.**

colors:
  primary: "#b8935a"
  primary-active: "#9a7a48"
  primary-disabled: "#dfc99e"
  ink: "#1a1918"
  body: "#3d3a36"
  muted: "#7a7570"
  hairline: "#e8e4de"
  hairline-soft: "#f0ede9"
  canvas: "#faf9f7"
  surface-soft: "#f5f2ee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  champagne: "#f0e6d3"
  metal-warm: "#d4a96a"
  stone-accent: "#e8dfd4"
  scrim: "#1a1918"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.04em
  body-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
    textTransform: uppercase
  price:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.08em
  stone-label:
    fontFamily: "'DM Sans', 'Inter', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.05em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
  section-lg: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
  consultation-cta:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoStyle: "wordmark-serif"
    position: sticky
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "4/5"
    imageFit: cover
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    nameTypography: "{typography.display-sm}"
    priceTypography: "{typography.price}"
    subtitleTypography: "{typography.body-sm}"
    ctaTypography: "{typography.button-sm}"
    gap: "{spacing.sm}"
    hoverEffect: "image scale 1.03 over 400ms ease"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    layout: "centered-overlay"
    imageStyle: "full-bleed, high-contrast stone photography"
    ctaStack: "vertical, {spacing.sm} gap"
    paddingVertical: "{spacing.section-lg}"
  stone-selector:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.muted}"
    typography: "{typography.stone-label}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    gap: "{spacing.xs}"
    options:
      - Round
      - Oval
      - Emerald
      - Pear
      - Cushion
      - Radiant
  metal-selector:
    backgroundColor: "transparent"
    activeOutline: "2px solid {colors.primary}"
    inactiveOutline: "1px solid {colors.hairline}"
    swatchSize: 24px
    rounded: "{rounded.full}"
    gap: "{spacing.xs}"
    metals:
      - label: "18k Yellow Gold"
        swatch: "#d4a96a"
      - label: "18k White Gold"
        swatch: "#e8e8e8"
      - label: "Platinum"
        swatch: "#c8c8d4"
      - label: "18k Rose Gold"
        swatch: "#e8b59a"
  carat-slider:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    thumbColor: "{colors.canvas}"
    thumbBorder: "2px solid {colors.primary}"
    thumbSize: 20px
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"
  ring-detail-panel:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.xl}"
    nameTypography: "{typography.display-md}"
    priceTypography: "{typography.price}"
    descriptionTypography: "{typography.body-md}"
    dividerColor: "{colors.hairline}"
    sectionGap: "{spacing.lg}"
    specLabelTypography: "{typography.caption}"
    specValueTypography: "{typography.body-sm}"
  consultation-banner:
    backgroundColor: "{colors.champagne}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.xxl} {spacing.section}"
    layout: "two-column: text left, illustration right"
  education-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    iconStyle: "thin-line, 24px, {colors.primary}"
    columns: 3
    padding: "{spacing.section} {spacing.xxl}"
    topics:
      - "The 4 Cs"
      - "Ring Sizing"
      - "Setting Styles"
  testimonial-block:
    backgroundColor: "{colors.canvas}"
    quoteTypography: "{typography.display-sm}"
    attributionTypography: "{typography.caption}"
    quoteMarkColor: "{colors.metal-warm}"
    quoteMarkSize: 80px
    layout: "centered single-quote with flanking rule lines"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.stone-accent}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption}"
    dividerColor: "#2e2c29"
    padding: "{spacing.section} 0"
    columns: 4

## Components

### Buttons

**`button-primary`** — Zero-radius rectangular block in muted champagne-gold (`{colors.primary}`), all-caps spaced tracking via `{typography.button-md}`. The deliberate absence of a border-radius signals precision over friendliness; on hover the background deepens to `{colors.primary-active}` with a 200ms ease transition. Disabled state washes out to `{colors.primary-disabled}` without changing shape.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` outline, same dimensions as primary (48px height, 32px horizontal padding). Intended for secondary ring-configuration actions like "Save to Wishlist" or "Compare." On hover, fill bleeds in as a very light `{colors.surface-soft}` wash.

**`consultation-cta`** — The "Book a Consultation" trigger rendered in `{colors.ink}` black fill with `{colors.canvas}` text, distinguishing it from the gold product CTAs. Often appears as a persistent floating element on mobile or as a full-width bar at the bottom of the ring detail page.

**`button-ghost`** — Text-only with underline, `{colors.muted}` color, `{typography.button-sm}` scale. Used for tertiary actions: "View Size Guide," "Compare Settings," "Learn About Certification."

### Stone & Metal Selectors

**`stone-selector`** — Pill-shaped toggle group (`{rounded.full}`) presenting cut options: Round, Oval, Emerald, Pear, Cushion, Radiant. Inactive pills sit in `{colors.surface-soft}` with `{colors.muted}` text; the active pill fills with `{colors.primary}` gold. The tight pill cluster aligns horizontally on desktop and wraps to two rows on mobile. Labels use `{typography.stone-label}` — 11px spaced uppercase to keep the selector visually subordinate to the ring name.

**`metal-selector`** — Circular color swatches (24px, `{rounded.full}`) with a 2px `{colors.primary}` outline ring on the active metal and a subtle 1px `{colors.hairline}` border on inactive. Swatches correspond to 18k Yellow Gold (#d4a96a), White Gold (#e8e8e8), Platinum (#c8c8d4), Rose Gold (#e8b59a). A text label below the swatch cluster updates to the selected metal name in `{typography.stone-label}`.

**`carat-slider`** — A clean horizontal slider with `{colors.primary}` fill track and a `{colors.canvas}` thumb outlined in `{colors.primary}`. Current carat value floats above the thumb in `{typography.caption}`. Min/max labels sit at track ends.

### Navigation

**`nav-bar`** — Sticky, 72px tall, `{colors.canvas}` background with a 1px `{colors.hairline}` bottom border that appears on scroll. Logo is a wordmark in the serif display face at roughly 20px. Nav links at `{typography.nav-link}` — 13px, wide tracking — read as quiet; the only emphasized element is the "Book a Consultation" ghost-button in the far right. A centered layout on desktop; on mobile collapses to hamburger + logo + bag icon.

### Product Card

**`product-card`** — No border-radius anywhere. A 4:5 ring image occupies the full card width; on hover the image scales to 1.03 over 400ms. Below the image: ring name in `{typography.display-sm}` (Cormorant, 22px light), starting price in `{typography.price}` (Cormorant, 20px), a one-line descriptor in `{typography.body-sm}`. No visible "Add to cart" button on the card face — the entire card is a navigate-to-PDP link, reinforcing the considered-purchase positioning.

### Hero

**`hero`** — Full-bleed stone or ring photography behind centered editorial text. Headline at `{typography.display-xl}` (Cormorant, 52px, weight 300) with extremely open leading. A subhead in `{typography.body-md}` at 300 weight follows, then two vertically stacked CTAs: `consultation-cta` above, `button-secondary` below. No gradient overlay — brand relies on high-contrast photography that reads clearly with white text at center.

### Ring Detail Panel

**`ring-detail-panel`** — The right-hand column on PDP. Ring name at `{typography.display-md}`, starting price in `{typography.price}`, then a horizontal `{colors.hairline}` rule. Stone selector, metal selector, and carat slider stack vertically with `{spacing.lg}` between groups. Spec table (Setting Type, Metal, Stone Origin, Certification) uses `{typography.caption}` for labels and `{typography.body-sm}` for values. Primary and consultation CTAs appear full-width at the bottom of the panel.

### Consultation Banner

**`consultation-banner`** — A two-column module on a `{colors.champagne}` field. Left: headline at `{typography.display-sm}` + a sentence of body copy + the `consultation-cta` button. Right: a thin-line ring illustration or lifestyle photograph. Appears on homepage below the ring grid and at the base of collection pages. Padding is generous (`{spacing.xxl}` vertical) to give the invitation room to breathe.

### Education Strip

**`education-strip`** — Three-column grid on `{colors.surface-soft}`. Each column: a 24px thin-line icon in `{colors.primary}`, a heading in `{typography.title-md}`, two lines of body in `{typography.body-sm}`. Topics: The 4 Cs, Ring Sizing, Setting Styles. Collapses to a horizontally scrollable carousel on mobile.

### Testimonial Block

**`testimonial-block`** — Centered single-quote layout on `{colors.canvas}`. An oversized quotation mark (80px, `{colors.metal-warm}`) precedes the quote text at `{typography.display-sm}`. Attribution — customer name and occasion — in `{typography.caption}` below. Flanked by thin horizontal rules extending to the column margins. No star ratings visible; the brand communicates quality through editorial voice rather than aggregate scores.

### Footer

**`footer`** — `{colors.ink}` fill, 4-column grid. Column heads in `{typography.caption}` (all-caps, `{colors.stone-accent}`), links in `{typography.body-sm}` at `{colors.canvas}`. A thin `#2e2c29` divider separates the link columns from a bottom bar containing legal copy and payment icons. The overall effect is a dark, editorial close — matching the hushed confidence of the product pages above.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column ring grid; nav collapses to hamburger + wordmark + bag; hero headline drops to ~32px; ring-detail-panel becomes full-width below the image; stone/metal selectors scroll horizontally; education strip becomes horizontal carousel; consultation-banner stacks vertically |
| Tablet | 744–1128px | Two-column ring grid; nav shows abbreviated links; hero at ~42px display; ring-detail-panel remains stacked below image; education strip shows 3 columns in tighter layout |
| Desktop | 1128–1440px | Three-column ring grid; full sticky nav with all links visible; PDP shifts to 50/50 image + panel split; hero at full 52px display-xl; consultation-banner at two-column |
| Wide | > 1440px | Ring grid expands to 4 columns; hero image extends edge-to-edge with max-width text container at ~1200px; side margins increase proportionally; section padding increases to `{spacing.section-lg}` |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Stone selector pills expand padding to ensure 44px touch height
- Metal swatches rendered at 36px on mobile (up from 24px on desktop)
- "Book a Consultation" sticky bar on mobile is 56px tall for easy thumb access
- Carat slider thumb expands to 28px touch area on mobile

### Collapsing Strategy

- Navigation collapses to icon-only bar (hamburger, logo wordmark, bag) at < 744px; no mega-menu, single-level drawer
- Ring grid: 4-col → 3-col (1128px) → 2-col (744px) → 1-col (< 744px)
- Education strip: 3-column grid → horizontal scroll carousel at < 744px (one card visible, peek of second)
- Consultation banner: side-by-side → stacked (image above text) at < 744px
- PDP layout: side-by-side 50/50 → image full-width stacked above detail panel at < 1128px
- Footer: 4-col → 2-col → single accordion at < 744px

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the live site returned zero color tokens; all palette values in this file are inferred from fine-jewelry DTC category conventions and must be validated against the actual brand stylesheet before use in production
- **No font families extracted** — Cormorant Garamond / DM Sans pairing is a category-common inference; DYNE may use a licensed or custom typeface not detectable via standard CSS extraction
- **No meta theme-color** — mobile browser chrome color unknown; defaulting to `{colors.canvas}` assumption
- **Platform unclear** — site is not confirmed Shopify; component architecture and available customization surface (theme vs. headless) is unknown
- **Primary color confidence is low** — the champagne-gold (#b8935a) is a plausible inference for a modern engagement ring brand but has not been confirmed against the actual logo or CTA color; could be a near-black or deep navy instead
- **Ring configurator depth unknown** — whether DYNE supports a 3D ring builder, photo-based previews, or stone-upload is not determinable without live site access
- **Animation and transition tokens absent** — hover, focus, and page-transition behaviors are inferred from category norms; actual durations and easing curves unconfirmed
- **Consultation booking flow** — whether this is an embedded calendar widget (Calendly, etc.), a bespoke form, or a phone-first CTA is unknown and affects the consultation-cta component's link behavior
