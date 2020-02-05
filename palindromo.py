def palindrome(word):
    reversed_lettters = []
    for letter in word :
        reversed_lettters.insert(0, letter)
    reversed_word = "".join(reversed_lettters)
    if reversed_word == word:
        return True
    else:
        return False

def palindrome2(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True 
    else:
        return False

if __name__ == '__main__':
    word = str(input("Escribe una palabra: "))

    result = palindrome2(word)
    if result == True:
        print("{} sí es un palíndromo.".format(word))
    else:
        print("{} no es un palíndromo.".format(word))

