mi_texto = "Esta es una prueba"

#resultado = mi_texto[-9]
resultado = mi_texto.index("prueba") #   "n", "prueba"
r2 = mi_texto.index("a", 5, 12)
# error si se busca algo que no esta en la oración, ejemplo "P" mayuscula no se encuentra

# otro modo es rindex() pero inicia derecha a izquierda 
r3 = mi_texto.rindex("a")
print(resultado)
print(r2)
print(r3)