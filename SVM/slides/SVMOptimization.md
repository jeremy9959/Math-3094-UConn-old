---
documentclass: extarticle
fontsize: 14pt
---
# Formulating the optimization problem

## The optimization problem

**Problem:** Given two linearly separable sets of points  $A^{\pm}\subset \mathbb{R}^{k}$:
$$
A^{+}=\{x_{1}^{+},\ldots, x^+_{n_{+}}\}
$$
and
$$
A^{-}=\{x_{1}^{-},\ldots, x^-_{n_{-}}\}
$$
Find points $p\in C(A^{+})$ and $q\in C(A^{-})$ so that
$$
\|p-q\|=\min_{{p'\in C(A^+)}\atop{q'\in C(A^-)}} \|p'-q'\|
$$

\newpage

## The optimization problem (continued)

As above, let our linearly separable sets be
$$
A^{+}=\{x_{1}^{+},\ldots, x^+_{n_{+}}\}
$$
and
$$
A^{-}=\{x_{1}^{-},\ldots, x^-_{n_{-}}\}
$$

**Problem 1:** Let $\lambda^{\pm}=(\lambda_{1}^{\pm},\ldots,\lambda^{\pm}_{n_{\pm}})$ be
two vectors of real numbers of length $n_{\pm}$ respectively. Define
$$
w(\lambda^{+},\lambda^{-}) = \sum_{i=1}^{n_{+}} \lambda^+_{i}x_{i}^+-\sum_{i=1}^{n_{-}} \lambda_{i}^{-}x_{i}^{-}.
$$
Find $\lambda^{\pm}$ such that $\|w(\lambda^{+},\lambda^{-})\|$ is minimal subject to the conditions
that all $\lambda_{i}^{\pm}\ge 0$ and $\sum_{i=1}^{n_{\pm}}\lambda_{i}^{\pm}=1$.

\newpage

## The optimization problem (continued)

Notice that:
\vfill
- $w(\lambda^{+},\lambda^{-})$ is a quadratic function in the $\lambda$'s with coefficients
coming from the dot products of the $x_{i}^{\pm}$.
\vfill
- The constraints are *inequalities* rather than equalities, so a direct application of Lagrange
multipliers as we learned in calculus won't work.
\vfill
- We will describe an iterative algorithm for solving this problem called Sequential Minimal
Optimization, due to John Platt and introduced in 1998.  
\vfill
- First, though, we reformulate the problem slightly.
\vfill
\newpage

## Reformulating the constrained optimization problem. 

**Problem 2:** Let 
$$
Q(\lambda^+,\lambda^-) = \|w(\lambda^+,\lambda^-)\|^2 - \sum_{i=1}^{n_{+}}\lambda_{i}^{+} -\sum_{i=1}^{n_{-}}\lambda_{i}^{-}.
$$
Let $\lambda^{\pm}$ be values that minimize $Q(\lambda^{+},\lambda^{-})$ where all $\lambda^{\pm}_{i}\ge 0$
and 
$$
\alpha = \sum_{i=1}^{n_{+}}\lambda_{i}^{+} = \sum_{i=1}^{n_{-}}\lambda_{i}^{-}.
$$
Then $\alpha\not=0$ at the $(\lambda^{+},\lambda^{-})$ that yield the minimum  and
$\tau^{\pm}=(1/\alpha)\lambda^{\pm}$  is a solution to optimization problem 1.

\newpage

## Equivalence of the reformulated problem

**Proof:**  

First let all $\lambda^{\pm}_{i}=0$ except $\lambda=\lambda^{\pm}_{1}$.  Then
$$
Q(\lambda^{+},\lambda^{-})=Q(\lambda)=\lambda^2\|x_{1}^{+}-x_{1}^{-}\|^2-2\lambda.
$$
This takes its minimum value at $\lambda=1/\|x_{1}^{+}-x_{1}^{-}\|^2$ and at that point
$$
Q(\lambda)=-\frac{1}{\|x_{1}^{+}-x_{1}^{-}\|^2}<0.
$$  
Therefore the minimum value is negative.  But if $\alpha=0$, then all $\lambda^{\pm}_{i}=0$,
so $Q=0$ at such a point.  Therefore $\alpha\not=0$ at the minimum value. 

To show the equivalence, we have $(\lambda^{+},\lambda^{-})$ solving problem 2 and $(\sigma^{+},\sigma^{-})$
solving problem 1; and finally we have $(\tau^{+},\tau^{-})=(1/\alpha)(\lambda^{+},\lambda^{-})$.

\vfill
1. Since $(\tau^{+},\tau^{-})$ satisfy the constraints of problem 2, we have:
$$Q(\lambda^{+},\lambda^{-}) = \|w(\lambda^{+},\lambda^{-})\|-2\alpha\le \|w(\tau^{+},\tau^{-})\|^2-2$$
\vfill
2.  Since $(\tau^{+},\tau^{-})$ satisfy the constraints of problem 1, we have 
$$
\|w(\sigma^{+},\sigma^{-})\|^2\le \|w(\tau^{+},\tau^{-})\|^2.
$$

\vfill\newpage

## Equivalence of optimization problems continued

3. From (2), we have 
$$
\|w(\alpha\sigma^{+},\alpha\sigma^{-})\|^2 
\le \alpha^2\|w(\tau^{+},\tau^{-})\|^2 
=\|w(\lambda^{+},\lambda^{-})\|^2
$$
\vfill
4.  Subtracting $2\alpha$ from both sides of this inequality yields
$$
\|w(\alpha\sigma^{+},\alpha\sigma^{-})\|^2-2\alpha\le Q(\lambda^{+},\lambda^{-}).
$$
Since $(\lambda^{+},\lambda^{-})$ minimize $Q(\lambda^{+},\lambda^{-})$, this inequality
must be an equality.  Therefore
$$
\alpha^2\|w(\sigma^{+},\sigma^{-})\|^2 = \alpha^2\|w(\tau^{+},\tau^{-})\|^2
$$
so $(\tau^{+},\tau^{-})$ also gives a minimal value for problem 1.
\vfill
\newpage
