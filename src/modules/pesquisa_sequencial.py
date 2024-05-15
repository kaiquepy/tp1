"""
Arquivo que contém a estrutura de dados pesquisa sequencial
"""


class PesquisaSequencial:
    """Class que representa a estrutura de dados pesquisa sequencial
    """
    def __init__(self, nome_do_arquivo: str = None):
        self.nome_do_arquivo = nome_do_arquivo

    def set_nome_do_arquivo(self, nome_do_arquivo: str) -> None:
        """Função que seta o nome do arquivo

        Args:
            nome_do_arquivo (str): Nome do arquivo.
        """
        self.nome_do_arquivo = nome_do_arquivo

    def buscar(self, chave: int) -> tuple:
        """Estrutura de dados de pesquisa sequencial

        Args:
            nome_do_arquivo (str): Nome do arquivo que será feita a pesquisa.
            chave (str): Registro a ser procurado.

        Returns:
            int: Retona o número comparações feitas.
        """
        numero_de_comparacoes = 0

        with open(self.nome_do_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                numero_de_comparacoes = numero_de_comparacoes + 1
                partes = linha.strip().split(";")
                if int(partes[0]) == chave:
                    return numero_de_comparacoes, True

        return numero_de_comparacoes, False
