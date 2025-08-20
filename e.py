class Employee:

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
        self.__salary = 30000

    def display(self):
        return ("Employee name: ", self.name, "\nEmployee idnumber: ", self.idnumber, "\nEmployee salary: ", self.__salary)

class Manager(Employee):

    def __init__(self, name, idnumber):
        Employee.__init__(self, name, idnumber)

    def change_salary(self, salary):
        self.__salary = salary
        return self.__salary

a = Manager("John", 23456)
print(a.display())
print(a.change_salary(31000))

