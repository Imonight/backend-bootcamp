import re
from pathlib import Path


def parse_new_name(filename: str, pattern: str, replacement: str) -> str:
    return re.sub(pattern, replacement, filename)


def bulk_rename(directory: str, pattern: str, replacement):
    dir_path = Path(directory)

    if not dir_path.exists():
        raise FileNotFoundError(f"Error file not find for: {directory}")

    for file in dir_path.iterdir():
        if file.is_file():
            new_name = parse_new_name(file.name, pattern, replacement)
            new_path = file.with_name(new_name)
            file.rename(new_path)
        print("BULK rename Done!!!")
