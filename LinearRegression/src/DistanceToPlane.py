import pandas as pd
from bokeh.models import ColumnDataSource, Label
from bokeh.io import show, export_png
from bokeh.plotting import figure


f=figure(width=600,height=600,title='Distance to a plane (side view)',toolbar_location=None)

f.line(x=range(-10,10,1),y=range(10,-10,-1))
f.scatter(x=[3,-1,-4],y=[5,1,4],size=10,color=['red','green','blue'])
f.line(x=[-4,3],y=[4,5])
f.line(x=[-1,3],y=[1,5])
f.add_layout(Label(x=-1,y=1,text='Yhat',x_offset=10,y_offset=-10))
f.add_layout(Label(x=3,y=5,text='Y',x_offset=10,y_offset=-10))
f.add_layout(Label(x=-4,y=4,text='General Pt',x_offset=-100))

export_png(f, filename='../img/distance-to-plane.png')
show(f)






