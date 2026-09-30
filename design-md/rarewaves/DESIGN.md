---
version: alpha
name: "Rarewaves"
source_url: "https://www.rarewaves.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-indigo (#2d398e) backbone anchors Rarewaves as a discount entertainment marketplace that feels more like a record-store discovery bin than a sterile e-commerce grid. That primary blue, pulled from the extracted site palette, runs across the top navigation bar, primary buttons, and footer — a confident, almost academic hue that signals value without discount-screaming. The brand’s secondary voltage comes from a warm marigold (#fbd600) used for price tags, sale badges, and hover states, creating a visual shorthand for “deal” that reads as cheerful rather than desperate. A supporting cast of accent colors — lime (#b1d135), teal (#00a54f), sky (#29aae1), magenta (#ea088e), and deep purple (#652f8e) — appear in category icons, genre badges, and promotional banners, giving the site a toy-box eclecticism that mirrors the breadth of its catalog (vinyl, Blu-ray, books, games). Typography splits between Mulish (a clean geometric sans for body text, navigation, and buttons) and Playfair Display (a high-contrast serif used sparingly for hero headlines and product titles, lending a touch of literary or cinematic gravitas). Cards use a soft {rounded.sm} (8px) radius, while search bars and filter pills adopt {rounded.full} for a friendly, approachable feel. The canvas is a warm off-white (#f5f5f5) rather than pure white, softening the reading experience across long browsing sessions. The overall impression is of a well-organized independent shop where every shelf section has its own color-coded spine label, and the checkout flow — powered by Shopify — fades into a clean, distraction-free white surface.

colors:
  primary: "#2d398e"
  primary-active: "#1e2670"
  primary-disabled: "#9da3c7"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#f5f5f5"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#fbd600"
  accent-lime: "#b1d135"
  accent-teal: "#00a54f"
  accent-sky: "#29aae1"
  accent-magenta: "#ea088e"
  accent-purple: "#652f8e"
  accent-orange: "#f69220"
  accent-red: "#eb2429"
  accent-teal-dark: "#17a8a2"
  accent-rose: "#95208c"
  accent-violet: "#8a06a4"
  accent-lavender: "#b866d9"
  accent-coral: "#d44437"
  star-rating: "#fbd600"
  sale-badge: "#eb2429"
  price-tag: "#fbd600"

