# MkDocs with Catppuccin Theme

Welcome to the MkDocs documentation with full support for all 4 Catppuccin flavors!

## Overview

This project demonstrates how to integrate the beautiful Catppuccin color palette into your MkDocs documentation. You get access to all 4 official flavors:

- **Latte** 🌅 - Light theme for daytime work
- **Frappé** 🌆 - Cool dark theme
- **Macchiato** 🌃 - Warm dark theme
- **Mocha** 🌌 - Warmest dark theme

## Features

### 🎨 All 4 Catppuccin Flavors
Users can easily switch between all four themes using the toggle button in the header.

### 🎯 Full Integration with Material for MkDocs
- Support for all Material theme components
- Optimized colors for code syntax highlighting
- Beautiful tables and admonitions
- Smooth transitions between themes

### 📝 Code Syntax Support
All themes include optimized syntax highlighting for various programming languages.

### 🔍 Enhanced Search
Integrated search with support for all Catppuccin themes.

## Quick Start

Check out the [Configuration Guide](configuration.md) for detailed instructions on integrating Catppuccin into your project.

## Examples

### Code Blocks

```python
def hello_catppuccin():
    """Example function with Catppuccin highlighting"""
    colors = {
        "latte": "#eff1f5",
        "frappe": "#303446",
        "macchiato": "#24273a",
        "mocha": "#1e1e2e"
    }
    return colors

# Test the function
flavors = hello_catppuccin()
print(f"Available flavors: {', '.join(flavors.keys())}")
```

```javascript
// JavaScript with beautiful highlighting
const catppuccinFlavors = ['latte', 'frappe', 'macchiato', 'mocha'];

function switchTheme(flavor) {
    if (catppuccinFlavors.includes(flavor)) {
        document.documentElement.setAttribute('data-md-color-scheme', flavor);
        localStorage.setItem('theme', flavor);
    }
}

// Apply saved theme
const savedTheme = localStorage.getItem('theme') || 'mocha';
switchTheme(savedTheme);
```

```typescript
// TypeScript example
interface CatppuccinTheme {
    name: string;
    type: 'light' | 'dark';
    colors: {
        base: string;
        text: string;
        primary: string;
        accent: string;
    };
}

const mochaTheme: CatppuccinTheme = {
    name: 'mocha',
    type: 'dark',
    colors: {
        base: '#1e1e2e',
        text: '#cdd6f4',
        primary: '#cba6f7',
        accent: '#89b4fa'
    }
};
```

### Admonitions

!!! note "Note"
    This is an example of an admonition with the Catppuccin theme. It looks great in all 4 flavors!

!!! tip "Pro Tip"
    Try switching the theme using the button in the header to see all the variations!

!!! warning "Important"
    Make sure you correctly configure the paths to CSS files in your `mkdocs.yml`.

!!! info "Information"
    Catppuccin is a cozy pastel theme available for a wide variety of applications and developer tools.

!!! success "Success"
    You've successfully configured Catppuccin for your MkDocs project!

!!! danger "Danger"
    Modifying core CSS variables may break the theme consistency.

### Tables

| Flavor | Type | Base Color | Best For |
|--------|------|------------|----------|
| Latte | Light | `#eff1f5` | Daytime reading |
| Frappé | Dark | `#303446` | Low-light environments |
| Macchiato | Dark | `#24273a` | Evening work |
| Mocha | Dark | `#1e1e2e` | Night owls |

### Lists

#### Features of each flavor:

**Latte** (Light Theme)
- High contrast for bright environments
- Easy on the eyes in daylight
- Professional appearance
- Perfect for printing

**Frappé** (Cool Dark)
- Balanced contrast
- Cooler color temperature
- Great for extended coding sessions
- Reduces eye strain

**Macchiato** (Warm Dark)
- Warmer color palette
- Comfortable for evening use
- Pleasant visual experience
- Good for creative work

**Mocha** (Warmest Dark)
- Deepest blacks
- Highest contrast in dark themes
- Ideal for late-night coding
- Minimal blue light

## Color Palette Reference

### Available Colors

Each flavor includes these color tokens:

| Token | Purpose |
|-------|---------|
| `base`, `mantle`, `crust` | Background colors |
| `surface0`, `surface1`, `surface2` | Surface layers |
| `overlay0`, `overlay1`, `overlay2` | Overlay elements |
| `subtext0`, `subtext1` | Secondary text |
| `text` | Primary text |
| `lavender`, `blue`, `sapphire`, `sky` | Blue shades |
| `teal`, `green` | Green shades |
| `yellow`, `peach` | Yellow/orange shades |
| `maroon`, `red` | Red shades |
| `mauve`, `pink` | Purple/pink shades |
| `flamingo`, `rosewater` | Pastel shades |

## About Catppuccin

[Catppuccin](https://github.com/catppuccin/catppuccin) is a community-driven pastel theme that aims to be the middle ground between low and high contrast themes. It provides soothing pastel colors with excellent readability.

## Resources

- [Official Catppuccin Website](https://catppuccin.com/)
- [Catppuccin GitHub Repository](https://github.com/catppuccin/catppuccin)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Catppuccin Style Guide](https://github.com/catppuccin/catppuccin/blob/main/docs/style-guide.md)

## License

This theme integration is released under the MIT License. Catppuccin itself is licensed under the MIT License.
