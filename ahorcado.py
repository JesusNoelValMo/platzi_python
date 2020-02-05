import random 

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
] 
def random_word():
    idx = random.randint(0, len(WORDS)-1)
    return WORDS[idx]
def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('---*---*---*---*---*---*---*---*---*---*---*---*---*---')
def run ():
    word = random_word()
    hidden_word = ['-'] * len(word)
    letters_found = 0
    letters_already_found = []
    check_if_letter_found = False
    tries = 0
    while True :
        display_board(hidden_word,tries)
        current_letter = str(input("Escoge una letra: "))
        idx_found = 0
        if current_letter in letters_already_found:
            print("Ya adivinaste esta letra, intenta con otra.")
        else:
            for letter in word:
                if current_letter == letter:
                    check_if_letter_found = True
                    hidden_word[idx_found] = current_letter
                    if current_letter == letters_already_found:
                        pass
                    else:
                        letters_already_found.append(current_letter)

                    letters_found += 1
                idx_found += 1
            if letters_found == len(word):
                display_board(hidden_word,tries)
                print("Felicidades!, encontraste la palabra correcta!")
                break
            if check_if_letter_found == False:
                tries += 1
                print("Vuelve a intentarlo")
                if tries == len(IMAGES)-1:
                    display_board(hidden_word,tries)
                    print("Mala suerte, la palabra era: {}".format(word))
                    print("FIN DEL JUEGO")
                    break
            check_if_letter_found = False
if __name__ == '__main__':
    print(' A H O R C A D O S')
    run()