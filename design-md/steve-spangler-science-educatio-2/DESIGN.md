---
version: alpha
name: "Steve Spangler Science"
source_url: "https://www.stevespanglerscience.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  #ff7700 orange arrives on the Steve Spangler Science site the way a Van de Graaff generator discharges — sudden, impossible to ignore, and entirely deliberate. Every primary action button, promotional callout, and sale indicator fires in this single frequency, set against a #282f37 charcoal navigation bar thick enough to anchor the energy without absorbing it. The canvas beneath opens to #f3f2f7, a faint lavender-white that positions product photography — mid-pour liquids, billowing chemical fog, color-changing crystals — as the actual selling surface. The visual grammar owes less to lifestyle retail than to the science fair: orange is the ignition, darkness is the void before the experiment starts, and the product image is the reaction. Age-range pills ({rounded.full}, solid #ff7700) floating on kit cards are the primary scanning signal parents use before reading any copy. Grade-level context arrives in #003388 navy pills, the brand's secondary authority color, carrying the curriculum-alignment cue that teachers and homeschool buyers need. Typography runs in a clean, accessible sans-serif hierarchy with no display theatrics — legibility matters more than style when the audience spans third-graders and their parents simultaneously. The broader extracted palette contains a recognizable cluster of WordPress Gutenberg block-editor defaults — #9b51e0 purple, #7bdcb5 mint, #cf2e2e red — accumulated across years of experiment and blog content rather than reflecting structural brand decisions. The load-bearing system is tighter: #ff7700 for every action, #282f37 for every container that needs weight, #f3f2f7 for breathing room, and #003388 when the brand needs to read as credible rather than exuberant.

colors:
  primary: "#ff7700"
  primary-hover: "#ff6900"
  primary-active: "#e06500"
  primary-disabled: "#ffcc99"
  accent-blue: "#003388"
  accent-blue-mid: "#015692"
  accent-blue-bright: "#4592fe"
  accent-green: "#116600"
  accent-green-bright: "#9aa600"
  accent-coral: "#df653e"
  ink: "#222222"
  body: "#444444"
  muted: "#555555"
  hairline: "#e9e9eb"
  hairline-soft: "#f3f2f7"
  canvas: "#ffffff"
  surface-soft: "#f3f2f7"
  surface-card: "#ffffff"
  dark-nav: "#282f37"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link-on-dark: "#7fa9c5"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
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
    padding: "12px 24px"
    height: 44px
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
    border: "2px solid {colors.primary}"
    padding: "10px 22px"
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.on-dark}"
    padding: "10px 22px"
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 14px"
    height: 44px
  text-input-focus:
    border: "1px solid {colors.primary}"
    outline: "2px solid rgba(255, 119, 0, 0.2)"
  nav-top-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  nav-bar:
    backgroundColor: "{colors.dark-nav}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonRounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "1 / 1"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.07)"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
  product-card-hover:
    boxShadow: "0 6px 20px rgba(0,0,0,0.13)"
    transform: "translateY(-2px)"
  age-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  grade-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  sale-badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  new-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.dark-nav}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    overlayGradient: "linear-gradient(90deg, rgba(40,47,55,0.88) 40%, transparent 80%)"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
  experiment-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    accentBarHeight: 4px
    accentBarColor: "{colors.primary}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 14px"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: "6px 14px"
  footer:
    backgroundColor: "{colors.dark-nav}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.link-on-dark}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    borderTop: "4px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Solid #ff7700 orange block with bold white text and 8px corner radius. Hover brightens to #ff6900; active press deepens to #e06500; disabled state washes out to a pastel #ffcc99. This is the single highest-frequency element on the site — every add-to-cart, checkout, and experiment download action routes through this orange.

**`button-secondary`** — White fill with a 2px #ff7700 border and matching orange text. Deploys on white-canvas sections where a full orange fill would crowd the signal. Hover softens the fill to #f3f2f7.

**`button-ghost-dark`** — Transparent background with 2px white border and white type, used exclusively over the dark #282f37 hero and nav zones where the orange-on-dark pairing would read as fire rather than a CTA.

### Inputs

**`text-input`** — 44px height, 1px #e9e9eb hairline border on white. Focus ring applies a 2px soft orange glow (`rgba(255, 119, 0, 0.2)`) that keeps the brand color present at interaction points without hard contrast. Placeholder text sits in {colors.muted}.

**`search-bar`** — Inline composition of text input and an attached solid-orange search trigger button sharing an 8px radius container. The orange submit button functions as a compressed `button-primary`, keeping the search action recognizable without requiring extra chrome.

### Navigation

**`nav-top-strip`** — 36px #ff7700 bar sitting above the main header. Carries promotional messaging, free shipping thresholds, and account utility links in small white caption type. This strip is the brand's loudest single color block and establishes orange as the authority signal before any content loads.

**`nav-bar`** — 64px #282f37 charcoal main navigation below the orange strip. White bold sans-serif links. The two-tier header — orange over dark — is the most consistent brand fingerprint across every page at every screen size.

