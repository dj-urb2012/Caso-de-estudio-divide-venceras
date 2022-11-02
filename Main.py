from Cuenta import Cuenta, RepositorioCuentas
from FuncionesCajero import *
from os import system as terminal
from time import sleep

#Comandos de cmd
pausar = "pause"
limpiar = "cls"

#Caso de estudio - Divide y venceras por Diego Urbina

#Cuentas de prueba
cuenta1 = Cuenta("Dayer Phillip", "1234-5678-8900-0000", "7845", 1000)
cuenta2 = Cuenta("Camilo Solis", "1000-1234-5678-9010", "7942", 5000)
cuenta3 = Cuenta("Andrew Morales", "5689-2023-7151-0000", "5248", 10000)

#Repositorio de cuentas
repositorio = RepositorioCuentas()
#Se agregan 3 cuentas de prueba
repositorio.agregarCuenta(cuenta1)
repositorio.agregarCuenta(cuenta2)
repositorio.agregarCuenta(cuenta3)

def main():
    terminal(limpiar)
    global repositorio, numTarjeta
    opcion = 0
    sesionIniciada = iniciarSesion(repositorio)
    if sesionIniciada is True:
        cuenta = obtenerCuenta(repositorio)
        while opcion != 5:
            terminal(limpiar)
            print(f"Bienvenido {cuenta.NombreUsuario}, seleccione una opcion")
            opcion = menu()
            if opcion == 1:
                terminal(limpiar) 
                depositar(cuenta)
                print("Procesando transaccion")
                sleep(2)
            elif opcion == 2: 
                terminal(limpiar)
                retiro(cuenta)
                print("Procesando transaccion")
                sleep(2)
            elif opcion == 3: 
                terminal(limpiar)
                verSaldo(cuenta.Saldo)
                terminal(pausar)
            elif opcion == 4:
                terminal(limpiar)
                cuenta.mostrarHistorial()
                terminal(pausar)
            elif opcion == 5:
                guardarDatos(repositorio, cuenta)
                print("Buen dia")
                main ()
            else: print("Opcion invalida")
    elif sesionIniciada is None:
        print("Tarjeta en mal estado o vencida")
        terminal(pausar)
        main()
    else:
        print("El pin es incorrecto, por favor intente de nuevo")
        terminal(pausar)
        main()

main()