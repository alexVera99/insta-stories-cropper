from pathlib import Path


class DirectoryNotFoundError(Exception):
    def __init__(self, directory: Path):
        super().__init__(f"Directory {directory.absolute()} not found")
