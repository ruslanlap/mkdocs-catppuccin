# Configuration Guide: Catppuccin for MkDocs!!!!!

This guide will help you integrate all 4 Catppuccin flavors into your own MkDocs project.

## Prerequisites

Before you begin, make sure you have the following installed:

```bash
pip install mkdocs
pip install mkdocs-material
python3 -m venv .venv
source .venv/bin/activate
mkdocs serve --livereload
```

## Step 1: Project Structure

Create the following structure in your project:

```
your-project/
├── docs/
│   ├── stylesheets/
│   │   └── extra.css
│   ├── index.md
│   └── ... (other documentation files)
├── mkdocs.yml
└── README.md
```

## Step 2: Create the CSS File with Catppuccin Themes

Create the file `docs/stylesheets/extra.css` and add all 4 Catppuccin flavors.

### CSS File Structure

The CSS file should contain:

1. **Color Palette Definitions** - all 4 flavors
2. **Configuration for Each Flavor** - Material theme variable settings
3. **Common Styling** - styles applied to all themes

### Example Palette Definition

```css
/* Catppuccin Latte (Light Theme) */
:root {
  --ctp-latte-base: #eff1f5;
  --ctp-latte-mantle: #e6e9ef;
  --ctp-latte-crust: #dce0e8;
  --ctp-latte-text: #4c4f69;
  --ctp-latte-mauve: #8839ef;
  --ctp-latte-blue: #1e66f5;
  /* ... other colors */
}
```

### Applying Colors to Material Theme

```css
[data-md-color-scheme="latte"] {
  --md-default-bg-color: var(--ctp-latte-base);
  --md-default-fg-color: var(--ctp-latte-text);
  --md-primary-fg-color: var(--ctp-latte-mauve);
  --md-accent-fg-color: var(--ctp-latte-blue);
  /* ... other variables */
}
```

!!! tip "Complete CSS File"
    The complete example CSS file with all 4 flavors is located in the `docs/stylesheets/extra.css` file of this repository.

## Step 3: Configure mkdocs.yml

Edit your `mkdocs.yml` file:

### Basic Configuration

```yaml
site_name: Your Documentation
site_description: Description of your project
site_url: https://yourdomain.com
repo_url: https://github.com/username/repo
repo_name: username/repo

theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.footer
    - navigation.top
    - navigation.tracking
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.code.annotate
```

### Palette Configuration with All 4 Flavors

```yaml
theme:
  palette:
    # Catppuccin Latte (Light theme)
    - scheme: latte
      primary: custom
      accent: custom
      toggle:
        icon: material/weather-sunny
        name: Switch to Frappé

    # Catppuccin Frappé (Dark theme)
    - scheme: frappe
      primary: custom
      accent: custom
      toggle:
        icon: material/weather-night
        name: Switch to Macchiato

    # Catppuccin Macchiato (Dark theme)
    - scheme: macchiato
      primary: custom
      accent: custom
      toggle:
        icon: material/weather-partly-cloudy
        name: Switch to Mocha

    # Catppuccin Mocha (Dark theme)
    - scheme: mocha
      primary: custom
      accent: custom
      toggle:
        icon: material/weather-cloudy
        name: Switch to Latte
```

!!! info "Why 'custom' for primary and accent?"
    Setting `primary: custom` and `accent: custom` tells Material for MkDocs to use the CSS variables we define in `extra.css` instead of the built-in color schemes.

### Including the CSS File

```yaml
extra_css:
  - stylesheets/extra.css
```

### Useful Markdown Extensions

```yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
      linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.tabbed:
      alternate_style: true
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true
```

## Step 4: Complete mkdocs.yml Structure

Here's a complete example configuration file:

