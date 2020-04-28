from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.io import export_png, show
from bokeh.palettes import Category20
from sklearn.decomposition import PCA
import numpy as np

N = 15

Profiles = np.random.uniform(0, 2, size=(5, N))
U = np.random.choice([0, 1, 2, 3, 4], size=200, replace=True)
d = np.zeros((200, N))
for i, x in enumerate(U):
    d[i, :] = np.random.normal(Profiles[x, :], 0.3)

colors = ["blue", "red", "black", "orange", "green"]

P = PCA(n_components=N).fit(d)
S = P.components_
D = P.transform(d)

pc_plot = figure(
    x_range=(-4, 4),
    y_range=(-4, 4),
    title="Scatter plot of two most significant principal components",
    toolbar_location = None
)
pc_plot.scatter(x=D[:, 0], y=D[:, 1])
export_png(pc_plot, filename='../img/pcadimred.png')

pc_plot_colored = figure(
    x_range=(-4, 4),
    y_range=(-4, 4),
    title="Scatter plot of two most significant principal components (colored by underlying group)",
    toolbar_location = None
)
pc_plot_colored.scatter(x=D[:, 0], y=D[:, 1],color = [Category20[10][i] for i in U])
export_png(pc_plot_colored, filename='../img/pcadimred_colors.png')

eigenvalue_plot = figure(title='Eigenvalues of the covariance matrix', toolbar_location=None)
eigenvalue_plot.line(x=range(1,N+1),y=P.explained_variance_)
eigenvalue_plot.circle(x=range(1,N+1),y=P.explained_variance_)
export_png(eigenvalue_plot,filename='../img/eigenvalues.png')

feature_plot = figure(
    x_range=(-4, 4),
    y_range=(-4, 4),
    title="Scatter plot of two of the original features",
    toolbar_location = None
)
feature_plot.scatter(x=d[:, 0], y=d[:, 7])
export_png(feature_plot,filename='../img/features.png')

show(column(pc_plot, pc_plot_colored, feature_plot, eigenvalue_plot))

