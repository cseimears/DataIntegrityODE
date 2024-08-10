# Connor Seimears
# CST305: Principles of Modeling and Simulation

# This program solves the ODE from part 2 of project 4 and graphs the
# solutions.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of linear differential equations
def system(x, t, A):
    return np.dot(A, x)

# Define the initial conditions
x0 = np.array([1, -1])

# Define the time interval to solve the ODE for
t = np.linspace(0, 10, 101)

# Define the matrix A
A = np.array([[-0.08, 0.04], [0.04, -0.08]])

# Solve the ODE
sol = odeint(system, x0, t, args=(A,))

# Plot the solution
plt.plot(t, sol[:, 0], label='x1(t)')
plt.plot(t, sol[:, 1], label='x2(t)')
plt.xlabel('Time (s)')
plt.ylabel('I/O data (MB)')
plt.legend()
plt.show()
