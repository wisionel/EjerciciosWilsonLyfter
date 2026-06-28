import csv
from collections import Counter


def genre_finder(path):
    with open(path,'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        genre_list=[]
        for line in reader:
            genre_list.append(line["Genero"])
        count=Counter(genre_list)   
        return count
    

def main(path):
    genre_quantity=genre_finder(path)
    sorted_dict=dict(sorted(genre_quantity.items()))
    print(f"Estos fueron los generos encontrados:")
    for genre,quantity in sorted_dict.items():
        print(f"{genre}:{quantity}")


main("Video game list.csv")
                                        