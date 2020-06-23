from scipy.spatial import ConvexHull
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import export_png, show, output_notebook
import pandas as pd
import numpy as np

def line(x,b):
    return 250*x+b

def margin(x,y):
    return 250*x-y+400


penguins = '../../data/penguins/penguins_raw.csv'
df = pd.read_csv(penguins)
df['type'] = df['Species'].apply(lambda x: x.split()[0])
df['color'] = df['type'].map({'Adelie':'blue','Gentoo':'green','Chinstrap':'red'})



f = figure(toolbar_location=None)
f.xaxis.axis_label = 'Culmen Depth (mm)'
f.yaxis.axis_label = 'Body Mass (g)'
f.title.text = 'Penguin Features with Convex Hulls'
adelie = df[df['type']=='Adelie']
gentoo = df[df['type']=='Gentoo']
f.circle(x='Culmen Depth (mm)',y='Body Mass (g)',fill_color='color',legend_label = 'Adelie',source=ColumnDataSource(adelie))
f.circle(x='Culmen Depth (mm)',y='Body Mass (g)',fill_color='color',legend_label = 'Gentoo',source=ColumnDataSource(gentoo))

adelie_pts = adelie[['Culmen Depth (mm)', 'Body Mass (g)']].dropna().values
gentoo_pts = gentoo[['Culmen Depth (mm)', 'Body Mass (g)']].dropna().values

adelie_vertices = adelie_pts[ConvexHull(adelie_pts).vertices,:]
gentoo_vertices = gentoo_pts[ConvexHull(gentoo_pts).vertices,:]


for i in range(1,adelie_vertices.shape[0]):
    f.line(x=[adelie_vertices[i-1,0],adelie_vertices[i,0]],y=[adelie_vertices[i-1,1],adelie_vertices[i,1]])
f.line(x=[adelie_vertices[i,0],adelie_vertices[0,0]],y=[adelie_vertices[i,1],adelie_vertices[0,1]])


for i in range(1,gentoo_vertices.shape[0]):
    f.line(x=[gentoo_vertices[i-1,0],gentoo_vertices[i,0]],y=[gentoo_vertices[i-1,1],gentoo_vertices[i,1]],color='green')
f.line(x=[gentoo_vertices[i,0],gentoo_vertices[0,0]],y=[gentoo_vertices[i,1],gentoo_vertices[0,1]],color='green')   

export_png(f,filename='../img/penguinswithhulls.png')


