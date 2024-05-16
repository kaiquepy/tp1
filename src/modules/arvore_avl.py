"""
Arquivo que contém a implementação da árvore AVL.
"""


class NoAVL:
    """Class que define um nó da árvore AVL.
    """
    def __init__(self, chave, dado1, dado2):
        self.chave = chave       # Chave do nó
        self.dado1 = dado1       # Primeiro dado (valor inteiro)
        self.dado2 = dado2       # Segundo dado (combinação de letras)
        self.esquerda = None     # Filho à esquerda
        self.direita = None      # Filho à direita
        self.altura = 1          # Altura do nó (inicializada como 1)


def obter_altura(no) -> int:
    """Função auxiliar para obter a altura de um nó.

    Args:
        no (_type_): Recebe um nó da árvore AVL.

    Returns:
        int: Retorna a altura do nó.
    """
    if no is None:
        return 0
    return no.altura


def obter_fator_balanceamento(no) -> int:
    """Função auxiliar para obter o fator de balanceamento de um nó.

    Args:
        no (_type_): Recebe um nó da árvore AVL.

    Returns:
        int: Retorna o fator de balanceamento do nó.
    """
    if no is None:
        return 0
    return obter_altura(no.esquerda) - obter_altura(no.direita)


def rotacao_direita(y) -> NoAVL:
    """Função auxiliar para fazer a rotação simples à direita.

    Args:
        y (_type_): Recebe um nó da árvore AVL.

    Returns:
        NoAVL: Retorna um nó da árvore AVL.
    """
    if y is None or y.esquerda is None:
        return y

    x = y.esquerda
    T2 = x.direita

    x.direita = y
    y.esquerda = T2

    y.altura = 1 + max(obter_altura(y.esquerda), obter_altura(y.direita))
    x.altura = 1 + max(obter_altura(x.esquerda), obter_altura(x.direita))

    return x


def rotacao_esquerda(x) -> NoAVL:
    """Função auxiliar para fazer a rotação simples à esquerda.

    Args:
        x (_type_): Recebe um nó da árvore AVL.

    Returns:
        NoAVL: Retorna um nó da árvore AVL.
    """
    if x is None or x.direita is None:
        return x

    y = x.direita
    T2 = y.esquerda

    y.esquerda = x
    x.direita = T2

    x.altura = 1 + max(obter_altura(x.esquerda), obter_altura(x.direita))
    y.altura = 1 + max(obter_altura(y.esquerda), obter_altura(y.direita))

    return y


def inserir(raiz, registro) -> NoAVL:
    """Função para inserir um registro na árvore AVL.

    Args:
        raiz (_type_): Recebe a raiz da árvore AVL.
        registro (_type_): Recebe o registro a ser inserido na árvore AVL.

    Returns:
        NoAVL: Retorna um nó da árvore AVL.
    """
    if raiz is None:
        return NoAVL(registro.chave, registro.dado1, registro.dado2)

    if registro.chave < raiz.chave:
        raiz.esquerda = inserir(raiz.esquerda, registro)
    else:
        raiz.direita = inserir(raiz.direita, registro)

    raiz.altura = 1 + max(obter_altura(raiz.esquerda), obter_altura(raiz.direita))

    balanceamento = obter_fator_balanceamento(raiz)

    # Casos de desequilíbrio
    if balanceamento > 1:
        if registro.chave < raiz.esquerda.chave:
            return rotacao_direita(raiz)
        else:
            raiz.esquerda = rotacao_esquerda(raiz.esquerda)
            return rotacao_direita(raiz)
    if balanceamento < -1:
        if registro.chave > raiz.direita.chave:
            return rotacao_esquerda(raiz)
        else:
            raiz.direita = rotacao_direita(raiz.direita)
            return rotacao_esquerda(raiz)

    return raiz


class ArvoreAVL:
    """Class que define uma árvore AVL.
    """
    def __init__(self):
        self.raiz = None
        self.numero_interacoes = 0

    def inserir(self, registro) -> None:
        """Função para inserir um registro na árvore AVL.

        Args:
            registro (_type_): Registro a ser inserido na árvore AVL.
        """
        self.raiz = inserir(self.raiz, registro)

    def buscar(self, chave):
        """Função para buscar um registro na árvore AVL.

        Args:
            chave (_type_): Registro a ser buscado na árvore AVL.

        Returns:
            _type_: Retorna o nó da árvore AVL que contém a chave buscada.
        """
        self.numero_interacoes = 0
        no = self._buscar(self.raiz, chave)
        return no

    def _buscar(self, no, chave):
        self.numero_interacoes += 1
        if no is None:
            return self.numero_interacoes, False
        if no.chave == chave:
            return self.numero_interacoes, True
        if chave < no.chave:
            return self._buscar(no.esquerda, chave)
        return self._buscar(no.direita, chave)
