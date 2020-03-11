#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320
import math

def fact(x):
    if x == 0:
        print("Factorial of ",x,"is equal to: 1")
    elif x < 0:
        print("You have to provide a positive number!")
    else:
        print("Factorial of ",x,"is equal to:",x*math.factorial(x-1))

x = int(input('Give an integral: '))
fact(x)
 