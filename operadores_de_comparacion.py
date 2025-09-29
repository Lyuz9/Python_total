bool = 10 == 25
# el resultado debe ser falso
print(bool)

# otro ejemplo
# el resultado debe ser verdadero porque en ambas partes es 10
bool = 10 == 10
print(bool)

#otro ejemplo pero diferente
color = "blanco" == "negro"
print(color)

# ejemplo con el mismo valor con la diferencia de mayus y minus usando lower
color = "blanco" == "BlanCo".lower()
# debe ser verdadero
print(color)


# ejemplo pero con distintos tipos
string = "100" == 100
print(string)

string = 100.0 == 100
print(string)

string = 100.0 != 100
print(string)

string = 100.0 != 99
print(string)

# ejemplo con operadores mayor menor que
bool = 5>=5
print(bool)
