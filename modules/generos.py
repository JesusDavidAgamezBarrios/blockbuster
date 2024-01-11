from utils.utils import load_json, save_json

def new_genero():
    generos = load_json()  # Esto debería devolver una lista

    genero = {}
    genero["id"]= input("Ingrese el id del genero: ")
    genero["nombre"]= input("Ingrese el nombre del genero: ")
    genero["sinopsis"]= input("Ingrese la sinopsis del genero: ")
    genero["actor"]= input("Ingrese el actor del genero: ")
    genero["formato"]= input("Ingrese el formato del genero: ")

    generos.append(genero)  # Agrega el nuevo genero a la lista de generos
    save_json(generos)  # Guarda la lista actualizada de generos

def list_genero():
    generos = load_json  # 

    for genero in generos:
        print("id: ", genero["id"])
        print("nombre: ", genero["nombre"])
        print("sinopsis: ", genero["sinopsis"])
        print("actor: ", genero["actor"])
        print("formato: ", genero["formato"])
        print("")