"""
Arquivo que contém os testes do estruturas de dados
"""

import random
import time
from modules.arvore_binaria import ArvoreBinaria, retorna_tipo_reg

def arvore_binaria_test() -> None:
    """_summary_
    """

    arvore = ArvoreBinaria()

    nome_arquivo = "arquivos_entrada/100.txt"
    total_presente = 1
    total_ausente = 1
    vetor_encontradas = ["" for _ in range(16)]
    vetor_nao_encontradas = ["" for _ in range(16)]

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

        end_time = time.time()
        elapsed_time = end_time - start_time

        if resultado_chave_encontrada:
            if total_presente <= 15:
                vetor_encontradas[total_presente - 1] = f"Chave ({chave_aleatoria:06}) encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arvore.numero_interacoes}"
                total_presente += 1
        else:
            if total_ausente <= 15:
                vetor_nao_encontradas[total_ausente - 1] = f"Chave ({chave_aleatoria:06}) não encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arvore.numero_interacoes}"
                total_ausente += 1

        gerou_todas = total_ausente == 16 and total_presente == 16

    with open("arquivos_saida/100.txt", "w", encoding="utf-8") as arquivo_saida:
        for i in range(15):
            arquivo_saida.write(vetor_encontradas[i] + "\n")
        for i in range(15):
            arquivo_saida.write(vetor_nao_encontradas[i] + "\n")


arvore_binaria_test()

#def arvore_avl():
#    random.seed(time.time())
#    arv = ArvoreAVL()
#    nomeArquivo = "dadosOrdenados500.txt"
#
#    with open(os.path.join("Arquivos Entrada", nomeArquivo), 'r') as arquivo:
#        for linha in arquivo:
#            linha = linha.strip()
#            if linha:
#                registro_temp = retornaTipoReg(linha)
#                arv.raiz = arv.inserir(arv.raiz, registro_temp)
#
#    vetorEncontradas = []
#    vetorNaoEncontradas = []
#    totalPresente = 0
#    totalAusente = 0
#    gerouTodas = False
#
#    while not gerouTodas:
#        chaveAleatoria = random.randint(0, 19999) if totalAusente < 15 else random.randint(0, 9999)
#        arv.numero_interacoes = 0
#
#        start_time = time.time()
#        resultadoChaveEncontrada = arv.buscar(arv.raiz, chaveAleatoria)
#        elapsed_time = time.time() - start_time
#
#        if resultadoChaveEncontrada:
#            if totalPresente < 15:
#                vetorEncontradas.append(f"Chave ({chaveAleatoria:06}) encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arv.numero_interacoes}")
#                totalPresente += 1
#        else:
#            if totalAusente < 15:
#                vetorNaoEncontradas.append(f"Chave ({chaveAleatoria:06}) não encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arv.numero_interacoes}")
#                totalAusente += 1
#
#        gerouTodas = (totalAusente == 15) and (totalPresente == 15)
#
#    with open(os.path.join("Arquivos Saida", "avl", f"arquivo_saida_{nomeArquivo}"), 'w') as arquivo_saida:
#        for linha in vetorEncontradas:
#            arquivo_saida.write(linha + "\n")
#        for linha in vetorNaoEncontradas:
#            arquivo_saida.write(linha + "\n")
#
