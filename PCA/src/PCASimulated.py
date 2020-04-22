from bokeh.plotting import figure
from bokeh.models import *
from bokeh.io import show,export_png
from bokeh.layouts import row, column
import numpy as np

N=50

x = np.random.multivariate_normal([0,0],[[2,-2],[-2,6]],size=N)
x = x/x.std()

freqx, edgesx = np.histogram(x[:,0],bins=20)
freqy,edgesy = np.histogram(x[:,1],bins=20)
deltax = edgesx[1]-edgesx[0]
deltay = edgesy[1]-edgesy[0]

fx = figure(height=200,width=200,title='X histogram',toolbar_location=None,x_range=(-5,5),y_range=(0,.2))
fx.vbar(x=edgesx[:-1],top=freqx/N,width=deltax)
fy = figure(height=200,width=200,title='Y histogram',toolbar_location=None,x_range=(-5,5),y_range=(0,.2))
fy.vbar(x=edgesy[:-1],top=freqy/N,width=deltay)
fs = figure(height=400,width=400,title='Scatter Plot of Raw Data',toolbar_location=None,x_range=(-3,3),y_range=(-3,3))
fs.scatter(x=x[:,0],y=x[:,1])
G=row(fs,column(fx,fy))
export_png(G ,filename='../img/PCAsimulated-1.png')

fs.line(x=[0,-3/5],y=[0,4/5],line_width=3,color='red')
xt = np.linspace(-6,6,10)
yt = -4/3*xt
fs.line(x=xt,y=yt,line_dash='dotted',line_color='red')
fs.add_layout(Arrow(end=NormalHead(size=10,fill_color='red'),x_start=0,y_start=0,x_end=-3/5,y_end=4/5))
export_png(G,filename='../img/PCAsimulated-2.png')


x0 = np.dot(x,np.array([-3/5,4/5]))
Z=x0.reshape(-1,1)*np.array([-3/5,4/5])
fs.circle(x=Z[:,0],y=Z[:,1],color='red',size=2)
xs = [[x[i,0],Z[i,0]] for i in range(x.shape[0])]
ys = [[x[i,1],Z[i,1]] for i in range(x.shape[0])]
fs.add_glyph(ColumnDataSource({'xs':xs,'ys':ys}),MultiLine(xs='xs',ys='ys',line_dash='dotted'))
fs.title.text='Raw Data with Projection'
export_png(G,filename='../img/PCAsimulated-3.png')


freqz, edgesz = np.histogram(Z,bins=20)
deltaz = edgesz[1]-edgesz[0]
fz = figure(height=200,width=200,title='Z histogram',toolbar_location=None,x_range=(-5,5),y_range=(0,.2))
fz.vbar(x=edgesz[:-1],top=freqz/N,width=deltaz,color='red')
export_png(row(G,fz),filename='../img/PCAsimulated-4.png')
show(row(G,fz))

# variance as angle changes

theta = np.linspace(0,2*np.pi,100)
ticks = [i*np.pi/4 for i in range(9)]
ticklabels = ['{}'.format(i) for i in range(8)]

#ticker = FixedTicker(ticks)
u = np.zeros((2,1000))
u[0,:] = np.cos(theta)
u[1,:] = np.sin(theta)
scores = np.dot(x,u)
k = figure(title='Variance along line at angle theta')
k.xaxis.axis_label = 'theta (multiples of pi/4'
k.yaxis.axis_label = 'variance'
k.xaxis.ticker = ticks
k.xaxis.major_label_overrides = dict(zip(ticks,ticklabels))
k.line(x=theta,y=scores.var(axis=0))
export_png(k,filename='../img/PCAtheta.png')

maxind =  np.argmax(scores.var(axis=0))
minind = np.argmin(scores.var(axis=0))
fm = figure(height=400,width=400,title='Scatter Plot of Raw Data',toolbar_location=None,x_range=(-3,3),y_range=(-3,3))
fm.scatter(x=x[:,0],y=x[:,1])
fm.line(x=[0,10*u[0,maxind]],y=[0,10*u[1,maxind]],color='red',line_width=2,line_dash='dashed',legend_label='max variance')
fm.line(x=[0,-10*u[0,maxind]],y=[0,-10*u[1,maxind]],color='red',line_width=2,line_dash='dashed')
fm.line(x=[0,10*u[0,minind]],y=[0,10*u[1,minind]],color='green',line_width=2,line_dash='dashed',legend_label='min variance')
fm.line(x=[0,-10*u[0,minind]],y=[0,-10*u[1,minind]],color='green',line_width=2,line_dash='dashed')
fm.legend.location = 'bottom_left'
export_png(fm,filename='../img/PCAprincipal.png')
