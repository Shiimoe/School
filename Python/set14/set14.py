import numpy as np
import matplotlib.pyplot as plt

# Question 1.
# Part (a, b)

def polar2cart(r, theta):
    '''converts polar coordinates to cartesian, returning the values as (x, y),
       can take either an array or a singular value, the r value(s) is inputted
       first and then followed by theta'''
    # Maybe try and sort out the rounding, it converts to array automatically
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

x, y = polar2cart(1, np.pi/3)
print(x, y)

# Question 2.
# Part (b)
def cartflorpos(nmax, ndiff):
    n = np.arange(1, nmax+1)
    rf = np.sqrt(n)
    phi = (1 + np.sqrt(5))/2 
    thetaf = (2 * np.pi/phi**2 + ndiff) * n
    xf, yf = polar2cart(rf, thetaf)
    plt.plot(xf, yf, 'bo')
#    plt.show()
    return xf, yf
# For some reason, that I cannot figure out for the life of me, this does not
# want to work when plt.plot is called outside of the function


ndiff = np.arange(-.25, 0.26, 0.1)
fig = plt.figure(figsize=(12,7), dpi=100)

for (i, n) in enumerate(ndiff, start=1):
    fig.add_subplot(2,3,i)
    plt.title("ndiff = %d" %i)
    cartflorpos(20, n)




plt.show()