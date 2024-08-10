# Project 4 - Benchmark - Data Integrity

## Purpose of This README

This readme explains how to run the dataIntegrity.py which solves
and displays graphically the ODE from Part 2 of project 4. The word 
document included with the project will go into more detail of the
mathematical approach and more.

## Description of Program

The program solves the ODE using 'odeint' function from the scipy
module. The 'odeint' function takes three arguments: the first
argument is the name of the function defining the system of ODEs, the
second argument is a list of initial conditions for the system, and 
the third argument is an array of time points at which to evaluate 
the solution.

The function defining the system of ODE's is 'system', which takes
two arguments: the first is a list of the current values of 'x1' and
'x2', and the second argument is the current time 't'.

The 'odeint' function returns an array containing the values of 'x1'
and 'x2' at the specified time points, which is then plotted using
the 'matplotlib' library. 


## Running the Program

Run the command: 'python dataIntegrity.py' in terminal



