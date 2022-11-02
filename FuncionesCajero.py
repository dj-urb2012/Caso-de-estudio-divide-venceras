from Cuenta import Transaccion

#Este archivo de Python contiene una serie de funciones
#necesarias para el funcionamiento del ATM

numTarjeta = ""

def menu():
    print("1. Depositar")
    print("2. Retirar")
    print("3. Ver saldos")
    print("4. Historial de transacciones")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion -> "))
    return opcion

def leerTarjeta():
    global numTarjeta
    numTarjeta = input("Ingrese el numero de la tarjeta -> ")

def leerPin():
    pin = input("Ingrese el pin -> ")
    return pin

#Obtiene del repositorio la cuenta ligada a la tarjeta
#Retorna None si no existe
def obtenerCuenta(repo):
    cuenta = repo.repositorio.get(numTarjeta)
    return cuenta

#Retorna True si la persona ingreso el pin correcto
#Retorna False en el caso contrario
def validarUsuario(pin):
    pinIngresado = leerPin()
    if pinIngresado == pin:
        return True
    else: return False

#Lee el numero de tarjeta y el pin para inicar el ATM
def iniciarSesion(repo):
    leerTarjeta()
    cuenta = obtenerCuenta(repo)
    #Si retorna None, la tarjeta probablemente esta en mal estado o vencida
    if cuenta is None: return None
    puedeIniciarSesion = validarUsuario(cuenta.Pin)
    return puedeIniciarSesion

#Operaciones de ATM
def pedirMontoTransaccion():
    monto = int(input("Ingrese el monto -> "))
    return monto
#El monto a depositar debe ser multiplo de 100
def depositar(cuenta):
    try:
        monto = pedirMontoTransaccion()
        if not monto % 100 == 0:
            print("El monto debe ser multiplo de 100")
        cuenta.Saldo += monto
        tran = Transaccion("Deposito", monto)
        cuenta.agregarHistorial(tran)
    except ValueError:
        print("El monto debe ser un entero")
    except Exception:
        print("Ha ocurrido un error")

#Verifica si es posible hacer el retiro
def verificarRetiro(monto, saldoTotal):
    retiro = saldoTotal - monto
    if retiro > 0:
        return True
    else: return False

#El monto a retirar debe ser multiplo de 100 y el balance no puede ser
#0 o negativo
def retiro(cuenta):
    try:
        monto = pedirMontoTransaccion()
        if not monto % 100 == 0:
            print("El monto debe ser multiplo de 100")
            return
        if verificarRetiro(monto, cuenta.Saldo) == False:
            print("Saldo insuficiente")
            return
        cuenta.Saldo -= monto
        tran = Transaccion("Retiro", monto)
        cuenta.agregarHistorial(tran)
    except ValueError:
        print("El monto debe ser un entero")
    except Exception:
        print("Ha ocurrido un error")

def verSaldo(saldo):
    print(f"El saldo de la cuenta es de {saldo}")

#Guardar cambios en el repositorio
def guardarDatos(repo, nuevosDatos):
    repo.repositorio[numTarjeta] = nuevosDatos