---
version: alpha
name: "Tushy"
source_url: "https://hellotushy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A warm, sustainable bathroom brand that uses a sky-blue primary (#71a7f4) as its visual anchor — a color that reads as clean water, fresh air, and modern hygiene rather than cold clinical white. The palette is built on a creamy off-white canvas (#fdf7f1) that feels like natural paper or unbleached cotton, with secondary blues (#346ab7, #487ecb) providing depth for navigation and interactive states. Peach and coral accents (#ffcf9f, #fcb68c, #f8cfa4) appear in illustrations, badges, and promotional elements, softening the brand's technical product (bidets) into something approachable and human. The typography runs Sofia Pro at moderate weights — display headlines sit at 500–700 weight, body text at 400, creating a clean editorial feel that lets product photography and sustainability messaging carry the emotional weight. Buttons use soft rounded corners ({rounded.sm}) and generous padding, while the primary CTA (#71a7f4 on white) stands out against the warm canvas without aggression. The brand's signature move is pairing its sky-blue primary with warm peach tones in badges and sale indicators, creating a visual temperature contrast that signals both trust and warmth. Error states use a restrained red (#e60000) that appears only in form validation, never in branding. The overall mood is calm, eco-conscious, and modern — a bathroom brand that wants you to feel good about water conservation without sacrificing comfort.

colors:
  primary: "#71a7f4"
  primary-active: "#346ab7"
  primary-disabled: "#cce0fd"
  ink: "#231f20"
  body: "#444444"
  muted: "#676986"
  muted-soft: "#b5b5ba"
  hairline: "#e5e5eb"
  hairline-soft: "#efefef"
  canvas: "#fdf7f1"
  surface-soft: "#f5f5f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-peach: "#ffcf9f"
  accent-coral: "#fcb68c"
  accent-warm: "#f8cfa4"
  badge-sale: "#e60000"
  badge-new: "#71a7f4"
  footer-bg: "#272d45"
  footer-text: "#ffffff"
  error: "#e60000"
  star-rating: "#ffcf9f"

