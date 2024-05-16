"""
Arquivo que contém a estrutura de dados árvore binária
"""


class No:
    """Nó da árvore binária
    """
    def __init__(self, registro):
        self.registro = registro
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    """Class que representa a árvore binária
    """
    def __init__(self):
        self.raiz = None
        self.numero_interacoes = 0


    def inserir(self, registro) -> None:
        """Função que insere um registro na árvore.

        Args:
            registro (_type_): Registro a ser inserido na árvore.
        """
        novo_no = No(registro)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            atual = self.raiz
            while True:
                if novo_no.registro.chave < atual.registro.chave:
                    if atual.esquerda is None:
                        atual.esquerda = novo_no
                        break
                    atual = atual.esquerda
                elif novo_no.registro.chave > atual.registro.chave:
                    if atual.direita is None:
                        atual.direita = novo_no
                        break
                    atual = atual.direita


    def buscar(self, chave) -> tuple:
        """Função que busca um registro na árvore.

        Args:
            chave (_type_): Registro a ser buscado na árvore.

        Returns:
            tuple: Retorna uma tupla com o número de interações e um booleano indicando se a chave foi encontrada.
        """
        atual = self.raiz
        self.numero_interacoes = 0
        while atual is not None:
            self.numero_interacoes += 1
            if chave == atual.registro.chave:
                return self.numero_interacoes, True
            elif chave < atual.registro.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return self.numero_interacoes, False
