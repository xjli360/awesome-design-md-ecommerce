---
version: alpha
name: "Watch Collectors"
source_url: "https://watchcollectorsllc.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Where most luxury e-commerce fights for brightness, Watch Collectors builds its visual language in the dark — near-black canvas layers (#121212, #242424) absorb ambient light and make every dial photograph read like a piece sitting under gallery track lighting. Against that darkness, the champagne-gold signature (#ccb17b) operates precisely as a private dealer's price tag or vitrined boutique signage would: warm, unhurried, unmistakably valuable. The cool silver-gray tones (#dedede, #d4d9db) handle secondary surfaces and form fields, echoing brushed steel and white-gold finishing without attempting to simulate them.

  Assistant — a geometric humanist sans-serif with unusually clean metrics and open counters — carries all text, from hero callouts down to spec-sheet captions. Its even stroke weight and natural tracking hold legibility at small sizes, which matters here: a watch listing card must simultaneously surface movement type, case diameter, reference number, and provenance status in a vertically compressed space. Luxury watch listings require a different information hierarchy than fashion or consumer goods; authentication details and condition grades carry equal or greater weight than the headline price, so the typographic system dedicates distinct caption and spec-label scales alongside larger display sizes.

  Shopify powers the cart and checkout layer, keeping the CTA pattern structurally familiar — but the primary button trades the platform's default cobalt for house gold, and the product detail page leans on full-bleed dial photography with floating specification overlays rather than thumbnail-plus-copy layouts. Corner rounding is deliberately minimal: {rounded.sm} (4px) on cards and inputs, {rounded.xs} (2px) on badges, no pill shapes anywhere except optional filter chips. The overall register is a digital private dealer or auction-preview room — sparse, dark, catalogued — where the inventory is the sole decorative element.

colors:
  primary: "#ccb17b"
  primary-active: "#b8945e"
  primary-disabled: "#e0cfa3"
  ink: "#242424"
  body: "#3a3a3a"
  muted: "#6b6b6b"
  hairline: "#dedede"
  canvas: "#ffffff"
  canvas-dark: "#121212"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#242424"
  on-primary: "#121212"
  on-dark: "#dedede"
  silver-cool: "#d4d9db"
  gold-muted: "#e8d4b0"

