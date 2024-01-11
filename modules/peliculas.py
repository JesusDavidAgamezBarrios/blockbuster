# Description: Funciones de peliculas
from utils.utils import load_json, save_json

def new_pelicula():
    peliculas = load_json()
    pelicula = {}
    pelicula["id"]= input("Ingrese el id de la pelicula: ")
    pelicula["nombre"]= input("Ingrese el nombre de la pelicula: ")
    pelicula["sinopsis"]= input("Ingrese la descripcion de la pelicula: ")
    pelicula["genero"]= input("Ingrese el genero de la pelicula: ")
    pelicula["actor"]= input("Ingrese el actor de la pelicula: ")
    pelicula["formato"]= input("Ingrese el formato de la pelicula: ")
    peliculas.append(pelicula)
    save_json(peliculas)

def list_pelicula():
    peliculas = load_json()
    for pelicula in peliculas:
        print("id: ", pelicula["id"])
        print("nombre: ", pelicula["nombre"])
        print("sinopsis: ", pelicula["sinopsis"])
        print("genero: ", pelicula["genero"])
        print("actor: ", pelicula["actor"])
        print("formato: ", pelicula["formato"])
        print("")
