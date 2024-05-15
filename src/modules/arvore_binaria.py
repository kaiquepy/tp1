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


    def inserir(self, no: No, registro) -> No:
        """Função que insere um registro na árvore

        Args:
            no (No): Nó da árvore.
            registro (_type_): Registro a ser inserido.

        Returns:
            No: Retorna o nó inserido.
        """
        if no is None:
            return No(registro)

        if registro.chave < no.registro.chave:
            no.esquerda = self.inserir(no.esquerda, registro)
        elif registro.chave > no.registro.chave:
            no.direita = self.inserir(no.direita, registro)

        return no


    def buscar(self, no: No, chave: int) -> bool:
        """Função que busca um registro na árvore

        Args:
            no (No): No da árvore.
            chave (int): Chave a ser buscada.

        Returns:
            bool: Retorna True se a chave foi encontrada, False caso contrário.
        """
        if no is None:
            return False

        if chave < no.registro.chave:
            self.numero_interacoes += 1
            return self.buscar(no.esquerda, chave)
        if chave > no.registro.chave:
            self.numero_interacoes += 1
            return self.buscar(no.direita, chave)

        return True
