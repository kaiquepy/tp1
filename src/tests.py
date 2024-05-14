"""
Arquivo que contém os testes do estruturas de dados
"""

import random
import time
from modules.arvore_binaria import ArvoreBinaria, retorna_tipo_reg
from modules.arvore_avl import ArvoreAVL


def arvore_binaria_test() -> None:
    """_summary_
    """
    arvore = ArvoreBinaria()

    nome_arquivo = "arquivos_entrada/100.txt"
    total_presente = 1
    total_ausente = 1
    vetor_encontradas = []
    vetor_nao_encontradas = []

    arvore.raiz = None

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            auxiliar = retorna_tipo_reg(linha.strip())
            arvore.raiz = arvore.inserir(arvore.raiz, auxiliar)
    arquivo.close()

    gerou_todas = False
    while not gerou_todas:
        if total_ausente < 15:
            chave_aleatoria = random.randint(0, 19999)
        else:
            chave_aleatoria = random.randint(0, 9999)

        arvore.numero_interacoes = 0

        start_time = time.time()
        resultado_chave_encontrada = arvore.buscar(arvore.raiz, chave_aleatoria)
        elapsed_time = time.time() - start_time

        if resultado_chave_encontrada and total_presente <= 15:
            vetor_encontradas.append(f"Chave ({chave_aleatoria:06}) encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arvore.numero_interacoes}")
            total_presente += 1
        elif total_ausente <= 15:
            vetor_nao_encontradas.append(f"Chave ({chave_aleatoria:06}) não encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arvore.numero_interacoes}")
            total_ausente += 1

        gerou_todas = total_ausente == 16 and total_presente == 16

    with open("arquivos_saida/100.txt", "w", encoding="utf-8") as arquivo_saida:
        for i in range(15):
            arquivo_saida.write(vetor_encontradas[i] + "\n")
        for i in range(15):
            arquivo_saida.write(vetor_nao_encontradas[i] + "\n")


def arvore_avl() -> None:
    """_summary_
    """
    arvore = ArvoreAVL()

    nome_arquivo = "arquivos_entrada/100.txt"
    vetor_encontradas = []
    vetor_nao_encontradas = []
    total_presente = 0
    total_ausente = 0

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            registro_temp = retorna_tipo_reg(linha)
            arvore.raiz = arvore.inserir(arvore.raiz, registro_temp)
    arquivo.close()

    gerou_todas = False
    while not gerou_todas:
        if total_ausente < 15:
            chave_aleatoria = random.randint(0, 19999)
        else:
            chave_aleatoria = random.randint(0, 9999)

        arvore.numero_interacoes = 0

        start_time = time.time()
        resultado_chave_encontrada = arvore.buscar(arvore.raiz, chave_aleatoria)
        elapsed_time = time.time() - start_time

        if resultado_chave_encontrada and total_presente < 15:
                vetor_encontradas.append(f"Chave ({chave_aleatoria:06}) encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arvore.numero_interacoes}")
                total_presente += 1
        elif total_ausente < 15:
                vetor_nao_encontradas.append(f"Chave ({chave_aleatoria:06}) não encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arvore.numero_interacoes}")
                total_ausente += 1

        gerou_todas = (total_ausente == 15) and (total_presente == 15)

    with open("arquivos_saida/100.txt", "w", encoding="utf-8") as arquivo_saida:
        for linha in vetor_encontradas:
            arquivo_saida.write(linha + "\n")
        for linha in vetor_nao_encontradas:
            arquivo_saida.write(linha + "\n")
