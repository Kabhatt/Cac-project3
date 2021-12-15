"""This is the function that will navigate the absolute path for the csv files"""
from pathlib import Path


def absolute_path(file_path):
    """This returns the absolute path of the object"""
    relative_path = Path(file_path)
    return relative_path.absolute()
