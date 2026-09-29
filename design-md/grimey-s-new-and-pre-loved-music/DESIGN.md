---
version: alpha
name: "Grimey's New & Pre-Loved Music"
source_url: "https://www.grimeys.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, ink-black (#112233) canvas sets the stage for a record store that feels more like a late-night listening session than a retail transaction. The brand's primary voltage is a weathered crimson (#bd0000) that appears on the "New Arrivals" badge, the shopping-cart icon, and the footer's newsletter call-to-action — a single accent that reads like a vintage record-label logo rather than a generic ecommerce button. The site's typography runs Alice, a serif face with the warmth of a handwritten setlist, at 16–20px for body copy, while navigation links sit in Arial at 14px with a muted gray (#aaaaaa) that recedes into the dark background. Product cards float on a near-white surface (#fafafa) with a soft shadow, their corners gently rounded ({rounded.md}), mimicking the feel of flipping through a crate of LPs. The footer is a dense block of deep navy (#112244) with links in a faded rose (#e99292), a quiet nod to the store's East Nashville location and its reputation for curated, pre-loved vinyl. The overall mood is intimate and unpolished — no hero sliders, no auto-playing video, just a grid of album covers, a search bar with a subtle red border, and the promise of "New & Pre-Loved" in every interaction.

colors:
  primary: "#bd0000"
  primary-active: "#8f0000"
  primary-disabled: "#e99292"
  ink: "#112233"
  body: "#1e1e1e"
  muted: "#aaaaaa"
  muted-soft: "#cccccc"
  hairline: "#272727"
  hairline-soft: "#e1e1e1"
  canvas: "#fafafa"
  surface-soft: "#fbfbfb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rose: "#e99292"
  accent-navy: "#112255"
  accent-dark-navy: "#112244"
  footer-bg: "#112244"
  footer-link: "#e99292"
  border-light: "#eeeeee"

typography:
  display-xl:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Alice', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Arial', 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
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
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  badge-new-arrival:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.primary}"
  footer-section:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-link}"
    typography: "{typography.link}"
    padding: 48px 24px
  footer-link:
    color: "{colors.footer-link}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and "Checkout". Rendered in the brand's weathered crimson (#bd0000) with white text and a 12px horizontal padding. On hover, the background darkens to `{colors.primary-active}` (#8f0000). The disabled state uses `{colors.primary-disabled}` (#e99292) with white text, signaling an unavailable action. The button uses `{typography.button-md}` (14px Arial bold) for legibility against the dark background.

**`button-secondary`** — A ghost-style button for secondary actions like "View Details" or "Learn More". Uses a white background with ink (#112233) text, matching the primary button's height and padding. On hover, a subtle border or background shift could be applied, though the extracted data doesn't confirm a specific hover state.

### Cards
**`product-card`** — The core product display for vinyl records, CDs, and merchandise. A white card (`{colors.surface-card}`) with 16px padding and a 12px border radius (`{rounded.md}`). The album cover image sits at the top with a 8px radius (`{rounded.sm}`), followed by the artist name, album title, and price in `{typography.body-sm}`. The card's background contrasts against the site's near-white canvas (#fafafa), creating a subtle stacking effect.

**`badge-new-arrival`** — A small, uppercase badge pinned to the top-left of product cards. Uses the primary red (#bd0000) with white text, 4px padding, and a 4px border radius. The badge signals recently added inventory, a key differentiator for a store that emphasizes "new & pre-loved" stock.

**`badge-sale`** — A secondary badge for discounted items. Uses the faded rose (#e99292) on a dark ink background, maintaining readability while distinguishing from the primary badge.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, rendered in the brand's deep ink (#112233) with white navigation links. The logo (likely "Grimey's" in Alice serif) sits on the left, with links like "New Arrivals", "Vinyl", "CDs", "Events", and "About" in 14px Arial bold. The bar uses no border radius, creating a sharp, authoritative top edge.

**`category-tag`** — A pill-shaped tag for filtering product categories (e.g., "Rock", "Jazz", "Folk"). Uses a soft background (`{colors.surface-soft}`) with muted gray text and full rounding (`{rounded.full}`). The tags are compact at 6px vertical padding, allowing multiple tags to sit in a horizontal strip.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and checkout forms. A white background with 12px padding and a 8px border radius. The input uses `{typography.body-md}` (16px Alice) for readability. The search variant includes a 2px red border (`{colors.primary}`) to draw attention.

**`search-bar`** — The primary search component, identical to `text-input` but with a red border (#bd0000) that signals the store's search function. The placeholder text reads "Search artists, albums, or genres..." in `{typography.body-md}`.

### Footer
**`footer-section`** — A deep navy (#112244) footer block with 48px vertical padding. Links appear in the faded rose (#e99292) on the dark background, creating a warm, vintage feel. The footer includes sections for "Hours & Location", "Newsletter Signup", "Social Links", and "Support". The typography uses `{typography.link}` (14px Arial) for consistency.

### Hero
**`hero-banner`** — A full-width hero section for featured releases or events. Uses the ink (#112233) background with white text in `{typography.display-xl}` (28px Alice). The hero includes a single headline and a subtle divider, with no auto-playing media. The padding is generous at 64px top and bottom, creating a breathing room that contrasts with the dense product grid below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero reduces to 32px padding; search bar moves below nav; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible; hero padding at 48px; search bar in nav row; footer splits into two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full padding (64px); search bar prominent in header; footer in three columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero scales with padding; search bar expands to 600px max-width |

### Touch Targets
- All buttons and links maintain a minimum 44px height for touch accessibility
- Product cards have a 48px minimum tap area for "Add to Cart" buttons
- Category tags are at least 32px tall with 16px horizontal padding
- Nav links on mobile have 48px tap targets

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer
- The product grid collapses from 3–4 columns to 1 column, with full-width cards
- The hero banner reduces padding and may hide secondary text
- The footer collapses from 3 columns to a single vertical stack
- Category tags wrap to multiple rows on smaller screens

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons, links, and cards are not fully confirmed from extracted data; `button-primary-active` is an inference based on common darkening patterns
- Error styling for form inputs (e.g., invalid email, missing required fields) is not available
- Sub-brand or seasonal color palettes (e.g., Record Store Day, holiday promotions) are not captured
- Dark mode or high-contrast mode styles are not present in the extracted data
- Typography scale for mobile (e.g., reduced font sizes) is not confirmed; the current scale assumes desktop-first
- Spacing values for specific components (e.g., card margins, grid gaps) are inferred from common patterns rather than extracted
- The exact font weight for Alice (likely 400) is assumed; no weight variations were found in the extracted CSS
- The `hero-banner` component is inferred from the site's structure; no specific hero styles were extracted
- The `category-tag` component's hover state is not documented
- The `search-bar` border color is inferred from the primary color; no specific search border was extracted
