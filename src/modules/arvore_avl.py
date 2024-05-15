# Classe que define um nó da árvore AVL.
class NoAVL:
    def __init__(self, chave, dado1, dado2):
        self.chave = chave       # Chave do nó
        self.dado1 = dado1       # Primeiro dado (valor inteiro)
        self.dado2 = dado2       # Segundo dado (combinação de letras)
        self.esquerda = None     # Filho à esquerda
        self.direita = None      # Filho à direita
        self.altura = 1          # Altura do nó (inicializada como 1)

# Função auxiliar para obter a altura de um nó.
def obter_altura(no):
    if no is None:
        return 0
    return no.altura

# Função auxiliar para obter o fator de balanceamento de um nó.
def obter_fator_balanceamento(no):
    if no is None:
        return 0
    return obter_altura(no.esquerda) - obter_altura(no.direita)

# Função auxiliar para fazer a rotação simples à direita.
def rotacao_direita(y):
    if y is None or y.esquerda is None:
        return y

    x = y.esquerda
    T2 = x.direita

    x.direita = y
    y.esquerda = T2

    y.altura = 1 + max(obter_altura(y.esquerda), obter_altura(y.direita))
    x.altura = 1 + max(obter_altura(x.esquerda), obter_altura(x.direita))

    return x

# Função auxiliar para fazer a rotação simples à esquerda.
def rotacao_esquerda(x):
    if x is None or x.direita is None:
        return x

    y = x.direita
    T2 = y.esquerda

    y.esquerda = x
    x.direita = T2

    x.altura = 1 + max(obter_altura(x.esquerda), obter_altura(x.direita))
    y.altura = 1 + max(obter_altura(y.esquerda), obter_altura(y.direita))

    return y

# Função que insere um nó na árvore AVL.
def inserir(raiz, registro):
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

# Classe que define a árvore AVL.
class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, registro):
        self.raiz = inserir(self.raiz, registro)

    def buscar(self, chave):
        no = self._buscar(self.raiz, chave)
        return no

    def _buscar(self, no, chave):
        if no is None:
            return 1, False
        if no.chave == chave:
            return 1, True
        if chave < no.chave:
            return self._buscar(no.esquerda, chave)
        return self._buscar(no.direita, chave)
