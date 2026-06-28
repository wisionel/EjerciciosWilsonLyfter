import json

def pokemon_name():
    my_name=input("Ingrese nombre de pokemon ")
    return my_name


def pokemon_type():
    my_type=input("Ingrese el tipo de pokemon ")
    return my_type

def pokemon_level():
    my_level=input("Ingrese el nivel del pokemon ")
    return my_level


def pokemon_weight():
    my_weight=float(input("Ingrese el peso del pokemon "))
    return my_weight


def pokemon_shine():
    shine=input("El pokemon es shiny si o no?").upper()
    if shine=="SI":
        shine=True
    elif shine=="NO":
        shine=False
    return shine




def pokemon_item():
    my_item=input("Ingrese el item del pokemon (si no tiene ingrese NA)").upper()
    if my_item=="NA":
        my_item=None
    return my_item    


def pokemon_skills():
    skill_list=[]
    counter=1
    while counter<=4:
        my_skill=input("Ingrese el skill del pokemon ")
        skill_list.append(my_skill)
        counter+=1
    return skill_list



def pokemon_stats():
    my_stats={}
    my_stats["hp"]=int(input("Ingrese el hp del pokemon "))
    my_stats["attack"]=int(input("Ingrese el valor de ataque del pokemon "))
    my_stats["defense"]=int(input("Ingrese el valor de defensa del pokemon "))
    my_stats["sp_attack"]=int(input("Ingrese el valor del ataque especial del pokemon "))
    my_stats["sp_defense"]=int(input("Ingrese el valor de defensa especial del pokemon "))
    my_stats["speed"]=int(input("Ingrese el valor de la velocidad del pokemon "))
    return my_stats


def main(path):
    new_pokemon={}
    new_pokemon["name"]=pokemon_name()
    new_pokemon["type"]=pokemon_type()
    new_pokemon["level"]=pokemon_level()
    new_pokemon["weight_kg"]=pokemon_weight()
    new_pokemon["is_shiny"]=pokemon_shine()
    new_pokemon["held-item"]=pokemon_item()
    new_pokemon["skills"]=pokemon_skills()
    new_pokemon["stats"]=pokemon_stats()

    with open(path,'r',encoding='utf-8') as file:
        content= json.load(file)
        content.append(new_pokemon)

    with open(path,'w',encoding='utf-8') as file:
        json.dump(content,file,indent=2)
    


main("pokemon.json")