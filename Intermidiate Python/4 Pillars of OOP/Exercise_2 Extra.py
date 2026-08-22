from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self,action):
        pass

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.role=None

    def get_role(self,role):
        self.role=role

    def has_permission(self,action):
        if action=="read":
            return True
        elif action== "write":
            return True
        elif action=="delete":
            return True

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.role=None

    def get_role(self,role):
        self.role=role

    def has_permission(self,action):
        if action=="read":
            return True
        elif action== "write":
            return False
        elif action=="delete":
            return False

manager_1=AdminUser("Wilson")
intern_1=RegularUser("Mark")
manager_1.get_role("Manager")
intern_1.get_role("Intern 1")
print(manager_1.role)
print(intern_1.role)
print(manager_1.has_permission("write"))
print(intern_1.has_permission("write"))

