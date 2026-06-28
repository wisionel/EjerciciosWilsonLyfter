def backward_string(string):
    new=[]
    for letter in range(len(string)-1,-1,-1):
        backward=string[letter]
        new.append(backward)
    backward_word="".join(new)
    print(backward_word)
    return backward_word

my_string="Wilson"
another_string="Cindy"

backward_string(my_string)
