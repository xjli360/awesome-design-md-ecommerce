---
version: alpha
name: "ShopBot Tools"
source_url: "https://www.shopbottools.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Hot pink at #f00069 cuts across midnight navy #0a112d wherever ShopBot commits to a call-to-action — an unconventional pairing for an American CNC manufacturer whose page title leads with "Made in USA." The navy anchors top navigation and hero backgrounds at full bleed; the pink fires only at Buy, Quote, and Request Info moments, making it function less as decoration and more as a machined warning stripe on industrial equipment. Albert Sans handles the display hierarchy with geometric precision across weights 400–700, while Museo Sans carries specification and body copy at a warmer curvature — a two-font system that lets a product page separate headline impact from dense technical prose without relying on size contrast alone. The neutral palette runs unusually deep: six gray steps (#646970, #3c434a, #aaaaaa, #767676, #dcdcde, #d3d3d3) spread across interface chrome, table rows, and disabled states because a machine configurator must make status, availability, and content level read as distinct signals without introducing color noise into a technically loaded page. Secondary interactive states defer to #003388 deep navy for active links and #008de4 for inline anchors; #ff9900 amber flags promotional SKUs or limited-availability callouts — a color decision that reads more like warehouse signage than lifestyle marketing. Success greens (#16a249) and alert reds (#d63638) handle order and stock states. Corner radii stay close to zero, 4–8px on buttons and cards, echoing the rectangular geometry of milled aluminum and routed sheet goods. The product configurator — spanning Buddy, Desktop, PRSalpha, and PRSstandard model lines — is the commercial core of the site, each machine carrying a spec-table breakdown, embedded demonstration video, and a "Get a Quote" primary CTA that opens a lead-capture form layered against navy-mid. Navigation collapses to a compact dark-navy drawer on mobile with {colors.primary} surviving as the sole chromatic element once the full desktop chrome collapses.

colors:
  primary: "#f00069"
  primary-active: "#b5004f"
  primary-disabled: "#f9a0c4"
  ink: "#1b1b1b"
  body: "#3c434a"
  muted: "#767676"
  muted-soft: "#aaaaaa"
  hairline: "#dcdcde"
  hairline-soft: "#eeeeee"
  canvas: "#fffffe"
  surface-soft: "#f6f7f7"
  surface-card: "#fbfcfe"
  on-primary: "#fffffe"
  navy-dark: "#0a112d"
  navy-mid: "#171b60"
  navy-deep: "#232153"
  accent-blue: "#008de4"
  accent-deep-blue: "#003388"
  accent-orange: "#ff9900"
  success: "#16a249"
  error: "#d63638"

