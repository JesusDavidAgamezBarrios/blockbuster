from utils.utils import load_json, save_json

def informe_genero():
    genero = input("Ingrese el género del informe que desea buscar: ")
    informes = load_json()
    for informe in informes:
        if informe["genero"] == genero:
            print("id: ", informe["id"])
            print("nombre: ", informe["nombre"])
            print("sinopsis: ", informe["sinopsis"])
            print("")

def informe_actor():
    actor = input("Ingrese el actor del informe que desea buscar: ")
    informes = load_json()
    for informe in informes:
        if informe["actor"] == actor:
            print("id: ", informe["id"])
            print("nombre: ", informe["nombre"])
            print("sinopsis: ", informe["sinopsis"])
            print("")

def informe_pelicula():
    pelicula = input("Ingrese la película del informe que desea buscar: ")
    informes = load_json()
    for informe in informes:
        if informe["pelicula"] == pelicula:
            print("id: ", informe["id"])
            print("nombre: ", informe["nombre"])
            print("sinopsis: ", informe["sinopsis"])
            print("")

def formato_tipo():
    tipo = input("Ingrese el tipo de formato que desea buscar: ")
    formatos = load_json()
    formatos = save_json()
    for formato in formatos:
        if formato["tipo"] == tipo:
            print("id: ", formato["id"])
            print("nombre: ", formato["nombre"])
            print("descripcion: ", formato["descripcion"])
            print("tipo: ", formato["tipo"])
            print("")