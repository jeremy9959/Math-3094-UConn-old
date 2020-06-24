# %load penguinsimple.py
from bokeh.models import ColumnDataSource, Range1d
from bokeh.plotting import figure
from bokeh.io import export_png, show, output_notebook
import pandas as pd
import numpy as np


def line(x,b):
    return (250/200)*x+b

def margin(x,y):
    return (250/200)*x-y+(400/200)


penguins = '../../data/penguins/penguins_raw.csv'

df = pd.read_csv(penguins)
df['type'] = df['Species'].apply(lambda x: x.split()[0])
df['color'] = df['type'].map({'Adelie':'blue','Gentoo':'green','Chinstrap':'red'})

f = figure(toolbar_location=None,match_aspect=True)
f.xaxis.axis_label = 'Culmen Depth (mm)'
f.yaxis.axis_label = 'Body Mass (x200 g)'
f.title.text = 'Penguin Features'
f.x_range=Range1d(12.5,22)
f.y_range=Range1d(12.5,33)
df['Body Mass (x200 g)'] = df['Body Mass (g)']/200
df['Body Mass (x200 g)'] = df['Body Mass (g)']/200
adelie = df[df['type']=='Adelie']
gentoo = df[df['type']=='Gentoo']

f.circle(x='Culmen Depth (mm)',y='Body Mass (x200 g)',fill_color='color',legend_label = 'Adelie',source=ColumnDataSource(adelie))
f.circle(x='Culmen Depth (mm)',y='Body Mass (x200 g)',fill_color='color',legend_label = 'Gentoo',source=ColumnDataSource(gentoo))
x = np.linspace(12.5,25,100)
#y = line(x,400)
#f.line(x,y, color='red',line_width=2,line_dash='dotted',legend_label='y=250x+400')
adelie_spot = margin(adelie['Culmen Depth (mm)'],adelie['Body Mass (x200 g)']).argmin()
adelie_b = margin(adelie['Culmen Depth (mm)'],adelie['Body Mass (x200 g)']).min()
gentoo_spot = margin(gentoo['Culmen Depth (mm)'],gentoo['Body Mass (x200 g)']).argmax()
gentoo_b = margin(gentoo['Culmen Depth (mm)'],gentoo['Body Mass (x200 g)']).max()
print(adelie_b,gentoo_b)
f.diamond(x=[adelie.iloc[adelie_spot]['Culmen Depth (mm)']],y=[adelie.iloc[adelie_spot]['Body Mass (x200 g)']],size=15,fill_color='blue')
f.diamond(x=[gentoo.iloc[gentoo_spot]['Culmen Depth (mm)']],y=[gentoo.iloc[gentoo_spot]['Body Mass (x200 g)']],size=15,fill_color='green')
f.line(x,line(x,(2-adelie_b)),line_width=2,legend_label='y=1.25x+{:.3f}'.format((400-adelie_b)/200),color='blue')
f.line(x,line(x,(2-gentoo_b)),line_width=2,legend_label='y=1.25x+{:.3f}'.format((400-gentoo_b)/200),color='green')
adelie_bs =  margin(adelie['Culmen Depth (mm)'],adelie['Body Mass (x200 g)'])
gentoo_bs =  margin(gentoo['Culmen Depth (mm)'],gentoo['Body Mass (x200 g)'])
for b in adelie_bs:
    f.line(x,line(x,(2-b)),line_width=1,color='blue',alpha=.1)
    
for b in gentoo_bs:
    f.line(x,line(x,(2-b)),line_width=1,color='green',alpha=.1)
show(f)
export_png(f,filename='../img/penguinhwy2.png') 

