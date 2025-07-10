
# debe usar []
mi_set = set([1,2,3,4,5])

print(type(mi_set))

print(mi_set)

# otra forma de crear un set
otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)


# no es posible usar esto:
#   print(mi_set[0])


# no va a mostrar valores dobles por mas que se repitan
mi_set = set([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])
print(mi_set)


# ni va a admitir valores lista dentro de un set ni diccionarios
#   mi_set = set([1,2,3,4,[1,2,3,4],1,2,3,4,5,1,2,3,4,5])



# puede admitir tuples
mi_set = set((1,2,3,(1,2,3),5,1,2,3,4,5,1,2,3,4,5))
print(mi_set)


# funciones
mi_set = set([1,2,3,4,5])

print("longitud del set")
print(len(mi_set))

print("verificar si un valor se encuentra en el set")
print(2 in mi_set)

print("unir sets, los valores repetidos no se muestran")
s1 = {1,2,3}
s2 = {3,4,5,6}

s3 = s1.union(s2)
print(s3)


print("agregar")
s1.add(7)
print(s1)

print("eliminar")
s1.remove(2)
print(s1)


print("descartar")
s1.discard(3)
print(s1)


print("elimina un valor aleatorio")
sorteo = s1.pop()
print(sorteo)


print("limpiar")
s1.clear()
print(s1)