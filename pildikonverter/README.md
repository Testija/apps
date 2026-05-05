# Image Converter (TIF / TIFF / PSD → JPG)

A simple command-line tool for converting `.tif`, `.tiff`, and `.psd` files in a selected folder to JPG format.

## Features

- Image width set to **1920 px** (height is scaled proportionally)
- **RGB** color space
- JPG quality **85** (recommended range 80–90)
- Converted files are saved to a **`jpg/`** subfolder
- Original files are **not modified**

---

## Installation (Windows, one-time setup)

1. Download and install **Python 3.10+** from:  
   https://www.python.org/downloads/windows/  
   ✅ Make sure to check **“Add Python to PATH”** during installation.

2. Open **Command Prompt** (Win+R → `cmd`) and navigate to the project folder:
   ```cmd
   cd C:\path\image-converter
