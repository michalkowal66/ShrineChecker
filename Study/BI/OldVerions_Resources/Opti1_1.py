import numpy as np
from scipy import optimize
import time

def optimizeIt():

    start_time = time.time()

    d = [0.25, 0.1, 0.25, 0.3, 0.1, 0.2, 0.3]
    L = [330, 245, 330, 225, 180, 390, 180]
    Q = [[53.79, 7.94, -40.39, 64.48, 8.195, -35.24, 81.595]]
    v = []
    f = []
    delta_h = []
    delta_q = []

    f_temp = []
    for elem in range(len(d)):
        results = []
        for n in range(1, 100000, 1):
            f_test = 0.00001*n
            result = getf(f_test, d[elem], np.absolute(Q[0][elem]))
            if result >= 0.9999 and result <= 1.0001:
                f_val = 0.00001*(n)
                f_temp.append(round(f_val, 6))
                break
    
    f.append(f_temp)    #Creating nested list with values of f in first iteration
    v_temp = []
    for elem in range(len(d)):
        v_elem = np.absolute(round(((4*Q[0][elem]/1000)/((np.pi)*(d[elem])**2)),4))
        v_temp.append(v_elem)

    v.append(v_temp)

    delta_temp = []
    for elem in range(len(d)):
        if Q[0][elem] < 0:
            delta = round(-(f[0][elem]*((L[elem])/(d[elem]))*((v[0][elem]**2)/(2*9.81))),5)
            delta_temp.append(delta)
        else:
            delta = round((f[0][elem]*((L[elem])/(d[elem]))*((v[0][elem]**2)/(2*9.81))),5)
            delta_temp.append(delta)

    delta_h.append(delta_temp)
  
    if findSum(0, d, L, Q, v, f, delta_h, delta_q):
        print("Wyswietlam 2 serie wynikow wstecz.\nCzas pracy kodu:", round((time.time() - start_time), 1), "sekund.")
    else:
        print("Error")

def getf(f, d, Q):

    k = 0.001
    visc = 0.000095
    Q_conv = Q*0.001
    vel = (4*Q_conv)/(3.14*d**2)
    Re = (vel*d)/visc
    k_d = k/d

    return -2*np.sqrt(f)*np.log10((k_d/3.7)+(2.51/(Re*np.sqrt(f))))

def findSum(i, d, L, Q, v, f, delta_h, delta_q):
    print("Wykonuje", i+1, "iteracje\n aktualna suma :",np.sum(delta_h[i]))
    if np.sum(delta_h[i]) >= -0.2 and np.sum(delta_h[i]) <= 0.2:
        print("Ilosc iteracji: ", i+1,"\nd = ", d, "\nL = ", L, "\nQ = ", Q[len(Q)-2:], "\nv = ", v[len(v)-2:], "\nf = ", f[len(f)-2:],"\ndelta_h = ", delta_h[len(delta_h)-2:], "\ndelta q =", delta_q[len(delta_q)-2:])
        return True

    delta_i = round(-((np.sum(delta_h[i]))/2*(np.sum(delta_h[i])/np.sum(Q[i]))),5)
    delta_q.append(delta_i)

    Q_temp = []
    for elem in range(len(d)):
        Q_new = round(Q[i][elem] + delta_q[i],5)
        Q_temp.append(Q_new)

    Q.append(Q_temp)

    f_temp = []
    for elem in range(len(d)):

        results = []
        for n in range(1, 100000, 1):
            f_test = 0.00001*n
            result = getf(f_test, d[elem], np.absolute(Q[i+1][elem]))
            if result >= 0.9999 and result <= 1.0001:
                f_temp.append(round(f_test, 5))
                break
    
    f.append(f_temp)

    v_temp = []
    for elem in range(len(d)):
        v_elem = np.absolute(round(((4*Q[i+1][elem]/1000)/((np.pi)*(d[elem])**2)),4))
        v_temp.append(v_elem)

    v.append(v_temp)

    delta_temp = []
    for elem in range(len(d)):
        if Q[i+1][elem] < 0:
            delta = round(-(f[i+1][elem]*((L[elem])/(d[elem]))*((v[i+1][elem]**2)/(2*9.81))),5)
            delta_temp.append(delta)
        else:
            delta = round((f[i+1][elem]*((L[elem])/(d[elem]))*((v[i+1][elem]**2)/(2*9.81))),5)
            delta_temp.append(delta)

    delta_h.append(delta_temp)

    if findSum(i+1, d, L, Q, v, f, delta_h, delta_q):
        return True


optimizeIt()