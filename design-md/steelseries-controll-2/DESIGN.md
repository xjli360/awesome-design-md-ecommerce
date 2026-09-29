---
version: alpha
name: "SteelSeries"
source_url: "https://steelseries.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dark, precise gaming-hardware brand that uses its own violet #9a8be5 as the single signal color against a near-black #383838 canvas — a deliberate inversion of the typical gaming RGB rainbow. The brand's visual system is built on hard corners and tight tolerances: product shots sit in 4px rounded frames (`{rounded.xs}`), buttons use 8px corners (`{rounded.sm}`), and the only generous radius is reserved for the search bar at `{rounded.full}`. Typography runs system-native — -apple-system, Helvetica, Roboto — at modest weights (400–500 for body, 600 for buttons), never competing with the product imagery. The primary CTA uses the violet #9a8be5 on white, while secondary actions drop to a transparent background with a 1px hairline in #383838. Navigation is a persistent 64px dark bar with white text and a subtle 1px bottom border, housing a search icon that expands into a full-width pill on interaction. Product cards are flat, borderless, and rely on the contrast between #383838 backgrounds and white text, with hover states that reveal a subtle violet glow. The brand avoids gradients, shadows, and decorative flourishes — every element serves the product, and the product is always the brightest thing on screen.

colors:
  primary: "#9a8be5"
  primary-active: "#703cd3"
  primary-disabled: "#c4bcf0"
  ink: "#ffffff"
  body: "#e0e0e0"
  muted: "#a0a0a0"
  muted-soft: "#707070"
  hairline: "#383838"
  hairline-soft: "#484848"
  canvas: "#1a1a1a"
  surface-soft: "#242424"
  surface-card: "#2a2a2a"
  on-primary: "#ffffff"
  accent-violet: "#9a8be5"
  accent-purple: "#703cd3"
  dark-bg: "#383838"
  dark-bg-soft: "#444444"
  error: "#ff4444"
  success: "#44cc44"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.dark-bg-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  search-bar-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  search-bar-expanded:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
  product-card-image:
    backgroundColor: "{colors.dark-bg}"
    rounded: "{rounded.xs}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 80px 0
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 52px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
  dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  dropdown-item:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 8px 16px
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: 8px 16px
  slider-track:
    backgroundColor: "{colors.dark-bg-soft}"
    height: 4px
    rounded: "{rounded.full}"
  slider-thumb:
    backgroundColor: "{colors.primary}"
    height: 16px
    rounded: "{rounded.full}"
  slider-thumb-active:
    backgroundColor: "{colors.primary-active}"
    height: 16px
    rounded: "{rounded.full}"
  toggle-track:
    backgroundColor: "{colors.dark-bg-soft}"
    height: 24px
    rounded: "{rounded.full}"
  toggle-track-active:
    backgroundColor: "{colors.primary}"
    height: 24px
    rounded: "{rounded.full}"
  toggle-thumb:
    backgroundColor: "{colors.ink}"
    height: 20px
    rounded: "{rounded.full}"
  toggle-thumb-active:
    backgroundColor: "{colors.ink}"
    height: 20px
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary action button uses the brand's violet #9a8be5 on a white label, with 8px rounded corners and 12px vertical padding. On hover, it shifts to the deeper purple #703cd3. The disabled state drops to a lighter violet #c4bcf0, maintaining readability while signaling inactivity. The button height is 44px, designed to sit comfortably alongside form fields and product cards.

**`button-secondary`** — A transparent button with a 1px violet border and violet text, used for secondary actions like "Learn More" or "Compare". The hover state fills the background with a dark tint #444444 and deepens the text to #703cd3. The 11px vertical padding accounts for the 1px border to maintain the same 44px height as the primary button.

**`button-ghost`** — A text-only button with no border or background, used for tertiary actions like "Cancel" or "View Details". The text sits in the body color #e0e0e0, shifting to violet on hover with a subtle dark background #242424. This is the quietest button variant, reserved for low-priority actions.

