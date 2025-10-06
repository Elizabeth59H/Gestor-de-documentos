# Gestor de documentos
Aplicación de organización de archivos con soporte en SQL.

✅ Nombre y descripción del proyecto

🔧 Tecnologías utilizadas

📂 Estructura del proyecto

🚀 Instalación y ejecución

📸 Capturas de pantalla (opcional)

📚 Cómo funciona

🛠️ Funcionalidades


# 🗂️ File Organizer + SQLite Logger

Una herramienta de automatización escrita en Python que organiza archivos de una carpeta en subcarpetas según su tipo (documentos, imágenes, vídeos, etc.) y **registra cada movimiento en una base de datos SQLite** para llevar un historial completo.

Ideal para mantener limpia y organizada tu carpeta de Descargas o Documentos.

🔧 2. Tecnologías utilizadas
## 🔧 Tecnologías utilizadas

- Python 3.10+
- SQLite (base de datos embebida)
- Módulos estándar: `os`, `shutil`, `sqlite3`, `datetime`, `pathlib`
 
## 📂 Estructura del proyecto

file-organizer-sql/
├── main.py # Script principal
├── file_organizer/
│ ├── organizer.py # Lógica para organizar archivos
│ └── db.py # Lógica para la base de datos SQLite
├── organized_files.db # Base de datos generada automáticamente
├── README.md
├── requirements.txt
└── .gitignore

🚀 4. Instalación y ejecución
## 🚀 Instalación y ejecución

1. Clona este repositorio:

```bash
git clone https://github.com/tuusuario/file-organizer-sql.git
cd file-organizer-sql

2. (Opcional) Crea un entorno virtual:

python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
3.Instala las dependencias (ninguna por ahora, pero útil para el futuro):

pip install -r requirements.txt
4. Ejecuta el script:

python main.py

5. Introduce la ruta absoluta de la carpeta que quieres organizar cuando se te solicite. ´´´



---

### 📚 5. **¿Cómo funciona?**

```md
## 📚 ¿Cómo funciona?

- El script escanea todos los archivos en la carpeta que el usuario proporciona.
- Determina el tipo de archivo según su extensión.
- Mueve el archivo a una subcarpeta correspondiente: `/Documentos`, `/Imágenes`, `/Videos`, etc.
- Si el archivo ya existe, le añade una marca de tiempo para evitar sobreescribir.
- Cada movimiento se guarda en una base de datos SQLite (`organized_files.db`) con:
  - Nombre del archivo
  - Extensión
  - Ruta original
  - Nueva ruta
  - Fecha de modificación del archivo
  - Fecha y hora del movimiento

🛠️ 6. Funcionalidades actuales
## 🛠️ Funcionalidades

✅ Organización automática por tipo de archivo  
✅ Registro en base de datos de cada archivo movido  
✅ Evita sobrescribir archivos duplicados  
✅ Totalmente local y sin dependencias externas


🔮 7. Posibles mejoras futuras (roadmap)
## 🔮 Posibles mejoras futuras

- Interfaz gráfica (Tkinter o PyQt)
- Organización por fecha o tamaño
- Configuración personalizada con archivo JSON
- Eliminación de archivos duplicados
- Visualización de estadísticas (cuántos archivos movidos, espacio liberado)
- Exportación del historial a CSV o PDF

🪪 8. Licencia
## 🪪 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

✅ ¿Qué hacer ahora?

Copia y pega todo esto en tu archivo README.md. Cuando estés listo, dime si quieres que:

Te ayude a generar capturas de pantalla o GIFs para agregar al README.

Agreguemos un archivo LICENSE.

Preparamos un botón de GitHub Actions para correr automáticamente el script (ideal para tareas programadas).

Lo empaquetamos como un ejecutable .exe o .app.


