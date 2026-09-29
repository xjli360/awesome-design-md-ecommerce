---
version: alpha
name: "Wacom"
source_url: "https://www.wacom.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Wacom deploys a near-black charcoal ground — #2b333f and #223344 — so that the instruments themselves occupy the light: tablets, styluses, and the images produced on them carry the visual energy the UI deliberately withholds. Into that controlled dark surfaces one voltage: #ffdb00, a fluorescent-adjacent yellow that functions like a felt-marker highlight stroke, marking every primary CTA and active state with unmissable contrast against the dark ground. The choice is precise — not brand-generic blue, not a warm coral, but the specific yellow of a highlighter that references the tools Wacom sells without illustrating them.

  A secondary palette extends product-family logic: #ffe3e5 blush for consumer entry lines, #b5dfad sage for studio bundles, #ffcc66 amber for education and portable products. These are chromatic tags that let campaigns and landing pages fork their visual identity without losing system coherence. Blues in the extraction (#1f73b7, #3ac5fd, #1199ff, #66a8cc) serve interactive and informational states — link underlines, focus rings, status chips — rather than carrying primary brand weight. The dark greens (#224411, #223311) appear in promotional overlays and campaign sections as isolated moments of natural warmth against the technical charcoal grid.

  Typography runs Roboto, a mechanical sans that communicates precision over personality, reinforcing that Wacom's UI is infrastructure for creative work rather than the creative work itself. Display scales reach 40px weight 700 for campaign headlines; product names run 20–24px at weight 500; spec-and-feature body copy stays at 16px weight 400, scannable for professional buyers who parse data rather than narrative. Uppercase button labels with modest letter-spacing complete the technical register.

  Geometry is rectangular throughout — `{rounded.xs}` for buttons and badges, `{rounded.sm}` for cards and modals — with `{rounded.full}` absent from the main interaction layer entirely. This restraint signals instrument precision rather than consumer friendliness, consistent with a brand whose customers measure pen pressure in levels of 8,192. Product cards hold hardware photography in a fixed 4:3 ratio, never cropped or softened. Navigation is sticky with a dark (#2b333f) top bar expanding to image-forward mega-menus on hover. The overall system reads as a professional creative platform whose primary loyalty is to the work made on Wacom hardware, not the page promoting it.

colors:
  primary: "#ffdb00"
  primary-active: "#e6c400"
  primary-disabled: "#fff5b3"
  ink: "#2b333f"
  body: "#223344"
  muted: "#73859f"
  muted-soft: "#888888"
  hairline: "#d4dae3"
  hairline-soft: "#eaecef"
  canvas: "#ffffff"
  surface-soft: "#f5f7f9"
  surface-card: "#ffffff"
  surface-dark: "#2b333f"
  surface-dark-secondary: "#223344"
  on-primary: "#2b333f"
  on-dark: "#ffffff"
  accent-blush: "#ffe3e5"
  accent-sage: "#b5dfad"
  accent-amber: "#ffcc66"
  accent-forest: "#224411"
  link: "#1199ff"
  link-hover: "#1f73b7"
  info: "#1f73b7"
  focus-ring: "#3ac5fd"
  focus-ring-soft: "#66a8cc"

typography:
  display-xl:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.44
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  caption-bold:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.4px
  badge:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  label-md:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.2px
  spec-value:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  price:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  legal:
    fontFamily: "Roboto, Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
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
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 48px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.link}"
    typography: "{typography.button-md}"
    padding: 0
    border: none
  button-sm-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.focus-ring}"
    placeholderColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 11px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    borderFocus: "2px solid {colors.focus-ring}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid rgba(255,255,255,0.08)"
    position: sticky
    activeIndicator: "2px solid {colors.primary}"
  nav-mega-menu:
    backgroundColor: "{colors.surface-dark-secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.xxl}"
    borderTop: "2px solid {colors.primary}"
    columns: 4
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "4:3"
    productNameTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    shadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageAspectRatio: "4:3"
    productNameTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadOpacity: 0.72
    paddingY: "{spacing.section}"
    imagePosition: right
    minHeight: 520px
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    paddingY: "{spacing.section}"
    imagePosition: right
    minHeight: 440px
  category-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-blush:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  badge-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    fontWeight: 600
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  spec-table-row:
    borderBottom: "1px solid {colors.hairline}"
    labelTypography: "{typography.label-md}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    paddingY: "{spacing.sm}"
  comparison-table-header:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  comparison-highlight-cell:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    fontWeight: 700
  feature-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    legalTypography: "{typography.legal}"
    columns: 4
    paddingY: "{spacing.xxl}"
    borderTop: "1px solid rgba(255,255,255,0.08)"
  footer-logo:
    fill: "{colors.on-dark}"
    height: 24px

