texto = "ABCDEFGHIJKLM"
fragmento = texto[2]

print(fragmento)

# desde un indice a otro indice
fragmento = texto[2:5]

print(fragmento)


# desde el comienzo del string hasta el indice indicado
fragmento = texto[:5]

print(fragmento)



# desde un indice a otro indice salteando 
fragmento = texto[2:10:2]
print("ABCDEFGHIJKLM")
print("--CD--G-I--")
print(fragmento)



# salteando de 3
fragmento = texto[::3]

print(fragmento)



# mostrar toda la cadena de caracteres al reves o iniciando desde fin a inicio
fragmento = texto[::-1]

print(fragmento)