from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self):
        pass

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.role=None

    def get_role(self,role):
        self.role=role

    def has_permission(self,action):
        if action=="read":
            print(True)
        elif action== "write":
            print(True)
        elif action=="delete":
            print(True)

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.role=None

    def get_role(self,role):
        self.role=role

    def has_permission(self,action):
        if action=="read":
            print(True)
        elif action== "write":
            print(False)
        elif action=="delete":
            print(False)

manager_1=AdminUser("Wilson")
intern_1=RegularUser("Mark")
manager_1.get_role("Manager")
intern_1.get_role("Intern 1")
print(manager_1.role)
print(intern_1.role)
manager_1.has_permission("write")
intern_1.has_permission("write")

