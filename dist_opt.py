#Code and report written by Murdock Aubry

from math import sqrt,exp
import numpy as np
from numpy import empty
from random import random,randrange, seed
import matplotlib.pyplot as plt
from matplotlib import rc

save=True # if True then we save images as files
font = {'size'   : 10}
rc('font', **font)
mydpi = 200


figure, axes = plt.subplots() 


'''PSEUDOCODE
1. Define relevant constants
2. Copy the code salesman.py
3. Run multiple times using various values of the seed within the while loop
4. Plot the final path and length of path
'''


'''DEFINING CONSTANTS'''


N = 100
R = 0.02
Tmax = 10.0
Tmin = 1e-3
tau = 1e3

# Function to calculate the magnitude of a vector
def mag(x):
    return sqrt(x[0]**2+x[1]**2)

# Function to calculate the total length of the tour
def distance():
    s = 0.0
    for i in range(N-1):
        s += mag(r[i+1]-r[i])
    return s


############################### Randomly generate the points ###############################

# Choose N city locations and calculate the initial distance
seed(5) #choosing seed for randomizing initial set of points

r = empty([N+1,2],float)
for i in range(N):
    r[i,0] = random() * 10
    r[i,1] = random() * 10
r[N] = r[0]


############################################################################################



############################### Specify Points Yourself ####################################

# r = np.transpose(np.loadtxt("points.tex", skiprows= 4, usecols= (0,1), unpack= True, delimiter=","))
# N = len(r[:, 0])

############################################################################################


dist = distance()
D = dist




r_initial = r.copy()


# Plot the initial locations 

# for i in range(N):
#     if i == 0:
#         plt.plot([r_initial[i, 0], r_initial[i+1, 0]], [r_initial[i, 1], r_initial[i+1, 1]], c = 'blue', label = 'distance = %3.2f'%(dist)) #Used for plotting optimized path
#         cc = plt.Circle(r[i], 2 * D / N ** 2, color = 'b') 
#         axes.set_aspect( 1 ) 
#         axes.add_artist( cc ) 
#     else: 
#         plt.plot([r_initial[i, 0], r_initial[i+1, 0]], [r_initial[i, 1], r_initial[i+1, 1]], c = 'blue') #Used for plotting optimized path
#         cc = plt.Circle(r[i], 2 * D / N**2, color = 'b') 
#         axes.set_aspect( 1 ) 
#         axes.add_artist( cc ) 

# plt.xlabel(r'$x$ position')
# plt.ylabel(r'$y$ position')
# plt.legend(loc = "best")
# plt.title(r'Original Path')
# if (save): plt.savefig('original_path.png',dpi=mydpi)
# plt.show()




''' MAIN LOOP '''

seed(10) #choosing seed to vary order of potential swapping
t = 0
T = Tmax
while T>Tmin:
    # Cooling
    t += 1
    T = Tmax*exp(-t/tau)

    # Choose two cities to swap and make sure they are distinct
    i,j = randrange(1,N),randrange(1,N)
    while i==j:
        i,j = randrange(1,N),randrange(1,N)

    # Swap them and calculate the change in distance
    oldD = dist
    r[i,0],r[j,0] = r[j,0],r[i,0]
    r[i,1],r[j,1] = r[j,1],r[i,1]
    dist = distance()
    deltaD = dist - oldD

    # If the move is rejected, swap them back again
    if random()>exp(-deltaD/T):
        r[i,0],r[j,0] = r[j,0],r[i,0]
        r[i,1],r[j,1] = r[j,1],r[i,1]
        dist = oldD


'''PLOTTING PATHS'''

print(dist)



for i in range(N):
    if i == 0:
        plt.plot([r[i, 0], r[i+1, 0]], [r[i, 1], r[i+1, 1]], c = 'blue', label = 'distance = %3.2f'%(dist)) #Used for plotting optimized path
        cc = plt.Circle(r[i], 2 * D / N ** 2, color = 'b') 
        axes.set_aspect( 1 ) 
        axes.add_artist( cc ) 
    else: 
        plt.plot([r[i, 0], r[i+1, 0]], [r[i, 1], r[i+1, 1]], c = 'blue') #Used for plotting optimized path
        cc = plt.Circle(r[i], 2 * D / N**2, color = 'b') 
        axes.set_aspect( 1 ) 
        axes.add_artist( cc ) 

plt.xlabel(r'$x$ position')
plt.ylabel(r'$y$ position')
plt.legend(loc = "best")
plt.title(r'Optimized Path')
if (save): plt.savefig('optimized_path.png',dpi=mydpi)
plt.show()
