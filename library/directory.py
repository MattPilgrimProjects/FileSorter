import os

def create_recursive_diretory(path):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError:
        pass
    else:
        return os.makedirs(path, exist_ok=True)