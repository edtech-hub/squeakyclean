# Sources (every element and where it comes from)

| Element | Source | Changes |
|---|---|---|
| Tokens: spacing 20-80, content 680 / wide 1240, pill buttons | Twenty Twenty-Five `theme.json` | Dark palette from TT25 "Evening" style variation, tinted to the logo's steel blue; brass action color from the logo's badge |
| Fonts: Jost (headings, 200-400) + Instrument Sans (body) | Twenty Twenty-Four bundled fonts (`assets/fonts/jost`, `instrument-sans`) | Served from Google Fonts for the prototype |
| Block CSS | `@wordpress/block-library` 11.2.0 (`assets/css/wp-blocks.css`) | Untouched |
| Header | TT25 `header.php` pattern; core Navigation block markup (`wp-block-navigation__container`, `wp-block-navigation-item`, `has-child`, `submenu__toggle`) | Phone number added |
| Services mega menu | Core Navigation submenu (hover + toggle button), laid out as the TT25 `services-3-col` cards | Five service cards, "All services" link |
| Page banners | TT25 page header pattern (`page-header` style: annotation, title, lede) | Jump links on Services |
| Service rows | Core Media & Text block, alternating (`has-media-on-the-right`) | Arched illustration panel instead of photo |
| Contact page | Gravity Forms single page + sidebar widgets (classic widget area) | |
| Card-to-page morph | WordPress View Transitions plugin (featured image morph between Query Loop card and single page) | Service card arch morphs into its Services row |
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
