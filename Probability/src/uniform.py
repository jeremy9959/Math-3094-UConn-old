from bokeh.plotting import figure
from bokeh.io import export_png
import numpy as np
from scipy.stats import norm

f=np.vectorize(lambda x: 0 if x<-20 or x>100 else 1)

x=np.linspace(-40,120,100)
y=f(x)/120
f=figure(title='Prior distribution on temperature',toolbar_location=None)
f.line(x,y,line_width=3)
export_png(f,filename='../img/uniform.png')
