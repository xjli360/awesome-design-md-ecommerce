---
version: alpha
name: "Three Ships"
source_url: "https://www.threeshipsbeauty.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Three Ships Beauty speaks in a voice that is at once earthy and electric, grounding its natural skincare promise in a deep indigo primary (`#170a69`) that reads as both trustworthy and aspirational — a midnight sky for a brand that believes in clean ingredients and visible results. The palette is a study in thoughtful contrast: warm cream canvases (`#fffce5`) and soft off-white surfaces (`#fafafa`, `#f7f7f7`) provide a gentle, almost editorial backdrop for product photography, while accent voltages of lime (`#ecfab3`, `#afb84a`), rose (`#911a4b`, `#d43747`), and amber (`#fff6b2`, `#e5cb00`) punctuate the interface like botanical highlights. Typography is where the brand reveals its dual nature — the display voice leans on Rauschen ABook and its italic variant, a sophisticated serif that whispers editorial luxury, while the UI layer runs on ABCFavoritMono, a monospaced sans that injects a modern, almost technical precision. This tension between the organic and the structured is the brand's signature design move: pill-shaped buttons (`{rounded.full}`) and softly rounded cards (`{rounded.md}`) keep the experience approachable, while tight monospaced captions and a disciplined `{spacing.section}` rhythm lend a lab-like rigor. The result feels like a wellness journal designed by a typographer — generous whitespace, deliberate color pops, and a quiet confidence that never shouts. Every `{colors.primary}` CTA, every `{colors.muted}` hairline, every `{rounded.sm}` input exists to make the product the hero, not the chrome.

colors:
  primary: "#170a69"
  primary-active: "#210e98"
  primary-disabled: "#737373"
  ink: "#03010c"
  body: "#170a69"
  muted: "#808080"
  muted-soft: "#a6a6a6"
  hairline: "#cccccc"
  hairline-soft: "#dedede"
  canvas: "#fffce5"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-lime: "#ecfab3"
  accent-lime-strong: "#afb84a"
  accent-rose: "#911a4b"
  accent-rose-strong: "#d43747"
  accent-amber: "#fff6b2"
  accent-amber-strong: "#e5cb00"
  accent-blue: "#3d22ea"
  error: "#d02e2e"
  error-soft: "#f3cbcb"
  star-rating: "#e5cb00"

