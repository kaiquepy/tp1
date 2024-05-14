"""
Arquivo que contém os testes do estruturas de dados
"""

def arvore_binaria():
    random.seed(time.time())

    arv = ArvoreBinaria()

    nomeArquivo = "dadosOrdenados10000.txt"
    totalPresente = 1
    totalAusente = 1
    vetorEncontradas = ["" for _ in range(16)]
    vetorNaoEncontradas = ["" for _ in range(16)]

    arv.raiz = None

    arquivo = open("Arquivos Entrada/" + nomeArquivo, "r")

    if not arquivo:
        print("Erro ao abrir o arquivo.")
        exit(1)

    for linha in arquivo:
        if linha.strip() != "":
            auxiliar = retornaTipoReg(linha.strip())
            arv.raiz = arv.inserir(arv.raiz, auxiliar)

    arquivo.close()

    gerouTodas = False
    while not gerouTodas:
        if totalAusente < 15:
            chaveAleatoria = random.randint(0, 19999)
        else:
            chaveAleatoria = random.randint(0, 9999)

        arv.numero_interacoes = 0
        start_time = time.time()

        resultadoChaveEncontrada = arv.Buscar(arv.raiz, chaveAleatoria)

        end_time = time.time()
        elapsed_time = end_time - start_time

        if resultadoChaveEncontrada:
            if totalPresente <= 15:
                vetorEncontradas[totalPresente - 1] = f"Chave ({chaveAleatoria:06}) encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arv.numero_interacoes}"
                totalPresente += 1
        else:
            if totalAusente <= 15:
                vetorNaoEncontradas[totalAusente - 1] = f"Chave ({chaveAleatoria:06}) não encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arv.numero_interacoes}"
                totalAusente += 1

        gerouTodas = totalAusente == 16 and totalPresente == 16

    arquivo_saida = open(f"Arquivos Saida/binaria/arquivo_saida_{nomeArquivo}", "w")

    if not arquivo_saida:
        print("Erro ao abrir o arquivo de saída.")
        exit(1)

    for i in range(15):
        arquivo_saida.write(vetorEncontradas[i] + "\n")

    for i in range(15):
        arquivo_saida.write(vetorNaoEncontradas[i] + "\n")

    arquivo_saida.close()


def arvore_avl():
    random.seed(time.time())
    arv = ArvoreAVL()
    nomeArquivo = "dadosOrdenados500.txt"

    with open(os.path.join("Arquivos Entrada", nomeArquivo), 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                registro_temp = retornaTipoReg(linha)
                arv.raiz = arv.inserir(arv.raiz, registro_temp)

    vetorEncontradas = []
    vetorNaoEncontradas = []
    totalPresente = 0
    totalAusente = 0
    gerouTodas = False

    while not gerouTodas:
        chaveAleatoria = random.randint(0, 19999) if totalAusente < 15 else random.randint(0, 9999)
        arv.numero_interacoes = 0

        start_time = time.time()
        resultadoChaveEncontrada = arv.buscar(arv.raiz, chaveAleatoria)
        elapsed_time = time.time() - start_time

        if resultadoChaveEncontrada:
            if totalPresente < 15:
                vetorEncontradas.append(f"Chave ({chaveAleatoria:06}) encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arv.numero_interacoes}")
                totalPresente += 1
        else:
            if totalAusente < 15:
                vetorNaoEncontradas.append(f"Chave ({chaveAleatoria:06}) não encontrada na árvore. Tempo de busca: {elapsed_time:.9f} segundos. Interações: {arv.numero_interacoes}")
                totalAusente += 1

        gerouTodas = (totalAusente == 15) and (totalPresente == 15)

    with open(os.path.join("Arquivos Saida", "avl", f"arquivo_saida_{nomeArquivo}"), 'w') as arquivo_saida:
        for linha in vetorEncontradas:
            arquivo_saida.write(linha + "\n")
        for linha in vetorNaoEncontradas:
            arquivo_saida.write(linha + "\n")
