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


    def buscar(self, chave):
        """Função que busca um registro na árvore

        Args:
            chave (int): Chave a ser buscada.

        Returns:
            bool: Retorna True se a chave foi encontrada, False caso contrário.
        """
        self.numero_interacoes = 0
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no, chave):
        """Função auxiliar recursiva para buscar um registro na árvore

        Args:
            no (No): Nó da árvore.
            chave (int): Chave a ser buscada.

        Returns:
            bool: Retorna True se a chave foi encontrada, False caso contrário.
        """
        if no is None:
            return self.numero_interacoes, False

        if chave < no.registro.chave:
            self.numero_interacoes += 1
            return self._buscar_recursivo(no.esquerda, chave)
        if chave > no.registro.chave:
            self.numero_interacoes += 1
            return self._buscar_recursivo(no.direita, chave)

        return self.numero_interacoes, True
