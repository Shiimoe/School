# Program to plot Fermat's spiral and floret positions

import numpy as np
import matplotlib.pyplot as plt

from set14 import polar2cart

#%% Floret positions
# Specify number of florets to plot
nmax = 20

# Parameter to alter positions of florets (=0 for positions that line on a
# Fermat spiral)
ndiff = 0

n = np.arange(1,nmax+1)
rf = np.sqrt(n)
# Define the Golden Mean
phi = (1 + np.sqrt(5))/2
thetaf = (2*np.pi/phi**2+ndiff)*n

# Convert to Cartesians
xf, yf = polar2cart(rf, thetaf)

# Plot floret positions
plt.plot(xf,yf,'ro')
plt.title('Fermat spiral')
plt.show()

#%% Fermat spiral

# Define the Golden Mean
phi = (1 + np.sqrt(5))/2
# (Actually this is defined in the first part so doesn't need to be
# redefined here, but you will need to include it in your function.)

# Define theta and r
theta = np.linspace(0,50,500)
r = np.sqrt(phi**2*theta/(2*np.pi))

# Convert theta and r to Cartesian coordinates
x, y = polar2cart(r, theta)

# Plot Fermat spiral
plt.plot(x,y)