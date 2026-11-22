class Game:
    def __init__(self,name):
        self.name=name

    def printer(func):
        def wrapper(self,genre,plataform):
            print(f'Genero:{genre}')
            print(f'Plataforma:{plataform}')
            function=func(self,genre,plataform)
            print(function)
            return function
        return wrapper

    @printer
    def characteristics(self,genre,plataform):
        genre:str
        plataform:str
        self.genre=genre
        self.plataform=plataform


my_game=Game("Halo")
my_game.characteristics("Shooter", "Xbox")
