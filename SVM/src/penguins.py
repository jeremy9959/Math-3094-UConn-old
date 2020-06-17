from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import export_png
import pandas as pd

penguins = 'https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/data-raw/penguins_raw.csv'

df = pd.read_csv(penguins)
df['type'] = df['Species'].apply(lambda x: x.split()[0])
df['color'] = df['type'].map({'Adelie':'blue','Gentoo':'green','Chinstrap':'red'})

f = figure(toolbar_location=None)
f.xaxis.axis_label = 'Culmen Depth (mm)'
f.yaxis.axis_label = 'Body Mass (g)'
f.title.text = 'Penguin Features'
adelie = f.circle(x='Culmen Depth (mm)',y='Body Mass (g)',fill_color='color',legend_label = 'Adelie',source=ColumnDataSource(df[df['type']=='Adelie']))
adelie = f.circle(x='Culmen Depth (mm)',y='Body Mass (g)',fill_color='color',legend_label = 'Gentoo',source=ColumnDataSource(df[df['type']=='Gentoo']))

export_png(f,filename='../img/penguins.png') 
