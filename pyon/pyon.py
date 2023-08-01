from ast import literal_eval


def check_pyon_file(path: str) -> None:
    if not path.endswith('.pyon'):
        return False
    else:
        return True


def apply_indentation(string: str, indentation_with: int = 4) -> str:
    indent_counter = 0
    indent_space = ' ' * indentation_with
    char_list = [c for c in string]
    before_char: str = ''

    for char in enumerate(char_list):
        if char[1] == '{' or char[1] == '[':
            indent_counter += 1
            c = char_list.pop(char[0])
            char_list.insert(char[0], c + '\n' + indent_space * indent_counter)
        elif char[1] == '}' or char[1] == ']':
            indent_counter -= 1
            c = char_list.pop(char[0])
            char_list.insert(char[0], '\n'+ indent_space * indent_counter + c)
        elif char[1] == ',':
            c = char_list.pop(char[0])
            char_list.insert(char[0], c + '\n' + indent_space * indent_counter)
        elif before_char == ',':
            c = char_list.pop(char[0])
            char_list.insert(char[0], '')

        before_char = char[1]

    return ''.join(char_list)


class PyonFile:
    def __init__(self, path: str, encoding='utf-8', identation: int =4) -> None:
        if not check_pyon_file(path):
            raise Exception(f'FileNameError - the path {path} not is a pyon file')
        
        self.path: str = path
        self.encoding: str = encoding
        self.identation: int = identation

    def load(self):
        with open(self.path, 'r', encoding=self.encoding) as pyon_file:
            return literal_eval(pyon_file.read())
        
    def loads(self, string: str) -> list | dict:
        return literal_eval(string)


    def dump(self, data: list|dict, indent: int = 4) -> None:

        with open(self.path, 'w', encoding=self.encoding) as pyon_file:
            text = apply_indentation(str(data), self.identation)
            pyon_file.write(text)

    def dumps(self, data: str) -> None:

        if not isinstance(data, str):
            raise Exception('DataError - A data must be a string ')

        with open(self.path, 'w', encoding=self.encoding) as pyon_file:
            text = apply_indentation(data, self.identation)
            pyon_file.write(text)



def load(path: str, encoding='UTF-8') -> list | dict:

    check_pyon_file(path)

    with open(path, 'r', encoding=encoding) as pyon_file:
        return literal_eval(pyon_file.read())

def loads(string: str) -> list | dict:
    return literal_eval(string)

def dump(path: str, data: list|dict, encoding='UTF-8', indent: int = 4) -> None:

    check_pyon_file(path)

    with open(path, 'w', encoding=encoding) as pyon_file:
        text = apply_indentation(str(data), indent)
        pyon_file.write(text)

def dumps(path: str, data: str, encoding='UTF-8', indent: int = 4) -> None:
    check_pyon_file(path)

    if not isinstance(data, str):
        raise Exception('DataError - A data must be a string ')

    with open(path, 'w', encoding=encoding) as pyon_file:
        text = apply_indentation(data, indent)
        pyon_file.write(text)
