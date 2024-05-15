"""
Arquivo de teste para as funções de busca em árvores binárias e AVL e pesquisa sequencial
"""

import json
import random
import time
from typing import List
from utils.registro import retorna_registro

def inserir_registros(arvore, nome_arquivo: str) -> None:
    """Função para inserir registros em uma árvore binária ou AVL

    Args:
        arvore (_type_): Recebe uma árvore binária ou AVL
        nome_arquivo (str): Recebe o nome do arquivo de entrada
    """
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            chave_registro = retorna_registro(linha.strip())
            arvore.raiz = arvore.inserir(arvore.raiz, chave_registro)


def buscar_chaves_aleatorias(estrutura, chave_limite: int, max_presente: int, max_ausente: int) -> List[str]:
    """Função para buscar chaves aleatórias em uma árvore binária ou AVL

    Args:
        arvore (_type_): Recebe uma árvore binária ou AVL
        chave_limite (int): Define o maior valor que a chave aleatória pode ter
        max_presente (int): Quantidade máxima de chaves presentes a serem buscadas
        max_ausente (int): Quantidade máxima de chaves ausentes a serem buscadas

    Returns:
        List[str]: Retorna uma lista com as chaves encontradas e não encontradas
    """
    total_presente = 0
    total_ausente = 0
    encontradas = []
    nao_encontradas = []

    while total_presente < max_presente or total_ausente < max_ausente:
        if total_ausente < max_ausente:
            chave_aleatoria = random.randint(chave_limite, chave_limite * 2)
        else:
            chave_aleatoria = random.randint(0, chave_limite)

        start_time = time.time()
        numero_de_comparacoes, resultado_chave_encontrada = estrutura.buscar(chave_aleatoria)
        elapsed_time = time.time() - start_time

        resultado = {
            "chave": chave_aleatoria,
            "encontrada": resultado_chave_encontrada,
            "tempo_de_busca": f'{elapsed_time:.9f}',
            "interacoes": numero_de_comparacoes
        }

        if resultado_chave_encontrada and total_presente < max_presente:
            encontradas.append(resultado)
            total_presente += 1
        elif not resultado_chave_encontrada and total_ausente < max_ausente:
            nao_encontradas.append(resultado)
            total_ausente += 1

    return encontradas + nao_encontradas


def gravar_resultados(arquivo_entrada: str, nome_arquivo_saida: str, resultados) -> None:
    """Função para gravar os resultados em um arquivo de saída

    Args:
        nome_arquivo_saida (str): Nome do arquivo de saída
        encontradas (List[str]): Lista com as chaves encontradas
        nao_encontradas (List[str]): Lista com as chaves não encontradas
    """
    print(f"\nEstrutura de dados testada: {nome_arquivo_saida.split('/')[1].split('.')[0]}")

    total_comparacoes = 0
    total_tempo_busca = 0
    total_encontradas = 0
    total_nao_encontradas = 0

    for resultado in resultados:
        total_comparacoes += resultado["interacoes"]
        total_tempo_busca += float(resultado["tempo_de_busca"])
        if resultado["encontrada"]:
            total_encontradas += 1
        else:
            total_nao_encontradas += 1

    media_comparacoes = total_comparacoes / len(resultados) if len(resultados) > 0 else 0
    media_tempo_busca = total_tempo_busca / len(resultados) if len(resultados) > 0 else 0

    data = {
        "arquivo_entrada": arquivo_entrada,
        "total_de_buscas": len(resultados),
        "total_encontradas": total_encontradas,
        "total_nao_encontradas": total_nao_encontradas,
        "media_comparacoes": f'{media_comparacoes:.2f}',
        "media_tempo_busca": f'{media_tempo_busca:.9f}',
        "resultados": resultados
    }
    with open(nome_arquivo_saida, "a", encoding="utf-8") as arquivo_saida:
        print(f"Arquivo: {arquivo_entrada.split('/')[1]}")
        json.dump(data, arquivo_saida, indent=4)


def arvore_test(arvore, ordenado: bool, arquivo_saida: str, chave_limite: int) -> None:
    """Função para testar a árvore binária ou AVL

    Args:
        arvore (_type_): Recebe uma árvore binária ou AVL
        arquivo_entrada (str): Nome do arquivo de entrada
        nome_arquivo_saida (str): Nome do arquivo de saída
        chave_limite (int): Define o maior valor que a chave aleatória pode ter
    """
    diretorio_entrada = "arquivos_entrada/"
    diretorio_saida = "arquivos_saida/"

    if ordenado:
        ordenado_str = ""
    else:
        ordenado_str = "_desordenado"

    entrada = f"{diretorio_entrada}{chave_limite}{ordenado_str}.txt"
    saida = f"{diretorio_saida}{arquivo_saida}.json"

    inserir_registros(arvore, entrada)
    data = buscar_chaves_aleatorias(arvore, chave_limite, 15, 15)
    gravar_resultados(entrada, saida, data)


def pesquisa_sequencial_test(estutura, ordenado: bool, arquivo_saida: str, chave_limite: int) -> None:
    """Função para testar a pesquisa sequencial

    Args:
        estutura (_type_): Estrutura de dados de pesquisa sequencial
        arquivo_entrada (str): Arquivo de entrada
        arquivo_saida (str): Arquivo de saída
        chave_limite (int): Define o maior valor que a chave aleatória pode ter
    """
    diretorio_entrada = "arquivos_entrada/"
    diretorio_saida = "arquivos_saida/"

    if ordenado:
        ordenado_str = ""
    else:
        ordenado_str = "_desordenado"

    entrada = f"{diretorio_entrada}{chave_limite}{ordenado_str}.txt"
    saida = f"{diretorio_saida}{arquivo_saida}.json"
    estutura.set_nome_do_arquivo(entrada)

    data = buscar_chaves_aleatorias(estutura, chave_limite, 15, 15)

    gravar_resultados(entrada, saida, data)
