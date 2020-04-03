**Proposition:**  Let $H$ be a (proper) subspace of $\mathbf{R}^{n}$ and let $Y\not=0$ be a vector.  Then there is a unique
vector $\hat{Y}\not=0$ in $H$ such that

$$
\|Y-\hat{Y}\|^2 \le \|Y-X\|^2
$$

for all $X\in H$.  In other words, there is a uniquely defined "closest point to $Y$" in $H$.

**Proof:**  Choose a basis $X_1,\ldots, X_k$ for $H$.  A general element $X$ of $H$ is a linear combination

$$
X = \sum{i=1}^{k} m_i X_i.
$$

The geometric argument that we wish to make is that *the closest point to $Y$ in the plane $H$ is the point
$\hat{Y}$ where the vector $Y-\hat{Y}$ is perpendicular to $H$.*  See {@fig:perpendicular} for an illustration
of this idea.

So how do we find $\hat{Y$} with this property?  A vector $V$ will be perpendicular to the plane $H$ if it
is perpendicular to the general element $X$, which happens if and only if $V$ is perpendicular to all of the $X_i$.
For $V=Y-\hat{Y}$ this gives the conditions:

$$
(Y-\hat{Y})\cdot X_i = 0 \mathrm{\ for\ } i=1,\ldots k.
$$

