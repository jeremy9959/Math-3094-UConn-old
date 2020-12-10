from bokeh.plotting import figure
from bokeh.io import export_png
import numpy as np
from scipy.stats import beta

x=np.linspace(0,1,100)
y=beta(5,5).pdf(x)
f=figure(title='Beta(5,5) prior',toolbar_location=None)
f.line(x,y,line_width=3)
export_png(f,filename='../img/betaprior.png')
