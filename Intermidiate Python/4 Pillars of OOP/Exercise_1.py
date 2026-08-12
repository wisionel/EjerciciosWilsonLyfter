class BankAccount:
    def __init__(self,balance):
        self.balance=int(balance)

    def _add_money(self,amount):
        self.balance += int(amount) 
        print(f"Se ha agregado {amount} a su cuenta")
        print(f"Estado de cuenta: {self.balance}")
        return self.balance

    def _subtract_money(self,amount):
        self.balance -= int(amount) 
        print(f"Se ha retirado {amount} de su cuenta")
        print(f"Estado de cuenta: {self.balance}")
        return self.balance

class SavingsAccount(BankAccount): 
    def __init__(self,balance,min_balance):
        super().__init__(balance)
        self.min_balance=min_balance

    
    def _subtract_money(self,amount):
        if self.balance - int(amount) < self.min_balance:
            raise Exception()
        elif self.balance > self.min_balance:
            self.balance -= int(amount) 
            print(f"Se ha retirado {amount} de su cuenta")
            print(f"Estado de cuenta: {self.balance}")
        else:
            raise Exception()
        return self.balance

try:
    account_1=SavingsAccount(5000,500)
    account_1._add_money(1000)
    account_1._subtract_money(6000)
    account_1._subtract_money(5500)
        
except Exception:
    print(f"Balance menor que balance minimo")

