import numpy as np
import sys

def fun(f, d, frate):

    k = 0.001
    visc = 0.000001
    frate_conv = frate*0.001
    vel = (4*frate_conv)/(3.14*d**2)
    Re = (vel*d)/visc
    k_d = k/d

    return -2*np.sqrt(f)*np.log10((k_d/3.7)+(2.51/(Re*np.sqrt(f))))

while True:
    d = float(input("Provide diameter d[m] = "))
    frate = float(input("Provide flow rate Q[l/s] = "))

    results = []
    for i in range(1, 100000, 1):
        f = 0.00001*i
        result = fun(f, d, frate)
        if result >= 0.9999 and result <= 1.0001:
            print("\nFor submitted:\nd = ", d,"and Q = ", frate,"\nFunction 'f' value for ",round(f,5),"Is equal to :",fun(f, d, frate))
            break

    while True:
        cont = input("\nContinue with next set of data(y/n)?\n>>>")
        if cont == "y":
            print("\n")
            break
        elif cont == "n":
            sys.exit(0)
        else:
            print("\nChoose 'y' or 'n'.")
    