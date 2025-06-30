x = 10
y = 5


#   antiguo:
print("No practico ->   Mis números son: " + str(x) + " y " + str(y))

#   nueva:
print("Forma legible ->     Mis números son: {} y {}".format(x,y))

#   orden distinto:
print("Forma legible ->     Mis números son: {} y {}".format(y,x))

#   operaciones:
print("operacion ->     Suma de mis números son: {} + {} = {}".format(x,y, x+y))

#   otra forma de operación:
z = x + y
print("otra forma de operación ->     Suma de mis números son: {} + {} = {}".format(x,y,z))


# otros:

color = "rojo"
matricula = "541926"

print("forma practica ->    "f"El auto es {color} y su matrícula es {matricula}")