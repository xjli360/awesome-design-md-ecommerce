---
version: alpha
name: "Goldilocks"
source_url: "https://cookwithgoldilocks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The name makes the brand argument before any product image loads — "just right" is borrowed from a children's story, but here it points at a real engineering claim: cookware that hits the weight window between flimsy stainless and back-wrenching cast iron. Warm amber and honey tones saturate every surface the eye lands on, from the primary call-to-action — a rich ochre gold that reads as earned rather than cheerful — to the off-cream canvas (#FAFAF7) that keeps photography from competing with a pure white void. The pan in every hero shot is mid-use, oil pooling, steam implied; the brand photographs process, not pristine product. Corner radii stay modest throughout: cards and buttons round only to `{rounded.sm}` or `{rounded.md}`, grounding the warmth in something solid rather than letting it float into pill-shaped softness. Navigation is lean — four or five links, with the wordmark carrying visual weight at the upper left and a cart icon closing the right — a cookware-specific restraint that prioritizes browse-to-buy over content sprawl. The type system leans on a clean geometric sans for body and UI copy, while display headlines carry slightly more weight, pulling the eye down a product page through a rhythm of bold claim, sub-claim, and photography. Spacing is generous at the section level — the kitchen metaphor requires breathing room between content blocks the way a good recipe requires resting time between steps. Product cards surface pan name, lifestyle image, and price without review stars cluttering the tile; social proof lives on individual product pages, not the grid. The warranty and materials story — carbon steel gauge, seasoning process, heat range — appears in a persistent trust strip beneath the hero, signaling that the purchase justification is functional, not aspirational.

colors:
  primary: "#C47D2E"
  primary-active: "#A5641A"
  primary-disabled: "#E8C99A"
  ink: "#1C1712"
  body: "#3A2E24"
  muted: "#7A6A5A"
  muted-soft: "#A89282"
  hairline: "#DDD4C5"
  hairline-soft: "#EDE6DC"
  canvas: "#FAFAF7"
  surface-soft: "#F4EEE5"
  surface-card: "#FFFFFF"
  surface-warm: "#FBF5EC"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  accent-cream: "#F2E8D6"
  accent-charcoal: "#2C2620"

