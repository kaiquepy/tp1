"""
Arquivo que contém a estrutura de dados pesquisa sequencial
"""

def pesquisa_sequencial(nome_do_arquivo: str, chave: str) -> int:
    """Estrutura de dadas de pesquisa sequencial

    Args:
        nome_do_arquivo (str): Nome do arquivo que será feita a pesquisa
        chave (str): Registro a ser procurado

    Returns:
        int: Retona o número comparações feitas
    """
    numero_de_comparacoes = 0

    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            numero_de_comparacoes = numero_de_comparacoes + 1
            partes = linha.strip().split(",")
            if partes[0] == chave:
                print(f'chave encontrada na linha {linha}')

    return numero_de_comparacoes
