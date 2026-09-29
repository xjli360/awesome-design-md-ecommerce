---
version: alpha
name: "Pristine Marketplace"
source_url: "https://www.pristinemarketplace.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The authentication economy runs on trust signals, and Pristine Marketplace builds its visual vocabulary around two competing anchor hues — deep crimson (#8a2432) and muted teal (#108474) — a pairing uncommon in sports memorabilia retail, where navy dominates. Crimson owns the primary CTAs and brand marks, while teal claims confirmation states, secondary actions, and authentication badges, giving the interface two clear lanes of user intent without defaulting to a monochromatic hierarchy. Gold (#fbcd0a) functions as a third voltage, appearing on championship-tier items, featured seller badges, and star-rating fills via the JudgemeStar font stack — a typographic flourish that ties the review system visually to the product it scores. Montserrat carries all display and body copy at weights ranging from 400 to 700; its geometric evenness keeps product titles readable at compressed card widths where signed memorabilia descriptions tend to run long. Times appears as a serif counterpoint in editorial contexts — provenance copy, signature authentication descriptions, and pullquote treatments — lending the patina of a printed catalog to what is otherwise a clean digital marketplace. The neutral field is a dense stack of near-identical off-whites (#f9f9f9, #fafafa, #f7f7f7) and hairline grays (#e6e6e6, #e1e1e1, #dadada), which collectively suppress visual noise so signed item photography — almost always shot against white — lands cleanly in the card grid. Orange (#ff580d) emerges only at the margin: flash-sale overlays and urgency nudges where Pristine Marketplace needs to convert scarcity into velocity. Buttons use `{rounded.sm}` throughout, cards hold at `{rounded.md}`, and the search bar sits at `{rounded.full}`, producing a domestic friendliness that softens what is fundamentally a premium authentication marketplace.

colors:
  primary: "#8a2432"
  primary-active: "#6b1a26"
  primary-disabled: "#c4909a"
  secondary: "#108474"
  secondary-active: "#0d6b5e"
  secondary-disabled: "#7bbdb7"
  accent-gold: "#fbcd0a"
  accent-orange: "#ff580d"
  ink: "#1a1a1a"
  body: "#444444"
  muted: "#7b7b7b"
  muted-soft: "#b7b7b7"
  hairline: "#e1e1e1"
  hairline-soft: "#eeeeee"
  hairline-strong: "#dadada"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#f7f7f7"
  surface-teal-wash: "#edf5f5"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  on-gold: "#1a1a1a"
  star-fill: "#fbcd0a"
  star-empty: "#e6e6e6"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  editorial:
    fontFamily: "Times, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.1px
  editorial-sm:
    fontFamily: "Times, 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  price-lg:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  price-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  badge-label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.5px
    textTransform: uppercase
  star-icon:
    fontFamily: "JudgemeStar, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.secondary-active}"
    textColor: "{colors.on-secondary}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    typography: "{typography.body-md}"
    focusBorderColor: "{colors.secondary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    searchIconColor: "{colors.muted}"
    submitButtonBackground: "{colors.primary}"
    submitButtonTextColor: "{colors.on-primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 36px
    activeTextColor: "{colors.primary}"
    dropdownBackground: "{colors.canvas}"
    dropdownBorderColor: "{colors.hairline}"
  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "1px solid {colors.hairline}"
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.md}"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-md}"
    priceColor: "{colors.primary}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    padding: "{spacing.base}"
    imageAspectRatio: "3/4"
    shadow: "0 1px 4px rgba(0,0,0,0.06)"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.10)"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.editorial}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    ctaBackground: "{colors.accent-gold}"
    ctaTextColor: "{colors.on-gold}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.sm}"
    overlayOpacity: 0.4
  badge-authenticated:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-featured:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  star-rating:
    filledColor: "{colors.star-fill}"
    emptyColor: "{colors.star-empty}"
    typography: "{typography.star-icon}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  authentication-seal:
    backgroundColor: "{colors.surface-teal-wash}"
    borderColor: "{colors.secondary}"
    borderWidth: 1px
    textColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.base}"
    iconColor: "{colors.secondary}"
  provenance-block:
    backgroundColor: "{colors.surface-soft}"
    borderLeft: "3px solid {colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.editorial-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  price-display:
    currentPriceTypography: "{typography.price-lg}"
    currentPriceColor: "{colors.primary}"
    originalPriceTypography: "{typography.body-sm}"
    originalPriceColor: "{colors.muted-soft}"
    originalPriceDecoration: line-through
    savingsColor: "{colors.accent-orange}"
    savingsTypography: "{typography.badge-label}"
  trust-strip:
    backgroundColor: "{colors.surface-teal-wash}"
    textColor: "{colors.secondary}"
    typography: "{typography.caption}"
    iconColor: "{colors.secondary}"
    padding: "{spacing.md} 0"
    borderTop: "1px solid {colors.secondary-disabled}"
    borderBottom: "1px solid {colors.secondary-disabled}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"
    newsletterInputBackground: "{colors.canvas}"
    newsletterButtonBackground: "{colors.primary}"
    newsletterButtonTextColor: "{colors.on-primary}"

