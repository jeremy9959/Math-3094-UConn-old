from bokeh.plotting import figure
from bokeh.io import export_png
import numpy as np
from scipy.stats import norm

x=np.linspace(-40,100,100)
y=norm(30,15).pdf(x)
f=figure(title='Prior distribution on temperature',toolbar_location=None)
f.line(x,y,line_width=3)
export_png(f,filename='../img/prior.png')