```yaml
site_name: My Documentation
site_description: Documentation with Catppuccin theme
site_url: https://example.com
repo_url: https://github.com/username/repo
repo_name: username/repo

theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.footer
    - navigation.top
    - navigation.tracking
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.code.annotate

  palette:
    - scheme: latte
      primary: custom
      accent: custom
      toggle:
        icon: material/weather-sunny
        name: Switch to Frappé

    - scheme: frappe
      primary: custom
      accent: custom
      toggle:
        icon: material/weather-night
        name: Switch to Macchiato

    - scheme: macchiato
      primary: custom
      accent: custom
      toggle:
        icon: material/weather-partly-cloudy
        name: Switch to Mocha

    - scheme: mocha
      primary: custom
      accent: custom
      toggle:
        icon: material/weather-cloudy
        name: Switch to Latte

extra_css:
  - stylesheets/extra.css

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
      linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.tabbed:
      alternate_style: true
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true

nav:
  - Home: index.md
  - Configuration: configuration.md

copyright: Copyright &copy; 2025 Your Name

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/username/repo
```

## Step 5: Run and Test

### Local Development

Start the local server for preview:

```bash
mkdocs serve
```

Open your browser at `http://127.0.0.1:8000/`

### Check Themes

1. Find the theme toggle icon in the top right corner
2. Click it to switch between themes
3. Verify that all 4 flavors display correctly

!!! tip "Browser Cache"
    If styles don't update, clear your browser cache with `Ctrl+F5` (or `Cmd+Shift+R` on Mac).

## Step 6: Deploy

### GitHub Pages

Add a GitHub Action for automatic deployment:

Create the file `.github/workflows/deploy.yml`:

```yaml
name: Deploy MkDocs

on:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```

### Other Platforms

```bash
# Build static files
mkdocs build

# Files will be in the site/ directory
# Upload them to your hosting provider
```

## Customizing Colors

### Changing the Accent Color

If you want to change the primary or accent color for a specific flavor, edit the variables in `extra.css`:

```css
[data-md-color-scheme="mocha"] {
  /* Use green instead of mauve as primary color */
  --md-primary-fg-color: var(--ctp-mocha-green);

  /* Use teal instead of blue as accent color */
  --md-accent-fg-color: var(--ctp-mocha-teal);
}
```

### Available Catppuccin Colors

Each flavor has the following colors:

| Category | Colors |
|----------|--------|
| Backgrounds | `base`, `mantle`, `crust` |
| Surfaces | `surface0`, `surface1`, `surface2` |
| Overlays | `overlay0`, `overlay1`, `overlay2` |
| Text | `subtext0`, `subtext1`, `text` |
| Blues | `lavender`, `blue`, `sapphire`, `sky` |
| Greens | `teal`, `green` |
| Yellows | `yellow`, `peach` |
| Reds | `maroon`, `red` |
| Purples/Pinks | `mauve`, `pink` |
| Pastels | `flamingo`, `rosewater` |

### Color Examples by Flavor

=== "Latte"

    ```css
    /* Example: Latte with green accent */
    [data-md-color-scheme="latte"] {
      --md-primary-fg-color: var(--ctp-latte-green);
      --md-accent-fg-color: var(--ctp-latte-teal);
    }
    ```

=== "Frappé"

    ```css
    /* Example: Frappé with pink accent */
    [data-md-color-scheme="frappe"] {
      --md-primary-fg-color: var(--ctp-frappe-pink);
      --md-accent-fg-color: var(--ctp-frappe-mauve);
    }
    ```

=== "Macchiato"

    ```css
    /* Example: Macchiato with peach accent */
    [data-md-color-scheme="macchiato"] {
      --md-primary-fg-color: var(--ctp-macchiato-peach);
      --md-accent-fg-color: var(--ctp-macchiato-yellow);
    }
    ```

=== "Mocha"

    ```css
    /* Example: Mocha with sapphire accent */
    [data-md-color-scheme="mocha"] {
      --md-primary-fg-color: var(--ctp-mocha-sapphire);
      --md-accent-fg-color: var(--ctp-mocha-sky);
    }
    ```

## Advanced Customization

### Adding Custom Styles

You can add your own styles after the Catppuccin styles in `extra.css`:

```css
/* Custom styles */
.md-header__title {
  font-weight: bold;
  font-size: 1.2rem;
}

.md-content h1 {
  color: var(--md-accent-fg-color);
  border-bottom: 2px solid var(--md-accent-fg-color);
  padding-bottom: 0.5rem;
}

/* Custom card style */
.custom-card {
  background-color: var(--md-code-bg-color);
  border: 1px solid var(--md-code-hl-color);
  border-radius: 0.5rem;
  padding: 1rem;
  margin: 1rem 0;
}
```

