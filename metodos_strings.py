
# metodo upper()

texto = "Este es el texto de Gabo"

# el metodo permite tener el texto en mayusculas
resultado = texto.upper()

# podemos añadir el uso de index: resultado = texto[3].upper()

print(resultado)



# metodo lower()

texto = "Este es el texto de Gabo"

# el metodo permite tener el texto en minusculas
resultado = texto.lower()

print(resultado)



# metodo split

texto = "Este es el texto de Gabo"

# el metodo permite tener separar los elementos en una tipo lista
resultado = texto.split()

# podemos usar un elemeto como separador: resultado = texto.split("t")
# ['Es', 'e es el ', 'ex', 'o de Gabo']

print(resultado)



# metodo join

a = "aprender"
b = "Python"
c = "Hola mundo"
d = " ".join([a, b, c])

# el metodo permite tener unir los elementos en una tipo lista
print(d)



# metodo find()

texto = "Este es el texto de Gabo"

# el metodo permite buscar un determinado caracter
resultado = texto.find("s")

print(resultado)



# metodo replace()

texto = "Este es el texto de Gabo"

# el metodo permite remplazar un parametro del texto por otro parametro especificado
resultado = texto.replace("Gabo", "todos")

print(resultado)



# metodo replace()

texto = "PANDA"

# el metodo permite remplazar un parametro del texto por otro parametro especificado
resultado = texto.replace("A", "X")

print(resultado)