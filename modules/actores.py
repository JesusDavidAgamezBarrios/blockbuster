from utils.utils import load_json, save_json

def new_actor(file_path_actores):
    actores = load_json(file_path_actores)
    actor = {}
    actor["id"]= input("Ingrese el id del actor: ")
    actor["nombre"]= input("Ingrese el nombre del actor: ")
    actor["apellido"]= input("Ingrese el apellido del actor: ")
    actor["nacionalidad"]= input("Ingrese la nacionalidad del actor: ")
    actores.append(actor)
    save_json(actores, file_path_actores)

def list_actor(file_path_actores):
    actores = load_json(file_path_actores)
    for actor in actores:
        print("id: ", actor["id"])
        print("nombre: ", actor["nombre"])
        print("apellido: ", actor["apellido"])
        print("nacionalidad: ", actor["nacionalidad"])
        print("")