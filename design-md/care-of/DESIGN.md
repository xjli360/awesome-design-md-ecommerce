---
version: alpha
name: "Care/of"
source_url: "https://takecareof.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Each foil packet that leaves a Care/of fulfillment center has the customer's first name printed on the face — this single production choice clarifies every downstream design decision. The interface is not a storefront so much as a diagnostic conversation that happens to end with a checkout. A warm coral (approximately #E8614F) shoulders the entire brand signal that most supplement companies split between clinical blue, warning orange, and hero green; here the same hue that says "take this now" also says "we made this for you." It sits against parchment backgrounds (#FAF8F4) rather than pure white, borrowing warmth from the paper-and-packaging world the brand grew up in.

  Two type families carry the expressive weight. Display headings run in an editorial serif — high-contrast strokes, generous at 36–56px, with subtly tight tracking — reserved for quiz questions, hero moments, and ingredient story panels. Everything operational — labels, CTAs, navigation, ingredient dosages — moves through a clean geometric sans-serif. The contrast is deliberate: serif belongs to the personal and the narrative; sans belongs to the clinical and the transactional. Rounded corners hold to `{rounded.sm}`–`{rounded.md}` for cards and inputs, inflating to `{rounded.full}` only for inline ingredient tags where a pill marks a discrete category.

  The quiz is the brand's architectural spine. A single-question-per-screen flow gathers name, goals, sleep, diet, and stress markers before assembling a personalized recommendation. Each question fills the viewport with one serif headline and two to four large tap-targets spaced at `{spacing.xl}` intervals. A thin proportional bar pinned at the top of the screen — no numbers, no "Step 3 of 12" — tracks progress without gamifying the experience. After the quiz, ingredient cards in a two-column desktop grid and single-column mobile scroll show each vitamin's purpose with a collapsible clinical study drawer; the depth is available, not imposed.

  Surface hierarchy runs on tonal warmth rather than shadow: canvas (#FFFFFF) for cards, surface-soft (#F3EFE8) for secondary panels, parchment (#FAF8F4) for page backgrounds. A 1px hairline (#E0DAD2) replaces drop shadows almost everywhere. The daily packet — a rendered foil pouch with the customer's name — reappears in the account dashboard and cart confirmation as both a product visual and a proof of personalization. This packet motif, more than the coral or the serif, is the brand's most concentrated design asset.

colors:
  primary: "#E8614F"
  primary-active: "#CC4A38"
  primary-disabled: "#F4B8AE"
  ink: "#1D1D1B"
  body: "#3A3632"
  muted: "#7C7670"
  hairline: "#E0DAD2"
  canvas: "#FFFFFF"
  surface-soft: "#F3EFE8"
  surface-card: "#FFFFFF"
  parchment: "#FAF8F4"
  on-primary: "#FFFFFF"
  kraft: "#8B7355"
  success: "#4A7C59"
  success-soft: "#E8F2EC"

typography:
  display-xl:
    fontFamily: "'Tiempos Display', 'Domaine Display', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: "-0.5px"
  display-md:
    fontFamily: "'Tiempos Display', 'Domaine Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.3px"
  display-sm:
    fontFamily: "'Tiempos Display', 'Domaine Display', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.1px"
  quiz-display:
    fontFamily: "'Tiempos Display', 'Domaine Display', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.2px"
  title-md:
    fontFamily: "'Matter', 'DM Sans', Inter, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "0"
  title-sm:
    fontFamily: "'Matter', 'DM Sans', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "0"
  body-md:
    fontFamily: "'Matter', 'DM Sans', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0"
  body-sm:
    fontFamily: "'Matter', 'DM Sans', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
  caption:
    fontFamily: "'Matter', 'DM Sans', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: "0.2px"
  ingredient-label:
    fontFamily: "'Matter', 'DM Sans', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.8px"
    textTransform: uppercase
  button-md:
    fontFamily: "'Matter', 'DM Sans', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "0.3px"
  button-sm:
    fontFamily: "'Matter', 'DM Sans', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "0.2px"
  nav-link:
    fontFamily: "'Matter', 'DM Sans', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: "0"

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
    padding: "14px 28px"
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.ink}"
    padding: "13px 27px"
    height: 52px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "14px 16px"
    height: 52px
    borderWidth: 1.5px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  quiz-card:
    backgroundColor: "{colors.parchment}"
    textColor: "{colors.ink}"
    questionTypography: "{typography.quiz-display}"
    padding: "{spacing.xxl} {spacing.xl}"
    maxWidth: 600px
  quiz-option:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    borderSelected: "1.5px solid {colors.ink}"
    backgroundSelected: "{colors.surface-soft}"
    padding: "16px 20px"
    minHeight: 56px
  quiz-progress-bar:
    backgroundColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    height: 3px
    rounded: "{rounded.full}"
    position: top
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageAspectRatio: "1/1"
  ingredient-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.ingredient-label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  ingredient-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  daily-pack-widget:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.display-sm}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  benefit-tag:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.parchment}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
  science-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — The primary CTA is a warm coral (#E8614F) block, 52px tall, with 14px vertical and 28px horizontal padding, rounded at `{rounded.sm}`. Text runs in the geometric sans at 16px/600 weight with 0.3px letter-spacing. On `:hover` the fill deepens immediately to `{colors.primary-active}` (#CC4A38) with no easing delay; on `:disabled` it flattens to a washed coral (`{colors.primary-disabled}`). Used for quiz CTAs, "Take the quiz," and "Add to cart" actions — the coral never shares this slot with another color.

**`button-secondary`** — Canvas fill with a 1.5px ink border at the same 52px height and `{rounded.sm}` radius. Used for secondary actions like "Learn more" or skip options within the quiz flow. On hover, the background shifts to `{colors.surface-soft}`, keeping the border solid.

**`button-ghost`** — No background, no border, underlined link-style text in `{colors.ink}` at `{typography.button-sm}`. Reserved for tertiary actions — "Skip," "Not now," or footer navigation links where additional visual weight would compete with surrounding content.

### Text Input

**`text-input`** — 52px tall, 1.5px hairline border at rest, sharpening to a full ink border on focus with an abrupt (not animated) state change that reads like filling in a paper form. Placeholder text in `{colors.muted}`. Rounded at `{rounded.sm}`. Used in the quiz for name entry and email capture, and in the account login flow.

### Navigation

**`nav-bar`** — 72px tall, white background with a 1px hairline bottom border. The wordmark or logotype sits at the far left. Nav links — typically "How it works," "Ingredients," "Reviews" — use `{typography.nav-link}` in ink with no underline at rest. A `button-primary` "Take the quiz" CTA anchors the far right. On mobile (< 744px), secondary links are hidden and a 44×44px hamburger triggers a full-screen overlay drawer with the quiz CTA prominent at the top.

### Product Cards

**`product-card`** — White card with 1px hairline border and `{rounded.md}` corners. The image area occupies the full card width at 1:1 aspect ratio. Below, the product name runs in `{typography.title-md}` and dose/form runs in `{typography.body-sm}` in `{colors.muted}`. Ingredient badges stack horizontally beneath with overflow scroll on mobile. No drop shadow — the 1px border does all separation work.

**`ingredient-card`** — Used on the recommendation results page alongside product cards. Same border and radius treatment. Ingredient name in `{typography.title-md}`, a one-line benefit statement in `{typography.body-sm}`, and a "See the science" expand trigger in `{typography.caption}` that opens a collapsible drawer with clinical study citations. The drawer expands in place without navigation away from the page.

### Quiz Components

**`quiz-card`** — Full-viewport parchment (#FAF8F4) background, max-width 600px centered horizontally. The question runs in `{typography.quiz-display}` (28px serif, tight tracking) with `{spacing.xxl}` above and below. Answer options are stacked `quiz-option` rows with `{spacing.sm}` gap between them. The selected state shifts the border to full ink and fills the background with `{colors.surface-soft}`, with no animation — the selection registers as a document state change, not a UI flourish.

**`quiz-progress-bar`** — A 3px strip pinned to the very top of the quiz viewport, spanning full browser width. Fill color is `{colors.primary}`, track is `{colors.hairline}`, both `{rounded.full}`. No percentage label, no step count — purely proportional fill that advances as the user moves forward.

### Personalization Components

**`daily-pack-widget`** — The rendered foil packet with the customer's name on the face. Appears in the cart confirmation, account dashboard, and renewal reminder emails. The name renders in `{typography.display-sm}` (serif) overlaid on the packet illustration. The surrounding container uses `{colors.surface-soft}` with `{rounded.md}` and `{spacing.lg}` padding, keeping the packet centered and prominent without a competing background texture.

**`ingredient-badge`** — A small `{rounded.full}` pill in `{colors.surface-soft}` with uppercase micro-text (`{typography.ingredient-label}`) labeling a category such as "MAGNESIUM" or "VITAMIN D3." Used as horizontally scrolling tags beneath product cards and as filter chips on the full ingredients listing page.

**`benefit-tag`** — A green-tinted `{rounded.full}` pill — `{colors.success-soft}` background, `{colors.success}` text — labeling confirmed health benefits: "Supports sleep," "Immune support." Smaller and more emphatic than ingredient badges, set in `{typography.caption}`. Appears in recommendation summaries and ingredient detail headers.

### Content Sections

**`hero-section`** — Parchment background (#FAF8F4) with headline in `{typography.display-xl}` and supporting body in `{typography.body-md}`. The `button-primary` "Take the quiz" CTA sits below with `{spacing.lg}` top margin. On desktop, product photography sits right of the text in a 55/45 split. `{spacing.section}` top and bottom padding. On mobile, the image drops below the headline and the CTA stretches to full width.

**`science-panel`** — A `{colors.surface-soft}` section block for clinical study data. Headline in `{typography.display-sm}` (serif), supporting copy in `{typography.body-md}`. Study citations render as collapsible accordion rows with `{typography.caption}` labels. Rounded at `{rounded.md}` with `{spacing.xl}` padding. Appears on ingredient detail pages and the brand science landing page.

### Footer

**`footer`** — Ink (#1D1D1B) background, canvas text across four desktop columns: product, company, legal, social. Column headers in `{typography.caption}` uppercase with `{colors.kraft}` tint. Links in `{typography.body-sm}` in `{colors.hairline}`. `{spacing.section}` vertical padding. On mobile, columns collapse into a single accordion-style stack with expand/collapse controls.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; nav collapses to hamburger + full-screen overlay; quiz options expand to full width; ingredient and product grids → single scroll column; footer columns → accordions; hero image moves below headline; all primary buttons full-width |
| Tablet | 744–1128px | Two-column ingredient and product grids; nav shows logo + quiz CTA, secondary links hidden; hero shifts to 60/40 text/image split |
| Desktop | 1128–1440px | Three-column ingredient grid; full nav with all links + quiz CTA; hero at 55/45; quiz flow max-width 600px centered |
| Wide | > 1440px | Max content width capped at 1320px with auto margins; all layouts lock to desktop proportions |

### Touch Targets

- Quiz answer options: minimum 56px tall, full-width tap surface with 20px horizontal padding
- Nav hamburger icon: 44×44px minimum hit area
- Ingredient badges: 32px minimum height with padded tap area
- All primary and secondary buttons: 52px tall minimum
- Accordion expand controls in mobile footer: 44px tall tap row

### Collapsing Strategy

- Navigation collapses to icon-only hamburger at < 744px; full-screen overlay shows stacked links with the quiz CTA prominent at the top in `button-primary`
- Product and ingredient grids: 3-col → 2-col → 1-col at the two major breakpoints
- Science panel accordions default to collapsed on mobile to reduce initial scroll depth
- Footer column groups collapse to a single accordion stack with inline +/− expand toggles
- Hero image hides on mobile or repositions below the headline block; the quiz CTA expands to full viewport width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — takecareof.com returned no extractable color tokens (likely CSS custom properties injected via JavaScript, or anti-bot protection active during extraction). All palette values — #E8614F primary coral, #FAF8F4 parchment, #1D1D1B ink, #F3EFE8 surface-soft — are inferred from brand packaging, marketing materials, and visual documentation. Treat as approximate until confirmed against live computed styles.
- **No font families extracted** — Font stack references ('Tiempos Display', 'Matter') are inferred from the brand's editorial aesthetic and DTC typeface conventions; the actual licensed typefaces in production are unconfirmed. Run `document.fonts` in a live browser session to extract the true families.
- **Exact primary coral value** — The coral is consistently visible across brand touchpoints but the precise hex varies slightly across print and screen renderings; #E8614F is a best approximation.
- **Dark mode** — No dark mode tokens or behavior observed; the brand appears to operate in a single light-mode color context.
- **Animation and motion** — Micro-interaction timing curves, quiz step transitions, ingredient drawer animations, and page transition specs are unavailable without live site instrumentation.
- **Icon and illustration system** — Care/of uses small illustrative icons and packet illustrations; the specific icon library or custom SVG set is unconfirmed.
- **Quiz branching logic** — The quiz has conditional paths based on dietary restrictions, health conditions, and medications that affect the recommendation output; these cannot be captured in a static design spec without full product access.
- **Internal component spacing** — Padding values for quiz options, ingredient drawers, and science panels are estimated from visual reference; production stylesheet values have not been extracted.
