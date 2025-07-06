diccionario = {"c1":"valor1","c2":"valor1"}

#   typo de dato
print(type(diccionario))
print("muestra el tipo de dato: ")
print(diccionario)

#   mostrar un valor especifico
resultado = diccionario["c1"]
print("Especificamos la llave y nos mostrara su valor:")
print(resultado)

#   crear una lista de distintos datos
print("creación de una lista con diferentes datos:")
cliente = {"nombre":"gabo", "apellido":"hernandez", "peso":88, "talla":1.76}

#   mostrar un valor por una llave
print("muestra el valor que tiene la llave de apellido:")
consulta = (cliente["apellido"])
print(consulta)

#   una lista con valores que tienen su propia lista
dic = {"c1":55, "c2":[10, 20, 30], "c3": {"s1":100, "s2":200}}
print("diccionario con subvalores, imprimir llave y especificando el valor a imprimir:")
print(dic["c2"][1])
print(dic["c3"])
print(dic["c3"]["s2"])

#   ajustar datos
dic = {"c1":["a","b","c"],"c2":["d","e","f"]}
print("mostrar el valor de una llave en mayuscula especificando llave y valor:")
print(dic["c2"][1].upper())

#   lista comun
dic = {1:"a",2:"b"}
print("diccionario común:")
print(dic)

#   añadir
print("añadimos una nueva llave con su respectivo valor:")
dic[3] = "c"
print(dic)

#   reescribir
print("sobreescribimos un valor existente, b con B:")
dic[2] = "B"
print(dic)

#   mostrar información
print("mostramos las llaves del diccionario:")
print(dic.keys())

print("mostramos los valores de las llaves:")
print(dic.values())

print("mostramos todos los items del diccionario:")
print(dic.items())