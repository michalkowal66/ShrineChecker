class Person():
    lista = []
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        Person.lista.append([self.fname, self.lname, self.age])

    @classmethod
    def print_list(cls):
        return cls.lista

class Student(Person):
    def __init__(self, fname, lname, age, year):
        super().__init__(fname, lname, age)
        self.year = year

class Teacher(Person):
    def __init__(self, fname, lname, age, salary):
        super().__init__(fname, lname, age)
        self.salary = salary

    def showSalary(self):
        print("Teacher:", self.fname, self.lname, "being", self.age, "years old makes:", self.salary, "dollars per annum")


if __name__ == "__main__":
    ex1 = Teacher("Michael", "Scott", 32, 55_000)
    ex1.showSalary()

    ex2 = Student("Andrew", "Maurice", 19, 1)

    ex3 = Person("Michał", "Kowal", 22)

    print(Person.print_list())
