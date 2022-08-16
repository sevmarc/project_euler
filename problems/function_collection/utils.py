import os
import pathlib


def handle_filepath(file_path: str, debug: bool = False) -> str:
    problems_dir_path = pathlib.Path(__file__).parent.resolve().parent.resolve()
    filename = os.path.join(problems_dir_path, file_path)
    if debug:
        print(f"{problems_dir_path = }")
        print(f"{filename = }")
    return filename
