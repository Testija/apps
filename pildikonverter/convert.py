"""
Pildikonverter: TIF/TIFF/PSD -> JPG
- Laius 1920 px (proportsioonid säilivad)
- RGB värviruum
- JPG kvaliteet 85
- Salvestab sisendkausta alamkausta `jpg/`

Kasutus:
    python convert.py "C:\\tee\\kaustani"
    python convert.py                # küsib kausta interaktiivselt
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

from PIL import Image, ImageOps

# Suurte piltide jaoks (100+ MP PSD/TIF)
Image.MAX_IMAGE_PIXELS = None

TARGET_WIDTH = 1920
JPG_QUALITY = 85
EXTENSIONS = {".tif", ".tiff", ".psd"}


def load_image(path: Path) -> Image.Image:
    """Avab faili sõltumata formaadist ja tagastab Pillow Image."""
    if path.suffix.lower() == ".psd":
        # Lazy import – psd-tools pole TIF-i jaoks vajalik
        from psd_tools import PSDImage

        psd = PSDImage.open(path)
        img = psd.composite()  # tasandab kõik kihid
        if img is None:
            raise RuntimeError("PSD composite tagastas tühja pildi")
        return img
    # TIF/TIFF
    img = Image.open(path)
    img.load()
    return img


def to_rgb(img: Image.Image) -> Image.Image:
    """Teisendab pildi RGB-ks. Alpha-kanal sulandatakse valgele taustale."""
    if img.mode == "RGB":
        return img
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        img = img.convert("RGBA")
        bg = Image.new("RGB", img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[-1])
        return bg
    # CMYK, I;16, L, P jne
    return img.convert("RGB")


def resize_to_width(img: Image.Image, width: int) -> Image.Image:
    if img.width == width:
        return img
    ratio = width / img.width
    height = max(1, round(img.height * ratio))
    return img.resize((width, height), Image.LANCZOS)


def convert_one(src: Path, out_dir: Path) -> tuple[bool, str]:
    try:
        img = load_image(src)
        # EXIF-orientatsioon (peamiselt TIF-de jaoks)
        try:
            img = ImageOps.exif_transpose(img)
        except Exception:
            pass
        img = to_rgb(img)
        img = resize_to_width(img, TARGET_WIDTH)
        dst = out_dir / (src.stem + ".jpg")
        img.save(
            dst,
            format="JPEG",
            quality=JPG_QUALITY,
            optimize=True,
            progressive=True,
        )
        return True, f"{img.width}x{img.height}"
    except Exception as e:
        return False, f"VIGA: {e}"


def ask_folder() -> Path:
    raw = input("Sisesta kausta tee: ").strip().strip('"').strip("'")
    return Path(raw)


def main() -> int:
    if len(sys.argv) >= 2:
        folder = Path(sys.argv[1])
    else:
        folder = ask_folder()

    if not folder.is_dir():
        print(f"Kaust ei eksisteeri: {folder}")
        input("Vajuta Enter sulgemiseks...")
        return 1

    files = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in EXTENSIONS
    )
    if not files:
        print("Ei leidnud .tif / .tiff / .psd faile.")
        input("Vajuta Enter sulgemiseks...")
        return 0

    out_dir = folder / "jpg"
    out_dir.mkdir(exist_ok=True)

    print(f"Leitud {len(files)} faili. Väljund: {out_dir}")
    print(f"Laius: {TARGET_WIDTH}px | Kvaliteet: {JPG_QUALITY} | RGB")
    print("-" * 60)

    t0 = time.time()
    ok = 0
    fail = 0
    for i, src in enumerate(files, 1):
        success, info = convert_one(src, out_dir)
        status = "OK " if success else "FAIL"
        print(f"[{i}/{len(files)}] {status}  {src.name}  ->  jpg/{src.stem}.jpg  ({info})")
        if success:
            ok += 1
        else:
            fail += 1

    dt = time.time() - t0
    print("-" * 60)
    print(f"Valmis. Õnnestus: {ok}  Ebaõnnestus: {fail}  Aeg: {dt:.1f}s")
    if sys.stdin.isatty():
        input("Vajuta Enter sulgemiseks...")
    return 0 if fail == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
