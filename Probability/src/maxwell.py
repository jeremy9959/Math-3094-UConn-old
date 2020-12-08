import numpy as np
from bokeh.plotting import figure
from bokeh.io import export_png

x = np.linspace(0,10,100)
y = x*np.exp(-x**2/2)
F = figure(title='Density of norm of multivariate gaussian x',toolbar_location=None)
F.line(x,y,line_width=2)
export_png(F,filename='../img/maxwell.png')
