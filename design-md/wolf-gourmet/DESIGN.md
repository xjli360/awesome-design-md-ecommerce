---
version: alpha
name: "Wolf Gourmet"
source_url: "https://www.subzero-wolf.com/wolf-gourmet"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Dusted violet steel — that's the first impression. Where most premium appliance brands lean on industrial chrome or cautious navy, Wolf Gourmet's digital presence anchors itself on an unexpected dusty purple (#5b5378) that reads like oxidized metal under warm light. The palette descends through deeper indigos (#494260, #2d293c) as if the user were moving from a sunlit counter into the shadow behind a commercial range hood. Museo Sans carries everything at ExtraLight to Medium weights — never bold enough to compete with product photography, always crisp enough to survive against those dark-purple grounds. The typographic restraint is surgical: headlines breathe at 200-weight thinness while CTAs firm up to 500, creating a clear hierarchy without ever shouting. Red (#af272e) appears sparingly as the unmistakable Wolf signature — a controlled burst on "Shop Now" badges and warning states that references the iconic red knob on every Wolf range. A secondary warm gold (#da9735) and dark teal (#00393b) provide seasonal or editorial flexibility without diluting the purple core. Corner radii stay tight — `{rounded.xs}` to `{rounded.sm}` at most — reflecting the machine-precision edges of die-cast housings and stainless steel bezels. Cards and product tiles sit on a near-white canvas (#f7f7f7) with generous `{spacing.section}` between content blocks, letting each appliance own its viewport the way a single blender owns a marble countertop. The overall rhythm is slow and confident: large product hero images, minimal animation, and typography that defers to the object.

colors:
  primary: "#5b5378"
  primary-active: "#494260"
  primary-disabled: "#524b6c"
  primary-deep: "#2d293c"
  accent-red: "#af272e"
  accent-red-dark: "#9c2815"
  accent-rust: "#a9402c"
  accent-teal: "#00393b"
  accent-gold: "#da9735"
  accent-green: "#c4d600"
  ink: "#38393a"
  body: "#4c4d4f"
  muted: "#808184"
  muted-soft: "#777777"
  hairline: "#d2d2d2"
  hairline-soft: "#e6e6e6"
  canvas: "#f7f7f7"
  surface-soft: "#ececec"
  surface-card: "#ffffff"
  surface-strong: "#ebebeb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#3d3e3f"

typography:
  display-xl:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 48px
    fontWeight: 200
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-mono:
    fontFamily: "'courier new', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.75px
    textTransform: uppercase
  nav-link:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  spec-label:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
  section: 80px
  section-lg: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.6
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 1.5px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    border: 1.5px solid {colors.primary}
  button-accent:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-red-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.primary}
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.accent-red}
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    height: 64px
    boxShadow: 0 1px 4px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.primary}
    hoverShadow: 0 4px 16px rgba(91,83,120,0.10)
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    aspectRatio: 1 / 1
    objectFit: contain
    padding: "{spacing.lg}"
  hero-banner:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    contentMaxWidth: 1200px
  hero-banner-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    aspectRatio: 4 / 3
    hoverBackgroundColor: "{colors.surface-strong}"
  spec-table-row:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.base}"
    borderBottom: 1px solid {colors.hairline-soft}
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-wolf:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 48px
    padding: 0 16px
    border: 1px solid {colors.hairline}
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.on-dark}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    marginBottom: "{spacing.md}"
  comparison-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline-soft}
    cellPadding: "{spacing.base} {spacing.lg}"
  price-display:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"

---

## Components

### Buttons

**`button-primary`** — The default CTA uses the dusty purple primary on a tight `{rounded.sm}` radius, uppercase Museo Sans at weight 500 with generous letter-spacing. Hover deepens to `{colors.primary-active}`; disabled state retains shape but drops opacity to 0.6 and shifts to the muted purple. Padding is wide (28px horizontal) to give the lightweight text room to breathe.

**`button-secondary`** — An outlined variant with a 1.5px purple border and transparent fill. On hover, the fill floods to `{colors.primary}` and text inverts to white, creating a smooth ink-fill transition. Used for secondary actions like "View Details" or "Compare" where the primary CTA already occupies the viewport.

**`button-accent`** — Reserved for high-urgency actions like "Shop Now" or "Add to Cart," this uses Wolf's signature red (#af272e). It appears sparingly — never more than once per viewport — to maintain the red-knob association without overwhelming the purple-led palette.

### Navigation

**`nav-bar`** — A clean white 72px bar with a thin bottom hairline. The Wolf Gourmet wordmark sits left; navigation links use `{typography.nav-link}` at medium weight. On scroll, the bar compresses to 64px and picks up a subtle drop shadow. Product category links are arranged horizontally with 24px gaps.

**`breadcrumb`** — Muted gray text at caption size, separated by forward-slash characters in `{colors.hairline}`. The current page renders in `{colors.ink}` without a link. Positioned below the nav-bar with `{spacing.base}` vertical clearance.

### Product Display

**`product-card`** — A white card with 1px hairline border that strengthens to purple on hover. The product image sits in a contained square area with generous internal padding and a light gray background, ensuring stainless steel appliances read cleanly. Below: product name in `{typography.title-sm}`, a one-line descriptor in `{typography.body-sm}`, and price in `{typography.price}`. Cards have minimal shadow at rest — the hover state introduces a soft purple-tinted shadow.