typography:
  display-xl:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  footer-link:
    fontFamily: "'Sofia Pro', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    border: "1px solid {colors.primary}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.hairline-soft}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  text-input-error:
    border: "1px solid {colors.error}"
    backgroundColor: "{colors.canvas}"
  text-input-disabled:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 20px
    width: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  radio-checked:
    border: "6px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-active:
    backgroundColor: "{colors.primary}"
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  mobile-nav-toggle:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    height: 40px
    width: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-peach}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-rating:
    textColor: "{colors.star-rating}"
    fontSize: "14px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: "600px"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: "500px"
    marginTop: "{spacing.base}"
  hero-cta:
    marginTop: "{spacing.lg}"
  hero-image:
    rounded: "{rounded.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
    width: 20px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.footer-link}"
    textColor: "{colors.footer-text}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.footer-text}"
    marginBottom: "{spacing.base}"
  footer-divider:
    backgroundColor: "rgba(255,255,255,0.15)"
    height: "1px"
    margin: "{spacing.lg} 0"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    backgroundColor: "{colors.surface-soft}"
  accordion-header-hover:
    backgroundColor: "{colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-icon:
    textColor: "{colors.primary}"
    fontSize: "16px"
  badge:
    backgroundColor: "{colors.accent-peach}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 10px"
  badge-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 10px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 10px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 10px"
  divider:
    backgroundColor: "{colors.hairline}"
    height: "1px"
    margin: "{spacing.base} 0"
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: "1px"
    margin: "{spacing.base} 0"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    fontSize: "12px"
  tooltip-arrow:
    borderTop: "4px solid {colors.ink}"
  loading-spinner:
    border: "3px solid {colors.hairline-soft}"
    borderTop: "3px solid {colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
  loading-spinner-lg:
    height: 40px
    width: 40px
    borderWidth: "4px"
  skeleton:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
    height: "16px"
  skeleton-card:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.md}"
    height: "200px"
  modal-overlay:
    backgroundColor: "rgba(0,0,0,0.5)"
  modal-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  modal-close-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
  notification-success:
    backgroundColor: "#d4edda"
    textColor: "#155724"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid #c3e6cb"
  notification-error:
    backgroundColor: "#f8d7da"
    textColor: "#721c24"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid #f5c6cb"
  notification-info:
    backgroundColor: "#d1ecf1"
    textColor: "#0c5460"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid #bee5eb"
  notification-warning:
    backgroundColor: "#fff3cd"
    textColor: "#856404"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid #ffeeba"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
  breadcrumb:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.primary}"
  breadcrumb-separator:
    textColor: "{colors.muted-soft}"
    margin: "0 {spacing.xs}"
  tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "2px solid transparent"
  tab-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  tab-hover:
    textColor: "{colors.ink}"
  stepper:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  stepper-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  stepper-complete:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  stepper-line:
    backgroundColor: "{colors.hairline}"
    height: "2px"
  stepper-line-active:
    backgroundColor: "{colors.primary}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: "8px"
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  progress-bar-fill-complete:
    backgroundColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, using sky-blue (#71a7f4) on white. Appears on product pages, checkout flows, and hero sections. On hover, shifts to a deeper navy-blue (#346ab7) for clear feedback. Disabled state uses a pale blue (#cce0fd) to indicate non-interactivity while maintaining brand color association.

**`button-secondary`** — Outlined variant with a 2px sky-blue border on the warm canvas background (#fdf7f1). Used for secondary actions like "Learn More" or "Add to Cart" alternatives. Active state fills the background with the surface-soft tone and deepens the border to primary-active.

**`button-tertiary-text`** — A text-only button using the primary blue, used for inline actions like "View Details" or "See All". No background or border — relies on color alone for affordance.

**`button-ghost`** — Transparent background with ink-colored text, used in navigation and toolbar contexts. On hover, gains a subtle surface-soft background for hit-state feedback.

**`button-pill`** — Fully rounded pill shape using the primary blue, used for promotional badges, filter tags, and compact CTAs. The pill form signals approachability and is used sparingly for emphasis.

**`button-pill-outline`** — Outlined pill variant with a 1px border, used for secondary filter tags and category selections. Maintains the friendly pill shape without full color fill.

### Cards
**`product-card`** — White card with 12px rounded corners and a subtle drop shadow (1px offset, 4px blur). Contains product image, title, price, and optional badges. On hover, shadow deepens to 4px offset with 12px blur for a gentle lift effect. Badges use peach (#ffcf9f) for standard labels, red (#e60000) for sale items, and sky-blue (#71a7f4) for new arrivals.

**`skeleton`** and **`skeleton-card`** — Loading placeholders using the hairline-soft gray (#efefef), matching the card rounded corners. Skeleton cards maintain the same dimensions and border-radius as product cards to prevent layout shift.

### Navigation
**`nav-bar`** — Fixed-height (64px) navigation bar on the warm canvas background with a subtle bottom border. Sticky variant adds a light drop shadow on scroll. Active nav links use the primary blue with a 2px bottom border underline. Mobile toggle uses a 40px icon button with full rounding.

**`breadcrumb`** — Small caption text in muted gray, with links in primary blue and a centered dot separator. Used on product detail and category pages for orientation.

### Forms
**`text-input`** — Standard text input on canvas background with 8px rounded corners and a hairline border. Focus state doubles the border width and switches to primary blue. Error state uses red (#e60000) border. Disabled state fades to hairline-soft background with muted-soft text.

**`checkbox`** and **`radio`** — 20px controls with 2px hairline borders. Checked state fills with primary blue. Radio buttons use a 6px inner circle pattern for the checked state.

**`toggle`** — 44px wide, 24px tall pill with a 20px white knob. Active state fills with primary blue. Used for settings and preferences.

### Feedback & Status
**`notification-success`**, **`notification-error`**, **`notification-info`**, **`notification-warning`** — Colored notification banners using standard semantic colors (green, red, blue, yellow) with matching borders. Used for form submission feedback, cart updates, and system messages.

**`tooltip`** — Dark background (#231f20) with white text, 4px rounded corners, and a small arrow. Used for icon explanations and truncated text reveals.

**`loading-spinner`** — Circular spinner with a hairline-soft track and primary blue animated segment. Available in 24px (default) and 40px (large) sizes.

**`progress-bar`** — 8px tall pill-shaped bar with hairline-soft background and primary blue fill. Used in checkout steps and onboarding flows.

**`stepper`** — Circular step indicators (32px) for multi-step processes. Active and complete steps use primary blue fill; inactive steps use hairline-soft with connecting lines.

### Modals & Overlays
**`modal-overlay`** — Semi-transparent black (50% opacity) backdrop. Modal content uses white background with 12px rounded corners, 32px padding, and a deeper shadow (8px offset, 32px blur). Close button is a 32px icon circle that gains a hairline-soft background on hover.

### Badges & Tags
**`badge`** — Small uppercase labels using peach background (#ffcf9f) for standard tags, primary blue for informational tags, red for sale tags, and sky-blue for new-arrival tags. All badges use 4px rounded corners and 2px vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, hamburger navigation, stacked product cards, full-width hero, reduced font sizes (display-xl drops to 28px), accordion-style footer, sticky bottom cart bar |
| Tablet | 744–1128px | Two-column product grid, persistent top nav with condensed links, side-by-side hero content, 3-column footer, search bar collapses to icon |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links visible, hero with image and text side-by-side, 4-column footer, expanded search bar |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero content max-width constrained, additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons use 40px minimum touch area (32px icon + 4px padding)
- Product card tap targets (title, image, price) have 48px minimum hit areas
- Mobile nav toggle uses 44px touch target
- Checkbox and radio controls use 44px minimum tap area with invisible padding
- Bottom navigation (mobile) uses 56px tall buttons for thumb reach

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Multi-column footer collapses to accordion below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport shrinks
- Hero section stacks vertically below 744px (image below text)
- Search bar collapses to icon-only trigger below 744px, expands to full-width overlay on tap
- Sidebar filters collapse to horizontal scroll strip on mobile
- Table-based content (specs, size guides) collapses to stacked cards below 744px
- Multi-step checkout collapses to single-column stacked layout below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; actual brand hover animations (ease curves, duration) not extracted
- Focus-visible ring styles (color, offset, thickness) not present in extracted data — default browser focus may be used
- Error message styling for form validation (color, typography, iconography) not confirmed beyond red border
- Dark mode or high-contrast mode tokens not present in extracted data
- Sub-brand or promotional campaign color palettes (seasonal, limited edition) not captured
- Animation timing and easing curves (transitions, micro-interactions) not extracted
- Icon library and stroke weights not identified — SVG icons may use 1.5px or 2px strokes
- Image aspect ratios and focal-point cropping rules not documented
- Print stylesheet or email-specific styling not available
- Shopify-specific checkout widget colors may be mixed into extracted palette — Afterpay, Klarna, and Shopify Pay colors may appear as #b5b5ba, #e5e5eb, etc.
- The extracted color list is large (30 hex values) and likely includes social media icon colors, stock image dominant tones, and third-party widget colors — the true brand palette is likely smaller and more focused
- Font weight values for Sofia Pro are inferred from common web usage; actual brand weights may vary (e.g., 300 for light, 800 for heavy)
- Letter-spacing values for display typography are estimated based on common brand patterns
- The brand's true primary may be a distinctive peach or coral tone (#ffcf9f, #fcb68c) rather than the sky-blue (#71a7f4) — the extracted data shows high frequency of both blue and warm tones, suggesting a dual-palette approach where blue dominates UI elements and warm tones appear in illustrations and badges
