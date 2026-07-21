import heapq


def top3_maker(my_dict):
    new_list=[]
    for student in my_dict:
        new_dict={}
        new_dict["Nombre Completo"]=student["Nombre Completo"]
        new_dict["Nota Promedio"]=float(student["Nota Promedio"])
        new_list.append(new_dict)
    top_3=heapq.nlargest(3,new_list,key= lambda x: x["Nota Promedio"])
    return top_3