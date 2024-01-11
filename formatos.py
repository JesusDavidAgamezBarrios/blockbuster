
from businness.utils.utils import load_json, save_json

def new_formato(file_path_formatos):
    formatos = load_json(file_path_formatos)
    formato = {}
    formato["id"]= input("Ingrese el id del formato: ")
    formato["nombre"]= input("Ingrese el nombre del formato: ")
    formato["sinopsis"]= input("Ingrese la sinopsis del formato: ")
    formato["tipo"]= input("Ingrese el tipo del formato: ")
    formatos.append(formato)
    save_json(file_path_formatos, formatos)

def list_formato(file_path_formatos):
    formatos = load_json(file_path_formatos)
    for formato in formatos:
        print("id: ", formato["id"])
        print("nombre: ", formato["nombre"])
        print("sinopsis: ", formato["sinopsis"])
        print("tipo: ", formato["tipo"])
        print("")