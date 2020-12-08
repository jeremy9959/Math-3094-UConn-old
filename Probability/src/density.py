from bokeh.plotting import figure
from bokeh.io import output_file, show,export_png
import numpy as np
from scipy.stats import norm


F = figure(title='Normal Probability Density',toolbar_location=None)
x=np.linspace(-5,5,100)
colors=['green','red','black','blue','orange'] 
for i,sigma in enumerate([.25,.5,1,1.5,2]):
    F.line(x, norm.pdf(x,0,np.sqrt(sigma)),color=colors[i],legend_label='{:.2f}'.format(sigma))
F.legend.title='\u03c3'
export_png(F,filename='../img/density.png')
