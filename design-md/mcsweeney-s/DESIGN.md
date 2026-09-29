---
version: alpha
name: "McSweeney's"
source_url: "https://www.mcsweeneys.net"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A literary institution that wears its seriousness lightly, McSweeney's Internet Tendency builds its digital home on a warm, almost sepia-toned foundation of #1a1a17 and #fff3e0 — the deep, ink-black brown of a well-worn book spine and the soft cream of aged paper. The palette is deliberately restrained: #2a2a26 and #3a3a36 for body text, #8a8a84 and #9e9e98 for muted captions and metadata, with #e8e6df and #c8c8c0 forming the hairline borders and surface edges that give the layout its quiet, bookish structure. Against this sober ground, two accents provide the voltage: #5bb8f5, a clear, literary blue used for links and interactive elements, and #2a2000, a deep amber-brown that surfaces in headings and blockquotes, evoking the warm glow of a reading lamp. The typography leans on Garamond Premier Pro and Baskerville for display and body text — serif faces that signal literary credibility without pretension — while Avenir and Helvetica Neue handle UI labels and navigation, creating a deliberate tension between the timeless and the functional. Buttons are softly rectangular with {rounded.sm} corners, never pill-shaped; the search bar is a simple outlined field, not a glowing orb. The site trusts its content — long-form humor, essays, and fiction — over chrome, using generous {spacing.section} margins and a single-column reading rhythm that lets the words breathe. The blue link color #5bb8f5 is the only bright element in an otherwise muted world, making every click feel like a deliberate choice.

colors:
  primary: "#5bb8f5"
  primary-active: "#89d0ff"
  primary-disabled: "#a0a09a"
  ink: "#1a1a17"
  body: "#2a2a26"
  muted: "#757575"
  muted-soft: "#9e9e98"
  hairline: "#c8c8c0"
  hairline-soft: "#e8e6df"
  canvas: "#fff3e0"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#1a1a17"
  accent-amber: "#2a2000"
  accent-deep-amber: "#3a2800"
  accent-warm: "#5a3800"
  link-hover: "#00b0ff"
  highlight-bg: "#fff9c4"
  dark-canvas: "#212121"
  dark-surface: "#2e2e2a"
  dark-body: "#eeeeee"

typography:
  display-xl:
    fontFamily: "'garamond-premier-pro', Baskerville, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'garamond-premier-pro', Baskerville, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'garamond-premier-pro', Baskerville, serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.15px
  body-md:
    fontFamily: "'garamond-premier-pro', Baskerville, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'garamond-premier-pro', Baskerville, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "'garamond-premier-pro', Baskerville, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  nav-link:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  blockquote:
    fontFamily: "'garamond-premier-pro', Baskerville, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
    fontStyle: italic

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 10px 20px
    height: 40px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 42px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}33"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  article-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  article-card-hover:
    backgroundColor: "{colors.surface-soft}"
  article-card-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  article-card-meta:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  article-card-excerpt:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  footer-link-hover:
    textColor: "{colors.primary-active}"
  blockquote-component:
    textColor: "{colors.accent-amber}"
    typography: "{typography.blockquote}"
    borderLeft: "3px solid {colors.accent-amber}"
    padding: "{spacing.md} {spacing.lg}"
    backgroundColor: "{colors.surface-soft}"
  section-heading:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.accent-amber}"
    paddingBottom: "{spacing.sm}"
  horizontal-rule:
    borderTop: "1px solid {colors.hairline}"
    margin: "{spacing.xl} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in McSweeney's distinctive blue (#5bb8f5) against the warm cream canvas. Uses Avenir Next at 14px weight 600 with tight letter-spacing for a clean, editorial feel. Corners are softly squared at {rounded.sm} (4px), never pill-shaped. On hover, the background shifts to the lighter #89d0ff; disabled state drops to the muted #a0a09a with cream text. Secondary buttons invert the scheme — cream background, ink text, a thin hairline border — and hover to reveal a soft surface tint. Ghost buttons exist for inline actions like "Read more" or "Subscribe," using only the blue link color with no background.

