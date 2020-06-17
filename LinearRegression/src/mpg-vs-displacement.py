from bokeh.plotting import figure
from bokeh.io import export_png,show, output_file
from bokeh.models import ColumnDataSource
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


data = pd.read_csv('../../data/auto-mpg/auto-mpg.csv')
source = ColumnDataSource(data)

L=LinearRegression()
L.fit(data.displacement.values.reshape(-1,1),data.mpg)
z = np.linspace(data.displacement.min(), data.displacement.max(),100)


F = figure(width=600,height=600, title='MPG vs Engine Displacement', x_axis_label='Displacement',y_axis_label='mpg')
F.scatter(x='displacement',y='mpg',source=source)
F.line(x=z,y=L.predict(z.reshape(-1,1)),line_dash='dashed',color='red',legend_label='Estimated Linear Relationship {:.2f}x+{:.2f}'.format(L.coef_[0],L.intercept_), line_width=2)
F.toolbar_location=None
export_png(F, filename='../img/mpg-vs-displacement.png')
output_file('./mpg-vs-displacement.html')
show(F)
