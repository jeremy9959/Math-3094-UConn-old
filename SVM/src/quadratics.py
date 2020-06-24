from bokeh.plotting import figure
from bokeh.io import export_png, show
from bokeh.models import ColumnDataSource, Span, BoxAnnotation,Label
from bokeh.layouts import row
import numpy as np

x=np.linspace(-3,4,100)
y=x**2-3
source = ColumnDataSource({'x':x,'y':y})

f= figure(title='Constraint below the critical point (star marks minimum)',toolbar_location=None)
g=figure(title='Constraint above the critical point (star marks minimum)',toolbar_location=None)

f.line(x='x',y='y',source=source)
f.xaxis.axis_label='delta'
f.yaxis.axis_label='Objective'
g.xaxis.axis_label='delta'
g.yaxis.axis_label='Objective'
constraint=Span(location=-2, dimension='height', line_dash='dashed')
f.add_layout(constraint)
f.asterisk(x=[0],y=[-3], size=20, color='red')
feasible = BoxAnnotation(left=-2,fill_alpha=.1,fill_color='green')
f.add_layout(feasible)
f.add_layout(Label(x=-1,y=5,text="Feasible Region"))
g.line(x='x',y='y',source=source)
constraint2=Span(location=2, dimension='height', line_dash='dashed')
g.asterisk(x=[2],y=[1],size=20,color='red')
feasible = BoxAnnotation(left=2,fill_alpha=.1,fill_color='green')
g.add_layout(Label(x=2.5,y=-2,text="Feasible Region"))
g.add_layout(constraint2)
g.add_layout(feasible)
h = row(f,g)
export_png(h,filename='../img/quadratic.png')
