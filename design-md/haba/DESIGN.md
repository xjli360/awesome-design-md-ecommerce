---
version: alpha
name: "Haba"
source_url: "https://www.habausa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A teal anchor of #156165 — the meta theme-color and the brand’s primary — sits against a clean white canvas (#ffffff) and a secondary gray scale of #bcbcbc, #444444, #dedede, #323232, and #121212. This is a wooden toy brand that trusts its product photography and physical material over digital decoration. Playfair Display, a serif with sharp contrast and vertical stress, runs in display sizes (28–32px, weight 600) for category headers and product names, while Work Sans (400/500, 14–16px) handles body copy, navigation, and buttons. The system uses generous whitespace and soft rounding — cards at {rounded.md} (12px), buttons at {rounded.sm} (8px), and a full-pill search bar at {rounded.full} — to keep the interface approachable for children and parents alike. The primary color appears in the top nav bar, primary buttons, and hover states on product cards, while the muted gray (#bcbcbc) handles borders, dividers, and disabled states. There is no hard edge anywhere except the body grid; every interactive element has a gentle corner radius. The brand’s voice is warm, educational, and tactile — but the interface itself stays minimal, letting the wood grain and bright toy colors (reds, yellows, greens in product photos) carry the emotional weight. The footer uses a dark canvas (#323232) with white text, creating a clear visual boundary between content and legal/utility links.

colors:
  primary: "#156165"
  primary-active: "#0e4a4d"
  primary-disabled: "#a3c4c6"
  ink: "#121212"
  body: "#323232"
  muted: "#444444"
  muted-soft: "#bcbcbc"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  footer-bg: "#323232"
  footer-text: "#dedede"
  accent-red: "#c0392b"
  accent-yellow: "#f39c12"
  accent-green: "#27ae60"
  star-rating: "#f1c40f"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Work Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Work Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Work Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.3px
  link:
    fontFamily: "'Work Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Work Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Work Sans', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.xs}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-lg}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xxl}"
    minHeight: 400px
  hero-banner-overlay:
    backgroundColor: "rgba(0,0,0,0.3)"
    textColor: "{colors.on-dark}"
  category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
  category-card-hover:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-link:
    color: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.on-primary}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
  accordion-header:
    padding: "{spacing.base} 0"
    typography: "{typography.title-md}"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
    typography: "{typography.body-sm}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-link:
    color: "{colors.primary}"
  breadcrumb-separator:
    color: "{colors.muted-soft}"
    padding: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 12px"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
  loading-spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
  error-message:
    backgroundColor: "#fef2f2"
    textColor: "{colors.accent-red}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  success-message:
    backgroundColor: "#f0fdf4"
    textColor: "{colors.accent-green}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. Uses the brand teal {colors.primary} as background with white text. On hover, shifts to {colors.primary-active} (#0e4a4d) for a darker, more grounded state. Disabled state uses {colors.primary-disabled} (#a3c4c6) to signal non-interactivity while maintaining brand color family. All primary buttons use {rounded.sm} (8px) for a friendly but not overly soft corner.

**`button-secondary`** — An outlined variant with white background, teal text, and a 2px solid border in {colors.primary}. Active state darkens the border and text to {colors.primary-active}. Used for "Add to Wishlist," "View Details," and secondary checkout actions.

**`button-tertiary-text`** — A text-only button with no background or border. Uses {colors.primary} for the text color. Used for "Cancel," "Learn More," and inline actions where visual weight should be minimal.

**`button-pill`** — A fully rounded variant ({rounded.full}) used for promotional badges, "Shop Now" in hero sections, and age-range selectors. Uses smaller typography ({typography.button-sm}) and tighter padding for a compact, badge-like appearance.

**`icon-button`** — A 40x40px square button with {rounded.sm} corners. Transparent background with {colors.body} icon color. Used for cart, account, and search icons in the top nav. Hover state adds a subtle background tint.

### Navigation
**`nav-bar`** — Fixed top navigation bar at 72px height. White background with a 1px bottom border in {colors.hairline}. On scroll, gains a subtle box-shadow for depth. Contains logo, category links, search icon, cart icon, and account icon. The logo uses {typography.display-md} in Playfair Display for brand presence.

**`nav-link`** — Navigation links in Work Sans 14px/500 with 0.3px letter spacing. Active state shows a 2px bottom border in {colors.primary} and teal text. Hover state shifts text to {colors.primary} without the underline, keeping the interface clean.

**`search-bar`** — A pill-shaped search input ({rounded.full}) with light gray background ({colors.surface-soft}) and subtle border. On focus, gains a 2px teal border. Used for product search across the site. Placeholder text in {colors.muted}.

