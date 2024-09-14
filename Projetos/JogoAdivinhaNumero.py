from random import randint

segredo = randint(1, 100)
contador_jogadas = 0
print(
    """
      -------  Jogo de acerte o numero -------
      O computador escolheu um numero entre 1 e 100
      tente acertar o numero com o menor numero de jogadas
      """
)
while True:

    chute = int(input("Digite um numero:"))
    contador_jogadas += 1
    if chute == segredo:
        print(f" voce acertou em {contador_jogadas} tentativas")
        break
    else:
        print(f"Errou ! - tentativa {contador_jogadas}")
        if chute > segredo:
            print(f"Numero menor que {chute}")
        else:
            print(f"Numero maior que  {chute}")
