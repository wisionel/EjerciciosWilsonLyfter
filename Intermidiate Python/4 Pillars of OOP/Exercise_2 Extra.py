from abc import ABC, abstractmethod

class User:
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
        if action=="Read":
            print(True)
        elif action== "Write":
            print(True)
        elif action=="Delete":
            print(True)

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.role=None

    def get_role(self,role):
        self.role=role

    def has_permission(self,action):
        if action=="Read":
            print(True)
        elif action== "Write":
            print(False)
        elif action=="Delete":
            print(False)

manager_1=AdminUser("Wilson")
intern_1=RegularUser("Mark")
manager_1.get_role("Manager")
intern_1.get_role("Intern 1")
print(manager_1.role)
print(intern_1.role)
manager_1.has_permission("Write")
intern_1.has_permission("Write")

