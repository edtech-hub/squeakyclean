# Sources (every element and where it comes from)

| Element | Source | Changes |
|---|---|---|
| Tokens: spacing 20-80, content 680 / wide 1240, pill buttons | Twenty Twenty-Five `theme.json` | Dark palette from TT25 "Evening" style variation, tinted to the logo's steel blue; brass action color from the logo's badge |
| Fonts: Literata + Ysabeau Office | TT25 bundled font collection (`assets/fonts`) | Served from Google Fonts for the prototype |
| Block CSS | `@wordpress/block-library` 11.2.0 (`assets/css/wp-blocks.css`) | Untouched |
| Header | TT25 `header.php` pattern (site logo, navigation, button) | Phone number added |
| Hero | Core Cover block (`wp-block-cover`, `__image-background`, `has-background-dim-80`) + Columns | Directional dim for text contrast |
| Estimate form | Gravity Forms markup (`gform_wrapper`, `gfield`, validation banner and messages) | Service radios as selectable cards |
| Annotation pills | TT25 `is-style-text-annotation` | |
| Trust row | TT25 `services-3-col` layout (4 columns) | Custom line drawings instead of icons |
| Services | TT25 `services-3-col` | Arched panes taken from the logo's arched window |
| Guarantee band | Core Cover block | Flat color (old site photos too small) |
| Steps | TT25 `cta-centered-heading` + columns | Numbered |
| Commercial statement | TT24 `text-centered-statement` | Buttons added |
| Review slot | TT25 `testimonials-large` | Empty placeholder, no invented review |
| FAQ | TT25 `text-faqs` (core Details block) | Two columns, `::details-content` open animation |
| Footer | TT25 `footer-columns` | |
| Motion | WP View Transitions plugin (`@view-transition`), WP 6.8 Speculative Loading, core-style fade-ins | |
| Photo | Client's old site (`wp-content/uploads/2020/08/banner_bg1.jpg`, via Wayback) | WebP |
| Logo | Client's old site (`header_logo.jpg`) | Converted to a light version for the dark theme |
