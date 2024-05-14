"""
Arquivo que contém a estrutura de dados árvore binária
"""


class Tiporeg:
    def __init__(self, chave: int, dado1: int, dado2: str) -> None:
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


def retorna_tipo_reg(s) -> Tiporeg:
    """_summary_

    Args:
        s (_type_): _description_

    Returns:
        Tiporeg: _description_
    """
    registro = Tiporeg(0, 0, "")

    aux = s.split(";")
    registro.chave = int(aux[0])
    registro.dado1 = int(aux[1])
    registro.dado2 = aux[2]
    return registro
