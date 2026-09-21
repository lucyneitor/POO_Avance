from paciente import Paciente #1°archivo_nom 2°clase_nom

def main(): #siempre
    p1 = Paciente("16.218.436-9","Luis Arriagada",40,"Isapre")
    print(p1)

if __name__ == "__main__": #archivo si lo usara como import (yo lo ejecute)
    main() #para evitar que al import se ejecute solo es la condicion