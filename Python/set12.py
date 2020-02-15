import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# Part (a)
grid = np.linspace(-2, 2, 100)
x, y = np.meshgrid(grid, grid)

# Part (b)
m1 = 0.8
m2 = 0.2
x1 = x2 = 0.5
U = (m1 / (np.sqrt((x+x1)**2 + y**2)))\
+ (m2 / (np.sqrt((x-x2)**2 + y**2))) + (0.5*(m1+m2)*(x**2+y**2))

# Part (c), (i) 
plt.contour(x, y, U) # bad plot

# Part (c), (ii)
ax = plt.axes()
ax.set_aspect(aspect=1)
plt.title('Gravitational potential contour plot')
# changed colours for legibility
plot = plt.contour(x, y, U, levels=np.arange(1.5, 2.1, 0.2), cmap='brg')
plt.clabel(plot)
plt.savefig('set12_1.png', dpi=500)

# Part (d)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(x, y, U, cmap='gnuplot')
plt.title('3D gravitational potential surface plot')
plt.colorbar(surf, shrink=0.75)
plt.savefig('set12_2.png', dpi=500)

# Part (e), (i)
star = plt.imread('stars.png') # Called AR Scorpii
# Part (e), (ii)
ax = plt.axes()
plt.axis('off')
plt.title('Ar Scorpii')
ax.imshow(star)
plt.show()