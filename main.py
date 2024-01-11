from modules.actores import new_actor, list_actor
from modules.formatos import new_formato, list_formato
from modules.peliculas import new_pelicula, list_pelicula
from modules.gestorInformes import informe_genero, informe_actor, informe_pelicula, formato_tipo
from modules.generos import new_genero, list_genero
from modules.menus import menu_Generos, menu_Actores, menu_Formatos, menu_Informes, menu_Peliculas, menu_Principal

def main():
    while True:
        opcion = menu_Principal()
        if opcion == "1":
            menu_Generos(new_genero, list_genero)
        elif opcion == "2":
            menu_Actores(new_actor, list_actor)
        elif opcion == "3":
            menu_Formatos(new_formato, list_formato)
        elif opcion == "4":
            menu_Informes (informe_genero, informe_actor, informe_pelicula, formato_tipo)
        elif opcion == "5":
            menu_Peliculas(new_pelicula, list_pelicula)
        elif opcion == "6":
            break
        else:
            print("Opcion incorrecta")

if __name__ == "__main__":
    main()