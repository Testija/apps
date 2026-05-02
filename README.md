# Pildikonverter (TIF / TIFF / PSD → JPG)

Konverdib kõik `.tif`, `.tiff` ja `.psd` failid valitud kaustas JPG-formaati:

- Laius **1920 px** (kõrgus skaleeritakse proportsionaalselt)
- Värviruum **RGB**
- JPG kvaliteet **85** (vahepealne 80–90)
- Tulemused salvestatakse alamkausta **`jpg/`**

Algfaile ei muudeta.

---

## Paigaldus Windowsis (üks kord)

1. **Paigalda Python 3.10+** aadressilt <https://www.python.org/downloads/windows/>.
   Installeris märgi linnuke **"Add Python to PATH"**.

2. Ava **Command Prompt** (Win+R → `cmd` → Enter) ja mine selle kausta:
   ```
   cd C:\tee\pildikonverter
   ```

3. Paigalda sõltuvused:
   ```
   pip install -r requirements.txt
   ```

---

## Kasutamine

**Variant A — anna kausta tee argumendina:**
```
python convert.py "C:\Users\Sina\Pildid\toores"
```

**Variant B — käivita ilma argumendita, küsib kausta:**
```
python convert.py
```

**Variant C — lohista kaust skripti peale** (Windows Exploreris).

Tulemused ilmuvad sisendkausta sees `jpg/` alamkausta.

---

## Soovikorral: tee `.exe`

Et skript töötaks ilma Pythoni paigalduseta:

```
pip install pyinstaller
pyinstaller --onefile convert.py
```

Valmis fail: `dist\convert.exe`. Lohista selle peale kaust või jooksuta:
```
convert.exe "C:\tee\pildidele"
```

---

## Sätete muutmine

Ava `convert.py` ja muuda faili algusest:

```python
TARGET_WIDTH = 1920    # piksli laius
JPG_QUALITY  = 85      # 1–100 (soovitatud 80–90)
```
