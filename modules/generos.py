
from utils.utils import load_json, save_json

def new_genero():
    generos = load_json()
    genero = {}
    genero["id"]= input("Ingrese el id del genero: ")
    genero["nombre"]= input("Ingrese el nombre del genero: ")
    genero["sinopsis"]= input("Ingrese la sinopsis del genero: ")
    generos.append(genero)
    save_json(generos)

def list_genero():
    generos = load_json()
    for genero in generos:
        print("id: ", genero["id"])
        print("nombre: ", genero["nombre"])
        print("sinopsis: ", genero["sinopsis"])
        print("")
