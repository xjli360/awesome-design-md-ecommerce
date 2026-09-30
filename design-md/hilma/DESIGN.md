---
version: alpha
name: "Hilma"
source_url: "https://hilma.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clean, science-forward wellness brand that uses a restrained palette of #121212 ink on a white canvas, with #007aff as its single accent — a crisp, clinical blue that reads as trustworthy rather than playful, more lab coat than apothecary. The site’s typography is minimal, with a single font-family declaration found (swiper-icons, likely a UI icon font), suggesting the brand relies on system fonts or a single loaded typeface for body and display — a pragmatic choice that keeps load times fast and the focus on product photography and ingredient callouts. The #dedede hairline appears frequently as a subtle separator, creating a clean grid that feels pharmaceutical in its precision. Hilma’s design language avoids the warm, earthy tones common in natural remedy brands; instead, it leans into a modern, almost clinical minimalism — white space is generous, product shots are large and well-lit, and the blue CTA buttons (`{rounded.sm}`) are the only visual punctuation. The overall mood is one of clarity and evidence: this is a brand that wants you to trust the science, not the vibe.

colors:
  primary: "#007aff"
  primary-active: "#0056cc"
  primary-disabled: "#b3d4ff"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
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
    padding: 12px 24px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  text-input-error:
    borderColor: "#d32f2f"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand’s signature blue (`{colors.primary}`) with white text. On hover, it shifts to a darker active state (`{colors.primary-active}`). When disabled, it uses a lighter blue (`{colors.primary-disabled}`) to indicate inactivity. The `{rounded.sm}` corners keep the button feeling modern and approachable without being overly soft.

**`button-secondary`** — A ghost-style button with a white background and blue text, used for secondary actions like "Learn More" or "View Details." On hover, the background shifts to `{colors.surface-soft}` and text to `{colors.primary-active}`. Maintains the same `{rounded.sm}` and 48px height as the primary button for visual consistency.

### Cards
**`product-card`** — A clean, white card (`{colors.canvas}`) with `{rounded.md}` corners, used to display individual products. The card contains a product image (with its own `{rounded.md}` treatment), a title, and a price. The layout is minimal, relying on the product photography to do the heavy lifting. No shadows or borders — the card sits flush against the background, separated only by whitespace.

**`product-card-price`** — The price text within a product card, set in `{typography.body-md}` and `{colors.ink}`. No dollar sign prefix or suffix — just the numeric value, keeping the look clean and clinical.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, white background (`{colors.canvas}`), with navigation links in `{typography.nav-link}`. The bar is minimal — no background color, no border — relying on the content below to define the page structure. Links are spaced generously, and the logo sits left-aligned.

### Forms
**`text-input`** — A standard input field with a white background, `{rounded.sm}` corners, and 48px height. On focus, it gains a 2px blue ring (`{colors.primary-disabled}`) and a `{colors.primary}` border. Error states use a red border (`#d32f2f`). The placeholder text is `{colors.muted}`.

### Badges
**`badge`** — Small, pill-shaped badges (`{rounded.full}`) used for labels like "New," "Best Seller," or ingredient callouts. They use `{colors.primary}` as the background with white text, set in `{typography.caption}` (uppercase, small). Padding is tight (4px 8px) to keep them compact.

### Search
**`search-bar`** — A full-rounded (`{rounded.full}`) search input, 48px tall, with a white background. Used on the homepage or product listing pages. The placeholder text is `{colors.muted}`. On focus, it follows the same ring pattern as `text-input`.

### Footer
**`footer`** — A dark footer section with `{colors.ink}` background and white text. Links within the footer use `{colors.muted-soft}` for a lower contrast that doesn’t compete with the main content. The footer is padded with `{spacing.section}` top and bottom, creating a clear visual break from the page content.

### Hero
**`hero-section`** — A full-width hero area with a `{colors.surface-soft}` background, used for major campaigns or product launches. The headline uses `{typography.display-xl}` in `{colors.ink}`, with generous padding (`{spacing.section}` top and bottom) to create breathing room. No background image or overlay — the hero relies on typography and whitespace to make an impact.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to `{spacing.xl}`; search bar becomes full-width; buttons expand to full width |
| Tablet | 744–1128px | Two-column product grid; nav-bar remains visible but links may condense; hero section uses `{spacing.section}` padding; search bar is centered |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; hero section uses `{spacing.section}` padding; search bar is centered with max-width |
| Wide | > 1440px | Max-width container (1440px) centered; product grid may expand to four columns; hero section remains centered with max-width |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Nav-bar links have a minimum 44px tap area, even if the text is smaller.
- Search bar and text inputs are 48px tall, exceeding the 44px minimum.

### Collapsing Strategy
- On mobile (< 744px), the primary navigation collapses into a hamburger menu. The search bar moves to a dedicated search icon that expands on tap.
- Product cards stack in a single column on mobile, with images scaling to full width.
- The hero section reduces its vertical padding from `{spacing.section}` to `{spacing.xl}` to save space.
- Footer links collapse into a single column, stacked vertically.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is limited to three hex values (#dedede, #007aff, #121212). The brand’s true primary may be #007aff, but this is a generic blue commonly used in web frameworks. The site may have additional brand-specific colors (e.g., a green for natural ingredients, a warm accent) that were not captured due to framework filtering or dynamic loading.
- Only one font-family declaration was found (swiper-icons), which is likely a UI icon font. The brand’s actual body and display typeface could not be reliably extracted. The typography block above uses a system font stack as a fallback.
- No hover, focus, or error states could be extracted for components beyond the primary button. The `text-input-error` color (#d32f2f) is a standard red and may not be the brand’s actual error color.
- The brand’s dark mode or high-contrast mode styling is unknown.
- Sub-brand or seasonal color palettes (e.g., for limited-edition products) are not captured.
- The site uses Shopify, so checkout-specific colors (e.g., Shopify Pay button) may have been filtered out. The brand’s actual checkout styling may differ.
- No data on loading states, skeleton screens, or empty states.
- The `hero-section` and `footer` components are inferred from common DTC patterns and may not match the exact implementation on the live site.