typography:
  display-xl:
    fontFamily: "'Playfair Display', 'Playfair Display-fallback', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', 'Playfair Display-fallback', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'Mulish', 'Mulish-fallback', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    color: "{colors.accent-red}"

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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 9px 15px
    height: 44px
  top-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 0 16px
    height: 56px
  top-nav-link-active:
    backgroundColor: "rgba(255, 255, 255, 0.15)"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.xs}"
    padding: 0 16px
    height: 56px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: 7px 15px
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    marginTop: "{spacing.xs}"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  category-badge-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  filter-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 16px"
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
    rounded: "{rounded.sm}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.xxl} {spacing.lg}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 1
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  newsletter-button:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  breadcrumb-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-current:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    height: 40px
  add-to-cart-button:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
  checkout-button:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the site, rendered in the deep indigo primary (#2d398e) with white uppercase Mulish text. On hover, it shifts to a darker navy (#1e2670) to signal action. The disabled state uses a muted periwinkle (#9da3c7) to indicate unavailability without confusing the user with a different color family.

**`button-secondary`** — An outlined variant with a white fill and indigo border, used for less prominent actions like "View Details" or "Cancel." The 2px border maintains visual weight parity with the primary button, while the white background keeps it clean against the off-white canvas.

**`button-accent-marigold`** — A high-energy marigold (#fbd600) button reserved for promotional calls-to-action, sale banners, and checkout flows. The dark ink (#121212) text ensures strong contrast against the bright yellow, and the button reads as urgent but cheerful — never alarmist.

**`button-accent-orange`** — Used specifically for newsletter signup and limited-time offers. The warm orange (#f69220) against white text creates a secondary promotional tier below the marigold, useful for A/B testing different offer intensities.

**`add-to-cart-button`** — A teal (#00a54f) button that signals a positive, confirmatory action. This green-adjacent hue is distinct from the primary indigo and the promotional marigold, giving the shopping cart action its own visual territory.

**`checkout-button`** — The final purchase CTA, rendered in marigold (#fbd600) to maximize visibility and conversion. This button appears only on the cart and checkout pages, where the Shopify-powered flow takes over.

### Cards
**`product-card`** — A white card with 8px rounded corners containing a product image, title, and price. The card sits on the off-white canvas (#f5f5f5) with no border — the shadow of the image and the typography create the card boundary. On hover, a subtle box-shadow elevates the card, mimicking the physical act of picking up a record or book for closer inspection.

**`product-card-title`** — Set in Mulish 16px/600, the title truncates to two lines maximum. For vinyl and Blu-ray products, the artist or director name appears as a smaller secondary line in muted gray.

**`product-card-price`** — The current price in bold 16px Mulish. Sale prices render in red (#eb2429) with the original price struck through in muted-soft (#999999) beside it.

### Navigation
**`top-nav`** — A 56px indigo (#2d398e) bar spanning the full viewport width. Navigation links are white with 0.3px letter spacing, and the active or hover state adds a semi-transparent white overlay (15% opacity) behind the link text. The bar contains the Rarewaves logo on the left, category links in the center, and account/cart icons on the right.

**`search-bar`** — A full-width, pill-shaped input field with a white background and subtle gray border. On focus, the border thickens to 2px and shifts to the primary indigo. The search icon sits inside the pill on the left, and a voice-search or camera-search icon may appear on the right in future iterations.

**`breadcrumb-link`** — Small, muted-gray links in 12px Mulish that show the user's navigation path (e.g., Home > Movies > Blu-ray > Action). The current page renders in the primary indigo for positional awareness.

### Badges & Labels
**`sale-badge`** — A compact red (#eb2429) badge with white uppercase text, placed in the top-left corner of product-card images. The badge reads "SALE" or a percentage off, and its small size (2px/8px padding) ensures it doesn't obscure the product artwork.

**`category-badge`** — Soft, pill-shaped tags used in filter strips and category navigation. The default state is a light gray background with muted text; the active state fills with the primary indigo and white text. These badges allow users to quickly toggle between genres (Rock, Jazz, Classic Film, etc.).

**`star-rating`** — A 5-star display using the marigold (#fbd600) for filled stars and hairline (#dedede) for empty stars. Ratings appear on product cards and detail pages, with the numeric average displayed beside the stars in body-sm Mulish.

### Forms
**`text-input`** — Standard form input with a white background, 8px rounded corners, and a 1px hairline border. Focus state upgrades to a 2px indigo border. Used for email collection, search queries, and address forms.

**`newsletter-input`** — A dedicated email input styled to pair with the orange newsletter button. The input and button sit side-by-side in the footer, forming a combined 44px height row.

**`quantity-selector`** — A compact input with increment/decrement buttons on either side, used on product detail and cart pages. The 40px height matches the add-to-cart button for visual alignment.

### Footer
**`footer`** — A deep indigo (#2d398e) section containing link columns, social media icons, and the newsletter signup form. Links render at 85% opacity by default and become fully opaque on hover. The footer uses the same background as the top nav, creating a bookend effect for the page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu; search bar moves below nav; footer stacks vertically; category badges wrap to two rows; hero banner reduces to 32px padding |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (Home, Movies, Music, Books); search bar remains full-width; footer splits into two columns; category badges show in a horizontal scrollable strip |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all category links; search bar sits in nav row; footer displays four columns; hero banner uses 48px padding; product cards show hover shadow |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centers content; top-nav links spread with generous spacing; hero banner may include a secondary promotional panel beside the main hero |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons (cart, account, search) use 44x44px tap targets even if the visible icon is smaller
- Filter pills and category badges use 36px minimum height with 16px horizontal padding
- Product card links (image + title) use the full card area as a tap target

### Collapsing Strategy
- Top navigation collapses from full link set to hamburger icon at 744px breakpoint
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Footer columns collapse from 4 to 2 to 1 stacked layout
- Category filter strip switches from horizontal scroll to a dropdown "Filter by" button below 744px
- Hero banner image hides on mobile, showing only the text and CTA button
- Search bar moves from inline (desktop) to full-width below nav (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (especially secondary buttons, filter pills, and footer links) were inferred from common patterns rather than extracted from the live site
- Error styling for form inputs (validation messages, error borders) was not observable in the extracted data
- The exact font weights and sizes for Playfair Display headings are estimated based on typical usage; the extracted CSS only showed fallback declarations
- Dark mode is not supported and no dark-mode color tokens were found
- The Shopify checkout flow uses its own design system (Shopify Checkout) which may override Rarewaves' colors and typography — the extracted palette may include Shopify Pay button colors that are not part of the Rarewaves brand
- Social media icon colors (Facebook blue, Twitter blue, Instagram gradient) were filtered from the extracted palette but may still appear in the footer
- The extracted color list includes 18 hex values, many of which are likely accent or promotional colors rather than core brand tokens — the primary (#2d398e) and marigold (#fbd600) are the most reliably branded
- No animation or transition timing values were extracted (ease-in-out durations, spring curves, etc.)
- The "Mulish-fallback" and "Playfair Display-fallback" font-family declarations suggest a custom font loading strategy, but the exact font files and weights available were not determined
- Product card shadow values and hover transitions were inferred from common e-commerce patterns
- The newsletter signup form's success/error states were not observed
- Accessibility contrast ratios for accent colors (especially marigold on white, magenta on indigo) have not been verified against WCAG standards