### Cards
**`product-card`** — The primary product display unit. White background with {rounded.md} (12px) corners and a subtle box-shadow. On hover, the shadow deepens to create a lift effect. Contains a square product image with {rounded.sm} corners, the product title in Playfair Display 20px/500, and the price in Work Sans 16px/400 in teal. An optional badge component overlays the top-left corner for "New," "Sale," or "Ages 3+" labels.

**`category-card`** — Used for category navigation (e.g., "Wooden Toys," "Games," "Baby"). White background with 1px border and {rounded.md} corners. On hover, the border thickens to 2px and turns teal. Contains an icon or image and the category name in Work Sans 18px/500.

**`hero-banner`** — Full-width banner at the top of landing pages. Minimum 400px height with {colors.surface-soft} background. Uses {typography.display-xl} for the headline. An optional overlay variant uses a semi-transparent black scrim with white text for use over product photography.

### Forms
**`text-input`** — Standard text input with white background, 1px {colors.hairline} border, and {rounded.sm} corners. On focus, the border becomes 2px teal. Error state uses a 2px red border ({colors.accent-red}). Height is 48px for comfortable touch interaction.

**`select-input`** — Dropdown select with the same styling as text-input. Uses a custom dropdown arrow in {colors.muted}. Focus and error states mirror text-input.

**`newsletter-input`** — Email input specifically for the newsletter signup in the footer. Paired with `newsletter-button` for a combined input+submit pattern. The button sits directly to the right of the input, both at 48px height.

