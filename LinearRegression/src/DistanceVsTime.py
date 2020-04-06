from bokeh.plotting import figure
import numpy as np
from bokeh.io import show, export_png
from bokeh.models import Range1d

x = [i for i in range(10)]
y=[-14.2*i+np.random.normal(0,5)+150 for i in x]


f=figure(title='Measured Distance to a Moving Object vs Time',toolbar_location=None)
f.xaxis.axis_label = 'Time'
f.yaxis.axis_label = 'Distance (m)'
f.scatter(x=x,y=y)
f.line(x=x,y=[150-14.2*i for i in x],line_dash='dashed',legend_label='Estimated Speed = -14.2m/s',color='red')
f.y_range=Range1d(0,200)
export_png(f, filename='../img/distance-vs-time.png')
show(f)







