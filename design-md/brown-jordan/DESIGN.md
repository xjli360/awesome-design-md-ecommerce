---
version: alpha
name: "Brown Jordan"
source_url: "https://www.brownjordan.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Pool-water teal against weathered stone. Brown Jordan's digital palette draws from the same material vocabulary as its furniture — cast aluminum, woven resin, aged teak — translating each into a warm gray that sits somewhere between #414040 and #cececa on an off-white canvas (#f7f7f4) that refuses pure white the way natural linen refuses bleach. The single chromatic break is #7bc7c7, a coastal teal that appears on primary CTAs, collection markers, and active navigation states, bright enough to register as intentional against the neutral field but never loud. A secondary voltage in red-orange (#f33d00) fires sparingly on sale indicators and urgency badges, warming the cool teal without competing for hierarchy. Typography pairs ABC Arizona Flare — a contemporary serif with open apertures and subtle ink traps — against Neue Haas Unica Pro for body copy and UI chrome. The serif runs large and light (display at 44–56px, weight 300–400) with negative letter-spacing that reads like engraved catalog titling, not digital-first marketing. Montserrat handles navigation and button labels in all-caps with generous tracking, lending architectural precision to the functional layer. Corner radii stay tight: {rounded.xs} on buttons, {rounded.sm} on cards, no pill shapes anywhere — edges mirror the extruded aluminum profiles that define Brown Jordan's physical design language. Spacing runs wide and unhurried. Hero banners occupy 85vh minimum with {spacing.section} gaps between folds, product grids breathe inside generous gutters, and the 72px navigation bar holds the logo and a sparse set of category links without crowding. Material swatches ({rounded.full} circles with a 2px border) replace standard variant dropdowns, foregrounding the fabric-and-finish decision that drives a high-end outdoor purchase. The footer inverts into #414040 ink, carrying legal links and trade-program callouts in {typography.body-sm} against the dark ground. The overall rhythm is editorial — long scroll, full-bleed photography, minimal copy per viewport — designed for someone furnishing an outdoor room, not adding items to a cart on impulse.

colors:
  primary: "#7bc7c7"
  primary-active: "#5fb3b3"
  primary-disabled: "#bde3e3"
  accent: "#f33d00"
  accent-warm: "#f66838"
  ink: "#414040"
  ink-soft: "#4d4d4d"
  body: "#545453"
  muted: "#949492"
  muted-soft: "#a6a6a3"
  border-strong: "#b6b6b6"
  hairline: "#cececa"
  hairline-soft: "#e0e0dd"
  canvas: "#f7f7f4"
  surface-soft: "#fef5f2"
  surface-warm: "#fffaf0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#f7f7f4"
  link: "#146ff8"

typography:
  display-xl:
    fontFamily: "'ABC Arizona Flare', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ABC Arizona Flare', Georgia, 'Times New Roman', serif"
    fontSize: 44px
    fontWeight: 300
    lineHeight: 1.14
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ABC Arizona Flare', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.17
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'ABC Arizona Flare', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.21
    letterSpacing: 0
  title-lg:
    fontFamily: "'Neue Haas Unica Pro', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'Neue Haas Unica Pro', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Neue Haas Unica Pro', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Unica Pro', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Unica Pro', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.17
    letterSpacing: 1.2px
    textTransform: uppercase
  eyebrow:
    fontFamily: "'Montserrat', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 2px
    textTransform: uppercase
  price-lg:
    fontFamily: "'Neue Haas Unica Pro', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Neue Haas Unica Pro', 'Lato', -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.primary}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    imageRatio: "4:5"
    imageFit: cover
  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 85vh
    padding: "{spacing.section} {spacing.xl}"
  collection-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.sm}"
    imageRatio: "3:4"
    imageFit: cover
  material-swatch:
    width: 48px
    height: 48px
    rounded: "{rounded.full}"
    border: 2px solid {colors.hairline}
    cursor: pointer
  material-swatch-active:
    width: 48px
    height: 48px
    rounded: "{rounded.full}"
    border: 2px solid {colors.primary}
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    linkColor: "{colors.on-dark}"
  search-overlay:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    boxShadow: 0 8px 32px rgba(0, 0, 0, 0.12)
    padding: "{spacing.lg}"
  trade-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  lifestyle-strip:
    backgroundColor: "{colors.canvas}"
    minHeight: 480px
    imageRatio: "16:9"
    gap: "{spacing.md}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  finish-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline}
  finish-selector-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary}

---

## Components

### Buttons

