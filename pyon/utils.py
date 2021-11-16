
def __checking_pyon(path: str):
    if not path.endswith('.pyon'):
        raise Exception(f'FileNameError - the path {path} not is a pyon file')

def indent_string(string: str, apply_indentation_with: int = 4) -> str:
    indent_counter = 0
    indent_space = ' ' * apply_indentation_with
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