typography:
  display-xl:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  spec-label:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.10em
    textTransform: uppercase
  price-display:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.01em
  button-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    padding: 14px 32px
    height: 48px
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.surface-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    secondaryTextColor: "{colors.muted}"
    imageBackgroundColor: "{colors.canvas-dark}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    border: "1px solid {colors.hairline}"
  watch-hero:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-md}"
    minHeight: 560px
    imageFit: contain
    imageBackground: "{colors.canvas-dark}"
  spec-table:
    backgroundColor: "{colors.surface-dark}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowBorder: "1px solid rgba(255,255,255,0.07)"
    padding: "{spacing.base} {spacing.lg}"
  auth-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  condition-badge:
    backgroundColor: "{colors.silver-cool}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  collection-header:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-md}"
    labelTypography: "{typography.spec-label}"
    borderBottom: "1px solid {colors.surface-dark}"
    padding: "{spacing.xl} 0"
  search-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px {spacing.base}"
    height: 44px
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.surface-dark}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Solid champagne-gold fill (#ccb17b) with near-black text label in uppercase 13px Assistant at 0.12em tracking, 48px tall, 4px radius. Hover deepens the fill to `{colors.primary-active}` (#b8945e); disabled state fades to `{colors.primary-disabled}` (#e0cfa3) with `cursor: not-allowed`. Used exclusively for transactional moments: "Add to Cart," "Inquire Now," "Request Price."

**`button-secondary`** — Transparent background with a 1px gold border and gold text, matching dimensions to `button-primary` for paired placement on product pages (e.g., "Save to Wishlist" alongside "Add to Cart"). On hover, the background accepts `{colors.primary}` at 10% opacity, maintaining the outline while signaling interactivity without the full fill commitment.

**`button-ghost-dark`** — Outlined treatment identical to `button-secondary` in structure, but targeting dark-background sections — the hero, collection headers, and footer CTAs — using `{colors.on-dark}` border and text so the button reads cleanly against the near-black canvas without competing with gold accent elements.

### Navigation

**`nav-bar`** — Fixed 64px-tall dark bar (`{colors.canvas-dark}`) with the brand logotype rendered in `{colors.primary}`. All navigation links run in uppercase 13px Assistant at 0.08em tracking (`{typography.nav-link}`). A 1px `{colors.surface-dark}` separator divides the bar from page content below. Cart count, account, and search icons sit right-aligned; search triggers the `search-bar` modal overlay. On scroll the bar remains opaque — no transparency or blur treatment.

### Product Cards

**`product-card`** — White surface with 1px `{colors.hairline}` border and 4px radius. The watch photograph renders on a `{colors.canvas-dark}` background to approximate a lightbox; images use `object-fit: contain` so bezels and case edges are never cropped. Title in `{typography.title-md}` (18px/600), brand and reference number in `{typography.body-sm}` at `{colors.muted}`, price in `{typography.price-display}` (24px/300). Authentication and condition badges stack in a tight horizontal row directly below the price line.

### Watch Hero

**`watch-hero`** — Full-width dark section with a centered or split-layout dial image rendered at `object-fit: contain` against `{colors.canvas-dark}`, minimum 560px tall. Headline in `{typography.display-xl}` (42px/300) in `{colors.on-dark}` with 0.02em tracking; subtitle in `{typography.display-md}` (28px/300). A thin horizontal rule in `{colors.primary}` may run beneath the headline callout as an accent divider. CTAs in this zone use `button-ghost-dark` rather than the gold-fill primary.

### Spec Table

**`spec-table`** — Two-column definition list on `{colors.surface-dark}`. Labels — Movement, Diameter, Case Material, Reference, Year, Condition, Certification — in `{typography.spec-label}` (11px, uppercase, 0.1em tracking) in `{colors.muted}`. Values in `{typography.body-sm}` in `{colors.on-dark}`. Rows separated by a hairline at 7% white opacity; no outer border or box shadow. Certification rows place an `auth-badge` inline with the value text.

### Badges

**`auth-badge`** — Solid gold fill (`{colors.primary}`) with dark text (`{colors.on-primary}`), 2px radius, uppercase 11px spec-label tracking. Used for provenance annotations: "Certified Pre-Owned," "Box & Papers," "Original Warranty Card," "Service Records." **`condition-badge`** — Cool silver-gray fill (`{colors.silver-cool}`) with dark ink text, same height and padding, for condition grades: "Mint," "Excellent," "Very Good," "Good."

### Collection Header

**`collection-header`** — Dark-background section header spanning the top of brand or category listing pages. A small `{typography.spec-label}` label in `{colors.primary}` announces the category above the main headline; the headline itself renders in `{typography.display-md}` (28px/300) in `{colors.on-dark}`. A 1px `{colors.surface-dark}` border-bottom separates the header from the product grid. Result count and active filter chips sit in a secondary row below the headline.

### Search

**`search-bar`** — Full-width modal overlay input on `{colors.surface-dark}`, 44px tall, 2px radius. Placeholder and entered text in `{typography.body-md}`. A gold magnifying-glass icon (`{colors.primary}`) anchors the left edge; an × dismiss icon sits right. The overlay appears over the page with a low-opacity dark scrim and no animation — immediate presence.

### Footer

**`footer`** — Dark bar (`{colors.canvas-dark}`) with a 1px `{colors.surface-dark}` top border. Column headers in `{typography.spec-label}` at `{colors.primary}`; body links and legal text in `{typography.body-sm}` at `{colors.muted}`, transitioning to `{colors.on-dark}` on hover. Brand logotype repeated in `{colors.primary}` at reduced size. Column layout collapses to stacked accordion sections on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; `watch-hero` stacks image above headline text; `spec-table` scrolls horizontally; nav collapses to hamburger + centered logo + cart icon; `collection-header` headline reduces to 22px |
| Tablet | 744–1128px | Two-column product grid; hero switches to split layout (dial image left, headline and CTA right); nav shows 3–4 primary links, remaining items under overflow menu |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links visible; `watch-hero` at full 560px height; `spec-table` renders inline alongside the hero image in a 50/50 split |
| Wide | > 1440px | Four-column product grid; all content max-width constrained to 1440px with padded gutters; no structural layout changes beyond column expansion |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Badges padded to 36px tap-height on mobile even when visually shorter
- Nav hamburger icon allocated 44×44px tap zone
- Entire `product-card` surface is tappable, not just the title link
- Filter chips minimum 36px height with 8px horizontal padding

### Collapsing Strategy
- Nav collapses to hamburger at < 744px; search accessible via icon in the collapsed bar
- `spec-table` converts to horizontally scrollable table on mobile — watch specification label/value pairs lose semantic meaning if reordered or stacked, so scrolling is preferred over reflowing
- `footer` columns collapse to accordion sections with `{typography.spec-label}` headers as expand/collapse triggers
- `collection-header` category label and headline compress to a single stacked block; filter row moves below the headline rather than inline
- `product-card` image aspect ratio held at 4:3 across all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only five hex values extracted; hover states for `text-input`, focus rings, link underline colors, and scrollbar styles inferred from brand character rather than measured
- Icon set unidentifiable from extraction — brand may use a third-party library (Feather, custom SVG sprite) for nav, badge, and UI icons
- Font weight range for Assistant not confirmed — whether the full variable range (100–900) or only subset weights (300/400/600/700) are loaded is unknown
- No motion or transition values extracted — overlay animation easing, hover transition durations, and image carousel behavior are estimated at system defaults
- Authentication or certification partner co-branding (CPO certifier logos, third-party grading badges) not visible in extraction; may introduce additional color or logo tokens
- Dark-mode vs. light-mode toggle behavior unknown; site may be dark-only or may offer a preference toggle that switches `{colors.canvas-dark}` sections to white
- Mobile hamburger animation style and drawer treatment not extractable without live interaction recording
