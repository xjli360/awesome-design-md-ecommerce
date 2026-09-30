---
version: alpha
name: "Stanford University Press"
source_url: "https://www.sup.org"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A scholarly publisher that wears its institutional heritage as a design asset, Stanford University Press builds its digital presence on a foundation of #2e2d29 (a warm, almost-black ink that reads as academic charcoal rather than cold #000) against a canvas of #ebeae4 — a subtle off-white that evokes aged paper stock rather than sterile digital white. The palette draws heavily from the natural world of the California campus: #8c1515 (Stanford Cardinal red) appears sparingly as an accent, while #a1c4b1 and #6aa083 introduce a sage-green quietness that tempers the institutional gravity. Typography splits between Source Serif Pro for reading — a serif face that signals scholarly authority — and Source Sans 3 for UI, creating a clear hierarchy between what is meant to be read (long-form scholarship) and what is meant to be navigated (menus, filters, buttons). The design language is restrained and rectilinear: cards use minimal rounding ({rounded.xs} ~4px), borders are thin and soft (#d5d5d4), and the overall mood is one of quiet competence — a press that trusts its content to command attention rather than demanding it through visual theatrics. The search experience, notably, uses a full-width bar with a prominent magnifying-glass icon in #b1040e, one of the few moments where the brand raises its voice above a murmur.

colors:
  primary: "#8c1515"
  primary-active: "#b1040e"
  primary-disabled: "#d5d5d4"
  ink: "#2e2d29"
  body: "#53565a"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d5d5d4"
  hairline-soft: "#e5e7eb"
  canvas: "#ebeae4"
  surface-soft: "#f2e8f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#a1c4b1"
  accent-sage-dark: "#6aa083"
  accent-stone: "#b6b1a9"
  accent-terracotta: "#5d4b3c"
  accent-warm-gray: "#544948"
  link-blue: "#006cb8"
  link-blue-active: "#2563eb"
  footer-bg: "#2f2424"
  footer-text: "#dcefec"

typography:
  display-xl:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', Times, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', Times, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', Times, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', Times, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Serif Pro', Georgia, 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  meta:
    fontFamily: "'Source Sans 3', 'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-submit:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    height: 48px
    width: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 0
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.button-sm}"
    textColor: "{colors.ink}"
  badge-new:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-series:
    backgroundColor: "{colors.accent-stone}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.footer-text}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  filter-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  filter-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  tab-primary:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  tab-primary-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for key actions like "Add to Cart", "Subscribe", and "Browse All". Rendered in Stanford Cardinal red (#8c1515) with white text on a minimally rounded ({rounded.xs}) rectangle. On hover, shifts to the deeper #b1040e. Disabled state drops to the muted gray #d5d5d4 with #6b7280 text, signaling inactivity without visual noise.

**`button-secondary`** — An outlined alternative for secondary actions such as "View Details" or "Learn More". Uses a transparent background with a 1px #d5d5d4 border and #2e2d29 ink text. Active state thickens the border to the ink color and adds a soft #f2e8f1 background wash.

**`button-tertiary`** — A text-only button reserved for subtle inline actions like "Clear Filters" or "Cancel". Uses the primary red for text color, no background or border, and the smaller button typography to visually subordinate it to primary and secondary buttons.

### Cards
**`product-card`** — The primary content container for book listings across search results, category pages, and the homepage. A white card with no padding at the card level — internal spacing is handled by child elements. The card groups a book cover thumbnail, the title in `{typography.title-sm}`, the author name in `{typography.caption}` in muted gray, and the price in `{typography.button-sm}`. Cards sit flush against each other in a grid with `{spacing.base}` gutters.

**`product-card-title`** — Book titles rendered in 16px Source Sans 3 semibold, the ink color. Truncates to two lines with an ellipsis on overflow.

**`product-card-author`** — Author names in 14px Source Sans 3 regular, muted gray. Prefixed with "by " in the same style.

**`product-card-price`** — Pricing displayed in 14px Source Sans 3 semibold, ink color. For sale items, the original price is shown as strikethrough in muted-soft gray alongside the sale price in primary red.

