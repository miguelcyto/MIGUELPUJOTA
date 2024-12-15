class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # Atributos privados (por convención con doble guión bajo)
        self.__titular = titular  # Solo accesible dentro de la clase
        self.__saldo = saldo_inicial  # Solo accesible dentro de la clase
        self.__historial_transacciones = []  # Lista privada de transacciones

    # Métodos públicos para interactuar con los atributos privados
    def depositar(self, monto):
        """Método para realizar un depósito"""
        if monto > 0:
            self.__saldo += monto
            self.__registrar_transaccion("Depósito", monto)
            return True
        return False

    def retirar(self, monto):
        """Método para realizar un retiro"""
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            self.__registrar_transaccion("Retiro", -monto)
            return True
        return False

    def consultar_saldo(self):
        """Método público para consultar el saldo"""
        return self.__saldo

    def obtener_titular(self):
        """Método público para obtener el nombre del titular"""
        return self.__titular

    def __registrar_transaccion(self, tipo, monto):
        """Método privado para registrar transacciones"""
        transaccion = {
            "tipo": tipo,
            "monto": monto
        }
        self.__historial_transacciones.append(transaccion)

    def ver_historial_transacciones(self):
        """Método público para ver el historial de transacciones"""
        return self.__historial_transacciones.copy()  # Devuelve una copia para evitar modificaciones directas

# Ejemplo de uso
def main():
    # Crear una cuenta bancaria
    mi_cuenta = CuentaBancaria("MIGUEL PUJOTA", 800)

    # Interacción a través de métodos públicos
    print(f"Titular: {mi_cuenta.obtener_titular()}")
    print(f"Saldo inicial: {mi_cuenta.consultar_saldo()}")

    # Realizar depósitos y retiros
    mi_cuenta.depositar(400)
    mi_cuenta.retirar(100)

    print(f"Saldo actual: {mi_cuenta.consultar_saldo()}")

    # Ver historial de transacciones
    print("Historial de transacciones:")
    for transaccion in mi_cuenta.ver_historial_transacciones():
        print(f"{transaccion['tipo']}: {transaccion['monto']}")

    # Intentar acceder a atributos privados (esto generará un error)
    try:
        print(mi_cuenta.__saldo)  # Esto causará un error de AttributeError
    except AttributeError as e:
        print("Error: No se puede acceder directamente a los atributos privados")

if __name__ == "__main__":
    main()