class Person:
    def __init__(self, name="", age=""):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name:{}, age:{}".format(self.name, self.age)




class Employee(Person):
    def __init__(self, name="", age="", salary=""):
        Person.__init__Name:John, age:22,(self, name, age)
        self.salary = salary

    def __str__(self):
        return Person.__str__(self) + ", Salary: " + self.salary


def run_test():
    employee_one = Employee("John", 22, "$60k")
    print(employee_one)


run_test()
