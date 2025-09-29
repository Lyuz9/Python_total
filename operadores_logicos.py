bool = 4 < 5 < 6
# mostrara verdadero
print(bool)

bool = 4 < 5 and 5 > 6
# aqui comparamos mas de 2 operadores
# para lograr eso usamos "and" y "or" que vendria siendo "y" o "o"
# tiene que cumplir las dos condiciones para ser verdatero
# como 4 es menor a 5 ahi es verdadero pero del lado de 5 mayor a 6 es falso
print(bool)

bool = 4 < 5 and 5 == 2+3
# aqui si es verdadero porque ambas partes se cumplen
print(bool)

# para comodidad usar parentesis
bool = (4 < 5) and (5 == 2+3)
print(bool)

# ejemplo diferente
bool = (55 == 55) and ("rojo" == "rojo")
print(bool)


# operador OR

bool = 10 == 10 or 3 == 3
# usar or es lo mismo que decir si 10 es igual a 10 o si 3 es igual 3 sin importar si una no lo es
# ejm 1 es igual a 10 "o" 3 es igual a 3 sera verdadero, no cumple con 1 y 10 pero si con 3
# la unica forma de que OR sea falso es que en todas las partes sea falso
print(bool)

bool = 1 == 10 or 13 == 3
# ejem de falso
print(bool)

#ejemplo
text = "hola mundo"
bool = "mundo" in text
print(bool)

# otro ejemplo
text = "hola mundo desde python"
bool = ("hola" in text) and ("python" in text)
print(bool)