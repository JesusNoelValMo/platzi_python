import random
def run():
    number_found = False
    min_number = int(input("Elige el numero mas pequeño posible para jugar:"))
    max_number = int(input("Elige el numero mas grande posible para jugar:"))
    random_number = random.randint(min_number,max_number)

    while not number_found:
        number = int(input('intenta un numero entre {} y {}:'.format(min_number, max_number)))
        if number == random_number:
            print('Adivinaste!')
            number_found = True 
        elif number > random_number:

            print('El numero es mas pequeño')
        else:
            print('El numero es mas grande')

if __name__ == '__main__':
    run()
