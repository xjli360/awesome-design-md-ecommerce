---
version: alpha
name: "Loll Designs"
source_url: "https://lolldesigns.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Milk jugs melted into Adirondack chairs — that material story shows up in every pixel of Loll's digital system. The primary brand teal (#108474) lands somewhere between a recycling bin icon and a shaded tree canopy, appearing on CTAs, active nav states, and the chunky "Shop" button that anchors the header. Surrounding it, a roster of playful product-swatch colors — sunny gold (#ffce07), soft coral (#fb8077), and a dusty lavender (#a89cc8) — rotate through hero banners and collection badges, reinforcing that this is furniture you configure in dozens of bold hues rather than safe beige. Typography pairs Nunito Sans for UI and body text with Baskerville pull-quotes on editorial pages; Nunito's generous x-height and rounded terminals echo the brand's physical forms — no sharp miter joints, just soft radii (`{rounded.md}` on cards, `{rounded.sm}` on inputs, `{rounded.full}` on color-swatch dots). The canvas stays light: a near-white #f9fafb base layered with #f2f2f2 section bands and #eeeeee card surfaces, keeping saturated product photography the loudest element on any viewport. Spacing runs wide — `{spacing.section}` or larger between content blocks on desktop — because Loll's pieces are meant to breathe in open air, and the layout mimics that openness. Navigation is flat and utilitarian: a sticky header with a teal wordmark, category links in `{typography.nav-link}`, and a persistent cart icon; no mega-menus, no hover animations, just direct paths to collections. Product cards carry a slight elevation via a 1px #dedede border rather than a drop-shadow, keeping the page feeling eco-printed rather than glossy-tech. The overall effect is a porch on a Saturday morning — bright color, clean surfaces, unhurried hierarchy.

colors:
  primary: "#108474"
  primary-active: "#0b6b5e"
  primary-disabled: "#c1e6e6"
  secondary-gold: "#ffce07"
  secondary-gold-active: "#caa700"
  accent-coral: "#fb8077"
  accent-lavender: "#a89cc8"
  accent-teal-light: "#c1e6e6"
  ink: "#212121"
  body: "#555555"
  muted: "#6c6c6c"
  muted-soft: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  border-strong: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-mid: "#f2f2f2"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#d02e2e"
  dark-accent: "#4d3f3f"
  scrim: "#212121"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  editorial-quote:
    fontFamily: "Baskerville, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  body-lg:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  label:
    fontFamily: "'Nunito Sans', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.border-strong}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.sm}"
  button-gold-accent:
    backgroundColor: "{colors.secondary-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
    position: sticky
  nav-bar-scrolled:
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4/3"
    objectFit: cover
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.price}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 28px
    width: 28px
    border: "2px solid {colors.hairline}"
    borderActive: "2px solid {colors.ink}"
  color-swatch-sm:
    rounded: "{rounded.full}"
    height: 18px
    width: 18px
  hero-banner:
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    textColor: "{colors.on-dark}"
    overlayGradient: "linear-gradient(to right, rgba(33,33,33,0.55) 0%, transparent 60%)"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-dark}"
  collection-badge:
    backgroundColor: "{colors.secondary-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  sustainability-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  footer-link:
    textColor: "{colors.hairline}"
    textColorHover: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.05)"
  breadcrumb:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.border-strong}"

---

## Components

### Buttons

