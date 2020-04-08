class Person():
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.list = []

    def addPerson(person):
        self.list.append(person)

class Student(Person):
    def __init__(self, fname, lname, age, year, grades):
        super().__init__(fname, lname, age)
        self.year = year
        self.courses_taken = courses_taken
        self.grades = []

class Teacher(Person):
    def __init__(self, fname, lname, age, salary):
        super().__init__(fname, lname, age)
        self.salary = salary

    def showSalary(self):
        print("Teacher: %a being %c years old makes: %d $/per annum" % (self.fname, self.age, self.salary))


ex1 = Teacher("Michael", "Scott", 32, 55000)
print(ex1.age)