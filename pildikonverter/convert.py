# Image Converter (TIF / TIFF / PSD → JPG)

A simple image conversion tool that converts all `.tif`, `.tiff`, and `.psd` files in a selected folder to JPG format.

The conversion is designed for consistent output size and quality while preserving the original files.

## Conversion details

- Output image width is **1920 px**  
  (height is scaled proportionally)
- Color space is converted to **RGB**
- JPG quality is set to **85**  
  (recommended mid-range between 80–90)
- Converted images are saved to a **`jpg/`** subfolder
- Original source files are **not modified**

---

## Installation on Windows (one-time setup)

1. **Install Python 3.10 or newer** from:  
   <https://www.python.org/downloads/windows/>

   During installation, make sure to enable the option  
   **“Add Python to PATH”**.

2. Open **Command Prompt**  
   (Win+R → `cmd` → Enter) and navigate to the project folder:
