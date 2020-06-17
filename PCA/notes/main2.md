--- 
pagetitle: The Spectral Theorem
colorlinks: true 
linkcolor: blue
link-citations: true 
csl: [../../resources/stat.csl]
bibliography: [../../references/references.bib]
reference-section-title: References 
---


# Eigenvalues and Eigenvectors of Real Symmetric Matrices (The Spectral Theorem)

In this section, we prove the four properties of eigenvalues and eigenvectors of real symmetric matrices
that we used in our discussion of Principal Components.  A key tool in the proof is the Gram-Schmidt
orthogonalization process.

## Gram-Schmidt {#sec:gsprocess}

**Proposition (Gram-Schmidt Process):** Let $w_{1},\ldots, w_{k}$ be a collection of linearly independent vectors
in $\mathbf{R}^{N}$ and let $W$ be the span of the $w_{i}$.  Let $u_{1} = w_{1}$ and let
$$
u_{i} = w_{i} - \sum_{j=1}^{i-1} \frac{w_{i}\cdot u_{j}}{u_{j}\cdot u_{j}}u_{j}
$$
for $i=2,\ldots, k$.  Then 

- The vectors $u_{i}$ are orthogonal: $u_{i}\cdot u_{j}=0$ unless $i=j$.
- The vectors $u_{i}$ span $W$.
- Each $u_{i}$ is orthogonal to the all of $w_{1},\ldots, w_{i-1}$. 
- The vectors $u'_{i} = u_{i}/\|u_{i}\|$ are orthonormal.

**Proof:** This is an inductive exercise, and we leave it to you to work out the details.

## The spectral theorem

**Theorem:** Let $D$ be a real symmetric $N\times N$ matrix.  Then:

1. All of the $N$ eigenvalues $\lambda_1\ge \lambda_2\ge \cdots \ge \lambda_{N}$ are real.  If 
$u^{\intercal}Du\ge 0$ for all $u\in\mathbf{R}^{N}$, then all eigenvalues $\lambda_{i}\ge 0$.
2. The matrix $D$ is diagonalizable -- that is, it has $N$ linearly independent eigenvectors.
3. If $v$ and $w$ are eigenvectors corresponding to eigenvalues $\lambda$ and $\lambda'$, with $\lambda\not=\lambda'$,
then $v$ and $w$ are orthogonal: $v\cdot w=0$.
4. There is an orthonormal basis $u_{1},\ldots, u_{N}$ of \mathbf{R}^{N}$ made up of eigenvectors for the eigenvalues
$\lambda_{i}$. 
5. Let $\Lambda$ be the diagonal matrix with entries $\lambda_{1},\ldots, \lambda_{N}$ and let $P$ be the matrix
whose columns are made up of the eigenvectors $u_{i}$.  Then $D=P\Lambda P^{\intercal}$.

**Proof:** Start with $1$. 
Suppose that $\lambda$ is an eigenvalue of
$D$.  Let $u$ be a corresponding nonzero eigenvector.  Then
$Du=\lambda u$ and $D\overline{u}=\overline{\lambda}\overline{u}$, where $\overline{u}$ is the
vector whose entries are the conjugates of the entries of $u$ (and $\overline{D}=D$ since $D$ is real).
Now we have
$$
\overline{u}^{\intercal}Du = \lambda \overline{u}\cdot u = \lambda\|u\|^2
$$
and
$$
u^{\intercal}D\overline{u} = \overline{\lambda}u\cdot \overline{u} = \overline{\lambda}\|u\|^2.
$$
But the left hand side of both of these equations are the same (take the transpose and use the symmetry of $D$)
so we must have $\lambda\|u\|^2 = \overline{\lambda}\|u\|^2$ so $\lambda=\overline{\lambda}$, meaning $\lambda$
is real.  

If we have the additional property that $u^{\intercal}Du\ge 0$ for all $u$, then in particular
$u_{i}^{\intercal}Du_{i} = \lambda\|u\|^2\ge 0$, and since $\|u\|^2> 0$ we must have $\lambda\ge 0$.


Property $2$ is in some ways the most critical fact. We know from the
general theory of the characteristic polynomial, and the fundamental
theorem of algebra, that $D$ has $N$ complex eigenvalues, although
some may be repeated.  However, it may not be the case that $D$ has $N$ linearly
independent eigenvectors -- it may not be *diagonalizable*.  So we will establish that now.

A one-by-one matrix is automatically symmetric and diagonalizable.  In the $N$-dimensional case, 
we know, at least, that $D$ has at least one eigenvector, and real one at that by part $1$,
and this gives us a place to begin an inductive argument.  

Let $v_{N}\not=0$ be an eigenvector with eigenvalue $\lambda$ and normalized so that $\|v_{N}\|^2=1$,  
and extend this to a basis $v_{1},\ldots v_{N}$ of $\mathbf{R}^{N}$.
Apply the Gram-Schmidt process  to construct an orthonormal basis of $\mathbf{R}^{N}$ 
$u_{1},\ldots, u_{N}$ so that $u_{N}=v_{N}$.  

Any vector $v\in\mathbf{R}^{N}$ is a linear combination
$$
v = \sum_{i=1}^{N} a_{i}u_{i}
$$
and, since the $u_{i}$ are orthonormal, the coefficients can be calculated as $a_{i}=(u_{i}\cdot v)$.

