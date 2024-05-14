"""
Arquivo principal
"""

from typing import List
from utils.utils import gerar_arquivo


def gerar_arquivos_facade(quantidade_de_linhas: List[int]) -> None:
    """Função que gera arquivos com diferentes quantidades de linhas.

    Para cada quantidade de linhas especificada, dois arquivos são gerados:
    um com o flag `True` e outro com o flag `False`.

    Args:
        quantidade_de_linhas (List[int]): Uma lista com a quantidade de linhas para cada arquivo a ser gerado.
    """
    for linhas in quantidade_de_linhas:
        gerar_arquivo(linhas, True)
        gerar_arquivo(linhas, False)


def main() -> None:
    """Função principal do progama
    """
    quantidade_de_linhas = [100, 500, 1_000, 5_000, 10_000]
    gerar_arquivos_facade(quantidade_de_linhas)


if __name__ == "__main__":
    main()
