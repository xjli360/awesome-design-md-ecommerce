---
version: alpha
name: "Alighieri"
source_url: "https://www.alighieri.co.uk"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every clasp and pendant Alighieri sends into the world looks as though it was unearthed rather than made — wax-cast, deliberately scarred into warmth, carrying the grain of a lost-wax mould as proof of origin. The website holds the same register: a parchment canvas ({colors.canvas}) keeps editorial photography from feeling clinical, while a near-black ink ({colors.ink}) drawn from the darker passages of a manuscript presses type into the eye with unhurried authority. Gold threads through the system not as a background fill but as a structural accent — the antique brass of {colors.primary} marks CTAs, link hovers, and the hairline rules that separate collection stanzas, always referencing the metal being sold rather than performing luxury in the abstract. Typography tilts wholly into the serif register. Display headings arrive at a light 300 weight and generous tracking — 52px at the editorial hero, stepping to 36px for collection titles — carrying the cadence of a couplet rather than an advertisement. Body copy holds the same serif family at reading weight with a loose 1.7 line-height, giving poetic product descriptions room to breathe. Buttons carry near-zero rounding ({rounded.none}), their sharp edges a deliberate counterpoint to the organic, irregular forms of the jewelry above. Product cards sit on the same {colors.surface-card} ground as the page itself, dissolving the frame between product and editorial and presenting pieces as though they rest on a page of manuscript rather than inside a commerce window. The interaction pattern is spare: no floating cart badges in saturated coral, no countdown timers, no aggregated star ratings above the fold. Navigation is a single horizontal rail — spaced, light-weight serif labels — sitting low-profile across the parchment. The collection grid uses two columns at desktop with generous vertical breathing room; price appears quietly below the piece name, never foregrounded. A newsletter footer band introduces the only high-contrast break in the system — the deep {colors.editorial-dark} ground against ivory type, a cinematic cut to black that briefly suspends the warm register before returning the viewer to the archive of objects.

colors:
  primary: "#B8964E"
  primary-active: "#9A7A38"
  primary-disabled: "#DDD0B0"
  ink: "#1C1510"
  body: "#3D2E1E"
  muted: "#7A6550"
  hairline: "#D4C9B8"
  canvas: "#F5F0E5"
  surface-soft: "#EDE8DC"
  surface-card: "#F5F0E5"
  on-primary: "#F5F0E5"
  gold-deep: "#8C6B2E"
  editorial-dark: "#0D0A08"

typography:
  display-xl:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: 0.02em
  display-md:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.015em
  display-sm:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.01em
  title-md:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
  body-md:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.01em
  caption:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.05em
  button-md:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.08em
  price-display:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.03em
  editorial-label:
    fontFamily: "Cormorant Garamond, Garamond, Georgia, serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.15em
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
    border: none
    hoverBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.ink}"
    hoverBorderColor: "{colors.primary}"
    hoverTextColor: "{colors.primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 0
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderStyle: "none none solid none"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 0px
    height: 44px
    focusBorderColor: "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    wordmarkTypography: "{typography.display-sm}"
    position: sticky
    scrollShadow: "0 1px 8px rgba(28,21,16,0.06)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
    hoverEffect: "crossfade to secondary image"
    secondaryActionComponent: "quick-add-overlay"
  hero-editorial:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    overlayColor: "{colors.ink}"
    overlayOpacity: 0.3
    layout: "full-bleed image, centered text overlay"
    ctaComponent: "button-primary"
    minHeight: 80vh
  collection-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.editorial-label}"
    labelColor: "{colors.primary}"
    titleTypography: "{typography.display-md}"
    layout: "centered label + title above 2–3 column product grid"
    padding: "{spacing.section} 0"
  editorial-story:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    tagTypography: "{typography.editorial-label}"
    tagColor: "{colors.primary}"
    layout: "50/50 — photography left, prose right; alternates per module"
    padding: "{spacing.section}"
  story-label:
    textColor: "{colors.primary}"
    typography: "{typography.editorial-label}"
    backgroundColor: "transparent"
  newsletter-band:
    backgroundColor: "{colors.editorial-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    inputBorderColor: "{colors.muted}"
    ctaComponent: "button-primary"
    layout: "centered heading + body, then inline input + CTA row"
    padding: "{spacing.section} 0"
  product-detail-badge:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.editorial-label}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  quick-add-overlay:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 36px
    opacity: 0.92
    position: "bottom of product card, slides up on hover"
    label: "ADD TO BAG"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    linkColor: "{colors.ink}"
    linkHoverColor: "{colors.primary}"
    padding: "{spacing.xxl} 0"
    columnLayout: "4-column grid at desktop, stacked on mobile"

