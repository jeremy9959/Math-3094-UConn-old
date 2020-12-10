from bokeh.plotting import figure
from bokeh.io import export_png
import numpy as np
from scipy.stats import norm

x=np.linspace(0,50,100)
y=norm(30,15).pdf(x)
z=norm(40.1,0.2).pdf(x)
f=figure(title='Prior and posterior distribution on temperature',toolbar_location=None)
f.line(x,y,color='red',legend_label='prior')
f.line(x,z,color='green',legend_label='posterior')
export_png(f,filename='../img/priorposterior.png')
