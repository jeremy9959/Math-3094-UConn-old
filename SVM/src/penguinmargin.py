from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import export_png, show
import pandas as pd
import numpy as np

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import export_png, show, output_notebook
import pandas as pd
import numpy as np
output_notebook()

def line(x):
    return 250*x+400

def margin(x,y):
    return 250*x-y+400


penguins = 'https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/data-raw/penguins_raw.csv'

df = pd.read_csv(penguins).sample(30,random_state=21)
df['type'] = df['Species'].apply(lambda x: x.split()[0])
df['color'] = df['type'].map({'Adelie':'blue','Gentoo':'green','Chinstrap':'red'})



f = figure(toolbar_location=None)
f.xaxis.axis_label = 'Culmen Depth (mm)'
f.yaxis.axis_label = 'Body Mass (g)'
f.title.text = 'Penguin Features'
adelie = df[df['type']=='Adelie']
gentoo = df[df['type']=='Gentoo']
f.circle(x='Culmen Depth (mm)',y='Body Mass (g)',fill_color='color',legend_label = 'Adelie',source=ColumnDataSource(adelie))
f.circle(x='Culmen Depth (mm)',y='Body Mass (g)',fill_color='color',legend_label = 'Gentoo',source=ColumnDataSource(gentoo))
x = np.linspace(12.5,22,100)
y = line(x)
f.line(x,y, color='red',line_width=2,line_dash='dotted',legend_label='y=250x+400')
adelie_spot = margin(adelie['Culmen Depth (mm)'],adelie['Body Mass (g)']).argmin()
gentoo_spot = margin(gentoo['Culmen Depth (mm)'],gentoo['Body Mass (g)']).argmax()
f.diamond(x=[adelie.iloc[adelie_spot]['Culmen Depth (mm)']],y=[adelie.iloc[adelie_spot]['Body Mass (g)']],size=15,fill_color='blue')
f.diamond(x=[gentoo.iloc[gentoo_spot]['Culmen Depth (mm)']],y=[gentoo.iloc[gentoo_spot]['Body Mass (g)']],size=15,fill_color='green')

export_png(f,filename='../img/penguinmargin.png') 
