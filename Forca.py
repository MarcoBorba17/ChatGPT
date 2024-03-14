import random

def escolher_palavra():
    """
    Escolhe uma palavra aleatória da lista e a converte para maiúsculas.
    """
    palavras = ['python', 'java', 'javascript', 'programacao', 'hacker']
    return random.choice(palavras).upper()

def inicializar_display(palavra_secreta):
    """
    Inicializa a lista de exibição da palavra oculta.
    """
    return ['_' for _ in palavra_secreta]

def imprimir_display(palavra_display):
    """
    Imprime a palavra oculta atualizada.
    """
    print(' '.join(palavra_display))

def imprimir_boneco(chances):
    """
    Imprime o boneco da forca de acordo com as chances restantes.
    """
    boneco = [
        "  ____ ",
        " |    |",
        " |",
        " |",
        " |",
        " |",
        "_|_"
    ]

    if chances <= 5:
        boneco[2] = " |    O"
    if chances <= 4:
        boneco[3] = " |    |"
    if chances <= 3:
        boneco[3] = " |   /|"
    if chances <= 2:
        boneco[3] = " |   /|\\"
    if chances <= 1:
        boneco[4] = " |   /"
    if chances == 0:
        boneco[4] = " |   / \\"

    for linha in boneco:
        print(linha)

def jogar_jogo():
    """
    Função principal para jogar o Jogo da Forca.
    """
    palavra_secreta = escolher_palavra()
    palavra_display = inicializar_display(palavra_secreta)
    chances = 6

    print('Bem-vindo ao Jogo da Forca!')

    while chances > 0 and '_' in palavra_display:
        imprimir_boneco(chances)
        imprimir_display(palavra_display)

        palpite = input('Digite uma letra ou chute a palavra inteira: ').upper()

        if len(palpite) == 1:
            if palpite in palavra_secreta:
                # Revela a letra na palavra_display
                for index, letra in enumerate(palavra_secreta):
                    if letra == palpite:
                        palavra_display[index] = letra
            else:
                # Reduz as chances se a letra não estiver na palavra
                chances -= 1
                print(f'Letra incorreta. Você tem {chances} chances restantes.')
        else:
            if palpite == palavra_secreta:
                palavra_display = list(palavra_secreta)
            else:
                chances -= 1
                print(f'Palavra incorreta. Você tem {chances} chances restantes.')

    # Imprime o resultado final
    imprimir_boneco(chances)
    imprimir_display(palavra_display)

    if '_' not in palavra_display:
        print('Parabéns, você ganhou!')
    else:
        print(f'Você perdeu! A palavra era: {palavra_secreta}')

if __name__ == "__main__":
    jogar_jogo()
https://github.com/MarcoBorba17/ChatGPT.git
