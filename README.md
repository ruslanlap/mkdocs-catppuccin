# MkDocs Catppuccin Theme

<div align="center">

<samp>

Beautiful MkDocs documentation with all 4 Catppuccin flavors

</samp>

[![MkDocs](https://img.shields.io/badge/MkDocs-Material-blue)](https://squidfunk.github.io/mkdocs-material/)
[![Catppuccin](https://img.shields.io/badge/Catppuccin-Theme-pink)](https://github.com/catppuccin/catppuccin)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deploy](https://github.com/ruslanlap/mkdocs-catppuccin/actions/workflows/deploy.yml/badge.svg)](https://github.com/ruslanlap/mkdocs-catppuccin/actions/workflows/deploy.yml)

**[📚 Live Demo](https://ruslanlap.github.io/mkdocs-catppuccin/)** • **[📖 Documentation](https://ruslanlap.github.io/mkdocs-catppuccin/configuration/)** • **[🎨 Catppuccin](https://github.com/catppuccin/catppuccin)**

</div>

---

## Overview

This project provides a complete integration of the **Catppuccin** color palette with **MkDocs Material** theme. Users can seamlessly switch between all 4 Catppuccin flavors directly from the documentation interface.

### Available Flavors

| Flavor | Type | Base Color | Description |
|--------|------|------------|-------------|
| **Latte** 🌅 | Light | `#eff1f5` | Light theme for daytime work |
| **Frappé** 🌆 | Dark | `#303446` | Cool dark theme |
| **Macchiato** 🌃 | Dark | `#24273a` | Warm dark theme |
| **Mocha** 🌌 | Dark | `#1e1e2e` | Warmest dark theme |

## Features

- ✨ **All 4 Catppuccin Flavors** - Complete color palette support
- 🎨 **Seamless Theme Switching** - Toggle between flavors with one click
- 📝 **Optimized Code Highlighting** - Beautiful syntax colors for all languages
- 🎯 **Full Material Integration** - All Material for MkDocs features supported
- 📱 **Responsive Design** - Perfect on desktop, tablet, and mobile
- ♿ **Accessibility** - WCAG AA compliant color contrasts
- 🔍 **Enhanced Search** - Themed search interface
- 📦 **Easy to Use** - Simple copy-paste integration

## Quick Start

### Prerequisites

```bash
pip install mkdocs mkdocs-material
```

### Installation

1. **Clone or download this repository**

```bash
git clone https://github.com/yourusername/mkdocs-catppuccin.git
cd mkdocs-catppuccin
```

2. **Copy the files to your project**

```bash
# Copy the CSS file
cp -r docs/stylesheets your-project/docs/

# Use the mkdocs.yml as reference
```

3. **Update your `mkdocs.yml`**

```yaml
theme:
  name: material
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
```

4. **Serve locally**

```bash
mkdocs serve
```

Visit `http://127.0.0.1:8000` to see your documentation with Catppuccin themes!

## Project Structure

```
mkdocs-catppuccin/
├── docs/
│   ├── stylesheets/
│   │   └── extra.css          # All 4 Catppuccin flavors
│   ├── index.md                # Home page
│   └── configuration.md        # Configuration guide
├── mkdocs.yml                  # MkDocs configuration
└── README.md                   # This file
```

## Documentation

This project includes comprehensive documentation:

- **[🌐 Live Demo](https://ruslanlap.github.io/mkdocs-catppuccin/)** - See all 4 Catppuccin flavors in action!
- **[Home Page](https://ruslanlap.github.io/mkdocs-catppuccin/)** - Overview and examples
- **[Configuration Guide](https://ruslanlap.github.io/mkdocs-catppuccin/configuration/)** - Step-by-step setup instructions

## Screenshots

### Latte (Light Theme)
Bright and clean theme perfect for daytime reading and work.

### Frappé (Dark Theme)
Cool dark theme with balanced contrast for extended coding sessions.

### Macchiato (Dark Theme)
Warm dark theme comfortable for evening use.

### Mocha (Dark Theme)
Deep, cozy dark theme ideal for late-night coding.

## Customization

### Changing Colors

You can customize the primary and accent colors in `docs/stylesheets/extra.css`:

```css
[data-md-color-scheme="mocha"] {
  /* Change primary color to green */
  --md-primary-fg-color: var(--ctp-mocha-green);

  /* Change accent color to teal */
  --md-accent-fg-color: var(--ctp-mocha-teal);
}
```

### Available Colors

Each flavor includes these colors:

- **Backgrounds**: `base`, `mantle`, `crust`
- **Surfaces**: `surface0`, `surface1`, `surface2`
- **Overlays**: `overlay0`, `overlay1`, `overlay2`
- **Text**: `subtext0`, `subtext1`, `text`
- **Colors**: `lavender`, `blue`, `sapphire`, `sky`, `teal`, `green`, `yellow`, `peach`, `maroon`, `red`, `mauve`, `pink`, `flamingo`, `rosewater`

See the [Configuration Guide](docs/configuration.md) for more customization options.

## Deployment

### GitHub Pages

Create `.github/workflows/deploy.yml`:

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
mkdocs build
# Upload the 'site/' directory to your hosting provider
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Theme not applying?
- Check that `extra.css` is in `docs/stylesheets/`
- Verify the path in `mkdocs.yml` is correct
- Clear browser cache with `Ctrl+F5`

### Colors look wrong?
- Ensure `scheme` names match between `mkdocs.yml` and CSS
- Check for CSS syntax errors
- Verify all color variables are defined

### Toggle not working?
- Make sure you have multiple palettes defined
- Check that each palette has a unique `scheme` name
- Verify the `toggle` sections are properly configured

For more help, see the [Configuration Guide](docs/configuration.md).

## Resources

- [Catppuccin Official Website](https://catppuccin.com/)
- [Catppuccin GitHub](https://github.com/catppuccin/catppuccin)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Catppuccin Style Guide](https://github.com/catppuccin/catppuccin/blob/main/docs/style-guide.md)

## Credits

- **[Catppuccin](https://github.com/catppuccin/catppuccin)** - The beautiful color palette
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** - The amazing documentation theme
- **[MkDocs](https://www.mkdocs.org/)** - The static site generator

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Catppuccin is licensed under the MIT License.

---

<div align="center">

**Made with ☕ and Catppuccin**

If you find this useful, consider ⭐ starring the repository!

</div>
