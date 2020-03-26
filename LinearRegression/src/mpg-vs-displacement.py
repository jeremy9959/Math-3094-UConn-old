from bokeh.plotting import figure
from bokeh.io import export_png
from bokeh.models import ColumnDataSource
import pandas as pd

data = pd.read_csv('../data/auto-mpg/auto-mpg.csv')
source = ColumnDataSource(data)

F = figure(width=600,height=600, title='MPG vs Engine Displacement', x_axis_label='Displacement',y_axis_label='mpg')
F.scatter(x='displacement',y='mpg',source=source)
F.toolbar_location=None
export_png(F, filename='../img/mpg-vs-displacement.png')
