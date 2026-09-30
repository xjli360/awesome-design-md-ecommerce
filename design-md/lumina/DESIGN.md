---
version: alpha
name: "Lumina"
source_url: "https://lumina.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-navy (#090a3f) and electric-blue (#2a93f4) platform for visual job postings that treats the job listing as a media-first experience rather than a text document. The brand's signature move is a saturated blue gradient from #090a3f to #2a93f4 that wraps hero sections and primary CTAs, creating a sense of depth that feels like looking into a lit screen — appropriate for a company selling webcams as the hiring interface. Warm accents of #e89e50 (a toasted amber) and #ff7a59 (coral) punctuate badges, secondary buttons, and notification dots, providing the only relief from an otherwise cool palette. Typography runs Poppins at 500–600 weight for headings and Lato at 400 for body, both geometric sans-serifs that read clean at small sizes on video overlays. Cards use `{rounded.md}` (12px) corners, while primary buttons and search inputs take `{rounded.sm}` (8px) — the brand avoids pill shapes entirely, preferring a squared-off professionalism that signals enterprise readiness. The extracted palette shows heavy blue dominance (#0283fa, #006bff, #0083fa, #4b91ed, #2e7cf7) suggesting a multi-tone blue system where each shade maps to a specific interaction state: #2a93f4 for primary, #0283fa for hover, #006bff for active. Purple accents (#8f53e7, #8459e9, #bf45d5) appear in feature badges and premium tiers, while the gray scale (#7a7a7a, #a1a1a1, #d2d2d2, #dadada) handles secondary text and disabled states. The brand's voice is direct and capability-focused — no whimsy, no illustration, just clear hierarchy and high-contrast readability against the navy backdrop.

