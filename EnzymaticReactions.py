# Alex Rigido

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

''' The following code is an implementation of the Gillespie Algorithm for 
    the following enzymatic reaction (irreversible product formation):

    E + S <--> ES --> E + P 

    E = Enzyme
    S = Substrate
    ES = Enzyme-Substrate Complex
    P = Product

    This can be broken down into the following system of equations:

    1.  E + S --> ES     (rate = k1)
    2.  ES --> E + S     (rate = k2)
    3.  ES --> E + P     (rate = k3)

    Note:   k1, k2, and k3 chosen arbitrarily for simulation purposes.
    '''

# define Rates
k1 = 4.07
k2 = 2.019
k3 = 0.75

# define set-up values for molecules
N = int(1e4)  # total number of molecules in the system (not including E)
Etot = N * 0.8  # total number of Enzyme in the system
initES = 0  # initial number of ES complex
initS = N  # initial number of substrate
initP = 0  # initial number of product
nS = initS
nE = Etot
nES = initES
nP = initP

# define set-up values for time
timeIndex = 0  # index of time (starting at 0) for simulation
tMax = 4  # max time

# initialize storage as arrays
T = np.array([])  # time stamp
S = np.array([])  # number of S molecules at time stamp
E = np.array([])  # number of E molecules at time stamp
ES = np.array([])  # number of ES molecules at time stamp
P = np.array([])  # number of P molecules at time stamp

# Main loop of the Gillespie Algorithm
while timeIndex <= tMax:
    # store appropriate values
    T = np.append(T, timeIndex)
    S = np.append(S, nS)
    E = np.append(E, Etot - nES)
    ES = np.append(ES, nES)
    P = np.append(P, nP)

    # define rates of formation/deformation
    rF_S = k2 * nES
    rF_ES = k1 * nS
    rF_P = k3 * nES

    # calculate probabilities based on system at the given time.
    pES = rF_ES / (rF_ES + rF_S)  # probability of forming ES Complex
    pP = rF_P / (rF_ES + rF_P)  # probability of forming Product
    pS = 1 - pES - pP  # probability of forming Substrate

    # stochastic determination of reaction step
    if pES > np.random.random():
        nS -= 1
        nES += 1
    elif pS > np.random.random():
        if (nES == 0):
            pass
        else:
            nES -= 1
            nS += 1
    if pP > np.random.random():
        if (nES == 0):
            pass
        else:
            nES -= 1
            nP += 1

    # exponential time step forward
    dt = np.random.exponential(1 / (rF_S + rF_ES + rF_P))
    timeIndex += dt

##################     End of the Main Loop     ##################

# Plot Results
plt.figure(1)
plt.title("Gillespie Simulation of Enzymatic Reaction (Irr.)")
plt.xlabel("Time")
plt.ylabel("Fraction of Total Molecules")
plt.plot(T, S / N, c='r', label="Substrate")
plt.plot(T, E / N, c='k', label="Free Enzyme")
plt.plot(T, ES / N, c='g', label="ES Complex")
plt.plot(T, P / N, c='b', label="Product")
plt.legend()
# plt.savefig("irrEnzymaticReaction.png")
plt.show()
