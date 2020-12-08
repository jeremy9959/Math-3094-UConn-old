from bokeh.plotting import figure
from bokeh.io import output_file, show,export_png
import numpy as np
from scipy.stats import norm


F = figure(title='Normal Probability Density')
x=np.linspace(-2,2,100)
colors=['green','red','black','blue','orange'] 
for i,sigma in enumerate([.25,.5,.1,1.5,2]):
    F.line(norm.pdf(x,0,np.sqrt(sigma)),color=colors[i])

export_png(F,'../img/density.png')
