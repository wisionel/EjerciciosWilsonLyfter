class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary

    @property
    def name(self):
        return self.__name
        

    @property
    def salary(self):
        if self.__salary>0:
            return self.__salary
        else:
            print("El salario no puede ser negativo")
        

    @salary.setter
    def salary(self,new_salary):
        if new_salary>0:
            print("Cambiando el salario")
            self.__salary=new_salary
            print(f"El nuevo salario es {self.__salary}")
        else:
            print("El salario no puede ser negativo")

    def promote(self,percentage):
        if self.__salary>0:
            print("Aplicando el porcentaje de promocion")
            decimal=percentage/100
            new_salary=self.__salary+(self.__salary*decimal)
            self.salary=new_salary
            print(f"El salario aumentado es de {new_salary}")
        else:
            print("El salario no puede ser negativo")


employee_1=Employee("Carlos",100)
print(employee_1.name)
print(employee_1.salary)
employee_1.salary=200
employee_1.promote(10)
print(employee_1.salary)