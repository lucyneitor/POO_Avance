from paciente import Paciente #1°archivo_nom 2°clase_nom

pacientes:list[Paciente] = [
        Paciente("11.111.111-1","Luis Arraigada",40,"Isapre"),
        Paciente("16.218.436-9","Paola Pardo",40,"Fonasa")
    ]

def menu() ->None:
    print("Clínica")
    print("1- Agregar paciente")
    print("2- Editar paciente")
    print("3- Eliminar paciente")
    print("4- Imprimir un paciente")
    print("5- Imprimir todos los pacientes")
    print("6- Salir")
    opcion = leer_numero("Seleccione una opción: ")
    return opcion

def leer_numero(mensaje:str) -> int:
    try:
        num=int(input(mensaje))
        return num
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def agregar_paciente()->None:
    rut = input("Ingrese el RUT del paciente: ")
    nombre = input("Ingrese el nombre del paciente: ")
    edad = leer_numero("Ingrese la edad del paciente: ")
    print("Previsones disponibles: \n",
    "1- Isapre\n",
    "2- Fonasa\n",
    "3- Particular \n",
    "4- Otro \n"
    "5- Salir")
    prevision = input("Ingrese el tipo de seguro (Isapre/Fonasa): ")
    if prevision == 0:
        prevision="Fonasa"
    if prevision == 1:
        prevision="Isapre"
    if prevision == 2:
        prevision="Particular"
    if prevision == 3:
        prevision="Otro"
    else:
       prevision = ""
       print("Opción no válida") 
       return # sale de la funcion para que no se guarde datos
    pacientes.append(Paciente(rut, nombre, edad, prevision))

def imprimir_pacientes() -> None:
    if pacientes: #si hay pacientes pasa esto
        for paciente in pacientes:
            print(paciente)
    else:
        print("No hay pacientes registrados.")

def main(): #siempre
    while True:
        op = menu()
        
        match op: #se sale del ciclo despues del primer intento
            case 1: #agregar paciente
                print("Agregando paciente")
                agregar_paciente()
                continue
            case 2: #editar paciente
                print("Editando paciente")
                continue
            case 3:
                print("Eliminando paciente")
                continue
            case 4:
                print("Imprimiendo paciente")
                continue
            case 5:
                print("Imprimiendo todos los pacientes")
                imprimir_pacientes()
                continue
            case 6:
                print("Saliendo del programa")
                break

if __name__ == "__main__": #archivo si lo usara como import (yo lo ejecute)
    main() #para evitar que al import se ejecute solo es la condicion

