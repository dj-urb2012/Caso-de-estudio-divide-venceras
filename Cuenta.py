class Transaccion:
    def __init__(self, tipo, monto):
        self.Tipo = tipo
        self.Monto = monto

class Cuenta:
    def __init__(self, nombreUsuario, numTarjeta, pin, saldo):
        self.NombreUsuario = nombreUsuario
        self.NumeroTarjeta = numTarjeta
        self.Pin = pin
        self.Saldo = saldo
        self.ListaTransacciones = []
    
    def agregarHistorial(self, transaccion):
        self.ListaTransacciones.append(transaccion)
    
    def mostrarHistorial(self):
        for transaccion in self.ListaTransacciones:
            print("=========================")
            print(f"Tipo de transaccion: {transaccion.Tipo}")
            print(f"Monto: {transaccion.Monto}")

#Contiene todas las cuentas
class RepositorioCuentas:
    def __init__(self):
        self.repositorio = {}

    def agregarCuenta(self, cuenta):
        self.repositorio[cuenta.NumeroTarjeta] = cuenta