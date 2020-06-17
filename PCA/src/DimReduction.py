from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.io import export_png, show
from bokeh.palettes import Category20
from sklearn.decomposition import PCA
import holoviews as hv
from holoviews.operation import gridmatrix
import numpy as np
import pandas as pd
import os

if not os.path.exists("./simulated_pca_data.csv"):
    print("Generating and saving new data")
    N = 15
    Profiles = np.random.uniform(0, 2, size=(5, N))
    U = np.random.choice([0, 1, 2, 3, 4], size=200, replace=True)
    d = np.zeros((200, N + 1))
    for i, x in enumerate(U):
        d[i, :-1] = np.random.normal(Profiles[x, :], 0.3)
    d[:, N] = U.astype(int)
    np.savetxt("./simulated_pca_data.csv", d, delimiter=",")
    d = d[:, :-1]
    pd.DataFrame(d,columns=[str(x) for x in range(N)]).to_csv('../data/simulated_pca_data.csv')
    pd.DataFrame(U).to_csv('../data/simulated_pca_data_labels.csv')
else:
    F = np.loadtxt("./simulated_pca_data.csv", delimiter=",")
    d = F[:, :-1]
    U = F[:, -1].astype(int)
    N = d.shape[1]
    print("Loaded array with {} features and {} samples".format(d.shape[0], d.shape[1]))

colors = ["blue", "red", "black", "orange", "green"]

P = PCA(n_components=N).fit(d)
S = P.components_
D = P.transform(d)

pc_plot = figure(
    x_range=(-4, 4),
    y_range=(-4, 4),
    title="Scatter plot of two most significant principal components",
    toolbar_location=None,
)
pc_plot.scatter(x=D[:, 0], y=D[:, 1])
export_png(pc_plot, filename="../img/pcadimred.png")

pc_plot_colored = figure(
    x_range=(-4, 4),
    y_range=(-4, 4),
    title="Scatter plot of two most significant principal components (colored by underlying group)",
    toolbar_location=None,
)
pc_plot_colored.scatter(x=D[:, 0], y=D[:, 1], color=[Category20[10][i] for i in U])
export_png(pc_plot_colored, filename="../img/pcadimred_colors.png")

eigenvalue_plot = figure(
    title="Eigenvalues of the covariance matrix", toolbar_location=None
)
eigenvalue_plot.line(x=range(1, N + 1), y=P.explained_variance_)
eigenvalue_plot.circle(x=range(1, N + 1), y=P.explained_variance_)
export_png(eigenvalue_plot, filename="../img/eigenvalues.png")

feature_plot = figure(
    x_range=(-4, 4),
    y_range=(-4, 4),
    title="Scatter plot of two of the original features",
    toolbar_location=None,
)
feature_plot.scatter(x=d[:, 0], y=d[:, 7])
export_png(feature_plot, filename="../img/features.png")


ds = hv.Dataset(pd.DataFrame(d, columns=[str(x) for x in range(N)]))
hv.extension("bokeh")
density_grid = gridmatrix(ds, chart_type=hv.Points).opts(
    height=1000, width=1000, toolbar=None
)
hv.save(density_grid, "../img/density.png")

with open("./simulated_pca_data_table.html", "w") as f:
    pd.DataFrame(
        d,
        columns=["f-{}".format(x) for x in range(15)],
        index=["s-{}".format(x) for x in range(200)],
    ).to_html(float_format=lambda x: "{:.2f}".format(x), max_rows=5, buf=f)


loading_plot = figure(
    x_range=(-4, 4),
    y_range=(-4, 4),
    title="Projection of feature axes (loadings) in PC space",
    toolbar_location=None,
)
loading_plot.scatter(x=D[:, 0], y=D[:, 1])
for i in range(15):
    loading_plot.line(
        x=[-100 * S[0, i], 100 * S[0, i]],
        y=[-100 * S[1, i], 100 * S[1, i]],
        color=Category20[20][i],
        line_width=1,
        legend_label=str(i),
    )

loading_plot.legend.location = "top_left"
loading_plot.legend.click_policy = "hide"
export_png(loading_plot, filename="../img/loading.png")

show(column(pc_plot, pc_plot_colored, feature_plot, eigenvalue_plot, loading_plot))
