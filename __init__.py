from ast import literal_eval as _literal_eval
from typing import Any
from utils import __checking_pyon, indent_string


def load(path: str, encoding='UTF-8') -> list | dict:

    __checking_pyon(path)

    with open(path, 'r', encoding=encoding) as pyon_file:
        return _literal_eval(pyon_file.read())

def loads(string: str) -> list | dict:
    return _literal_eval(string)

def dump(path: str, data: list|dict, encoding='UTF-8', indent: int = 4) -> None:

    __checking_pyon(path)

    with open(path, 'w', encoding=encoding) as pyon_file:
        text = indent_string(str(data), indent)
        pyon_file.write(text)

def dumps(path: str, data: str, encoding='UTF-8', indent: int = 4) -> None:
    __checking_pyon(path)

    if not isinstance(data, str):
        raise Exception('DataError - A data must be a string ')

    with open(path, 'w', encoding=encoding) as pyon_file:
        text = indent_string(data, indent)
        pyon_file.write(text)