typography:
  display-xl:
    fontFamily: "'Albert Sans', 'Museo Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Albert Sans', 'Museo Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Albert Sans', 'Museo Sans', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Albert Sans', 'Museo Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Albert Sans', 'Museo Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Museo Sans', 'Albert Sans', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Museo Sans', 'Albert Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.7px
    textTransform: uppercase
  caption:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: 11px
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    states:
      hover: { backgroundColor: "{colors.primary-active}" }
      disabled: { backgroundColor: "{colors.primary-disabled}", textColor: "{colors.on-primary}" }

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.navy-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.navy-dark}"
    padding: 12px 26px
    height: 48px
    states:
      hover: { backgroundColor: "{colors.surface-soft}" }

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 48px
    states:
      hover: { backgroundColor: "{colors.surface-soft}" }

  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 36px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocused: "2px solid {colors.accent-blue}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"

  nav-bar:
    backgroundColor: "{colors.navy-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
    logoColor: "{colors.canvas}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-sm}"
    ctaRounded: "{rounded.xs}"
    borderBottom: none
    mobileDrawerBackground: "{colors.navy-dark}"

  sub-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    height: 40px
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"

  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    shadow: "0 2px 10px rgba(10,17,45,0.08)"
    imageBg: "{colors.surface-soft}"
    padding: "{spacing.lg}"
    ctaTypography: "{typography.button-sm}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"

  hero-banner:
    backgroundColor: "{colors.navy-dark}"
    textColor: "{colors.canvas}"
    overlayColor: "rgba(10,17,45,0.70)"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    secondaryCtaColor: "{colors.canvas}"
    secondaryCtaBorder: "2px solid {colors.canvas}"
    secondaryCtaTypography: "{typography.button-md}"
    secondaryCtaRounded: "{rounded.xs}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"

  spec-table:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    rowBorder: "1px solid {colors.hairline}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.lg}"
    headerBackgroundColor: "{colors.navy-dark}"
    headerTextColor: "{colors.canvas}"
    headerTypography: "{typography.title-sm}"

  promo-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

  status-badge-available:
    backgroundColor: "{colors.success}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  status-badge-unavailable:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.navy-mid}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 14px"
    activeBackgroundColor: "{colors.navy-dark}"
    activeTextColor: "{colors.canvas}"
    activeBorder: "1px solid {colors.navy-dark}"

  lead-capture-form:
    backgroundColor: "{colors.navy-mid}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    inputBackgroundColor: "{colors.canvas}"
    inputTextColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    inputRounded: "{rounded.xs}"
    inputBorder: "1px solid {colors.hairline-soft}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    padding: "{spacing.xxl} {spacing.xl}"
    rounded: "{rounded.sm}"

  alert-banner:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    iconColor: "{colors.ink}"

  video-embed:
    backgroundColor: "{colors.navy-dark}"
    rounded: "{rounded.sm}"
    overlayColor: "rgba(10,17,45,0.45)"
    playIconColor: "{colors.primary}"
    playIconSize: 64px
    aspectRatio: "16/9"

  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline-soft}"
    typography: "{typography.caption}"
    linkColor: "{colors.accent-deep-blue}"

  footer:
    backgroundColor: "#1e1e1e"
    textColor: "{colors.muted-soft}"
    linkColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"
    copyrightTypography: "{typography.caption}"
    copyrightColor: "{colors.muted}"

## Components

### Buttons

