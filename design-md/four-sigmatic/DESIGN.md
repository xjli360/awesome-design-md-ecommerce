---
version: alpha
name: "Four Sigmatic"
source_url: "https://foursigmatic.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every product in the Four Sigmatic lineup names its mushroom twice — once on the front panel in display type, once in a subhead reading like a formulation card: "Lion's Mane & Chaga, 250 mg each." That dual-naming convention shapes the UI system from the ground up: ingredient callout chips sit inside product cards the way nutrition facts sit on a label, not as decoration but as the primary decision lever. The brand's signature orange (#F0621E) is an earthy amber, far from the synthetic brights of sports nutrition; paired against a forest green (#2C5F2E) and an off-cream canvas (#FDF8F3), the whole palette reads like a field guide rather than a pharmacy shelf. Corners stay soft throughout — {rounded.md} on cards, {rounded.full} on benefit badges and pill CTAs — reflecting the organic positioning without sliding into rounded-corners-as-personality territory. Typography leans on a geometric sans-serif for display headings, stepped down to a comfortable readable weight at body scale; the brand's instructional voice demands long-form editorial treatment, so line-heights open up to 1.6 in body copy. Subscription framing is structurally embedded: every product card carries a "Subscribe & Save" toggle at the component level, not appended as an afterthought, and a clear visual grammar enforces the distinction — orange for one-time purchase, green for subscription. Educational modules occupy full-bleed sections with a surface-soft (#F5EDE4) background that warms the content without competing with product photography. The footer doubles as a content hub: newsletter signup, podcast links, and certifications (USDA Organic, Non-GMO Project Verified, Informed Sport) anchor every page with the same visual weight as primary navigation, because trust signals are a first-class product feature in the adaptogen category.

colors:
  primary: "#F0621E"
  primary-active: "#D5521A"
  primary-disabled: "#F9C4A6"
  secondary: "#2C5F2E"
  secondary-active: "#1E4820"
  mushroom-gold: "#C9952B"
  ink: "#1A1208"
  body: "#3D2B1F"
  muted: "#7A6558"
  hairline: "#DDD4CC"
  hairline-soft: "#EDE6DF"
  canvas: "#FDF8F3"
  surface-soft: "#F5EDE4"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  on-secondary: "#FFFFFF"
  on-dark: "#FFFFFF"
  badge-green-text: "#FFFFFF"
  star: "#C9952B"

typography:
  display-xl:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-lg:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  overline:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  badge-label:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  ingredient-callout:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'GT Walsheim', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
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
    rounded: "{rounded.xl}"
    padding: 14px 28px
    height: 52px
    hover:
      backgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: 14px 28px
    height: 52px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: 12px 26px
    height: 52px
    hover:
      backgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 8px 0
    borderBottom: "1px solid {colors.ink}"
  button-pill-green:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  subscribe-cta:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: 14px 28px
    height: 52px
    hover:
      backgroundColor: "{colors.secondary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 52px
    focus:
      border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoMaxHeight: 36px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.xxl}"
    columnGap: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    ingredientChipTypography: "{typography.ingredient-callout}"
    hover:
      border: "1px solid {colors.hairline}"
  subscribe-toggle:
    backgroundColor: "{colors.surface-soft}"
    selectedColor: "{colors.secondary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    toggleIndicator:
      backgroundColor: "{colors.canvas}"
      rounded: "{rounded.xs}"
  ingredient-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.ingredient-callout}"
    rounded: "{rounded.full}"
    padding: 4px 10px
    border: "1px solid {colors.hairline}"
  benefit-badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.badge-green-text}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-lg}"
    ctaSpacing: "{spacing.lg}"
    layout: split-50-50
    imageSide: right
    minHeight: 560px
  mushroom-callout-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-lg}"
    accentColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.xxl}"
    iconSize: 48px
    columns: 3
  educational-module:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    linkColor: "{colors.primary}"
    padding: "{spacing.section} 0"
    maxWidth: 760px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 10px {spacing.base}
    textAlign: center
  certification-strip:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
    iconSize: 40px
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
  review-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    starColor: "{colors.star}"
    bodyTypography: "{typography.body-sm}"
    authorTypography: "{typography.caption}"
  quiz-entry:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The main conversion button uses the brand's earthy amber (#F0621E) at 52px height with 28px horizontal padding and a 32px border radius (`{rounded.xl}`), sitting just short of full-pill to feel substantial rather than playful. Hover darkens to #D5521A with no shadow added, keeping the interaction flat and decisive. The disabled state uses a washed apricot (#F9C4A6) with white text.