**`product-card-image`** — The image container uses `object-fit: contain` with 24px internal padding so no appliance is cropped. Background stays at `{colors.canvas}` to create a studio-shot feel regardless of source photography quality.

**`comparison-table`** — A structured grid for side-by-side appliance specs. Column headers use `{typography.title-sm}`, row labels use `{typography.spec-label}` (uppercase, tracked-out), and cell values use `{typography.body-sm}`. Alternating rows have no color shift — separation comes from the hairline borders alone.

**`spec-table-row`** — Individual specification rows with uppercase tracked labels on the left in muted gray and values on the right in body color. Thin bottom borders provide structure without visual weight.

### Hero & Marketing

**`hero-banner`** — Full-width block in deep purple (#2d293c) with white display text at 48px / weight 200. The extreme thinness of the type creates tension against the dark ground. Content maxes at 1200px and centers. Minimum height of 560px ensures the block commands the viewport even before a product image loads.

**`hero-banner-light`** — An alternate light-canvas hero for secondary pages. Same typographic treatment but in ink on off-white, with slightly reduced min-height (480px). Used for category landing pages where a darker tone would compete with product imagery below.

**`category-tile`** — Rectangular cards (4:3 aspect ratio) in `{colors.surface-soft}` with centered product imagery and a title-sm label. Hover shifts the background one notch darker to `{colors.surface-strong}`. Tiles are used in grid layouts for browsing appliance categories (blenders, toasters, cookware).

### Badges

**`badge-new`** — A compact pill in chartreuse green (#c4d600) with dark text, calling out newly launched products. The green is bright enough to catch attention without clashing with the purple-red palette.

**`badge-wolf`** — A red badge carrying the Wolf insignia or "Wolf Gourmet" label. Used on product cards to reinforce brand lineage.

### Search

**`search-bar`** — A 48px-tall input field with hairline border and left-aligned magnifying glass icon in muted gray. On focus, the border transitions to purple. Rounded corners are minimal (`{rounded.sm}`) to match the overall rectilinear language. Placeholder text uses `{typography.body-md}` at 300 weight in `{colors.muted}`.

### Footer

**`footer`** — Deep purple ground (#2d293c) matching the hero palette, creating bookend framing for the page. Section headings use the spec-label style (11px, uppercase, tracked). Links render in soft gray and brighten to white on hover. Four-column layout on desktop collapses to accordion on mobile.

### Price & Commerce

**`price-display`** — Clean 20px Museo Sans at weight 300 — no dollar-sign enlargement or strike-through patterns. The deliberate lightness of the price typography avoids a discount-retail feel, consistent with the premium positioning.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text drops to `{typography.display-md}`; nav collapses to hamburger; footer stacks to single column accordion; product cards go full-width with 16px horizontal margin |
| Tablet | 744–1128px | Two-column product grid; hero maintains full height but text centers; nav stays expanded but drops secondary links to overflow menu; comparison table scrolls horizontally |
| Desktop | 1128–1440px | Three-column product grid; full nav with all categories visible; hero uses full `{typography.display-xl}`; footer renders four columns; spec tables display inline |
| Wide | > 1440px | Content maxes at 1440px and centers; additional horizontal padding on hero; product grid can extend to four columns for category pages; generous whitespace flanking content |

### Touch Targets

- All interactive elements maintain a minimum 44px touch target on mobile, even when visually smaller
- Product card tap area covers the entire card surface, not just the title or image
- Nav hamburger icon has 48px tap zone with 12px visual padding
- Footer accordion headers have full-width tap areas at 56px height
- Spacing between adjacent tap targets is at least 8px to prevent mis-taps

### Collapsing Strategy

- Desktop multi-column grids collapse to 2-col at tablet, 1-col at mobile — never intermediate breakpoints
- Horizontal navigation becomes a slide-out drawer (left-anchored, dark purple overlay)
- Comparison tables switch from fixed columns to a horizontally scrollable container with sticky first column
- Hero banner images shift from right-aligned product shot to a stacked layout (image above, text below) at mobile
- Spec tables on product detail pages collapse from two-column key-value pairs to full-width stacked rows
- Footer columns collapse into expandable accordion sections with `{spacing.md}` between headers

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Museo Sans weight mapping (whether the site uses 200/300/500 or named ExtraLight/Light/Medium CSS values) could not be confirmed from extraction alone
- No CSS custom properties or design-token variable names were captured — the purple hierarchy is inferred from frequency, not declared intent
- Interaction animations (easing curves, transition durations) are not available from static extraction
- The relationship between Sub-Zero, Wolf, and Wolf Gourmet sub-brands on the shared domain means some extracted colors (#0081c6, #603cba, #116699) may belong to sibling brands rather than Wolf Gourmet specifically
- Icon system (line weight, size grid, fill vs stroke) could not be determined
- Dark-mode or reduced-motion preferences are not evidenced in the extraction
- Whether the chartreuse green (#c4d600) is a persistent brand accent or a seasonal/promotional color is unclear from a single extraction pass
