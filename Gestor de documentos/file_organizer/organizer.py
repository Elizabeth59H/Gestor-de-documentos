import os
import shutil
from pathlib import Path
from datetime import datetime
from .db import create_table, log_movement

# Tipos de archivos por categoría
FILE_TYPES = {
    "Documentos": [".pdf", ".docx", ".txt", ".xls", ".xlsx", ".pptx"],
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Música": [".mp3", ".wav", ".aac"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Otros": []
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Otros"

def organize_files(folder_path):
    create_table()
    base_path = Path(folder_path)

    if not base_path.exists():
        print("❌ La ruta especificada no existe.")
        return

    for item in base_path.iterdir():
        if item.is_file():
            extension = item.suffix
            category = get_category(extension)
            target_dir = base_path / category
            target_dir.mkdir(exist_ok=True)

            new_file_path = target_dir / item.name

            # Evita sobrescribir archivos duplicados
            if new_file_path.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_file_path = target_dir / f"{item.stem}_{timestamp}{item.suffix}"

            shutil.move(str(item), str(new_file_path))

            # Guarda el registro en la base de datos
            modified_time = datetime.fromtimestamp(new_file_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            log_movement(item.name, extension, str(item), str(new_file_path), modified_time)

            print(f"📁 {item.name} → {category}/")
