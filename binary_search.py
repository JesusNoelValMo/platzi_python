def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False

    mid = int ((low + high) /2)

    if numbers [mid] == number_to_find:
        return True 
    elif numbers [mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
         return binary_search(numbers, number_to_find, mid + 1, high)
if __name__ == '__main__':
    numbers = [1,3,5,6,9,10,11,25,27,28,34,36,49,51, 2, 100]
    numbers.sort()
  
    
    number_to_find = int(input("Ingresa un numero: "))
    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)
    if result == True:
        print("El número sí está en la lista.")

    else:
        print("El número no está en la lista.")
