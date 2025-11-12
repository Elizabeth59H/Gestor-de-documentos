# 🗂️ Gestor de Documentos con SQLite

**Gestor de Documentos** es una herramienta desarrollada en **Python** que organiza automáticamente los archivos de una carpeta en subcarpetas según su tipo (documentos, imágenes, vídeos, etc.) y registra cada movimiento en una base de datos **SQLite**, manteniendo un historial completo.

Ideal para mantener ordenadas carpetas como **Descargas** o **Documentos** 📁✨

---

## 🚀 Tecnologías utilizadas

- 🐍 **Python 3.10+**
- 🧱 **SQLite** (base de datos local)
- 📦 Módulos estándar: `os`, `shutil`, `sqlite3`, `datetime`, `pathlib`

---
```## 📂 Estructura del proyecto

Gestor-de-documentos/
│
├── main.py # Script principal
├── file_organizer/
│ ├── init.py
│ ├── organizer.py # Lógica para organizar archivos
│ └── db.py # Lógica para la base de datos SQLite
├── organized_files.db # Base de datos generada automáticamente
└── README.md # Documentación del proyecto

Copiar código
```

---

## 🧠 ¿Cómo funciona?

1. El usuario introduce la ruta de la carpeta que desea organizar.
2. El programa escanea los archivos dentro de esa carpeta.
3. Los mueve a subcarpetas según su tipo:
   - **Documentos/** (`.pdf`, `.docx`, `.txt`, etc.)
   - **Imágenes/** (`.jpg`, `.png`, `.gif`, etc.)
   - **Videos/** (`.mp4`, `.avi`, etc.)
   - **Otros/** (todo lo demás)
4. Si un archivo ya existe, se le agrega una marca de tiempo para evitar sobrescribirlo.
5. Cada movimiento se guarda en la base de datos `organized_files.db` con:
   - Nombre del archivo
   - Extensión
   - Ruta original
   - Nueva ruta
   - Fecha de modificación
   - Fecha y hora del movimiento

---

## 🛠️ Funcionalidades actuales

✅ Organización automática por tipo de archivo  
✅ Registro detallado en base de datos SQLite  
✅ Evita sobrescribir archivos duplicados  
✅ Totalmente local y sin dependencias externas  

---

## 🔮 Mejoras futuras

✨ Interfaz gráfica con **Tkinter** o **PyQt**  
📅 Organización por fecha o tamaño  
⚙️ Configuración personalizada mediante archivo JSON  
📊 Estadísticas: cantidad de archivos movidos y espacio liberado  
📤 Exportación del historial a **CSV** o **PDF**

---

## 💻 Instalación y ejecución

1️⃣ Clona este repositorio:

```bash
git clone https://github.com/tuusuario/file-organizer-sql.git
cd file-organizer-sql
2️⃣ (Opcional) Crea un entorno virtual:

bash
Copiar código
python -m venv venv
venv\Scripts\activate   # En Windows
3️⃣ Ejecuta el programa:

bash
Copiar código
python main.py
4️⃣ Ingresa la ruta absoluta de la carpeta que deseas organizar, por ejemplo:

makefile
Copiar código
C:\Users\Beatriz\Downloads
📚 Autor
👩‍💻 Elizabeth Herrera

⭐ Si te gusta este proyecto, no olvides dejar una estrella en GitHub.
