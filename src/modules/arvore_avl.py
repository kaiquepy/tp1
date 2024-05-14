"""
Arquivo que contém a estrutura de dados árvore avl
"""


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


    def rotacao_direita(self, y):
        x = y.esquerda
        T = x.direita
        x.direita = y
        y.esquerda = T
        y.altura = self.maximo(self.altura(y.esquerda), self.altura(y.direita)) + 1
        x.altura = self.maximo(self.altura(x.esquerda), self.altura(x.direita)) + 1
        return x


    def rotacao_esquerda(self, x):
        y = x.direita
        T = y.esquerda
        y.esquerda = x
        x.direita = T
        x.altura = self.maximo(self.altura(x.esquerda), self.altura(x.direita)) + 1
        y.altura = self.maximo(self.altura(y.esquerda), self.altura(y.direita)) + 1
        return y


    def fator_balanceamento(self, no):
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
        balance = self.fator_balanceamento(no)

        if balance > 1 and registro.chave < no.esquerda.registro.chave:
            return self.rotacao_direita(no)
        if balance < -1 and registro.chave > no.direita.registro.chave:
            return self.rotacao_esquerda(no)
        if balance > 1 and registro.chave > no.esquerda.registro.chave:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
        if balance < -1 and registro.chave < no.direita.registro.chave:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)
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


def retorna_tipo_reg(s):
    parts = s.split(';')
    chave = int(parts[0])
    dado1 = int(parts[1])
    dado2 = parts[2]
    return Tiporeg(chave, dado1, dado2)
