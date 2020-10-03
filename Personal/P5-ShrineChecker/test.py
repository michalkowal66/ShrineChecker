class Parent():
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def foo1(self):
        self.c = 'c'
        self.d = 'd'
        print(f'{self.c} from Parent')

class Child(Parent):    
    def foo1(self):
        super(Child, self).foo1()
        self.dict = {'1' : self.c, '2' : self.d}
        for i in range(1,3):
            print(self.dict[str(i)])
        print("Child method")

    def foo2(self):
        for i in range(1,3):
            print(self.dict[str(i)])

parent = Parent()
child = Child()
child.foo1()
child.foo2()