---
version: alpha
name: "Midori"
source_url: "https://www.midori-japan.co.jp"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The brand name is the Japanese word for green, and the design system takes that etymology literally: #036248 — a dense, resinous forest-floor green — claims every primary button fill, every nav-link hover state, and every active indicator, leaving no interpretive gap between the word and the color. BrandonGrotesque and BrandonText handle Latin headings in geometric sans forms at controlled weights (600 for display headers, 400–500 for body), while Hiragino Kaku Gothic ProN, Noto Sans Japanese, Yu Gothic, and YuGothic carry Japanese copy — not as fallbacks but as co-equal first-class stacks loaded via YakuHanJP and YakuHanMP for proper Japanese punctuation spacing. Both writing systems share identical size and weight scales; there is no Japanese-mode override, only one unified scale that works in either script.

  The canvas is #fafafa rather than full white, which softens contrast against the dark #036248 primary and prevents harshness when dense kanji runs at caption size. Surface hierarchy moves through a stepped gray band — #f2f2f2 for background panels, #e5e5e5 for dividers, #dadada for stronger rule lines — with no colored surfaces except green treatments. A red (#ee0a15, darkened to #bc1d21 on hover) operates strictly as a high-urgency signal: sale pricing, stock warnings, and required-field errors. A mid-range sage (#4f917f) appears in secondary badges and hover fills, keeping the palette within a coherent green family that reinforces the brand name without adding unrelated hues.

  Corner radii run deliberately small. Cards and inputs sit at 4px (`{rounded.xs}`), buttons at 8px (`{rounded.sm}`), and modals at 12px (`{rounded.md}`) — a precision-over-friendliness stance that reads as Japanese stationery logic: neat, edited, purposeful. Vertical rhythm is generous (48px section padding at minimum), horizontal grid density is high — product thumbnails share screen space efficiently. Type weights avoid heavy extremes; 700 appears only in hero display, reinforcing the sense that the photography and the green carry the brand voltage, not typographic muscle.

colors:
  primary: "#036248"
  primary-active: "#004a59"
  primary-disabled: "#4f917f"
  accent-red: "#ee0a15"
  accent-red-dark: "#bc1d21"
  accent-green-mid: "#4f917f"
  ink: "#111111"
  body: "#313131"
  muted: "#32373c"
  hairline: "#dadada"
  hairline-soft: "#e5e5e5"
  canvas: "#fafafa"
  canvas-white: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#fcfcfc"
  surface-mid: "#e0e0e0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'BrandonGrotesque', 'BrandonText', 'Noto Sans Japanese', 'Hiragino Kaku Gothic ProN', 'YuGothic', 'Yu Gothic', Verdana, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'BrandonGrotesque', 'BrandonText', 'Noto Sans Japanese', 'Hiragino Kaku Gothic ProN', 'YuGothic', Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'BrandonGrotesque', 'BrandonText', 'Noto Sans Japanese', 'YuGothic', Verdana, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'BrandonGrotesque', 'BrandonText', 'Noto Sans Japanese', 'YuGothic', Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'BrandonGrotesque', 'BrandonText', 'Noto Sans Japanese', 'YuGothic', Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'BrandonText', 'BrandonGrotesque', 'Noto Sans Japanese', 'Hiragino Kaku Gothic ProN', 'Meiryo', 'YuGothic', Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  body-sm:
    fontFamily: "'BrandonText', 'BrandonGrotesque', 'Noto Sans Japanese', 'YuGothic', Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  caption:
    fontFamily: "'BrandonText', 'BrandonGrotesque', 'Noto Sans Japanese', 'YuGothic', Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'BrandonGrotesque', 'BrandonText', 'Noto Sans Japanese', 'YuGothic', Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'BrandonGrotesque', 'BrandonText', 'Noto Sans Japanese', 'YuGothic', Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'BrandonGrotesque', 'BrandonText', 'Noto Sans Japanese', 'YuGothic', Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
  badge-label:
    fontFamily: "'BrandonGrotesque', 'BrandonText', 'Noto Sans Japanese', 'YuGothic', Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  price-display:
    fontFamily: "'BrandonGrotesque', 'BrandonText', 'Noto Sans Japanese', 'YuGothic', Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
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
    height: 44px
    border: none
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
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1.5px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    linkHoverColor: "{colors.primary}"
    activeColor: "{colors.primary}"
    padding: "0 {spacing.xl}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    padding: "{spacing.sm} 0"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.body}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xl}"
    ctaComponent: button-primary
    accentColor: "{colors.primary}"
    minHeight: 480px
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  search-bar:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    height: 40px
    iconColor: "{colors.muted}"
    iconFocusColor: "{colors.primary}"
  product-grid:
    columns: 4
    gap: "{spacing.base}"
    tabletColumns: 3
    mobileColumns: 2
    padding: "0 {spacing.xl}"
  section-heading:
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.muted}"
    accentBar: "3px solid {colors.primary}"
    accentBarWidth: 40px
    marginBottom: "{spacing.xxl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.surface-mid}"
    linkHoverColor: "{colors.canvas-white}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas-white}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "3px solid {colors.primary}"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackgroundColor: "{colors.canvas-white}"
    inactiveTextColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 36px
    width: 36px

## Components

### Buttons

