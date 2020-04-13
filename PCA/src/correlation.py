from bokeh.io import show, export_png
from bokeh.plotting import figure
from bokeh.layouts import row
import numpy as np


A = np.array([[1,.8],[.8,1]])
B = np.array([[1,.4],[.4,1]])
C = np.array([[1,-.8],[-.8,1]])


a = np.random.multivariate_normal([1,3],cov=A,size=100)
b = np.random.multivariate_normal([-1,2],cov=B,size=100)
c = np.random.multivariate_normal([0,0],cov=C,size=100)

f1 = figure(title='r=.8',width=300,height=300)
f1.xaxis.axis_label='x'
f1.yaxis.axis_label='y'
f1.scatter(x=a[:,0],y=a[:,1])
f2 = figure(title='r=.4',width=300,height=300)
f2.xaxis.axis_label='x'
f2.yaxis.axis_label='y'
f2.scatter(x=b[:,0],y=b[:,1])
f3 = figure(title='r=-.8',width=300,height=300)
f3.xaxis.axis_label='x'
f3.yaxis.axis_label='y'
f3.scatter(x=c[:,0],y=c[:,1])
export_png(row(f1,f2,f3),filename='../img/correlation.png')
show(row(f1,f2,f3))