## Components

### Buttons

**`button-primary`** — A sharp-cornered ({rounded.none}) bar filled with antique gold ({colors.primary}), serving as the primary add-to-bag and checkout action. The all-caps spaced label ({typography.button-md}, 0.12em tracking) echoes the editorial-label system used throughout the site. On hover the fill deepens to {colors.primary-active}; on disabled the gold washes back to {colors.primary-disabled}. The 44px height is present without being dominant — commerce-functional but never brash.

**`button-secondary`** — The same sharp geometry, but hollow: a 1px {colors.ink} border against the {colors.canvas} ground. Used for secondary actions like "Explore the collection" or filter triggers. Hover shifts both border and label to {colors.primary}, introducing gold as a directional signal without filling the button. The contrast between filled primary and outlined secondary is intentionally low-key — both read as similarly weighted options.

**`button-ghost`** — No border, no fill — a bare uppercase underlined string in {colors.primary}. Appears inline within editorial prose and at section footers as "Read more" or "Discover" anchors. The underline is the only affordance; the interaction is closer to a footnote than a CTA.

### Text Input

**`text-input`** — Three sides open, one hairline rule ({colors.hairline}) active at the bottom in resting state. On focus the rule sharpens to {colors.ink} and the cursor appears. Placeholder text in {colors.muted} with the same {typography.body-md} as surrounding editorial copy, so the field feels part of the page rather than a UI intrusion. No border radius ({rounded.none}), no background fill — used across search, email signup, and checkout address fields.

### Navigation

**`nav-bar`** — A 60px sticky horizontal rail on the {colors.canvas} ground with a single {colors.hairline} bottom border. The wordmark "ALIGHIERI" appears left-aligned in {typography.display-sm}, treated as a typographic element rather than a logo lockup — the name is the identity. Navigation links in {typography.nav-link} (13px, spaced at 0.08em) float across the center with wide breathing room. Bag count and search icon sit right-aligned. On scroll the bar acquires a faint warm shadow without shifting its background color.

### Product Card

**`product-card`** — No border, no shadow, no card container — the product image rests directly on the {colors.surface-card} ground, collapsing the distinction between shelf and page. Portrait-ratio photography (3:4) crossfades to a second shot on hover. Product name in {typography.title-sm} and price in {typography.price-display} sit below, both in {colors.ink}, with price subordinate in size. The `quick-add-overlay` slides up from the bottom on hover: a full-width {colors.ink} bar with ivory "ADD TO BAG" in {typography.button-sm}, reading as a cinematic caption rather than a shop widget.

### Hero Editorial

**`hero-editorial`** — Full-bleed photography at 80vh minimum, with a warm {colors.ink} scrim at 0.3 opacity and centered text overlay. The headline renders in {typography.display-xl} at 300 weight — the lightest scale in the system — trusting the serif's authority without bolding. A short italic subline in {typography.body-md} and a `button-primary` CTA complete the stack. On mobile the image crops to a tall portrait and text drops below rather than overlaying, preserving legibility without a heavier scrim.

### Collection Band

**`collection-band`** — A recurring section module that anchors a named collection: a small {colors.primary} category string in {typography.editorial-label} above a {typography.display-md} title, both centered, followed by a two- or three-column `product-card` grid. No carousel — the full grid is visible at once, encouraging browse-by-eye. Generous {spacing.section} padding above and below gives the module room to breathe against adjacent editorial content.

### Editorial Story

**`editorial-story`** — A 50/50 split panel: full-height photography on one side, flowing prose on the other, set against {colors.surface-soft}. The text column opens with a {story-label} tag in {colors.primary} (e.g. "PARADISO · CANTO III"), followed by a {typography.display-md} heading, then {typography.body-md} body copy running to 3–5 paragraphs. Modules alternate left/right image placement as the page scrolls, creating a visual rhythm that echoes the call-and-response of terza rima. A `button-ghost` link closes the column.

