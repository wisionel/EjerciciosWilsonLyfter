my_dictionary={
    "Mexico":"Tacos",
    "USA":"Hamburguer",
    "Costa Rica":"Gallo Pinto",
    "Japan":"Sushi"
}
key=["Mexico","Costa Rica","Japan"]

for country in range(len(key)):
    my_dictionary.pop(key[country])

print(my_dictionary)