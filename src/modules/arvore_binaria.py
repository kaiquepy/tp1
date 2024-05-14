"""
Arquivo que contém a estrutura de dados árvore binária
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


def novo_no(pRegistro):
    no = No(pRegistro)
    no.esquerda = None
    no.direita = None
    return no


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        self.numero_interacoes = 0


    def inserir(self, no, registro):
        if no is None:
            return novo_no(registro)

        if registro.chave < no.registro.chave:
            no.esquerda = self.inserir(no.esquerda, registro)
        elif registro.chave > no.registro.chave:
            no.direita = self.inserir(no.direita, registro)

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
    aux = Tiporeg(0, 0, "")
    auxS = s
    delimiter = ";"
    pos = s.find(delimiter)
    aux.chave = int(s[:pos])
    aux.dado1 = int(s[pos + 1:])
    pos = s.find(delimiter, pos + 1)
    auxS = s[pos + 1:]
    aux.dado2 = auxS
    return aux