### Newsletter Band

**`newsletter-band`** — The site's only fully dark module: a {colors.editorial-dark} ground that cuts the parchment register like a blackout between scenes. A short heading in {typography.display-sm} in ivory, one line of {typography.body-sm} copy, then an inline `text-input` (email) paired with a `button-primary`. The antique gold CTA against the near-black ground is the highest-contrast moment in the system — the only place where {colors.primary} reads as luminous rather than warm.

### Product Detail Badge

**`product-detail-badge`** — A small outlined label (1px {colors.primary} border, {rounded.none}) carrying provenance strings like "24kt Gold Plated", "Sterling Silver", or "Limited Edition" in {typography.editorial-label}. Sits below the product title on the PDP. No fill — the gold border alone signals material authenticity without shouting.

### Breadcrumb

**`breadcrumb`** — A single horizontal line of ancestry links in {typography.caption} and {colors.muted}, with chevron separators in {colors.hairline}. The active (current) page renders in {colors.ink} to confirm location. Positioned above the page heading on collection and product pages; absent from the homepage.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text drops below image rather than overlaying; nav collapses to hamburger + centered wordmark; `quick-add-overlay` becomes a persistent below-image tap target rather than a hover state; `editorial-story` stacks image above text full-width |
| Tablet | 744–1128px | Two-column product grid; `editorial-story` stacks vertically (full-width image above text column); nav-bar remains horizontal but with fewer visible links; `newsletter-band` stacks input above button |
| Desktop | 1128–1440px | Two- to three-column product grid; full 50/50 `editorial-story` split restored; nav fully expanded; `newsletter-band` inline input + CTA layout |
| Wide | > 1440px | Content max-width ~1400px centered on {colors.canvas}; hero photography scales to fill viewport but headline and text column are width-capped to ~680px to prevent over-long measure |

### Touch Targets

- All nav links and icon buttons maintain a minimum 44×44px tap target regardless of visual rendering size
- `quick-add-overlay` on mobile is a persistent bar below the product image, not a hover-triggered overlay
- Form inputs sized at 44px height on mobile to match button height and reduce mis-tap
- Breadcrumb links padded to 32px vertical for comfortable reachability

### Collapsing Strategy

- Navigation drawer at < 744px slides in from the left on the {colors.canvas} ground with a faint {colors.hairline} right border; links render in {typography.display-sm} rather than the compressed `nav-link` scale
- `editorial-story` panels stack vertically at tablet and below: photography first (full-width, 60vw tall), text column second
- `collection-band` grid drops from three columns → two → one as viewport narrows; vertical gap between cards increases on single-column to preserve the airy editorial feel
- `newsletter-band` input stacks above CTA on mobile; the `text-input` becomes full-width at 100%

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (JS-loaded design tokens or anti-bot protection). All color values are inferred from published brand photography, editorial imagery, and lookbooks — not scraped CSS. Treat the entire palette as provisional and verify against the live stylesheet before production use.
- No font-family stacks were detected. Typography is inferred from the brand's Dante-inspired literary aesthetic and published press imagery; the specific typeface (possibly a licensed or custom serif distinct from Cormorant Garamond) is unconfirmed.
- No `theme-color` meta tag was present, removing a common signal for the primary brand color.
- Exact button and card border-radius values unconfirmed — the near-zero rounding assumption is inferred from the brand's object-first, anti-commercial aesthetic.
- Hover animation timing, image crossfade duration, and drawer slide easing could not be extracted and are omitted from this spec.
- PDP image aspect ratio (portrait 3:4 vs. square vs. mixed) is unconfirmed; the 3:4 assumption reflects common practice for fine jewelry and the brand's editorial photography style.
- Whether the site implements a dark mode or inverted colorway is unknown — the warm parchment system likely ships with no dark-mode variant.
- Material filter and size-selector UI patterns on PDP are unconfirmed; Alighieri's sizing conventions (metal type, chain length) may require bespoke selector components not covered here.
