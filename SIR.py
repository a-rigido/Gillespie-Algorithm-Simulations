# Alex Rigido

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

'''	The following code is an implementation of the Gillespie Algorithm 
    for a SIR simulation:

    Susceptible --> Infected --> Recovered

    For this case, there is no birth immunity and the recovered 
    maintain immunity. Also death rate of the infected is higher than
    the birth rate of the population. It should be noted that this 
    is the simplest of the main population epidemics and further parameters
    can be added if desired. (Main goal is to show Gillespie Algorithm uses
    outside of biophysical modelling).
'''

# define rate parameters
alpha = 4.07
beta = 0.75
deathRate_I = 0.15
birthRate = 0.10

# define scenario set-up values for molecules
N = int(1e4)  # population
initI = 10  # initial number of Infected
initS = N - initI  # initial number of Susceptible
initR = 0  # initial number of Recovered
nS = initS
nI = initI
nR = initR

# define set-up values for time
timeIndex = 0  # index of time (starting at 0) for simulation
tMax = 10  # max time

# initialize storage as arrays
T = np.array([])  # time stamp
S = np.array([])  # number of S individuals at time stamp
I = np.array([])  # number of I individuals at time stamp
R = np.array([])  # number of R individuals at time stamp

# Main loop of the Gillespie Algorithm
while timeIndex <= tMax:
    # store appropriate values
    T = np.append(T, timeIndex)
    S = np.append(S, nS)
    I = np.append(I, nI)
    R = np.append(R, nR)

    # define rates of formation/deformation
    rF_I = alpha * nI
    rF_R = beta * nI

    # calculate probabilities based on system at the given time.
    pI = rF_I / (rF_R + rF_I)  # probability of Infection
    pR = rF_R / (rF_R + rF_I)  # probability of Recovery

    # stochastic determination of reaction step
    if pI > np.random.random():
        if nS > 0:
            nS -= 1
            nI += 1
        else:
            pass
    if birthRate > np.random.random():
        nS += 1
    if deathRate_I > np.random.random():
        if nI > 0:
            nI -= 1
    if pR > np.random.random():
        if nI > 0:
            nI -= 1
            nR += 1
        else:
            pass
    if (nS == 0 and nI == 0):
        break
    # exponential time step forward
    dt = np.random.exponential(1 / (rF_I + rF_R))
    timeIndex += dt

##################     End of the Main Loop     ##################

# plot results
plt.figure(1)
plt.title("Gillespie Simulation of SIR Model (Immunity)")
plt.xlabel("Time")
plt.ylabel("Population")
plt.plot(T, S, c='r', label='Susceptible')
plt.plot(T, I, c='b', label='Infected')
plt.plot(T, R, c='g', label='Recovered')
plt.legend()
# plt.savefig("SIRmodel.pdf")
plt.show()