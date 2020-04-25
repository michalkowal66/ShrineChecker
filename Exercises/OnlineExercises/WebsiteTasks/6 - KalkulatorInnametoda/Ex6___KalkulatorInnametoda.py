import math

c = 50
h = 30

results = list()
values = [x for x in input("Podaj sekwencje wartosci zmiennej D(oddziel wartosci przecinkiem): ").split(',')]

for d in values:
    results.append(int(math.sqrt((2*c*float(d))/h)))

print(*results, sep = ',')

