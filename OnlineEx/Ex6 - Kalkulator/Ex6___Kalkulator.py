import math

class Wzor(object):
    def __init__(self):
        self.D = input('Podaj sekwencje liczb majacych okreslic wartosc D: ')

    def licz(self):
        k = list()
        l = self.D.split(',')
        print(l)
        for i in range(0, len(l), 1):
            pp = (2*50*int(l[i]))/30
            w = int(math.sqrt(pp))
            k.append(w)
        print(*k, sep=',')

liczby = Wzor()
liczby.licz()