def mergeSort(lista):
    if len(lista) < 2:
        return lista
    else:
        middle = len(lista) // 2
        right = mergeSort(lista[:middle])
        left = mergeSort(lista[middle:])
        return merge(right, left)


def merge(lista1, lista2):
    i, j = 0, 0
    result = []  # Lista vacía

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i].getEdad() < lista2[j].getEdad()):  # Ordena en funión de la edad
            result.append(lista1[i])  # Se añade el objeto a la lista
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]
    return result  # Se devuelve la lista
