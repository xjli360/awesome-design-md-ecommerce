---
version: alpha
name: "Branch Furniture"
source_url: "https://www.branchfurniture.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Branch's most telling commitment is color-architectural: the meta theme-color (#314438), the primary CTA fill, the mobile nav drawer background, and the wordmark are all the same deep forest green — not color-coordinated, but literally the same value, as though the brand picked one hex before opening any design tool. That green never reads outdoors or environmental; it reads like the color of a room where serious work happens, closer to a London club library than a forest trail. The warm-white canvas (#faf8f4) and aged-linen surface (#f3eeea) prevent the palette from going cold or corporate, while a muted sage bridge (#9fb59e) appears in swatch selectors, hover states, and secondary fills to keep forest and cream in quiet conversation. When the brand needs temperature contrast it reaches for a sun-dried terracotta (#da5f4d) — not a conventional e-commerce red but something closer to a clay pot on a concrete windowsill — reserving it for promotional banners, urgency badges, and review star fills rather than letting it anywhere near primary navigation. Frank Ruhl Libre, a serif with visible ink traps and old-style proportions, carries every display headline: an atypical choice for DTC furniture commerce where geometric grotesques dominate, but one that positions Branch alongside interior design editorial rather than big-box retail. Quicksand manages all body copy and UI labels with its rounded terminals, providing an approachable counterweight to the serif gravity above. Koulen, a condensed all-caps display face, surfaces in hero category stamps and collection badges — giving the brand a way to assert scale or urgency without a weight change or added visual mass. Corner radii stay deliberately restrained throughout: product cards and primary buttons share a 6px curve, the brand avoids pill shapes for standard CTAs, and the palette is left to carry the expressive weight that other brands assign to geometry. The configurator experience — desk dimensions, finishes, add-on shelving — is Branch's signature interaction: a card-select grid where a 2px forest-green border rings chosen options tightly while hairline-bordered inactives recede into the warm canvas, the whole surface sitting on the linen {colors.surface-soft} background. On mobile, the nav collapses into a full-height drawer in {colors.primary} with white-reversed type — the clearest signal that forest green is the brand's structural element, not merely a button fill.

colors:
  primary: "#314438"
  primary-hover: "#3d5546"
  primary-active: "#253630"
  primary-disabled: "#9fb59e"
  accent: "#da5f4d"
  accent-hover: "#c54f3d"
  accent-soft: "#f5d8d3"
  teal: "#00caaa"
  sky: "#8cc1d2"
  ink: "#212225"
  body: "#4b4e53"
  muted: "#6b6b6b"
  muted-light: "#848484"
  slate: "#676986"
  navy: "#272d45"
  sage: "#9fb59e"
  hairline: "#d3d2d0"
  hairline-soft: "#e5e5e5"
  canvas: "#faf8f4"
  surface-soft: "#f3eeea"
  surface-card: "#f9f9f9"
  surface-sage: "#d6dad7"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 52px
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  hero-stamp:
    fontFamily: "'Koulen', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  category-tag:
    fontFamily: "'Koulen', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  title-md:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 4px
  sm: 6px
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
    padding: "12px 24px"
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "11px 23px"
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-sage}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "0px"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    scrollShadow: "0 2px 8px rgba(33,34,37,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspect: "3/2"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    hoverShadow: "0 4px 16px rgba(49,68,56,0.10)"
  hero-section:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    subColor: "{colors.body}"
    stampTypography: "{typography.hero-stamp}"
    stampColor: "{colors.primary}"
    layout: "split-right-image"
    maxWidth: 1440px
    padding: "80px 64px"
  product-configurator:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    optionSelectedBorder: "2px solid {colors.primary}"
    optionInactiveBorder: "1px solid {colors.hairline}"
    optionSelectedBackground: "{colors.canvas}"
    optionSelectedLabel: "{colors.primary}"
    optionInactiveLabel: "{colors.body}"
    padding: "{spacing.lg}"
    stepHeadingTypography: "{typography.title-md}"
  trust-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    accentColor: "{colors.accent}"
    height: 44px
    padding: "0 {spacing.xl}"
    iconSize: 18px
  promo-banner:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    closeIconColor: "{colors.on-primary}"
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.category-tag}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.surface-sage}"
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.category-tag}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  review-stars:
    activeColor: "{colors.accent}"
    inactiveColor: "{colors.hairline}"
    countTypography: "{typography.caption}"
    countColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-sage}"
    linkHoverColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption}"
    columns: 4
  mobile-nav-drawer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    width: "100vw"
    sectionDividerColor: "{colors.sage}"
    closeIconColor: "{colors.on-primary}"

