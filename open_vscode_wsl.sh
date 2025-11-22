#!/bin/bash

# Script to properly open VSCode in WSL mode
# This ensures file watching works correctly

echo "🔧 Opening VSCode in WSL mode..."
echo "📁 Project: /home/ubuntuvm/Projects/mkdocs-catppuccin"
echo ""
echo "Make sure you have 'Remote - WSL' extension installed in VSCode"
echo ""

# Open VSCode in WSL mode
code /home/ubuntuvm/Projects/mkdocs-catppuccin

echo "✅ VSCode should open in WSL mode"
echo "💡 Check the bottom-left corner of VSCode - it should say 'WSL: Ubuntu'"
