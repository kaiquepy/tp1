"""
Arquivo que contém a classe Registro, que representa um registro do arquivo de entrada.
"""

class Registro:
    """Classe que representa um registro
    """
    def __init__(self, chave: int, dado1: int, dado2: str) -> None:
        self.chave = chave
        self.dado1 = dado1
        self.dado2 = dado2


def retorna_registro(entrada: str) -> Registro:
    """Função que retorna um registro a partir de uma string.

    Args:
        entrada (str): Linha do arquivo de entrada.

    Returns:
        Registro: Registro criado a partir da linha de entrada.
    """
    parts = entrada.split(';')

    chave = int(parts[0])
    dado1 = int(parts[1])
    dado2 = parts[2]

    return Registro(chave, dado1, dado2)