typography:
  display-xl:
    fontFamily: "var(--font-display, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "var(--font-display, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "var(--font-display, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "var(--font-display, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "var(--font-display, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "var(--font-body, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "var(--font-body, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "var(--font-body, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "var(--font-display, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "var(--font-display, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  overline:
    fontFamily: "var(--font-body, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  badge:
    fontFamily: "var(--font-body, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  price-display:
    fontFamily: "var(--font-display, 'Inter', 'Helvetica Neue', Arial, sans-serif)"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
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
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.accent-charcoal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 40px
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    imageAspectRatio: "4:5"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
  hero:
    backgroundColor: "{colors.surface-warm}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaButton: button-primary
    minHeight: 560px
    imagePosition: right
  trust-strip:
    backgroundColor: "{colors.accent-cream}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    iconSize: 24px
    iconColor: "{colors.primary}"
    padding: "{spacing.lg} 0"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
  size-selector:
    activeBackground: "{colors.primary}"
    activeText: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveText: "{colors.ink}"
    inactiveBorder: "1.5px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-sm}"
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.overline}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  recipe-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    imageAspectRatio: "16:9"
    overlineTypography: "{typography.overline}"
    overlineColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    padding: "{spacing.base}"
  feature-icon-row:
    backgroundColor: "{colors.canvas}"
    iconColor: "{colors.primary}"
    iconSize: 32px
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.body}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    gap: "{spacing.xl}"
  comparison-table:
    headerBackground: "{colors.accent-cream}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    highlightBackground: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    buttonSize: 36px
  footer:
    backgroundColor: "{colors.accent-charcoal}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    bodyTypography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    padding: "{spacing.xxl} 0 {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Amber gold (`{colors.primary}`) fill with white text in `{typography.button-md}` at 600 weight, rounded to `{rounded.sm}` (8px). The ochre tone reads earned and kitchen-warm rather than generic CTA orange. Hover state darkens to `{colors.primary-active}`; disabled washes to `{colors.primary-disabled}`, keeping the amber family intact across all states. Sits at 48px tall to align with `text-input` in inline email-capture rows.

**`button-secondary`** — White canvas fill with a 1.5px hairline border and ink text. Used wherever a secondary action ("Compare materials," "Learn more") needs to coexist with `button-primary` without competing. Padding matches `button-primary` so the two sit at equal height (48px) without adjustment.

**`button-ghost`** — Transparent background, primary amber text, no border. Handles the lowest-hierarchy actions — "See all recipes," "View care guide" — where a filled button would overweight the surrounding content. No active state color change beyond opacity.

**`button-sm`** — Compact 36px amber button in `{typography.button-sm}`, rounded to `{rounded.xs}`. Used inside product cards, filter rows, or anywhere a full 48px button would crowd the layout.

### Navigation

**`nav-bar`** — 64px tall white bar with a 1px `{colors.hairline}` border below. Wordmark anchors left; a four-link set (Shop, About, Recipes, Care) runs center or right in `{typography.title-sm}` at weight 500; cart icon closes the far right. Stays white across all scroll positions — no color inversion on hero overlap.

**`announcement-bar`** — Dark charcoal strip (`{colors.accent-charcoal}`) pinned above the nav at 40px tall. Carries shipping thresholds or launch notices in `{typography.caption}` white, centered. Thin enough to read past without distraction, but persistent enough to land the offer.

### Product Discovery

**`product-card`** — Portrait 4:5 image sits above a two-line metadata row: product name in `{typography.title-sm}`, price in `{typography.price-display}`. No star ratings at the tile; reviews live on the product page. Card background is white (`{colors.surface-card}`) with `{rounded.md}` corners and `{spacing.base}` padding below the image. The warm canvas (`{colors.surface-warm}`) of the surrounding page creates gentle contrast without a drop shadow.

**`size-selector`** — Inline chip row for pan diameter (8", 10", 12"). Active chip fills `{colors.primary}` with `{colors.on-primary}` text; inactive chips show white with `{colors.hairline}` border. Rounded to `{rounded.xs}` to feel utilitarian rather than playful. Type in `{typography.body-sm}` — sized for scan, not emphasis. Chips wrap on narrow viewports.

**`material-badge`** — Pill (`{rounded.full}`) in `{colors.surface-soft}` carrying an uppercase material label ("CARBON STEEL," "CAST IRON"). Uses `{typography.overline}` at 11px/600 weight with 1.2px letter-spacing. Appears below the product title or overlaid on hero photography.

### Hero

**`hero`** — Warm cream background (`{colors.surface-warm}`) with a split-panel layout: headline and CTA left, full-bleed pan photography right. Headline in `{typography.display-xl}`, sub-head in `{typography.body-md}` at `{colors.body}`. Minimum height 560px on desktop. Photography always shows the pan in active use — oil slicked, not spotless — reinforcing the process-over-product editorial stance.

### Trust & Education

**`trust-strip`** — A full-width cream band (`{colors.accent-cream}`) placed immediately below the hero. Four icon-and-label pairs communicate functional specs: oven-safe temperature ceiling, pan weight, warranty length, pre-seasoned claim. Icons at 24px in `{colors.primary}`; labels in `{typography.body-sm}` body color. Hairline borders above and below separate it from adjacent sections without adding visual weight.

**`feature-icon-row`** — Loosely spaced icon columns (gap `{spacing.xl}`) used mid-page to elaborate on material properties or cooking advantages. Icon in `{colors.primary}` amber, label in `{typography.body-sm}`, supporting caption in `{typography.caption}` muted. Sits on the white canvas with no background fill; the color carry of the icon and the generous gap do all the separation work.

**`comparison-table`** — Three- or four-column table comparing cookware categories (Carbon Steel vs. Cast Iron vs. Stainless). Header row fills `{colors.accent-cream}`; the highlighted recommendation column fills `{colors.surface-soft}`. Cell borders in `{colors.hairline}`. Body type in `{typography.body-sm}`, column heads in `{typography.title-sm}`. Outer container rounds to `{rounded.md}`.

### Content Marketing

**`recipe-card`** — 16:9 image with an overline category label in `{typography.overline}` at `{colors.primary}`, title in `{typography.title-md}`. White card, `{rounded.md}` corners, `{spacing.base}` inner padding. Recipe content functions as material demonstration — every recipe implicitly shows off heat distribution or seasoning depth — so image quality is the card's primary job; metadata stays minimal.

### Forms

**`text-input`** — 48px-tall input with `{rounded.sm}` corners. Resting border in `{colors.hairline}`; focus ring shifts to `{colors.primary}` amber. Placeholder in `{colors.muted}`. Pairs with `button-primary` in inline email-capture rows at matched height so no vertical alignment adjustment is needed.

**`quantity-stepper`** — Plus/minus button pair flanking a centered count, all inside a `{colors.surface-soft}` container rounded to `{rounded.xs}`. Buttons 36px; typography in `{typography.title-sm}`. Used on product detail pages above the add-to-cart button.

### Footer

**`footer`** — Dark charcoal background (`{colors.accent-charcoal}`) with four content columns: Shop, Learn (care guides, material science), Company, Legal. Column headings in `{typography.title-sm}` white (`{colors.on-dark}`); link copy in `{typography.body-sm}` at `{colors.hairline}` tone. Vertical padding `{spacing.xxl}` top, `{spacing.xl}` bottom keeps the footer from feeling compressed against the preceding content section.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hero stacks vertically (image above, text below); nav collapses to hamburger + wordmark + cart; product grid drops to single column; trust-strip wraps to 2×2 icon grid; size-selector chips wrap; comparison table scrolls horizontally with pinned label column |
| Tablet | 744–1128px | 2-column product grid; hero shifts to 50/50 split panel; nav may show 3 primary links visible with overflow behind hamburger; trust-strip runs in a single 4-up row; feature-icon-row collapses to 2×2 |
| Desktop | 1128–1440px | 3-column product grid; full nav link set; hero at full 560px height with 50/50 split; comparison table fully visible without scroll |
| Wide | > 1440px | Content capped at ~1320px, page centered on `{colors.canvas}`; hero image can bleed edge if a full-width photo treatment is applied |

### Touch Targets

- All interactive controls minimum 44×44px; size-selector chips expand padding on mobile to meet this floor
- Cart and hamburger icons target 48×48px tap area even when visual icon renders smaller
- Quantity stepper buttons (36px visual) receive additional surrounding margin on mobile to prevent mis-taps
- Size-selector chips gain vertical padding from 8px to 12px on mobile

### Collapsing Strategy

- Nav collapses to hamburger at < 744px; "Shop" may persist as a visible text link beside the hamburger to preserve primary conversion path
- Announcement bar stays visible on mobile, text truncated to one short promotional phrase
- Comparison table becomes a swipeable horizontal scroll container below 744px, left label column pinned with `position: sticky`
- Feature icon row collapses from 4-across (desktop) to 2×2 grid (tablet) to stacked single-column list (mobile)
- Footer collapses from 4-column grid to 2-column at tablet, then single-column accordion (one section open at a time) at mobile
- Recipe card grid drops from 3-column to 2-column at tablet, 1-column at mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site injects design tokens via JavaScript or is behind anti-bot protection; all color values are estimated from the brand's warm amber/ochre identity and cookware photography aesthetic and must be verified against live CSS or a brand style guide before production use
- **No font stacks extracted** — font families are placeholder system sans-serif stacks; actual licensed typefaces (likely a geometric or humanist sans) should be confirmed by inspecting network waterfall requests or computed CSS `font-family` values on the live site
- **No meta theme-color** — browser chrome accent is unknown; browsers will fall back to white or the system default
- **Platform not confirmed Shopify** — component conventions (cart drawer, checkout flow, product page structure) are inferred from cookware DTC norms, not confirmed platform inspection
- **Border-radius values** — rounded scale uses standard 8px-grid increments; actual computed border-radius on buttons, cards, and inputs should be verified via browser DevTools
- **Spacing scale** — section padding and gap values are estimated at 8px-grid increments; actual values require CSS inspection of the live layout
- **Dark mode** — no evidence of a dark-mode variant was available; the `{colors.accent-charcoal}` surface is used only for announcement bar and footer, not a full dark theme
