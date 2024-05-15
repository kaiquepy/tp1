"""
Arquivo principal do programa.
"""

from typing import List

from utils.utils import gerar_arquivo
from tests.teste import arvore_test, pesquisa_sequencial_test
from modules.arvore_binaria import ArvoreBinaria
from modules.arvore_avl import ArvoreAVL
from modules.pesquisa_sequencial import PesquisaSequencial


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


def teste_automatizado(quantidade_de_linhas: List[int]) -> None:
    """Função que realiza testes automatizados com as árvores binária e AVL.

    Args:
        quantidade_de_linhas (List[int]): Quantidade de linhas do arquivo de entrada.
    """
    order = [True, False]
    for num_linhas, is_order in zip(quantidade_de_linhas, order):
        arvore_binaria = ArvoreBinaria()
        arvore_test(arvore_binaria, ordenado=is_order, arquivo_saida="arvore_binaria", chave_limite=num_linhas)

        arvore_avl = ArvoreAVL()
        arvore_test(arvore_avl, ordenado=is_order, arquivo_saida="arvore_avl", chave_limite=num_linhas)

        pesquisa_sequencial = PesquisaSequencial()
        pesquisa_sequencial_test(pesquisa_sequencial, ordenado=is_order, arquivo_saida="pesquisa_sequencial", chave_limite=num_linhas)


def main() -> None:
    """Função principal do progama
    """
    quantidade_de_linhas = [100, 500]
    gerar_arquivos_facade(quantidade_de_linhas)
    teste_automatizado(quantidade_de_linhas)


if __name__ == "__main__":
    main()
