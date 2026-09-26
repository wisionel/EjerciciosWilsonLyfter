from datetime import date

class User:
    date_of_birth=date

    def __init__(self, date_of_birth):
        self.date_of_birth=date_of_birth

    @property
    def age(self):
        today=date.today()
        my_age=today.year-self.date_of_birth.year -((today.month, today.day)<(self.date_of_birth.month, self.date_of_birth.day))
        return my_age

def is_of_age(func):
    def wrapper(user):
        try: 
            if user.age>= 18:
                print("Usuario mayor de edad")
            else:
                raise ValueError()
            func(user)
        except ValueError:
            print("Usuario menor de edad")
            print("No puede comprar alcohol")
    return wrapper

@is_of_age
def buy_alcohol(user):
    usuario=user
    print(f"Puede comprar alcohol")

my_user=User(date(2007,9,9))

buy_alcohol(my_user)
