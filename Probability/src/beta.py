from scipy.stats import beta
import numpy as np
from bokeh.plotting import figure
from bokeh.models import Span,Label
from bokeh.io import export_png

x=np.linspace(0,1,100)
y=beta(56,46).pdf(x)
f=figure(title='Likelihood of 55 heads in 100 flips',toolbar_location=None)
f.line(x,y,line_width=3)
f.add_layout(Span(location=.55,dimension='height',line_dash='dashed',line_color='red'))
f.add_layout(Label(x=.57,y=8,text='maximum likelihood at p=.55'))
f.xaxis.axis_label='Probability of Heads'
f.xaxis.ticker=np.arange(0,1.1,.1)
export_png(f,filename='../img/beta.png')

