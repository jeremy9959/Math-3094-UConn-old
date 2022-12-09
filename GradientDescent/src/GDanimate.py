import numpy as np
import bokeh
from bokeh.palettes import TolRainbow23
from bokeh.plotting import figure, show, output_notebook, curdoc
from bokeh.models import PointDrawTool, FreehandDrawTool, ColumnDataSource, PointDrawTool
from bokeh.models.callbacks import CustomJS

def F(x,y):
    return 1.3*np.exp(-2.5*((x-1.3)**2 + (y-0.8)**2)) - 1.2*np.exp(-2*((x-1.8)**2 + (y-1.5)**2)) +4*np.exp(-3*((x-2.8)**2+.8*(y-.5)**2))


def DF(x,y,epsilon):
    DFx=(F(x+epsilon,y)-F(x,y))/epsilon
    DFy=(F(x,y+epsilon)-F(x,y))/epsilon
    return [DFx,DFy]

def pth(u,v,epsilon,nu=.1):
    xs,ys=[u],[v]
    x0,y0=u,v
    while True:
        grad = DF(x0,y0,epsilon)
        z=F(x0,y0)
        x0=x0-nu*grad[0]
        y0=y0-nu*grad[1]
        xs.append(x0)
        ys.append(y0)
        if np.abs(F(x0,y0)-z)<.0001:
            break
    return xs,ys

def handler(attr,old,new):
    x,y=new['x'][-1],new['y'][-1]
    xs,ys = pth(x,y,.01,.1)
    path.data={'x':xs,'y':ys}


# Data to contour is the sum of two Gaussian functions.
x, y = np.meshgrid(np.linspace(-2, 4, 100), np.linspace(-2, 4, 100))
z=F(x,y)


sketch=ColumnDataSource({'x':[],'y':[]})
path = ColumnDataSource({'x':[],'y':[]})
p = figure(width=800, height=600, x_range=(-2, 4), y_range=(-2, 4),tooltips=[("(x,y)","($x,$y)")])
levels = np.linspace(-1, 4, 20)
contour_renderer = p.contour(x, y, z, levels, fill_color=TolRainbow23, line_color="black",fill_alpha=.3)
colorbar = contour_renderer.construct_color_bar()
p.add_layout(colorbar, "right")

l=p.circle(x='x',y='y',source=sketch,visible=False)
p.line(x='x',y='y',source=path,line_width=2,color='red')
tool=PointDrawTool(renderers=[l])

p.add_tools(tool)
sketch.on_change('data',handler)

curdoc().add_root(p)