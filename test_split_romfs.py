import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path("win").resolve()))
sys.path.insert(0, str(Path("dm/tools").resolve()))

import romfs as rfs
import build_app as app

game = os.environ["GAME"]
w = Path(os.environ["W"])

sys.path.insert(0, str(Path("dm/games").resolve()))
import game as gm

profile = gm.load(game)
pkg = profile.get("package")

romfs = rfs.Path(
    os.environ.get("ROMFS") or rfs.source(w / f"data/{pkg}")
)

print("RomFS:", romfs)
print("Это образ:", rfs.is_image(romfs))
print("Существует:", romfs.exists())
print("Это папка:", romfs.is_dir())

files = app.list_files(romfs)

print("Количество файлов:", len(files))
print("Общий размер:", round(sum(x[2] for x in files) / 1024**3, 2), "GB")

print("\nПервые 5 файлов:")
for path, relative, size in files[:5]:
    print(relative, "-", size, "bytes")

    with rfs.open(path, "rb") as f:
        print("Первые байты:", f.read(16).hex())