
#creamos una funcion con el nombre calcular descuento con los parametros que vamos almacenar
#en este caso total, y asignamos porcentaje de descuento con el 10% que va por defecto en el descuento.
def calcular_descuento(total, porcentaje_descuento=10):
#prodedemos a realizar los calculos correspondientes y que nos deveulva el resultado
    descuento = total - (precio * porcentaje_descuento / 100)
    return descuento
#ingresamos el valor total de la compra (ya no ingresamos en % ya que definimos en la parte superior por defecto)
precio=float(input("INGRESE EL PRECIO DEL PRODUCTO:  "))
#llamamos a nuestra funcion y procedemosa desplegar a pantalla
monto_final = calcular_descuento(precio)
print(f"PRECIO FINAL CON EL 10% DE DESCUENTO ES:{monto_final:.2f}")
print(f"*******************************************************")
print(f"MONTO TOTAL DE COMPRA ES:{precio:.2f}")
print(f"MONTO TOTAL CON DESCUENTO ES:{monto_final:.2f}")

