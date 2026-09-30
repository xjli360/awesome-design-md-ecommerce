---
version: alpha
name: "Seventh Generation"
source_url: "https://seventhgeneration.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep green (#006449) anchors a brand that treats household cleaning as an act of environmental stewardship, not just surface sanitation. That primary green — the color of a forest canopy at dusk — runs through every primary button, every navigation accent, and every product-badge border, while a secondary leaf-green (#4d8000) and a high-contrast safety-orange (#ff3008) provide the voltage for limited-time offers and ingredient-callout icons. The canvas is a clean off-white (#f7f7f7) that reads as unbleached paper, and body text sits in a warm charcoal (#494a4d) rather than pure black — a deliberate softening that avoids the harshness of petrochemical blacks. The brand uses Arial and ps-roobert (a geometric sans with slightly condensed proportions) at modest sizes: display headlines rarely exceed 28px, and body copy stays at 16px with generous line-height (1.6) to keep dense ingredient lists and sustainability claims readable. Corners are soft but not pill-shaped — buttons use {rounded.sm} (8px), cards use {rounded.md} (12px), and only the search bar reaches {rounded.full} (9999px), creating a single focal point of maximum approachability. The visual system trusts white space and photography over decorative elements: product shots float on white backgrounds with thin {hairline} (#dedede) borders, and the only decorative flourish is a subtle leaf-icon watermark on hero sections. The result is a brand that feels serious without being stern, activist without being strident — a household name that looks like it belongs in a CSA box, not a supermarket aisle.

colors:
  primary: "#006449"
  primary-active: "#015b42"
  primary-disabled: "#d4e3d8"
  ink: "#232323"
  body: "#494a4d"
  muted: "#53565b"
  muted-soft: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#ededed"
  canvas: "#f7f7f7"
  surface-soft: "#ededed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#4d8000"
  accent-orange: "#ff3008"
  accent-yellow: "#fffa90"
  accent-yellow-dark: "#777620"
  accent-blue: "#003399"
  accent-sky: "#51c9ee"
  badge-green: "#e3f1ca"
  star-rating: "#006449"

