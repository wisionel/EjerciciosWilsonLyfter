def list_creator(words):
    my_list=words.split("-")
    return my_list


def list_sorter(list):
    list.sort()
    return list


def list_creator_sorter(strings):
    new_list=list_creator(strings)
    alphabetical_list=list_sorter(new_list)
    alphabetical_string="-".join(alphabetical_list)
    print(alphabetical_string)

my_string="Queso-Arroz-Pan-Huevo"
list_creator_sorter(my_string)
