{
  "title": "Pildikonverter (TIF / TIFF / PSD → JPG)",
  "description": "Converts all .tif, .tiff, and .psd files in the selected folder to JPG format.",
  "conversion": {
    "width": "1920 px (height is scaled proportionally)",
    "colorSpace": "RGB",
    "jpgQuality": "85 (mid-range 80–90)",
    "outputFolder": "jpg/",
    "originalFiles": "Original files are not modified."
  },
  "installation": {
    "platform": "Windows",
    "steps": [
      {
        "step": 1,
        "text": "Install Python 3.10+ from https://www.python.org/downloads/windows/. During installation, check \"Add Python to PATH\"."
      },
      {
        "step": 2,
        "text": "Open Command Prompt (Win+R → cmd → Enter) and navigate to the folder:",
        "command": "cd C:\\path\\image-converter"
      },
      {
        "step": 3,
        "text": "Install dependencies:",
        "command": "pip install -r requirements.txt"
      }
    ]
  },
  "usage": {
    "optionA": {
      "description": "Provide the folder path as an argument:",
      "command": "python convert.py \"C:\\Users\\You\\Pictures\\raw\""
    },
    "optionB": {
      "description": "Run without arguments, it will prompt for a folder:",
      "command": "python convert.py"
    },
    "optionC": {
      "description": "Drag and drop a folder onto the script (in Windows Explorer)."
    },
    "result": "The results will appear in the jpg/ subfolder inside the input folder."
  },
  "optionalExe": {
    "description": "To run the script without installing Python:",
    "commands": [
      "pip install pyinstaller",
      "pyinstaller --onefile convert.py"
    ],
    "output": "dist\\convert.exe",
    "runExample": "convert.exe \"C:\\path\\to\\images\""
  },
  "settings": {
    "file": "convert.py",
    "variables": {
      "TARGET_WIDTH": "1920  # pixel width",
      "JPG_QUALITY": "85  # 1–100 (recommended 80–90)"
    }
  }
}