## Components

### Buttons
**`button-primary`** — Crimson (#8a2432) fill with white Montserrat text at 14px/600 uppercase, 4px radius, 44px tall. Hover darkens to `{colors.primary-active}` (#6b1a26), preserving contrast without a border shift. Disabled state washes out to `{colors.primary-disabled}`, a dusty rose that signals inactivity clearly without hard graying.

**`button-secondary`** — Teal (#108474) fill with white text, identical sizing and radius to `button-primary`. Teal handles confirmation-lane actions — "Add to Watchlist," verification CTAs, seller contact — while crimson holds commerce primacy. Hover deepens to `{colors.secondary-active}`.

**`button-outline`** — Transparent background with a 1.5px crimson border and crimson text in the same uppercase Montserrat treatment. Used where a filled button would overpower a light surface, such as filter panels or secondary PDP actions.

**`button-ghost`** — Text-only, 12px muted gray Montserrat, no border or fill. Applied to dismiss links, "See all" secondary navigation, and low-stakes inline actions.

### Search Bar
**`search-bar`** — Pill-shaped (`{rounded.full}`), 44px tall, with a magnifying glass icon in `{colors.muted}` on the left. A small crimson submit button caps the right terminus inside the pill, creating a contained search-and-go affordance. Focus ring expresses as a teal border, connecting focus state to the secondary action color system.

### Navigation
**`nav-bar`** — 64px white header with a 1px `{colors.hairline-soft}` underrule. Logo sits left at 36px height. Category links render in 13px/600 Montserrat; the active item underlines in crimson. The search bar occupies center. Cart, account, and wishlist icons cluster right. Hover-triggered dropdowns appear on white with hairline border and `{rounded.sm}` corners.

**`category-nav`** — A secondary 44px strip in `{colors.surface-soft}` immediately below the main nav, housing sport and culture tabs (Baseball, Football, Basketball, Pop Culture, etc.). Active tab shows a 2px crimson bottom border with crimson text; all inactive tabs render in `{colors.body}`. Horizontally scrollable on narrower viewports.

### Product Cards
**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.md}` corners, lifting to a more pronounced shadow on hover. Item photography fills a 3:4 aspect container at the top. Below the image: item title in `{typography.title-sm}`, signer name in `{typography.body-sm}` muted gray, a star rating row with JudgemeStar glyphs filled gold, then the ask price in crimson `{typography.price-md}`. A `badge-authenticated` teal chip may overlay the top-left image corner on certified listings.

### Badges
**`badge-authenticated`** — Teal fill, white 11px/700 uppercase Montserrat, 2px radius, 3px/8px padding. The semantically weightiest badge in the system — applied only to listings with a verified COA. **`badge-featured`** — Gold (#fbcd0a) fill with dark `{colors.on-gold}` text, signaling editor-curated or premium placement. **`badge-sale`** — Orange (#ff580d) fill for price-reduction urgency. **`badge-new`** — Crimson fill for newly listed items. All four share identical geometry; color alone carries the semantic differentiation.

### Authentication Seal
**`authentication-seal`** — A teal-washed panel (`{colors.surface-teal-wash}`) with a 1px teal border and `{rounded.md}` corners. Houses a shield or checkmark icon, "Certificate of Authenticity" heading, and authenticator attribution in `{typography.body-sm}`. Appears on every PDP below the add-to-cart zone; it is the primary trust anchor of the product page and should never be collapsed or deprioritized on mobile.

### Provenance Block
**`provenance-block`** — A left-bordered editorial inset with a 3px crimson rule and `{colors.surface-soft}` background, using Times for the body copy in `{typography.editorial-sm}`. Describes where the item was signed — the event, location, and chain of custody — in a register that reads like a printed auction note. The serif type creates tonal separation from surrounding Montserrat marketing copy.

### Price Display
**`price-display`** — Current price in crimson `{typography.price-lg}` (24px/700). On sale, the original price appears struck-through in `{colors.muted-soft}` at `{typography.body-sm}`, with a savings callout label in `{colors.accent-orange}` using `{typography.badge-label}` — the only place orange appears outside the flash-sale badge context.

### Hero
**`hero`** — Full-width crimson panel with white headline (`{typography.display-xl}`) and a Times serif subtitle (`{typography.editorial}`). Minimum 480px height with athlete or item photography filling the right half behind a 0.4 scrim. The CTA button uses `{colors.accent-gold}` fill with `{colors.on-gold}` dark text — the only instance where gold fills an interactive element rather than a passive badge, creating a high-contrast focal point against the crimson field.

### Trust Strip
**`trust-strip`** — A narrow teal-wash band spanning full width between the hero and the product grid, carrying three icon-and-caption trust claims: "100% Authentic," "COA Included," "Expert-Verified." Teal icons and 12px Montserrat captions, evenly spaced with consistent horizontal gap. The strip is bordered top and bottom with `{colors.secondary-disabled}` lines, framing it as a distinct informational tier.

### Star Rating
**`star-rating`** — Five JudgemeStar glyphs at 16px, filled gold for earned rating and `{colors.star-empty}` gray for remainder. Review count appears to the right in 12px muted Montserrat. On product cards the stars render at 14px; on the PDP they expand to 16px with a visible linked count. The JudgemeStar font implies Judge.me app integration rather than native Shopify ratings.

### Footer
**`footer`** — Near-black (`{colors.ink}`) background anchored by a 3px crimson top border — the brand's primary color reappearing as a structural accent that visually grounds the page bottom to the header. Column headings in white `{typography.title-sm}`, body links in `{colors.hairline-soft}` fading to white on hover. A newsletter subscription input and crimson submit button appear in the rightmost column, maintaining the primary action color system even at the page's far edge.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category-nav collapses to horizontal scroll strip; search bar expands full-width below logo row; hero stacks text above photography; nav-bar reduces to logo + hamburger + cart icon |
| Tablet | 744–1128px | Two-column product grid; category-nav visible as horizontally scrollable strip; hero maintains side-by-side at reduced padding; secondary nav links may truncate to icon-only with tooltips |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with all category links; hero at full 480px min-height with right photography panel; authentication-seal renders as a horizontal row on PDP |
| Wide | > 1440px | Layout constrained to ~1440px max-width centered on canvas; product grid holds at four columns; hero expands photography region while text column stays fixed width |

### Touch Targets
- All buttons and nav links minimum 44px tall on mobile
- Product card tap target spans the full card face including the image region
- Filter and category badge tap targets padded to 36px minimum height
- Cart, account, and wishlist icons in mobile nav padded to 44×44px touch areas
- Star rating row tap area expands to full row height for review navigation

### Collapsing Strategy
- Category-nav becomes a single-row horizontal scroll on tablet and mobile with a hidden scrollbar and fade-out edge gradient
- Main nav hamburger reveals a slide-in drawer with full category tree, search bar, and account links
- Product card titles truncate to two lines via `line-clamp: 2`; signer name to one line
- Authentication-seal collapses from a horizontal three-column layout to a stacked vertical block on mobile
- Trust-strip collapses from three-column icon-caption pairs to a single scrolling row on mobile below 480px
- Provenance block collapses to a "Read more" toggle on mobile to preserve above-the-fold PDP real estate

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Ink/primary text hex not present in extracted palette; `{colors.ink}` set to #1a1a1a as a reasonable dark default — actual value may differ
- Canvas white (#ffffff) not in extracted list (filtered as a framework default); assumed standard white throughout
- No standalone heading or display font beyond Montserrat detected; Times may be limited to body editorial copy rather than display-size headline use
- Exact nav-bar height, button padding, and input dimensions not extractable from color/font meta alone — values estimated from Shopify marketplace conventions
- JudgemeStar is a review-widget icon font; whether ratings are powered by the Judge.me app or another provider is unconfirmed, though the font name strongly implies Judge.me
- No dark mode palette detected; all surfaces assumed light-mode only
- Mobile breakpoint thresholds are estimated; actual Shopify theme breakpoints may differ from the values above
- Logo mark dimensions, wordmark lockup, and favicon palette not extractable from color/font extraction data
- Whether the orange (#ff580d) accent appears in the nav or only in promotional overlays could not be confirmed from static extraction