**`nav-mega-menu`** — White dropdown panel with 1px hairline border and a soft box shadow. Product category columns, grade-level filters, and featured experiment tiles organize into a scannable grid. No branded color in the dropdown body — it resets to white to let the category imagery breathe.

### Cards

**`product-card`** — White card with 1px hairline border, 8px radius, and square product photography. Title in {typography.title-sm}, price in bold {typography.price}. Age badge ({age-badge}) and grade badge ({grade-badge}) stack at the image corner as the primary metadata layer parents scan before clicking. Hover lifts the card 2px and deepens the shadow.

**`experiment-card`** — Used in the free experiments library to distinguish editorial content from purchasable kits. Off-white #f3f2f7 fill with a 4px #ff7700 orange top accent bar that visually connects experiment content to the product grid. Title and excerpt type in accessible sans-serif.

### Badges

**`age-badge`** — Solid #ff7700 pill ({rounded.full}) showing age range ("Ages 8+"). The dominant at-a-glance filter signal in the product grid — parents locate these before processing product names.

**`grade-badge`** — Solid #003388 navy pill for curriculum grade range ("Grades 3–5"). Paired with the age badge, the two pills deliver audience qualification in under one second of scan time.

**`sale-badge`** — Coral #df653e rectangular flag ({rounded.xs}) positioned as an absolute overlay on product images. Communicates discount urgency without competing with the orange primary CTA.

**`new-badge`** — Dark green #116600 flag for newly added experiments or kits. Completes a three-badge signal system: orange for age, navy for grade, green for new, coral for sale.

### Hero

**`hero-banner`** — Full-width dark #282f37 banner with a left-anchored text column and linear gradient mask fading to transparent at 80%. Experiment photography — smoke, pour sequences, reaction imagery — fills the right side as the emotional hook. Headline in {typography.display-xl} white; body copy in {typography.body-md} at reduced opacity; CTA in orange ({colors.primary}) with white text and {rounded.sm}. Minimum 480px desktop height.

### Browsing

**`category-chip`** — Soft off-white pills with hairline border used in filter and category browse rails. Active state inverts to solid #ff7700 with white text, making the selected filter immediately legible against the surrounding unselected gray chips.

### Footer

**`footer`** — #282f37 dark footer with a 4px #ff7700 orange top border marking the page boundary. Link text in muted dusty blue (#7fa9c5) for contrast against the dark background without reading as primary-level CTAs. Section headings in bold white {typography.title-sm}. Newsletter signup field uses the same input style as the main search bar with an orange submit button.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger menu collapses nav-bar into a full-screen dark drawer; nav-top-strip hides to reclaim header height; hero stacks image above text at full width; age and grade badges move below product title; category chips scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; mega-menu collapses to accordion drawer; hero maintains landscape ratio with left text overlay; footer four-column link grid reflows to two columns |
| Desktop | 1128–1440px | Three to four-column product grid; full mega-menu dropdown on hover; dual-strip nav at full height; experiment cards render in sidebar grid alongside product results |
| Wide | > 1440px | Grid holds at four columns inside a max-width container (~1400px centered); hero photography scales up within fixed text zone; section padding increases to {spacing.section} on outer rails |

### Touch Targets

- All buttons minimum 44px height
- Mobile nav links padded to 48px tap target height
- Category chips minimum 36px height
- Product card tappable as a unified block with no nested dead zones
- Badge pills are display-only; tap area belongs to the parent card

### Collapsing Strategy

- Primary navigation collapses to hamburger icon at < 744px; mega-menu category grid becomes a full-screen slide-in drawer with accordion subcategories
- Promotional top strip (#ff7700) hides on mobile — height budget prioritized for content
- Footer four-column link grid collapses to two columns at tablet, then single-column expandable sections on mobile
- Age and grade badge pair shifts from horizontal row (desktop) to stacked vertical pair (mobile product card) to maintain legibility at smaller card widths
- Hero layout transitions from side-by-side (desktop) to image-above-text (mobile) below 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Actual web typeface not captured; the extracted font stack (Andale Mono, Arial, Baskerville, Courier New, Copperplate, Geneva, etc.) is the complete TinyMCE block editor font-picker list, not the live typeface used in the UI. Real heading and body fonts are almost certainly loaded via `@font-face` or a third-party CDN absent from extraction.
- Many extracted hex values (#9b51e0, #00d084, #7bdcb5, #8ed1fc, #0693e3, #fcb900, #eeee22, #f78da7, #cf2e2e) are WordPress Gutenberg block editor default palette entries embedded in CMS content over years, not structural brand colors.
- No `theme-color` meta tag; #ff7700 primary designation is inferred from visual dominance in CTA and badge usage rather than a confirmed brand specification.
- Precise button border-radius, shadow values, and hover transition durations not confirmed from live CSS.
- Mobile navigation structure (drawer vs. bottom sheet vs. full-screen overlay) unconfirmed.
- Whether the front-end is powered by a utility framework (Tailwind, Bootstrap) or a bespoke theme is unknown; component token values are approximations.
- Exact product-card layout for "Wow Factor" star ratings or experiment difficulty indicators not confirmed — these elements are referenced in brand content but their visual spec was not captured.