## Components

### Buttons

**`button-primary`** — A 48px-tall uppercase Roboto 700 label at 14px with 0.8px letter-spacing, filled #ffdb00 with #2b333f text. Hover deepens to `primary-active` (#e6c400); disabled fades to `primary-disabled` (#fff5b3) with muted gray text. Corners are `{rounded.xs}` (4px), keeping the silhouette rectangular and instrument-precise rather than friendly-rounded.

**`button-secondary`** — Same height and typographic weight as primary, but transparent fill with a 2px solid #2b333f border. On dark surfaces, `button-secondary-on-dark` swaps both border and label to white against the charcoal ground. Border weight is constant across all states; there is no fill or background hover transition.

**`button-ghost`** — Text-only, no border, no background, label in `{colors.link}` (#1199ff) at the same uppercase Roboto 700 weight. Reserved for secondary actions inside spec panels, support flows, and inline "Learn more" links.

**`button-sm-primary`** — A compact 36px variant of the primary button in the same yellow fill, used for card-level CTAs, comparison table actions, and accessory add-to-cart surfaces where the full 48px height would crowd the layout.

### Navigation

**`nav-bar`** — Sticky 64px dark (#2b333f) bar carrying the Wacom wordmark at left. Product-family categories render in `{typography.nav-link}` Roboto 500 14px at center-left; the active category receives a 2px #ffdb00 underline indicator. A utility row (region selector, account, cart) sits at the far right in `{typography.caption}` weight. The `nav-mega-menu` drops from a slightly lighter dark (#223344) ground with a 2px #ffdb00 top border, showing product families in a four-column image-forward grid — photography of actual tablets rather than icon grids.

### Forms

**`text-input`** — 48px height, 1px `{colors.hairline}` border at rest, `{rounded.xs}`, Roboto 16px body. Focus state replaces the hairline with a 2px `{colors.focus-ring}` cyan ring (#3ac5fd). Placeholder text in `{colors.muted}` gray (#73859f).

**`search-bar`** — Slightly shorter at 44px with a `{colors.surface-soft}` gray fill instead of white canvas, and a leading magnifier icon in muted gray. Lives in the nav utility area and in category-filtering panels above product grids.

### Product Card

**`product-card`** — White card with 1px hairline border and `{rounded.sm}` (8px) corners. A fixed 4:3 image zone at top holds hardware photography without crop, bleed, or zoom effect — the physical object sits in neutral light against a clean background. Below the image: a family badge (sage, blush, or amber), product name in `{typography.title-md}` Roboto 500, a descriptor line in `{typography.body-sm}`, and price in `{typography.price}` Roboto 700 20px. A `button-sm-primary` yellow CTA spans the base. The `product-card-dark` variant flips the entire card to the #2b333f charcoal ground for hero grids and campaign band sections.

### Badges

**`category-badge`**, **`badge-blush`**, **`badge-amber`** — Uppercase 11px Roboto 700 chips at 4px padding with `{rounded.xs}` corners, in sage (#b5dfad), blush (#ffe3e5), or amber (#ffcc66) respectively. All three maintain legible dark-text contrast without needing white overrides. A `badge-dark` variant on the charcoal ground uses white text for "NEW," "PRO," or "SALE" tags on dark product cards. Badges attach to the top-left of card image zones or inline before product names.

### Hero

**`hero-section`** — Full-width dark (#2b333f) panel, minimum 520px tall, padded `{spacing.section}` top and bottom. Headline in `{typography.display-xl}` Roboto 700 40px; subhead in `{typography.body-md}` at 72% opacity white for visual hierarchy without additional type weight. Primary yellow CTA anchors below the subhead. Product imagery floats right at roughly 50% panel width on desktop, collapses above copy on mobile. `hero-light` mirrors the structure on a `{colors.surface-soft}` ground for secondary campaign panels and educational landing sections.

### Promo Banner

**`promo-banner`** — An edge-to-edge #ffdb00 strip with no rounded corners, sitting above the nav or anchored at page top. Carries short promotional copy (sale events, new product drops) in `{typography.body-sm}` Roboto 600 at #2b333f text. The full-bleed yellow stripe is the loudest moment in the page hierarchy outside of a CTA button.

### Spec Table and Comparison

**`spec-table-row`** — Two-column rows with label in `{typography.label-md}` muted blue-gray (#73859f) and value in `{typography.spec-value}` ink (#2b333f), separated by a `{colors.hairline}` bottom border. Dense and scannable — professional buyers navigate spec tables more than any hero banner. The `comparison-table-header` uses the dark (#2b333f) surface for column headers, and `comparison-highlight-cell` floods the recommended SKU column in #ffdb00 with dark ink text for immediate upsell visibility.

### Feature Panel

**`feature-panel`** — Soft gray (#f5f7f9) section background with headline in `{typography.display-md}` Roboto 600 24px and body in `{typography.body-md}`. Feature icons render in #ffdb00 primary yellow. Used in three- to four-column benefit grids between hero sections and product listings — pressure levels, connectivity specs, bundle inclusions.

### Filter Chips

**`filter-chip`** — Small rectangular chips in `{colors.surface-soft}` fill with a 1px hairline border at rest. Active state fills the chip with #2b333f ink and turns label text white. Used in product category pages to filter by line (Intuos, Cintiq, One), connectivity (Bluetooth, USB-C), or feature level. No rounded-pill shape — keeps the filtering surface in the same rectangular register as the rest of the system.

### Footer

**`footer`** — Four-column grid on a #2b333f dark ground matching the nav. Link text is white (`{colors.on-dark}`); secondary descriptive text drops to `{colors.muted}` gray (#73859f). The Wacom wordmark anchors the footer-top at left; a social icon row sits at the bottom of the grid. Legal copy runs in `{typography.legal}` 11px at muted gray. A hairline border-top at 8% white opacity separates footer from page content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + wordmark; hero stacks image above copy; product grid goes single-column; spec tables scroll horizontally; all primary CTAs expand to full width |
| Tablet | 744–1128px | Nav shows top-level categories without mega-menu hover (tap reveals a slide-in panel); product grid goes 2-column; hero splits 55/45 copy/image |
| Desktop | 1128–1440px | Full sticky nav with 4-column mega-menu on hover; 3–4 column product grids; 50/50 hero split; comparison table fully visible |
| Wide | > 1440px | Content max-width ~1400px centered; hero padding increases; footer grid expands to 5 columns with added region/language selector column |

### Touch Targets

- Minimum 44×44px on all interactive elements — buttons, nav items, filter chips, card CTAs, breadcrumb links
- Filter chips expand to 10px vertical padding on mobile to meet the 44px touch target minimum
- Search bar stays at 44px height across all breakpoints; form text inputs stay at 48px
- Nav mega-menu items gain 12px padding on touch devices to prevent misfire between adjacent product categories

### Collapsing Strategy

- Nav mega-menu becomes a full-screen slide-in drawer on mobile, with product-family sections as accordions that reveal sub-SKUs
- Spec tables switch from two-column grid layout to stacked label/value pairs below 744px — label on its own line in muted gray, value directly below in ink
- Comparison tables collapse to a horizontally swipeable card stack on mobile, showing one product per visible card with a scroll indicator
- Feature panels reflow from 4-column to 2-column at tablet, single-column at mobile with icon and copy stacked vertically
- Footer grid collapses from 4 columns to 2 at tablet and 1 at mobile; link groups become accordions with yellow chevron indicators

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; Roboto inferred as primary face from the font stack — Wacom may use a licensed or proprietary display face on campaign pages not captured in this extraction
- Dark greens (#224411, #223311) were extracted but their exact semantic role is unclear — possible promotional overlay color or product-specific campaign surface; used conservatively as `{colors.accent-forest}` without assigning to component backgrounds
- No explicit border-radius values extracted from computed styles; radii assigned from visual convention consistent with the technical/rectangular brand register
- Light blues (#1f73b7, #1199ff, #66a8cc, #3ac5fd) suggest a multi-tone interactive system; precise semantic mapping (link, info, focus, visited) could not be confirmed from extraction alone
- No dark-mode token set detected; the dark surfaces (#2b333f, #223344) appear to be designed light-mode dark zones rather than a system-level color-scheme preference
- Product-family color assignments (which badge accent maps to Intuos vs. Cintiq vs. Wacom One) could not be confirmed; sage/blush/amber assignments are reasoned approximations based on product tier positioning
- Precise spacing scale (gap values, section padding) not confirmed from extraction; values follow standard Roboto UI conventions
