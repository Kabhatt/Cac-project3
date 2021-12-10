from pathlib import Path

class absolute_path:
    def absolute_path(filepath):
        relative = Path(filepath)
        return relative.absolute()