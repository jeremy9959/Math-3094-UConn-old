from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import export_png, show
import pandas as pd
import numpy as np
from scipy.spatial import ConvexHull
from itertools import product

def line(x,b):
    return 250*x+b


def margin(x,y):
    return 250*x-y+400


def smo(ap, am, tol=.01):

    lp = np.ones(ap.shape[0])/ap.shape[0]
    lm = np.ones(am.shape[0])/am.shape[0]
    p = lp @ ap
    q = lm @ am
    alpha = lp.sum()
    ps = np.array(p/alpha).reshape(1,2)
    qs = np.array(q/alpha).reshape(1,2)
    rounds = 0
    while(True):
        maxdelta = 0
        pairs = [(i,j) for i,j in product(range(ap.shape[0]),range(am.shape[0]))]
        np.random.shuffle(pairs)
        for i,j in pairs:
            M = np.max([-lp[i],-lm[j]])
            delta = (1-np.sum((p-q)*(ap[i,:]-am[j,:])))/np.sum(np.square(ap[i,:]-am[j,:]))
            dstar=np.max([delta, M])
            lp[i] = lp[i]+dstar
            lm[j] = lm[j]+dstar
            alpha = alpha+dstar
            p= lp @ ap
            q= lm @ am
            maxdelta = np.max([maxdelta,np.abs(dstar)])
        if np.abs(maxdelta)<tol:
            break
        oldlp = lp
        oldlm = lm
        ps = np.append(ps,(p/alpha).reshape(1,2),axis=0)
        qs = np.append(qs,(q/alpha).reshape(1,2),axis=0)
        rounds+=1
            
    return lp/alpha, lm/alpha,ps,qs


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

adelie_pts = adelie[['Culmen Depth (mm)', 'Body Mass (x200 g)']].dropna().values
gentoo_pts = gentoo[['Culmen Depth (mm)', 'Body Mass (x200 g)']].dropna().values

adelie_vertices = adelie_pts[ConvexHull(adelie_pts).vertices,:]
gentoo_vertices = gentoo_pts[ConvexHull(gentoo_pts).vertices,:]


for i in range(1,adelie_vertices.shape[0]):
    f.line(x=[adelie_vertices[i-1,0],adelie_vertices[i,0]],y=[adelie_vertices[i-1,1],adelie_vertices[i,1]])
f.line(x=[adelie_vertices[i,0],adelie_vertices[0,0]],y=[adelie_vertices[i,1],adelie_vertices[0,1]])   


for i in range(1,gentoo_vertices.shape[0]):
    f.line(x=[gentoo_vertices[i-1,0],gentoo_vertices[i,0]],y=[gentoo_vertices[i-1,1],gentoo_vertices[i,1]],color='green')
f.line(x=[gentoo_vertices[i,0],gentoo_vertices[0,0]],y=[gentoo_vertices[i,1],gentoo_vertices[0,1]],color='green')  

lp,lm,ps, qs = smo(adelie_pts,gentoo_pts,tol=.01)
pstar = lp @ adelie_pts
qstar = lm @ gentoo_pts

f.asterisk(x=pstar[0],y=pstar[1],size=10,color='black')
f.asterisk(x=qstar[0],y=qstar[1],size=10,color='black')
f.line(x=[pstar[0],qstar[0]],y=[pstar[1],qstar[1]],color='black')

w = pstar-qstar
b = (np.sum(np.square(pstar))-np.sum(np.square(qstar)))/2
x=np.linspace(10,25,100)
y = (b-w[0]*x)/w[1]
f.line(x=x,y=y,color='red',line_width=2,legend_label='y={:.2f}x-{:.2f}'.format(-w[0]/w[1],-b/w[1]))

export_png(f,filename='../img/solution.png')
show(f)
