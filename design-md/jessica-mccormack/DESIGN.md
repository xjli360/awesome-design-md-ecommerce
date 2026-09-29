---
version: alpha
name: "Jessica McCormack"
source_url: "https://www.jessicamccormack.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Monospaced type on diamond rings — ABC Diatype Mono carries every product label, navigation link, and price point in letterforms borrowed from technical instruments and typewriter ribbons rather than the hand-engraved cartouches of a traditional Mayfair jeweller. The tension between that utilitarian grid typeface and the extraordinary one-of-a-kind Georgian and Victorian pieces being sold is the entire brand proposition compressed to one font choice. Bellefair Regular — an old-style serif with humanist warmth in its terminal strokes — takes the editorial headline role, offering the collector-register counterpart to Diatype Mono's ledger tone.

  The palette is almost entirely suppressed. A near-black (#121212) provides ink and the main CTA body; five grays from #9ca3af through #dedede build the hairline, muted, and surface layers without ever introducing warmth or saturation. A single pure red (#ff0000) breaks the chromatic restraint — appearing on sale flags, error states, and active navigation markers with the sudden clarity of a red wax seal pressed onto an otherwise bleached auction catalogue. The canvas holds at #ffffff, but editorial photography is typically set against dark stone or black velvet, so the digital negative space reads as deliberate emptiness before the object takes over.

  Geometry is austere: buttons carry no radius (`{rounded.none}`) and are set in uppercase Diatype Mono at an expanded letter-spacing, conveying appointment-desk authority rather than retail urgency. Product cards occupy a portrait 3:4 aspect ratio and sit flush against one another with minimal gutter, so the editorial grid feels closer to a collector's album spread than a standard commerce listing. The navigation bar uses `{typography.nav-label}` in Diatype Mono at the smallest legible size, each initial-capped category balanced against a centred wordmark with a bottom hairline (`{colors.hairline}`) as the only structural line on the page.

  Ring detail pages deploy a clean left/right split — full-bleed imagery to the left, a structured data panel to the right with Bellefair for the piece name (`{typography.display-md}`) and Diatype Mono for pricing and specifications (`{typography.price-display}`). The result reads as a curated private-sale catalogue entry rather than a Shopify product page.

colors:
  primary: "#ff0000"
  primary-active: "#cc0000"
  primary-disabled: "#ff9999"
  ink: "#121212"
  body: "#747474"
  muted: "#9ca3af"
  mid-gray: "#767676"
  hairline: "#dedede"
  hairline-strong: "#c7c7c7"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Bellefair Regular', Bellefair, Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: 0.01em
  display-md:
    fontFamily: "'Bellefair Regular', Bellefair, Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  editorial-subhead:
    fontFamily: "'Bellefair Regular', Bellefair, Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'ABC Diatype Mono', ABCDiatypeMono, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'ABC Diatype Mono', ABCDiatypeMono, 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.02em
  body-sm:
    fontFamily: "'ABC Diatype Mono', ABCDiatypeMono, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.03em
  caption:
    fontFamily: "'ABC Diatype Mono', ABCDiatypeMono, 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
  nav-label:
    fontFamily: "'ABC Diatype Mono', ABCDiatypeMono, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "'ABC Diatype Mono', ABCDiatypeMono, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.14em
    textTransform: uppercase
  price-display:
    fontFamily: "'ABC Diatype Mono', ABCDiatypeMono, 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.04em
  label-micro:
    fontFamily: "'ABC Diatype Mono', ABCDiatypeMono, 'Courier New', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.12em
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 40px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.hairline-strong}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 39px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoAlign: center
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    accentColor: "{colors.primary}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.body-md}"
    labelTypography: "{typography.label-micro}"
    priceTypography: "{typography.price-display}"
    textColor: "{colors.ink}"
    mutedColor: "{colors.body}"
    gap: "{spacing.md}"
  hero:
    backgroundColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.editorial-subhead}"
    labelTypography: "{typography.title-md}"
    textColor: "{colors.on-dark}"
    overlayColor: "rgba(18,18,18,0.45)"
    ctaTypography: "{typography.button-md}"
    minHeight: 90vh
  collection-header:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-md}"
    labelTypography: "{typography.title-md}"
    labelColor: "{colors.muted}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  ring-detail-panel:
    backgroundColor: "{colors.canvas}"
    nameTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    specLabelTypography: "{typography.label-micro}"
    textColor: "{colors.ink}"
    mutedColor: "{colors.body}"
    sectionDivider: "1px solid {colors.hairline}"
    paddingLeft: "{spacing.xxl}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    gap: "{spacing.sm}"
  filter-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.ink}"
    padding: 8px 16px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-micro}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-md}"
    mutedColor: "{colors.mid-gray}"
    borderTop: none
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xxl}"
    columnGap: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Full-bleed near-black (#121212) with no border radius and uppercase Diatype Mono at 0.14em letter-spacing; the typographic choice makes the CTA read as a printed label on an instrument panel rather than a retail call to action. Hover shifts the background to a slightly lifted charcoal; disabled state uses `{colors.hairline-strong}` fill with `{colors.muted}` text to signal unavailability without colour.

**`button-secondary`** — Matches the primary in geometry and typography but inverts to a white fill with a 1px `{colors.ink}` border; used for secondary actions such as "Book an Appointment" alongside a primary "Add to Bag". On hover, the border intensifies and the fill transitions to `{colors.surface-soft}`.

**`button-ghost`** — Transparent background with no border; text in `{colors.ink}` using `{typography.button-md}`. Primarily used inline within editorial copy blocks for "Read more" or "Explore the collection" links that should not interrupt the reading rhythm with a contained shape.

### Text Input

**`text-input`** — Square-cornered with a `{colors.hairline}` border that thickens to `{colors.ink}` on focus; placeholder text sits in `{colors.muted}`. Form labels float above the field in `{typography.label-micro}` at 10px — the micro uppercase Diatype Mono label gives enquiry forms the same clinical register as a gemological certificate.

### Navigation Bar

**`nav-bar`** — Fixed to the top at 60px tall, white canvas with a single `{colors.hairline}` bottom rule. The wordmark is centred; navigation links sit left and utility icons (search, bag, account) sit right, all in `{typography.nav-label}`. No mega-menu: links expand to a minimal dropdown or trigger a full-screen overlay with a single category's imagery rather than a dense grid.

### Product Card

**`product-card`** — Portrait 3:4 image with no radius, no shadow, no card container — image sits directly on the page canvas. Below the image: a `{typography.label-micro}` category tag in `{colors.muted}`, the piece name in `{typography.body-md}`, and the price in `{typography.price-display}`. Cards grid in 2 columns on mobile and up to 4 on wide desktop with a tight `{spacing.md}` gap so the collection reads as a dense archive rather than a spaced boutique display.

### Hero

**`hero`** — Full-viewport editorial image with a dark overlay, headline in `{typography.display-xl}` Bellefair at white, and a supporting line in `{typography.editorial-subhead}`. The CTA button sits below the headline in the same `button-primary` treatment but inverted to white fill on dark for legibility. On mobile the overlay deepens to improve contrast and the headline reduces to `{typography.display-md}`.

### Collection Header

**`collection-header`** — White canvas, category label in `{typography.title-md}` Diatype Mono in `{colors.muted}` above a Bellefair headline in `{typography.display-md}`. An optional editorial paragraph follows in `{typography.body-md}`. A bottom `{colors.hairline}` rule separates the header from the filter bar and product grid. Padding-top matches `{spacing.section}` to give the page a considered interval after the navigation.

### Announcement Bar

**`announcement-bar`** — Anchored to the very top of the viewport at 36px in `{colors.ink}`, text centred in `{typography.caption}` on-dark white. The `{colors.primary}` red appears here as an accent for sale copy or urgency markers — a single coloured word or short phrase within an otherwise white sentence, never as a full-width coloured background.

### Ring Detail Panel

**`ring-detail-panel`** — The right-side panel in the two-column detail layout. The piece name leads in `{typography.display-md}` Bellefair; price in `{typography.price-display}` Diatype Mono; specification rows (carat, cut, metal) use `{typography.label-micro}` for the key and `{typography.body-sm}` for the value, separated by `{colors.hairline}` dividers. "Enquire" and "Book Viewing" sit as stacked CTAs — primary for enquire, secondary for viewing — with `{spacing.lg}` between them.

### Filter Tag / Breadcrumb

**`filter-tag`** — Zero-radius chip with `{colors.hairline}` border in default state; active state inverts to `{colors.ink}` fill with `{colors.on-dark}` text. Used to filter by metal, stone type, and era in collection views. **`breadcrumb`** uses `{typography.caption}` with `/` separators; inactive crumbs in `{colors.muted}`, the final active crumb in `{colors.ink}`.

### Sale Badge

**`sale-badge`** — Flat `{colors.primary}` red rectangle with no radius, white `{typography.label-micro}` text. Sits as an absolute overlay at the top-left of a product card image. The pure #ff0000 is reserved almost exclusively for this element and for error states; its appearance is therefore genuinely arresting against the otherwise achromatic page.

### Footer

**`footer`** — Full-width `{colors.ink}` background in four columns: brand story, navigation links, contact details, and newsletter sign-up. Column headings in `{typography.title-md}` uppercase Diatype Mono in on-dark white; body links in `{typography.body-sm}` in `{colors.mid-gray}`, turning full white on hover. No border-top — the transition from white page to black footer is an abrupt cut, consistent with the brand's editorial severity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero headline drops to `display-md` Bellefair; ring-detail-panel stacks below image in full width; announcement bar scrolls to two lines if needed |
| Tablet | 744–1128px | Two-column product grid; nav shows wordmark + icons with hamburger for links; hero retains full-bleed; ring-detail-panel becomes a 50/50 split |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav at 60px; ring-detail-panel at 55/45 image/panel split; collection-header allows wider editorial text measure |
| Wide | > 1440px | Four-column product grid; layout caps at 1440px max-width with symmetric margins; hero imagery scales but text block holds to a fixed 600px measure |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Filter tags expand to a minimum 44px height on mobile even at small type size
- Nav icons are 44px tap targets regardless of visual icon size (24px)
- "Enquire" and "Book Viewing" CTAs stack vertically on mobile with `{spacing.base}` gap

### Collapsing Strategy

- Navigation collapses from a horizontal label strip to a hamburger icon at < 744px; the open state is a full-screen overlay with category links in `{typography.display-md}` Bellefair, reversing the desktop register
- Ring detail panel stacks image above panel on mobile; panel padding reduces from `{spacing.xxl}` to `{spacing.lg}`
- Footer collapses from four columns to two columns at tablet and a single column at mobile; column heading spacing tightens to `{spacing.lg}`
- Collection header editorial paragraph is hidden on mobile to reduce scroll depth before the product grid

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed primary brand colour from brand guidelines; #ff0000 is the most distinctive extracted colour but may be reserved for error/sale states rather than serving as a true primary CTA colour — production implementation should verify
- ABC Diatype Mono is a licensed custom typeface; fallback stack relies on generic monospace — the exact weight variants (Regular only, or also Medium/Bold?) could not be confirmed from extraction
- Exact button hover and transition states (duration, easing) not recoverable from static extraction
- Ring detail panel layout specifics (exact column ratio, sticky scroll behaviour for panel) inferred from luxury-jewellery conventions rather than extracted
- Animation and page-transition behaviour (fade, scroll-triggered reveals) not captured — the brand likely uses subtle entrance animations given the editorial positioning
- Mobile navigation overlay design (background colour, link style, close button treatment) not confirmed from extraction
- Dark-mode support status unknown; meta theme-color is #ffffff suggesting light-only, but unconfirmed