typography:
  display-xl:
    fontFamily: "'ps-roobert', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.28px
  display-lg:
    fontFamily: "'ps-roobert', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-md:
    fontFamily: "'ps-roobert', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.36
    letterSpacing: 0
  title-lg:
    fontFamily: "'ps-roobert', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'ps-roobert', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'ps-roobert', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.16px
  button-sm:
    fontFamily: "'ps-roobert', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.14px
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "'ps-roobert', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.14px
  badge:
    fontFamily: "'ps-roobert', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.11px
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
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.accent-orange}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "2px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-item-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  top-nav-item-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px
  ingredient-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  ingredient-callout-icon:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  sustainability-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  footer-link-hover:
    typography: "{typography.link}"
    textColor: "{colors.accent-yellow}"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 40px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.base} 0"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 8px
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-switch-knob:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.full}"
    height: 20px
  checkbox:
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
    size: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    size: 20px
  radio:
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    size: 20px
  radio-checked:
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    size: 20px
  radio-dot:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    size: 10px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"
  badge-new:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.accent-yellow-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-plant-based:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with {colors.primary} (#006449) deep green and white text. Used for "Shop Now", "Subscribe", and "Learn More" actions. On hover, shifts to {colors.primary-active} (#015b42) for a subtle darkening. Disabled state uses {colors.primary-disabled} (#d4e3d8) with {colors.muted-soft} text, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined variant with a white fill and {colors.primary} border and text. Used for secondary actions like "Compare Products" or "View Details". Active state darkens the border to {colors.primary-active} and adds a {colors.surface-soft} background. The 2px border maintains visual weight parity with the filled primary button.

**`button-tertiary`** — A text-only button with no background or border, using {colors.primary} text. Used for inline actions like "Read More" or "See Ingredients". Padding matches primary button height for alignment in form layouts.

**`button-accent-green`** — A high-energy variant using {colors.accent-green} (#4d8000), the brand's secondary leaf-green. Used for sustainability certifications, plant-based ingredient callouts, and eco-friendly shipping options. Creates visual hierarchy alongside the primary green.

**`button-accent-orange`** — An urgent-action variant using {colors.accent-orange} (#ff3008). Reserved for limited-time offers, clearance sales, and donation-match campaigns. The high contrast against the green palette draws immediate attention.

### Navigation
**`top-nav`** — A fixed-height 64px bar on {colors.canvas} (#f7f7f7) with {colors.ink} (#232323) nav links. The brand logo sits left-aligned, with category links (Cleaning, Laundry, Dish, Baby, Personal Care) center-aligned. Active items show a 3px {colors.primary} bottom border. Hover state shifts text to {colors.primary} without the border, keeping the active indicator unique.

**`top-nav-item-active`** — The currently selected navigation item, distinguished by a 3px solid {colors.primary} bottom border. Text color shifts to {colors.primary} to reinforce the active state. No background change — the brand relies on the underline and color shift rather than a filled tab.

**`top-nav-item-hover`** — Non-active items shift text to {colors.primary} on hover, with no underline. This creates a subtle preview of the active state without competing with the current selection indicator.

### Cards
**`product-card`** — A white card with {rounded.md} (12px) corners and no background fill (transparent to the {colors.canvas} page background). Product images sit flush to the top with rounded top corners only, creating a magazine-like float. Title uses {typography.title-md} in {colors.ink}, price uses {typography.body-md} in {colors.body}. Badges overlay the image top-left.

**`product-card-image`** — The product photo area, with rounded corners only at the top ({rounded.md} top-left and top-right). This creates a visual anchor where the image appears to emerge from the card. No border — the image edges define the card boundary.

**`product-card-title`** — Product name in {typography.title-md} (18px, weight 600) with {colors.ink} (#232323). Positioned below the image with {spacing.base} (16px) padding on left and right, {spacing.base} top, {spacing.xs} (4px) bottom. The tight spacing keeps the title close to the price.

**`product-card-price`** — Pricing in {typography.body-md} (16px, weight 400) with {colors.body} (#494a4d). Positioned below the title with padding on left, right, and bottom ({spacing.base}). No dollar sign styling — the brand uses standard currency formatting.

**`product-card-badge`** — A small green badge overlaid on the product image, using {colors.badge-green} (#e3f1ca) background and {colors.primary} (#006449) text. Uses {typography.badge} (11px, weight 700, uppercase). Content includes "Plant-Based", "EPA Safer Choice", or "Cruelty-Free". Positioned top-left with {spacing.xs} offset.

### Forms
**`text-input`** — Standard text input with white background, {colors.body} text, and a 1px {colors.hairline} (#dedede) border. {rounded.sm} (8px) corners. Focus state upgrades to a 2px {colors.primary} border, maintaining the same padding to avoid layout shift. Error state uses a 2px {colors.accent-orange} (#ff3008) border.

**`text-input-focus`** — The focused state, distinguished by a 2px solid {colors.primary} (#006449) border. The thicker border replaces the 1px hairline without changing the overall input dimensions (padding remains 12px 16px). No glow or shadow — the brand avoids decorative focus indicators.

**`text-input-error`** — Error state with a 2px {colors.accent-orange} (#ff3008) border. The orange provides high contrast against the green palette and signals urgency without using red (which could conflict with the brand's natural aesthetic). Error message appears below in {typography.caption} with {colors.accent-orange} text.

**`select-input`** — Dropdown select styled identically to text inputs: white background, 1px {colors.hairline} border, {rounded.sm} corners. The dropdown arrow uses {colors.primary} (#006449) for brand consistency. Focus state mirrors text-input focus with a 2px {colors.primary} border.

**`search-bar`** — The only component using {rounded.full} (9999px), creating a pill-shaped search field that stands out as the most approachable element in the system. White background with 1px {colors.hairline} border. Focus state upgrades to a 2px {colors.primary} border. The pill shape contrasts with the {rounded.sm} buttons and {rounded.md} cards, making search the single most inviting interaction point.

**`newsletter-input`** — Email input styled consistently with standard text inputs but designed to pair with the newsletter-submit button. White background, 1px {colors.hairline} border, {rounded.sm} corners. The input and submit button share the same height (48px and 40px respectively) for a clean inline form.

**`newsletter-submit`** — A compact submit button using {colors.accent-green} (#4d8000) background. Slightly shorter (40px) than the primary button (48px) to create visual hierarchy when paired with the newsletter input. Uses {typography.button-sm} (14px, weight 600) for a more contained appearance.

### Hero & Content
**`hero-section`** — Full-width section on {colors.canvas} (#f7f7f7) with {spacing.section} (64px) vertical padding. Display headline uses {typography.display-xl} (28px, weight 700) in {colors.ink} (#232323). A single CTA button sits below the headline. Background may feature a subtle leaf-icon watermark at low opacity.

**`hero-cta`** — The hero's primary action button, identical to `button-primary` but with wider horizontal padding (32px vs 24px) to match the hero's generous scale. Deep green fill with white text, {rounded.sm} corners.

**`ingredient-callout`** — A soft gray box on {colors.surface-soft} (#ededed) with {rounded.sm} corners and {spacing.base} padding. Used to highlight specific ingredient information (e.g., "Made with plant-based enzymes"). An icon sits to the left in a green circle ({colors.accent-green}, {rounded.full}).

**`ingredient-callout-icon`** — A 32px circular icon container using {colors.accent-green} (#4d8000) fill and white icon. The {rounded.full} shape creates a friendly, approachable visual for ingredient highlights. Icon content varies (leaf, droplet, plant, etc.).

**`sustainability-badge`** — A small green badge using {colors.badge-green} (#e3f1ca) background and {colors.primary} (#006449) text. {rounded.xs} (4px) corners. Used for "EPA Safer Choice", "Plant-Based", "Cruelty-Free", and "Recyclable" labels. The uppercase {typography.badge} keeps text compact.

### Footer
**`footer-section`** — A deep green footer using {colors.primary} (#006449) as background with white text. {spacing.xxl} (48px) vertical padding. Contains link columns, newsletter signup, and social icons. The dark footer creates a visual bookend with the light hero section.

**`footer-link`** — Standard footer link in white ({colors.on-primary}) using {typography.link} (14px, weight 400). No underline in default state for a clean appearance. Hover state shifts to {colors.accent-yellow} (#fffa90) for high-contrast feedback against the dark green background.

**`footer-link-hover`** — Hover state for footer links, shifting text color to {colors.accent-yellow} (#fffa90). The yellow provides the highest contrast against {colors.primary} (#006449) background, ensuring accessibility while maintaining brand color usage. No underline decoration.

### Interactive Elements
**`accordion-header`** — Expandable section header on {colors.canvas} with {colors.ink} text in {typography.title-md} (18px, weight 600). Bottom border of 1px {colors.hairline} separates items. Padding of {spacing.base} top and bottom creates comfortable tap targets. A chevron icon rotates on expand.

**`accordion-content`** — The expandable content area, with {spacing.base} bottom padding and no top padding (content sits directly below the header). Uses {typography.body-md} (16px, weight 400) in {colors.body} (#494a4d). Transition animation uses 300ms ease-in-out.

**`star-rating`** — Product rating stars in {colors.star-rating} (#006449), the brand's primary green. Stars are 16px each, with half-star support for precise ratings. Empty stars use {colors.hairline} (#dedede) for low-contrast unfilled states.

**`progress-bar`** — Thin 8px bar with {rounded.full} corners on {colors.hairline} (#dedede) background. The fill uses {colors.primary} (#006449) with matching rounded corners. Used for subscription progress, donation meters, and loading states.

**`toggle-switch`** — A 24px tall pill-shaped toggle with {rounded.full} corners. Inactive state uses {colors.hairline} (#dedede) background. Active state uses {colors.primary} (#006449). The 20px circular knob slides horizontally with a 200ms transition.

**`toggle-switch-active`** — Active toggle state with {colors.primary} (#006449) background. The knob slides to the right side, maintaining the 20px diameter for consistent visual weight.

**`toggle-switch-knob`** — The circular knob element, 20px in diameter with {rounded.full} corners and white ({colors.surface-card}) fill. Casts a subtle shadow (1px offset, 2px blur) for depth. Positioned with 2px margin from the toggle edges.

**`checkbox`** — A 20px square checkbox with {rounded.xs} (4px) corners and a 2px {colors.hairline} (#dedede) border. Checked state fills with {colors.primary} (#006449) and displays a white checkmark. The 2px border ensures visibility against white backgrounds.

**`checkbox-checked`** — Checked checkbox with {colors.primary} (#006449) fill and 2px {colors.primary} border. The white checkmark icon uses a 2px stroke width for clarity at small sizes. The {rounded.xs} corners match the unchecked state.

**`radio`** — A 20px circular radio button with 2px {colors.hairline} (#dedede) border. Selected state shows a 10px {colors.primary} (#006449) dot centered inside a 2px {colors.primary} border. The dot-to-border ratio (10px dot in 20px container) provides clear visual distinction.

**`radio-checked`** — Selected radio button with 2px {colors.primary} (#006449) border. The inner dot uses {colors.primary} fill at 10px diameter, centered with 5px margin from the outer border. No animation on selection — instant state change.

**`radio-dot`** — The inner fill dot for selected radio buttons, 10px diameter with {rounded.full} corners and {colors.primary} (#006449) fill. Positioned with 5px offset from the outer border edge.

**`loading-spinner`** — A 24px circular spinner using {colors.primary} (#006449) as the stroke color. The spinner arc spans approximately 270 degrees with a 3px stroke width. Animation rotates at 1.5 seconds per revolution with a linear timing function.

**`divider`** — A 1px horizontal line using {colors.hairline} (#dedede). Used between major sections and form fields. Full width with no margin — spacing is handled by parent container padding.

**`divider-soft`** — A 1px horizontal line using {colors.hairline-soft} (#ededed), lighter than the standard divider. Used within cards and accordion content for subtle visual separation without competing with the card's structure.

**`tooltip`** — A dark tooltip with {colors.ink} (#232323) background and {colors.canvas} (#f7f7f7) text. Uses {typography.caption} (13px, weight 400) with {rounded.xs} (4px) corners and 6px 10px padding. A 6px triangular arrow points to the trigger element.

### Badges
**`badge-new`** — An orange badge using {colors.accent-orange} (#ff3008) background with white text. Used for "New" and "Just Launched" labels. The high-contrast orange creates urgency and draws attention to new products. Compact padding (2px 6px) keeps the badge small.

**`badge-sale`** — A yellow badge using {colors.accent-yellow} (#fffa90) background with {colors.accent-yellow-dark} (#777620) text. Used for "Sale", "Save", and promotional labels. The yellow-green combination maintains brand color harmony while signaling value.

**`badge-plant-based`** — A green badge using {colors.badge-green} (#e3f1ca) background with {colors.primary} (#006449) text. Used for "Plant-Based", "Vegan", and "Natural" certifications. The soft green background reinforces the brand's environmental positioning without competing with the primary green.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger menu; product cards stack vertically; hero padding reduces to {spacing.xl} (32px); search bar moves to sticky header; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; top-nav shows 4-5 category links; hero uses 50/50 text/image split; footer shows 2-column link layout; search bar in header |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all categories; hero uses 60/40 text/image split; footer shows 4-column link layout; search bar in header with full width |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; hero content centered with max-width 1200px; footer columns at max-width 1200px; search bar remains in header |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets extend to full card width for easy selection
- Accordion headers have 48px minimum height for comfortable tapping
- Toggle switches are 24px tall with 44px touch area via padding
- Checkbox and radio buttons have 44px touch area via label association

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with slide-in drawer from left
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer link columns collapse from 4 (desktop) to 2 (tablet) to stacked (mobile)
- Hero section stacks image below text on mobile, side-by-side on tablet and above
- Search bar moves from header to sticky top bar on mobile for persistent access
- Product filters collapse to a "Filter" button with modal overlay on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Only primary, secondary, and footer link hover states were extracted. Button hover animations, card hover effects (shadow elevation, image zoom), and navigation dropdown hover states are inferred from common patterns but not confirmed from the live site.
- **Error states**: Form error styling (text color, icon placement, error message typography) was not fully extracted. The error border color (#ff3008) is confirmed, but error message styling and animation are estimated.
- **Dark mode**: No dark mode implementation was detected. The brand's color palette (deep greens on white) suggests a light-only design system, but dark mode tokens are not available.
- **Sub-brand palettes**: Seventh Generation operates sub-brands (Baby, Personal Care, Cleaning) that may have distinct accent colors. Only the main brand palette was extracted.
- **Animation tokens**: No animation durations, easing curves, or transition properties were extracted. The 300ms accordion and 200ms toggle transitions are reasonable defaults.
- **Icon system**: The brand uses leaf, plant, droplet, and certification icons, but exact SVG paths, sizes, and color tokens were not extracted. Icon colors are assumed to use {colors.primary} and {colors.accent-green}.
- **Typography scale**: The extracted font-family list includes "ps-roobert" and Arial, but exact font sizes for all typography tokens (especially display variants below 28px) are estimated based on common DTC patterns. The brand may use additional weights (300, 400, 500, 600, 700) that were not all confirmed.
- **Spacing scale**: The spacing tokens (xxs through section) are based on common 8px grid patterns. The live site may use a different base unit or custom spacing values for specific components.
- **Component-specific tokens**: Badge positioning (offset from card edge), tooltip arrow size/direction, and loading spinner stroke width
