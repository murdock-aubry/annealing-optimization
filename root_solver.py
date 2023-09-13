#Code and report written by Murdock Aubry

from math import sqrt,exp
import numpy as np
from random import random,randrange, seed, choice
import matplotlib.pyplot as plt


'''PSUEDOCODE
PART B
1. Define the function f(x, y) as given in the lab manual
2. Define relevant constants such as sigma, Tmax, Tmin, and tau
3. Define a random number generator using gaussian distribution, as defined in the textbook
4. Set initial guess points (x, y)
5. Write a while loop for when the value of T is greater than Tmax
    5.1. Set t += 1
    5.2. Set T = Tmax * exp(-t/tau)
    5.3. Evaluate f at the points (x, y)
    5.4. Randomly generate new (x, y) values using the gaussian distribution
    5.5. Evaluate f(x, y) at the new points
    5.6. Calculate the change in the value of f compared to the prevous (x, y) values
    5.7. Compare this change in f, namely the value exp(-delta_f/T), with a random number normally distributed between 0 and 1
    5.8. If this value is greater than the random number, disgrard and go back to initial (x, y) values
    5.9. If the vlaue is less than the random number, accept the values (x, y) and complete steps 5.1 - 5.7
    5.10. Either way, record the current values of (x, y), which will be used in a plot
6. Return the final (x, y) values, and plot (x, y) in a scatter plot with gradient colouring to indicate which guess it was

PART C
7. Complete all of the above steps, however using the new function f(x) as given in the textbook  
8. Alter step 5.8 to also disregard (x, y) in (x, y) not it (0, 50) x (-20, -20)
'''

sigma = 1
Tmax = 1.0
Tmin = 1e-4
tau = 1e5

def f(x,y):
    return x**2 - np.cos(4 * np.pi * x) + (y - 1)**2

def g(x, y):
    return np.cos(x) + np.cos(np.sqrt(2) * x) + np.cos(np.sqrt(3) * x) + (y - 1)**2

def gaussian():
    return np.sqrt(-2 * sigma ** 2 * np.log(1 - random())) * choice((-1, 1)) #sqrt() is strictly positive, we are also looking for negative values so make a random choice to multiply by 1 or -1

''' MAIN LOOP '''

t = 0
T = Tmax
xi, yi = 0, 1
fval = f(xi, yi)

xvalues1 = []
yvalues1 = []
xvalues2 = []
yvalues2 = []


while T>Tmin:
    # Cooling
    t += 1
    T = Tmax*exp(-t/tau)

    # Swap them and calculate the change in distance
    fval_old = fval
    x_new, y_new = xi + gaussian(), yi + gaussian()
    fval = f(x_new, y_new)
    delta_f = fval - fval_old

    # If the move is rejected, swap them back again
    if random()>exp(-delta_f/T):
        xi, yi = xi, yi
        fval = fval_old
    else:
        xi, yi = x_new, y_new
        xvalues1.append(xi)
        yvalues1.append(yi)
        fval = f(xi, yi)

print(xi, yi)
f, ax = plt.subplots()
col = np.arange(len(xvalues1))
points = ax.scatter(xvalues1, yvalues1, s = 1, c = col)
f.colorbar(points)
plt.xlabel(r'$x$-values')
plt.ylabel(r'$y$-value')
#plt.show()


T = Tmax
t=0
xj, yj = 2, 8
gval = g(xj, yj)

while T>Tmin:
    # Cooling
    t += 1
    T = Tmax*exp(-t/tau)

    # Swap them and calculate the change in distance
    gval_old = gval
    x_new, y_new = xj + gaussian(), yj + gaussian()
    gval = g(x_new, y_new)
    delta_g = gval - gval_old

    # If the move is rejected, swap them back again
    if random()>exp(-delta_g/T) or x_new > 50 or x_new < 0 or abs(y_new) > 20:
        xj, yj = xj, yj
        gval = gval_old
    else:
        xj, yj = x_new, y_new
        xvalues2.append(xj)
        yvalues2.append(yj)
        gval = g(xj, yj)



print(xj, yj)
f, ax = plt.subplots()
col = np.arange(len(xvalues2))
points = ax.scatter(xvalues2, yvalues2, s = 1, c = col)
f.colorbar(points)
plt.xlabel(r'$x$-values')
plt.ylabel(r'$y$-value')
#plt.show()