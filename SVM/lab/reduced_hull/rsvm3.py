import numpy as np
from collections import namedtuple
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, TapTool
from bokeh.models.callbacks import CustomJS

Vertex = namedtuple("Vertex", "vertex support")

callback_code = """
    var selected = data.selected.indices[0];
    var support = info[selected][1] ;
    var special = info[selected][1][info[selected][1].length-1] ;
    for(let i=0; i<pts.data['color'].length;i++){
        pts.data['color'][i]=support.includes(i)?'green':'blue';
        pts.data['size'][i]=support.includes(i)?10:4 ;
    }
    pts.data['color'][special]='#33ee00' ;
    pts.change.emit() ;
"""


class RCH:
    def __init__(self, pts, mu):
        self.pts = pts
        self.indices = np.array(range(pts.shape[0]))
        self.mu = mu
        first = self._top(self.pts, self.indices, np.array([0, 1]), self.mu)
        second = self._top(self.pts, self.indices, np.array([0, -1]), self.mu)
        L = self._RCH0(self.pts, self.indices, first, second, self.mu)
        R = self._RCH0(self.pts, self.indices, second, first, self.mu)
        self.rch = L[:-1] + R
        self.vertices = np.stack([x.vertex for x in self.rch])
        self.support = np.stack([pts[x.support] for x in self.rch])
        self.fig = self._fig()

    def _top(self, pts, indices, w, mu):
        p = pts[indices]
        k = int(np.ceil(1 / mu))
        z = np.dot(p, w.T)
        n_indices = np.argsort(-z)[:k]
        v = indices[n_indices]
        u = pts[v]
        vert = u[: (k - 1), :].sum(axis=0) * mu + (1 - (k - 1) * mu) * u[k - 1, :]
        return Vertex(vertex=vert, support=v)

    def _normal(self, x, y):
        z = y - x
        return np.array([-z[1], z[0]])

    def _bump(self, pts, indices, x, y, mu):
        z = self._normal(x.vertex, y.vertex)
        x_support = pts[x.support]
        y_support = pts[y.support]
        support = np.concatenate([x_support, y_support])
        p = pts[indices]
        A0 = indices[np.dot(p, z.T) >= np.min(np.dot(support, z.T))]
        return A0

    def _RCH0(self, pts, indices, left, right, mu):
        h = self._top(pts, indices, self._normal(left.vertex, right.vertex), mu)
        if (
            np.allclose(h.vertex, left.vertex)
            or np.allclose(h.vertex, right.vertex)
            or indices.shape[0] < 2
        ):
            return [left, right]
        A = self._bump(pts, indices, left, h, mu)
        B = self._bump(pts, indices, h, right, mu)
        x = self._RCH0(pts, A, left, h, mu)
        y = self._RCH0(pts, B, h, right, mu)
        return x[:-1] + y

    def _fig(self):
        f = figure(
            aspect_ratio=1.0, title="Reduced Convex Hull with \u03BC={:.2f}".format(self.mu)
        )
        N = self.pts.shape[0]
        data = ColumnDataSource(
            {"x": self.vertices[:-1, 0], "y": self.vertices[:-1, 1]}
        )
        data2 = ColumnDataSource({"x": self.vertices[:, 0], "y": self.vertices[:, 1]})
        points = ColumnDataSource(
            {
                "x": self.pts[:, 0],
                "y": self.pts[:, 1],
                "color": ["blue" for i in range(N)],
                "size": [4 for i in range(N)],
            }
        )
        callback = CustomJS(
            args=dict(data=data, info=self.rch, pts=points), code=callback_code
        )
        f.scatter(x="x", y="y", color="color", source=points, size="size")
        f.line(x="x", y="y", color="red", source=data2)
        vertices = f.circle(
            x="x",
            y="y",
            selection_color="red",
            color="red",
            nonselection_fill_alpha=0.5,
            size=10,
            source=data,
        )
        f.add_tools(TapTool(callback=callback, renderers=[vertices]))
        return f
