import time
import os


agenda = {}
booleano = True
def borrarPantalla():
    if os.name == "posix":
        var = "clear"       
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    return os.system(var)

print("Bienvenido a la agenda")

while booleano:
    print("¿Qué desea realizar?")
    print("1 - Agendar contacto")
    print("2 - Buscar en la agenda")
    print("3 - Ver agenda")
    print("4 - Salir")
    
    op = int(input("Seleccione la opción correspondiente\n"))

    if op == 1:
        nombre = str(input("Ingrese el nombre de su contacto\n")).capitalize()
        tel = int(input(f'Ingrese el número telefónico de {nombre}\n'))
        agenda[nombre] = tel 
        input("Presione Enter para volver al menú")
        borrarPantalla()      

    elif op == 2:
        contador = 0
        
        busca = str(input("Ingrese el nombre que desea buscar\n")).capitalize()
        for clave, valor in agenda.items():
            verificador = True
            iterancia = 0
            
            if clave.startswith(busca):
                print(f'{clave} ------> {valor}')
                contador += 1
                
        if contador == 0:
           print("No se han encontrado coincidencias")

        input("Presione Enter para volver al menú")
        borrarPantalla()
            

    elif op == 3:
        for clave, valor in agenda.items():
            print(f'{clave} ------> {valor}')
            
        input("Presione Enter para volver al menú")
        borrarPantalla()
            
    elif op == 4:
        print("Ha salido del programa")
        booleano = False
        time.sleep(5)
        borrarPantalla()

    else: 
        print("No ha ingresado un valor correcto")
        time.sleep(5)
        borrarPantalla()



