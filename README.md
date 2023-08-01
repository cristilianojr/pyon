# Pyon
Pyon é um arquivo de notação para listas e dicionários em Python, servindo como um arquivo de armazenamento de dados. Similar ao formato JSON, Pyon oferece os comandos dump e load para gravar e carregar dados em formato Pyon.

# Utilização
O módulo Pyon oferece duas formas de utilização: utilizando a classe PyonFile ou diretamente chamando as funções load, loads, dump e dumps.

# Usando a classe PyonFile
```py
from pyon import PyonFile

# Cria um objeto PyonFile para um arquivo específico
pyon_file = PyonFile('example.pyon')

# Carrega os dados do arquivo
data = pyon_file.load()

# Faz alterações nos dados...

# Salva as alterações no arquivo
pyon_file.dump(data)
```
# Usando as funções diretas

```py
from pyon import load, loads, dump, dumps

# Carrega os dados de um arquivo Pyon
data = load('example.pyon')

# Faz alterações nos dados...

# Salva as alterações no arquivo Pyon
dump('example.pyon', data)
```

# Funções e Métodos
- check_pyon_file(path: str) -> bool
Função para verificar se o caminho do arquivo possui a extensão ".pyon". Retorna True se o caminho for válido e False caso contrário.

- apply_indentation(string: str, indentation_with: int = 4) -> str
Função que aplica a indentação adequada em um texto Pyon. Ela é usada internamente pelos métodos dump e dumps da classe PyonFile, mas também pode ser utilizada de forma independente.

- class PyonFile
Classe que representa um arquivo Pyon. Possui os seguintes métodos:

- load(self) -> list | dict
Carrega e retorna os dados contidos no arquivo Pyon.

- loads(self, string: str) -> list | dict
Analisa uma string em formato Pyon e retorna os dados correspondentes.

- dump(self, data: list | dict, indent: int = 4) -> None
Grava os dados (lista ou dicionário) no arquivo Pyon com a indentação especificada.

- dumps(self, data: str) -> None
Grava uma string contendo dados em formato Pyon no arquivo com a indentação especificada.

# Funções Diretas
- load(path: str, encoding='UTF-8') -> list | dict
Carrega e retorna os dados contidos no arquivo Pyon especificado pelo caminho path.

- loads(string: str) -> list | dict
Analisa uma string em formato Pyon e retorna os dados correspondentes.

- dump(path: str, data: list | dict, encoding='UTF-8', indent: int = 4) -> None
Grava os dados (lista ou dicionário) no arquivo Pyon especificado pelo caminho path, com a indentação especificada.

- dumps(path: str, data: str, encoding='UTF-8', indent: int = 4) -> None
Grava uma string contendo dados em formato Pyon no arquivo especificado pelo caminho path, com a indentação especificada.

# Exemplos
## Exemplo 1: Utilizando a classe PyonFile
```py
from pyon import PyonFile

# Criando um objeto PyonFile para um arquivo específico
pyon_file = PyonFile('data.pyon')

# Carregando os dados do arquivo
data = pyon_file.load()

# Realizando alterações nos dados
data['nova_chave'] = 'Novo valor'

# Salvando as alterações no arquivo
pyon_file.dump(data)
```
## Exemplo 2: Utilizando as funções diretas
```py
from pyon import load, dump

# Carregando os dados de um arquivo Pyon
data = load('data.pyon')

# Realizando alterações nos dados
data['nova_chave'] = 'Novo valor'

# Salvando as alterações no arquivo Pyon
dump('data.pyon', data)
```
Lembre-se de sempre verificar a extensão do arquivo ao usar as funções load, loads, dump e dumps. Arquivos Pyon devem possuir a extensão ".pyon".
