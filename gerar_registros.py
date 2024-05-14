import random
import string
import time

class Registro:
    def __init__(self, chave, dado1, dado2):
        self.chave = chave
        self.dado1 = dado1
        self.dado2 = dado2

def gerar_registro_aleatorio(chave):
    dado1 = random.randint(0, 999)
    dado2 = ''.join(random.choices(string.ascii_uppercase, k=1000))
    return Registro(chave, dado1, dado2)

def main():
    numero_de_registro_proposto = 100

    for i in range(1, 6):
        random.seed(time.time())

        nome_arquivo = f"dadosOrdenados{numero_de_registro_proposto}.txt"
        nome_arquivo_r = f"dadosDesordenados{numero_de_registro_proposto}.txt"

        with open(nome_arquivo, 'w') as arquivo, open(nome_arquivo_r, 'w') as arquivo_r:
            for chave in range(1, numero_de_registro_proposto + 1):
                registro = gerar_registro_aleatorio(chave)

                arquivo.write(f"{registro.chave};{registro.dado1};{registro.dado2}\n")
                print(f"chave: {registro.chave} dado1: {registro.dado1} dado2: {registro.dado2}")

                chave_desordenada = registro.chave + random.randint(0, 999)
                arquivo_r.write(f"{chave_desordenada};{registro.dado1};{registro.dado2}\n")
                print(f"chave: {chave_desordenada} dado1: {registro.dado1} dado2: {registro.dado2}")

        if numero_de_registro_proposto == 100:
            numero_de_registro_proposto = 500
        elif numero_de_registro_proposto == 500:
            numero_de_registro_proposto = 1000
        elif numero_de_registro_proposto == 1000:
            numero_de_registro_proposto = 5000
        elif numero_de_registro_proposto == 5000:
            numero_de_registro_proposto = 10000

if __name__ == "__main__":
    main()
