import numpy as np
from collections import namedtuple

Vertex = namedtuple('Vertex','support vertex indices')


def _top(pts, indices, w, mu):
    p = pts[indices]
    k = int(np.ceil(1 / mu))
    z = np.dot(p, w.T)
    n_indices = np.argsort(-z)[:k]
    v = indices[n_indices]
    u = pts[v]
    vert = u[: (k - 1), :].sum(axis=0) * mu + (1 - (k - 1) * mu) * u[k - 1, :]
    return Vertex(support=u, vertex=vert, indices=v)


def _normal(x, y):
    z = y - x
    return np.array([-z[1], z[0]])


def _bump(pts, indices, x, y, mu):
    z = _normal(x.vertex, y.vertex)
    x_support = pts[x.indices]
    y_support = pts[y.indices]
    support = np.concatenate([x_support, y_support])
    p = pts[indices]
    A0 = indices[np.dot(p, z.T) >= np.min(np.dot(support, z.T))]
    return A0


def _RCH0(pts, indices, left, right, mu):
    h = _top(pts, indices, _normal(left.vertex, right.vertex), mu)
    if np.allclose(h.vertex, left.vertex) or np.allclose(h.vertex, right.vertex) or indices.shape[0]<2 :
        return [left, right]
    A = _bump(pts, indices,  left, h, mu)
    B = _bump(pts, indices, h, right, mu)
    x = _RCH0(pts, A, left, h, mu)
    y = _RCH0(pts, B, h, right, mu)
    return x[:-1] + y


def RCH(pts, mu):
    indices = np.array(range(pts.shape[0]))
    first = _top(pts, indices, np.array([0, 1]), mu)
    second = _top(pts, indices,  np.array([0, -1]), mu)
    L = _RCH0(pts, indices, first, second, mu)
    R = _RCH0(pts, indices, second, first, mu)
    return L[:-1] + R