**`button-secondary`** — An outlined variant in the same orange, used for secondary CTAs like "Learn More" on educational panels. Transparent background fills to `{colors.surface-soft}` on hover, maintaining warmth without a full color flip. Same height and radius as primary to keep the two peers visually matched.

**`button-ghost`** — Underline-only text button in ink (#1A1208), no background and no border radius. Deployed for in-paragraph links, "View all" affordances inside category sections, and inline navigation within educational copy.

**`subscribe-cta`** — Identical dimensions to `button-primary` but filled with forest green (#2C5F2E), reserved exclusively for subscription-tier actions. The orange/green grammar is the single most load-bearing visual decision in the system: every conversion surface uses one or both, and their pairing makes the subscription value proposition legible without a single word of explanation.

### Subscribe Toggle

**`subscribe-toggle`** — A two-state pill switch embedded in every product card and PDP, toggling between "One-time purchase" and "Subscribe & Save" modes. At rest the container background is `{colors.surface-soft}` with a white sliding indicator card. When subscription is selected, the outer container shifts to `{colors.secondary}` (green), reinforcing the subscription color grammar at the component level. Text labels update simultaneously with no animation delay.

### Navigation

**`nav-bar`** — A 68px fixed header on warm cream canvas, separated from page content by a hairline-soft bottom border. Logo sits left; category links (Mushroom Coffee, Protein, Bundles, Learn) center in 15px medium-weight type; cart and account icons right. On scroll the bar gains a subtle box shadow without changing background color. A dismissible `promo-banner` in primary orange sits above the nav and collapses it slightly on scroll.

**`mega-menu`** — Full-width dropdown triggered on category link hover, two columns: subcategory text links left, a featured product card with ingredient chips right. Background stays warm canvas; a hairline top border divides it from the nav bar. Keyboard navigation cycles through both columns before closing.

### Product Card

**`product-card`** — Square 1:1 product image above a white card body at `{rounded.md}`. Content order: image → benefit badges (max 3, green pills) → product name in `{typography.title-sm}` → ingredient chips row → price in `{typography.title-md}` → embedded `subscribe-toggle`. Border upgrades from hairline-soft to hairline on hover with no scale or shadow change. On mobile, ingredient chips scroll horizontally rather than wrapping.

### Ingredient Chip

**`ingredient-chip`** — A `{rounded.full}` label in warm cream with a thin hairline border and 13px semi-bold text, listing active ingredients with dosages (e.g., "Lion's Mane 500 mg", "Chaga 250 mg"). These appear inside product cards, as a horizontal scroll row on PDPs, and inside mega-menu featured cards. They are the information-dense alternative to marketing language.

### Benefit Badge

**`benefit-badge`** — Smaller pill in forest green (#2C5F2E) with white 11px bold text carrying functional claim labels: "Focus", "Calm", "Energy", "Immunity". Maximum 3 per product to prevent credential overload. Appears above product names in cards and at the top of hero sections. Never used as CTAs — interaction belongs to buttons only.

### Hero Banner

**`hero-banner`** — A 50/50 split layout at a minimum 560px height: product photography fills the right half edge-to-edge, while the left half carries the headline at `{typography.display-xl}` (52px, −0.5px tracking), a benefit subhead at `{typography.body-lg}` (18px, 1.6 line-height), and two stacked CTAs — primary orange and secondary outlined — separated by `{spacing.lg}`. Background stays canvas (#FDF8F3) so photography provides all color saturation without a colored overlay competing with product imagery.

### Mushroom Callout Section

**`mushroom-callout-section`** — A full-bleed section on `{colors.surface-soft}` explaining individual mushroom benefits in a 3-column grid of icon + heading + body copy. Icons are 48px line-style illustrations in earthy tones. Heading at `{typography.display-sm}`, body at `{typography.body-lg}` with generous 1.6 line-height. The accent color (`{colors.primary}`) appears in icon stroke or a thin top rule per column, never in background fills.

### Educational Module

**`educational-module`** — A narrow single-column reading layout (max-width 760px, centered) for long-form content: study citations, ingredient science explainers, founder essays. Heading `{typography.display-md}`, body `{typography.body-md}` at 1.6 line-height. Background `{colors.surface-soft}`. Inline links to cited studies use `{colors.primary}`. No sidebar, no pull quotes — editorial restraint signals scientific credibility.

### Certification Strip

**`certification-strip`** — A horizontal row of trust-mark icons (USDA Organic, Non-GMO Project Verified, Informed Sport, Vegan, Gluten-Free) with `{typography.caption}` labels in muted color beneath each. Appears above the footer on every page and below the add-to-cart button on PDPs. Icons are 40px; the strip carries a top hairline border and `{spacing.xl}` vertical padding.

### Review Card

**`review-card`** — White card at `{rounded.md}` with a thin hairline-soft border. Star row in mushroom gold (#C9952B) at top, followed by review body in `{typography.body-sm}`, author name and verified purchase label in `{typography.caption}`. Cards sit in a 3-column grid on desktop, a 2-column grid on tablet, and a horizontal scroll row on mobile. No truncation on desktop — the brand's testimonials run long and that length is intentional.

### Quiz Entry

**`quiz-entry`** — A large rounded panel (`{rounded.lg}`) in `{colors.surface-soft}` inviting users into a mushroom-finder quiz. Heading at `{typography.display-sm}`, single sentence of supporting copy in `{typography.body-md}`, and a primary orange CTA button. Used as a mid-page module between the product grid and educational sections on the homepage and category pages.

### Footer

**`footer`** — Deep ink (#1A1208) background with white type. Four-column link grid on desktop: Shop, Learn, Company, Social. Newsletter email input embedded in the top-right column with a `{rounded.xl}` pill input and orange submit button. Certification strip appears in `{colors.muted}` above the footer divider. Bottom bar carries legal links and copyright in `{typography.caption}` at 60% opacity. On mobile the link columns collapse to accordions with chevron toggles.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks vertically (image above, text below); product grid 1-column; ingredient chips scroll horizontally; subscribe toggle spans full width; nav collapses to hamburger; mega-menu becomes full-screen slide-in drawer |
| Tablet | 744–1128px | 2-column product grid; hero shifts to 40/60 text/image split; mushroom callout section drops to 2 columns; footer collapses to 2-column link grid; mega-menu becomes a 1-column dropdown |
| Desktop | 1128–1440px | Full 4-column product grid; 50/50 hero; 3-column mushroom callout; footer 4-column layout; full mega-menu with featured product card |
| Wide | > 1440px | All content max-width 1440px with symmetric auto margins; hero image scales via object-fit cover without stretching; section padding increases by 1.5× |

### Touch Targets

- All primary and secondary buttons minimum 52px height; full-width on mobile viewports
- Subscribe toggle: minimum 44px height per tap zone; both states tap-accessible
- Hamburger nav icon: 44×44px tap target with 8px padding inset
- Cart and account icons padded to 44×44px tap area regardless of icon render size
- Ingredient chips: minimum 36px height; horizontal scroll row prevents crowding on narrow screens
- Benefit badges are display-only and carry no tap affordance

### Collapsing Strategy

- Footer link columns collapse to accordions (chevron toggle, full-width tap target) on mobile; newsletter signup moves to top of footer above the accordions
- Mega-menu becomes a full-screen slide-in drawer with a back-arrow header on mobile, preserving the two-level hierarchy without nested dropdowns
- Certification strip reflows from a single horizontal row to a 3×2 icon grid on mobile rather than horizontal scroll, keeping all marks visible without interaction
- Educational module stays single-column at all breakpoints; display heading steps down from `{typography.display-md}` (32px) to `{typography.display-sm}` (24px) on mobile
- Review cards shift from 3-column grid → 2-column grid → horizontal scroll container across desktop → tablet → mobile; no truncation at any breakpoint
- Mushroom callout section: 3 columns on desktop, 2 on tablet, 1 stacked on mobile with icon centered above copy

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (empty extraction result); all color values above are inferred from Four Sigmatic's widely documented visual brand identity and may not match the current production palette exactly
- No font stacks were detected; "GT Walsheim" is used as a plausible geometric sans-serif based on the brand's visual character, but the actual licensed typeface and fallback stack are unverified
- No meta theme-color was captured; the warm cream canvas (#FDF8F3) is inferred from recurring brand photography backgrounds, not a direct computed-style extraction
- Typography scale sizes, weights, and letter-spacing values are approximated from visual observation of brand materials, not extracted from computed styles
- Platform was not confirmed as Shopify (extraction flagged false); component architecture — particularly subscription toggle implementation — may differ on a custom or headless stack
- Dark mode support is unknown; the warm-canvas orientation suggests it may not be implemented
- Animation and transition specs (hover durations, drawer easing, toggle slide timing) could not be extracted and are omitted rather than guessed
- Exact subscription discount percentage shown in the toggle label is unverified (commonly 15–20% in the adaptogen category but not confirmed for this brand)
- Mobile navigation structure (number of top-level items, whether "Learn" is a mega-menu or a flat link) is inferred from desktop patterns and may differ in the live implementation
