import os

def remove_prefix(name, prefix="x-"):
    if name.startswith(prefix):
        return name[len(prefix):]
    return name

def rename_in_tree(root_dir, prefix="x-"):
    # Renombrar archivos primero
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.startswith(prefix):
                old_path = os.path.join(dirpath, filename)
                new_filename = remove_prefix(filename, prefix)
                new_path = os.path.join(dirpath, new_filename)
                print(f'Renombrando archivo: {old_path} -> {new_path}')
                os.rename(old_path, new_path)
    # Renombrar directorios de adentro hacia afuera
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            if dirname.startswith(prefix):
                old_dir = os.path.join(dirpath, dirname)
                new_dirname = remove_prefix(dirname, prefix)
                new_dir = os.path.join(dirpath, new_dirname)
                print(f'Renombrando directorio: {old_dir} -> {new_dir}')
                os.rename(old_dir, new_dir)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    rename_in_tree(base_dir)