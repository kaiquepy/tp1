import random
import time
import os

class Tiporeg:
    def __init__(self, chave, dado1, dado2):
        self.chave = chave
        self.dado1 = dado1
        self.dado2 = dado2

class No:
    def __init__(self, registro):
        self.registro = registro
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.numero_interacoes = 0

    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def maximo(self, a, b):
        return max(a, b)

    def rotacaoDireita(self, y):
        x = y.esquerda
        T = x.direita
        x.direita = y
        y.esquerda = T
        y.altura = self.maximo(self.altura(y.esquerda), self.altura(y.direita)) + 1
        x.altura = self.maximo(self.altura(x.esquerda), self.altura(x.direita)) + 1
        return x

    def rotacaoEsquerda(self, x):
        y = x.direita
        T = y.esquerda
        y.esquerda = x
        x.direita = T
        x.altura = self.maximo(self.altura(x.esquerda), self.altura(x.direita)) + 1
        y.altura = self.maximo(self.altura(y.esquerda), self.altura(y.direita)) + 1
        return y

    def fatorBalanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def inserir(self, no, registro):
        if no is None:
            return No(registro)
        if registro.chave < no.registro.chave:
            no.esquerda = self.inserir(no.esquerda, registro)
        elif registro.chave > no.registro.chave:
            no.direita = self.inserir(no.direita, registro)
        else:
            return no

        no.altura = 1 + self.maximo(self.altura(no.esquerda), self.altura(no.direita))
        balance = self.fatorBalanceamento(no)

        if balance > 1 and registro.chave < no.esquerda.registro.chave:
            return self.rotacaoDireita(no)
        if balance < -1 and registro.chave > no.direita.registro.chave:
            return self.rotacaoEsquerda(no)
        if balance > 1 and registro.chave > no.esquerda.registro.chave:
            no.esquerda = self.rotacaoEsquerda(no.esquerda)
            return self.rotacaoDireita(no)
        if balance < -1 and registro.chave < no.direita.registro.chave:
            no.direita = self.rotacaoDireita(no.direita)
            return self.rotacaoEsquerda(no)
        return no

    def buscar(self, no, chave):
        if no is None:
            return False
        if chave < no.registro.chave:
            self.numero_interacoes += 1
            return self.buscar(no.esquerda, chave)
        elif chave > no.registro.chave:
            self.numero_interacoes += 1
            return self.buscar(no.direita, chave)
        else:
            return True

def retornaTipoReg(s):
    parts = s.split(';')
    chave = int(parts[0])
    dado1 = int(parts[1])
    dado2 = parts[2]
    return Tiporeg(chave, dado1, dado2)

def main():
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

if __name__ == "__main__":
    main()
