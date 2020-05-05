#TESTING SCRIPT


# #Program uses nested lists to hold values calculated in each iteration, it calls for the i-th list in list for values.

# import numpy as np
# from scipy import optimize
# import time
# import sys

# def optimizeIt():

#     print("\nInitial assumptions for function calculation: viscosity = 0.000001[m^2/s], k factor = 0.001 [m]")

#     d = [0.25, 0.1, 0.25, 0.3, 0.1, 0.2, 0.3]
#     L = [330, 245, 330, 225, 180, 390, 180]
#     Q = [[53.79, 7.94, -40.39, 64.48, 8.195, -35.24, 81.595]]
#     v = []
#     f = []
#     delta_h = []
#     delta_q = []
#     limit = 0.01

#     print("\nExamplary data:\n d =", d,"\n L = ", L,"\n Q = ", Q,"\n Boundary value = ", limit)

#     while True:
#         use_ex = input("\nDo you want to use examplary set of data?(y/n)\n>>>")

#         if use_ex == "y":
#             print("\nUsing examplary data in calculations.")
#             break
            
#         elif use_ex == "n":
#             d = []
#             L = []
#             Q = [[]]
#             print("\nNOTICE: The program will now ask you to provide needed data to perform iterations.\nProviding wrong data type (such as text, where a number is expected) will cause the program to crash.")
#             sec_num = int(input("\nEnter number of sections: "))
#             for num in range(sec_num):
#                 print("\nProvide value of d no.", num+1,", in [m]")
#                 elem = float(input(">>>"))
#                 d.append(elem)
#             for num in range(sec_num):
#                 print("\nProvide value of L no.", num+1,", in [m]")
#                 elem = float(input(">>>"))
#                 L.append(elem)
#             for num in range(sec_num):
#                 print("\nProvide value of Q no.", num+1,", in [l/s]")
#                 elem = float(input(">>>"))
#                 Q[0].append(elem)
#             limit = float(input("\nProvide the boundary value for calculations, sum e <-limit, limit>: "))

#             print("\nProvided data:\n d =", d,"\n L = ", L,"\n Q = ", Q,"\n Boundary value = ", limit)
#             break
        
#         else:
#             print("\nChoose between y or n")

#     start_time = time.time()
#                                 #Initial calculations performed below
#     f_temp = []
#     for elem in range(len(d)):  #Calculating value of function getf(x) starting with x = 0.00001, and immediately checking if value gives wanted function value.
#         results = []
#         for n in range(1, 100000, 1):
#             f_test = 0.00001*n
#             result = getf(f_test, d[elem], np.absolute(Q[0][elem]))
#             if result >= 0.9999 and result <= 1.0001:
#                 f_val = 0.00001*(n)
#                 f_temp.append(round(f_val, 6))
#                 break
    
#     f.append(f_temp)    #Creating nested list with values of f in first iteration
#     v_temp = []
#     for elem in range(len(d)):
#         v_elem = np.absolute(round(((4*Q[0][elem]/1000)/((np.pi)*(d[elem])**2)),4))
#         v_temp.append(v_elem)

#     v.append(v_temp)

#     delta_temp = []
#     for elem in range(len(d)):  #Calculating delta_h values and appending it to the list
#         if Q[0][elem] < 0:
#             delta = round(-(f[0][elem]*((L[elem])/(d[elem]))*((v[0][elem]**2)/(2*9.81))),5)
#             delta_temp.append(delta)
#         else:
#             delta = round((f[0][elem]*((L[elem])/(d[elem]))*((v[0][elem]**2)/(2*9.81))),5)
#             delta_temp.append(delta)

#     delta_h.append(delta_temp)
  
#     if findSum(0, d, L, Q, v, f, delta_h, delta_q, limit):  #Iterative function
#         print("\nPrinted results.\nProgram finished calculations successfully after", round((time.time() - start_time), 1), "seconds.")
#         while True:
#             quit_dec = input("\nChoose action:\n 1 - move to main menu\n 2 - close program\n>>>")
#             if quit_dec == "1":
#                 print("\n***Redirecting to main menu***\n")
#                 break
#             elif quit_dec == "2":
#                 sys.exit(0)
#             else:
#                 print("\nUse (1) or (2) keys to make decision.\n")
#     else:
#         print("Error")

# def getf(f, d, Q):

#     k = 0.001
#     visc = 0.000001
#     Q_conv = Q*0.001
#     vel = (4*Q_conv)/(3.14*d**2)
#     Re = (vel*d)/visc
#     k_d = k/d

#     return -2*np.sqrt(f)*np.log10((k_d/3.7)+(2.51/(Re*np.sqrt(f))))

# def findSum(i, d, L, Q, v, f, delta_h, delta_q, limit): #Function calling itself after calculating all needed values in order to proceed and increase iterator.
#     print("\nPerforming", i+1, "iteration\n Sum :",np.sum(delta_h[i]))
#     if np.sum(delta_h[i]) >= -limit and np.sum(delta_h[i]) <= limit:    #Finish condition
#         print("\nNumber of iterations performed:", i+1,"\nSum acquired =", np.sum(delta_h[i]),"\n\nd =", d, "\nL =", L, "\nQ =", Q, "\nv =", v, "\nf =", f,"\ndelta_h =", delta_h, "\ndelta q =", delta_q)
#         return True

#     suma_dh = np.sum(delta_h[i])
#     suma_dh_q = 0
#     for elem in range(len(d)):
#         temp_den = delta_h[i][elem]/Q[i][elem]
#         suma_dh_q += temp_den
    
#     delta_i = -((suma_dh)/(2*(suma_dh_q)))
#     delta_q.append(delta_i)

#     Q_temp = []
#     for elem in range(len(d)):
#         Q_new = round(Q[i][elem] + delta_q[i],5)
#         Q_temp.append(Q_new)

#     Q.append(Q_temp)

#     f_temp = []
#     for elem in range(len(d)):

#         results = []
#         for n in range(1, 100000, 1):
#             f_test = 0.00001*n
#             result = getf(f_test, d[elem], np.absolute(Q[i+1][elem]))
#             if result >= 0.9999 and result <= 1.0001:
#                 f_temp.append(round(f_test, 5))
#                 break
    
#     f.append(f_temp)

#     v_temp = []
#     for elem in range(len(d)):
#         v_elem = np.absolute(round(((4*Q[i+1][elem]/1000)/((np.pi)*(d[elem])**2)),4))
#         v_temp.append(v_elem)

#     v.append(v_temp)

#     delta_temp = []
#     for elem in range(len(d)):
#         if Q[i+1][elem] < 0:
#             delta = round(-(f[i+1][elem]*((L[elem])/(d[elem]))*((v[i+1][elem]**2)/(2*9.81))),5)
#             delta_temp.append(delta)
#         else:
#             delta = round((f[i+1][elem]*((L[elem])/(d[elem]))*((v[i+1][elem]**2)/(2*9.81))),5)
#             delta_temp.append(delta)

#     delta_h.append(delta_temp)

#     if findSum(i+1, d, L, Q, v, f, delta_h, delta_q, limit):    #Calling itself in this line with increased value of iterator.
#         return True

# while True:                                                     #Trivial while statement to prevent program closing after code execution.
#     print("You are in main menu.\n\n Choose option:\n 1 - Start program\n 2 - Quit")
#     dec = input(">>>")
#     if dec == "1":
#         optimizeIt()
#     elif dec == "2":
#         print("Closing...")
#         break
#     else:
#         print("Choose option 1 or 2.")

