import os
import tempfile


def create_tmp_file() -> str:
    """
    Создает временная папка и возвращается  путь к папке.
    """
    fd, path = tempfile.mkstemp()
    print(fd)
    print(path)
    with os.fdopen(fd, "w") as tmp:
        tmp.write("stuff")
        return path
