from ManejoArchivo.manejoArchivo import lecturaArchivo as lA  # Importación de la clase para leer el archivo
from Ejecutor.persona import persona as P  # Importación de la clase persona
from Ejecutor.ordenamiento import mergeSort  # Importación del metodo de ordenamiento

m = lA("Archivo/ejemplo.txt")  # Lectura del archivo creando un objeto
listaPersonas = []  # Lista vacía
persona = m.obtenerInformacion()  # Lectura de la información del archivo
persona = [l.split(";") for l in persona]  # Separación de los elementos
for l in persona:  # Eliminación de los saltos de línea
    l[2] = l[2].replace("\n", "")

for l in persona:  # Asignación de valores a los atributos de los objetos persona
    p = P(l[0], l[1], l[2])
    listaPersonas.append(p)  # El objeto se añade a la lista vacía
for l in listaPersonas:  # Se presenta la lista sin ordenar
    print(l)

sort = mergeSort(listaPersonas)  # Se procede a crear un objeto para ordenar la lista
print("\n\n")
for l in sort:  # Se imprime la lista ordenada
    print(l)