## Components

### Buttons

**`button-primary`** — Forest green (#314438) fill with a white Quicksand Bold label at 15px and 0.3px tracking; 6px corner radius, 48px tall. Hover darkens to #3d5546, active deepens further to #253630, and disabled surfaces the sage tone (#9fb59e) as fill — keeping the green family present while signaling unavailability without using gray. This button carries every primary commerce action: Add to Cart, Configure, Shop Now.

**`button-secondary`** — Warm canvas (#faf8f4) fill with a 1.5px forest-green stroke and matching text color; mirrors the primary in radius and height for compositional pairing. Hover shifts the fill to surface-sage (#d6dad7) without disturbing the border. Used alongside the primary button on configurator sidebars, comparison modules, and editorial CTAs where two parallel actions have equal weight.

**`button-accent`** — Terracotta (#da5f4d) fill, white Quicksand Bold label; same 48px height and radius as primary. Hover steps down to #c54f3d. Reserved strictly for promotional contexts, urgency CTAs ("Shop the Sale", "Limited Stock"), and any surface where primary green would blend into a green background.

**`button-ghost`** — Transparent, borderless, underlined Quicksand Bold at 13px in ink (#212225). Used for secondary text-link actions inside product descriptions, review prompts, and footer utility links where a boxed button would add visual weight without adding hierarchy.

### Form Inputs

**`text-input`** — 48px tall on the warm canvas background, 1px hairline border (#d3d2d0) at 4px radius, Quicksand 16px body copy. Focus upgrades to a 1.5px forest-green ring. Placeholder text in muted (#6b6b6b). Applied in email capture bars, checkout address fields, and the workspace quiz flow.

### Navigation

**`nav-bar`** — 68px tall, warm canvas background with a subtle hairline bottom border. The Branch wordmark renders in forest green at far left; center navigation links use Quicksand SemiBold 14px with 0.3px tracking in ink. Right slot carries a cart icon and a compact `button-primary`. On scroll, a soft box shadow (0 2px 8px rgba(33,34,37,0.08)) emerges from beneath the bar without changing the background color.

**`mobile-nav-drawer`** — Full-height, full-width overlay in forest green (#314438), the brand's most committed application of primary-as-architecture. Navigation links in Quicksand Bold 15px white, section dividers in sage (#9fb59e) at low opacity. A white × icon closes the drawer top-right. Sub-category accordions expand inline rather than pushing to a second panel.

### Product Components

**`product-card`** — 3:2 image aspect ratio on a #f9f9f9 card surface with 6px corner radius. Product name in Quicksand Bold 15px, price in Frank Ruhl Libre 20px (the serif weight creates subtle editorial contrast with the sans label above), and a Koulen uppercase category tag overlaid bottom-left on the image in a translucent forest-green strip. Hover elevates with a forest-green-tinted shadow (0 4px 16px rgba(49,68,56,0.10)) — no image zoom, no border change.

**`product-configurator`** — Branch's signature UI component: a step-through card-select grid sitting on a warm linen (#f3eeea) surface. Each option renders as a white card with a hairline border in resting state; selection stamps a 2px forest-green border around the card and pulls the label to primary green. Step headings use Quicksand Bold 18px; option labels use Quicksand caption. A summary sidebar on desktop recaps selections with a full-width `button-primary` anchored at bottom. On mobile the grid collapses to a horizontally scrolling row of option chips.

### Brand Fixtures

**`hero-section`** — Split desktop layout: Frank Ruhl Libre display headline at 52px sits left at 1.08 line height, lifestyle product photography fills the right half to the container edge. A Koulen uppercase stamp ("THE HOME OFFICE DESK", "AS SEEN IN WIRED") sits above the headline in forest green at 13px with 1.5px letter-spacing. Body copy in Quicksand 16px at 1.6 line height, muted body-gray. Primary CTA anchors the text block with standard 48px height.

**`trust-bar`** — 44px strip in forest green (#314438) pinned directly below the nav bar. Three trust propositions (free shipping, 30-day home trial, lifetime warranty) rendered in Quicksand 14px white, each prefixed by an 18px icon with terracotta fill for the accent color. The strip scrolls with the page on mobile at full width.

**`promo-banner`** — 36px announcement bar in terracotta (#da5f4d) sitting above the nav bar. White Quicksand caption text centered; a white × dismiss icon at far right. The terracotta at this position is the first thing a visitor sees, anchoring the brand's sale or launch message before the forest-green nav takes over.

**`category-badge`** — Small rounded-xs label on the warm surface background; forest-green Koulen uppercase type at 11px with 1.2px tracking, outlined by a sage hairline border. Appears on collection page filter rows and product card overlays to segment desk types (Standing Desk, L-Shaped, Corner, Bundle).

**`sale-badge`** — Terracotta fill, white Koulen uppercase at 11px, 4px radius. Applied top-left on product card images during promotional events; never used for non-sale information to preserve the signal.

**`review-stars`** — Five-star row filled in terracotta for active stars, hairline gray for inactive. Review count in Quicksand caption 12px in body-gray. The terracotta star color mirrors the badge and banner system, tying social proof visually to the brand's warmth register rather than to conventional gold or yellow star systems.

**`footer`** — Dark navy (#272d45) background creates a clean dark terminus after the warm-white body, requiring no top border to separate. Four-column link grid on desktop: column heads in Quicksand Bold 12px with 0.2px tracking in sage-gray (#d6dad7); links in Quicksand 14px sage-gray that step to full white on hover. No forest green appears here — the navy registers as a separate architectural zone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks image above text block; nav collapses to hamburger + full-height forest-green drawer; configurator becomes a horizontal scroll-snap card row; trust-bar collapses to a single scrolling marquee |
| Tablet | 744–1128px | Two-column product grid; hero retains split layout at reduced padding (40px); nav shows primary links inline, secondary links in a dropdown; configurator expands to a 2-column card grid with summary panel below |
| Desktop | 1128–1440px | Three-column product grid; full hero split at 80px section padding; five-link nav with cart and CTA button; configurator shows four-column card grid with sticky summary sidebar |
| Wide | > 1440px | Content max-width 1440px centered with wider gutters; hero product image extends to the container edge; product grid holds at three columns; section padding increases to ~96px |

### Touch Targets
- All buttons minimum 48px tall × 44px wide
- Mobile nav drawer links minimum 52px tall for comfortable thumb tap across the full green surface
- Configurator option cards minimum 72px tall on mobile to prevent accidental mis-selection
- Review star touch zone expanded to 32px height even at 16px visual render size
- Promo-banner dismiss × minimum 44×44px tap area regardless of visual icon size

### Collapsing Strategy
- Navigation: full five-link bar → hamburger trigger at < 744px; drawer slides from left in forest green with white type
- Product grid: 3-col → 2-col at 744px → 1-col at < 480px
- Hero: side-by-side split → stacked image-first at < 744px; headline drops from 52px to 32px (display-md)
- Configurator: card grid → horizontal scroll-snap chips at < 744px; summary sidebar moves below the option grid
- Trust bar: three static items → single scrolling marquee at < 480px
- Footer: four columns → two columns at 744px → single-column accordion at < 480px; column heads become tap-to-expand toggles

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Motion and animation tokens (hover transition curves, configurator step transitions, drawer slide timing) not extractable from static analysis
- Exact button height and padding values unconfirmed from live DOM; 48px height is inferred from DTC norms and visual inspection
- Frank Ruhl Libre weight distribution across heading levels not fully confirmed; weight 600 across all display sizes is inferred from visual hierarchy rather than CSS inspection
- Koulen usage scope unclear — may be limited to specific hero modules or a single campaign rather than a systematic badge and stamp system
- Icon set and glyph library unidentified; no SVG sprite or icon font found in extraction beyond the OKendo review widget icon font
- Teal (#00caaa) and sky blue (#8cc1d2/#8dc0d2) placement unclear — likely used in chatbot widget (e.g. Gorgias) or third-party overlay rather than core brand UI; not assigned to brand tokens
- Dark-mode support not confirmed; no dark-surface or inverted color tokens extracted
- Exact nav bar height unconfirmed from live DOM; 68px is estimated from screenshot analysis
- Koulen font weight: the font is a single-weight display face (400 only) — no bold variant exists, which affects any component spec that might expect bold display stamps