typography:
  display-xl:
    fontFamily: "'Rauschen ABook', 'Rauschen-ABook-Desktop', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Rauschen ABook', 'Rauschen-ABook-Desktop', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Rauschen ABook', 'Rauschen-ABook-Desktop', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Rauschen ABook', 'Rauschen-ABook-Desktop', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'ABCFavoritMono', 'Consolas', monospace, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'ABCFavoritMono', 'Consolas', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  body-md:
    fontFamily: "'Instrument Sans', 'Poppins', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'ABCFavoritMono', 'Consolas', monospace, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'ABCFavoritMono', 'Consolas', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'ABCFavoritMono', 'Consolas', monospace, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  link:
    fontFamily: "'Instrument Sans', 'Poppins', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'ABCFavoritMono', 'Consolas', monospace, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'ABCFavoritMono', 'Consolas', monospace, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 16px
  button-accent-lime:
    backgroundColor: "{colors.accent-lime-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-accent-rose:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
    textColor: "{colors.error}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.surface-card}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    size: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.surface-card}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    size: 20px
  radio-checked:
    border: "6px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    width: 44px
    height: 24px
  toggle-active:
    backgroundColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.lg}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(3, 1, 12, 0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-card-title:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-rating:
    textColor: "{colors.star-rating}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
  hero-secondary-cta:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    textColor: "{colors.ink}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-lime}"
  footer-heading:
    typography: "{typography.caption}"
    textColor: "{colors.accent-lime}"
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "0 {spacing.lg} {spacing.lg}"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  ingredient-badge:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  ingredient-badge-rose:
    backgroundColor: "{colors.accent-rose-strong}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  ingredient-badge-amber:
    backgroundColor: "{colors.accent-amber-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  section-heading:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    padding: "0 0 {spacing.lg} 0"
  section-subheading:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "0 0 {spacing.sm} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered as a full pill shape (`{rounded.full}`) in deep indigo (`{colors.primary}`) with white monospaced uppercase text (`{typography.button-md}`). On hover, it shifts to `{colors.primary-active}`; when disabled, it fades to `{colors.primary-disabled}`. The generous horizontal padding (`32px`) and fixed height (`48px`) ensure a substantial, confident tap target. **`button-secondary`** — An outlined variant that inverts the primary: a transparent fill with a `2px` indigo border, indigo text, and the same pill silhouette. On active state, it fills solid with `{colors.primary}` and flips text to white. **`button-tertiary-text`** — A ghost button with no border or background, using only indigo text and minimal padding for inline actions like "Learn More" or "Skip." **`button-accent-lime`** and **`button-accent-rose`** — Brand-specific accent buttons for promotional or category-specific CTAs, using the lime (`{colors.accent-lime-strong}`) or rose (`{colors.accent-rose}`) palette voltages while maintaining the same monospaced uppercase typography and pill shape.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.md}` corners and `{spacing.base}` padding, designed to float product imagery and metadata. The image area is a perfect square (`aspectRatio: 1 / 1`) with `{rounded.sm}` corners. On hover, a subtle `boxShadow` lifts the card. The price is set in monospaced `{typography.title-sm}` in primary indigo, while the product name uses `{typography.body-md}` in ink. A **`product-card-badge`** — a small lime pill (`{colors.accent-lime}`) — can overlay the image for "New" or "Best Seller" flags. Ratings use the amber star color (`{colors.star-rating}`). **`ingredient-badge`** — A compact pill badge in lime, rose, or amber to tag key ingredients (e.g., "Vitamin C", "Niacinamide", "Retinol") on product detail cards or ingredient lists.

### Navigation
**`nav-bar`** — A fixed-height (`72px`) bar on the cream canvas (`{colors.canvas}`) with monospaced uppercase nav links (`{typography.nav-link}`). Active links gain a `2px` bottom border in `{colors.primary}`; inactive links render in `{colors.muted}`. The bar uses `{spacing.lg}` horizontal padding. On mobile, the nav collapses into a hamburger menu with a slide-out drawer. **`tab-active`** and **`tab-inactive`** — Pill-shaped tabs for filtering product categories (e.g., "Face", "Body", "Sets"). Active tabs fill with indigo and white text; inactive tabs sit on `{colors.surface-soft}` with muted text.

### Forms
**`text-input`** — A standard input field with white background, `{rounded.sm}` corners, and a `1px` hairline border. On focus, the border thickens to `2px` and turns indigo. Error state uses `{colors.error}` border and text. Disabled inputs fade to `{colors.surface-soft}` with muted text. **`select-input`** — Mirrors the text input styling but includes a custom dropdown chevron. **`textarea`** — Same styling as text-input but without a fixed height. **`checkbox`** and **`radio`** — Custom-styled controls with a `20px` bounding box, `{rounded.xs}` for checkboxes and `{rounded.full}` for radios. Checked states fill with `{colors.primary}`. **`toggle`** — A pill-shaped toggle (`44px x 24px`) that switches from `{colors.hairline}` to `{colors.primary}` when active.

### Footer
**`footer-section`** — A deep indigo (`{colors.primary}`) footer with white body text and lime (`{colors.accent-lime}`) headings set in monospaced uppercase (`{typography.caption}`). Links are white and turn lime on hover. The section uses `{spacing.section}` vertical padding and `{spacing.lg}` horizontal padding. A **`divider`** in `{colors.hairline}` or `{colors.hairline-soft}` separates footer columns.

### Hero & Sections
**`hero-section`** — A full-width section on the cream canvas (`{colors.canvas}`) with the largest display typography (`{typography.display-xl}`) and a primary CTA button. A secondary ghost CTA with an indigo border sits alongside for alternative actions. **`section-heading`** and **`section-subheading`** — Standard section headers using `{typography.display-lg}` for the title and `{typography.caption}` (uppercase monospaced) for the subtitle, with `{spacing.lg}` bottom padding.

### Accordion
**`accordion`** — A collapsible panel with white background, `{rounded.sm}` corners, and a `1px` hairline border. The header uses monospaced `{typography.title-sm}` with `{spacing.base}` vertical padding; the content area collapses with `{spacing.lg}` bottom padding when open. Used for FAQ sections and product details.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger; product cards stack vertically; hero typography scales down to `{typography.display-md}`; buttons become full-width; footer columns stack; accordion becomes default for product details; search bar moves to top of page. |
| Tablet | 744–1128px | Two-column grid for product cards; nav-bar remains visible but links may condense; hero uses `{typography.display-lg}`; side-by-side layout for product detail images and description; footer uses two-column grid. |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links; hero uses `{typography.display-xl}`; multi-column footer; standard spacing and typography tokens apply. |
| Wide | > 1440px | Max-width container (`1440px`) centered; additional whitespace on sides; product grid can expand to four columns; hero may include larger imagery or video. |

### Touch Targets
- All interactive elements (buttons, inputs, links) maintain a minimum `48px` height for touch accessibility.
- Icon-only buttons and toggles use `44px` minimum touch area.
- Product card tap targets (title, price, add-to-cart) are at least `44px` tall.
- Nav-bar links have `48px` tap height.
- Accordion headers are `48px` minimum tap height.

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px).
- Product filters collapse into a slide-out drawer or modal on mobile.
- Multi-column footer stacks to single column on mobile.
- Product detail sections (description, ingredients, how to use) collapse into accordion panels on mobile and tablet.
- Search bar moves from inline to a full-screen overlay on mobile.
- Hero section reduces typography scale and may stack CTA buttons vertically on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (e.g., nav-link hover, card hover) were inferred from common patterns rather than extracted from live CSS.
- Error and success states for forms (e.g., validation messages, success banners) were not observed on the live site.
- Sub-brand or collection-specific palettes (e.g., "The Dewy Duo", "The Glow Set") may exist but were not captured.
- Dark mode is not supported and no dark mode tokens were found.
- Animation and transition durations/easings were not extracted; a default `0.2s ease` is assumed for interactive states.
- Specific iconography (e.g., cart icon, search icon, hamburger menu) was not captured; SVG or font-icon usage is assumed.
- Typography scale for mobile (e.g., responsive font-size reductions) was estimated based on common breakpoint behavior.
- The exact `fontWeight` values for Rauschen ABook and ABCFavoritMono were inferred from font names; actual weights may vary.
- The `letterSpacing` values for monospaced fonts were estimated to achieve a "tight" uppercase look; live values may differ.
- The `textTransform: uppercase` on captions and buttons was inferred from the brand's aesthetic; not all instances may use it.
- The `boxShadow` for product-card-hover was not found in CSS; a generic shadow was assumed.
- The `aspectRatio: 1 / 1` for product-card-image was inferred from common e-commerce patterns; actual ratios may vary by product.
- The `border` property on button-secondary was assumed to be `2px`; live site may use a different thickness.
- The `height: 48px` for buttons and inputs was inferred from common accessibility standards; actual heights may vary.
- The `padding` values for components were estimated based on typical spacing tokens; live values may differ.
- The `max-width: 1440px` for wide screens was assumed; actual container width may vary.
- The `color` values for `star-rating` and `error` were inferred from the extracted palette; live values may differ.
- The `fontFamily` fallbacks for Rauschen ABook and ABCFavoritMono were assumed; actual fallbacks may include additional fonts.
