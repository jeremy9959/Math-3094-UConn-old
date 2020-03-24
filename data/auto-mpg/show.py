import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.io import show, output_file, export_png
output_file('auto_mpg.html')
f=figure(width=500,height=500,x_axis_label='Engine Displacement (cc)',y_axis_label='mpg')
data = pd.read_csv('auto-mpg.csv')
source=ColumnDataSource(data)
f.sizing_mode='fixed'
f.scatter(x='displacement',y='mpg',source=source)
f.background_fill_color=None
f.border_fill_color=None
export_png(f,filename='./auto-mpg.png')
