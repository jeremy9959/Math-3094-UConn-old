import holoviews as hv
from holoviews.operation import gridmatrix
import numpy as np
import pandas as pd

hv.extension('bokeh')
x = np.random.multivariate_normal([3,-1],[[4,3],[3,4]],size=50)
ds = hv.Dataset(pd.DataFrame(x,columns=['x','y']))
density_grid = gridmatrix(ds,chart_type=hv.Points).opts(height=600,width=600)

hv.save(density_grid,'../img/density2x2.png')