### Navigation
**`nav-bar`** — The persistent top navigation bar, 64px tall, set against the warm off-white canvas (#ebeae4). Contains the Stanford University Press wordmark on the left, a set of nav links (Books, Subjects, Series, About, Blog) in 15px Source Sans 3 semibold, and a search icon on the right. The bar uses a subtle bottom border in #d5d5d4.

**`nav-link-active`** — The active nav link state, distinguished by a 2px bottom border in Stanford Cardinal red (#8c1515). The link text remains the ink color.

**`nav-link-inactive`** — Inactive nav links rendered in muted gray (#6b7280) with no bottom border. On hover, the text transitions to the ink color.

### Forms
**`text-input`** — Standard text input fields used in search filters, account forms, and checkout. A white background with a 1px #d5d5d4 border, 12px/16px padding, and 44px height. Focus state swaps the border to #8c1515. Error state uses #b1040e for both border and text color.

**`search-bar`** — The primary search input, 48px tall with a white background and 1px hairline border. The input uses body serif typography (18px Source Serif Pro) to match the reading experience. A 48px square submit button in #b1040e with a white magnifying glass icon sits at the right edge.

**`filter-dropdown`** — Dropdown selectors used on category and search results pages for sorting and filtering. A compact 40px tall field with a white background, 1px hairline border, and caption typography. The dropdown arrow is rendered in muted gray.

### Badges & Tags
**`badge-new`** — A small sage-green (#a1c4b1) pill badge used to flag newly published titles. Uses 11px uppercase Source Sans 3 bold with 0.5px letter-spacing. Minimal padding (2px/8px) keeps it compact.

**`badge-sale`** — A red (#8c1515) badge for discounted titles, using the same typography and sizing as the new badge but with white text for contrast.

**`badge-series`** — A stone-colored (#b6b1a9) badge indicating a book belongs to a specific series or collection. Uses the same sizing and typography as other badges.

**`filter-tag`** — Active filter indicators that appear above search results. Rendered as full-pill shapes in the soft surface color (#f2e8f1) with a small "×" dismiss icon. Active state shifts to the primary red background with white text.

### Footer
**`footer`** — The site footer, a dark panel (#2f2424) with light text (#dcefec). Contains columns for About, Subjects, Series, and Connect, each with a heading in `{typography.title-sm}` and links in `{typography.link}`. The footer uses generous vertical padding ({spacing.xxl}) and sits at the bottom of every page.

**`footer-link`** — Footer navigation links in the light sage text color (#dcefec). On hover, the text lightens toward white.

### Hero & Content
**`hero-section`** — The homepage hero, a full-width panel on the off-white canvas background. Contains a large display headline (36px Source Serif Pro bold), a supporting subtitle in body typography, and a primary CTA button. The section uses 64px vertical padding and 32px horizontal padding.

**`hero-cta`** — The hero's primary call-to-action button, slightly larger than standard buttons at 14px/32px padding and 48px height. Uses the same primary red styling as `button-primary` but with more generous internal spacing.

**`breadcrumb`** — Breadcrumb navigation appearing on category and product pages. Rendered in 13px Source Sans 3 regular, muted gray, with ">" separators between levels. The active (current page) breadcrumb uses the ink color.

**`pagination`** — Page number navigation at the bottom of search results and category listings. Individual page numbers are rendered as clickable text in button-sm typography, muted gray. The active page number gets a primary red background with white text and minimal rounding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product grid switches to single column; hero section reduces padding to {spacing.lg}; search bar becomes full-width below nav; footer columns stack vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product grid shows 2–3 columns; hero uses {spacing.xl} padding; sidebar filters become horizontal filter strip above results |
| Desktop | 1128–1440px | Full nav with all links; 3–4 column product grid; hero at full {spacing.section} padding; sidebar filters visible on left; breadcrumb shown |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grid can show 4–5 columns; hero content max-width at 1128px; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Filter tags and badges are at least 32px tall with 12px horizontal padding for comfortable tapping
- Nav links have a minimum 40px tap area, even when text is smaller
- Pagination numbers are at least 40px × 40px tap targets
- Search submit button is 48px × 48px

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu at < 744px, with a slide-in drawer from the left
- Sidebar filters collapse to a horizontal filter strip at < 1128px, then to a "Filters" button that opens a modal at < 744px
- Footer columns stack vertically at < 744px, with accordion-style expand/collapse for each column heading
- Product grid reduces columns progressively: 5 → 4 → 3 → 2 → 1
- Breadcrumb truncates to show only the current page and one parent level at < 744px, with a "Back" link replacing the full trail

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted from static CSS; `button-primary-active` and `button-secondary-active` are inferred from common patterns rather than confirmed from the live site
- Error, success, and warning form validation states beyond the text-input error state are undocumented
- Dark mode is not present on the live site and no dark-mode color tokens exist
- Sub-brand or imprint-specific palettes (e.g., Stanford Briefs, Stanford Studies in Middle Eastern and Islamic Societies) could not be extracted
- The extracted color list includes several generic blues (#2563eb, #006cb8) that likely come from link styling or third-party widgets rather than brand identity — these are included as `link-blue` tokens but may not be intentional brand colors
- Font sizes and line heights for typography tokens are estimated from common academic press patterns and the extracted font declarations; exact values from the live site's computed styles were not available
- Animation durations, easing curves, and transition properties are not documented
- Focus-visible ring styles for keyboard navigation are not specified
- The Stanford University Press wordmark/logo SVG or its exact spacing requirements are not captured
- Print stylesheet behavior is not documented