### Configuring Navigation

In `mkdocs.yml`, you can customize the navigation structure:

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Installation: getting-started/installation.md
    - Quick Start: getting-started/quickstart.md
  - Guides:
    - Basic Concepts: guides/basics.md
    - Advanced Topics: guides/advanced.md
  - API Reference: api/index.md
  - Configuration: configuration.md
```

### Custom Logo and Favicon

Add a logo and favicon to your theme:

```yaml
theme:
  name: material
  logo: assets/logo.png
  favicon: assets/favicon.png
```

Place your logo and favicon files in `docs/assets/`.

## Common Issues

### Theme Not Applying

1. Verify the path to `extra.css` is correct in `mkdocs.yml`
2. Check that the `extra.css` file is in `docs/stylesheets/`
3. Clear browser cache (Ctrl+F5 or Cmd+Shift+R)
4. Check browser console for CSS loading errors

### Colors Look Wrong

1. Verify that `scheme` in `mkdocs.yml` matches `data-md-color-scheme` in CSS
2. Ensure all CSS variables are properly defined
3. Check for CSS syntax errors (missing semicolons, brackets, etc.)
4. Verify the color hex codes are correct

### Theme Toggle Not Working

1. Make sure you have defined multiple palettes in `mkdocs.yml`
2. Check that the `toggle` sections are properly configured
3. Verify each palette has a unique `scheme` name
4. Ensure JavaScript is enabled in your browser

### Build Errors

```bash
# Common error: Module not found
pip install --upgrade mkdocs-material

# Clear build cache
rm -rf site/
mkdocs build

# Validate mkdocs.yml syntax
python -m yaml mkdocs.yml
```

## Performance Optimization

### Reducing CSS Size

If you only need specific flavors, remove unused ones from `extra.css`:

```css
/* Keep only Mocha and Latte */
/* Remove Frappé and Macchiato sections */
```

### Caching

Enable caching in your web server for static files:

```nginx
# Nginx example
location ~* \.(css|js|png|jpg|jpeg|gif|ico)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

## Accessibility

Catppuccin themes are designed with accessibility in mind:

- **WCAG AA Compliant**: All themes meet WCAG 2.1 AA standards
- **High Contrast**: Sufficient contrast ratios for readability
- **Color Blind Friendly**: Tested with various color vision deficiencies

## Migration Guide

### From Default Material Theme

1. Install Catppuccin CSS file
2. Update `mkdocs.yml` palette configuration
3. Change `primary` and `accent` to `custom`
4. Test all 4 flavors

### From Other Themes

1. Remove old theme configuration
2. Follow the installation steps in this guide
3. Update any custom CSS to use Catppuccin variables
4. Test thoroughly

## Best Practices

### Theme Selection

- **Latte**: Use for documentation that may be printed
- **Frappé**: Good default dark theme
- **Macchiato**: Popular choice for developer docs
- **Mocha**: Best for late-night coding sessions

### Color Usage

- Use primary color for navigation and headers
- Use accent color for links and interactive elements
- Use background colors for cards and containers
- Maintain consistency across pages

### Typography

```yaml
theme:
  font:
    text: Roboto
    code: Roboto Mono
```

## Useful Resources

- [Catppuccin Official Site](https://catppuccin.com/)
- [Catppuccin Style Guide](https://github.com/catppuccin/catppuccin/blob/main/docs/style-guide.md)
- [Material for MkDocs Documentation](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs User Guide](https://www.mkdocs.org/user-guide/)
- [Catppuccin Color Palette](https://github.com/catppuccin/catppuccin#-palette)
- [Material Icons](https://materialdesignicons.com/)

## Community and Support

If you encounter issues:

1. Check [Catppuccin Issues](https://github.com/catppuccin/catppuccin/issues)
2. Review [Material for MkDocs Discussions](https://github.com/squidfunk/mkdocs-material/discussions)
3. Join the [Catppuccin Discord](https://discord.gg/catppuccin)
4. Create an issue in your repository with details

## Contributing

Contributions are welcome! If you improve the theme integration:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

**Enjoy beautiful documentation with Catppuccin! ☕**
