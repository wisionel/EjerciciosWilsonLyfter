countries=["Costa Rica","China","Canada"]
city=["San Jose","Beijing","Toronto"]
my_dictionary={}

for pair in range(len(countries)):
    country=countries[pair]
    capital=city[pair]
    my_dictionary[country]=capital

print(my_dictionary)