import shutil
import os
from pathlib import Path
from zipfile import ZipFile

DESKTOP = Path.home() / "Desktop" 
ZIP_DIR_PATH = DESKTOP / "FILERS_ZIP"
COMPRESSED_PATH = DESKTOP / "Aula_186_compressed.zip"
EXTRACTED_PATH = DESKTOP / "FILERS_extracted"

# shutil.rmtree(ZIP_DIR_PATH, ignore_errors=True)
# Path.unlink(COMPRESSED_PATH, missing_ok=True)
# shutil.rmtree(str(COMPRESSED_PATH).replace(".zip", ""), ignore_errors=True)
# shutil.rmtree(EXTRACTED_PATH, ignore_errors=True)

ZIP_DIR_PATH.mkdir(exist_ok=True)

def create_files(count: int, ZIP_DIR: Path):
    for i in range(count):
        text = f"File_{i}"
        with open(ZIP_DIR / f'{text}.txt', 'w') as file:
            file.write(text)

create_files(10, ZIP_DIR_PATH)



