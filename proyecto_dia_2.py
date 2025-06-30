nombre = input("Nombre del empleado: \n")
venta = input("Ventas realizadas: \n")

print("\n")

calcular_comision = round(int(venta) * 13 / 100, 2)

venta_texto = str(venta)
comision_texto = str(calcular_comision)

print("--------------------------")
print("Nombre del empleado: {}\nVentas realizadas: {}\nComisión: ${}".format(nombre, venta_texto,comision_texto))
print("\n__________________________\n")
print("Datos anisionales \nEmpleado: {}\nVenta: {}\nComisión: {}".format(type(nombre), type(venta), type(calcular_comision)))
print("--------------------------")

