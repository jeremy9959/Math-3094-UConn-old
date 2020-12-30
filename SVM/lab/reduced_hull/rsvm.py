from bokeh.plotting import figure
from bokeh.io import show, output_notebook
import numpy as np


output_notebook()
pts = np.random.normal(0,1,size=(10,2))

def top(pts,w,mu):
    k = int(np.ceil(1/mu))
    z = np.dot(pts,w.T)
    u = pts[np.argsort(-z)[:k]]
    vertex = u[:(k-1),:].sum(axis=0)*mu+(1-(k-1)*mu)*u[k-1,:]
    return (u,vertex)

def normal(x,y):
    z = y-x
    return np.array([-z[1],z[0]])

def bump(pts, x,y,mu):
    z=normal(x[1],y[1])
    support = np.concatenate([x[0],y[0]])
    A=pts[np.dot(pts,z.T)>=np.min(np.dot(support,z.T))]
    return A


def RGH(pts,l,r,mu):
    h = top(pts,normal(l[1],r[1]),mu)
    if np.allclose(h[1],l[1]) or np.allclose(h[1],r[1]):
        return [l,r]
    A = bump(pts,l,h,mu)
    B = bump(pts,h,r,mu)
    x = RGH(A,l,h,mu)
    y = RGH(B,h,r,mu)
    return x+y




first = top(pts,np.array([0,1]),.4)
second = top(pts,np.array([0,-1]),.4)
z=normal(first[1],second[1])
right = top(pts,z,.4)
left=top(pts,-z,.4)


A  = bump(pts,first,right,.4)
new1 = top(A,normal(first[1],right[1]),.4)
B = bump(pts,right,second,.4)
new2 = top(B,normal(right[1],second[1]),.4)
f=figure(x_range=(-2,2),y_range=(-2,2))


f.scatter(x=pts[:,0],y=pts[:,1])

#for i,u in enumerate([first,left,second,right]):
#    f.circle(x=u[1][0],y=u[1][1],color=['orange','black','blue','green'][i],size=5)
#f.circle(x=A[:,0],y=A[:,1],color='red',size=5)
#f.circle(x=B[:,0],y=B[:,1],color='pink',size=5)

f.circle(x=new1[1][0],y=new1[1][1],color='black',size=10)
show(f)