### Text Inputs
**`text-input`** — A 48px tall input field with a dark surface background #2a2a2a and light body text #e0e0e0. The 8px rounded corners match the button radius, creating visual consistency across form elements. On focus, the border shifts to the primary violet. The error state uses a red border #ff4444 with the same dark background, keeping the error visible without overwhelming the user.

### Navigation
**`nav-bar`** — A persistent 64px dark bar (#1a1a1a) with white navigation links. The bar uses a subtle 1px bottom border in #383838 to separate it from the page content. On scroll, the bar shrinks to 56px, reducing the logo and link sizes slightly. Active nav links use the primary violet, while inactive links sit in #a0a0a0.

**`nav-link-active`** — Active navigation links use the primary violet #9a8be5 with no background or border. The link sits at 14px with 0.3px letter spacing, matching the brand's preference for tight, precise typography.

**`nav-link-inactive`** — Inactive navigation links use the muted gray #a0a0a0, maintaining readability without competing with the active state. On hover, they shift to the primary violet.

### Search
**`search-bar-pill`** — A compact 40px pill-shaped search bar with a dark surface background #2a2a2a and muted placeholder text #a0a0a0. The full rounded radius (`{rounded.full}`) is the only generous curve in the system, making the search action feel distinct and inviting. On interaction, it expands to a 48px version with brighter text and a wider padding.

**`search-bar-expanded`** — The expanded state of the search bar, triggered by focus or click. The height increases to 48px, padding widens to 12px 20px, and the text shifts to the body color #e0e0e0. The background remains the same dark surface, ensuring the transition feels smooth and intentional.

### Product Cards
**`product-card`** — A flat, borderless card with a dark surface background #2a2a2a and white text. The card uses 4px rounded corners (`{rounded.xs}`), the smallest radius in the system, keeping the focus on the product image. On hover, a subtle violet glow appears around the card edges, signaling interactivity without adding visual noise.

**`product-card-image`** — The product image container uses a darker background #383838 with 4px rounded corners. Images are the brightest element on the card, often featuring the product against a white or gradient background for maximum contrast.

### Badges
**`badge-new`** — A small violet badge with white text, used to mark new products or features. The badge uses 4px rounded corners and 2px 8px padding, sitting compactly in the top corner of product cards or navigation items.

**`badge-sale`** — A red badge (#ff4444) with white text, used for sale or discount indicators. The red provides immediate visual contrast against the dark surface, drawing attention to price reductions.

**`badge-out-of-stock`** — A muted gray badge (#707070) with white text, used for out-of-stock items. The gray signals unavailability without the harshness of a red error state.

### Hero Section
**`hero-section`** — A full-width section with a dark background (#1a1a1a) and large white display text. The section uses 80px vertical padding, creating generous breathing room around the headline and CTA. The hero often features a product image or video as the primary visual, with the text and CTA overlaid.

**`hero-cta`** — A larger version of the primary button, using 14px 32px padding and a 52px height. The button uses the same violet #9a8be5 but with larger typography (`{typography.button-lg}`) to match the hero's scale.

### Footer
**`footer`** — A dark footer (#1a1a1a) with muted gray links (#a0a0a0) and 48px vertical padding. The footer uses the same background as the nav bar, creating a visual bookend for the page. Links shift to violet on hover, maintaining the brand's consistent interaction pattern.

**`footer-link`** — Footer links use the muted gray #a0a0a0 at 14px with no decoration. On hover, they shift to the primary violet #9a8be5, providing a subtle but clear interaction cue.

### Dividers
**`divider`** — A 1px horizontal line in #383838, used to separate sections or content blocks. The dark gray provides subtle separation without adding visual weight.

**`divider-soft`** — A lighter 1px horizontal line in #484848, used for less prominent separations like within cards or dropdowns.

### Icon Buttons
**`icon-button`** — A 40px circular button with a transparent background and muted gray icon. On hover, the background fills with a dark tint #242424 and the icon shifts to violet. This is used for actions like search, cart, or user menu.

### Dropdowns
**`dropdown`** — A floating menu with a dark surface background #2a2a2a and 8px rounded corners. The dropdown uses 8px vertical padding and contains items with 8px 16px padding. On hover, items shift to a dark tint #242424 with violet text.

**`dropdown-item`** — Individual dropdown items use the body color #e0e0e0 with no background. On hover, the background shifts to #242424 and the text shifts to violet, providing a clear hover state.

### Sliders
**`slider-track`** — A 4px tall track in #444444 with full rounded corners. The track provides a subtle path for the slider thumb.

**`slider-thumb`** — A 16px circular thumb in the primary violet #9a8be5. On hover or drag, the thumb shifts to the deeper purple #703cd3. The thumb is the most interactive element on the slider, using the brand's signal color.

### Toggles
**`toggle-track`** — A 24px tall pill-shaped track in #444444. When active, the track fills with the primary violet #9a8be5.

**`toggle-thumb`** — A 20px circular thumb in white, sitting inside the track. When active, the thumb shifts to the right side of the track, maintaining the same white color for consistency.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; hero text reduces to 24px; search bar becomes full-width; footer links stack vertically |
| Tablet | 744–1128px | Nav bar shows limited links (Home, Products, Support); product cards display in 2-column grid; hero uses 28px text; search bar remains pill-shaped but wider |
| Desktop | 1128–1440px | Full nav bar with all links; product cards in 3-column grid; hero uses 32px text; search bar sits in nav bar |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero uses 36px text; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons use 40px diameter, meeting the 44px touch target recommendation with 2px padding
- Dropdown items use 40px height with 8px 16px padding for comfortable tapping
- Toggle switches use 24px track height with 20px thumb for easy manipulation
- Slider thumbs use 16px diameter, slightly below the 44px recommendation but acceptable for precision controls

### Collapsing Strategy
- Nav bar collapses to hamburger menu below 744px, hiding all navigation links behind a single icon
- Product cards collapse from 3-column grid to 2-column at tablet, then single column at mobile
- Hero section reduces padding from 80px to 48px on mobile, with text scaling down proportionally
- Footer links collapse from horizontal rows to vertical stack below 744px
- Search bar expands from pill to full-width input on mobile, maximizing usable space
- Dropdowns convert to full-screen overlays on mobile for easier navigation

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is limited to three hex values (#9a8be5, #703cd3, #383838) from the live site's HTML and CSS. The brand likely uses additional colors for accents, errors, and success states that were not captured. The error (#ff4444) and success (#44cc44) colors in this document are inferred from common gaming-hardware conventions and may not match the actual brand.
- Font-family declarations were extracted as system-native stacks (-apple-system, Helvetica, Roboto, etc.). SteelSeries may use a custom typeface (e.g., a proprietary gaming font) that was not loaded in the captured page state. The typography tokens use the extracted system stack as a fallback.
- Hover states for product cards (violet glow) and button variants are inferred from common design patterns and may not reflect the actual implementation.
- Dark mode is the default and only mode captured. The brand may have a light mode variant that was not detected.
- Error and success states for forms, validation messages, and toast notifications were not captured from the live site.
- The brand's logo, icon set, and illustration style were not extracted. These are significant visual elements that should be documented separately.
- Animation and transition timings (hover effects, scroll behaviors, modal transitions) were not captured.
- The brand's grid system and container widths were not extracted. The responsive breakpoints are estimated based on common patterns.
- Accessibility states (focus rings, aria labels, keyboard navigation) were not documented. These should be added based on WCAG 2.1 AA compliance.
- The brand may use additional component variants (e.g., different button sizes, card layouts, or navigation patterns) that were not present in the captured page state.