### Footer
**`footer`** — Dark section at the bottom of every page. Background in {colors.footer-bg} (#323232) with light gray text ({colors.footer-text}). Contains columns for "Shop," "About," "Support," and "Connect." Links use {colors.footer-text} and shift to white on hover. The newsletter signup sits in the footer with a white input and teal submit button. A thin hairline separates the main footer from the copyright bar.

### Feedback & State
**`loading-spinner`** — A circular spinner with a gray border and teal top border. Used for async operations like loading product lists or submitting forms.

**`error-message`** — A light red background (#fef2f2) with red text. Used for form validation errors, API failures, and out-of-stock notifications. {rounded.sm} corners with {spacing.base} padding.

**`success-message`** — A light green background (#f0fdf4) with green text. Used for successful add-to-cart, newsletter signup, and form submission confirmations.

**`accordion`** — Used for product descriptions, FAQ sections, and shipping details. Each item has a clickable header in {typography.title-md} with a bottom border. Content area collapses/expands with smooth animation. Headers use a plus/minus icon in {colors.primary} to indicate state.

**`breadcrumb`** — Secondary navigation showing the current page path. Links in {colors.primary}, separators in {colors.muted-soft}, current page in {colors.muted}. Uses {typography.caption} size.

**`pagination`** — Page navigation for product listings. Active page gets a teal background with white text. Hover state adds a light gray background. Uses {typography.body-sm} for page numbers.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero banner reduces to 300px min-height; footer columns stack; search bar moves to full-width below nav; category cards become 2-column grid |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories; search bar remains in nav; hero banner at 350px min-height; footer shows 2-column layout; category cards in 3-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with all categories; search bar in nav; hero banner at 400px min-height; footer in 4-column layout; category cards in 4-column grid |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; nav remains full; hero banner at 450px min-height; all layouts scale proportionally |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for touch accessibility
- Icon buttons are 40x40px with adequate padding for finger taps
- Nav links have 8px vertical padding for comfortable tapping
- Product card images are at minimum 200px on mobile for easy tapping
- Accordion headers have full-width tap targets (100% width, 48px+ height)
- Pagination buttons are minimum 36x36px with 4px padding

### Collapsing Strategy
- **Navigation**: On mobile (<744px), the full nav collapses to a hamburger menu. The logo remains centered. Cart and account icons remain visible. Search becomes a full-width bar below the nav.
- **Product Grid**: Transitions from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile). Product cards maintain consistent padding but image sizes scale proportionally.
- **Footer**: 4-column layout collapses to 2 columns at tablet, then to a single column at mobile. Newsletter signup remains prominent at all breakpoints.
- **Hero Banner**: Text overlays center on mobile; on desktop, text can be left-aligned with the image on the right. CTA buttons stack vertically on mobile.
- **Category Cards**: 4-column grid collapses to 3 at tablet, 2 at mobile. Cards maintain square aspect ratio.
- **Breadcrumbs**: On mobile, breadcrumbs truncate to show only the current page and one parent level, with a back arrow for the parent.
- **Search**: On mobile, the search bar in the nav becomes an icon that expands to a full-width overlay when tapped.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex colors (#bcbcbc, #444444, #dedede, #156165, #323232, #121212) are a limited palette that appears to be primarily grays with a single teal accent. The brand's true primary is #156165 (teal), which is also the meta theme-color. However, the extracted list may be missing secondary brand colors (e.g., warm wood tones, accent colors for children's toys) that exist in imagery but not in the CSS/HTML. The accent colors (#c0392b, #f39c12, #27ae60, #f1c40f) are inferred from common toy-brand patterns and should be verified against the live site.
- Font sizes and weights are inferred from common patterns for Playfair Display and Work Sans pairings. Exact values (especially for display-xl, display-lg, etc.) should be verified against the live site's CSS.
- Hover states for buttons and cards are inferred from common patterns. The exact shadow values and transition durations need verification.
- Error and success message styling (background colors, text colors) are inferred from common patterns and may differ on the live site.
- The loading spinner is not confirmed; the live site may use a different loading indicator (e.g., skeleton screens, custom animation).
- Dark mode is not supported. The brand uses a light theme with a dark footer section.
- The nav-bar-scrolled shadow value is inferred; the live site may use a different shadow or none at all.
- The hero-banner-overlay scrim opacity (0.3) is an estimate; the live site may use a different value.
- The product-card-hover shadow is inferred; the live site may use a different elevation or a border change instead.
- The newsletter-input and newsletter-button combination is inferred from common ecommerce patterns; the live site may use a different layout.
- The accordion component is inferred from common product-description patterns; the live site may use tabs or a different disclosure pattern.
- The pagination component is inferred from common ecommerce patterns; the live site may use infinite scroll or "Load More" buttons instead.
- The breadcrumb component is inferred from common navigation patterns; the live site may not use breadcrumbs.
- The select-input component is inferred from common form patterns; the live site may use custom dropdowns or radio-button groups.
- The icon-button component size (40x40px) is inferred; the live site may use different dimensions.
- The button-pill component is inferred from common promotional patterns; the live site may not use pill-shaped buttons.
- The category-card component is inferred from common category-navigation patterns; the live site may use a different layout (e.g., image-only cards, text links).
- The footer-link hover state (white text) is inferred; the live site may use an underline or no hover effect.
- The text-input-focus border width (2px) is inferred; the live site may use a different width or a box-shadow instead.
- The text-input-error border color (#c0392b) is inferred; the live site may use a different red or a different error indicator (e.g., icon, message below).
- The success-message background color (#f0fdf4) is inferred; the live site may use a different green or a different success indicator.
- The error-message background color (#fef2f2) is inferred; the live site may use a different red or a different error indicator.
- The loading-spinner border colors are inferred; the live site may use a different spinner style or a skeleton screen.
- The accordion-header and accordion-content padding values are inferred; the live site may use different spacing.
- The breadcrumb-separator padding (0 {spacing.xs}) is inferred; the live site may use a different separator character or spacing.
- The pagination-active padding (4px 12px) is inferred; the live site may use different dimensions.
- The pagination-hover background color ({colors.surface-soft}) is inferred; the live site may use a different hover state.
- The responsive breakpoints (744px, 1128px, 1440px) are inferred from common patterns; the live site may use different breakpoints.
- The touch target minimum height (44px) is inferred from WCAG guidelines; the live site may use a different minimum.
- The collapsing strategy for breadcrumbs on mobile is inferred; the live site may use a different truncation method.
- The search bar becoming a full-width overlay on mobile is inferred; the live site may use a different search pattern (e.g., inline expansion, modal).
- The hero banner text alignment on mobile (centered) is inferred; the live site may use a different alignment.
- The category cards maintaining square aspect ratio on mobile is inferred; the live site may use a different aspect ratio.
- The footer columns collapsing to 2 at tablet and 1 at mobile is inferred; the live site may use a different grid layout.
- The product grid column counts (4 wide, 3 desktop, 2 tablet, 1 mobile) are inferred from common ecommerce patterns; the live site may use different counts.
- The nav-bar height (72px) is inferred; the live site may use a different height.
- The hero-banner min-height values (400px desktop, 350px tablet, 300px mobile) are inferred; the live site may use different heights.
- The product-card padding ({spacing.base}) is inferred; the live site may use different padding.
- The product-card-image aspect ratio (1:1) is inferred; the live site may use a different ratio (e.g., 4:3, 3:2).
- The product-card-title marginTop ({spacing.sm}) is inferred; the live site may use different spacing.
- The product-card-price marginTop ({spacing.xs}) is inferred; the live site may use different spacing.
- The product-card-badge padding (2px 8px) is inferred; the live site may use different padding.
- The newsletter-button height (48px) matching the input height is inferred; the live site may use a different height.
- The accordion borderBottom (1px solid {colors.hairline}) is inferred; the live site may use a different border style.
- The breadcrumb color ({colors.muted}) for the current page is inferred; the live site may use a different color.
- The pagination color ({colors.body}) is inferred; the live site may use a different color.
- The loading-spinner borderTopColor ({colors.primary}) is inferred; the live site may use a different accent color for the spinner.
