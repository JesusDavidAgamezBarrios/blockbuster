from utils.utils import load_json

def informe_genero():
    file_path_informes = "data/informes.json"
    genero = input("Ingrese el género del informe que desea buscar: ")
    informes = load_json(file_path_informes)
    for informe in informes:
        if informe["genero"] == genero:
            print("id: ", informe["id"])
            print("nombre: ", informe["nombre"])
            print("sinopsis: ", informe["sinopsis"])
            print("")

def informe_actor():
    file_path_informes = "data/informes.json"
    actor = input("Ingrese el actor del informe que desea buscar: ")
    informes = load_json(file_path_informes)
    for informe in informes:
        if informe["actor"] == actor:
            print("id: ", informe["id"])
            print("nombre: ", informe["nombre"])
            print("sinopsis: ", informe["sinopsis"])
            print("")

def informe_pelicula():
    file_path_informes = "data/informes.json"
    pelicula = input("Ingrese la película del informe que desea buscar: ")
    informes = load_json(file_path_informes)
    for informe in informes:
        if informe["pelicula"] == pelicula:
            print("id: ", informe["id"])
            print("nombre: ", informe["nombre"])
            print("sinopsis: ", informe["sinopsis"])
            print("")

def formato_tipo():
    file_path_formatos = "data/formatos.json"
    tipo = input("Ingrese el tipo de formato que desea buscar: ")
    formatos = load_json(file_path_formatos)
    for formato in formatos:
        if formato["tipo"] == tipo:
            print("id: ", formato["id"])
            print("nombre: ", formato["nombre"])
            print("descripcion: ", formato["descripcion"])
            print("tipo: ", formato["tipo"])
            print("")