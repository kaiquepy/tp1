"""
Arquivo com funções uteis que podem ser reutilizadas
"""

import time, random, string


def tempo_gasto(funcao):
  def wrapper(*args, **kwargs):
    tempo_inicial = time.time()
    funcao(*args, **kwargs)
    tempo_final = time.time() - tempo_inicial
    print(f'{tempo_final:.6f}')
  return wrapper


def gerar_arquivo(linhas: int, chaves_ordenadas: bool) -> None:
  nome_do_arquivo = f'arquivos_entrada/{linhas}_desordenado.txt'
  chave = random.sample(range(linhas), linhas)

  if chaves_ordenadas:
    nome_do_arquivo = f'arquivos_entrada/{linhas}.txt'
    chave = range(linhas)

  with open(nome_do_arquivo, "w") as arquivo:
    for i in range(linhas):
      dado2 = ''.join(random.choices(string.ascii_uppercase, k=1000))
      linha = f'{chave[i]},12345,{dado2}\n'
      arquivo.write(linha)
