"""
Arquivo principal do programa.
"""

import sys
from typing import List

from utils.utils import gerar_arquivo, limpar_tela
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
    print()
    for linhas in quantidade_de_linhas:
        gerar_arquivo(linhas, chaves_ordenadas=True)
        gerar_arquivo(linhas, chaves_ordenadas=False)


def teste_automatizado(quantidade_de_linhas: List[int]) -> None:
    """Função que realiza testes automatizados com as árvores binária e AVL.

    Args:
        quantidade_de_linhas (List[int]): Quantidade de linhas do arquivo de entrada.
    """
    order = [True, False]
    for num_linhas in quantidade_de_linhas:
        for is_order in order:
            arvore_binaria = ArvoreBinaria()
            arvore_test(arvore_binaria, ordenado=is_order, arquivo_saida="arvore_binaria", chave_limite=num_linhas)

            arvore_avl = ArvoreAVL()
            arvore_test(arvore_avl, ordenado=is_order, arquivo_saida="arvore_avl", chave_limite=num_linhas)

            pesquisa_sequencial = PesquisaSequencial()
            pesquisa_sequencial_test(pesquisa_sequencial, ordenado=is_order, arquivo_saida="pesquisa_sequencial", chave_limite=num_linhas)


def menu(quantidade_de_linhas = None) -> None:
    """Função que exibe o menu do programa.
    """
    if quantidade_de_linhas is None:
        quantidade_de_linhas = [100, 500, 1_000, 5_000, 10_000]

    limpar_tela()
    print(f"{'='*10} Menu - TP1 {'='*10}")
    print("1 - Gerar arquivos")
    print("2 - Testar estruturas de dados")
    print("3 - Sair")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        limpar_tela()
        print(f"{'='*10} Gerador de arquivos {'='*10}")

        linhas = input("Digite a quantidade de linhas [100, 500, ...]: ")
        if linhas != "":
            quantidade_de_linhas = [int(x.strip()) for x in linhas.split(",")]

        gerar_arquivos_facade(quantidade_de_linhas)

        input("\nPressione Enter para continuar...")
        menu(quantidade_de_linhas)
    if opcao == "2":
        limpar_tela()
        print(f"{'='*10} Testes automatizados {'='*10}")

        teste_automatizado(quantidade_de_linhas)

        input("Pressione Enter para continuar...")
        menu(quantidade_de_linhas)


def main() -> None:
    """Função principal do progama
    """
    menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Programa finalizado.")
        sys.exit(0)
