"""
Arquivo que contém a implementação da árvore AVL.
"""


class No:
    """Nó da árvore AVL
    """
    def __init__(self, registro):
        self.registro = registro
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    """Class que representa a árvore AVL
    """
    def __init__(self):
        self.raiz = None
        self.numero_interacoes = 0


    def altura(self, no) -> int:
        """Retorna a altura de um nó.

        Args:
            no (_type_): No da árvore.

        Returns:
            int: Altura do nó.
        """
        if no is None:
            return 0
        return no.altura


    def maximo(self, a: int, b: int) -> int:
        """Função que retorna o maior valor entre dois números.

        Args:
            a (int): Primeiro número.
            b (int): Segundo número.

        Returns:
            int: O mair valor entre os dois números.
        """
        return max(a, b)


    def rotacao_direita(self, y: No) -> No:
        """Função que realiza a rotação para a direita.

        Args:
            y (No): Recebe um nó da árvore.

        Returns:
            No: Retorna o nó rotacionado.
        """
        x = y.esquerda
        t = x.direita
        x.direita = y
        y.esquerda = t
        y.altura = self.maximo(self.altura(y.esquerda), self.altura(y.direita)) + 1
        x.altura = self.maximo(self.altura(x.esquerda), self.altura(x.direita)) + 1
        return x


    def rotacao_esquerda(self, x: No) -> No:
        """Função que realiza a rotação para a esquerda.

        Args:
            x (No): Recebe um nó da árvore.

        Returns:
            No: Retorna o nó rotacionado.
        """
        y = x.direita
        t = y.esquerda
        y.esquerda = x
        x.direita = t
        x.altura = self.maximo(self.altura(x.esquerda), self.altura(x.direita)) + 1
        y.altura = self.maximo(self.altura(y.esquerda), self.altura(y.direita)) + 1
        return y


    def fator_balanceamento(self, no):
        """Função que retorna o fator de balanceamento de um nó.

        Args:
            no (_type_): No da árvore.

        Returns:
            _type_: Retorna o fator de balanceamento do nó.
        """
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)


    def inserir(self, no, registro) -> No:
        """Função que insere um registro na árvore

        Args:
            no (_type_): No da árvore.
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
