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
    "0- Isapre\n",
    "1- Fonasa\n",
    "2- Particular \n",
    "3- Otro \n"
    "4- Salir")
    prevision = leer_numero("Ingrese el tipo de seguro (Isapre/Fonasa): ")
    if prevision == 0:
        prevision="Fonasa"
    elif prevision == 1:
        prevision="Isapre"
    elif prevision == 2:
        prevision="Particular"
    elif prevision == 3:
        prevision="Otro"
    else:
       prevision = ""
       print("Opción no válida") 
       return # sale de la funcion para que no se guarde datos
    
    try:
        nuevo_paciente = Paciente(rut,nombre,edad,prevision)
    except (ValueError, TypeError) as e:#el objeto que genero error lo captura e
        print(f"Error al crear paciente: {e}")
        return

    pacientes.append(nuevo_paciente)
    print("Paciente agregado exitosamente")

def imprimir_pacientes() -> None:
    if pacientes: #si hay pacientes pasa esto
        for paciente in pacientes:
            print(paciente)
    else:
        print("No hay pacientes registrados.")

def buscar_paciente()->Paciente | None: #paciente da mayor precision que decir object
    rut=input("Ingrese Rut del paciente a buscar: ")
    for paciente in pacientes:
        if paciente.rut == rut: #paciente.rut viene de la clase paciente property self__rut pido dato
            return paciente
    return None

def imprimir_paciente()->None:
    paciente = buscar_paciente() #retorna el objeto
    if paciente:
        print(paciente)
    else: #si objeto no tiene existencia de valor
        print("Paciente no encontrado.")

def eliminar_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        decision = confirmar_proceso(f"¿Seguro de eliminar a {paciente.nombre}? \n")
        #resp=input(f"¿Seguro de eliminar a {paciente.nombre}? si/no \n")#input no funciona concadenar con comas
        if decision:
            pacientes.remove(paciente)
            print("Paciente Eliminado")
        else:
            print("Eliminación cancelada")
    else:
        print("Paciente no encontrado.")

def confirmar_proceso(msg:str)->bool:
    while True:
        resp=input(f"{msg} (si/no)").strip().lower()
        if resp in ("si","no"):
            if resp == "si":
                return True
            else:
                return False
        print("Para seguir el procedimiento debe ingresar 'si o 'no'")

def editar_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        print("Menú edición")
        print("1- Editar nombre")
        print("2- Editar edad")
        print("3- Editar previsión")
        op = leer_numero("Seleccione una opción: ")

        msg="Edición cancelada"
        if op == 1:
            print(f"Nombre actual: {paciente.nombre}")
            nombre = input("Ingrese nuevo nombre: ")
            decision = confirmar_proceso(f"¿Confirma el cambio ({paciente.nombre} ---> {nombre})?")
            if decision:
                paciente.nombre = nombre #nombre.setter
            else:
                print(msg)
        elif op == 2:
            print(f"Edad actual: {paciente.edad}")
            edad = leer_numero("Ingrese nuevo edad: ")
            decision = confirmar_proceso(f"¿Confirma el cambio ({paciente.edad} ---> {edad})?")
            if decision:
                paciente.edad = edad #edad.setter
            else:
                print(msg)
        elif op == 3:
            print(f"La previsión actual es: {paciente.prevision}")
            print("Previsiones disponibles: \n"
                  "1- Fonasa \n"
                  "2- Isapre \n"
                  "3- Particular \n"
                  "4- Otro")
            prevision = leer_numero("Seleccione una prevision: ")
            if prevision == 0:
                prevision="Fonasa"
            elif prevision == 1:
                prevision="Isapre"
            elif prevision == 2:
                prevision="Particular"
            elif prevision == 3:
                prevision="Otro"
            else:
                print("No se realizaron cambios en la previsión")
            paciente.prevision = prevision #prevision.setter
    else:
        print("Paciente no encontrado.")

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
                editar_paciente()
                continue
            case 3:
                print("Eliminando paciente")
                eliminar_paciente()
                continue
            case 4:
                print("Imprimiendo paciente")
                imprimir_paciente()
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

