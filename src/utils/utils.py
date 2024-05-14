"""
Arquivo com funções uteis que podem ser reutilizadas
"""

import time
import random
import string
from typing import Any

def tempo_gasto(funcao: Any):
    """
    Decorator que mede o tempo gasto para executar uma função.

    Args:
        funcao (Callable): A função cuja execução será medida.

    Returns:
        Callable: Uma função wrapper que mede o tempo de execução da função original.
    """
    def wrapper(*args: Any, **kwargs: Any) -> None:
        """
        Função interna que envolve a função original e mede o tempo de execução.

        Args:
            *args (Any): Argumentos posicionais da função original.
            **kwargs (Any): Argumentos nomeados da função original.
        """
        tempo_inicial = time.time()
        funcao(*args, **kwargs)
        tempo_final = time.time() - tempo_inicial
        print(f'{tempo_final:.6f}')

    return wrapper


def gerar_arquivo(linhas: int, chaves_ordenadas: bool) -> None:
    """Função geradora de arquivos

    Args:
        linhas (int): Quantidade de linhas do arquivo gerado.
        chaves_ordenadas (bool): Define se o arquivo gerado tem chaves ordenadas.
    """

    nome_do_arquivo = f'arquivos_entrada/{linhas}.txt'
    range_chaves = range(linhas)
    chave = range_chaves

    if not chaves_ordenadas:
        nome_do_arquivo = f'arquivos_entrada/{linhas}_desordenado.txt'
        chave = random.sample(range_chaves, linhas)

    with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
        for i in range(linhas):
            dado2 = ''.join(random.choices(string.ascii_uppercase, k=1000))
            linha = f'{chave[i]},12345,{dado2}\n'
            arquivo.write(linha)
