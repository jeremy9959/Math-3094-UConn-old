import numpy as np
from collections import namedtuple

Vertex = namedtuple('Vertex','support vertex indices')


def _top(pts, w, mu):
    k = int(np.ceil(1 / mu))
    z = np.dot(pts, w.T)
    indices = np.argsort(-z)[:k]
    u = pts[indices]
    
    vert = u[: (k - 1), :].sum(axis=0) * mu + (1 - (k - 1) * mu) * u[k - 1, :]
    return Vertex(support=u, vertex=vert, indices=indices)


def _normal(x, y):
    z = y - x
    return np.array([-z[1], z[0]])


def _bump(pts, x, y, mu):
    z = _normal(x.vertex, y.vertex)
    support = np.concatenate([x.support, y.support])
    A = pts[np.dot(pts, z.T) >= np.min(np.dot(support, z.T))]
    return A


def _RCH0(pts, left, right, mu):
    h = _top(pts, _normal(left.vertex, right.vertex), mu)
    if np.allclose(h.vertex, left.vertex) or np.allclose(h.vertex, right.vertex):
        return [left, right]
    A = _bump(pts, left, h, mu)
    B = _bump(pts, h, right, mu)
    x = _RCH0(A, left, h, mu)
    y = _RCH0(B, h, right, mu)
    return x[:-1] + y


def RCH(pts, mu):
    first = _top(pts, np.array([0, 1]), mu)
    second = _top(pts, np.array([0, -1]), mu)
    L = _RCH0(pts, first, second, mu)
    R = _RCH0(pts, second, first, mu)
    return L[:-1] + R
