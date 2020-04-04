from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row, column
from bokeh.models import Range1d
from bokeh.io import export_png
from sklearn.linear_model import LinearRegression
import numpy as np


x0 = np.random.normal(2, 0.7, 1000)
y0 = x0 + 3 * np.random.normal(0, 0.5, 1000)
x1 = np.random.normal(1, 0.7, 1000)
y1 = x1 + 3 * np.random.normal(0, 0.51, 1000) + np.random.normal(5, 1, 1000)
x2 = np.random.normal(0, 0.7, 1000)
y2 = x2 + 3 * np.random.normal(0, 0.51, 1000) + np.random.normal(9, 1, 1000)

L = LinearRegression()

b0 = L.fit(x0.reshape(-1, 1), y0).intercept_
b1 = L.fit(x1.reshape(-1, 1), y1).intercept_
b2 = L.fit(x2.reshape(-1, 1), y2).intercept_

m0 = L.fit(x0.reshape(-1, 1), y0).coef_
m1 = L.fit(x1.reshape(-1, 1), y1).coef_
m2 = L.fit(x2.reshape(-1, 1), y2).coef_

z = np.linspace(-4, 6, 100)


y = np.concatenate([y0, y1, y2])
x = np.concatenate([x0, x1, x2])


mx = L.fit(x.reshape(-1, 1), y).coef_
bx = L.fit(x.reshape(-1, 1), y).intercept_

f0 = figure(
    width=300,
    height=300,
    title="Blue Lab Results m = {}".format(m0),
    toolbar_location=None,
)
f1 = figure(
    width=300,
    height=300,
    title="Green Lab Results m={}".format(m1),
    toolbar_location=None,
)
f2 = figure(
    width=300,
    height=300,
    title="Red Lab Results m={}".format(m2),
    toolbar_location=None,
)
f1.y_range = Range1d(-5, 16)
f2.y_range = Range1d(-5, 16)
f0.y_range = Range1d(-5, 16)
f0.xaxis.axis_label = "Marker level"
f0.yaxis.axis_label = "Weight Gain"
f1.xaxis.axis_label = "Marker level"
f1.yaxis.axis_label = "Weight Gain"
f2.xaxis.axis_label = "Marker level"
f2.yaxis.axis_label = "Weight Gain"


f0.scatter(x=x0, y=y0, color="blue")
f0.line(x=z, y=m0 * z + b0, color="blue")
f1.scatter(x=x1, y=y1, color="green")
f1.line(x=z, y=m1 * z + b1, color="green")
f2.scatter(x=x2, y=y2, color="red")
f2.line(x=z, y=m2 * z + b2, color="red")

f = figure(
    width=300, height=300, title="Pooled Result m={}".format(mx), toolbar_location=None
)
f.y_range = Range1d(-5, 16)
f.xaxis.axis_label = "Marker level"
f.yaxis.axis_label = "Weight Gain"
f.line(x=z, y=mx * z + bx, color="black")
f.scatter(x=x0, y=y0, color="blue", alpha=0.1)
f.scatter(x=x1,y=y1,color='green',alpha=.1)
f.scatter(x=x2,y=y2,color='red',alpha=0.1)
C = column([row([f, f0]), row([f1, f2])])
export_png(C, filename="../img/SimpsonsEffect.png")
show(C)