**`button-primary`** — Teal (#108474) background with white text, 8px border-radius, and bold 700-weight Nunito Sans at 16px. On hover the background darkens to `primary-active` (#0b6b5e); disabled state fades to the light teal `primary-disabled` (#c1e6e6) with muted text. Used for "Add to Cart," "Shop Now," and primary form submissions.

**`button-secondary`** — White background with a 1px `border-strong` (#bbbbbb) border and dark ink text. On hover the border sharpens to ink (#212121) and the background picks up `surface-soft`. Frequently used for "View Details" and filter toggles on collection pages.

**`button-gold-accent`** — Bright yellow (#ffce07) background with dark text, slightly smaller at 44px height. Reserved for promotional callouts and seasonal sale banners where the teal primary would compete with product imagery.

### Navigation

**`nav-bar`** — A sticky 72px header on white canvas with a 1px bottom hairline. Logo sits left (teal wordmark rendered via the custom "loll" icon font), center houses category links in `nav-link` weight-600 type, and right holds cart/account icons. On scroll, gains a subtle box-shadow to separate from content. Mobile collapses to a hamburger with full-screen overlay.

**`announcement-bar`** — A 40px teal strip above the nav carrying shipping/promo messaging in white caption text. Dismissible on mobile.

### Product Cards

**`product-card`** — Light #eeeeee background card with a 1px #dedede border and 12px radius. Product image fills a 4:3 container with 8px radius. Below: title in `title-sm`, price in bold `price` type, and a row of `color-swatch` circles showing available HDPE colors. On hover, the border transitions to teal, providing a subtle selection cue without elevation change.

**`color-swatch`** — 28px circles with `rounded.full`, showing the actual material color. Active state gains a 2px ink border. Small variant (18px) appears in cart line items and quick-compare overlays.

### Hero

**`hero-banner`** — Full-bleed lifestyle photography (outdoor patios, fire pits, lakeside decks) at minimum 560px height. A left-aligned gradient overlay darkens just enough for white `display-xl` headlines and `body-lg` subheads. CTA button sits below in `button-primary` or `button-gold-accent` depending on campaign.

### Badges

**`collection-badge`** — Gold (#ffce07) pill with uppercase label text and dark ink color. Marks "New," "Best Seller," or "Limited Edition" on collection grid items.

**`sustainability-badge`** — Teal background, white text, extra-small radius. Appears on PDP pages communicating recycled content percentage or warranty info.

### Search

**`search-bar`** — Sits in the nav on desktop (expandable) or full-width on mobile search page. Light gray `surface-soft` background, 8px radius, 1px hairline border that transitions to teal on focus. Placeholder text in `muted` color.

### Configurator

**`configurator-panel`** — White panel with 12px radius, light border, and subtle shadow. Houses the color/material selector on PDP pages where customers build their furniture configuration step-by-step. Contains `color-swatch` groups, dimension selectors, and a sticky "Add to Cart" button at panel bottom.

### Footer

**`footer`** — Dark ink (#212121) background with generous section padding. Four-column layout on desktop: brand story, shop links, support links, and newsletter signup. Headings in `title-sm` weight-600 white, links in #dedede that brighten to white on hover. Bottom row carries legal links, social icons, and the "Made from recycled materials" tagline.

### Breadcrumb

**`breadcrumb`** — Simple inline path at `body-sm` in muted gray, separated by forward-slash characters in `border-strong` color. Appears below the nav on collection and product detail pages.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav with slide-out drawer, hero image becomes 320px min-height with stacked text below image, configurator panel goes full-width fixed to bottom, footer stacks to single column with accordions |
| Tablet | 744–1128px | Two-column product grid, nav links collapse to hamburger, hero retains overlay layout at reduced height (440px), configurator panel inline below product images |
| Desktop | 1128–1440px | Three-column product grid, full nav with all category links visible, hero at 560px with gradient overlay, configurator panel sits right of product gallery in 40/60 split |
| Wide | > 1440px | Content max-width 1440px centered, four-column product grid on large collections, increased section spacing (`section-lg`), hero scales proportionally with capped text width at 600px |

### Touch Targets

- All interactive elements minimum 44×44px tap area on mobile
- Color swatches expand to 36px on touch devices with 8px gap between
- Nav hamburger icon padded to 48×48px
- "Add to Cart" button stretches full-width on mobile with 56px height
- Footer links spaced with 12px vertical padding for thumb reach

### Collapsing Strategy

- Desktop mega-nav category links collapse into a hamburger drawer at tablet breakpoint
- Product filters move from a persistent left sidebar to a top "Filter" button triggering a bottom sheet on mobile
- Configurator panel repositions from side-by-side (desktop) to below-gallery (tablet) to fixed-bottom drawer (mobile)
- Footer four-column grid becomes stacked accordions on mobile, each section collapsible
- Announcement bar text truncates with ellipsis on narrow viewports; swipe for multiple messages

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom icon font "loll" glyphs could not be mapped — glyph names and unicode points unknown
- Exact animation/transition durations not extractable from static hints (likely 200–300ms ease for hover states)
- Baskerville usage context unclear — may be limited to blog/editorial pages or removed in recent updates
- Multiple near-identical yellows extracted (#ffce07, #fdd100, #fbcd0a) — unclear which is canonical; using #ffce07 as it appeared most frequently
- No elevation/shadow tokens extractable; shadow values estimated from typical Shopify theme patterns
- Mobile nav drawer animation style (slide vs. fade) not determinable
- Newsletter signup form styling and success/error states not captured
- Sustainability page-specific layout components (timeline, material breakdown graphics) not represented
