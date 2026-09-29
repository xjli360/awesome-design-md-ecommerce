---
version: alpha
name: "Roman"
source_url: "https://ro.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A direct-to-consumer men's health brand that uses a crisp, clinical white canvas and a single accent of deep teal (#1990c6) to signal medical credibility without feeling sterile. The site runs Source Sans Pro at modest weights — body text sits at 400 weight with generous line-height, while buttons and headings use 600 weight for clear hierarchy. The brand avoids the heavy, masculine typography common in men's health; instead, it opts for a clean, approachable look with soft corners (`{rounded.md}` on cards, `{rounded.sm}` on buttons) that feel more like a modern clinic than a locker room. Navigation is minimal — a sticky top bar with the Roman logo, a few key links, and a prominent CTA button in the brand teal. Product cards use a two-column grid with clear pricing, a brief description, and a single action, avoiding information overload. The overall impression is one of straightforward, no-nonsense healthcare delivery — the design gets out of the way so the medical information and treatment options can lead.

colors:
  primary: "#1990c6"
  primary-active: "#1473a0"
  primary-disabled: "#b3d9e8"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  success: "#28a745"
  error: "#dc3545"
  warning: "#ffc107"

typography:
  display-xl:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  link:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px

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
    padding: 11px 23px
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
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-cta:
    typography: "{typography.button-sm}"
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Get Started", "Order Now", and "Book Appointment". Uses the brand teal (`{colors.primary}`) with white text and a soft 8px radius. On hover, it darkens to `{colors.primary-active}`. When disabled, it fades to a pale blue (`{colors.primary-disabled}`) with white text, signaling the action is unavailable.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". It has a white background with a 2px teal border and teal text. On hover, the background shifts to `{colors.surface-soft}` and the border darkens. This button maintains the same height and padding as the primary button for consistent alignment in forms.

**`button-tertiary-text`** — A text-only button used for inline actions like "Cancel" or "Skip". It has no background or border, only teal text. On hover, it may add a subtle underline or opacity change. This is the least prominent button style, used to de-emphasize secondary actions.

### Cards
**`product-card`** — The core content container for treatment options and services. It has a white background, a 1px hairline border, and 12px rounded corners. Inside, it uses `{typography.body-md}` for descriptions and `{typography.title-md}` for pricing. On hover, the border turns teal and a subtle box shadow appears, indicating the card is interactive. The card includes a text-based CTA link in teal, not a full button, to keep the focus on the product information.

### Navigation
**`nav-bar`** — A fixed top navigation bar that spans the full width. It is 64px tall with a white background and a 1px bottom border. The logo sits on the left, followed by navigation links in `{typography.nav-link}`. The active link is highlighted in teal. On the right, a "Get Started" button in `{typography.button-sm}` serves as the primary CTA. On mobile, the navigation collapses into a hamburger menu.

### Forms
**`text-input`** — Standard text input fields used throughout the site for name, email, and health questionnaire forms. They have a white background, 1px hairline border, and 8px rounded corners. On focus, the border thickens to 2px and turns teal. Error states show a red border (`{colors.error}`). The input height is 48px to match button heights for consistent form layouts.

### Hero
**`hero-section`** — The top-of-page hero area, typically with a light gray background (`{colors.surface-soft}`) and generous padding. It contains a large heading (`{typography.display-xl}`) and a supporting subheading in muted gray. This section is used on landing pages and treatment detail pages to introduce the value proposition.

### Badges
**`badge`** — Small, pill-shaped labels used for status indicators (e.g., "FDA Approved", "New", "Most Popular"). They use `{colors.primary}` as the background with white text, set in `{typography.caption}`. A `badge-success` variant uses green for positive statuses like "In Stock" or "Available".

### Footer
**`footer`** — The site footer with a light gray background and muted text. It contains links to legal pages (Privacy, Terms), social media icons, and a copyright notice. The footer uses `{typography.body-sm}` and has section-level padding (`{spacing.section}`) top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to `{typography.display-md}`; buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains two-column layout with reduced padding |
| Desktop | 1128–1440px | Full layout with max-width container; three-column product grid on some pages; nav links fully expanded |
| Wide | > 1440px | Content constrained to 1440px max-width; extra whitespace on sides; no layout changes |

### Touch Targets
- All buttons and interactive elements are minimum 48px tall for touch accessibility.
- Text inputs are 48px tall to match button height.
- Nav links have a minimum tap target of 44x44px.
- Product card CTAs are at least 44px tall.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- Product grids collapse from three columns to two on tablet, and to single column on mobile.
- Hero sections stack vertically on mobile, with the image or illustration moving below the text.
- Footer links collapse into a single column on mobile, with accordion-style sections for multiple link groups.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors were limited due to the site's captcha verification page blocking full CSS extraction. The primary teal (#1990c6) was inferred from the brand's known identity and limited available data, not from a comprehensive site scan.
- No hover, focus, or active states could be reliably extracted for any component beyond the primary button.
- Font weights and sizes are based on common patterns for Source Sans Pro in healthcare DTC, not extracted from the live site.
- Spacing values are estimated based on standard web design patterns for this category.
- No dark mode or high-contrast mode data is available.
- Error message styling, form validation states, and tooltip designs are not documented.
- The brand may use additional accent colors for specific treatment categories or marketing campaigns that were not captured.
- No animation or transition timing data is available.
