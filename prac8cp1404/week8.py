""" to use this just import "from employee imprort Employee or musician
"""


from person import Person

class Employee(Person):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


    def get_salary(self):
        return self.salary


    def __str__(self):
        return Person.__str(self) + "\nSalary:" + str(self.salary)



from person import Person

"""MUSICIAN PART"""
class Musician(Person):
    def __init__(self, name="",age=0):
        Person.__init__(self, name, age)
        self. duration = 0


    def play(selfself, duration):
        self.duration += duration

    def __str__(self):
        return Person.__str__(self)