colors:
  primary: "#2a93f4"
  primary-hover: "#0283fa"
  primary-active: "#006bff"
  primary-disabled: "#a1a1a1"
  ink: "#090a3f"
  body: "#606060"
  body-dark: "#05002d"
  muted: "#7a7a7a"
  muted-soft: "#a1a1a1"
  hairline: "#d2d2d2"
  hairline-soft: "#dadada"
  canvas: "#fbfbfb"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#e89e50"
  accent-coral: "#ff7a59"
  accent-purple: "#8f53e7"
  accent-purple-light: "#8459e9"
  accent-purple-bright: "#bf45d5"
  blue-deep: "#00449e"
  blue-mid: "#3d85c6"
  blue-light: "#53b8fb"
  navy: "#011e24"
  scrim: "#090a3f"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Arial', 'Helvetica', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Arial', 'Helvetica', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Lato', 'Arial', 'Helvetica', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "'Lato', 'Arial', 'Helvetica', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
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
    padding: 12px 28px
    height: 48px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  button-accent-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
    height: 40px
  button-accent-coral:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 24px
    height: 40px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-coral}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 64px
    boxShadow: "0 2px 8px rgba(9,10,63,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    gradient: "linear-gradient(135deg, {colors.ink} 0%, {colors.blue-deep} 100%)"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 36px
    height: 56px
  hero-secondary-cta:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 36px
    height: 56px
    border: "1px solid rgba(255,255,255,0.3)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 2px 12px rgba(9,10,63,0.06)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    boxShadow: "0 8px 24px rgba(9,10,63,0.1)"
  product-card-image:
    rounded: "{rounded.md}"
    height: 200px
    objectFit: cover
  badge-new:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-premium:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-feature:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  search-icon:
    color: "{colors.muted}"
    size: 20px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 32px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    height: 4px
    rounded: "{rounded.full}"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the platform, rendered in `{colors.primary}` (#2a93f4) with white text. On hover, shifts to `{colors.primary-hover}` (#0283fa) for a subtle brightening effect. Active state uses `{colors.primary-active}` (#006bff), and disabled state drops to `{colors.primary-disabled}` (#a1a1a1). All primary buttons use `{rounded.sm}` (8px) corners — no pill shapes. The `button-lg` variant (used in hero sections) increases padding to 16px 36px and height to 56px with `{typography.button-lg}`.

**`button-secondary`** — Outlined variant on white background with `{colors.ink}` text and a `{colors.hairline}` border. Hover state reveals a `{colors.primary}` border and `{colors.surface-soft}` background, providing a clear affordance without competing with the primary button.

**`button-accent-amber`** and **`button-accent-coral`** — Used for secondary actions that need visual distinction: amber (#e89e50) for "Featured" or "Promoted" actions, coral (#ff7a59) for "Urgent" or "Limited Time" CTAs. Both use `{typography.button-sm}` to sit alongside larger primary buttons without visual conflict.

**`button-text-link`** — A text-only button styled as a link, used for "Learn more", "View details", and "Cancel" actions. No background, no border, just `{colors.primary}` text that underlines on hover.

### Cards
**`product-card`** — The core content container for job listings and webcam profiles. White background with `{rounded.md}` (12px) corners and a subtle shadow (`0 2px 12px rgba(9,10,63,0.06)`). On hover, the shadow deepens to `0 8px 24px rgba(9,10,63,0.1)` to signal interactivity. Cards contain an image area (`{rounded.md}`, 200px height), title, description, and action buttons. Padding is `{spacing.lg}` (24px) for comfortable reading.

**`product-card-image`** — The media container within a card, using `object-fit: cover` to maintain aspect ratio. No border radius on the image itself — the card's `{rounded.md}` clips the top corners naturally.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height with white background and `{colors.ink}` text. A subtle bottom border (`1px solid {colors.hairline-soft}`) separates it from content. On scroll, the nav compresses to 64px and gains a light shadow (`0 2px 8px rgba(9,10,63,0.08)`). Navigation links use `{typography.nav-link}` (Poppins 15px, weight 500) with active state underlined in `{colors.primary}`.

**`nav-link-active`** — Active nav item with `{colors.primary}` text and a 2px bottom border in the same blue. Inactive items use `{colors.muted}` (#7a7a7a) to de-emphasize.

### Forms
**`text-input`** — Standard text input with white background, `{colors.body}` text, and a `{colors.hairline}` border. On focus, the border thickens to 2px and shifts to `{colors.primary}`. Error state uses `{colors.accent-coral}` (#ff7a59) border. All inputs use `{rounded.sm}` (8px) and 48px height for comfortable touch targets.

**`select-input`** — Dropdown variant matching the text input styling, with a custom chevron in `{colors.muted}`. Same height, padding, and border treatment.

**`textarea`** — Multi-line input for job descriptions and application questions. Same styling as text inputs but without fixed height — min-height of 120px recommended.

### Badges
**`badge-new`** — Amber (#e89e50) badge for "New" or "Just posted" labels. Uses `{typography.badge}` (Poppins 11px uppercase, weight 600) with `{rounded.xs}` (4px) corners. Compact padding (2px 8px) keeps it unobtrusive.

**`badge-premium`** — Purple (#8f53e7) badge for premium or sponsored listings. Same typography and sizing as the new badge, but the purple signals exclusivity.

**`badge-feature`** — Coral (#ff7a59) badge for featured or promoted content. Used sparingly to draw attention to high-priority items.

### Search
**`search-bar`** — The primary search input for finding jobs or webcams. White background with `{colors.hairline}` border and `{colors.body}` placeholder text. On focus, the border becomes 2px `{colors.primary}`. A `search-icon` in `{colors.muted}` sits at the left edge. The bar is 48px tall with `{rounded.sm}` corners.

**`filter-chip`** — Toggleable filter buttons for refining search results. Light gray background (`{colors.surface-soft}`) with `{colors.body}` text and a `{colors.hairline}` border. Active state fills with `{colors.primary}` and white text. Chips are 36px tall with `{rounded.sm}` corners.

### Footer
**`footer`** — Full-width footer on `{colors.ink}` (#090a3f) background with white text. Links use `{colors.muted-soft}` (#a1a1a1) and lighten to white on hover. Padding is `{spacing.xxl}` (48px) vertically and `{spacing.xl}` (32px) horizontally.

### Dividers
**`divider`** — Standard 1px line in `{colors.hairline}` (#d2d2d2) for separating sections. **`divider-soft`** uses `{colors.hairline-soft}` (#dadada) for less visual weight.

### Loading & Progress
**`loading-spinner`** — Circular spinner in `{colors.primary}` at 32px diameter. Used for async operations like loading search results or submitting forms.

**`progress-bar`** — Thin (4px) progress indicator with `{rounded.full}` ends. Background is `{colors.hairline}`, fill is `{colors.primary}`. Used for multi-step forms and upload progress.

**`tooltip`** — Dark tooltip on `{colors.ink}` background with white text. Uses `{typography.caption-sm}` (Lato 12px) and `{rounded.xs}` (4px) corners. Padding is 6px 12px for compact information display.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav compresses to hamburger menu; hero text drops to `{typography.display-md}` (28px); product cards stack vertically; search bar becomes full-width; filter chips wrap to two rows; footer links stack |
| Tablet | 744–1128px | Two-column grid for product cards; nav shows top-level links only; hero uses `{typography.display-lg}` (36px); search bar remains full-width with filter chips in a horizontal scroll |
| Desktop | 1128–1440px | Three-column grid for product cards; full nav with all links; hero uses `{typography.display-xl}` (48px); search bar centered with max-width 640px; filter chips in a single row |
| Wide | > 1440px | Max-width container at 1440px; content centered; hero section expands with wider gradient; product cards grid can show 4 columns; extra whitespace around search bar |

### Touch Targets
- All interactive elements (buttons, inputs, chips) maintain minimum 44px height for touch accessibility
- Primary CTAs are 48px height with 28px horizontal padding for easy tapping
- Filter chips at 36px height are the smallest touch target — acceptable for secondary controls
- Nav links have 44px minimum tap area even when text is smaller
- Search bar at 48px height provides ample touch surface

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px, with a slide-out drawer for links
- Product card grid collapses from 4 columns → 3 → 2 → 1 as viewport narrows
- Hero section reduces typography size and stacks CTAs vertically below 744px
- Filter chips switch from horizontal row to wrapped grid below 744px
- Footer columns stack to single column below 744px
- Sidebar filters (if present) collapse into a modal or bottom sheet below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components are inferred from extracted colors — actual transition durations, easing curves, and shadow animations were not extractable
- Error state styling for forms (error messages, validation icons) is assumed based on coral accent — exact implementation unknown
- Dark mode is not present in extracted data — all colors assume light theme
- Typography hierarchy (font sizes, weights, line heights) is reconstructed from extracted font declarations and common patterns — exact scale may differ
- Spacing values are estimated from common design system patterns — actual padding/margin values may vary
- The extracted color list contains many blue variants (#0283fa, #006bff, #0083fa, #4b91ed, #2e7cf7) that may represent a multi-tone blue system — exact mapping to states (hover, active, visited, disabled) is inferred
- Purple accents (#8f53e7, #8459e9, #bf45d5) appear in extracted data but their specific use cases (premium badges, feature highlights, tier indicators) are assumed
- The brand may use additional accent colors not captured in extraction (green for success, red for errors beyond coral)
- Icon library and illustration style are unknown — FontAwesome presence suggests icon support but no custom icon set was detected
- Animation and transition specifications (duration, easing, keyframes) are not available
- Focus ring styling (outline, offset, color) for keyboard accessibility is not extractable
- Print stylesheet and reduced-motion preferences are not documented