**`button-primary`** — The hot-pink (#f00069) primary action is set in uppercase Albert Sans at 15px/700 with 0.4px tracking, 48px tall, and 4px radius. It appears at CNC machine configurator CTAs ("Get a Quote", "Buy Now") and never as a secondary trigger. Hover deepens to #b5004f; disabled washes to #f9a0c4 while retaining white text so the affordance shape is preserved.

**`button-secondary`** — White fill with a 2px #0a112d navy border and matching navy uppercase label. Used for "Learn More" and "View Specs" alongside a primary; hover introduces a #f6f7f7 tint to signal the boundary without competing with the primary.

**`button-ghost`** — Transparent fill with a 2px #f00069 border and pink text label. Used for secondary CTAs on dark-background sections where the white/navy pair reads poorly; conveys the primary brand volt without the filled weight.

**`button-sm`** — Pink-filled, 36px tall, same uppercase tracking as button-md, 4px radius. Used inside product cards and inline filter controls where 48px would crowd the layout.

### Text Input

**`text-input`** — White fill, 44px tall, 4px radius, 1px #dcdcde border at rest, 2px #008de4 on focus. Placeholder in #767676. Appears in quote forms, lead-capture, and the site search field. Validation errors swap the border to #d63638 with an inline error caption in the same red.

### Navigation

**`nav-bar`** — Full-bleed #0a112d navy at 64px. The ShopBot wordmark renders in white; product line categories (Tools, Accessories, Software, Support) sit in 15px/600 Albert Sans with a white text color and a pink hover underline. A "Get a Quote" pill in #f00069 right-aligned is the only chromatic break. On mobile, all items collapse to a hamburger icon; the drawer slides in from the left on the same dark navy background.

**`sub-nav`** — 40px white strip below the main nav at desktop, carrying secondary breadcrumbs, currency selector, and account links in 13px/400 caption style with a 1px #dcdcde bottom border. Collapses entirely on mobile.

### Product Card

**`product-card`** — White card with 1px #dcdcde border, 8px radius, and a soft directional shadow (0 2px 10px rgba 8%). The machine image sits on a #f6f7f7 field. Below: machine name in 20px/600 Albert Sans, a 2–3 line spec preview in 14px Museo Sans, a promo or availability badge, and a full-width pink "Get a Quote" button at the bottom. Cards grid at 3-up on desktop, 2-up on tablet, single column on mobile.

### Hero Banner

**`hero-banner`** — Full-bleed with a dark-navy (#0a112d) base and a 70% navy overlay over photographic or video content. Display headline at 52px/700, sub-headline at 26px/600, both in white Albert Sans. Two CTAs sit inline: a filled pink primary and a white-bordered ghost secondary. Minimum height 560px on desktop.

### Spec Table

**`spec-table`** — Two-column grid on a #f6f7f7 surface. Row labels render in 11px/700 uppercase Albert Sans in #767676 (a classified/dim gray); values render in 14px Museo Sans in #1b1b1b. A 1px #dcdcde horizontal rule separates rows. Table header (machine model name) sits in a dark navy block with white 16px/600 Albert Sans. This is the primary data structure for communicating cut area, spindle power, and rapid speed to evaluating buyers.

### Lead Capture Form

**`lead-capture-form`** — Navy-mid (#171b60) panel with white heading text at 26px/600 and white body copy. Inputs render on white fills with navy labels. The submit CTA mirrors button-primary. Used on product pages and the contact page; on mobile it stacks to full-width columns.

### Video Embed

**`video-embed`** — 16:9 aspect ratio block with dark navy background, 8px radius. A centered 64px #f00069 play icon overlays a 45% navy scrim until activated. Used on every machine product page to show the router in motion at a fabrication facility.

### Badges

**`promo-badge`** — #ff9900 amber fill, ink text, uppercase 11px/700, 4px radius. Tags limited-time pricing or featured machine bundles.

**`status-badge-available`** — #16a249 green fill with white uppercase 11px/700 text. Signals in-stock or available-to-ship status.

**`category-chip`** — Pill-shaped filter chips (9999px radius) in #f6f7f7 with navy-mid text. Active state inverts to solid #0a112d with white text. Used in the accessories and software catalog filter bar.

### Footer

**`footer`** — Dark charcoal (#1e1e1e) with a 3px #f00069 top border — the pink's only passive appearance on the page. Column headings in 16px/600 white Albert Sans; links and body in 14px #aaaaaa Museo Sans. Copyright line in 13px #767676.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hamburger nav replaces the full bar; sub-nav hidden; product cards stack to 1-up; hero headline drops to 32px/700; spec table scrolls horizontally; lead-capture form stacks label+input vertically |
| Tablet | 744–1128px | 2-up product card grid; nav retains wordmark + truncated links + Quote CTA; hero at 40px headline; sub-nav collapses to icon strip |
| Desktop | 1128–1440px | 3-up product grid; full sub-nav bar visible; hero at 52px full width; spec tables side by side with video embed |
| Wide | > 1440px | Max-width container at 1320px centered; hero photographic field extends edge-to-edge behind the constrained content; 4-up product grid on catalog pages |

### Touch Targets

- All primary CTAs minimum 48px tall, full-width on mobile
- Nav hamburger target 44×44px
- Category chips padded to 40px height on mobile via increased vertical padding
- Spec table rows minimum 44px tall for accessible tap on mobile scroll

### Collapsing Strategy

- Sub-nav disappears entirely below 744px; its links fold into the mobile drawer
- Spec tables scroll horizontally at viewport < 480px rather than reflowing to stacked pairs
- Hero dual-CTA row stacks vertically on mobile with primary first
- Footer columns collapse from 4-up to 2-up at tablet, single column at mobile
- Video embed maintains 16:9 ratio at all breakpoints; minimum width 320px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed border-radius values from live extraction; 4–8px values are inferred from industrial brand convention and the anti-lifestyle aesthetic of the extracted palette
- Albert Sans and Museo Sans confirmed as font-family stacks from extraction, but specific weight mappings per component (e.g., whether display uses 800 vs 700) could not be verified without direct CSS inspection
- Exact nav height (64px) and hero min-height (560px) are estimates; live extraction did not surface layout metrics
- Dark mode or alternate theme presence unknown — the palette contains both very dark (#0a112d, #1e1e1e) and near-white (#fbfcfe) surfaces, suggesting a possible dark/light mode toggle that was not confirmed
- Animation and transition values (hover easing, drawer slide duration) not extractable from static hints
- #ff9900 orange confirmed present but its exact usage context (promo badge vs. third-party partner logo) could not be verified with certainty from extraction alone
- Icon system (line vs. filled, weight, size) not determinable from extracted hints