Using this, we can find the matrix $D'$ of the linear map defined by our original matrix $D$
in this new basis.  By definition, if $d'_{ij}$ are the entries of $D'$, then

$$
Du_{i} = \sum_{j=1}^{N} d'_{ij} u_{j}
$$

and so 

$$
d'_{ij} = u_{j}\cdot Du_{i} = u_{j}^{\intercal}Du_{i}.
$$

Since $D$ is symmetric, $u_{j}^{\intercal}Du_{i} =u_{i}^{\intercal}Du_{j}$ and so $d'_{ij}=d'_{ji}$.
In other words, the matrix $D'$ is still symmetric.  Furthermore,

$$
d'_{Ni} = u_{i}\cdot Du_{N} = u_{i}\cdot \lambda u_{N} = \lambda (u_{i}\cdot u_{N})
$$

since $u_{N}=v_{N}$.  Since the $u_{i}$ are an orthonormal basis, we see that
$d'_{iN}=0$ unless $i=N$, and $d'_{NN}=\lambda$.

In other words, the matrix $D'$ has a block form:
$$
D' = \left(\begin{matrix} * & * & \cdots &*  & 0 \\ \vdots & \vdots & \ddots   & \vdots & \vdots \\
* & * & \cdots &*  & 0 \\
0 & 0 & \cdots &0 &\lambda \end{matrix}\right)
$$
and the block denoted by $*$'s is symmetric.  If we call that block $D_{*}$, 
the inductive hypothesis tells us that the symmetric matrix $D_{*}$ is diagonalizable, so it has a basis of
eigenvectors $u'_{1},\ldots, u'_{N-1}$ with eigenvalues $\lambda_{1},\ldots, \lambda_{N-1}$; this gives
us a basis for the subspace of $\mathbf{R}^{N}$ spanned by $u_{1},\ldots, u_{N-1}$ which, together
with $u_{N}$ gives us a basis of $\mathbf{R}^{N}$ consisting of eigenvectors of $D$.


This finishes the proof of Property $2$.

For property $3$, compute 
$$
v^{\intercal}Dw = \lambda'(v\cdot w)=w^{\intercal}Dv = \lambda (w\cdot v).
$$
Since $\lambda\not=\lambda'$, we must have $v\cdot w=0$.

For property $4$, if the eigenvalues are all distinct, this is a consequence of property $2$ -- you have
$N$ eigenvectors, scaled to length $1$, for different eigenvalues, and by $2$ they are orthogonal.  So the
only complication is the case where some eigenvalues are repeated.  If $\lambda$ occurs $r$ times, then
you have $r$ linearly independent vectors $u_{1},\ldots, u_{r}$ that span the $\lambda$ eigenspace.
The Gram-Schmidt process allows you to construct an orthonormal set that spans this eigenspace, and while
this orthonormal set isn't unique, any one of them will do.

For property $5$, let $e_{i}$ be the column vector that is zero except for a $1$ in position $i$. 
The product $e_{j}^{\intercal}De_{i}=d_{ij}$.  Let's write $e_{i}$ and $e_{j}$ in terms of the orthonormal
basis $u_{1},\ldots u_{N}$:
$$
e_{i} = \sum_{k=1}^{N} (e_{i}\cdot u_{k})u_k \hbox{ and } e_{j} = \sum_{k=1}^{N}(e_{j}\cdot u_{k})u_{k}.
$$
Using this expansion, we compute $e_{j}^{\intercal}De_{i}$ in a more complicated way:
$$
e_{j}^{\intercal}De_{i} = \sum_{r=1}^{N}\sum_{s=1}^{N} (e_{j}\cdot u_{r})(e_{i}\cdot u_{s})(u_{r}^{\intercal}Du_{s}).
$$
But $u_{r}^{\intercal}Du_{s}=\lambda_{s}(u_{r}\cdot u_{s})=0$ unless $r=s$, in which case it equals $\lambda_{r}$, so
$$
e_{j}^{\intercal}De_{i} = \sum_{r=1}^{N} \lambda_{r}(e_{j}\cdot u_{r})(e_{i}\cdot u_{r}).
$$
On the other hand,
$$
P^{\intercal}e_{i} = \left[\begin{matrix} (e_{i}\cdot u_{1})\\ (e_{i}\cdot u_{2})\\ \vdots \\(e_{i}\cdot u_{N})\end{matrix}\right]
$$
and 
$$
\Lambda P^{\intercal}e_{i} = \left[\begin{matrix} \lambda_{1}(e_{i}\cdot u_{i})\\ \lambda_{2}(e_{i}\cdot u_{2})\\ \vdots \\ \lambda_{N}(e_{i}\cdot u_{N})\end{matrix}\right]
$$
Therefore the $i,j$ entry of $P\Lambda P^{\intercal}$ is
$$
(e_{j}^{\intercal}P)\Lambda (P^{\intercal}e_{j}) = \sum_{r=1}^{N} \lambda_{r}(e_{i}\cdot u_{r})(e_{j}\cdot u_{r}) = d_{ij}
$$
so the two matrices $D$ and $P\Lambda P^{\intercal}$ are in fact equal.

Exercises

1. Prove the Gram-Schmidt Process has the claimed properties in +@sec:gsprocess.



# PCA for dimension reduction
# "loadings"
