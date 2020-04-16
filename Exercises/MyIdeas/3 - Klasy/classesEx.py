import random

objs = []

class Person():
    lista = []
    def __init__(self, fname, lname, yob, role = None):
        self.fname = fname
        self.lname = lname
        self.role = role
        self.yob = yob
        Person.lista.append([self.fname, self.lname, self.yob, self.role])

    @classmethod
    def print_list(cls):
        print(cls.lista)

class Student(Person):
    def __init__(self, fname, lname, yob, year, role = "Student"):
        super().__init__(fname, lname, yob, role)
        self.year = year

class Teacher(Person):
    def __init__(self, fname, lname, yob, salary, role = "Teacher"):
        super().__init__(fname, lname, yob, role)
        self.salary = salary

    def showSalary(self):
        print(f"Teacher: {self.fname} {self.lname} being {self.yob} years old makes: {self.salary} dollars per annum")

class Menu():
    @classmethod
    def addObject(cls, Repeat = True):
        print("Adding (T)eacher or (S)tudent?")
        add = input(">>> ")
        if add == "T":
            fname = input("Give first name: ")
            lname = input("Give last name: ")
            while Repeat:
                try:
                    yob = int(input("Give year of birth: "))
                except:
                    print("Age must be an integer. Want to try again?")
                    dec = input(">>> ")
                    if dec == "n":
                        Repeat = False
                    else:
                        Repeat = True 
                else:
                    Repeat = False
            salary = input("Give salary: ")      
            objs.append(Teacher(fname, lname, yob, salary))
        elif add == "S":
            fname = input("Give first name: ")
            lname = input("Give last name: ")
            while Repeat:
                try:
                    yob = int(input("Give year of birth: "))
                except:
                    print("Age must be an integer. Want to try again?")
                    dec = input(">>> ")
                    if dec == "n":
                        Repeat = False
                    else:
                        Repeat = True 
                else:
                    Repeat = False
            year = input("Give year of studies: ")
            objs.append(Student(fname, lname, yob, year))   

if __name__ == "__main__":
    print("Choose action:\n1 - Add new entry\n2 - See list of entries\n3 - ")
    dec = input(">>> ")
    if dec == "1":
        Menu.addObject()
    elif dec == "2":
        pass
    elif dec == "3":
        pass

