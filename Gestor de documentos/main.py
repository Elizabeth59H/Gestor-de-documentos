from file_organizer.organizer import organize_files

if __name__ == "__main__":
    folder_path = input("👉 Ingresa la ruta de la carpeta que quieres organizar: ")
    organize_files(folder_path)
