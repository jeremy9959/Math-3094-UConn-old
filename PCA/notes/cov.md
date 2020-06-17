<!-- Saved for later -->

### The Covariance Matrix

Given our discussion in the last paragraph, let's assume we begin with
data $Y$ and $X$ where $Y$ is an $N\times 1$ column vector and $X$ is
an $N\times k$ matrix whose columns are features.

Let $X_{0}$ and $Y_{0}$ be the associated *centered* data, so that $$
Y_{0} = Y -\mu_{Y}\left[\begin{matrix} 1 \\ 1 \\ \vdots \\
1\end{matrix}\right] $$ where $\mu_{Y} = \sum_{j=1}^{N} y_{j}$, and $$
X_0[:,i] = X[:,i] - \mu_{i}\left[\begin{matrix} 1 \\ 1 \\ \vdots \\
1\end{matrix}\right], $$ where $\mu_{i} = \sum_{j=1}^{N} x_{ji}$.

The $i,j$-entry of the matrix $k\times k$ matrix
$D_0=X_0^{\intercal}X_0$ is the dot product of the $i^{th}$ and
$j^{th}$ columns of $X_{0}$, explicitly:

$$\begin{aligned} (d_0)_{ij} & = X_0[:,i]\cdot X_0[:,j]\\ &=
\sum_{s=1}^{N} (x_0)_{si}(x_0)_{sj} \\ &= \sum_{s=1}^{N}
(x_{si}-\mu_{i})(x_{sj}-\mu_{j}) \end{aligned} $$

**Definition:** For $i=j$, the quantity $$ \sigma_{ii} = \frac{1}{N}
d_{ii} =\frac{1}{N}\sum_{s=1}^{N} (x_{si}-\mu_{i})^2 $$ is called the
*variance* of $x_{i}$.  For $i\not=j$, The quantity $$ \sigma_{ij} =
\frac{1}{N} d_{ij} =\frac{1}{N}\sum_{s=1}^{N} (x_{si}-\mu_{i})
(x_{sj}-\mu_{j}) $$ is called the *covariance* of $x_{i}$ and $x_{j}$.
The matrix $\Sigma=\frac{1}{N}D_0$ is called the *covariance matrix*
of the data $X$.

**Lemma:** We can simplify the expression for the variance:
$$\begin{aligned} \sigma_{ii} &= \frac{1}{N}\sum_{s=1}^{N}
(x_{si}-\mu_{i})^2\\ &=\frac{1}{N}\sum_{s=1}^{N}(
x_{si}^2-2x_{si}\mu_{i}+\mu_{i}^2)\\ &=\frac{1}{N}(\sum_{s=1}^{N}
x_{si}^2 -2\mu_{i}\sum_{s=1}^{N} x_{si}+\mu_{i}^2 \\
&=\frac{1}{N}(\sum_{s=1}^{N} x_{si}^2) -2\mu_{i}^2 + \mu_{i}^2 \\
&=\frac{1}{N}(\sum_{s=1}^{N} x_{si}^2) -\mu_{i}^2 .  \end{aligned} $$

The variance is a statistical measure of how "spread out" the values
of the feature $X[:,i]$ are around its mean.  A high variance means
the data is spread out; a small variance means it clusters around its
mean.

The covariance $X[:,i]$ and $X[:,j]$ measures how closely these two
features are correlated -- are they both large at the same
time, and both small at the same time?  

The covariance matrix $\Sigma$ summarizes these relationships among
the features.  Later, we will see that the covariance matrix $\Sigma$
captures a great deal of information about the data.  We will return
to this in later chapters.