### Cards
**`article-card`** — The fundamental content unit of the site. A white card with no border-radius, separated from its neighbors by a single hairline-soft rule. Each card contains a display-md title in Garamond Premier Pro, a caption-line of metadata (author, date, category badge), and a body-sm excerpt. On hover, the card gains a subtle #f5f5f5 background tint. The category badge sits in the top-left corner as a small uppercase label in Avenir Next, either in the primary blue for new content or muted gray for archived pieces.

### Navigation
**`nav-bar`** — A 56px cream bar spanning the full viewport width, anchored by the McSweeney's wordmark on the left and a row of nav links on the right. Links are set in Avenir Next 14px weight 600 with generous letter-spacing. The active page is indicated by a 2px blue underline; inactive links render in muted gray. On mobile, the nav collapses into a hamburger menu with a full-screen overlay. The search bar lives as a separate element below the nav on desktop, or inside the mobile menu.

### Forms
**`text-input`** — Standard form fields for search, newsletter signup, and submission forms. White background with a hairline border, 4px corners, and 14px padding. On focus, the border turns blue and a 2px blue ring appears. The search bar follows the same pattern but is slightly shorter (40px) and sits in a dedicated search section below the nav on the homepage.

### Footer
**`footer`** — A deep ink (#1a1a17) footer that grounds the page. Links appear in the primary blue, set in Avenir Next caption size. The footer contains three columns on desktop: About, Categories, and Follow. Copyright and legal text sit in a smaller caption-sm size at the bottom. Padding is generous at {spacing.xxl} top and bottom, creating a visual rest after the content.

### Blockquotes & Section Headings
**`blockquote-component`** — Pull quotes and blockquotes are rendered in italic Garamond Premier Pro at 22px, colored in the deep amber #2a2000, with a 3px left border in the same hue and a soft cream background. Section headings use display-lg Garamond with a 2px amber underline, signaling a new thematic section.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; article cards stack with no side margins; search bar moves inside mobile menu; footer stacks to single column; section padding reduces to 32px |
| Tablet | 744–1128px | Two-column article grid possible; nav links remain visible but condensed; search bar sits below nav; footer shows two columns |
| Desktop | 1128–1440px | Full layout: single-column reading rhythm for articles; three-column footer; nav at full width; search bar prominent below nav |
| Wide | > 1440px | Max-width container at 1128px for content; nav and footer stretch full viewport; increased side margins for readability |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch targets
- Nav links on mobile menu have 48px tap height
- Article card tap targets are the full card width, minimum 64px height
- Search bar submit button is 44x44px minimum

### Collapsing Strategy
- Top nav links collapse into hamburger menu below 744px
- Footer columns collapse from three to one below 744px
- Article grid collapses from two columns to single column below 744px
- Search bar collapses from visible element to menu item below 744px
- Category badges hide on mobile, replaced by color-coded dots

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color palette is heavily weighted toward grays and neutrals (#1a1a17 through #fafafa) with only two distinctive accents: #5bb8f5 (blue) and #2a2000 (amber). The blue was selected as primary based on its use as the only saturated link color in the extracted data. The amber tones (#2a2000, #3a2800, #5a3800) may represent a secondary accent palette for headings and blockquotes, but their exact usage rules could not be confirmed.
- Font stack extracted from CSS includes Garamond Premier Pro, Baskerville, Avenir, and Helvetica Neue, but exact size/weight pairings for all typography tokens are inferred from common literary-site patterns rather than extracted from live CSS.
- Hover states for buttons and links are inferred from the extracted primary-active (#89d0ff) and link-hover (#00b0ff) values, but exact transition durations and shadow effects are unknown.
- Error states for forms (validation, error messages) could not be extracted.
- Dark mode is not confirmed; the extracted palette includes some dark values (#212121, #2e2e2a) that may indicate a dark theme, but no toggle or media-query preference was found.
- Sub-brand or section-specific color variations (e.g., for different McSweeney's series or store products) are not captured.
- The site may use a custom serif font (Garamond Premier Pro) via Adobe Fonts or similar service; the exact font-face declarations and loading strategy are unknown.
- Spacing values are estimated from common literary-site patterns; exact padding/margin values for all components could not be extracted.
- Badge and tag color variants (e.g., for different content types) are speculative.
- The meta theme-color tag was absent, suggesting no browser chrome theming is implemented.
