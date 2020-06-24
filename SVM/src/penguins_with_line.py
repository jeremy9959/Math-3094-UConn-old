from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import export_png, show
import pandas as pd
import numpy as np


penguins = '../../data/penguins/penguins_raw.csv'

df = pd.read_csv(penguins)
df['type'] = df['Species'].apply(lambda x: x.split()[0])
df['color'] = df['type'].map({'Adelie':'blue','Gentoo':'green','Chinstrap':'red'})

f = figure(toolbar_location=None,match_aspect=True)
f.xaxis.axis_label = 'Culmen Depth (mm)'
f.yaxis.axis_label = 'Body Mass (x200 g)'
f.title.text = 'Penguin Features'

df['Body Mass (x200 g)'] = df['Body Mass (g)']/200
df['Body Mass (x200 g)'] = df['Body Mass (g)']/200
adelie = df[df['type']=='Adelie']
gentoo = df[df['type']=='Gentoo']

f.circle(x='Culmen Depth (mm)',y='Body Mass (x200 g)',fill_color='color',legend_label = 'Adelie',source=ColumnDataSource(adelie))
f.circle(x='Culmen Depth (mm)',y='Body Mass (x200 g)',fill_color='color',legend_label = 'Gentoo',source=ColumnDataSource(gentoo))

x = np.linspace(12.5,22,100)
y = 1.25*x+2
f.line(x,y, color='red',line_width=2,line_dash='dotted')
export_png(f,filename='../img/penguins_with_line.png') 
show(f)
