
def menu_Principal():
    print("Sistema Gestor de Peliculas BlockBuster")
    print("1.Administrador de Generos")
    print("2.administrador de Actores")
    print("3.administrador de Formatos")
    print("4. Gestor de Informes")
    print("5.Gestor de peliculas")
    print("6. Salir")
    opcion = input("Ingrese una opcion: ")
    return opcion

def menu_Generos(new_genero, list_genero):
    while True:
        print("1.crear Generos")
        print("2.Listar Generos")
        print("3.ir al menu principal")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            new_genero()
        elif opcion == "2":
            list_genero()
        elif opcion == "3":
            break
        else:
            print("Opcion incorrecta")

def menu_Actores(new_actor, list_actor):
    while True:
        print("1.crear Actores")
        print("2.Listar Actores")
        print("3.ir al menu principal")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            new_actor()
        elif opcion == "2":
            list_actor()
        elif opcion == "3":
            break
        else:
            print("Opcion incorrecta")

def menu_Formatos(new_formato, list_formato):
    while True:
        print("1.crear Formatos")
        print("2.Listar Formatos")
        print("3.ir al menu principal")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            new_formato()
        elif opcion == "2":
            list_formato()
        elif opcion == "3":
            break
        else:
            print("Opcion incorrecta")

def menu_Informes(new_informe, list_informe, informe_genero, informe_actor, informe_pelicula):
    while True:
        print("1.crear Informes")
        print("2.Listar Informes")
        print("3.Informe por Genero")
        print("4.Informe por Actor")
        print("5.Informe por Pelicula")
        print("6.ir al menu principal")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            new_informe()
        elif opcion == "2":
            list_informe()
        elif opcion == "3":
            informe_genero()
        elif opcion == "4":
            informe_actor()
        elif opcion == "5":
            informe_pelicula()
        elif opcion == "6":
            break
        else:
            print("Opcion incorrecta")

def menu_Peliculas(new_pelicula, list_pelicula):
    while True:
        print("1.crear Peliculas")
        print("2.Listar Peliculas")
        print("3.ir al menu principal")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            new_pelicula()
        elif opcion == "2":
            list_pelicula()
        elif opcion == "3":
            break
        else:
            print("Opcion incorrecta")