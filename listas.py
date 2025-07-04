mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]

# imprime solo el valor con el indice indicado, ejem: 0 = "a"
resultado = mi_lista[0]

# imprime solo los valores con los indicies indicaddos, ejem: del intice 0 a 2
resultado2 = mi_lista[0:2]

# podemos mostrar 2 listas de diferentes variables en una sola como si fuera una suma
mi_lista3 = mi_lista + mi_lista2

# muestra el tipo de dato
print(type(mi_lista))

# muestra los valores que tiene la lista
print(len(mi_lista))

# imprime solo el valor con el indice indicado, ejem: 0 = "a"
print(resultado)

# imprime solo los valores con los indicies indicaddos, ejem: del intice 0 a 2
print(resultado2)

# podemos mostrar 2 listas de diferentes variables en una sola como si fuera una suma
print(mi_lista3)

# podemos sobreescribir un valor especificando el indice de dicho valor
mi_lista3[0] = "alfa"
print(mi_lista3)

# podemos añadir un nuevo valor especificando la lista
mi_lista3.append("g")
print(mi_lista3)

# podemos eliminar todos los valores a excepcion de los valores especificados segun el indice
eliminado = mi_lista3.pop(0)
print(eliminado)

# podemos organizar los valores a - z
lista_desorden = ["g","o","b","m","c"]
lista_desorden.sort()
print(lista_desorden)

# podemos organizar los valores al revez z - a 
lista_desorden.reverse()
print(lista_desorden)
