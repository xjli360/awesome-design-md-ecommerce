---
version: alpha
name: "Amigo Games"
source_url: "https://amigo.games"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A press release page for Amigo Games, the card game publisher behind *The Game* and *Saboteur*, uses a starkly utilitarian interface that prioritizes information delivery over visual personality. The page is built entirely on a white canvas (`#ffffff`) with black ink (`#000000`) and a single blue accent (`#1990c6`) reserved exclusively for hyperlinks — no primary brand color, no decorative flourishes, no game-themed illustration. Body text runs at 16px in a system font stack (Arial, Helvetica, sans-serif) with 1.5 line-height, creating a reading experience indistinguishable from a government document or academic press release. The only design move that signals "this is a games company" is the logo lockup at the top: a red-and-white square mark (unreadable in extraction) paired with the wordmark, set against the white field. Below that, the page is a single column of text blocks — headline in bold 24px, dateline in italic 14px, body paragraphs separated by 24px gaps — with no cards, no CTAs, no product imagery, no social proof. The blue link color (`#1990c6`) is the only non-neutral element, and it appears only in the email contact at the bottom. This is a brand that, in this context, has chosen to disappear into the generic web — the design system is essentially the browser default with a logo pasted on top.

colors:
  primary: "#1990c6"
  primary-active: "#1478a8"
  primary-disabled: "#b3d9f0"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#1990c6"
  link-visited: "#551a8b"
  logo-red: "#cc0000"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.44
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption-italic:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.43
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  link-inline:
    textColor: "{colors.link}"
    typography: "{typography.link}"
  link-visited:
    textColor: "{colors.link-visited}"
    typography: "{typography.link}"
  logo-lockup:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 80px
  press-release-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  press-release-dateline:
    typography: "{typography.caption-italic}"
    textColor: "{colors.muted}"
  press-release-body:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  footer-contact:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — A flat, rectangular button with no border radius, using the blue accent (`#1990c6`) as background and white text. On hover, shifts to `#1478a8` (`primary-active`). Disabled state uses `#b3d9f0` (`primary-disabled`). Padding is 12px vertical, 24px horizontal, with 44px height. This button is not present on the press release page but would be used for any game purchase or sign-up flow.

**`button-secondary`** — White background with black text and a 1px `#cccccc` border. Same dimensions as primary. Used for secondary actions like "Learn More" or "View All Games." No border radius — consistent with the brand's flat, no-frills approach.

### Links
**`link-inline`** — The only interactive element on the press release page. Blue (`#1990c6`) with underline, 16px Arial. Visited state shifts to `#551a8b` (browser default). No hover color change detected — likely remains blue. Used for email addresses and external references.

### Navigation
**`nav-bar`** — A simple 60px white bar at the top of the page, containing the logo lockup and a horizontal list of text links (Games, About, Press, Contact). Links are 14px Arial, black, no underline until hover. No dropdowns, no search, no icons — just text.

### Logo
**`logo-lockup`** — An 80px-tall white container holding the Amigo Games logo: a red (`#cc0000`) square mark with a white geometric shape (likely a stylized "A" or game piece) alongside the wordmark in black Arial. The logo is left-aligned and does not link to the homepage (it's already on the page).

### Press Release
**`press-release-headline`** — 24px bold Arial, black, no letter-spacing. Set as a single `<h1>` at the top of the content area. No decorative line, no icon, no background — just text on white.

**`press-release-dateline`** — 14px italic Arial, gray (`#666666`), placed directly below the headline. Contains the city, date, and "—" em dash before the body text begins.

**`press-release-body`** — 16px regular Arial, dark gray (`#333333`), 1.5 line-height. Paragraphs separated by 24px gaps. No images, no pull quotes, no sidebars — a single column of text.

### Footer
**`footer-contact`** — 14px Arial, gray (`#666666`), containing the company address and email link. The email uses `link-inline` styling. No social media icons, no newsletter signup, no sitemap — just a text block.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single column layout; logo lockup shrinks to 60px height; body text remains 16px; margins reduce to 16px on each side |
| Tablet | 744–1128px | Content max-width at 720px centered; logo lockup at 80px; margins at 24px |
| Desktop | 1128–1440px | Content max-width at 960px centered; full logo lockup height; margins at 32px |
| Wide | > 1440px | Content max-width at 1120px centered; no further scaling |

### Touch Targets
- All links: minimum 44px height (text only, no padding)
- Logo lockup: 80px height, easily tappable
- No buttons present on press release page

### Collapsing Strategy
- No navigation menu to collapse (text links remain visible at all widths)
- No images to hide or resize
- Content remains single column at all breakpoints
- Logo lockup reduces height on mobile but does not collapse

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations could be extracted from the live site — the system font stack (Arial, Helvetica, sans-serif) is inferred from browser defaults and common practice; the brand may use a custom typeface on other pages
- No primary brand color could be extracted — the blue `#1990c6` is used only for links and may not be the brand's actual primary; the red `#cc0000` in the logo is a candidate but could not be confirmed from CSS
- No hover states, active states, or focus styles could be extracted for any interactive element
- No button components exist on the press release page — button styling is speculative based on common patterns
- No form elements, error states, or validation styling could be extracted
- No dark mode or high-contrast mode styling detected
- No animation, transition, or interaction patterns could be extracted
- The press release page may not be representative of the full brand experience — product pages, game instructions, and e-commerce flows likely have richer design systems
- No social media icons, share buttons, or footer navigation could be extracted
- No card components, grid systems, or layout patterns beyond single-column text could be confirmed
