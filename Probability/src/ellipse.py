import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

X,Y = np.meshgrid(np.linspace(-5,5,100),np.linspace(-5,5,100))
Z = np.exp(-(X**2-X*Y+Y**2)/2)
map = plt.get_cmap('viridis')
fig = plt.figure()
ax = fig.add_subplot(122)
ax.set_aspect('equal')
ax.contour(X,Y,Z,10,cmap=map)
ax2 = fig.add_subplot(121,projection='3d')
ax2.plot_surface(X,Y,Z,cmap=map, linewidth=0)
fig.suptitle('Multivariate Gaussian') 
fig.savefig('../img/ellipse.png')