**`button-primary`** — Filled teal (#7bc7c7) rectangle with white uppercase Montserrat text at 13px/600 weight and 1.5px letter-spacing. Corners clip to `{rounded.xs}` (4px), keeping the silhouette architectural rather than playful. On hover the background deepens to `primary-active` (#5fb3b3); on press a subtle inset shadow appears. Disabled state fades to `primary-disabled` (#bde3e3) at reduced opacity, preventing ghost clicks on out-of-stock configurators.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border and dark uppercase label, sized identically to the primary button (48px height, same typography). On hover the border fills to solid `{colors.ink}` and the text inverts to `{colors.canvas}`, creating a full dark button. Used for secondary actions like "View Collection" alongside a primary "Configure" CTA, or as the default action when teal would compete with product photography.

### Text Input

**`text-input`** — White card surface with a 1px `{colors.hairline}` border and `{rounded.xs}` corners, standing 48px tall to match button heights for inline form layouts. Placeholder text renders in `{colors.muted}` (#949492), input text in `{colors.ink}`. On focus the border transitions to `{colors.primary}`, providing a clear teal ring without a heavy box-shadow — consistent with the brand's minimal ornamentation. Labels sit above the input in `{typography.caption}` weight.

### Navigation

**`nav-bar`** — A 72px-tall horizontal bar on the warm canvas (#f7f7f4) with a 1px `{colors.hairline-soft}` bottom border. The logo sits left-aligned; primary category links (Residential, Hospitality, Collections) run in `{typography.nav-link}` — 12px uppercase Montserrat with 1.2px tracking. Active link state adds a 2px bottom border in `{colors.primary}`. A utility cluster (search icon, trade login, cart) sits right-aligned. On scroll the bar becomes sticky with a subtle drop shadow (0 2px 8px rgba(0,0,0,0.06)) and the canvas background remains opaque.

### Product Card

**`product-card`** — Borderless card on `{colors.surface-card}` with `{rounded.sm}` (8px) corners clipping the product image, which fills a 4:5 aspect container via object-fit cover. Below the image: product name in `{typography.title-md}` (18px/500), collection name in `{typography.caption}` at `{colors.muted}`, and price in `{typography.price-lg}` (20px/400). On hover the image scales to 1.03× over a 400ms ease-out, and a "Quick View" label fades in as a centered overlay in `{typography.button-sm}`. Cards sit in a CSS grid with `{spacing.lg}` (24px) column and row gaps.

### Hero Banner

**`hero-banner`** — Full-bleed image or video container spanning a minimum of 85vh, with a warm `{colors.surface-warm}` (#fffaf0) fallback behind slow-loading assets. Headline text overlays in `{typography.display-xl}` — 56px ABC Arizona Flare at weight 300 with -0.5px tracking, positioned bottom-left with `{spacing.section}` padding. A single CTA button (primary or secondary depending on image brightness) sits below the headline. On darker images, text and button colors invert to `{colors.on-dark}`. The banner supports an optional `{typography.eyebrow}` tag above the headline for collection or season labels.

### Collection Card

**`collection-card`** — Tall (3:4 aspect ratio) image card with `{rounded.sm}` corners, used in grid layouts to represent product collections like "Dining", "Lounge", or "Accessories". The collection name overlays at the bottom in `{typography.title-lg}` (22px/500) against a subtle gradient scrim (transparent to rgba(0,0,0,0.35)). Text renders in `{colors.on-dark}`. On hover the image pans slightly (translateY -2%) and the gradient intensifies. No border, no drop shadow — the image does the work.

### Material Swatch

**`material-swatch`** — A 48px circular element (`{rounded.full}`) displaying a fabric or finish thumbnail, bordered by 2px `{colors.hairline}`. Swatches sit in a horizontal row with `{spacing.sm}` gaps beneath a "Select Finish" label in `{typography.caption}`. On selection the border transitions to 2px `{colors.primary}` and a small checkmark icon appears at bottom-right in white against a teal dot. This component replaces traditional dropdown selectors for the fabric-and-finish decision central to outdoor furniture purchase, giving customers a visual preview rather than a text label.

### Breadcrumb

**`breadcrumb`** — Horizontal text trail in `{typography.caption}` (12px) at `{colors.muted}`, separated by "/" characters with `{spacing.sm}` gaps. The final (active) segment renders in `{colors.ink}` at the same size. Sits at the top of product and collection pages with `{spacing.lg}` bottom margin, providing orientation without visual weight.

### Footer

**`footer`** — Dark block in `{colors.ink}` (#414040) with text and links in `{colors.on-dark}` (#f7f7f4). Content organizes into four columns: Product Categories, About (heritage, sustainability, trade program), Customer Service, and a newsletter signup input. Column headers use `{typography.eyebrow}` (11px uppercase Montserrat); links use `{typography.body-sm}`. A bottom bar carries copyright, legal links, and social icons separated by a 1px `{colors.muted}` top border. Vertical padding is `{spacing.section}` (64px) top and bottom.

### Search Overlay

**`search-overlay`** — A centered modal panel on `{colors.surface-card}` with `{rounded.sm}` corners and a 0 8px 32px rgba(0,0,0,0.12) shadow, triggered from the nav-bar search icon. The input field auto-focuses, styled per `text-input` but wider (100% of the 640px panel). Below the input, recent searches and suggested collections appear in `{typography.body-sm}`. A click-away scrim (rgba(0,0,0,0.3)) covers the page behind the overlay.

### Badges

**`trade-badge`** — Small pill in `{colors.primary}` with white `{typography.eyebrow}` text (11px uppercase, 2px tracking), used to flag trade-program pricing or hospitality-exclusive items. Corners at `{rounded.xs}`, padding 4px 10px. Appears inline next to product titles or on card overlays.

**`sale-badge`** — Same dimensions as trade-badge but filled with `{colors.accent}` (#f33d00) to signal clearance or seasonal promotions. The red-orange is reserved exclusively for price reductions — it never appears as a decorative element — so its presence carries immediate meaning against the otherwise neutral-and-teal palette.

### Lifestyle Strip

**`lifestyle-strip`** — A horizontal row of 2–3 full-bleed editorial images in 16:9 aspect ratio, separated by `{spacing.md}` (12px) gaps. Images show furniture in situ — poolside terraces, hotel lobbies, coastal balconies. No text overlay, no CTA; the strip is purely atmospheric, breaking up the product grid with environmental context. On mobile the strip collapses to a single swipeable carousel.

### Announcement Bar

**`announcement-bar`** — A 40px-tall dark bar (`{colors.ink}`) pinned above the nav-bar, carrying a single centered line of text in `{typography.caption}` at `{colors.on-dark}`. Used for shipping thresholds ("Complimentary White Glove Delivery on Orders Over $2,500"), trade-program invitations, or seasonal events. Dismissible via a small × icon aligned right, which sets a session cookie to prevent reappearance.

### Finish Selector

**`finish-selector`** — A bordered card (`{rounded.xs}`, 1px `{colors.hairline}`) containing a finish name in `{typography.body-sm}` and an optional thumbnail swatch. Used on product detail pages as an alternative to material swatches when finishes need descriptive labels (e.g., "Parchment Powder-Coat" or "Natural Teak"). Active state swaps to a 2px `{colors.primary}` border; the card background remains `{colors.surface-card}` in both states. Cards arrange in a wrapping flex row with `{spacing.sm}` gaps.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + logo + cart icon. Hero shrinks to 70vh with display-md (36px) headline. Product grid drops to 2 columns at {spacing.sm} gap. Footer stacks into single column accordion. Material swatches shrink to 36px. Announcement bar text drops to 11px. |
| Tablet | 744–1128px | Nav shows top-level category links but utility links collapse to icons. Hero runs 80vh with display-lg (44px) headline. Product grid at 3 columns. Collection cards shift to 2-up. Footer columns wrap to 2×2. |
| Desktop | 1128–1440px | Full nav with all links visible. Hero at 85vh with display-xl (56px). Product grid at 3–4 columns with {spacing.lg} gaps. Lifestyle strip shows all 3 images. Footer renders 4 columns side by side. |
| Wide | > 1440px | Content max-width caps at 1440px, centered with auto margins. Product grid allows up to 4 columns. Hero image may extend beyond content-width as a full-bleed background. Spacing scales up: section gaps increase to 80px. |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target on mobile, even when visually smaller (padding expands the hit area)
- Material swatches at 36px on mobile include 4px invisible padding to reach the 44px minimum
- Nav hamburger icon renders at 24px but its tap region spans 48×48px
- Footer accordion headers carry 48px row height for comfortable thumb tapping

### Collapsing Strategy
- Navigation: hamburger slide-out drawer on mobile/tablet, full horizontal bar on desktop
- Product grid: 2 → 3 → 4 columns as width increases; card aspect ratio remains 4:5 at all breakpoints
- Hero text: shifts from display-xl to display-md as viewport narrows, maintaining a maximum of ~20 characters per line
- Footer: single-column accordion on mobile, 2×2 grid on tablet, 4-column row on desktop
- Lifestyle strip: carousel with pagination dots on mobile, full row on tablet and above
- Search overlay: full-screen takeover on mobile (no rounded corners, no shadow), centered panel on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The teal primary (#7bc7c7) against white text (#ffffff) should be verified for WCAG AA contrast compliance; if the live site uses dark text on teal instead, `on-primary` should be adjusted to `{colors.ink}`
- Several extracted color scales (#fef5f2 → #f33d00 → #631900 and #fffaf0 → #dd6b20) follow a 10-step gradient pattern consistent with a CSS framework (Chakra UI or Tailwind); these may not all be intentional brand tokens — only the endpoints (#f33d00 as accent, #fef5f2 and #fffaf0 as warm surfaces) are referenced in this system
- The exact font weights and optical sizes used for ABC Arizona Flare could not be confirmed from extraction alone; the typeface ships in multiple optical grades and the live site may use a variable-font axis not captured here
- Neue Haas Unica Pro versus Lato usage hierarchy is inferred — the site loads both but their exact assignment to body versus UI roles may differ from what is specified
- Interaction motion curves (easing functions, transition durations) were not extracted; the 400ms ease-out on card hover is estimated from typical luxury-furniture site patterns
- The site is not Shopify-based, and JS-loaded design tokens or CSS custom properties may define additional values not visible in static extraction
- Trade-program gated content (pricing tiers, exclusive collections) was not accessible and may carry distinct styling not reflected here
