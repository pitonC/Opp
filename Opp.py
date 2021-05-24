
class Empleado():
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

        #crea objeto

        emp1 = Empleado("harshit", 22, 1000, 1234)  # creating objects
        emp2 = Empleado("arjun", 23, 2000, 2234)
        print(emp1.__dict__)  #imprime


#---------------------------Herencia---------------------------
class Empleado1(): #clase padre
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class EmpleadoHijo(Empleado1): #clase hijo
    def __init__(self, name, age, salary, id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
        emp1 = Empleado1('harshit', 22, 1000)

        print(emp1.age)

#---------------------------Polimorfismo-----------------------
class Empleado():
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id


def earn(self):
    pass


class EmpleadoHijo1(Empleado):

    def earn(self):
        print("no dinero")


class EmpleadoHijo2(Empleado):

    def earn(self):
        print("tiene dinero")


c = EmpleadoHijo1
c.earn(Empleado)
d = EmpleadoHijo2
d.earn(Empleado)

#-------------------------Encapsulamiento-------------------------
class Empleado(object):
    def __init__(self):
        self.name = 1234
        self._age = 1234
        self.__salary = 1234

        object1 = Empleado()
        print(object1.name)
        print(object1._age)
        print(object1.__salary)

#--------------------------Abstraccion----------------------------
from abc import ABC, abstractmethod


class Empleado(ABC):
    def emp_id(self, id, name, age, salary):
        pass

class EmpleadoHijo1(Empleado):
    def emp_id(self, id):

        print("emp_id es 12345")
        emp1 = EmpleadoHijo1()
        emp1.emp_id(id)






