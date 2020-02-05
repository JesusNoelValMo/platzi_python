countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina':43,
    'chile':18,
    'peru':31
}
def main():
    while True:
        country = input("Escribe el nombre de un pais: ").lower()
        try:
            print("La poblacion de {} es: {} millones".format(country, countries[country]))
        except KeyError:
            print("No tenemos el dato de la poblacion de {}".format(country))


if __name__ == '__main__':
    main()
