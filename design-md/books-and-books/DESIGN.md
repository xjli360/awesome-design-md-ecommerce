---
version: alpha
name: "Books & Books"
source_url: "https://www.booksandbooks.com"
captured_at: "2026-09-29T04:22:07.853349+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Books & Books runs its storefront on a Drupal-based commerce theme (shop.booksandbooks.com) whose
  CSS custom properties expose a two-tone action palette: `--color-primary: #000000` and
  `--color-secondary: #52409d`, a muted violet. Buttons and form controls swap between these two
  values on hover/active, so this spec treats the violet as the brand's primary accent (its more
  distinctive, brand-specific hue) and pure black as a secondary ink/heading color, reusing both
  across components per the observed toggle behavior. Body copy renders in Figtree (`--font-family:
  var(--font-figtree)`), the only font explicitly wired to a live CSS variable; Domine, a serif also
  present in the site's loaded font stack, is proposed here for display headings to reflect the
  literary, independent-bookstore character suggested by the events/staff-pick/banned-books content —
  this heading-role pairing is inferred, not confirmed by a captured heading selector. Neutral grays
  (#fafafa–#404040 range) and hairline tones (#dddddd, #e5e5e5) come directly from the supplied
  palette and are assigned to backgrounds, muted text, and dividers by convention. A warm yellow
  (#fffa90) and a red (#da4343) from the palette are reserved for tag-style badges (SIGNED, STAFF
  PICK, sale/banned-books callouts) seen in the page's merchandising rails; their exact production
  usage is inferred, not observed in a captured badge rule.

colors:
  primary: "#52409d"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#404040"
  muted: "#696969"
  hairline: "#dddddd"
  surface-soft: "#fafafa"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  border-strong: "#c8c8c8"
  badge-sale: "#da4343"
  highlight: "#fffa90"
  accent-teal: "#1a936f"
typography:
  display-xl: {fontFamily: "Domine, serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Domine, serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Figtree, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Figtree, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Figtree, sans-serif", fontSize: 12px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Figtree, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0.5px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
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
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  event-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.body-sm}"
    dateBadgeBackground: "{colors.primary}"
    dateBadgeTextColor: "{colors.on-primary}"
    cta: "button-primary"

## Components

**button-primary / button-secondary**: The captured CSS shows default submit/button elements filled with the violet secondary color, swapping to black on hover, while `.button--primary` does the reverse — black by default, violet on hover. This spec resolves that ambiguity by fixing violet as the primary action fill and black as a secondary/alternate fill, both reusing the same two observed hex values; hover/active states are proposed, not re-verified pixel-for-pixel.

**text-input**: Derived from the theme's `--form--border-radius: 2px` and `--form--border-color` variables (mapped to the hairline gray), giving a tight, minimal input outline consistent with a utilitarian storefront search/filter UI. Focus and error states are proposed, not observed.

**nav-bar**: Represents the "Shop / Events / Contact / Stores" primary navigation plus the utility row (Log in / Wishlist / Cart) referenced in the page text. Background and ink color are inferred from the site's white-canvas, black-heading convention; no nav-specific selector was captured.

**product-card**: A general book-tile pattern (cover, title, author, price) inferred from the homepage's repeated "Image" carousel items and merchandising rails (New Release, Staff Pick, Signed, Discounted). Card chrome uses a slightly warmer off-white surface than pure canvas to separate it from the page background; this differentiation is proposed.

**hero**: Maps to the homepage's rotating slide carousel ("GO TO SLIDE 1–9"). Typography uses the large serif display size to suggest editorial/literary tone; no hero-specific font-size rule was captured, so sizing is proposed.

**footer**: Corresponds to the "Custom Footer Menu" (About Us, Return Policy, Shipping Policy, Visit Us store list, social links) and legal/utility row. Styled as a light, low-contrast block rather than an inverted dark footer, since no footer background rule was present in the evidence — this is a conservative, unconfirmed choice.

**badge**: Covers the repeated tag labels visible in the page text — SIGNED, STAFF PICK, NEW RELEASE, DISCOUNTED, PREORDER. The soft-yellow highlight color from the observed palette is proposed for these tags; actual production badge coloring (e.g., red for discounts) was not confirmed by a captured selector.

**search**: Reflects the "Search type: Books / Audiobooks / Local Books / Merchandise" filtered search control described in the page content. Field chrome reuses the text-input treatment; the type-filter dropdown's interaction states are not observed.

**event-card**: A category-appropriate component for Books & Books' heavy events programming (author talks, book clubs, RSVP/GET TICKETS actions). The date badge reuses the primary violet fill to give upcoming-event dates visual priority in a list, and the card CTA reuses `button-primary`. This entire pattern is proposed to fit the observed event-listing content, not drawn from a captured event-card selector.

## Responsive Behavior

This is a recommended structure, not measured site behavior — no responsive CSS or breakpoint rules were present in the supplied evidence.

| Breakpoint | Width       | Layout guidance (proposed) |
|-----------|-------------|------------------------------|
| Mobile    | < 640px     | Single-column stacks; nav collapses to a hamburger/off-canvas menu; hero carousel becomes swipe-only. |
| Tablet    | 640–1023px  | 2-column product/event grids; utility nav (login/wishlist/cart) condenses to icons. |
| Desktop   | ≥ 1024px    | Multi-column product rails and event lists; full text nav-bar with visible utility menu. |

Touch targets should be at least 44×44px for cart/RSVP/search buttons. Nav collapse threshold and carousel swipe behavior are suggested defaults, not confirmed against live rendering.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was gathered via static CSS/text extraction; no live rendering, computed styles, or DOM screenshots were reviewed, so layout, spacing rhythm, and component composition are inferred from selector names and page copy only.
- The primary/secondary color roles are ambiguous in the source CSS (buttons alternate between `--color-primary` black and `--color-secondary` violet depending on state and class); this spec's fixed assignment of violet as "primary" is an interpretive choice, not a directly observed convention.
- All typography sizes, weights, and line-heights beyond the confirmed `--font-family: Figtree` variable are proposed scale values, not measured from rendered headings or body text.
- Domine is used here for display type as an inferred literary-brand fit; it was present in the site's loaded font list but its actual applied role (if any) was not confirmed by a captured heading rule.
- No hover/focus/active states, mobile menu behavior, or carousel interaction were observed directly; all such states are proposed and should be validated against the live site before implementation.
- Font licensing/self-hosting terms for Figtree and Domine were not verified as part of this extraction.