**`button-primary`** — Forest-green (#036248) fill with white type at 14px/600 weight, 8px radius, 44px tall, and 24px horizontal padding. The active state deepens to #004a59; the disabled state uses the mid sage (#4f917f) at 60% opacity rather than a gray — keeping the green family coherent even in non-interactive states. No drop shadow on the resting state; the brand relies on color saturation rather than elevation effects.

**`button-secondary`** — White fill with a 1.5px #036248 border and primary-green text. Signals an alternative action without reducing the green presence on screen. Active state shifts the background to #f2f2f2 and the border to #004a59, providing clear press feedback without heavy treatment.

**`button-ghost`** — Transparent with a 1px #dadada border and #313131 text. Used for low-priority actions such as "view all" links in product grids or filter reset triggers. Minimal visual weight ensures product photography remains the dominant element.

### Inputs

**`text-input`** — White fill, 1px #dadada border, 4px radius. On focus the border thickens to 1.5px and shifts to #036248 — matching primary brand color without an additional glow or box-shadow layer. Placeholder text runs in #32373c at body-md weight 400.

**`search-bar`** — Same border treatment as text-input at 40px height with a leading search icon that shifts from #32373c to #036248 on focus. Positioned in the nav-bar at all breakpoints; collapses to an icon-only trigger on mobile with a slide-down expansion panel.

### Navigation

**`nav-bar`** — White bar, 64px tall, with a 1px #e5e5e5 bottom border. Nav links use 14px/500 BrandonGrotesque in #111111 turning #036248 on hover. The Midori logo sits left; a horizontal category menu extends center-left; search, cart, and account icons sit right. No mega-menu drop shadows — sub-menus float with a 1px hairline border only.

**`breadcrumb`** — Caption-size (12px/0.2px tracking) in #32373c with #dadada separators. Active (current page) segment runs in #111111 at weight 400. Horizontally flush with the page content grid.

### Product Display

**`product-card`** — #fcfcfc background, 4px radius, 1px #e5e5e5 border, 16px inner padding. Image occupies a 4:3 aspect ratio container at top; title follows in 16px/600 BrandonGrotesque in #111111; price in 18px/600 below. On hover the border lifts to #036248 with a soft `0 2px 8px rgba(0,0,0,0.08)` shadow — the green border is the primary hover signal, not a background tint.

**`sale-badge`** / **`new-badge`** — Both use the same 11px/700/uppercase badge-label scale and 4px radius pill. Sale is #ee0a15 fill; New is #036248 fill; both white text. Layered in the top-left corner of product-card images.

**`category-badge`** — #f2f2f2 background with #036248 text and 1px #dadada border at rest; inverts to solid #036248 fill on hover. Used for taxonomy tags on product detail pages and filter chips in listing grids.

### Layout Sections

**`hero-banner`** — #f2f2f2 background (keeps the full-bleed block warm without competing with product photography), minimum 480px tall. Display-xl headline in #111111, body-md subtitle in #313131, primary CTA button left-aligned. A 3px #036248 vertical accent bar optionally flanks the headline on desktop. No parallax or animation; the brand favors static editorial compositions.

**`section-heading`** — Display-md title in #111111 with a 40px × 3px #036248 underline bar below it, then body-md subtitle in #32373c. Consistent across all category landing and editorial pages.

**`product-grid`** — 4-column on desktop, 3-column on tablet, 2-column on mobile. 16px gap. 32px horizontal page padding at desktop; 16px at mobile.

### Footer

**`footer`** — Near-black (#111111) background with a 3px #036248 top border — the green reappears at the page boundary to close the brand frame. Column headings in 14px/600 white; links in 13px/400 #e0e0e0 softening to full white on hover. 64px vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 2-column product grid; search bar expands below nav; nav collapses to hamburger; horizontal padding drops to 16px; hero min-height 320px |
| Tablet | 744–1128px | 3-column product grid; nav shows full logo and category links, search icon only; horizontal padding 24px |
| Desktop | 1128–1440px | 4-column product grid; full nav with search bar visible; hero 480px min-height |
| Wide | > 1440px | Content max-width 1320px centered; hero spans full viewport width with content constrained |

### Touch Targets

- Minimum touch target 44 × 44px on all interactive elements
- Cart, search, and account nav icons expand to 44px tap area via padding even when the icon renders at 20px
- Product card tap area covers the full card surface, not just the title or image
- Pagination dots and number buttons minimum 36px (tappable via 44px wrapper)

### Collapsing Strategy

- Navigation: hamburger drawer at < 744px; category mega-menu becomes full-screen drawer overlay
- Search: icon trigger at ≤ 1128px; full inline search bar at > 1128px
- Product grid: 4 → 3 → 2 columns; card image aspect ratio stays 4:3 at all breakpoints
- Hero: copy stack collapses to single column with reduced padding at mobile; CTA button goes full-width
- Footer columns: 4-column grid at desktop; 2-column at tablet; single column stacked at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` tag detected — the mobile browser chrome color (status bar) is unknown; recommend #036248 as the logical candidate given primary brand usage
- Many extracted hex values (#00d084, #0693e3, #7a00df, #4721fb, #ab1dfe, #faaca8, #dad0ec, #fafae1, #fdd79a, #330968, #34e2e4) are WordPress Gutenberg block editor palette defaults, not brand colors; they were excluded from the token set
- Custom typeface licensing details for BrandonGrotesque and BrandonText could not be confirmed (whether self-hosted or served via a type foundry CDN)
- No design tokens, CSS custom properties, or JS token exports were extractable — spacing scale and rounded scale inferred from visual inspection conventions for Japanese stationery brand sites
- Hover and focus animation duration/easing not extractable from static extraction; standard 150ms ease-in-out assumed
- Dark-mode palette not detected; the site appears to be light-only
- Japanese-specific typographic adjustments (font-feature-settings for proportional kana, line-break rules) not verifiable without runtime inspection
