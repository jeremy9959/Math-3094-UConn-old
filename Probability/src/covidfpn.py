from bokeh.plotting import figure
from bokeh.io import output_file, show,export_png
import numpy as np
from scipy.stats import norm

def h(x):
    return 750*x/(5+745*x)

F = figure(title='P(S|+) as a function of population incidence if 25% false negatives and .5% false positives',toolbar_location=None)
x=np.linspace(0,.2,100)
y=750*x/(5+745*x)
F.line(x, y)
u=[.01,.03,.05,.1]
v=[h(x) for x in u]
F.circle(u,v)
export_png(F,filename='../img/covidfn.png')
