#   esto es un tuple
mi_tuple = (1,2,3,4)



#   mostrar tipo de dato
print("mostrar tipo de dato")
print(type(mi_tuple))



#   almacenamiento
t = (95, 9.5, "hola mundo")
print("demostracion de los valores que puede almacenar un tuple")
print(t)



#   mostrar valores especificos
print("mostrar valores especificos almacenados en el tuple")
print(mi_tuple[0])
print("mostrar valores especificos almacenados en el tuple pero a la inversa")
print(mi_tuple[-2])


#   configurar tuple
print("un tuple dentro de otro tuple")
mi_tuple = (1,2,(10,20),4)
print(mi_tuple)
#   mostrar un valor en especifico
print("mostrar un tuple especifico dentro del otro tuple especifico")
print("ejemplo: del tuple anterior en el tuple de indice 2 mostrar el tuple de indice 0, tumple 10 a tuple 10 (2 a 0)")
print(mi_tuple[2][0])


#   reajustar variable a otro tipo
print("reajustar el tuple a otro tipo de dato")
mi_tuple = list(mi_tuple)
print(type(mi_tuple))



#   jugar con los valores
print("asignamos un valor a otras variables solo si los valores y las variables tienen la misma cantidad, ejemplo 3 a 3")
t = (1,2,3)

x,y,z = t

print(x,y,z)

print("mostrar la numero de valores almacenados")
#   cantidad de valores almacenados
print(len(t))

print("mostrar cuantas veces aparece un solo valor en el tuple")
#   contar cuantos valores
print(t.count(1))

print("buscar un valor desde el indice")
#   buscar valores
print(t.index(2))